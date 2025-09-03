from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import json
import os
from datetime import datetime, timedelta
import pandas as pd

# Import données e-commerce réelles
import sys
sys.path.append(os.path.join(os.path.dirname(__file__)))
from data_ecommerce import (
    ECOMMERCE_MAIN_METRICS, TOP_PRODUCTS, MONTHLY_PERFORMANCE,
    CATEGORIES_PERFORMANCE, BUSINESS_ALERTS, BUSINESS_OPPORTUNITIES,
    ACTIONABLE_RECOMMENDATIONS, DASHBOARD_CONFIG
)

app = Flask(__name__, template_folder='../templates', static_folder='../static')
CORS(app)

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.jinja_env.auto_reload = True

# Charger les données Amazon (optionnel - pour compatibilité)
def load_amazon_data():
    """Charge les données et insights Amazon si disponibles"""
    try:
        with open('data/amazon_insights.json', 'r') as f:
            insights = json.load(f)
        # Charger aussi les données brutes pour les graphiques détaillés
        products_df = pd.read_csv('data/amazon_products.csv')
        sales_df = pd.read_csv('data/amazon_sales_timeseries.csv')
        return insights, products_df, sales_df
    except FileNotFoundError:
        print("⚠️ Données Amazon non trouvées - utilisation des données e-commerce réelles")
        return None, None, None

# Charger les données au démarrage (optionnel)
try:
    amazon_insights, products_df, sales_df = load_amazon_data()
except:
    amazon_insights, products_df, sales_df = None, None, None
    print("📊 Mode E-commerce Dashboard activé")

@app.route('/')
def index():
    """Page d'accueil - Nouveau dashboard e-commerce avec données Power BI réelles"""
    # Utilisation des données e-commerce réelles au lieu des anciennes données Amazon
    dashboard_data = {
        'main_metrics': ECOMMERCE_MAIN_METRICS,
        'top_products': TOP_PRODUCTS,
        'categories': CATEGORIES_PERFORMANCE,
        'business_alerts': BUSINESS_ALERTS
    }
    
    # Redirection vers le nouveau template e-commerce
    return render_template('ecommerce.html', **dashboard_data)

@app.route('/ecommerce')
def ecommerce_study():
    """Dashboard E-commerce Power BI - Page principale de showcase"""
    
    # Préparer les données pour le template
    dashboard_data = {
        'main_metrics': ECOMMERCE_MAIN_METRICS,
        'top_products': TOP_PRODUCTS,
        'monthly_performance': MONTHLY_PERFORMANCE,
        'categories': CATEGORIES_PERFORMANCE,
        'alerts': BUSINESS_ALERTS,
        'opportunities': BUSINESS_OPPORTUNITIES,
        'recommendations': ACTIONABLE_RECOMMENDATIONS,
        'dashboard_config': DASHBOARD_CONFIG
    }
    
    return render_template('ecommerce.html', **dashboard_data)

@app.route('/finance')
def finance_study():
    """Étude de cas Finance (placeholder)"""
    return render_template('coming_soon.html', study='Financial Market Analysis')

@app.route('/saas')
def saas_study():
    """Étude de cas SaaS (placeholder)"""
    return render_template('coming_soon.html', study='SaaS Customer Analytics')

# API Endpoints

@app.route('/api/studies')
def api_studies():
    """Liste des études disponibles"""
    return jsonify([
        {'id': 'ecommerce', 'title': 'E-commerce Analytics', 'status': 'active'},
        {'id': 'finance', 'title': 'Financial Analysis', 'status': 'coming_soon'},
        {'id': 'saas', 'title': 'SaaS Analytics', 'status': 'coming_soon'}
    ])

@app.route('/api/ecommerce/overview')
def api_ecommerce_overview():
    """Métriques générales E-commerce - Données réelles"""
    return jsonify({
        'main_metrics': ECOMMERCE_MAIN_METRICS,
        'dashboard_config': DASHBOARD_CONFIG,
        'last_update': datetime.now().isoformat()
    })

@app.route('/api/ecommerce/temporal')
def api_ecommerce_temporal():
    """Données d'évolution temporelle"""
    return jsonify({
        'monthly_data': MONTHLY_PERFORMANCE,
        'insights': {
            'peak_month': max(MONTHLY_PERFORMANCE, key=lambda x: x['revenue']),
            'low_month': min(MONTHLY_PERFORMANCE, key=lambda x: x['revenue']),
            'total_revenue': sum(month['revenue'] for month in MONTHLY_PERFORMANCE),
            'avg_conversion': sum(month['conversion'] for month in MONTHLY_PERFORMANCE) / len(MONTHLY_PERFORMANCE)
        }
    })

@app.route('/api/ecommerce/categories')
def api_ecommerce_categories():
    """Performance par catégories"""
    return jsonify({
        'categories': CATEGORIES_PERFORMANCE,
        'summary': {
            'leader': max(CATEGORIES_PERFORMANCE, key=lambda x: x['revenue']),
            'most_profitable': max(CATEGORIES_PERFORMANCE, key=lambda x: x['margin']),
            'needs_attention': [cat for cat in CATEGORIES_PERFORMANCE if cat['status'] in ['alert', 'warning']]
        }
    })

@app.route('/api/ecommerce/products')
def api_ecommerce_products():
    """Top produits et analyse"""
    return jsonify({
        'top_products': TOP_PRODUCTS,
        'analysis': {
            'best_performer': TOP_PRODUCTS[0],
            'highest_growth': max(TOP_PRODUCTS, key=lambda x: x['growth']),
            'highest_margin': max(TOP_PRODUCTS, key=lambda x: x['margin']),
            'needs_attention': [prod for prod in TOP_PRODUCTS if prod['growth'] < 0]
        }
    })

@app.route('/api/ecommerce/alerts')
def api_ecommerce_alerts():
    """Alertes business et recommandations"""
    return jsonify({
        'alerts': BUSINESS_ALERTS,
        'opportunities': BUSINESS_OPPORTUNITIES,
        'recommendations': ACTIONABLE_RECOMMENDATIONS,
        'priority_actions': [rec for rec in ACTIONABLE_RECOMMENDATIONS if rec['priority'] <= 2]
    })

# ===== LEGACY AMAZON API ROUTES (pour compatibilité) =====

@app.route('/api/ecommerce/seasonal')
def api_ecommerce_seasonal():
    """Tendances saisonnières - Legacy Amazon API"""
    if not amazon_insights:
        return jsonify({'error': 'Data not available - using real e-commerce data'}), 500
    return jsonify(amazon_insights['seasonal_trends'])

@app.route('/api/ecommerce/pricing')
def api_ecommerce_pricing():
    """Insights pricing - Legacy Amazon API"""
    if not amazon_insights:
        return jsonify({'error': 'Data not available - using real e-commerce data'}), 500
    return jsonify(amazon_insights['pricing_insights'])

@app.route('/api/ecommerce/top-performers')
def api_ecommerce_top_performers():
    """Top produits et marques"""
    if not amazon_insights:
        return jsonify({'error': 'Data not available'}), 500

    return jsonify(amazon_insights['top_performers'])

@app.route('/api/ecommerce/timeseries')
def api_ecommerce_timeseries():
    """Données temporelles pour graphiques"""
    if sales_df is None:
        return jsonify({'error': 'Data not available'}), 500

    # Prendre les 90 derniers jours pour éviter trop de données
    recent_data = sales_df.tail(90)

    timeseries_data = {
        'dates': recent_data['date'].tolist(),
        'sales': recent_data['total_sales'].tolist(),
        'revenue': recent_data['revenue'].round(2).tolist(),
        'orders': recent_data['orders'].tolist()
    }

    return jsonify(timeseries_data)

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'data_loaded': amazon_insights is not None
    })

if __name__ == '__main__':
    if not amazon_insights:
        print("⚠️  ATTENTION: Données Amazon manquantes!")
        print("🔧 Lancez d'abord: python generate_amazon_data.py && python analyze_amazon_data.py")
    else:
        print("✅ Données Amazon chargées avec succès!")
        print(f"📊 {amazon_insights['general_metrics']['total_products']:,} produits disponibles")

    # Démarrer le serveur sur le port 8002 (nginx proxie vers ce port)
    app.run(debug=True, host='0.0.0.0', port=8002)
