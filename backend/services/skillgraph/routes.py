"""
🌐 SKILLGRAPH ROUTES - API ENDPOINTS
===================================
Routes Flask pour le service SkillGraph
API moderne pour recommandations carrière et compétences

Endpoints:
- POST /api/career → Analyse principale carrière
- GET /api/sectors → Secteurs d'activité supportés
- GET /api/markets → Marchés emploi internationaux
- GET /api/skills → Compétences tendance
"""

import logging
from flask import Blueprint, request, jsonify, session
from typing import Dict, Any
from .algorithm import SkillGraphAlgorithm

logger = logging.getLogger(__name__)

# Blueprint SkillGraph
skillgraph_bp = Blueprint('skillgraph', __name__, url_prefix='/api')

# Instance globale de l'algorithme
skillgraph_algorithm = SkillGraphAlgorithm()


@skillgraph_bp.route('/career', methods=['POST'])
def analyze_career():
    """
    API principale SkillGraph - Analyse carrière et compétences
    Recommandations emplois + gap analysis + formations
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400

        questionnaire = data.get('questionnaire', data.get('responses', {}))
        country = data.get('country', data.get('market', 'france'))

        if not questionnaire:
            return jsonify({'error': 'Questionnaire is required'}), 400

        # Analyse via algorithme moderne
        results = skillgraph_algorithm.analyze(questionnaire, country)

        if 'error' in results:
            logger.warning(f"SkillGraph analysis error: {results['error']}")
            return jsonify(results), 400

        # Stocker en session pour upgrade premium potentiel
        session['skillgraph_results'] = results
        session['skillgraph_completed'] = True

        logger.info(f"✅ SkillGraph analysis completed: {len(results.get('career_recommendations', []))} recommendations")
        return jsonify(results)

    except Exception as e:
        logger.error(f"❌ SkillGraph API error: {e}")
        return jsonify({'error': 'Career analysis failed'}), 500


@skillgraph_bp.route('/sectors', methods=['GET'])
def get_supported_sectors():
    """Retourne les secteurs d'activité supportés avec métadonnées"""
    try:
        sectors = skillgraph_algorithm.get_supported_sectors()

        # Enrichir avec métadonnées
        sectors_info = []
        for sector_code in sectors:
            sector_info = skillgraph_algorithm.supported_sectors.get(sector_code, {})
            sectors_info.append({
                'code': sector_code,
                'name': sector_info.get('name', sector_code.title()),
                'growth': sector_info.get('growth', 'medium'),
                'remote_friendly': sector_info.get('remote_friendly', False)
            })

        return jsonify({
            'success': True,
            'sectors': sectors_info,
            'total': len(sectors_info)
        })

    except Exception as e:
        logger.error(f"❌ Sectors API error: {e}")
        return jsonify({'error': 'Failed to load sectors'}), 500


@skillgraph_bp.route('/markets', methods=['GET'])
def get_job_markets():
    """Retourne les marchés emploi internationaux supportés"""
    try:
        markets = skillgraph_algorithm.get_job_markets()

        # Enrichir avec métadonnées
        markets_info = []
        for market_code in markets:
            market_info = skillgraph_algorithm.job_markets.get(market_code, {})
            markets_info.append({
                'code': market_code,
                'name': market_code.title(),
                'currency': market_info.get('currency', 'EUR'),
                'salary_range': market_info.get('avg_salary_range', 'N/A'),
                'visa_required': market_info.get('visa_req', True)
            })

        return jsonify({
            'success': True,
            'markets': markets_info,
            'total': len(markets_info)
        })

    except Exception as e:
        logger.error(f"❌ Markets API error: {e}")
        return jsonify({'error': 'Failed to load job markets'}), 500


@skillgraph_bp.route('/skills/<country>', methods=['GET'])
def get_trending_skills(country: str):
    """Retourne les compétences tendance pour un pays"""
    try:
        trending_skills = skillgraph_algorithm._get_trending_skills(country)
        salary_trends = skillgraph_algorithm._get_salary_trends(country)

        return jsonify({
            'success': True,
            'country': country,
            'trending_skills': trending_skills,
            'salary_trends': salary_trends,
            'updated_at': '2025-08-19'
        })

    except Exception as e:
        logger.error(f"❌ Skills API error: {e}")
        return jsonify({'error': 'Failed to load trending skills'}), 500


@skillgraph_bp.route('/profile-analysis', methods=['POST'])
def analyze_profile():
    """Analyse approfondie du profil utilisateur"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No profile data provided'}), 400

        questionnaire = data.get('questionnaire', {})
        if not questionnaire:
            return jsonify({'error': 'Questionnaire is required'}), 400

        # Analyse profil uniquement
        user_profile = skillgraph_algorithm._analyze_user_profile(questionnaire)

        return jsonify({
            'success': True,
            'profile_analysis': user_profile,
            'recommendations': {
                'focus_areas': user_profile.get('strengths', []),
                'priority_sectors': user_profile.get('preferred_sectors', []),
                'development_areas': ['Leadership', 'Technical Skills', 'Communication'][:3]
            }
        })

    except Exception as e:
        logger.error(f"❌ Profile analysis error: {e}")
        return jsonify({'error': 'Profile analysis failed'}), 500


@skillgraph_bp.route('/stats', methods=['GET'])
def get_skillgraph_stats():
    """Statistiques détaillées de l'algorithme SkillGraph"""
    try:
        stats = skillgraph_algorithm.get_algorithm_info()

        return jsonify({
            'success': True,
            'stats': stats,
            'service': 'skillgraph',
            'version': skillgraph_algorithm.version
        })

    except Exception as e:
        logger.error(f"❌ Stats API error: {e}")
        return jsonify({'error': 'Failed to get stats'}), 500


@skillgraph_bp.route('/health', methods=['GET'])
def skillgraph_health():
    """Health check spécifique au service SkillGraph"""
    try:
        # Test basique de l'algorithme
        test_questionnaire = {'career_priority': 'growth', 'sector_interest': 'tech'}
        test_result = skillgraph_algorithm.analyze(test_questionnaire, 'france')

        health_status = {
            'service': 'skillgraph',
            'version': skillgraph_algorithm.version,
            'status': 'healthy' if test_result.get('success') else 'degraded',
            'sectors_available': len(skillgraph_algorithm.get_supported_sectors()),
            'markets_available': len(skillgraph_algorithm.get_job_markets()),
            'criteria_count': len(skillgraph_algorithm.get_all_criteria()),
            'data_loader_status': 'connected' if skillgraph_algorithm.data_loader else 'disconnected'
        }

        status_code = 200 if health_status['status'] == 'healthy' else 503
        return jsonify(health_status), status_code

    except Exception as e:
        logger.error(f"❌ SkillGraph health check failed: {e}")
        return jsonify({
            'service': 'skillgraph',
            'status': 'unhealthy',
            'error': str(e)
        }), 503


@skillgraph_bp.route('/clear-cache', methods=['POST'])
def clear_skillgraph_cache():
    """Vide le cache de l'algorithme SkillGraph"""
    try:
        # Vider cache algorithme
        skillgraph_algorithm.clear_cache()

        return jsonify({
            'success': True,
            'message': 'SkillGraph cache cleared successfully'
        })

    except Exception as e:
        logger.error(f"❌ Cache clear error: {e}")
        return jsonify({'error': 'Failed to clear cache'}), 500


# Error handlers pour le blueprint
@skillgraph_bp.errorhandler(404)
def skillgraph_not_found(error):
    return jsonify({
        'error': 'SkillGraph endpoint not found',
        'service': 'skillgraph'
    }), 404


@skillgraph_bp.errorhandler(500)
def skillgraph_internal_error(error):
    return jsonify({
        'error': 'SkillGraph internal server error',
        'service': 'skillgraph'
    }), 500
