from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import json
import os
from datetime import datetime, timedelta
import pandas as pd

app = Flask(__name__, template_folder='../templates', static_folder='../static')
CORS(app)

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.jinja_env.auto_reload = True

# Charger les données Amazon
def load_amazon_data():
    """Charge les données et insights Amazon"""
    try:
        with open('data/amazon_insights.json', 'r') as f:
            insights = json.load(f)

        # Charger aussi les données brutes pour les graphiques détaillés
        products_df = pd.read_csv('data/amazon_products.csv')
        sales_df = pd.read_csv('data/amazon_sales_timeseries.csv')

        return insights, products_df, sales_df
    except FileNotFoundError:
        print("⚠️ Données Amazon non trouvées. Lancez d'abord generate_amazon_data.py")
        return None, None, None

# Charger les données au démarrage
amazon_insights, products_df, sales_df = load_amazon_data()

@app.route('/')
def index():
    """Page d'accueil - Aperçu des 3 études de cas"""
    studies = [
        {
            'id': 'ecommerce',
            'title': 'E-commerce Analytics',
            'subtitle': 'Amazon Product Performance Analysis',
            'description': 'Deep dive into 50K+ Amazon products with pricing strategies, seasonal trends, and category performance insights.',
            'metrics': [
                {'label': 'Products Analyzed', 'value': '50,000+'},
                {'label': 'Revenue Tracked', 'value': '$150M+'},
                {'label': 'Categories', 'value': '12'},
                {'label': 'Time Period', 'value': '2 Years'}
            ],
            'insights': [
                'Electronics dominate with $54M revenue',
                'Prime eligibility increases sales by 35%',
                'Black Friday drives 200% sales spike',
                '4.5+ rating products sell 60% more'
            ],
            'technologies': ['Python', 'Pandas', 'Plotly', 'Statistical Analysis'],
            'status': 'Active',
            'url': '/ecommerce'
        },
        {
            'id': 'finance',
            'title': 'Financial Market Analysis',
            'subtitle': 'Sentiment-Driven Trading Signals',
            'description': 'AI-powered analysis combining S&P 500 data with news sentiment to predict market movements and generate trading signals.',
            'metrics': [
                {'label': 'Stocks Tracked', 'value': '500'},
                {'label': 'News Sources', 'value': '50+'},
                {'label': 'Prediction Accuracy', 'value': '73%'},
                {'label': 'Time Frame', 'value': '5 Years'}
            ],
            'insights': [
                'Sentiment leads price by 2-4 hours',
                'Tech stocks most sensitive to news',
                'Weekend gaps predictable via sentiment',
                '15% annual returns achievable'
            ],
            'technologies': ['Python', 'NLP', 'Machine Learning', 'Financial APIs'],
            'status': 'Coming Soon',
            'url': '/finance'
        },
        {
            'id': 'saas',
            'title': 'SaaS Customer Analytics',
            'subtitle': 'Churn Prediction & Retention Strategy',
            'description': 'Machine learning model to predict customer churn with 85% accuracy and actionable retention recommendations.',
            'metrics': [
                {'label': 'Customers Analyzed', 'value': '7,000+'},
                {'label': 'Churn Prediction Accuracy', 'value': '85%'},
                {'label': 'Features Analyzed', 'value': '20+'},
                {'label': 'Retention Improvement', 'value': '23%'}
            ],
            'insights': [
                'Contract type is #1 churn predictor',
                'Support tickets correlation with churn',
                'Monthly customers churn 2x more',
                'Senior citizens need special attention'
            ],
            'technologies': ['Python', 'Scikit-learn', 'XGBoost', 'Cohort Analysis'],
            'status': 'Coming Soon',
            'url': '/saas'
        }
    ]

    return render_template('index.html', studies=studies)

@app.route('/ecommerce')
def ecommerce_study():
    """Étude de cas E-commerce Amazon"""
    if not amazon_insights:
        return "Données Amazon non disponibles. Lancez d'abord la génération des données.", 500

    return render_template('ecommerce.html', insights=amazon_insights)

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
    """Métriques générales E-commerce"""
    if not amazon_insights:
        return jsonify({'error': 'Data not available'}), 500

    return jsonify(amazon_insights['general_metrics'])

@app.route('/api/ecommerce/categories')
def api_ecommerce_categories():
    """Performance par catégorie"""
    if not amazon_insights:
        return jsonify({'error': 'Data not available'}), 500

    return jsonify(amazon_insights['category_performance'])

@app.route('/api/ecommerce/seasonal')
def api_ecommerce_seasonal():
    """Tendances saisonnières"""
    if not amazon_insights:
        return jsonify({'error': 'Data not available'}), 500

    return jsonify(amazon_insights['seasonal_trends'])

@app.route('/api/ecommerce/pricing')
def api_ecommerce_pricing():
    """Insights pricing"""
    if not amazon_insights:
        return jsonify({'error': 'Data not available'}), 500

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

    app.run(debug=True, host='0.0.0.0', port=5000)
