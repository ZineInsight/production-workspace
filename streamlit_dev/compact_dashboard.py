"""
📊 DASHBOARD COMPACT - VERSION ONGLETS
====================================
Alternative avec navigation par onglets pour comparaison
Otmane Boulahia - Data Engineer Portfolio
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from itertools import combinations
from collections import Counter

# Configuration
st.set_page_config(
    page_title="📊 Compact Analytics | Otmane Portfolio",
    page_icon="📊",
    layout="wide"
)

@st.cache_data
def load_data():
    """Charge les données enrichies"""
    sales_df = pd.read_csv('data/cleaned_datasets/sales_cleaned.csv')
    products_df = pd.read_csv('data/cleaned_datasets/products_cleaned.csv')

    sales_df['date_date'] = pd.to_datetime(sales_df['date_date'])

    # Joindre avec produits pour calcul marge
    enriched = sales_df.merge(products_df, left_on='pdt_id', right_on='products_id', how='left')
    enriched['margin'] = enriched['revenue'] - (enriched['purchSE_PRICE'] * enriched['quantity'])
    enriched['margin_rate'] = (enriched['margin'] / enriched['revenue'] * 100).fillna(0)

    return enriched

def main():
    # Header
    st.title("📊 Advanced Analytics Portfolio")
    st.markdown("**Otmane Boulahia** - Data Engineer | Analytics Avancées & Multi-Pages")

    # Charger données
    df = load_data()

    # Navigation par onglets
    tab1, tab2, tab3, tab4 = st.tabs(["📈 Overview", "🏆 Top Produits", "📊 Analyse ABC", "🔍 Market Basket"])

    with tab1:
        st.header("📈 Vue d'ensemble")

        # KPIs
        col1, col2, col3, col4 = st.columns(4)

        total_revenue = df['revenue'].sum()
        total_orders = df['orders_id'].nunique()
        avg_basket = total_revenue / total_orders
        margin_total = df['margin'].sum()
        margin_rate = margin_total / total_revenue * 100

        col1.metric("💰 Revenue", f"{total_revenue:,.0f}€")
        col2.metric("🛒 Commandes", f"{total_orders:,}")
        col3.metric("📦 Panier Moyen", f"{avg_basket:.2f}€")
        col4.metric("💹 Marge", f"{margin_rate:.1f}%")

        # Graphiques temporels
        col1, col2 = st.columns(2)

        with col1:
            monthly = df.groupby(df['date_date'].dt.to_period('M')).agg({
                'revenue': 'sum',
                'margin': 'sum'
            }).reset_index()
            monthly['date'] = monthly['date_date'].astype(str)
            monthly['margin_rate'] = monthly['margin'] / monthly['revenue'] * 100

            fig1 = go.Figure()
            fig1.add_bar(x=monthly['date'], y=monthly['revenue'], name='Revenue', yaxis='y')
            fig1.add_scatter(x=monthly['date'], y=monthly['margin_rate'],
                           name='Marge %', yaxis='y2', mode='lines+markers')
            fig1.update_layout(
                title="Revenue & Marge Mensuelle",
                yaxis=dict(title="Revenue €", side='left'),
                yaxis2=dict(title="Marge %", side='right', overlaying='y')
            )
            st.plotly_chart(fig1, use_container_width=True)

        with col2:
            weekly = df.groupby(df['date_date'].dt.day_name())['revenue'].sum().reindex([
                'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
            ])
            fig2 = px.bar(x=['Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam', 'Dim'],
                         y=weekly.values, title="Saisonnalité Hebdomadaire")
            st.plotly_chart(fig2, use_container_width=True)

    with tab2:
        st.header("🏆 Analyse Top & Flop Produits")

        products_metrics = df.groupby('pdt_id').agg({
            'revenue': 'sum',
            'quantity': 'sum',
            'margin': 'sum',
            'orders_id': 'nunique'
        }).round(2)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("🔥 TOP 15 Produits")
            top_products = products_metrics.sort_values('revenue', ascending=False).head(15)
            st.dataframe(top_products)

            # Évolution du top produit
            top_id = top_products.index[0]
            evolution = df[df['pdt_id'] == top_id].groupby(df['date_date'].dt.to_period('M'))['revenue'].sum().reset_index()
            evolution['month'] = evolution['date_date'].astype(str)

            fig = px.line(evolution, x='month', y='revenue',
                         title=f"Évolution Produit #{top_id} (Top)", markers=True)
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.subheader("❄️ FLOP 15 Produits")
            flop_products = products_metrics[products_metrics['revenue'] > 0].sort_values('revenue').head(15)
            st.dataframe(flop_products)

            # Distribution des marges
            fig_margin = px.histogram(df, x='margin_rate', title="Distribution Taux de Marge",
                                    nbins=25, color_discrete_sequence=['orange'])
            st.plotly_chart(fig_margin, use_container_width=True)

    with tab3:
        st.header("📊 Analyse ABC - Courbe de Concentration")

        # Calculer ABC
        abc_df = products_metrics.sort_values('revenue', ascending=False).reset_index()
        abc_df['revenue_pct'] = abc_df['revenue'] / abc_df['revenue'].sum() * 100
        abc_df['cumulative_pct'] = abc_df['revenue_pct'].cumsum()

        # Classifier
        def classify_abc(cum_pct):
            if cum_pct <= 80: return 'A (80%)'
            elif cum_pct <= 95: return 'B (15%)'
            else: return 'C (5%)'

        abc_df['classe'] = abc_df['cumulative_pct'].apply(classify_abc)

        col1, col2 = st.columns([2, 1])

        with col1:
            # Courbe ABC
            fig_abc = go.Figure()
            fig_abc.add_scatter(x=list(range(1, len(abc_df) + 1)), y=abc_df['cumulative_pct'],
                              mode='lines', name='% Cumulé', line=dict(color='blue', width=3))
            fig_abc.add_hline(y=80, line_dash="dash", line_color="red", annotation_text="80% - Classe A")
            fig_abc.add_hline(y=95, line_dash="dash", line_color="orange", annotation_text="95% - Classe B")
            fig_abc.update_layout(title="Courbe ABC des Ventes",
                                xaxis_title="Rang Produits", yaxis_title="% Cumulé Revenue")
            st.plotly_chart(fig_abc, use_container_width=True)

        with col2:
            # Répartition ABC
            abc_counts = abc_df['classe'].value_counts()
            fig_pie = px.pie(values=abc_counts.values, names=abc_counts.index,
                           title="Répartition ABC",
                           color_discrete_sequence=['#ff6b6b', '#feca57', '#48dbfb'])
            st.plotly_chart(fig_pie, use_container_width=True)

            st.subheader("📈 Statistiques ABC")
            for classe, count in abc_counts.items():
                pct = count / len(abc_df) * 100
                st.write(f"**{classe}**: {count} produits ({pct:.1f}%)")

    with tab4:
        st.header("🔍 Market Basket Analysis")

        # Calculer associations
        baskets = df.groupby('orders_id')['pdt_id'].apply(list)
        multi_baskets = baskets[baskets.apply(len) > 1]

        if len(multi_baskets) == 0:
            st.warning("Pas assez de paniers multi-produits")
            return

        # Associations de produits
        associations = []
        for products in multi_baskets:
            for combo in combinations(products, 2):
                associations.append(tuple(sorted(combo)))

        assoc_counts = Counter(associations)
        top_associations = pd.DataFrame([
            {'Produit_1': assoc[0], 'Produit_2': assoc[1], 'Fréquence': count}
            for assoc, count in assoc_counts.most_common(20)
        ])

        col1, col2 = st.columns([2, 1])

        with col1:
            st.subheader("🛒 Top 20 Associations Produits")
            st.dataframe(top_associations, use_container_width=True)

            # Graphique associations
            if not top_associations.empty:
                top_10 = top_associations.head(10)
                top_10['combo'] = top_10['Produit_1'].astype(str) + ' + ' + top_10['Produit_2'].astype(str)
                fig = px.bar(top_10, x='Fréquence', y='combo', orientation='h',
                           title="Associations les Plus Fréquentes")
                fig.update_layout(yaxis={'categoryorder': 'total ascending'})
                st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.subheader("📊 Stats Paniers")

            basket_sizes = baskets.apply(len)
            multi_count = (basket_sizes > 1).sum()
            avg_size = basket_sizes.mean()
            max_size = basket_sizes.max()

            st.metric("🛒 Paniers Multi-produits", f"{multi_count:,}")
            st.metric("📦 Taille Moyenne", f"{avg_size:.1f} items")
            st.metric("🔝 Plus Gros Panier", f"{max_size} items")

            # Distribution tailles
            fig_sizes = px.histogram(basket_sizes, title="Distribution Tailles Paniers",
                                   labels={'x': 'Items', 'y': 'Fréquence'}, nbins=10)
            st.plotly_chart(fig_sizes, use_container_width=True)

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center;'>
        <p>🚀 <strong>Version Compacte - Navigation Onglets</strong> |
        Otmane Boulahia Data Engineer |
        Comparaison avec Version Multi-Pages</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
