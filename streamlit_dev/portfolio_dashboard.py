"""
📊 PORTFOLIO ANALYTICS DASHBOARD
================================
Dashboard Streamlit pour démonstration des compétences data engineering
Otmane Boulahia - Data Engineer - zineinsight.com

Données : BigQuery Export → Pandas → Plotly → Streamlit
Stack : Python, BigQuery API, Streamlit, Plotly, Pandas
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np

# Configuration Streamlit
st.set_page_config(
    page_title="📊 Analytics Portfolio | Otmane Data Engineer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
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
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Charge les données exportées depuis BigQuery"""
    try:
        # Charger les datasets nettoyés
        sales_df = pd.read_csv('data/cleaned_datasets/sales_cleaned.csv')
        products_df = pd.read_csv('data/cleaned_datasets/products_cleaned.csv')
        facebook_df = pd.read_csv('data/cleaned_datasets/facebook_cleaned.csv')

        # Traitement des dates
        sales_df['date_date'] = pd.to_datetime(sales_df['date_date'])

        # Calculs business
        sales_df['order_value'] = sales_df['revenue'] * sales_df['quantity']

        return sales_df, products_df, facebook_df
    except Exception as e:
        st.error(f"Erreur chargement données : {e}")
        return None, None, None

def main():
    """Application principale"""

    # En-tête
    st.markdown('<h1 class="main-header">📊 Data Engineering Portfolio</h1>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([2, 3, 2])
    with col2:
        st.markdown("""
        ### 🎯 Otmane Boulahia - Data Engineer
        **Stack Technique :** Python • BigQuery • Streamlit • Plotly
        **Données :** 1.3M+ transactions e-commerce réelles
        **Source :** BigQuery API → Pandas → Visualisation interactive
        """)

    # Chargement des données
    sales_df, products_df, facebook_df = load_data()

    if sales_df is None:
        st.error("❌ Impossible de charger les données")
        return

    # Sidebar
    st.sidebar.header("🎛️ Contrôles Dashboard")
    st.sidebar.markdown("---")

    # Filtres de dates
    min_date = sales_df['date_date'].min()
    max_date = sales_df['date_date'].max()

    date_range = st.sidebar.date_input(
        "📅 Période d'analyse",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )

    # Filtrer les données
    if len(date_range) == 2:
        mask = (sales_df['date_date'] >= pd.to_datetime(date_range[0])) & (sales_df['date_date'] <= pd.to_datetime(date_range[1]))
        filtered_sales = sales_df.loc[mask]
    else:
        filtered_sales = sales_df

    # KPIs principaux
    st.header("📈 KPIs E-commerce")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        total_revenue = filtered_sales['revenue'].sum()
        st.metric(
            label="💰 Chiffre d'Affaires",
            value=f"{total_revenue:,.0f}€",
            delta=f"{len(filtered_sales)} transactions"
        )

    with col2:
        avg_order = filtered_sales['revenue'].mean()
        st.metric(
            label="🛒 Panier Moyen",
            value=f"{avg_order:.2f}€",
            delta=f"±{filtered_sales['revenue'].std():.2f}€"
        )

    with col3:
        total_orders = filtered_sales['orders_id'].nunique()
        st.metric(
            label="📦 Commandes Uniques",
            value=f"{total_orders:,}",
            delta=f"{len(filtered_sales)} lignes"
        )

    with col4:
        avg_quantity = filtered_sales['quantity'].mean()
        st.metric(
            label="📊 Qté Moyenne",
            value=f"{avg_quantity:.1f}",
            delta=f"Max: {filtered_sales['quantity'].max()}"
        )

    st.markdown("---")

    # Graphiques
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📈 Évolution du CA quotidien")
        daily_sales = filtered_sales.groupby('date_date')['revenue'].sum().reset_index()

        fig1 = px.line(
            daily_sales,
            x='date_date',
            y='revenue',
            title="Chiffre d'affaires par jour",
            labels={'revenue': 'Revenue (€)', 'date_date': 'Date'}
        )
        fig1.update_traces(line_color='#1f77b4', line_width=3)
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.subheader("🛍️ Distribution des paniers")

        fig2 = px.histogram(
            filtered_sales,
            x='revenue',
            nbins=50,
            title="Répartition des montants de commande",
            labels={'revenue': 'Montant (€)', 'count': 'Nombre de commandes'}
        )
        fig2.update_traces(marker_color='#ff7f0e')
        st.plotly_chart(fig2, use_container_width=True)

    # Analyse produits
    st.header("🎯 Analyse Produits")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🏆 Top 10 Produits (Revenue)")
        top_products = filtered_sales.groupby('pdt_id')['revenue'].sum().sort_values(ascending=False).head(10)

        fig3 = px.bar(
            x=top_products.values,
            y=[f"Produit {pid}" for pid in top_products.index],
            orientation='h',
            title="Top 10 produits par chiffre d'affaires",
            labels={'x': 'Revenue (€)', 'y': 'Produits'}
        )
        fig3.update_traces(marker_color='#2ca02c')
        st.plotly_chart(fig3, use_container_width=True)

    with col2:
        st.subheader("📦 Top 10 Produits (Quantité)")
        top_qty = filtered_sales.groupby('pdt_id')['quantity'].sum().sort_values(ascending=False).head(10)

        fig4 = px.bar(
            x=top_qty.values,
            y=[f"Produit {pid}" for pid in top_qty.index],
            orientation='h',
            title="Top 10 produits par quantité vendue",
            labels={'x': 'Quantité', 'y': 'Produits'}
        )
        fig4.update_traces(marker_color='#d62728')
        st.plotly_chart(fig4, use_container_width=True)

    # 🚀 NOUVELLE FONCTIONNALITÉ - Analyse mensuelle
    st.header("📅 Analyse Temporelle Avancée")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📈 Tendances Mensuelles")
        monthly_sales = filtered_sales.groupby(filtered_sales['date_date'].dt.to_period('M'))['revenue'].agg(['sum', 'count', 'mean']).reset_index()
        monthly_sales['date_date'] = monthly_sales['date_date'].dt.to_timestamp()

        fig5 = go.Figure()
        fig5.add_trace(go.Scatter(
            x=monthly_sales['date_date'],
            y=monthly_sales['sum'],
            mode='lines+markers',
            name='CA Total',
            line=dict(color='#1f77b4', width=3),
            marker=dict(size=8)
        ))
        fig5.update_layout(
            title="Évolution du CA mensuel",
            xaxis_title="Mois",
            yaxis_title="Chiffre d'affaires (€)",
            showlegend=True
        )
        st.plotly_chart(fig5, use_container_width=True)

    with col2:
        st.subheader("📊 Saisonnalité par Jour de la Semaine")
        filtered_sales['day_name'] = filtered_sales['date_date'].dt.day_name()
        weekly_pattern = filtered_sales.groupby('day_name')['revenue'].sum().reindex([
            'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
        ])

        fig6 = px.bar(
            x=['Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam', 'Dim'],
            y=weekly_pattern.values,
            title="Répartition du CA par jour de la semaine",
            labels={'x': 'Jour', 'y': 'Revenue (€)'}
        )
        fig6.update_traces(marker_color='#9467bd')
        st.plotly_chart(fig6, use_container_width=True)

    # Données brutes
    st.header("🔍 Exploration des Données")

    if st.checkbox("Afficher les données brutes"):
        st.subheader("📊 Échantillon des transactions")
        st.dataframe(
            filtered_sales.head(1000),
            use_container_width=True
        )

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>🚀 <strong>Portfolio Data Engineering</strong> |
        Otmane Boulahia |
        <a href='https://zineinsight.com'>zineinsight.com</a> |
        Python + BigQuery + Streamlit</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
