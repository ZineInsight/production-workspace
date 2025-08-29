"""
📊 PORTFOLIO ANALYTICS DASHBOARD - VERSION AVANCÉE
=================================================
Dashboard Streamlit multi-pages avec analyses produits avancées
Otmane Boulahia - Data Engineer - zineinsight.com

Features:
- 🏆 Analyses produits Top/Flop avec évolution
- 💰 Analyse de marge (revenue vs coût)
- 📊 Courbe ABC et concentration des ventes
- 🔍 Market Basket Analysis
- 🎨 Interface multi-pages moderne
- 🌓 Thème sombre/clair
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np
from itertools import combinations
from collections import Counter
import plotly.figure_factory as ff

# Configuration Streamlit
st.set_page_config(
    page_title="📊 Advanced Analytics | Otmane Data Engineer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Variables globales
if 'theme' not in st.session_state:
    st.session_state.theme = 'light'

def toggle_theme():
    st.session_state.theme = 'dark' if st.session_state.theme == 'light' else 'light'

# CSS dynamique selon le thème
def get_theme_css():
    if st.session_state.theme == 'dark':
        return """
        <style>
            .main-header {
                font-size: 2.5rem;
                font-weight: bold;
                text-align: center;
                margin-bottom: 2rem;
                background: linear-gradient(90deg, #64b5f6, #81c784);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            .metric-card {
                background: #2b2b2b;
                padding: 1rem;
                border-radius: 10px;
                border: 1px solid #555;
                box-shadow: 0 2px 8px rgba(0,0,0,0.3);
                color: white;
            }
            .stTabs [data-baseweb="tab"] {
                background-color: #2b2b2b;
                color: white;
            }
        </style>
        """
    else:
        return """
        <style>
            .main-header {
                font-size: 2.5rem;
                font-weight: bold;
                text-align: center;
                margin-bottom: 2rem;
                background: linear-gradient(90deg, #1f77b4, #ff7f0e);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            .metric-card {
                background: white;
                padding: 1rem;
                border-radius: 10px;
                border: 1px solid #ddd;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            .page-nav {
                background: #f8f9fa;
                padding: 1rem;
                border-radius: 10px;
                margin-bottom: 1rem;
            }
        </style>
        """

@st.cache_data
def load_and_process_data():
    """Charge et enrichit les données avec analyses avancées"""
    try:
        # Charger les datasets nettoyés
        sales_df = pd.read_csv('data/cleaned_datasets/sales_cleaned.csv')
        products_df = pd.read_csv('data/cleaned_datasets/products_cleaned.csv')

        # Convertir les dates
        sales_df['date_date'] = pd.to_datetime(sales_df['date_date'])

        # Joindre avec les produits
        sales_enriched = sales_df.merge(
            products_df,
            left_on='pdt_id',
            right_on='products_id',
            how='left'
        )

        # Calculer les métriques avancées
        sales_enriched['margin'] = sales_enriched['revenue'] - (sales_enriched['purchSE_PRICE'] * sales_enriched['quantity'])
        sales_enriched['margin_rate'] = (sales_enriched['margin'] / sales_enriched['revenue'] * 100).fillna(0)

        # Analyser les top produits avec évolution temporelle
        products_evolution = []
        for month in sales_enriched['date_date'].dt.to_period('M').unique():
            month_data = sales_enriched[sales_enriched['date_date'].dt.to_period('M') == month]
            monthly_products = month_data.groupby('pdt_id').agg({
                'revenue': 'sum',
                'quantity': 'sum',
                'margin': 'sum',
                'orders_id': 'nunique'
            }).reset_index()
            monthly_products['month'] = str(month)
            products_evolution.append(monthly_products)

        if products_evolution:
            products_evolution_df = pd.concat(products_evolution, ignore_index=True)
        else:
            products_evolution_df = pd.DataFrame()

        return sales_enriched, products_df, products_evolution_df

    except Exception as e:
        st.error(f"Erreur chargement données : {e}")
        return None, None, None

def calculate_abc_analysis(sales_enriched):
    """Calcule l'analyse ABC des produits"""
    product_metrics = sales_enriched.groupby('pdt_id').agg({
        'revenue': 'sum',
        'quantity': 'sum',
        'orders_id': 'nunique'
    }).sort_values('revenue', ascending=False).reset_index()

    # Calculer les pourcentages cumulés
    product_metrics['revenue_pct'] = product_metrics['revenue'] / product_metrics['revenue'].sum() * 100
    product_metrics['cumulative_pct'] = product_metrics['revenue_pct'].cumsum()

    # Classification ABC
    def classify_abc(cumulative_pct):
        if cumulative_pct <= 80:
            return 'A (80%)'
        elif cumulative_pct <= 95:
            return 'B (15%)'
        else:
            return 'C (5%)'

    product_metrics['abc_class'] = product_metrics['cumulative_pct'].apply(classify_abc)

    return product_metrics

def perform_market_basket_analysis(sales_enriched):
    """Analyse du panier d'achat"""
    # Grouper par commande
    baskets = sales_enriched.groupby('orders_id')['pdt_id'].apply(list).reset_index()
    baskets = baskets[baskets['pdt_id'].apply(len) > 1]  # Seulement paniers multi-produits

    if len(baskets) == 0:
        return pd.DataFrame()

    # Calculer les associations de produits
    associations = []
    for _, row in baskets.iterrows():
        products = row['pdt_id']
        for combo in combinations(products, 2):
            associations.append(sorted(combo))

    # Compter les associations
    association_counts = Counter(tuple(assoc) for assoc in associations)

    # Convertir en DataFrame
    market_basket_df = pd.DataFrame([
        {'product_1': assoc[0], 'product_2': assoc[1], 'frequency': count}
        for assoc, count in association_counts.most_common(20)
    ])

    return market_basket_df

def page_overview(sales_enriched):
    """Page d'aperçu général"""
    st.markdown('<h2 class="main-header">📊 Vue d\'ensemble Business</h2>', unsafe_allow_html=True)

    # KPIs principaux
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        total_revenue = sales_enriched['revenue'].sum()
        st.metric("💰 Chiffre d'Affaires", f"{total_revenue:,.0f}€")

    with col2:
        total_orders = sales_enriched['orders_id'].nunique()
        st.metric("🛒 Commandes", f"{total_orders:,}")

    with col3:
        avg_basket = total_revenue / total_orders if total_orders > 0 else 0
        st.metric("📦 Panier Moyen", f"{avg_basket:.2f}€")

    with col4:
        total_margin = sales_enriched['margin'].sum()
        margin_rate = (total_margin / total_revenue * 100) if total_revenue > 0 else 0
        st.metric("💹 Marge Globale", f"{margin_rate:.1f}%", f"{total_margin:,.0f}€")

    # Graphiques temporels
    st.subheader("📈 Évolution Mensuelle")

    monthly_metrics = sales_enriched.groupby(sales_enriched['date_date'].dt.to_period('M')).agg({
        'revenue': 'sum',
        'margin': 'sum',
        'orders_id': 'nunique'
    }).reset_index()
    monthly_metrics['date_date'] = monthly_metrics['date_date'].astype(str)
    monthly_metrics['margin_rate'] = (monthly_metrics['margin'] / monthly_metrics['revenue'] * 100).fillna(0)

    col1, col2 = st.columns(2)

    with col1:
        fig1 = go.Figure()
        fig1.add_trace(go.Bar(
            x=monthly_metrics['date_date'],
            y=monthly_metrics['revenue'],
            name='Revenue',
            marker_color='#1f77b4',
            yaxis='y'
        ))
        fig1.add_trace(go.Scatter(
            x=monthly_metrics['date_date'],
            y=monthly_metrics['margin_rate'],
            name='Taux de Marge (%)',
            marker_color='#ff7f0e',
            yaxis='y2',
            mode='lines+markers'
        ))
        fig1.update_layout(
            title="Revenue vs Taux de Marge",
            xaxis_title="Mois",
            yaxis=dict(title="Revenue (€)", side='left'),
            yaxis2=dict(title="Taux de Marge (%)", side='right', overlaying='y'),
            hovermode='x unified'
        )
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        fig2 = px.line(
            monthly_metrics,
            x='date_date',
            y='orders_id',
            title="Évolution du Nombre de Commandes",
            markers=True
        )
        fig2.update_traces(line_color='#2ca02c')
        st.plotly_chart(fig2, use_container_width=True)

def page_products(sales_enriched, products_evolution_df):
    """Page d'analyse des produits"""
    st.markdown('<h2 class="main-header">🛍️ Analyses Produits Avancées</h2>', unsafe_allow_html=True)

    # Top/Flop produits avec évolution
    st.subheader("🏆 Top & Flop Produits")

    product_summary = sales_enriched.groupby('pdt_id').agg({
        'revenue': 'sum',
        'quantity': 'sum',
        'margin': 'sum',
        'orders_id': 'nunique'
    }).round(2)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**🔥 TOP 10 Produits (Revenue)**")
        top_products = product_summary.sort_values('revenue', ascending=False).head(10)
        st.dataframe(top_products, use_container_width=True)

        # Graphique évolution du top produit
        top_product_id = top_products.index[0]
        top_evolution = products_evolution_df[products_evolution_df['pdt_id'] == top_product_id]

        if not top_evolution.empty:
            fig_top = px.line(
                top_evolution,
                x='month',
                y='revenue',
                title=f"Évolution Produit #{top_product_id} (Top Performer)",
                markers=True
            )
            st.plotly_chart(fig_top, use_container_width=True)

    with col2:
        st.markdown("**❄️ FLOP 10 Produits (Revenue)**")
        flop_products = product_summary[product_summary['revenue'] > 0].sort_values('revenue', ascending=True).head(10)
        st.dataframe(flop_products, use_container_width=True)

        # Distribution des marges
        fig_margin = px.histogram(
            sales_enriched,
            x='margin_rate',
            title="Distribution des Taux de Marge (%)",
            nbins=30
        )
        fig_margin.update_traces(marker_color='#ff7f0e')
        st.plotly_chart(fig_margin, use_container_width=True)

    # Analyse ABC
    st.subheader("📊 Analyse ABC - Concentration des Ventes")

    abc_analysis = calculate_abc_analysis(sales_enriched)

    col1, col2 = st.columns([2, 1])

    with col1:
        # Courbe ABC
        fig_abc = go.Figure()
        fig_abc.add_trace(go.Scatter(
            x=list(range(1, len(abc_analysis) + 1)),
            y=abc_analysis['cumulative_pct'],
            mode='lines',
            name='% Cumulé Revenue',
            line=dict(color='#1f77b4', width=3)
        ))
        fig_abc.add_hline(y=80, line_dash="dash", line_color="red", annotation_text="80% (Classe A)")
        fig_abc.add_hline(y=95, line_dash="dash", line_color="orange", annotation_text="95% (Classe B)")
        fig_abc.update_layout(
            title="Courbe ABC - Concentration des Ventes",
            xaxis_title="Rang des Produits",
            yaxis_title="% Cumulé du Revenue",
            yaxis=dict(range=[0, 100])
        )
        st.plotly_chart(fig_abc, use_container_width=True)

    with col2:
        # Répartition ABC
        abc_summary = abc_analysis['abc_class'].value_counts()
        fig_pie = px.pie(
            values=abc_summary.values,
            names=abc_summary.index,
            title="Répartition ABC",
            color_discrete_sequence=['#ff6b6b', '#feca57', '#48dbfb']
        )
        st.plotly_chart(fig_pie, use_container_width=True)

        # Métriques ABC
        st.markdown("**📈 Métriques ABC:**")
        for classe in ['A (80%)', 'B (15%)', 'C (5%)']:
            if classe in abc_summary.index:
                count = abc_summary[classe]
                pct = count / len(abc_analysis) * 100
                st.write(f"• **{classe}**: {count} produits ({pct:.1f}%)")

def page_market_basket(sales_enriched):
    """Page d'analyse du panier d'achat"""
    st.markdown('<h2 class="main-header">🔍 Market Basket Analysis</h2>', unsafe_allow_html=True)

    # Calculer les associations
    market_basket_df = perform_market_basket_analysis(sales_enriched)

    if market_basket_df.empty:
        st.warning("⚠️ Pas assez de paniers multi-produits pour l'analyse")
        return

    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("🛒 Top 20 Associations de Produits")
        st.dataframe(market_basket_df, use_container_width=True)

        # Graphique des associations
        fig_basket = px.bar(
            market_basket_df.head(10),
            x='frequency',
            y=[f"{row['product_1']} + {row['product_2']}" for _, row in market_basket_df.head(10).iterrows()],
            orientation='h',
            title="Associations les Plus Fréquentes",
            color='frequency',
            color_continuous_scale='viridis'
        )
        fig_basket.update_layout(yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig_basket, use_container_width=True)

    with col2:
        st.subheader("📊 Statistiques Paniers")

        # Analyser la distribution des tailles de panier
        basket_sizes = sales_enriched.groupby('orders_id')['pdt_id'].nunique()

        st.metric("🛒 Commandes Multi-produits", f"{(basket_sizes > 1).sum():,}")
        st.metric("📦 Taille Moyenne Panier", f"{basket_sizes.mean():.1f} items")
        st.metric("🔝 Plus Gros Panier", f"{basket_sizes.max()} items")

        # Distribution des tailles
        fig_sizes = px.histogram(
            basket_sizes.values,
            title="Distribution Tailles Paniers",
            nbins=10,
            labels={'x': 'Nombre d\'items', 'y': 'Fréquence'}
        )
        st.plotly_chart(fig_sizes, use_container_width=True)

def sidebar_navigation():
    """Navigation sidebar améliorée"""
    st.sidebar.markdown("# 🎛️ Navigation")

    # Toggle thème
    if st.sidebar.button("🌓 Basculer Thème", key="theme_toggle"):
        toggle_theme()
        st.rerun()

    st.sidebar.markdown(f"**Thème actuel:** {st.session_state.theme.title()}")
    st.sidebar.markdown("---")

    # Pages
    pages = {
        "📊 Vue d'ensemble": "overview",
        "🛍️ Analyse Produits": "products",
        "🔍 Market Basket": "basket"
    }

    selected_page = st.sidebar.radio(
        "Choisir une page",
        options=list(pages.keys()),
        key="page_selector"
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown("""
    ### 🎯 Analytics Disponibles
    - **Top/Flop produits** avec évolution
    - **Analyse de marge** (coût vs revenue)
    - **Courbe ABC** et concentration
    - **Market Basket** associations
    - **Interface multi-pages** moderne
    - **Thème sombre/clair** toggle
    """)

    return pages[selected_page]

def main():
    """Application principale multi-pages"""

    # CSS thème
    st.markdown(get_theme_css(), unsafe_allow_html=True)

    # Navigation
    current_page = sidebar_navigation()

    # Chargement des données
    sales_enriched, products_df, products_evolution_df = load_and_process_data()

    if sales_enriched is None:
        st.error("❌ Impossible de charger les données")
        return

    # Affichage conditionnel des pages
    if current_page == "overview":
        page_overview(sales_enriched)
    elif current_page == "products":
        page_products(sales_enriched, products_evolution_df)
    elif current_page == "basket":
        page_market_basket(sales_enriched)

    # Footer
    st.markdown("---")
    theme_icon = "🌙" if st.session_state.theme == 'dark' else "☀️"
    st.markdown(f"""
    <div style='text-align: center; color: #666;'>
        <p>{theme_icon} <strong>Advanced Analytics Portfolio</strong> |
        Otmane Boulahia - Data Engineer |
        <a href='https://zineinsight.com'>zineinsight.com</a> |
        Python + BigQuery + Streamlit + Advanced Analytics</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
