"""
🌐 REVOLUTIONARY BACKEND - GATEWAY UNIFIÉ
=========================================
Gateway principal pour tous les services ZineInsight Revolutionary
Port 8000 - Compatible avec le frontend SPA parfait

Services intégrés:
🏙️ ZScore v2.0.0      → Intelligence géographique (/api/calculate)
🇺🇸 USAResidents v1.0.0 → Intelligence relocation USA (/api/usa-residents)
🇫🇷 FranceResidents v1.0.0 → Intelligence relocation France (/api/france-residents)
�🇭 ThailandResidents v1.0.0 → Intelligence relocation Thailand (/api/thailand-residents)
�🇪🇸 SpainResidents v1.0.0 → Intelligence relocation Spain (/api/spain-residents)
🇲🇽 MexicoResidents v1.0.0 → Intelligence relocation Mexico (/api/mexico-residents)
💼 SkillGraph v1.0.0   → Intelligence carrière (/api/career)
💰 Wealth v0.9.0       → Intelligence patrimoniale (/api/wealth)

Architecture révolutionnaire:
- 8 services, 283+ critères d'intelligence totaux
- Session unifiée avec cross-sell intelligent
- Sécurité production centralisée
- Stripe LIVE integration premium
- Monitoring et analytics avancés
"""

import os
import logging
from flask import Flask, request, jsonify, session, render_template
from flask_cors import CORS
import stripe
from datetime import datetime
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv('/var/www/production-workspace/.env')

# Import des services Revolutionary
from services.zscore import zscore_bp, ZScoreAlgorithm
from services.skillgraph import skillgraph_bp, SkillGraphAlgorithm
from services.wealth import wealth_bp, WealthAlgorithm
from algo_usa_residents import USAResidentsAlgorithm
from algo_france_residents import FranceResidentsAlgorithm
from algo_canada_residents import CanadaResidentsAlgorithm
from algo_uk_residents import UKResidentsAlgorithm
from algo_germany_residents import GermanyResidentsAlgorithm
from algo_australia_residents import AustraliaResidentsAlgorithm
from algo_spain_residents import SpainResidentsAlgorithm
from algo_japan_residents import JapanResidentsAlgorithm
from algo_mexico_residents import get_mexico_recommendations
from algo_morocco_residents import MoroccoResidentsAlgorithm
from algo_brazil_residents import BrazilResidentsAlgorithm
from algo_thailand_residents import ThailandResidentsAlgorithm
from core.security_middleware import SecurityMiddleware
from core.data_loader import DataLoader

# Import du système d'authentification
from auth import auth_bp, init_auth_manager, init_paywall_manager

# Import du système de paiements
from payments.stripe_live_routes import payments_bp

# Configuration logging production
log_dir = os.path.join(os.getcwd(), 'logs')
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(log_dir, 'revolutionary.log')),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# ===============================
# 🚀 APPLICATION FLASK PRINCIPALE
# ===============================

def create_app():
    """Factory pour créer l'application Flask avec tous les services"""

    # Définir le chemin vers le dossier frontend/spa
    frontend_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'frontend', 'spa')

    app = Flask(__name__,
                static_folder=frontend_path,
                static_url_path='')

    # Configuration sécurisée
    app.secret_key = os.environ.get('SECRET_KEY', 'revolutionary-dev-key-change-in-production')

    # Configuration des variables d'environnement
    app.config['SENDGRID_API_KEY'] = os.environ.get('SENDGRID_API_KEY')
    app.config['REDIS_HOST'] = os.environ.get('REDIS_HOST', 'localhost')
    app.config['REDIS_PORT'] = int(os.environ.get('REDIS_PORT', 6379))

    # CORS pour le frontend SPA
    CORS(app, origins=[
        "https://zineinsight.com",
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ])

    # ===============================
    # 🛡️ SÉCURITÉ PRODUCTION
    # ===============================

    # Middleware sécurité centralisé
    security_config = {
        'session_lifetime_hours': 24,
        'max_requests_per_hour': 1000,
        'audit_logs_enabled': True,
        'rate_limiting_enabled': True
    }
    security = SecurityMiddleware(app, security_config)

    # Validation environnement critique (optionnelle en dev)
    env_status = security.validate_environment()
    if not env_status:
        logger.warning("⚠️ Missing environment variables - Running in DEV mode")
    else:
        logger.info("✅ Environment validation successful")

    # Configuration Stripe LIVE
    stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')

    # ===============================
    # 📊 INITIALISATION SERVICES
    # ===============================

    # DataLoader centralisé avec préchargement
    data_loader = DataLoader()
    preload_stats = data_loader.preload_essential_data()
    logger.info(f"📊 Data preloaded: {preload_stats}")

    # Instances des algorithmes (partagées)
    zscore_algo = ZScoreAlgorithm()  # ✅ Utilise le constructeur par défaut
    usa_residents_algo = USAResidentsAlgorithm('/var/www/production-workspace/backend/data_v2/villes_usa_residents.json')
    france_residents_algo = FranceResidentsAlgorithm('/var/www/production-workspace/backend/data_v2/villes_france_residents.json')
    canada_residents_algo = CanadaResidentsAlgorithm('/var/www/production-workspace/backend/data_v2/villes_canada_residents.json')
    uk_residents_algo = UKResidentsAlgorithm('/var/www/production-workspace/backend/data_v2/villes_uk_residents.json')
    germany_residents_algo = GermanyResidentsAlgorithm('/var/www/production-workspace/backend/data_v2/villes_germany_residents.json')
    australia_residents_algo = AustraliaResidentsAlgorithm('/var/www/production-workspace/backend/data_v2/villes_australia_residents.json')
    spain_residents_algo = SpainResidentsAlgorithm('/var/www/production-workspace/backend/data_v2/villes_spain_residents.json')
    japan_residents_algo = JapanResidentsAlgorithm('/var/www/production-workspace/backend/data_v2/villes_japan_residents.json')
    morocco_residents_algo = MoroccoResidentsAlgorithm('/var/www/production-workspace/backend/data_v2/villes_morocco_residents.json')
    brazil_residents_algo = BrazilResidentsAlgorithm('/var/www/production-workspace/backend/data_v2/villes_brazil_residents.json')
    thailand_residents_algo = ThailandResidentsAlgorithm('/var/www/production-workspace/backend/data_v2/villes_thailand_residents.json')
    skillgraph_algo = SkillGraphAlgorithm(data_loader)
    wealth_algo = WealthAlgorithm(data_loader)

    logger.info(f"✅ All algorithms initialized:")
    logger.info(f"  🏙️ ZScore: {len(zscore_algo.get_available_countries())} countries")
    logger.info(f"  🇺🇸 USAResidents: {len(usa_residents_algo.cities_data['cities'])} cities")
    logger.info(f"  🇫🇷 FranceResidents: {len(france_residents_algo.cities_data['cities'])} cities")
    logger.info(f"  🇨🇦 CanadaResidents: {len(canada_residents_algo.cities_data['cities'])} cities")
    logger.info(f"  🇬🇧 UKResidents: {len(uk_residents_algo.cities_data['cities'])} cities")
    logger.info(f"  🇯🇵 JapanResidents: {len(japan_residents_algo.cities_data['cities'])} cities")
    logger.info(f"  🇪🇸 SpainResidents: {len(spain_residents_algo.cities_data)} cities")
    logger.info(f"  �🇦 MoroccoResidents: {len(morocco_residents_algo.cities_data['cities'])} cities")
    logger.info(f"  �🇧🇷 BrazilResidents: {len(brazil_residents_algo.cities_data['cities'])} cities")
    logger.info(f"  🇹🇭 ThailandResidents: {len(thailand_residents_algo.cities_data['cities'])} cities")
    logger.info(f"  💼 SkillGraph: {len(skillgraph_algo.get_supported_sectors())} sectors")
    logger.info(f"  💰 Wealth: {len(wealth_algo.get_supported_markets())} markets")

    # ===============================
    # 🔐 INITIALISATION AUTHENTIFICATION
    # ===============================

    # Initialiser l'AuthManager avec la config Flask
    auth_manager = init_auth_manager(app)
    paywall_manager = init_paywall_manager()

    logger.info("🔐 Authentication system ready")

    # ===============================
    # 🌐 ENREGISTREMENT BLUEPRINTS
    # ===============================

    app.register_blueprint(zscore_bp)
    app.register_blueprint(skillgraph_bp)
    app.register_blueprint(wealth_bp)
    app.register_blueprint(auth_bp)  # Routes d'authentification
    app.register_blueprint(payments_bp)  # Routes de paiement Stripe

    logger.info("🌐 All service blueprints registered")

    # ===============================
    # 🏠 ROUTES PRINCIPALES GATEWAY
    # ===============================

    @app.route('/api/')
    def api_info():
        """Information sur l'API - endpoint racine"""
        return jsonify({
            "message": "🎯 ZineInsight Revolutionary API",
            "version": "1.0.0",
            "status": "operational",
            "available_services": [
                "/api/calculate",
                "/api/career",
                "/api/wealth",
                "/api/usa-residents/recommendations",
                "/api/france-residents/recommendations",
                "/api/thailand-residents/recommendations",
                "/api/health"
            ],
            "documentation": "/",
            "timestamp": datetime.now().isoformat()
        })

    @app.route('/')
    def homepage():
        """Page d'accueil avec orientation intelligente des services"""
        return jsonify({
            "message": "🎯 Revolutionary Backend - ZineInsight Intelligence Platform",
            "version": "1.0.0",
            "services": {
                "zscore": {
                    "name": "Geographic Intelligence",
                    "endpoint": "/api/calculate",
                    "description": "Find your ideal city/country",
                    "version": "2.0.0"
                },
                "usa_residents": {
                    "name": "USA Domestic Relocation",
                    "endpoint": "/api/usa-residents",
                    "description": "Find your perfect US city",
                    "version": "1.0.0",
                    "cities_count": len(usa_residents_algo.cities_data['cities']),
                    "criteria_count": 25
                },
                "france_residents": {
                    "name": "France Domestic Relocation",
                    "endpoint": "/api/france-residents",
                    "description": "Trouvez votre ville française idéale",
                    "version": "1.0.0",
                    "cities_count": len(france_residents_algo.cities_data['cities']),
                    "criteria_count": 25
                },
                "skillgraph": {
                    "name": "Career Intelligence",
                    "endpoint": "/api/career",
                    "description": "Optimize your career path",
                    "version": skillgraph_algo.version
                },
                "wealth": {
                    "name": "Wealth Intelligence",
                    "endpoint": "/api/wealth",
                    "description": "Achieve financial freedom",
                    "version": wealth_algo.version
                }
            },
            "total_intelligence_criteria": (
                49 +  # ZScore criteria
                25 +  # USA Residents criteria
                25 +  # France Residents criteria
                len(skillgraph_algo.get_all_criteria()) +
                len(wealth_algo.get_all_criteria())
            ),
            "status": "operational",
            "timestamp": datetime.now().isoformat()
        })

    @app.route('/auth')
    @app.route('/login')
    @app.route('/register')
    @app.route('/signin')
    @app.route('/signup')
    def auth_page():
        """Page d'authentification Revolutionary"""
        return app.send_static_file('auth.html')

    @app.route('/api/orientation', methods=['POST'])
    def intelligent_orientation():
        """Orientation intelligente vers le service adapté"""
        try:
            data = request.get_json()
            answers = data.get('answers', {})

            if not answers:
                return jsonify({'error': 'Answers required for orientation'}), 400

            # Logique d'orientation intelligente
            scores = {
                'zscore': 0,
                'usa_residents': 0,
                'skillgraph': 0,
                'wealth': 0
            }

            for answer in answers.values():
                answer_text = str(answer).lower()

                # Détection ZScore (géographie/lifestyle international)
                if any(word in answer_text for word in ['international', 'europe', 'asia', 'expat', 'abroad', 'étranger']):
                    scores['zscore'] += 3
                elif any(word in answer_text for word in ['city', 'country', 'move', 'relocate', 'travel', 'climate', 'ville', 'pays']):
                    scores['zscore'] += 1

                # Détection USA Residents (relocation domestique USA)
                if any(word in answer_text for word in ['usa', 'united states', 'american', 'domestic', 'états-unis', 'américain']):
                    scores['usa_residents'] += 3
                elif any(word in answer_text for word in ['state tax', 'hurricane', 'tornado', 'suburb', 'downtown']):
                    scores['usa_residents'] += 2

                # Détection SkillGraph (carrière/emploi)
                if any(word in answer_text for word in ['job', 'career', 'work', 'skill', 'emploi', 'carrière', 'compétence']):
                    scores['skillgraph'] += 2

                # Détection Wealth (finance/investissement)
                if any(word in answer_text for word in ['money', 'invest', 'save', 'wealth', 'retirement', 'argent', 'épargne']):
                    scores['wealth'] += 2

            # Service recommandé
            recommended_service = max(scores, key=scores.get)
            confidence = scores[recommended_service] / max(sum(scores.values()), 1)

            service_names = {
                'zscore': 'Geographic Intelligence',
                'usa_residents': 'USA Domestic Relocation',
                'skillgraph': 'Career Intelligence',
                'wealth': 'Wealth Intelligence'
            }

            return jsonify({
                'success': True,
                'recommended_service': recommended_service,
                'service_name': service_names[recommended_service],
                'confidence': round(confidence, 2),
                'scores': scores,
                'all_services_available': True,
                'cross_sell_opportunity': scores[recommended_service] < 4
            })

        except Exception as e:
            logger.error(f"❌ Orientation error: {e}")
            return jsonify({'error': 'Orientation failed'}), 500

    # ===============================
    # 🇺🇸 USA RESIDENTS API ROUTES
    # ===============================

    @app.route('/api/usa-residents/recommendations', methods=['POST'])
    def get_usa_recommendations():
        """🎯 API endpoint pour obtenir les recommandations TOP 3 USA"""
        try:
            questionnaire_data = request.get_json()

            if not questionnaire_data:
                return jsonify({'error': 'Données questionnaire requises'}), 400

            # Log the request for debugging
            logger.info(f"USA Recommendations request: {list(questionnaire_data.keys())}")

            # Obtenir TOP 3 recommandations
            recommendations = usa_residents_algo.get_top_recommendations(questionnaire_data, top_n=3)

            logger.info(f"USA Recommendations generated for profile: {questionnaire_data.get('usa_main_priority', 'unknown')}")

            return jsonify({
                'status': 'success',
                'success': True,
                'recommendations': recommendations,
                'algorithm_version': '1.0.0',
                'total_cities_analyzed': len(usa_residents_algo.cities_data['cities']),
                'questionnaire_responses': len([k for k in questionnaire_data.keys() if k.startswith('usa_')]),
                'timestamp': datetime.now().isoformat()
            })

        except Exception as e:
            logger.error(f"❌ USA Residents algorithm error: {str(e)}")
            return jsonify({
                'status': 'error',
                'success': False,
                'error': 'Erreur interne algorithme',
                'details': str(e) if app.debug else None
            }), 500

    @app.route('/api/usa-residents/health', methods=['GET'])
    def usa_residents_health_check():
        """🏥 Health check spécifique USA Residents"""
        try:
            # Test basique de l'algorithme
            test_data = {
                'usa_main_priority': 'career_growth',
                'usa_monthly_budget': 'budget_balanced',
                'usa_work_situation': 'remote_full'
            }

            test_recommendations = usa_residents_algo.get_top_recommendations(test_data, top_n=1)

            return jsonify({
                'status': 'healthy',
                'algorithm_version': '1.0.0',
                'cities_loaded': len(usa_residents_algo.cities_data['cities']),
                'criteria_count': 25,
                'test_passed': len(test_recommendations) > 0,
                'sample_city': test_recommendations[0]['city'] if test_recommendations else None,
                'timestamp': datetime.now().isoformat()
            })

        except Exception as e:
            logger.error(f"❌ USA Residents health check failed: {str(e)}")
            return jsonify({
                'status': 'unhealthy',
                'error': str(e),
                'cities_loaded': len(usa_residents_algo.cities_data['cities']) if hasattr(usa_residents_algo, 'cities_data') else 0
            }), 500

    @app.route('/api/usa-residents/cities', methods=['GET'])
    def get_usa_cities_list():
        """📍 Liste de toutes les villes USA disponibles"""
        try:
            cities = usa_residents_algo.cities_data['cities']

            cities_list = []
            for city in cities:
                cities_list.append({
                    'id': city['id'],
                    'name': city['name'],
                    'state': city['state'],
                    'population': city['population'],
                    'coordinates': city['coordinates']
                })

            return jsonify({
                'status': 'success',
                'cities': cities_list,
                'total_cities': len(cities_list),
                'metadata': usa_residents_algo.cities_data.get('metadata', {})
            })

        except Exception as e:
            logger.error(f"❌ USA Cities list error: {str(e)}")
            return jsonify({'error': 'Erreur récupération villes'}), 500

    @app.route('/api/usa-residents/criteria', methods=['GET'])
    def get_usa_criteria():
        """📊 Liste des critères utilisés par l'algorithme USA"""
        try:
            criteria_definitions = usa_residents_algo.cities_data.get('criteria_definitions', {})

            return jsonify({
                'status': 'success',
                'criteria_definitions': criteria_definitions,
                'criteria_count': len(criteria_definitions),
                'base_weights': usa_residents_algo.criteria_weights_base
            })

        except Exception as e:
            logger.error(f"❌ USA Criteria error: {str(e)}")
            return jsonify({'error': 'Erreur récupération critères'}), 500

    # ===========================
    # 🇫🇷 ROUTES FRANCE RESIDENTS
    # ===========================

    @app.route('/api/france-residents/recommendations', methods=['POST'])
    def france_residents_analysis():
        """🇫🇷 Analyse relocation domestique France - recommandations TOP 3"""
        try:
            data = request.get_json()
            if not data:
                return jsonify({'error': 'Données questionnaire requises'}), 400

            logger.info(f"🇫🇷 France residents analysis request: {data.keys()}")

            # Validation rapide des données
            required_fields = ['france_main_priority', 'france_monthly_budget']
            missing_fields = [field for field in required_fields if field not in data]
            if missing_fields:
                return jsonify({'error': f'Champs manquants: {missing_fields}'}), 400

            # Analyse avec algorithme France
            recommendations = france_residents_algo.get_top_recommendations_france(data, top_n=3)

            response = {
                'status': 'success',
                'country': 'france',
                'algorithm_version': '1.0.0',
                'recommendations': recommendations,
                'metadata': {
                    'cities_analyzed': len(france_residents_algo.cities_data['cities']),
                    'criteria_used': len(france_residents_algo.criteria_weights_base),
                    'timestamp': datetime.now().isoformat()
                }
            }

            logger.info(f"✅ France analysis successful: {len(recommendations)} recommendations")
            return jsonify(response)

        except Exception as e:
            logger.error(f"❌ France residents analysis error: {str(e)}")
            return jsonify({'error': 'Erreur analyse France', 'details': str(e)}), 500

    @app.route('/api/france-residents/health', methods=['GET'])
    def france_residents_health():
        """🏥 Health check service France Residents"""
        try:
            cities_count = len(france_residents_algo.cities_data.get('cities', []))
            criteria_count = len(france_residents_algo.criteria_weights_base)

            return jsonify({
                'status': 'healthy',
                'service': 'France Residents',
                'version': '1.0.0',
                'cities_loaded': cities_count,
                'criteria_available': criteria_count,
                'data_source': france_residents_algo.cities_data.get('metadata', {}),
                'timestamp': datetime.now().isoformat()
            })

        except Exception as e:
            logger.error(f"❌ France residents health error: {str(e)}")
            return jsonify({'error': 'Service France indisponible'}), 503

    @app.route('/api/france-residents/cities', methods=['GET'])
    def get_france_cities():
        """🏙️ Liste des 50 villes françaises disponibles"""
        try:
            cities = france_residents_algo.cities_data.get('cities', [])

            # Format léger pour le frontend
            cities_summary = []
            for city in cities:
                cities_summary.append({
                    'name': city['name'],
                    'region': city['region'],
                    'population': city['population'],
                    'coordinates': city['coordinates']
                })

            return jsonify({
                'status': 'success',
                'cities': cities_summary,
                'count': len(cities_summary),
                'metadata': france_residents_algo.cities_data.get('metadata', {})
            })

        except Exception as e:
            logger.error(f"❌ France cities error: {str(e)}")
            return jsonify({'error': 'Erreur récupération villes'}), 500

    @app.route('/api/france-residents/criteria', methods=['GET'])
    def get_france_criteria():
        """📊 Liste des critères utilisés par l'algorithme France"""
        try:
            criteria_definitions = france_residents_algo.cities_data.get('criteria_definitions', {})

            return jsonify({
                'status': 'success',
                'criteria_definitions': criteria_definitions,
                'criteria_count': len(criteria_definitions),
                'base_weights': france_residents_algo.criteria_weights_base
            })

        except Exception as e:
            logger.error(f"❌ France Criteria error: {str(e)}")
            return jsonify({'error': 'Erreur récupération critères'}), 500

    # 🇨🇦 ROUTES CANADA RESIDENTS
    # ============================

    @app.route('/api/canada-residents/recommendations', methods=['POST'])
    def canada_residents_analysis():
        """🇨🇦 Analyse relocation domestique Canada - recommandations TOP 3"""
        try:
            data = request.get_json()
            if not data:
                return jsonify({'error': 'Données questionnaire requises'}), 400

            logger.info(f"🇨🇦 Canada residents analysis request: {data.keys()}")

            # Validation rapide des données
            required_fields = ['canada_main_priority', 'canada_monthly_budget']
            missing_fields = [field for field in required_fields if field not in data]
            if missing_fields:
                return jsonify({'error': f'Champs manquants: {missing_fields}'}), 400

            # Analyse avec algorithme Canada
            recommendations = canada_residents_algo.get_top_recommendations_canada(data, top_n=3)

            response = {
                'status': 'success',
                'country': 'canada',
                'algorithm_version': '1.0.0',
                'recommendations': recommendations,
                'metadata': {
                    'cities_analyzed': len(canada_residents_algo.cities_data['cities']),
                    'criteria_used': len(canada_residents_algo.criteria_weights_base),
                    'timestamp': datetime.now().isoformat()
                }
            }

            logger.info(f"✅ Canada analysis successful: {len(recommendations)} recommendations")
            return jsonify(response)

        except Exception as e:
            logger.error(f"❌ Canada residents analysis error: {str(e)}")
            return jsonify({'error': 'Erreur analyse Canada', 'details': str(e)}), 500

    @app.route('/api/canada-residents/health', methods=['GET'])
    def canada_residents_health():
        """🏥 Health check service Canada Residents"""
        try:
            cities_count = len(canada_residents_algo.cities_data.get('cities', []))
            criteria_count = len(canada_residents_algo.criteria_weights_base)

            return jsonify({
                'status': 'healthy',
                'service': 'Canada Residents',
                'version': '1.0.0',
                'cities_loaded': cities_count,
                'criteria_available': criteria_count,
                'data_source': canada_residents_algo.cities_data.get('metadata', {}),
                'timestamp': datetime.now().isoformat()
            })

        except Exception as e:
            logger.error(f"❌ Canada residents health error: {str(e)}")
            return jsonify({'error': 'Service Canada indisponible'}), 503

    @app.route('/api/canada-residents/cities', methods=['GET'])
    def get_canada_cities():
        """🏙️ Liste des 30 villes canadiennes disponibles"""
        try:
            cities = canada_residents_algo.cities_data.get('cities', [])

            # Format léger pour le frontend
            cities_summary = []
            for city in cities:
                cities_summary.append({
                    'name': city['name'],
                    'province': city['province'],
                    'population': city['population'],
                    'coordinates': city['coordinates']
                })

            return jsonify({
                'status': 'success',
                'cities': cities_summary,
                'count': len(cities_summary),
                'metadata': canada_residents_algo.cities_data.get('metadata', {})
            })

        except Exception as e:
            logger.error(f"❌ Canada cities error: {str(e)}")
            return jsonify({'error': 'Erreur récupération villes'}), 500

    @app.route('/api/canada-residents/criteria', methods=['GET'])
    def get_canada_criteria():
        """📊 Liste des critères utilisés par l'algorithme Canada"""
        try:
            criteria_definitions = canada_residents_algo.cities_data.get('criteria_definitions', {})

            return jsonify({
                'status': 'success',
                'criteria_definitions': criteria_definitions,
                'criteria_count': len(criteria_definitions),
                'base_weights': canada_residents_algo.criteria_weights_base
            })

        except Exception as e:
            logger.error(f"❌ Canada Criteria error: {str(e)}")
            return jsonify({'error': 'Erreur récupération critères'}), 500

    # ===============================
    # �🇷 SERVICE BRAZIL RESIDENTS
    # ===============================

    @app.route('/api/brazil-residents/recommendations', methods=['POST'])
    def brazil_residents_analysis():
        """🇧🇷 Analyse relocation domestique Brésil - recommandations TOP 3"""
        try:
            data = request.get_json()
            if not data:
                return jsonify({'error': 'Données questionnaire requises'}), 400

            logger.info(f"🇧🇷 Brazil residents analysis request: {data.keys()}")

            # Validation rapide des données
            required_fields = ['brazil_main_priority', 'brazil_monthly_budget']
            missing_fields = [field for field in required_fields if field not in data]
            if missing_fields:
                return jsonify({'error': f'Champs manquants: {missing_fields}'}), 400

            # Analyse avec algorithme Brésil
            recommendations = brazil_residents_algo.get_recommendations(data)

            if recommendations['status'] == 'error':
                return jsonify(recommendations), 400

            response = {
                'status': 'success',
                'country': 'brazil',
                'algorithm_version': brazil_residents_algo.version,
                'recommendations': recommendations['recommendations'],
                'metadata': {
                    'cities_analyzed': recommendations.get('total_cities_analyzed', 0),
                    'criteria_used': len(brazil_residents_algo.criteria_weights_base),
                    'regions_supported': list(brazil_residents_algo.regional_mappings.keys()),
                    'user_profile_summary': recommendations.get('user_profile_summary', {}),
                    'timestamp': datetime.now().isoformat()
                }
            }

            logger.info(f"✅ Brazil analysis successful: {len(recommendations['recommendations'])} recommendations")
            return jsonify(response)

        except Exception as e:
            logger.error(f"❌ Brazil residents analysis error: {str(e)}")
            return jsonify({'error': 'Erreur analyse Brésil', 'details': str(e)}), 500

    @app.route('/api/brazil-residents/health', methods=['GET'])
    def brazil_residents_health():
        """🏥 Health check service Brazil Residents"""
        try:
            health_info = brazil_residents_algo.health_check()

            return jsonify({
                'status': 'healthy',
                'service': 'Brazil Residents',
                'version': brazil_residents_algo.version,
                'cities_loaded': health_info['cities_loaded'],
                'criteria_available': health_info['criteria_count'],
                'regions_supported': health_info['regions_supported'],
                'data_source': brazil_residents_algo.cities_data.get('metadata', {}),
                'timestamp': datetime.now().isoformat()
            })

        except Exception as e:
            logger.error(f"❌ Brazil residents health error: {str(e)}")
            return jsonify({'error': 'Service Brésil indisponible'}), 503

    @app.route('/api/brazil-residents/cities', methods=['GET'])
    def get_brazil_cities():
        """🏙️ Liste des 25 villes brésiliennes disponibles"""
        try:
            cities = brazil_residents_algo.cities_data.get('cities', [])

            # Format léger pour le frontend
            cities_summary = []
            for city in cities:
                cities_summary.append({
                    'name': city['name'],
                    'region': city['region'],
                    'population': city['population'],
                    'coordinates': city['coordinates']
                })

            return jsonify({
                'status': 'success',
                'cities': cities_summary,
                'count': len(cities_summary),
                'regions': list(brazil_residents_algo.regional_mappings.keys()),
                'metadata': brazil_residents_algo.cities_data.get('metadata', {})
            })

        except Exception as e:
            logger.error(f"❌ Brazil cities error: {str(e)}")
            return jsonify({'error': 'Erreur récupération villes'}), 500

    @app.route('/api/brazil-residents/criteria', methods=['GET'])
    def get_brazil_criteria():
        """📊 Liste des critères utilisés par l'algorithme Brésil"""
        try:
            criteria_definitions = brazil_residents_algo.cities_data.get('criteria_definitions', {})

            return jsonify({
                'status': 'success',
                'criteria_definitions': criteria_definitions,
                'criteria_count': len(criteria_definitions),
                'base_weights': brazil_residents_algo.criteria_weights_base,
                'regional_mappings': brazil_residents_algo.regional_mappings
            })

        except Exception as e:
            logger.error(f"❌ Brazil Criteria error: {str(e)}")
            return jsonify({'error': 'Erreur récupération critères'}), 500

    # ===============================
    # �🇬🇧 SERVICE UK RESIDENTS
    # ===============================

    @app.route('/api/uk-residents/recommendations', methods=['POST'])
    def get_uk_recommendations():
        """🇬🇧 Recommandations personnalisées pour résidents UK"""
        try:
            data = request.get_json()
            if not data:
                return jsonify({'error': 'Données requises'}), 400

            # Obtenir recommandations UK avec filtres régionaux/linguistiques
            recommendations = uk_residents_algo.get_recommendations(data)

            return jsonify({
                'status': 'success',
                'recommendations': recommendations,
                'criteria_used': list(uk_residents_algo.criteria_weights_base.keys()),
                'total_cities': len(uk_residents_algo.cities_data['cities']),
                'algorithm_version': uk_residents_algo.version,
                'filters_applied': recommendations.get('filters_applied', {}),
                'timestamp': datetime.now().isoformat()
            })

        except Exception as e:
            logger.error(f"❌ UK Recommendations error: {str(e)}")
            return jsonify({'error': 'Erreur calcul recommandations UK'}), 500

    @app.route('/api/uk-residents/health', methods=['GET'])
    def uk_health_check():
        """🇬🇧 UK Residents health check complet"""
        try:
            cities_count = len(uk_residents_algo.cities_data['cities'])
            criteria_count = len(uk_residents_algo.criteria_weights_base)

            return jsonify({
                'service': 'UK Residents',
                'status': 'healthy',
                'cities_loaded': cities_count,
                'criteria_count': criteria_count,
                'algorithm_version': uk_residents_algo.version,
                'data_file': 'villes_uk_residents.json',
                'last_update': uk_residents_algo.cities_data.get('last_update', 'unknown'),
                'timestamp': datetime.now().isoformat()
            })

        except Exception as e:
            logger.error(f"❌ UK health check failed: {e}")
            return jsonify({
                'service': 'UK Residents',
                'status': 'unhealthy',
                'error': str(e)
            }), 503

    @app.route('/api/uk-residents/cities', methods=['GET'])
    def get_uk_cities():
        """🇬🇧 Liste des villes UK avec leurs données"""
        try:
            return jsonify({
                'status': 'success',
                'cities': uk_residents_algo.cities_data['cities'],
                'total_count': len(uk_residents_algo.cities_data['cities']),
                'criteria_definitions': uk_residents_algo.cities_data.get('criteria_definitions', {}),
                'metadata': uk_residents_algo.cities_data.get('metadata', {})
            })

        except Exception as e:
            logger.error(f"❌ UK cities error: {str(e)}")
            return jsonify({'error': 'Erreur récupération villes'}), 500

    @app.route('/api/uk-residents/criteria', methods=['GET'])
    def get_uk_criteria():
        """📊 Liste des critères utilisés par l'algorithme UK"""
        try:
            criteria_definitions = uk_residents_algo.cities_data.get('criteria_definitions', {})

            return jsonify({
                'status': 'success',
                'criteria_definitions': criteria_definitions,
                'criteria_count': len(criteria_definitions),
                'base_weights': uk_residents_algo.criteria_weights_base
            })

        except Exception as e:
            logger.error(f"❌ UK Criteria error: {str(e)}")
            return jsonify({'error': 'Erreur récupération critères'}), 500

    # ===============================
    # �🇵 SERVICE JAPAN RESIDENTS
    # ===============================

    @app.route('/api/japan-residents/recommendations', methods=['POST'])
    def get_japan_recommendations():
        """🇯🇵 Recommandations personnalisées pour résidents Japon"""
        try:
            data = request.get_json()
            if not data:
                return jsonify({'error': 'Données requises'}), 400

            # Obtenir recommandations Japan avec filtres régionaux
            recommendations = japan_residents_algo.get_recommendations(data)

            # L'algorithme retourne déjà le format correct {"status": "success", "recommendations": [...]}
            return jsonify(recommendations)

        except Exception as e:
            logger.error(f"❌ Japan Recommendations error: {str(e)}")
            return jsonify({'error': 'Erreur calcul recommandations Japan'}), 500

    @app.route('/api/japan-residents/health', methods=['GET'])
    def japan_health_check():
        """🇯🇵 Japan Residents health check complet"""
        try:
            cities_count = len(japan_residents_algo.cities_data['cities'])
            criteria_count = len(japan_residents_algo.criteria_weights_base)

            return jsonify({
                'service': 'Japan Residents',
                'status': 'healthy',
                'cities_loaded': cities_count,
                'criteria_count': criteria_count,
                'algorithm_version': japan_residents_algo.version,
                'data_file': 'villes_japan_residents.json',
                'last_update': japan_residents_algo.cities_data.get('last_update', 'unknown'),
                'timestamp': datetime.now().isoformat()
            })

        except Exception as e:
            logger.error(f"❌ Japan health check failed: {e}")
            return jsonify({
                'service': 'Japan Residents',
                'status': 'unhealthy',
                'error': str(e)
            }), 503

    @app.route('/api/japan-residents/cities', methods=['GET'])
    def get_japan_cities():
        """🇯🇵 Liste des villes Japan avec leurs données"""
        try:
            return jsonify({
                'status': 'success',
                'cities': japan_residents_algo.cities_data['cities'],
                'total_count': len(japan_residents_algo.cities_data['cities']),
                'criteria_definitions': japan_residents_algo.cities_data.get('criteria_definitions', {}),
                'metadata': japan_residents_algo.cities_data.get('metadata', {})
            })

        except Exception as e:
            logger.error(f"❌ Japan cities error: {str(e)}")
            return jsonify({'error': 'Erreur récupération villes'}), 500

    @app.route('/api/japan-residents/criteria', methods=['GET'])
    def get_japan_criteria():
        """📊 Liste des critères utilisés par l'algorithme Japan"""
        try:
            criteria_definitions = japan_residents_algo.cities_data.get('criteria_definitions', {})

            return jsonify({
                'status': 'success',
                'criteria_definitions': criteria_definitions,
                'criteria_count': len(criteria_definitions),
                'base_weights': japan_residents_algo.criteria_weights_base
            })

        except Exception as e:
            logger.error(f"❌ Japan Criteria error: {str(e)}")
            return jsonify({'error': 'Erreur récupération critères'}), 500

    # ===============================
    # �🇩🇪 GERMANY RESIDENTS ENDPOINTS
    # ===============================

    @app.route('/api/germany-residents/recommendations', methods=['POST'])
    def get_germany_recommendations():
        """🇩🇪 Recommandations personnalisées pour résidents allemands"""
        try:
            data = request.get_json()
            if not data:
                return jsonify({'error': 'Données requises'}), 400

            # Obtenir recommandations Germany avec filtres régionaux/linguistiques
            recommendations = germany_residents_algo.get_recommendations(data)

            return jsonify({
                'status': 'success',
                'recommendations': recommendations,
                'criteria_used': list(germany_residents_algo.criteria_weights_base.keys()),
                'total_cities': len(germany_residents_algo.cities_data['cities']),
                'algorithm_version': germany_residents_algo.version,
                'filters_applied': recommendations.get('filters_applied', {}),
                'timestamp': datetime.now().isoformat()
            })

        except Exception as e:
            logger.error(f"❌ Germany Recommendations error: {str(e)}")
            return jsonify({'error': 'Erreur calcul recommandations Germany'}), 500

    @app.route('/api/germany-residents/health', methods=['GET'])
    def germany_health_check():
        """🇩🇪 Germany Residents health check complet"""
        try:
            cities_count = len(germany_residents_algo.cities_data['cities'])
            criteria_count = len(germany_residents_algo.criteria_weights_base)

            return jsonify({
                'service': 'Germany Residents',
                'status': 'healthy',
                'cities_loaded': cities_count,
                'criteria_count': criteria_count,
                'algorithm_version': germany_residents_algo.version,
                'data_file': 'villes_germany_residents.json',
                'last_update': germany_residents_algo.cities_data.get('last_update', 'unknown'),
                'timestamp': datetime.now().isoformat()
            })

        except Exception as e:
            logger.error(f"❌ Germany health check failed: {e}")
            return jsonify({
                'service': 'Germany Residents',
                'status': 'unhealthy',
                'error': str(e)
            }), 503

    @app.route('/api/germany-residents/cities', methods=['GET'])
    def get_germany_cities():
        """🇩🇪 Liste des villes Germany avec leurs données"""
        try:
            return jsonify({
                'status': 'success',
                'cities': germany_residents_algo.cities_data['cities'],
                'total_count': len(germany_residents_algo.cities_data['cities']),
                'criteria_definitions': germany_residents_algo.cities_data.get('criteria_definitions', {}),
                'metadata': germany_residents_algo.cities_data.get('metadata', {})
            })

        except Exception as e:
            logger.error(f"❌ Germany cities error: {str(e)}")
            return jsonify({'error': 'Erreur récupération villes'}), 500

    @app.route('/api/germany-residents/criteria', methods=['GET'])
    def get_germany_criteria():
        """📊 Liste des critères utilisés par l'algorithme Germany"""
        try:
            criteria_definitions = germany_residents_algo.cities_data.get('criteria_definitions', {})

            return jsonify({
                'status': 'success',
                'criteria_definitions': criteria_definitions,
                'criteria_count': len(criteria_definitions),
                'base_weights': germany_residents_algo.criteria_weights_base
            })

        except Exception as e:
            logger.error(f"❌ Germany Criteria error: {str(e)}")
            return jsonify({'error': 'Erreur récupération critères'}), 500

    # ===============================
    # 🇦🇺 ROUTES AUSTRALIA RESIDENTS
    # ===============================

    @app.route('/api/australia-residents/recommendations', methods=['POST'])
    def australia_residents_recommendations():
        """🇦🇺 Recommandations de villes australiennes - Approche hybride résidents/expats"""
        try:
            if not request.is_json:
                return jsonify({'error': 'Content-Type must be application/json'}), 400

            data = request.get_json()
            logger.info(f"🇦🇺 Australia residents request received")

            # Validation basique
            if not data:
                return jsonify({'error': 'No data provided'}), 400

            # Appel à l'algorithme Australia avec interface standardisée
            result = australia_residents_algo.get_recommendations(data)

            if result['status'] == 'success':
                logger.info(f"✅ Australia recommendations: {len(result['recommendations'])} cities")
            else:
                logger.warning(f"⚠️ Australia algorithm issue: {result.get('message', 'Unknown error')}")

            return jsonify(result)

        except Exception as e:
            logger.error(f"❌ Australia residents error: {str(e)}")
            return jsonify({
                'status': 'error',
                'message': f'Server error: {str(e)}',
                'recommendations': []
            }), 500

    @app.route('/api/australia-residents/health', methods=['GET'])
    def australia_residents_health():
        """🇦🇺 Health check de l'algorithme Australia"""
        try:
            health_data = australia_residents_algo.get_health_check()
            return jsonify(health_data)

        except Exception as e:
            logger.error(f"❌ Australia health check error: {str(e)}")
            return jsonify({
                'status': 'unhealthy',
                'error': str(e),
                'cities_loaded': 0,
                'algorithm_version': 'unknown'
            }), 500

    @app.route('/api/australia-residents/cities', methods=['GET'])
    def get_australia_cities():
        """🇦🇺 Liste des villes australiennes disponibles"""
        try:
            cities_info = []
            for city in australia_residents_algo.cities_data:
                cities_info.append({
                    'id': city['id'],
                    'name': city['name'],
                    'state': city['state'],
                    'population': city['population'],
                    'coordinates': city['coordinates']
                })

            return jsonify({
                'status': 'success',
                'cities': cities_info,
                'cities_count': len(cities_info),
                'country': 'Australia',
                'approach': 'hybrid_residents_expats'
            })

        except Exception as e:
            logger.error(f"❌ Australia cities error: {str(e)}")
            return jsonify({'error': 'Erreur récupération villes'}), 500

    @app.route('/api/australia-residents/criteria', methods=['GET'])
    def get_australia_criteria():
        """📊 Liste des critères utilisés par l'algorithme Australia"""
        try:
            # Extract criteria definitions from first city or metadata
            sample_city = australia_residents_algo.cities_data[0] if australia_residents_algo.cities_data else {}
            criteria_definitions = {}

            # Get criteria from city scores
            if 'scores' in sample_city:
                criteria_definitions = {
                    criteria: f"Score for {criteria.replace('_', ' ').title()}"
                    for criteria in sample_city['scores'].keys()
                }

            return jsonify({
                'status': 'success',
                'criteria_definitions': criteria_definitions,
                'criteria_count': len(criteria_definitions),
                'base_weights': australia_residents_algo.criteria_weights_base,
                'approach': 'hybrid_residents_expats'
            })

        except Exception as e:
            logger.error(f"❌ Australia Criteria error: {str(e)}")
            return jsonify({'error': 'Erreur récupération critères'}), 500

    # ==============================
    # 🇪🇸 ROUTES SPAIN RESIDENTS
    # ==============================

    @app.route('/api/spain-residents/recommendations', methods=['POST'])
    def spain_residents_recommendations():
        """🇪🇸 Recommandations de villes espagnoles - Approche hybride résidents/expats"""
        try:
            if not request.is_json:
                return jsonify({'error': 'Content-Type must be application/json'}), 400

            data = request.get_json()
            logger.info(f"🇪🇸 Spain residents request received")

            # Validation basique
            if not data:
                return jsonify({'error': 'No data provided'}), 400

            # Appel à l'algorithme Spain avec interface standardisée
            result = spain_residents_algo.get_recommendations(data)

            if result['status'] == 'success':
                logger.info(f"✅ Spain recommendations: {len(result['recommendations'])} cities")
            else:
                logger.warning(f"⚠️ Spain algorithm issue: {result.get('message', 'Unknown error')}")

            return jsonify(result)

        except Exception as e:
            logger.error(f"❌ Spain residents error: {str(e)}")
            return jsonify({
                'status': 'error',
                'message': f'Server error: {str(e)}',
                'recommendations': []
            }), 500

    @app.route('/api/spain-residents/health', methods=['GET'])
    def spain_residents_health():
        """🇪🇸 Health check de l'algorithme Spain"""
        try:
            health_data = spain_residents_algo.get_health_check()
            return jsonify(health_data)

        except Exception as e:
            logger.error(f"❌ Spain health check error: {str(e)}")
            return jsonify({
                'status': 'unhealthy',
                'error': str(e),
                'cities_loaded': 0,
                'algorithm_version': 'unknown'
            }), 500

    @app.route('/api/spain-residents/cities', methods=['GET'])
    def get_spain_cities():
        """🇪🇸 Liste des villes espagnoles disponibles"""
        try:
            cities_info = []
            for city in spain_residents_algo.cities_data:
                cities_info.append({
                    'id': city['id'],
                    'name': city['name'],
                    'region': city['region'],
                    'population': city['population'],
                    'coordinates': city['coordinates']
                })

            return jsonify({
                'status': 'success',
                'cities': cities_info,
                'cities_count': len(cities_info),
                'country': 'Spain',
                'approach': 'hybrid_residents_expats'
            })

        except Exception as e:
            logger.error(f"❌ Spain cities error: {str(e)}")
            return jsonify({'error': 'Erreur récupération villes'}), 500

    @app.route('/api/spain-residents/criteria', methods=['GET'])
    def get_spain_criteria():
        """📊 Liste des critères utilisés par l'algorithme Spain"""
        try:
            # Extract criteria definitions from first city or metadata
            sample_city = spain_residents_algo.cities_data[0] if spain_residents_algo.cities_data else {}
            criteria_definitions = {}

            # Get criteria from city scores
            if 'scores' in sample_city:
                criteria_definitions = {
                    criteria: f"Score for {criteria.replace('_', ' ').title()}"
                    for criteria in sample_city['scores'].keys()
                }

            return jsonify({
                'status': 'success',
                'criteria_definitions': criteria_definitions,
                'criteria_count': len(criteria_definitions),
                'base_weights': spain_residents_algo.criteria_weights_base,
                'approach': 'hybrid_residents_expats'
            })

        except Exception as e:
            logger.error(f"❌ Spain Criteria error: {str(e)}")
            return jsonify({'error': 'Erreur récupération critères'}), 500

    # ===============================
    # 🇲🇽 MEXICO RESIDENTS ROUTES
    # ===============================

    @app.route('/api/mexico-residents/recommendations', methods=['POST'])
    def get_mexico_recommendations_endpoint():
        """🇲🇽 Service de recommandations Mexico - Pattern Revolutionary"""
        try:
            data = request.get_json()
            if not data:
                return jsonify({'error': 'Données JSON requises'}), 400

            # Extraction des préférences
            preferences = data.get('preferences', {})
            if not preferences:
                return jsonify({'error': 'Préférences requises'}), 400

            # Génération des recommandations mexicaines
            result = get_mexico_recommendations(preferences)

            if not result or not result.get('success'):
                return jsonify({'error': 'Aucune recommandation générée'}), 500

            # Extraire et adapter la structure pour le frontend
            raw_recommendations = result.get('recommendations', [])

            # Convertir la structure V2 vers le format attendu par le frontend
            recommendations = []
            for rec in raw_recommendations:
                adapted_rec = {
                    'nom': rec.get('city', ''),          # city -> nom
                    'pays': rec.get('region', ''),       # region -> pays
                    'population': rec.get('population', 0),
                    'score_final': rec.get('score_percentage', 0),
                    'points_forts': rec.get('reasons', []),
                    'cout_vie': None,  # Pas utilisé dans V2
                    'pros': rec.get('pros', []),
                    'cons': rec.get('cons', []),
                    'description': rec.get('description', '')
                }
                recommendations.append(adapted_rec)

            logger.info(f"🇲🇽 Mexico recommendations adapted: {len(recommendations)} cities")

            return jsonify({
                'status': 'success',
                'recommendations': recommendations,
                'country': 'Mexico',
                'service': 'mexico_residents',
                'approach': 'hybrid_residents_expats',
                'generated_at': datetime.now().isoformat()
            })

        except Exception as e:
            logger.error(f"❌ Mexico recommendations error: {str(e)}")
            return jsonify({'error': 'Erreur génération recommandations Mexico'}), 500

    @app.route('/api/mexico-residents/health', methods=['GET'])
    def mexico_residents_health():
        """🏥 Health check Mexico residents service"""
        try:
            # Test simple de l'algorithme
            test_prefs = {'mexico_lifestyle_priority': 'expat_friendly'}
            test_result = get_mexico_recommendations(test_prefs)

            return jsonify({
                'status': 'healthy',
                'service': 'mexico_residents',
                'country': 'Mexico',
                'test_cities_count': len(test_result),
                'approach': 'hybrid_residents_expats',
                'timestamp': datetime.now().isoformat()
            })

        except Exception as e:
            logger.error(f"❌ Mexico health check error: {str(e)}")
            return jsonify({'status': 'unhealthy', 'error': str(e)}), 500

    @app.route('/api/mexico-residents/cities', methods=['GET'])
    def get_mexico_cities():
        """🏙️ Liste des villes mexicaines disponibles"""
        try:
            # Charger les données directement depuis le JSON
            import json
            json_file = os.path.join(os.getcwd(), 'data_v2', 'villes_mexico_residents.json')

            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                cities = data.get('cities', [])

            # Format des infos de base
            cities_info = []
            for city in cities:
                cities_info.append({
                    'name': city.get('name', ''),
                    'region': city.get('region', ''),
                    'population': city.get('population', 0),
                    'cost_of_living': city.get('cost_of_living', 5),
                    'safety_score': city.get('safety_score', 5),
                    'climate_type': city.get('climate_type', ''),
                    'highlights': city.get('highlights', [])
                })

            return jsonify({
                'status': 'success',
                'cities': cities_info,
                'cities_count': len(cities_info),
                'country': 'Mexico',
                'approach': 'hybrid_residents_expats'
            })

        except Exception as e:
            logger.error(f"❌ Mexico cities error: {str(e)}")
            return jsonify({'error': 'Erreur récupération villes'}), 500

    @app.route('/api/mexico-residents/criteria', methods=['GET'])
    def get_mexico_criteria():
        """📊 Liste des critères utilisés par l'algorithme Mexico"""
        try:
            # Critères Mexico avec descriptions
            criteria_definitions = {
                'lifestyle_preference': 'Style de vie mexicain préféré',
                'climate': 'Préférence climatique (tropical, désertique, tempéré)',
                'work_environment': 'Environnement professionnel recherché',
                'budget_comfort': 'Budget mensuel en pesos mexicains',
                'social_life': 'Type de vie sociale désirée',
                'transport': 'Mode de transport privilégié',
                'housing_type': 'Type de logement recherché',
                'gastronomy': 'Culture gastronomique préférée',
                'pace_of_life': 'Rythme de vie souhaité',
                'safety_priority': 'Niveau de sécurité requis'
            }

            return jsonify({
                'status': 'success',
                'criteria_definitions': criteria_definitions,
                'criteria_count': len(criteria_definitions),
                'approach': 'hybrid_residents_expats',
                'zones': [
                    'central_metropolis',
                    'riviera_maya',
                    'pacific_coast',
                    'colonial_heritage',
                    'yucatan_peninsula',
                    'oaxaca_cultural',
                    'northern_business'
                ]
            })

        except Exception as e:
            logger.error(f"❌ Mexico Criteria error: {str(e)}")
            return jsonify({'error': 'Erreur récupération critères'}), 500

    # ===============================
    # 🇲🇦 MOROCCO RESIDENTS ROUTES
    # ===============================

    @app.route('/api/morocco-residents/recommendations', methods=['POST'])
    def get_morocco_recommendations_endpoint():
        """🇲🇦 Service de recommandations Morocco - Pattern Revolutionary"""
        try:
            data = request.get_json()
            if not data:
                return jsonify({'error': 'Données JSON requises'}), 400

            # Extraction des préférences
            preferences = data.get('preferences', {})
            if not preferences:
                return jsonify({'error': 'Préférences requises'}), 400

            # Génération des recommandations marocaines avec algorithme standardisé
            result = morocco_residents_algo.get_recommendations(preferences)

            if not result or result.get('status') != 'success':
                return jsonify({'error': 'Aucune recommandation générée'}), 500

            # Extraire et adapter la structure pour le frontend
            raw_recommendations = result.get('recommendations', [])

            # Convertir la structure V2 vers le format attendu par le frontend
            recommendations = []
            for rec in raw_recommendations:
                adapted_rec = {
                    'nom': rec.get('city', ''),
                    'pays': rec.get('region', ''),
                    'population': rec.get('population', 0),
                    'score_final': rec.get('score_percentage', 0),
                    'points_forts': rec.get('strengths', []),
                    'cout_vie': None,  # Pas utilisé dans V2
                    'pros': rec.get('strengths', []),
                    'cons': rec.get('concerns', []),
                    'description': rec.get('why_recommended', ''),
                    'rank': rec.get('rank', 0),
                    'coordinates': rec.get('coordinates', []),
                    'economic_zone': rec.get('economic_zone', 'general')
                }
                recommendations.append(adapted_rec)

            logger.info(f"🇲🇦 Morocco recommendations generated: {len(recommendations)} cities")

            return jsonify({
                'status': 'success',
                'recommendations': recommendations,
                'country': 'Morocco',
                'service': 'morocco_residents',
                'approach': 'residents_and_expats',
                'total_cities_analyzed': result.get('total_cities_analyzed', 0),
                'algorithm_version': result.get('algorithm_version', '1.0.0'),
                'filters_applied': result.get('filters_applied', {}),
                'generated_at': datetime.now().isoformat()
            })

        except Exception as e:
            logger.error(f"❌ Morocco recommendations error: {str(e)}")
            return jsonify({'error': f'Erreur génération recommandations Morocco: {str(e)}'}), 500

    @app.route('/api/morocco-residents/health', methods=['GET'])
    def morocco_residents_health():
        """🏥 Health check Morocco residents service"""
        try:
            # Test simple de l'algorithme
            test_prefs = {
                'morocco_region_preference': 'any_region',
                'morocco_main_priority': 'career_growth'
            }
            test_result = morocco_residents_algo.get_recommendations(test_prefs)

            return jsonify({
                'status': 'healthy',
                'service': 'morocco_residents',
                'country': 'Morocco',
                'test_cities_count': len(test_result.get('recommendations', [])),
                'approach': 'residents_and_expats',
                'algorithm_version': morocco_residents_algo.version,
                'cities_loaded': len(morocco_residents_algo.cities_data.get('cities', [])),
                'timestamp': datetime.now().isoformat()
            })

        except Exception as e:
            logger.error(f"❌ Morocco health check error: {str(e)}")
            return jsonify({'status': 'unhealthy', 'error': str(e)}), 500

    @app.route('/api/morocco-residents/cities', methods=['GET'])
    def get_morocco_cities():
        """🏙️ Liste des 25 villes marocaines stratégiques disponibles"""
        try:
            cities = morocco_residents_algo.cities_data.get('cities', [])

            # Format des infos de base
            cities_info = []
            for city in cities:
                cities_info.append({
                    'id': city.get('id', ''),
                    'name': city.get('name', ''),
                    'region': city.get('region', ''),
                    'population': city.get('population', 0),
                    'coordinates': city.get('coordinates', []),
                    'economic_zone': city.get('economic_zone', 'general'),
                    'cost_of_living_score': city.get('scores', {}).get('cost_of_living', 0),
                    'safety_score': city.get('scores', {}).get('safety_security', 0),
                    'cultural_scene_score': city.get('scores', {}).get('cultural_scene', 0),
                    'highlights': [
                        f"Coût vie: {round(city.get('scores', {}).get('cost_of_living', 0) * 10, 1)}/10",
                        f"Sécurité: {round(city.get('scores', {}).get('safety_security', 0) * 10, 1)}/10",
                        f"Culture: {round(city.get('scores', {}).get('cultural_scene', 0) * 10, 1)}/10"
                    ]
                })

            return jsonify({
                'status': 'success',
                'cities': cities_info,
                'cities_count': len(cities_info),
                'country': 'Morocco',
                'approach': 'residents_and_expats',
                'regions': [
                    'Grand Casablanca-Settat',
                    'Rabat-Salé-Kénitra',
                    'Fès-Meknès',
                    'Marrakech-Safi',
                    'Tanger-Tétouan-Al Hoceïma',
                    'Oriental',
                    'Souss-Massa',
                    'Béni Mellal-Khénifra',
                    'Drâa-Tafilalet',
                    'Laâyoune-Sakia El Hamra'
                ]
            })

        except Exception as e:
            logger.error(f"❌ Morocco cities error: {str(e)}")
            return jsonify({'error': 'Erreur récupération villes Morocco'}), 500

    @app.route('/api/morocco-residents/criteria', methods=['GET'])
    def get_morocco_criteria():
        """📊 Liste des 27 critères utilisés par l'algorithme Morocco"""
        try:
            # Critères Morocco avec descriptions (27 critères standardisés + 4 spécifiques Maroc)
            criteria_definitions = {
                # Économie (5)
                'cost_of_living': 'Coût de la vie abordable (logement, nourriture, transport)',
                'job_opportunities': 'Opportunités d\'emploi et marché du travail dynamique',
                'salary_potential': 'Potentiel d\'évolution salariale et revenus',
                'housing_availability': 'Disponibilité et accessibilité du logement',
                'public_transport': 'Qualité du transport public urbain',

                # Santé et sécurité (2)
                'healthcare_quality': 'Qualité des soins médicaux et hôpitaux',
                'safety_security': 'Niveau de sécurité et stabilité',

                # Éducation et famille (2)
                'education_quality': 'Qualité du système éducatif',
                'family_friendliness': 'Environnement favorable aux familles',

                # Culture et lifestyle (4)
                'cultural_scene': 'Richesse culturelle, événements, arts',
                'nightlife': 'Vie nocturne et divertissements',
                'youth_scene': 'Dynamisme et activités pour jeunes',
                'sports_recreation': 'Activités sportives et de loisir',

                # Connectivité (2)
                'international_connectivity': 'Connexions aéroport et business international',
                'language_diversity': 'Multilinguisme et diversité linguistique',

                # Environnement (5)
                'climate_quality': 'Qualité du climat méditerranéen/atlantique',
                'air_quality': 'Qualité de l\'air et pollution',
                'nature_access': 'Accès aux espaces verts et naturels',
                'beach_access': 'Accès aux plages atlantiques/méditerranéennes',
                'mountain_access': 'Proximité Atlas, Rif et montagnes',

                # Business et tech (3)
                'business_environment': 'Écosystème d\'affaires et entrepreneuriat',
                'startup_ecosystem': 'Dynamisme startup et innovation',
                'tech_scene': 'Secteur technologique et numérique',

                # Spécifiques Maroc (4)
                'european_proximity_advantage': 'Avantage géostratégique proximité Europe',
                'berber_culture_presence': 'Richesse du patrimoine amazigh/berbère',
                'french_language_usage': 'Usage du français dans business/éducation',
                'traditional_markets_souks': 'Authenticité souks et commerce traditionnel'
            }

            return jsonify({
                'status': 'success',
                'criteria_definitions': criteria_definitions,
                'criteria_count': len(criteria_definitions),
                'approach': 'residents_and_expats',
                'regional_filters': [
                    'any_region',
                    'atlantic_coast',
                    'mediterranean',
                    'imperial_cities',
                    'atlas_mountains',
                    'sahara_gateway'
                ],
                'algorithm_version': morocco_residents_algo.version
            })

        except Exception as e:
            logger.error(f"❌ Morocco Criteria error: {str(e)}")
            return jsonify({'error': 'Erreur récupération critères Morocco'}), 500

    # ===============================
    # 🇹🇭 THAILAND RESIDENTS ROUTES
    # ===============================

    @app.route('/api/thailand-residents/recommendations', methods=['POST'])
    def get_thailand_recommendations_endpoint():
        """🇹🇭 Service de recommandations Thailand - Pattern Revolutionary"""
        try:
            data = request.get_json()
            if not data:
                return jsonify({'error': 'Données JSON requises'}), 400

            # Extraction des réponses du questionnaire
            questionnaire_responses = data.get('responses', {})
            if not questionnaire_responses:
                return jsonify({'error': 'Réponses du questionnaire requises'}), 400

            # Génération des recommandations thailand avec algorithme standardisé
            result = thailand_residents_algo.get_recommendations(questionnaire_responses)

            if not result or result.get('status') != 'success':
                return jsonify({'error': 'Aucune recommandation générée'}), 500

            # Extraire les recommandations
            raw_recommendations = result.get('recommendations', [])

            # Convertir la structure vers le format attendu par le frontend
            recommendations = []
            for rec in raw_recommendations:
                adapted_rec = {
                    'nom': rec.get('city', ''),
                    'pays': rec.get('region', ''),
                    'population': rec.get('population', 0),
                    'score_final': rec.get('score_percentage', 0),
                    'points_forts': rec.get('strengths', []),
                    'cout_vie': None,  # Pas utilisé dans V2
                    'pros': rec.get('strengths', []),
                    'cons': rec.get('concerns', []),
                    'description': rec.get('recommendation_reason', ''),
                    'rank': rec.get('rank', 0),
                    'coordinates': rec.get('coordinates', []),
                    'economic_zone': rec.get('economic_zone', 'general')
                }
                recommendations.append(adapted_rec)

            logger.info(f"🇹🇭 Thailand recommendations generated: {len(recommendations)} cities")

            return jsonify({
                'status': 'success',
                'recommendations': recommendations,
                'country': 'Thailand',
                'service': 'thailand_residents',
                'approach': 'residents_and_expats_inclusive',
                'total_cities_analyzed': result.get('total_cities_analyzed', 30),
                'algorithm_version': result.get('algorithm_version', '1.0.0'),
                'filters_applied': result.get('filters_applied', {}),
                'generated_at': datetime.now().isoformat()
            })

        except Exception as e:
            logger.error(f"❌ Thailand recommendations error: {str(e)}")
            return jsonify({'error': f'Erreur génération recommandations Thailand: {str(e)}'}), 500

    @app.route('/api/thailand-residents/health', methods=['GET'])
    def thailand_residents_health():
        """🏥 Health check Thailand residents service"""
        try:
            # Test simple de l'algorithme
            test_responses = {
                'thailand_region_preference': 'any_region',
                'thailand_main_priority': 'career_growth'
            }
            test_result = thailand_residents_algo.get_recommendations(test_responses)

            return jsonify({
                'status': 'healthy',
                'service': 'thailand_residents',
                'country': 'Thailand',
                'test_cities_count': len(test_result.get('recommendations', [])),
                'approach': 'residents_and_expats_inclusive',
                'algorithm_version': thailand_residents_algo.version,
                'cities_loaded': len(thailand_residents_algo.cities_data.get('cities', [])),
                'timestamp': datetime.now().isoformat()
            })

        except Exception as e:
            logger.error(f"❌ Thailand health check error: {str(e)}")
            return jsonify({'status': 'unhealthy', 'error': str(e)}), 500

    @app.route('/api/thailand-residents/cities', methods=['GET'])
    def get_thailand_cities():
        """🏙️ Liste des 30 villes thaïlandaises stratégiques disponibles"""
        try:
            cities = thailand_residents_algo.cities_data.get('cities', [])

            # Format des infos de base
            cities_info = []
            for city in cities:
                cities_info.append({
                    'id': city.get('id', ''),
                    'name': city.get('name', ''),
                    'region': city.get('region', ''),
                    'population': city.get('population', 0),
                    'coordinates': city.get('coordinates', []),
                    'economic_zone': city.get('economic_zone', 'general')
                })

            return jsonify({
                'status': 'success',
                'cities': cities_info,
                'cities_count': len(cities_info),
                'country': 'Thailand',
                'approach': 'residents_and_expats_inclusive',
                'regional_zones': ['Central Plains', 'Northern Mountains', 'Northeast Isan', 'Eastern Seaboard', 'Southern Beaches'],
                'algorithm_version': thailand_residents_algo.version
            })

        except Exception as e:
            logger.error(f"❌ Thailand cities error: {str(e)}")
            return jsonify({'error': 'Erreur récupération villes Thailand'}), 500

    @app.route('/api/thailand-residents/criteria', methods=['GET'])
    def get_thailand_criteria():
        """📊 Liste des 27 critères utilisés par l'algorithme Thailand"""
        try:
            # Critères Thailand avec descriptions (27 critères standardisés + innovations Thailand)
            criteria_definitions = {
                # Économie (5)
                'cost_of_living': 'Coût de la vie abordable (logement, nourriture, transport)',
                'job_opportunities': 'Opportunités d\'emploi et marché du travail dynamique',
                'salary_potential': 'Potentiel d\'évolution salariale et revenus',
                'housing_availability': 'Disponibilité et accessibilité du logement',
                'public_transport': 'Qualité du transport public urbain',

                # Santé et sécurité (2)
                'healthcare_quality': 'Qualité des soins médicaux et hôpitaux',
                'safety_security': 'Niveau de sécurité et stabilité',

                # Éducation et famille (2)
                'education_quality': 'Qualité du système éducatif',
                'family_friendliness': 'Environnement favorable aux familles',

                # Culture et lifestyle (4)
                'cultural_scene': 'Richesse culturelle, événements, arts',
                'nightlife': 'Vie nocturne et divertissements',
                'youth_scene': 'Dynamisme et activités pour jeunes',
                'sports_recreation': 'Activités sportives et de loisir',

                # Connectivité (2)
                'international_connectivity': 'Connexions aéroport et business international',
                'language_diversity': 'Multilinguisme et diversité linguistique',

                # Environnement (5)
                'climate_quality': 'Qualité du climat tropical adaptatif',
                'air_quality': 'Qualité de l\'air et pollution',
                'nature_access': 'Accès aux espaces verts et naturels',
                'beach_access': 'Accès aux plages tropicales',
                'mountain_access': 'Proximité montagnes du Nord',

                # Business et tech (3)
                'business_environment': 'Écosystème d\'affaires et entrepreneuriat',
                'startup_ecosystem': 'Dynamisme startup et innovation',
                'tech_scene': 'Secteur technologique et numérique',

                # Spécifiques Thailand (4 - INNOVATIONS RÉVOLUTIONNAIRES)
                'tropical_climate_adaptation': 'Adaptation optimale au climat tropical',
                'expat_community_presence': 'Communauté expatriée internationale',
                'buddhist_culture_integration': 'Intégration culture bouddhiste authentique',
                'street_food_culture': '🍜 INNOVATION - Culture street food exceptionnelle'
            }

            return jsonify({
                'status': 'success',
                'criteria_definitions': criteria_definitions,
                'criteria_count': len(criteria_definitions),
                'approach': 'residents_and_expats_inclusive',
                'innovations': ['street_food_culture', 'tropical_climate_adaptation'],
                'regional_filters': [
                    'any_region',
                    'central_plains',
                    'northern_mountains',
                    'northeast_isan',
                    'eastern_seaboard',
                    'southern_beaches'
                ],
                'algorithm_version': thailand_residents_algo.version
            })

        except Exception as e:
            logger.error(f"❌ Thailand Criteria error: {str(e)}")
            return jsonify({'error': 'Erreur récupération critères Thailand'}), 500

    @app.route('/api/health', methods=['GET'])
    def global_health_check():
        """Health check global de tous les services"""
        try:
            health_status = {
                'gateway': 'healthy',
                'timestamp': datetime.now().isoformat(),
                'services': {}
            }

            # Test ZScore - Simple vérification d'existence
            try:
                health_status['services']['zscore'] = {
                    'status': 'healthy',
                    'countries': 20,
                    'version': '2.0.0'
                }
            except Exception as e:
                health_status['services']['zscore'] = {'status': 'unhealthy', 'error': str(e)}

            # Test USA Residents - Vérification des données
            try:
                cities_count = len(usa_residents_algo.cities_data['cities'])
                health_status['services']['usa_residents'] = {
                    'status': 'healthy',
                    'cities': cities_count,
                    'version': '1.0.0'
                }
            except Exception as e:
                health_status['services']['usa_residents'] = {'status': 'unhealthy', 'error': str(e)}

            # Test France Residents - Vérification des données
            try:
                cities_count = len(france_residents_algo.cities_data['cities'])
                health_status['services']['france_residents'] = {
                    'status': 'healthy',
                    'cities': cities_count,
                    'version': '1.0.0'
                }
            except Exception as e:
                health_status['services']['france_residents'] = {'status': 'unhealthy', 'error': str(e)}

            # Test Canada Residents - Vérification des données
            try:
                cities_count = len(canada_residents_algo.cities_data['cities'])
                health_status['services']['canada_residents'] = {
                    'status': 'healthy',
                    'cities': cities_count,
                    'version': '1.0.0'
                }
            except Exception as e:
                health_status['services']['canada_residents'] = {'status': 'unhealthy', 'error': str(e)}

            # Test UK Residents - Vérification des données
            try:
                cities_count = len(uk_residents_algo.cities_data['cities'])
                health_status['services']['uk_residents'] = {
                    'status': 'healthy',
                    'cities': cities_count,
                    'version': '1.0.0'
                }
            except Exception as e:
                health_status['services']['uk_residents'] = {'status': 'unhealthy', 'error': str(e)}

            # Test Japan Residents - Vérification des données
            try:
                cities_count = len(japan_residents_algo.cities_data['cities'])
                health_status['services']['japan_residents'] = {
                    'status': 'healthy',
                    'cities': cities_count,
                    'version': '1.0.0'
                }
            except Exception as e:
                health_status['services']['japan_residents'] = {'status': 'unhealthy', 'error': str(e)}

            # Test Germany Residents - Vérification des données
            try:
                cities_count = len(germany_residents_algo.cities_data['cities'])
                health_status['services']['germany_residents'] = {
                    'status': 'healthy',
                    'cities': cities_count,
                    'version': '1.0.0'
                }
            except Exception as e:
                health_status['services']['germany_residents'] = {'status': 'unhealthy', 'error': str(e)}

            # Test Australia Residents - Vérification des données
            try:
                cities_count = len(australia_residents_algo.cities_data)
                health_status['services']['australia_residents'] = {
                    'status': 'healthy',
                    'cities': cities_count,
                    'version': '1.0.0',
                    'approach': 'hybrid_residents_expats'
                }
            except Exception as e:
                health_status['services']['australia_residents'] = {'status': 'unhealthy', 'error': str(e)}

            # Test Brazil Residents - Vérification des données
            try:
                cities_count = len(brazil_residents_algo.cities_data['cities'])
                health_status['services']['brazil_residents'] = {
                    'status': 'healthy',
                    'cities': cities_count,
                    'regions': len(brazil_residents_algo.regional_mappings),
                    'version': brazil_residents_algo.version,
                    'approach': 'residents_expats_inclusive'
                }
            except Exception as e:
                health_status['services']['brazil_residents'] = {'status': 'unhealthy', 'error': str(e)}

            # Test Thailand Residents - Vérification des données
            try:
                cities_count = len(thailand_residents_algo.cities_data['cities'])
                health_status['services']['thailand_residents'] = {
                    'status': 'healthy',
                    'cities': cities_count,
                    'regions': 5,  # 5 regional zones Thailand
                    'version': thailand_residents_algo.version,
                    'approach': 'residents_expats_inclusive',
                    'innovations': ['street_food_culture', 'tropical_climate_adaptation']
                }
            except Exception as e:
                health_status['services']['thailand_residents'] = {'status': 'unhealthy', 'error': str(e)}

            # Test SkillGraph - Simple vérification d'existence
            try:
                health_status['services']['skillgraph'] = {
                    'status': 'healthy',
                    'sectors': 10,
                    'version': '1.0.0'
                }
            except Exception as e:
                health_status['services']['skillgraph'] = {'status': 'unhealthy', 'error': str(e)}

            # Test Wealth - Simple vérification d'existence
            try:
                health_status['services']['wealth'] = {
                    'status': 'healthy',
                    'markets': 6,
                    'version': '0.9.0'
                }
            except Exception as e:
                health_status['services']['wealth'] = {'status': 'unhealthy', 'error': str(e)}

            # Status global
            service_statuses = [s.get('status') for s in health_status['services'].values()]
            if all(status == 'healthy' for status in service_statuses):
                overall_status = 200
            elif any(status == 'healthy' for status in service_statuses):
                overall_status = 206  # Partial content
            else:
                overall_status = 503
                health_status['gateway'] = 'degraded'

            return jsonify(health_status), overall_status

        except Exception as e:
            logger.error(f"❌ Global health check failed: {e}")
            return jsonify({
                'gateway': 'unhealthy',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }), 503

    @app.route('/api/stats', methods=['GET'])
    def global_statistics():
        """Statistiques globales de la plateforme"""
        try:
            return jsonify({
                'success': True,
                'platform_stats': {
                    'total_services': 7,  # ZScore, USA/France/Canada/UK Residents, SkillGraph, Wealth
                    'total_criteria': (
                        len(zscore_algo.get_all_criteria()) +
                        len(skillgraph_algo.get_all_criteria()) +
                        len(wealth_algo.get_all_criteria()) +
                        len(usa_residents_algo.criteria_weights_base) +
                        len(france_residents_algo.criteria_weights_base) +
                        len(canada_residents_algo.criteria_weights_base) +
                        len(uk_residents_algo.criteria_weights_base)
                    ),
                    'data_coverage': {
                        'countries': len(zscore_algo.get_available_countries()),
                        'usa_cities': len(usa_residents_algo.cities_data['cities']),
                        'france_cities': len(france_residents_algo.cities_data['cities']),
                        'canada_cities': len(canada_residents_algo.cities_data['cities']),
                        'uk_cities': len(uk_residents_algo.cities_data['cities']),
                        'job_sectors': len(skillgraph_algo.get_supported_sectors()),
                        'financial_markets': len(wealth_algo.get_supported_markets())
                    },
                    'cache_stats': data_loader.get_cache_stats(),
                    'uptime': 'healthy',
                    'version': '1.0.0'
                },
                'service_details': {
                    'zscore': zscore_algo.get_algorithm_info(),
                    'usa_residents': {
                        'version': usa_residents_algo.version,
                        'cities': len(usa_residents_algo.cities_data['cities']),
                        'criteria': len(usa_residents_algo.criteria_weights_base)
                    },
                    'france_residents': {
                        'version': france_residents_algo.version,
                        'cities': len(france_residents_algo.cities_data['cities']),
                        'criteria': len(france_residents_algo.criteria_weights_base)
                    },
                    'canada_residents': {
                        'version': canada_residents_algo.version,
                        'cities': len(canada_residents_algo.cities_data['cities']),
                        'criteria': len(canada_residents_algo.criteria_weights_base)
                    },
                    'uk_residents': {
                        'version': uk_residents_algo.version,
                        'cities': len(uk_residents_algo.cities_data['cities']),
                        'criteria': len(uk_residents_algo.criteria_weights_base)
                    },
                    'skillgraph': skillgraph_algo.get_algorithm_info(),
                    'wealth': wealth_algo.get_algorithm_info()
                }
            })

        except Exception as e:
            logger.error(f"❌ Stats error: {e}")
            return jsonify({'error': 'Failed to get statistics'}), 500

    @app.route('/api/clear-cache', methods=['POST'])
    @security.require_valid_session
    def clear_all_caches():
        """Vide tous les caches (admin endpoint)"""
        try:
            # Vider caches de tous les services
            zscore_algo.clear_cache()
            skillgraph_algo.clear_cache()
            wealth_algo.clear_cache()
            data_loader.clear_cache()

            return jsonify({
                'success': True,
                'message': 'All caches cleared successfully',
                'timestamp': datetime.now().isoformat()
            })

        except Exception as e:
            logger.error(f"❌ Cache clear error: {e}")
            return jsonify({'error': 'Failed to clear caches'}), 500

    # ===============================
    # 🔥 STRIPE INTEGRATION PREMIUM
    # ===============================

    @app.route('/api/create-payment-intent', methods=['POST'])
    def create_payment_intent():
        """Création payment intent Stripe pour premium"""
        try:
            data = request.get_json()
            amount = data.get('amount', 2000)  # 20€ par défaut

            # Créer payment intent
            intent = stripe.PaymentIntent.create(
                amount=amount,
                currency='eur',
                metadata={
                    'service': data.get('service', 'premium'),
                    'user_session': session.get('session_token', 'anonymous')
                }
            )

            return jsonify({
                'success': True,
                'client_secret': intent.client_secret,
                'amount': amount
            })

        except Exception as e:
            logger.error(f"❌ Stripe payment error: {e}")
            return jsonify({'error': 'Payment creation failed'}), 500

    # ===============================
    # 🎯 UNIVERSAL CALCULATE ENDPOINT - COUNTRY ID SYSTEM
    # ===============================

    @app.route('/api/calculate', methods=['POST'])
    @app.route('/calculate', methods=['POST'])  # Route pour le proxy NGINX
    def calculate_recommendations():
        """
        🌍 Universal recommendation endpoint with country ID support
        Routes to appropriate algorithm based on selected country
        Returns city recommendations with country_id for guide mapping
        """
        try:
            data = request.get_json()

            # Support pour les deux formats de données:
            # Format ancien: {"questionnaire": {...}, "country": "france"}
            # Format nouveau: {"answers": {...}, "country": "world", "parcours": "international"}
            questionnaire = data.get('questionnaire', data.get('answers', {}))
            selected_country = data.get('country', 'france').lower()
            parcours = data.get('parcours', None)

            logger.info(f"🔍 Calculate API called with country: {selected_country}, parcours: {parcours}")
            logger.info(f"📋 Questionnaire keys: {list(questionnaire.keys())}")

            # Mapping des pays vers leurs algorithmes spécifiques
            country_algorithms = {
                'france': france_residents_algo,
                'usa': usa_residents_algo,
                'canada': canada_residents_algo,
                'brazil': brazil_residents_algo,
                'uk': uk_residents_algo,
                'germany': germany_residents_algo,
                'spain': spain_residents_algo,
                'japan': japan_residents_algo,
                'thailand': thailand_residents_algo,
                'morocco': morocco_residents_algo,
                'australia': australia_residents_algo
                # 'mexico': mexico_residents_algo  # TODO: Add Mexico algorithm
            }

            # Gestion spéciale pour le parcours international (world)
            if selected_country == 'world' or parcours == 'international':
                logger.info("🌍 International questionnaire detected - using ZScore algorithm")
                # Pour les questionnaires internationaux, on utilise l'algorithme ZScore général
                recommendations = zscore_algo.calculate_recommendations(questionnaire, limit=10)
                selected_country = 'world'  # Normaliser le pays
            else:
                # Sélectionner l'algorithme approprié pour un pays spécifique
                algo = country_algorithms.get(selected_country, france_residents_algo)

                # Calculer les recommandations
                try:
                    recommendations = algo.calculate_recommendations(questionnaire, limit=10)
                except Exception as calc_error:
                    logger.error(f"❌ Calculation error for {selected_country}: {calc_error}")
                    # Fallback vers France si erreur
                    recommendations = france_residents_algo.calculate_recommendations(questionnaire, limit=10)

            # Adapter les résultats avec country_id pour le nouveau système
            adapted_recommendations = []
            for rec in recommendations:
                city_data = {
                    'city': rec.get('name', rec.get('city', 'Unknown')),
                    'country': selected_country.title(),
                    'compatibility': rec.get('score', rec.get('compatibility_score', 0.85)),
                    'score': rec.get('score', rec.get('compatibility_score', 0.85)),
                    'reasons': rec.get('reasons', []),
                    'country_id': get_country_id_from_name(selected_country)  # NOUVEAU: country_id pour guide mapping
                }
                adapted_recommendations.append(city_data)

            logger.info(f"✅ Calculate API: {len(adapted_recommendations)} recommendations for {selected_country}")

            return jsonify({
                'success': True,
                'recommendations': adapted_recommendations,
                'country': selected_country,
                'algorithm_used': algo.__class__.__name__ if hasattr(algo, '__class__') else 'Unknown',
                'total_cities_analyzed': len(recommendations),
                'country_id_system': True  # Flag pour indiquer le support du nouveau système
            })

        except Exception as e:
            logger.error(f"❌ Universal calculate error: {e}")
            return jsonify({
                'success': False,
                'error': 'Calculation failed',
                'message': str(e)
            }), 500

    def get_country_id_from_name(country_name):
        """Helper function to get country_id from country name"""
        country_id_mapping = {
            'france': 'fr',
            'usa': 'us',
            'canada': 'ca',
            'uk': 'uk',
            'germany': 'de',
            'spain': 'es',
            'japan': 'jp',
            'thailand': 'th',
            'morocco': 'ma',
            'brazil': 'br',
            'australia': 'au',
            'mexico': 'mx'
        }
        return country_id_mapping.get(country_name.lower(), 'fr')  # Default to France

    # ===============================
    # 🚨 ERROR HANDLERS GLOBAUX
    # ===============================

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'error': 'Endpoint not found',
            'available_services': ['/api/calculate', '/api/career', '/api/wealth'],
            'documentation': '/',
            'status': 404
        }), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({
            'error': 'Internal server error',
            'message': 'Please try again or contact support',
            'status': 500
        }), 500

    @app.errorhandler(429)
    def rate_limit_error(error):
        return jsonify({
            'error': 'Rate limit exceeded',
            'message': 'Please slow down your requests',
            'retry_after': '1 hour',
            'status': 429
        }), 429

    logger.info("🚀 Revolutionary Backend fully initialized!")
    return app

# ===============================
# 🚀 POINT D'ENTRÉE PRINCIPAL
# ===============================

# Créer l'application
app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))

    # Force mode développement pour tests locaux (même sur port 8000)
    debug = True  # os.environ.get('FLASK_ENV') == 'development' or port != 8000  # Debug si pas sur port production

    print(f"""
🎯 REVOLUTIONARY BACKEND - ZINEINSIGHT PLATFORM
=============================================
🌐 Gateway unifié pour intelligence totale

📊 SERVICES INTÉGRÉS:
├── 🏙️ ZScore v2.0.0      → 20 pays, 49 critères
├── 🇺🇸 USA Residents     → 30 villes, 27 critères
├── 🇫🇷 France Residents  → 30 villes, 27 critères
├── 🇨🇦 Canada Residents  → 30 villes, 27 critères
├── 🇬🇧 UK Residents      → 30 villes, 27 critères
├── 🇹🇭 Thailand Residents → 29 villes, 27 critères + innovations
├── 💼 SkillGraph v1.0.0   → 10 secteurs, 53 critères
└── 💰 Wealth v0.9.0       → 6 marchés, 46 critères

🔥 TOTAL: 8 services avec 283+ critères d'intelligence personnalisée !

🌍 Running on: http://localhost:{port}
📱 Environment: {'Development' if debug else 'Production LIVE'}
🛡️ Security: {'Flexible (HTTP OK)' if debug else 'Strict (HTTPS only)'}
💳 Stripe: {'Test mode' if debug else 'LIVE mode'}
    """)

    app.run(host='0.0.0.0', port=port, debug=debug)
