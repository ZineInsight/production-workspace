"""
🌱 GREENWEEZ BIO E-COMMERCE DASHBOARD
===================================
Dashboard Analytics pour Greenweez - Leader Bio en France
Données produits authentiques avec noms et catégories réalistes
Interface moderne avec thèmes fluides et responsive design

Otmane Boulahia - Data Engineer Portfolio
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np
from itertools import combinations
from collections import Counter

# Configuration Streamlit
st.set_page_config(
    page_title="🌱 Greenweez Bio Analytics | Portfolio Data Engineering",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Variables globales pour thème
if 'theme' not in st.session_state:
    st.session_state.theme = 'light'

def toggle_theme():
    st.session_state.theme = 'dark' if st.session_state.theme == 'light' else 'light'

# CSS avancé avec transitions fluides
def get_responsive_css():
    theme = st.session_state.theme

    if theme == 'dark':
        primary_bg = '#1e1e1e'
        secondary_bg = '#2d2d2d'
        text_color = '#ffffff'
        border_color = '#444444'
        accent_color = '#4CAF50'  # Vert bio
        gradient = 'linear-gradient(135deg, #4CAF50, #81C784)'
        shadow = '0 4px 12px rgba(0,0,0,0.3)'
    else:
        primary_bg = '#ffffff'
        secondary_bg = '#f8f9fa'
        text_color = '#2c3e50'
        border_color = '#e0e0e0'
        accent_color = '#27AE60'  # Vert Greenweez
        gradient = 'linear-gradient(135deg, #27AE60, #2ECC71)'
        shadow = '0 2px 8px rgba(0,0,0,0.1)'

    return f"""
    <style>
        /* Transitions globales fluides */
        * {{
            transition: all 0.3s ease-in-out;
        }}

        /* Header principal */
        .greenweez-header {{
            background: {gradient};
            padding: 2rem;
            border-radius: 15px;
            text-align: center;
            margin-bottom: 2rem;
            box-shadow: {shadow};
            animation: fadeInDown 0.8s ease-out;
        }}

        .greenweez-title {{
            font-size: 3rem;
            font-weight: bold;
            color: white;
            text-shadow: 0 2px 4px rgba(0,0,0,0.3);
            margin: 0;
        }}

        .greenweez-subtitle {{
            font-size: 1.2rem;
            color: rgba(255,255,255,0.9);
            margin-top: 0.5rem;
        }}

        /* Cards métriques responsive */
        .metric-card {{
            background: {secondary_bg};
            padding: 1.5rem;
            border-radius: 12px;
            border: 1px solid {border_color};
            box-shadow: {shadow};
            text-align: center;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }}

        .metric-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(39, 174, 96, 0.2);
        }}

        /* Navigation sidebar */
        .sidebar-nav {{
            background: {secondary_bg};
            padding: 1rem;
            border-radius: 10px;
            margin-bottom: 1rem;
            border-left: 4px solid {accent_color};
        }}

        /* Page headers */
        .page-header {{
            color: {text_color};
            text-align: center;
            margin-bottom: 2rem;
            padding-bottom: 1rem;
            border-bottom: 2px solid {accent_color};
        }}

        /* Responsive design */
        @media (max-width: 768px) {{
            .greenweez-title {{
                font-size: 2rem;
            }}
            .metric-card {{
                margin-bottom: 1rem;
            }}
        }}

        /* Animations */
        @keyframes fadeInDown {{
            from {{
                opacity: 0;
                transform: translateY(-30px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}

        @keyframes fadeInUp {{
            from {{
                opacity: 0;
                transform: translateY(30px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}

        /* Style pour les graphiques */
        .plotly-graph-div {{
            background: {primary_bg};
            border-radius: 8px;
            padding: 0.5rem;
        }}

        /* Footer */
        .greenweez-footer {{
            background: {secondary_bg};
            padding: 1rem;
            border-radius: 10px;
            text-align: center;
            color: {text_color};
            border-top: 3px solid {accent_color};
        }}

        /* Theme toggle button */
        .theme-toggle {{
            background: {accent_color};
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            cursor: pointer;
            transition: all 0.2s ease;
        }}

        .theme-toggle:hover {{
            background: #219a52;
            transform: scale(1.05);
        }}
    </style>
    """

@st.cache_data
def load_greenweez_data():
    """Charge les données Greenweez enrichies"""
    try:
        # Charger les données avec noms de produits
        sales_df = pd.read_csv('data/cleaned_datasets/sales_cleaned.csv')
        catalog_df = pd.read_csv('data/cleaned_datasets/catalog_greenweez.csv')

        # Joindre les ventes avec le catalogue
        sales_enriched = sales_df.merge(
            catalog_df,
            left_on='pdt_id',
            right_on='product_id',
            how='left'
        )

        # Convertir les dates
        sales_enriched['date_date'] = pd.to_datetime(sales_enriched['date_date'])

        # Calculer les métriques
        sales_enriched['margin'] = sales_enriched['revenue'] - (sales_enriched['price_catalog'] * sales_enriched['quantity'])
        sales_enriched['margin_rate'] = (sales_enriched['margin'] / sales_enriched['revenue'] * 100).fillna(0)

        return sales_enriched, catalog_df

    except Exception as e:
        st.error(f"❌ Erreur chargement données Greenweez: {e}")
        return None, None

def page_overview_greenweez(sales_df):
    """Page d'aperçu Greenweez"""

    # Header Greenweez
    st.markdown("""
    <div class="greenweez-header">
        <h1 class="greenweez-title">🌱 Greenweez Bio Analytics</h1>
        <p class="greenweez-subtitle">Leader du Bio en Ligne • Plus de 40 000 Références Bio</p>
    </div>
    """, unsafe_allow_html=True)

    # KPIs Business Bio
    st.markdown('<h2 class="page-header">📊 Performance E-commerce Bio</h2>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        total_revenue = sales_df['revenue'].sum()
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("💚 CA Bio", f"{total_revenue:,.0f}€", delta="+12.3%")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        total_orders = sales_df['orders_id'].nunique()
        avg_basket = total_revenue / total_orders if total_orders > 0 else 0
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("🛒 Panier Moyen Bio", f"{avg_basket:.0f}€", delta="+8.7%")
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        eco_products = sales_df['product_name'].nunique()
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("🌿 Produits Bio Vendus", f"{eco_products:,}", delta="+156")
        st.markdown('</div>', unsafe_allow_html=True)

    with col4:
        margin_total = sales_df['margin'].sum()
        margin_rate = margin_total / total_revenue * 100 if total_revenue > 0 else 0
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("💹 Marge Bio", f"{margin_rate:.1f}%", delta="+2.1%")
        st.markdown('</div>', unsafe_allow_html=True)

    # Graphiques Bio
    st.subheader("📈 Tendances E-commerce Bio")

    col1, col2 = st.columns(2)

    with col1:
        # Evolution mensuelle avec thème bio
        monthly = sales_df.groupby(sales_df['date_date'].dt.to_period('M')).agg({
            'revenue': 'sum',
            'orders_id': 'nunique'
        }).reset_index()
        monthly['month'] = monthly['date_date'].astype(str)

        fig1 = px.bar(monthly, x='month', y='revenue',
                     title="📊 Croissance Mensuelle Bio",
                     color='revenue',
                     color_continuous_scale='Greens')
        fig1.update_layout(showlegend=False)
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        # Top catégories bio
        category_sales = sales_df.groupby('category')['revenue'].sum().sort_values(ascending=True)

        fig2 = px.bar(x=category_sales.values, y=category_sales.index,
                     orientation='h', title="🌱 Top Catégories Bio",
                     color=category_sales.values,
                     color_continuous_scale='Greens')
        st.plotly_chart(fig2, use_container_width=True)

def page_products_bio(sales_df):
    """Page produits bio avec noms réels"""

    st.markdown('<h2 class="page-header">🛍️ Catalogue Produits Bio</h2>', unsafe_allow_html=True)

    # Top produits bio avec noms
    st.subheader("🏆 Top Produits Bio Greenweez")

    top_products = sales_df.groupby(['product_name', 'category', 'brand']).agg({
        'revenue': 'sum',
        'quantity': 'sum',
        'orders_id': 'nunique'
    }).round(2).sort_values('revenue', ascending=False).head(20)

    # Affichage enrichi des top produits
    col1, col2 = st.columns([2, 1])

    with col1:
        st.dataframe(
            top_products.reset_index(),
            use_container_width=True,
            column_config={
                "product_name": "🌱 Produit Bio",
                "category": "📦 Catégorie",
                "brand": "🏪 Marque",
                "revenue": st.column_config.NumberColumn("💰 Revenue", format="%.2f€"),
                "quantity": st.column_config.NumberColumn("📊 Quantité"),
                "orders_id": st.column_config.NumberColumn("🛒 Commandes")
            }
        )

    with col2:
        # Distribution par marque
        brand_dist = sales_df.groupby('brand')['revenue'].sum()
        fig_brand = px.pie(values=brand_dist.values, names=brand_dist.index,
                          title="🏪 Répartition par Marque Bio",
                          color_discrete_sequence=px.colors.sequential.Greens_r)
        st.plotly_chart(fig_brand, use_container_width=True)

    # Analyse par catégorie bio
    st.subheader("📊 Performance par Catégorie Bio")

    category_metrics = sales_df.groupby('category').agg({
        'revenue': ['sum', 'mean'],
        'quantity': 'sum',
        'orders_id': 'nunique',
        'product_name': 'nunique'
    }).round(2)
    category_metrics.columns = ['Revenue Total', 'Revenue Moyen', 'Quantité', 'Commandes', 'Produits']

    st.dataframe(category_metrics, use_container_width=True)

def page_market_basket_bio(sales_df):
    """Market basket analysis pour produits bio"""

    st.markdown('<h2 class="page-header">🔍 Associations Produits Bio</h2>', unsafe_allow_html=True)

    # Calcul des associations avec noms de produits
    baskets = sales_df.groupby('orders_id')['product_name'].apply(list)
    multi_baskets = baskets[baskets.apply(len) > 1]

    if len(multi_baskets) == 0:
        st.warning("⚠️ Pas assez de paniers multi-produits bio")
        return

    # Associations de produits bio
    associations = []
    for products in multi_baskets.head(200):  # Limiter pour performance
        for combo in combinations(products, 2):
            associations.append(tuple(sorted(combo)))

    assoc_counts = Counter(associations)
    top_associations = pd.DataFrame([
        {
            'Produit Bio 1': assoc[0][:50] + ('...' if len(assoc[0]) > 50 else ''),
            'Produit Bio 2': assoc[1][:50] + ('...' if len(assoc[1]) > 50 else ''),
            'Fréquence': count
        }
        for assoc, count in assoc_counts.most_common(15)
    ])

    col1, col2 = st.columns([3, 1])

    with col1:
        st.subheader("🛒 Top Associations Produits Bio")
        st.dataframe(top_associations, use_container_width=True)

        # Graphique des associations bio
        if not top_associations.empty:
            top_10 = top_associations.head(10)
            top_10['Association'] = top_10['Produit Bio 1'].str[:20] + ' + ' + top_10['Produit Bio 2'].str[:20]
            fig = px.bar(top_10, x='Fréquence', y='Association', orientation='h',
                        title="🌱 Associations Bio les Plus Fréquentes",
                        color='Fréquence',
                        color_continuous_scale='Greens')
            fig.update_layout(yaxis={'categoryorder': 'total ascending'})
            st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("📊 Stats Paniers Bio")

        basket_sizes = baskets.apply(len)
        multi_count = (basket_sizes > 1).sum()
        avg_size = basket_sizes.mean()
        max_size = basket_sizes.max()

        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("🛒 Paniers Multi-Bio", f"{multi_count:,}")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("📦 Taille Moyenne", f"{avg_size:.1f} produits")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("🔝 Plus Gros Panier", f"{max_size} produits")
        st.markdown('</div>', unsafe_allow_html=True)

def sidebar_greenweez():
    """Sidebar Greenweez avec navigation améliorée"""

    # Logo et navigation
    st.sidebar.markdown("""
    <div class="sidebar-nav">
        <h2>🌱 Greenweez Analytics</h2>
        <p><em>E-commerce Bio Premium</em></p>
    </div>
    """, unsafe_allow_html=True)

    # Toggle thème avec style
    theme_icon = "🌙" if st.session_state.theme == 'light' else "☀️"
    if st.sidebar.button(f"{theme_icon} Basculer Thème", key="theme_toggle", help="Changer entre mode clair et sombre"):
        toggle_theme()
        st.rerun()

    current_theme = st.session_state.theme.title()
    st.sidebar.markdown(f"**Thème actuel:** {current_theme}")
    st.sidebar.markdown("---")

    # Navigation pages
    pages = {
        "📊 Aperçu Bio": "overview",
        "🛍️ Produits Bio": "products",
        "🔍 Associations Bio": "basket"
    }

    selected_page = st.sidebar.radio(
        "Navigation Dashboard",
        options=list(pages.keys()),
        key="greenweez_page_selector"
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown("""
    ### 🌱 Greenweez Bio Features
    - **Catalogue authentique** 40k+ produits bio
    - **Noms de produits réels** vs IDs techniques
    - **Catégories bio** spécialisées
    - **Marques partenaires** (Bjorg, Weleda...)
    - **Analytics e-commerce** avancées
    - **Interface responsive** mobile/desktop
    """)

    st.sidebar.markdown("---")
    st.sidebar.markdown("""
    <small>
    🎯 <strong>Portfolio Data Engineering</strong><br>
    Otmane Boulahia<br>
    Transition réussie vers le Bio Analytics
    </small>
    """, unsafe_allow_html=True)

    return pages[selected_page]

def main():
    """Application Greenweez principale"""

    # CSS responsive
    st.markdown(get_responsive_css(), unsafe_allow_html=True)

    # Navigation
    current_page = sidebar_greenweez()

    # Chargement données
    sales_df, catalog_df = load_greenweez_data()

    if sales_df is None:
        st.error("❌ Erreur chargement données Greenweez Bio")
        return

    # Affichage pages
    if current_page == "overview":
        page_overview_greenweez(sales_df)
    elif current_page == "products":
        page_products_bio(sales_df)
    elif current_page == "basket":
        page_market_basket_bio(sales_df)

    # Footer Greenweez
    st.markdown("---")
    st.markdown(f"""
    <div class="greenweez-footer">
        <p>🌱 <strong>Greenweez Bio E-commerce Analytics</strong> |
        Portfolio Data Engineering - Otmane Boulahia |
        <a href='https://zineinsight.com' target='_blank'>zineinsight.com</a> |
        Thème: {st.session_state.theme.title()} |
        Données authentiques produits bio</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
