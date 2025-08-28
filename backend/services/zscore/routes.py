"""
🌐 ZSCORE ROUTES - API ENDPOINTS
===============================
Routes Flask pour le service ZScore
Compatible avec l'API existante et le frontend SPA

Endpoints:
- POST /api/calculate → Analyse principale (existant)
- GET /api/countries → Liste pays supportés
- GET /api/stats → Statistiques algorithme
"""

import logging
from flask import Blueprint, request, jsonify, session
from typing import Dict, Any
import requests
import sys
import os
# 🌍 Import de l'algorithme EXPAT INTERNATIONAL
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from algorithms_historical.algo_expat import AlgorithmeExpat

logger = logging.getLogger(__name__)

# Blueprint ZScore
zscore_bp = Blueprint('zscore', __name__, url_prefix='/api')

# Instance globale de l'algorithme EXPAT
zscore_algorithm = AlgorithmeExpat()


@zscore_bp.route('/calculate', methods=['POST'])
def calculate_zscore():
    """
    🚀 API ZScore SIMPLE - VERSION QUI MARCHE !
    Analyse villes/pays selon questionnaire utilisateur
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No JSON data provided', 'success': False}), 400

        questionnaire = data.get('questionnaire', data.get('responses', data.get('answers', {})))
        country = data.get('country', data.get('pays', 'france'))

        if not questionnaire:
            logger.error(f"❌ QUESTIONNAIRE VIDE: data={data}")
            return jsonify({'error': 'Questionnaire is required', 'success': False}), 400

        logger.info(f"🎯 ZScore SIMPLE - Questionnaire: {questionnaire}, Pays: {country}")
        logger.info(f"🔍 DEBUG - Nombre de réponses: {len(questionnaire)}")
        logger.info(f"🔍 DEBUG - Clés questionnaire: {list(questionnaire.keys())}")

        try:
            # 🌍 UTILISER L'ALGORITHME EXPAT INTERNATIONAL
            algorithm = AlgorithmeExpat()
            logger.info(f"🧠 DEBUG - Algorithme expat créé")

            # Utiliser la nouvelle méthode calculer_recommandations
            recommendations = algorithm.calculer_recommandations(questionnaire, country)
            logger.info(f"🧠 DEBUG - Analyse terminée, nombre de recommandations: {len(recommendations)}")

            if recommendations:
                # Formater pour compatibilité avec l'ancien format
                results = {
                    'success': True,
                    'recommendations': recommendations,
                    'message': f'Top {len(recommendations)} villes trouvées'
                }
                reco_names = [r.get('city', 'Unknown') for r in recommendations]
                logger.info(f"✅ TOP {len(recommendations)}: {reco_names}")
            else:
                results = {
                    'success': False,
                    'error': 'Aucune ville compatible trouvée',
                    'recommendations': []
                }
                logger.error(f"❌ Aucune recommandation trouvée")

        except Exception as e:
            logger.error(f"💥 EXCEPTION dans calculate: {str(e)}")
            import traceback
            logger.error(f"💥 TRACEBACK: {traceback.format_exc()}")
            return jsonify({'error': str(e), 'success': False}), 500

        return jsonify(results)

    except Exception as e:
        logger.error(f"❌ Erreur API calculate: {e}")
        return jsonify({
            'success': False,
            'error': str(e),
            'recommendations': []
        }), 500

        # 📊 AUTO-SAUVEGARDE pour le dashboard (si utilisateur connecté)
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith('Bearer '):
            try:
                # Calculer un score global pour l'analyse
                recommendations = results.get('recommendations', [])
                avg_score = sum([r.get('final_score', 0) for r in recommendations]) / len(recommendations) if recommendations else 0

                # Préparer les données à sauvegarder
                save_data = {
                    'service': 'zscore',
                    'results': recommendations[:3],  # Top 3 pour dashboard
                    'score': round(avg_score, 1),
                    'questionnaire': {
                        'budget_monthly': questionnaire.get('budget_monthly'),
                        'age': questionnaire.get('age'),
                        'status': questionnaire.get('status'),
                        'country': country,
                        'preferences': data.get('preferences', {})
                    }
                }

                # Appel interne à l'API de sauvegarde
                requests.post('http://localhost:8000/api/auth/save-analysis',
                            headers={'Authorization': auth_header, 'Content-Type': 'application/json'},
                            json=save_data)

                logger.info(f"✅ ZScore analysis saved to user dashboard (score: {avg_score:.1f})")

            except Exception as save_error:
                logger.warning(f"⚠️ Could not save ZScore analysis to dashboard: {save_error}")

        # Stocker en session pour upgrade premium potentiel
        session['zscore_results'] = results
        session['zscore_completed'] = True

        logger.info(f"✅ ZScore calculation completed: {len(results.get('recommendations', []))} recommendations")
        return jsonify(results)

    except Exception as e:
        logger.error(f"❌ ZScore API error: {e}")
        return jsonify({'error': 'Analysis failed'}), 500


@zscore_bp.route('/countries', methods=['GET'])
def get_supported_countries():
    """Retourne la liste des pays supportés avec métadonnées"""
    try:
        countries = zscore_algorithm.get_available_countries()

        # Enrichir avec métadonnées
        countries_info = []
        for country_code in countries:
            country_info = zscore_algorithm.supported_countries.get(country_code, {})
            countries_info.append({
                'code': country_code,
                'name': country_info.get('display', country_code.title()),
                'file': country_info.get('file', country_code)
            })

        return jsonify({
            'success': True,
            'countries': countries_info,
            'total': len(countries_info)
        })

    except Exception as e:
        logger.error(f"❌ Countries API error: {e}")
        return jsonify({'error': 'Failed to load countries'}), 500


@zscore_bp.route('/stats', methods=['GET'])
def get_zscore_stats():
    """Statistiques détaillées de l'algorithme ZScore"""
    try:
        stats = zscore_algorithm.get_algorithm_info()

        return jsonify({
            'success': True,
            'stats': stats,
            'service': 'zscore',
            'version': zscore_algorithm.version
        })

    except Exception as e:
        logger.error(f"❌ Stats API error: {e}")
        return jsonify({'error': 'Failed to get stats'}), 500


@zscore_bp.route('/health', methods=['GET'])
def zscore_health():
    """Health check spécifique au service ZScore"""
    try:
        # Test basique de l'algorithme avec la bonne méthode
        test_questionnaire = {'expat_passport': 'france'}
        test_result = zscore_algorithm.calculer_recommandations(test_questionnaire, 'world')

        health_status = {
            'service': 'zscore',
            'version': '2.0.0',
            'status': 'healthy' if test_result and len(test_result) > 0 else 'degraded',
            'countries_available': 20,
            'criteria_count': 33,  # Fixed count for expat algorithm
            'data_loader_status': 'expat_focused'
        }

        status_code = 200 if health_status['status'] == 'healthy' else 503
        return jsonify(health_status), status_code

    except Exception as e:
        logger.error(f"❌ ZScore health check failed: {e}")
        return jsonify({
            'service': 'zscore',
            'status': 'unhealthy',
            'error': str(e)
        }), 503


@zscore_bp.route('/clear-cache', methods=['POST'])
def clear_zscore_cache():
    """Vide le cache de l'algorithme ZScore"""
    try:
        # Vider caches algorithme et data loader
        zscore_algorithm.clear_cache()

        if zscore_algorithm.data_loader:
            zscore_algorithm.data_loader.clear_cache()

        return jsonify({
            'success': True,
            'message': 'ZScore caches cleared successfully'
        })

    except Exception as e:
        logger.error(f"❌ Cache clear error: {e}")
        return jsonify({'error': 'Failed to clear cache'}), 500


# Error handlers pour le blueprint
@zscore_bp.errorhandler(404)
def zscore_not_found(error):
    return jsonify({
        'error': 'ZScore endpoint not found',
        'service': 'zscore'
    }), 404


@zscore_bp.errorhandler(500)
def zscore_internal_error(error):
    return jsonify({
        'error': 'ZScore internal server error',
        'service': 'zscore'
    }), 500
