"""
🌐 WEALTH ROUTES - API ENDPOINTS
===============================
Routes Flask pour le service Wealth
API révolutionnaire pour liberté financière et optimisation patrimoniale

Endpoints:
- POST /api/wealth → Analyse principale liberté financière
- GET /api/wealth/markets → Marchés financiers supportés
- GET /api/wealth/strategies → Stratégies d'investissement
- POST /api/wealth/timeline → Simulateur timeline liberté
- GET /api/wealth/tax → Optimisations fiscales par pays
"""

import logging
from flask import Blueprint, request, jsonify, session
from typing import Dict, Any
from .algorithm import WealthAlgorithm

logger = logging.getLogger(__name__)

# Blueprint Wealth
wealth_bp = Blueprint('wealth', __name__, url_prefix='/api')

# Instance globale de l'algorithme
wealth_algorithm = WealthAlgorithm()


@wealth_bp.route('/wealth', methods=['POST'])
def analyze_wealth():
    """
    API principale Wealth - Analyse liberté financière révolutionnaire
    Roadmap personnalisée vers indépendance financière
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400

        questionnaire = data.get('questionnaire', data.get('responses', {}))
        country = data.get('country', data.get('market', 'france'))

        if not questionnaire:
            return jsonify({'error': 'Questionnaire is required'}), 400

        # Analyse via algorithme révolutionnaire
        results = wealth_algorithm.analyze(questionnaire, country)

        if 'error' in results:
            logger.warning(f"Wealth analysis error: {results['error']}")
            return jsonify(results), 400

        # Stocker en session pour upgrade premium potentiel
        session['wealth_results'] = results
        session['wealth_completed'] = True

        logger.info(f"✅ Wealth analysis completed: {results['timeline_analysis']['years_to_freedom']} years to freedom")
        return jsonify(results)

    except Exception as e:
        logger.error(f"❌ Wealth API error: {e}")
        return jsonify({'error': 'Wealth analysis failed'}), 500


@wealth_bp.route('/wealth/markets', methods=['GET'])
def get_wealth_markets():
    """Retourne les marchés financiers supportés avec métadonnées"""
    try:
        markets = wealth_algorithm.get_supported_markets()

        # Enrichir avec métadonnées détaillées
        markets_info = []
        for market_code in markets:
            market_data = wealth_algorithm.wealth_markets.get(market_code, {})
            markets_info.append({
                'code': market_code,
                'name': market_code.title(),
                'currency': market_data.get('currency', 'EUR'),
                'freedom_threshold': market_data.get('freedom_threshold', '2000€/month'),
                'real_estate_roi': market_data.get('real_estate_roi', '4-7%'),
                'stock_market_roi': market_data.get('stock_market_roi', '7-10%'),
                'tax_tools': market_data.get('tax_optimization', []),
                'retirement_age': market_data.get('retirement_age', 62),
                'social_security': market_data.get('social_security', 'medium')
            })

        return jsonify({
            'success': True,
            'markets': markets_info,
            'total': len(markets_info),
            'recommended_for_beginners': ['france', 'canada', 'germany']
        })

    except Exception as e:
        logger.error(f"❌ Markets API error: {e}")
        return jsonify({'error': 'Failed to load wealth markets'}), 500


@wealth_bp.route('/wealth/strategies', methods=['GET'])
def get_investment_strategies():
    """Retourne les stratégies d'investissement disponibles"""
    try:
        strategies = wealth_algorithm.get_investment_strategies()

        # Enrichir avec détails complets
        strategies_info = []
        for strategy_code in strategies:
            strategy_data = wealth_algorithm.investment_strategies.get(strategy_code, {})
            strategies_info.append({
                'code': strategy_code,
                'name': strategy_data.get('name', strategy_code.title()),
                'risk_level': strategy_data.get('risk_level', 'medium'),
                'expected_roi': strategy_data.get('expected_roi', '5-8%'),
                'allocation': strategy_data.get('allocation', {}),
                'timeline': strategy_data.get('timeline', 'medium-term'),
                'suitable_for': strategy_data.get('suitable_for', []),
                'description': f"Stratégie {strategy_data.get('risk_level', 'équilibrée')} avec ROI attendu {strategy_data.get('expected_roi', '5-8%')}"
            })

        return jsonify({
            'success': True,
            'strategies': strategies_info,
            'total': len(strategies_info),
            'popular_choice': 'balanced'
        })

    except Exception as e:
        logger.error(f"❌ Strategies API error: {e}")
        return jsonify({'error': 'Failed to load investment strategies'}), 500


@wealth_bp.route('/wealth/timeline', methods=['POST'])
def simulate_timeline():
    """Simulateur interactif de timeline vers liberté financière"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No simulation data provided'}), 400

        # Paramètres simulation
        monthly_savings = data.get('monthly_savings', 1000)
        target_amount = data.get('target_amount', 500000)
        expected_roi = data.get('expected_roi', 0.07)
        current_age = data.get('current_age', 30)

        # Calcul timeline avec croissance composée
        years_needed = 0
        current_amount = data.get('current_wealth', 0)

        milestones = []
        while current_amount < target_amount and years_needed < 50:
            years_needed += 1
            current_amount = (current_amount + monthly_savings * 12) * (1 + expected_roi)

            # Milestones importantes
            if years_needed in [5, 10, 15, 20] or current_amount >= target_amount:
                milestones.append({
                    'year': years_needed,
                    'age': current_age + years_needed,
                    'amount': int(current_amount),
                    'milestone': f"Patrimoine {int(current_amount//1000)}K €" if current_amount < target_amount else "🎯 Liberté Financière!"
                })

        return jsonify({
            'success': True,
            'timeline_simulation': {
                'years_to_freedom': years_needed,
                'freedom_age': current_age + years_needed,
                'final_amount': int(current_amount),
                'total_invested': monthly_savings * 12 * years_needed,
                'growth_earnings': int(current_amount - (monthly_savings * 12 * years_needed)),
                'milestones': milestones,
                'monthly_passive_income': int(current_amount * 0.04 / 12)  # Règle des 4%
            },
            'recommendations': {
                'optimize_savings': 'Augmentez vos économies de 10% pour gagner 2-3 ans',
                'improve_roi': 'Diversifiez pour viser 8-9% de rendement',
                'reduce_timeline': f'Avec +200€/mois: {max(1, years_needed-2)} ans seulement!'
            }
        })

    except Exception as e:
        logger.error(f"❌ Timeline simulation error: {e}")
        return jsonify({'error': 'Timeline simulation failed'}), 500


@wealth_bp.route('/wealth/tax/<country>', methods=['GET'])
def get_tax_optimizations(country: str):
    """Optimisations fiscales spécifiques par pays"""
    try:
        market_data = wealth_algorithm.wealth_markets.get(country, {})
        tax_tools = market_data.get('tax_optimization', [])

        # Détails des outils fiscaux
        tax_details = {
            'PEA': {
                'name': 'Plan Épargne en Actions',
                'country': 'france',
                'max_amount': '150,000€',
                'tax_benefit': 'Exonération après 5 ans',
                'eligibility': 'Résidents fiscaux français'
            },
            'Assurance-vie': {
                'name': 'Assurance-vie',
                'country': 'france',
                'max_amount': 'Illimité',
                'tax_benefit': 'Fiscalité progressive avantageuse',
                'eligibility': 'Tous'
            },
            '401k': {
                'name': '401(k) Plan',
                'country': 'usa',
                'max_amount': '$23,000/year',
                'tax_benefit': 'Déduction fiscale immédiate',
                'eligibility': 'Employés US'
            },
            'TFSA': {
                'name': 'Tax-Free Savings Account',
                'country': 'canada',
                'max_amount': '$6,500/year',
                'tax_benefit': 'Croissance libre d\'impôt',
                'eligibility': 'Résidents canadiens'
            }
        }

        optimizations = []
        for tool in tax_tools:
            if tool in tax_details:
                optimizations.append(tax_details[tool])

        return jsonify({
            'success': True,
            'country': country,
            'tax_optimizations': optimizations,
            'general_tips': [
                'Maximiser comptes défiscalisés en priorité',
                'Étaler gains sur plusieurs années fiscales',
                'Considérer résidence fiscale optimale'
            ]
        })

    except Exception as e:
        logger.error(f"❌ Tax optimization error: {e}")
        return jsonify({'error': 'Failed to load tax optimizations'}), 500


@wealth_bp.route('/wealth/health-check', methods=['POST'])
def wealth_health_check():
    """Diagnostic rapide santé financière"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No financial data provided'}), 400

        # Données financières basiques
        monthly_income = data.get('monthly_income', 3000)
        monthly_expenses = data.get('monthly_expenses', 2500)
        current_savings = data.get('current_savings', 10000)
        monthly_savings = monthly_income - monthly_expenses

        # Diagnostic santé financière
        savings_rate = monthly_savings / monthly_income if monthly_income > 0 else 0
        emergency_months = current_savings / monthly_expenses if monthly_expenses > 0 else 0

        # Score santé financière
        health_score = 0
        recommendations = []

        if savings_rate >= 0.2:
            health_score += 30
        elif savings_rate >= 0.1:
            health_score += 20
            recommendations.append("Visez 20% d'épargne pour accélérer vers liberté financière")
        else:
            health_score += 10
            recommendations.append("PRIORITÉ: Réduisez dépenses pour épargner au moins 10%")

        if emergency_months >= 6:
            health_score += 25
        elif emergency_months >= 3:
            health_score += 15
            recommendations.append("Complétez fonds d'urgence à 6 mois de frais")
        else:
            health_score += 5
            recommendations.append("URGENT: Constituez fonds d'urgence de 3-6 mois")

        # Bonus diversification (simulé)
        if current_savings > 20000:
            health_score += 20
            recommendations.append("Diversifiez placements pour optimiser rendements")

        health_status = 'excellent' if health_score >= 70 else 'good' if health_score >= 50 else 'needs_work'

        return jsonify({
            'success': True,
            'financial_health': {
                'score': health_score,
                'status': health_status,
                'savings_rate': f"{savings_rate*100:.1f}%",
                'emergency_months': f"{emergency_months:.1f} mois",
                'monthly_surplus': f"{monthly_savings}€"
            },
            'recommendations': recommendations[:3],
            'next_steps': [
                "Automatiser épargne dès réception salaire",
                "Analyser et optimiser dépenses récurrentes",
                "Diversifier investissements selon profil risque"
            ]
        })

    except Exception as e:
        logger.error(f"❌ Health check error: {e}")
        return jsonify({'error': 'Health check failed'}), 500


@wealth_bp.route('/wealth/stats', methods=['GET'])
def get_wealth_stats():
    """Statistiques détaillées de l'algorithme Wealth"""
    try:
        stats = wealth_algorithm.get_algorithm_info()

        return jsonify({
            'success': True,
            'stats': stats,
            'service': 'wealth',
            'version': wealth_algorithm.version,
            'specialization': 'Financial Freedom Intelligence'
        })

    except Exception as e:
        logger.error(f"❌ Stats API error: {e}")
        return jsonify({'error': 'Failed to get stats'}), 500


@wealth_bp.route('/wealth/health', methods=['GET'])
def wealth_service_health():
    """Health check spécifique au service Wealth"""
    try:
        # Test basique de l'algorithme
        test_questionnaire = {'monthly_income': '3000', 'savings_goal': 'freedom'}
        test_result = wealth_algorithm.analyze(test_questionnaire, 'france')

        health_status = {
            'service': 'wealth',
            'version': wealth_algorithm.version,
            'status': 'healthy' if test_result.get('success') else 'degraded',
            'markets_available': len(wealth_algorithm.get_supported_markets()),
            'strategies_available': len(wealth_algorithm.get_investment_strategies()),
            'criteria_count': len(wealth_algorithm.get_all_criteria()),
            'specialization': 'Financial Freedom & Wealth Optimization'
        }

        status_code = 200 if health_status['status'] == 'healthy' else 503
        return jsonify(health_status), status_code

    except Exception as e:
        logger.error(f"❌ Wealth health check failed: {e}")
        return jsonify({
            'service': 'wealth',
            'status': 'unhealthy',
            'error': str(e)
        }), 503


# Error handlers pour le blueprint
@wealth_bp.errorhandler(404)
def wealth_not_found(error):
    return jsonify({
        'error': 'Wealth endpoint not found',
        'service': 'wealth'
    }), 404


@wealth_bp.errorhandler(500)
def wealth_internal_error(error):
    return jsonify({
        'error': 'Wealth internal server error',
        'service': 'wealth'
    }), 500
