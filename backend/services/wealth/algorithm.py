"""
💰 WEALTH ALGORITHM - INTELLIGENCE PATRIMONIALE RÉVOLUTIONNAIRE
===============================================================
Algorithme de liberté financière et optimisation patrimoniale
Hérite de BaseAlgorithm pour patterns communs et évolutivité

Features:
- 34+ critères patrimoniaux personnalisables
- Analyse gap patrimoine actuel vs liberté financière
- Stratégies investissement personnalisées par profil
- Timeline réaliste vers indépendance financière
- Optimisation fiscale multi-pays

Vision: Projeter les utilisateurs vers leur liberté financière
Architecture: BaseAlgorithm + Intelligence financière révolutionnaire
"""

import json
import random
import logging
from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta

# Import depuis la racine backend
import sys
from pathlib import Path
backend_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(backend_root))

from core.base_algorithm import BaseAlgorithm
from core.data_loader import DataLoader

logger = logging.getLogger(__name__)


class WealthAlgorithm(BaseAlgorithm):
    """Algorithme Wealth moderne - Intelligence patrimoniale et liberté financière"""

    def __init__(self, data_loader: Optional[DataLoader] = None):
        # Initialiser la classe mère
        super().__init__(service_name="wealth", version="0.9.0")

        # DataLoader centralisé (prêt pour données financières)
        self.data_loader = data_loader or DataLoader()

        # 🌍 Marchés financiers internationaux
        self.wealth_markets = {
            'france': {
                'currency': 'EUR',
                'freedom_threshold': '2000€/month',
                'real_estate_roi': '4-7%',
                'stock_market_roi': '7-10%',
                'tax_optimization': ['PEA', 'Assurance-vie', 'SCPI'],
                'crypto_regulations': 'favorable',
                'retirement_age': 62,
                'social_security': 'strong'
            },
            'usa': {
                'currency': 'USD',
                'freedom_threshold': '$3500/month',
                'real_estate_roi': '6-10%',
                'stock_market_roi': '8-12%',
                'tax_optimization': ['401k', 'Roth IRA', 'HSA'],
                'crypto_regulations': 'complex',
                'retirement_age': 67,
                'social_security': 'medium'
            },
            'canada': {
                'currency': 'CAD',
                'freedom_threshold': '$3000/month',
                'real_estate_roi': '5-9%',
                'stock_market_roi': '7-11%',
                'tax_optimization': ['RRSP', 'TFSA', 'RESP'],
                'crypto_regulations': 'favorable',
                'retirement_age': 65,
                'social_security': 'strong'
            },
            'uk': {
                'currency': 'GBP',
                'freedom_threshold': '£2500/month',
                'real_estate_roi': '4-8%',
                'stock_market_roi': '6-10%',
                'tax_optimization': ['ISA', 'SIPP', 'Premium Bonds'],
                'crypto_regulations': 'regulated',
                'retirement_age': 66,
                'social_security': 'medium'
            },
            'germany': {
                'currency': 'EUR',
                'freedom_threshold': '2200€/month',
                'real_estate_roi': '3-6%',
                'stock_market_roi': '6-9%',
                'tax_optimization': ['Riester', 'Rürup', 'ETF Sparplan'],
                'crypto_regulations': 'strict',
                'retirement_age': 67,
                'social_security': 'strong'
            },
            'switzerland': {
                'currency': 'CHF',
                'freedom_threshold': '4000 CHF/month',
                'real_estate_roi': '2-5%',
                'stock_market_roi': '5-8%',
                'tax_optimization': ['Pillar 3a', 'Pillar 3b'],
                'crypto_regulations': 'favorable',
                'retirement_age': 65,
                'social_security': 'excellent'
            }
        }

        # 📊 Stratégies d'investissement types
        self.investment_strategies = {
            'conservative': {
                'name': 'Stratégie Sécurisée',
                'risk_level': 'low',
                'expected_roi': '3-5%',
                'allocation': {'bonds': 60, 'stocks': 30, 'cash': 10},
                'timeline': 'long-term',
                'suitable_for': ['risk_averse', 'near_retirement']
            },
            'balanced': {
                'name': 'Stratégie Équilibrée',
                'risk_level': 'medium',
                'expected_roi': '5-8%',
                'allocation': {'stocks': 50, 'bonds': 30, 'real_estate': 15, 'cash': 5},
                'timeline': 'medium-term',
                'suitable_for': ['balanced_risk', 'long_term_goals']
            },
            'aggressive': {
                'name': 'Stratégie Dynamique',
                'risk_level': 'high',
                'expected_roi': '8-12%',
                'allocation': {'stocks': 70, 'real_estate': 20, 'crypto': 5, 'cash': 5},
                'timeline': 'long-term',
                'suitable_for': ['young_investors', 'high_risk_tolerance']
            },
            'real_estate': {
                'name': 'Immobilier Locatif',
                'risk_level': 'medium',
                'expected_roi': '6-10%',
                'allocation': {'real_estate': 80, 'cash': 10, 'stocks': 10},
                'timeline': 'long-term',
                'suitable_for': ['tangible_assets', 'passive_income']
            }
        }

        logger.info(f"✅ Wealth Algorithm v{self.version} initialized - {len(self.wealth_markets)} markets")

    def get_specific_criteria(self) -> List[str]:
        """Critères spécifiques à Wealth (34+ critères patrimoniaux)"""
        return [
            # 💰 Revenus et cash-flow actuels
            'current_monthly_income', 'income_stability', 'income_growth_rate', 'salary_progression',
            'passive_income_current', 'rental_income', 'dividend_income', 'business_income',

            # 🏠 Patrimoine immobilier
            'primary_residence_value', 'mortgage_remaining', 'rental_properties_count',
            'rental_properties_value', 'real_estate_debt', 'property_maintenance_costs',

            # 📈 Investissements financiers
            'stock_portfolio_value', 'bonds_portfolio', 'crypto_holdings', 'cash_savings',
            'retirement_accounts', 'emergency_fund_months', 'investment_diversification',

            # 🎯 Objectifs de liberté financière
            'target_monthly_expenses', 'desired_lifestyle_cost', 'retirement_age_target',
            'financial_freedom_timeline', 'legacy_planning', 'luxury_goals',

            # 🛡️ Protection et risques
            'insurance_coverage', 'health_insurance', 'life_insurance', 'disability_insurance',
            'risk_tolerance', 'investment_experience', 'market_volatility_comfort',

            # 🌍 Optimisation fiscale et géographique
            'current_tax_rate', 'tax_optimization_interest', 'offshore_banking',
            'residency_planning', 'inheritance_planning', 'wealth_protection_strategies'
        ]

    def analyze(self, questionnaire: Dict, country: str = "france") -> Dict:
        """
        Analyse principale Wealth - Roadmap vers liberté financière
        Implémentation de la méthode abstraite BaseAlgorithm
        """
        try:
            # Validation questionnaire (héritée)
            if not self.validate_questionnaire(questionnaire):
                return {"error": "Invalid questionnaire", "recommendations": []}

            # Cache check
            cache_key = f"wealth_{country}_{len(questionnaire)}"
            cached_result = self.get_cached_result(cache_key)
            if cached_result:
                logger.info("📦 Returning cached Wealth result")
                return cached_result

            # 1. Analyser situation financière actuelle
            current_wealth = self._analyze_current_wealth(questionnaire)

            # 2. Définir objectifs de liberté financière
            freedom_targets = self._calculate_freedom_targets(questionnaire, country)

            # 3. Gap analysis patrimoine
            wealth_gaps = self._analyze_wealth_gaps(current_wealth, freedom_targets)

            # 4. Recommandations stratégies personnalisées
            strategies = self._recommend_wealth_strategies(wealth_gaps, current_wealth, country)

            # 5. Calculer timeline réaliste
            timeline = self._calculate_freedom_timeline(wealth_gaps, strategies, current_wealth)

            # 6. Optimisations fiscales
            tax_optimizations = self._recommend_tax_optimizations(country, current_wealth)

            # 7. Préparer résultat final
            result = {
                "success": True,
                "wealth_analysis": {
                    "current_wealth_score": current_wealth.get('wealth_score', 45),
                    "financial_health": current_wealth.get('health_status', 'developing'),
                    "monthly_cash_flow": current_wealth.get('monthly_surplus', 0),
                    "net_worth_estimate": current_wealth.get('net_worth', 0)
                },
                "freedom_targets": {
                    "target_passive_income": freedom_targets.get('monthly_target', 2000),
                    "target_net_worth": freedom_targets.get('net_worth_needed', 500000),
                    "lifestyle_cost": freedom_targets.get('lifestyle_cost', 2500),
                    "freedom_age": freedom_targets.get('target_age', 55)
                },
                "wealth_recommendations": strategies[:3],  # TOP 3 strategies
                "timeline_analysis": {
                    "years_to_freedom": timeline.get('years_needed', 15),
                    "monthly_savings_needed": timeline.get('monthly_savings', 800),
                    "investment_growth_required": timeline.get('roi_needed', 0.07),
                    "milestones": timeline.get('milestones', [])
                },
                "tax_optimization": tax_optimizations[:3],
                "market_insights": {
                    "country": country,
                    "market_data": self.wealth_markets.get(country, {}),
                    "economic_outlook": self._get_economic_outlook(country)
                },
                "algorithm_version": f"Wealth {self.version}",
                "analysis_date": datetime.now().strftime("%Y-%m-%d")
            }

            # Cache et logs
            self.cache_result(cache_key, result, ttl_minutes=120)  # Cache plus long pour wealth
            self.log_calculation(len(questionnaire), len(strategies), country)

            return result

        except Exception as e:
            logger.error(f"❌ Wealth analysis error: {e}")
            return {"error": str(e), "wealth_recommendations": []}

    def calculate_score(self, wealth_data: Dict, questionnaire: Dict) -> float:
        """
        Calcule le score de santé financière global
        Implémentation de la méthode abstraite BaseAlgorithm
        """
        # Facteurs de scoring financier
        income_stability = wealth_data.get('income_stability', 0.5)
        savings_rate = wealth_data.get('savings_rate', 0.1)
        debt_ratio = wealth_data.get('debt_ratio', 0.3)
        investment_diversification = wealth_data.get('diversification_score', 0.5)
        emergency_fund_months = wealth_data.get('emergency_months', 3)

        # Calcul score composite
        stability_score = income_stability * 20
        savings_score = min(savings_rate * 200, 25)  # Max 25 points pour 12.5%+ savings
        debt_score = max(0, (1 - debt_ratio) * 20)  # Moins de dette = mieux
        diversification_score = investment_diversification * 15
        emergency_score = min(emergency_fund_months * 4, 20)  # Max 20 points pour 5+ mois

        # Score final normalisé (0-100)
        total_score = stability_score + savings_score + debt_score + diversification_score + emergency_score
        final_score = self.normalize_score(total_score, 0, 100)

        return final_score

    def _analyze_current_wealth(self, questionnaire: Dict) -> Dict:
        """Analyse la situation financière actuelle"""
        wealth_profile = {
            'monthly_income': 3000,
            'monthly_expenses': 2500,
            'monthly_surplus': 500,
            'net_worth': 50000,
            'savings_rate': 0.15,
            'debt_ratio': 0.2,
            'wealth_score': 60,
            'health_status': 'developing'
        }

        # Extraction des données du questionnaire
        for key, response in questionnaire.items():
            response_text = str(response).lower() if not isinstance(response, dict) else str(response.get('value', '')).lower()

            # Détection revenus
            if 'income' in key or 'salary' in key or 'revenu' in key:
                try:
                    # Extraire montant numérique
                    import re
                    numbers = re.findall(r'\d+', response_text)
                    if numbers:
                        wealth_profile['monthly_income'] = int(numbers[0])
                except:
                    pass

            # Détection épargne
            if any(word in response_text for word in ['save', 'épargne', 'invest']):
                if any(word in response_text for word in ['high', 'much', 'beaucoup']):
                    wealth_profile['savings_rate'] = 0.25
                elif any(word in response_text for word in ['little', 'peu', 'difficile']):
                    wealth_profile['savings_rate'] = 0.05

        # Calculer métriques dérivées
        wealth_profile['monthly_expenses'] = wealth_profile['monthly_income'] * (1 - wealth_profile['savings_rate'])
        wealth_profile['monthly_surplus'] = wealth_profile['monthly_income'] - wealth_profile['monthly_expenses']

        # Score de santé financière
        if wealth_profile['savings_rate'] > 0.2:
            wealth_profile['health_status'] = 'excellent'
            wealth_profile['wealth_score'] = 85
        elif wealth_profile['savings_rate'] > 0.15:
            wealth_profile['health_status'] = 'good'
            wealth_profile['wealth_score'] = 70
        elif wealth_profile['savings_rate'] > 0.1:
            wealth_profile['health_status'] = 'developing'
            wealth_profile['wealth_score'] = 55
        else:
            wealth_profile['health_status'] = 'needs_improvement'
            wealth_profile['wealth_score'] = 35

        return wealth_profile

    def _calculate_freedom_targets(self, questionnaire: Dict, country: str) -> Dict:
        """Calcule les objectifs de liberté financière personnalisés"""
        market_data = self.wealth_markets.get(country, self.wealth_markets['france'])

        # Objectifs par défaut basés sur le pays
        base_monthly_target = int(market_data['freedom_threshold'].replace('€', '').replace('$', '').replace('£', '').replace('CHF', '').replace('/month', ''))

        targets = {
            'monthly_target': base_monthly_target,
            'annual_target': base_monthly_target * 12,
            'net_worth_needed': base_monthly_target * 12 * 25,  # Règle des 4% (25x annual expenses)
            'lifestyle_cost': int(base_monthly_target * 1.2),
            'target_age': 55
        }

        # Ajustements selon les réponses
        for key, response in questionnaire.items():
            response_text = str(response).lower() if not isinstance(response, dict) else str(response.get('value', '')).lower()

            # Détection objectifs lifestyle
            if any(word in response_text for word in ['luxury', 'luxe', 'premium']):
                targets['monthly_target'] = int(targets['monthly_target'] * 1.5)
                targets['lifestyle_cost'] = int(targets['lifestyle_cost'] * 1.8)
            elif any(word in response_text for word in ['simple', 'modest', 'basic']):
                targets['monthly_target'] = int(targets['monthly_target'] * 0.8)
                targets['lifestyle_cost'] = int(targets['lifestyle_cost'] * 0.7)

            # Détection âge cible
            if 'retire' in key or 'retirement' in key or 'retraite' in key:
                if 'early' in response_text or 'tôt' in response_text:
                    targets['target_age'] = 45
                elif 'late' in response_text or 'tard' in response_text:
                    targets['target_age'] = 65

        # Recalculer net worth nécessaire
        targets['net_worth_needed'] = targets['monthly_target'] * 12 * 25

        return targets

    def _analyze_wealth_gaps(self, current_wealth: Dict, freedom_targets: Dict) -> Dict:
        """Analyse les gaps entre situation actuelle et objectifs"""
        gaps = {
            'income_gap': max(0, freedom_targets['monthly_target'] - current_wealth.get('monthly_surplus', 0)),
            'net_worth_gap': max(0, freedom_targets['net_worth_needed'] - current_wealth.get('net_worth', 0)),
            'savings_rate_needed': 0.2,  # Minimum recommandé
            'investment_growth_required': 0.07,  # 7% annuel
            'priority_areas': []
        }

        # Identifier zones prioritaires
        if current_wealth.get('savings_rate', 0) < 0.15:
            gaps['priority_areas'].append('increase_savings_rate')

        if current_wealth.get('monthly_surplus', 0) < 500:
            gaps['priority_areas'].append('increase_income')

        if current_wealth.get('net_worth', 0) < 10000:
            gaps['priority_areas'].append('build_emergency_fund')

        return gaps

    def _recommend_wealth_strategies(self, wealth_gaps: Dict, current_wealth: Dict, country: str) -> List[Dict]:
        """Recommande des stratégies personnalisées"""
        strategies = []

        # Stratégies basées sur les gaps identifiés
        if 'build_emergency_fund' in wealth_gaps.get('priority_areas', []):
            strategies.append({
                'name': 'Fonds d\'urgence prioritaire',
                'type': 'emergency_fund',
                'description': 'Constituer 6 mois de frais de fonctionnement',
                'target_amount': current_wealth.get('monthly_expenses', 2500) * 6,
                'timeline': '12-18 mois',
                'risk_level': 'very_low',
                'expected_return': '2-3%',
                'priority': 'critical',
                'actions': [
                    'Ouvrir compte épargne séparé',
                    'Automatiser virement mensuel',
                    'Cibler livrets défiscalisés'
                ]
            })

        if 'increase_savings_rate' in wealth_gaps.get('priority_areas', []):
            strategies.append({
                'name': 'Optimisation budget et épargne',
                'type': 'savings_optimization',
                'description': 'Augmenter le taux d\'épargne à 20-25%',
                'target_amount': current_wealth.get('monthly_income', 3000) * 0.25,
                'timeline': '6 mois',
                'risk_level': 'none',
                'expected_return': 'guaranteed_savings',
                'priority': 'high',
                'actions': [
                    'Analyser et réduire dépenses non-essentielles',
                    'Automatiser épargne dès réception salaire',
                    'Négocier contrats (assurance, téléphone, etc.)'
                ]
            })

        # Stratégies d'investissement selon profil
        market_data = self.wealth_markets.get(country, {})

        strategies.append({
            'name': 'Portefeuille diversifié croissance',
            'type': 'investment_portfolio',
            'description': 'Investissement équilibré actions/obligations',
            'target_amount': wealth_gaps.get('net_worth_gap', 100000),
            'timeline': '10-15 ans',
            'risk_level': 'medium',
            'expected_return': '6-8% annuel',
            'priority': 'medium',
            'actions': [
                f'Ouvrir {market_data.get("tax_optimization", ["compte titres"])[0]}',
                'Diversifier sur ETFs monde',
                'Investir régulièrement (DCA)'
            ]
        })

        if current_wealth.get('net_worth', 0) > 50000:
            strategies.append({
                'name': 'Immobilier locatif',
                'type': 'real_estate',
                'description': 'Investissement immobilier pour revenus passifs',
                'target_amount': 100000,
                'timeline': '2-5 ans',
                'risk_level': 'medium',
                'expected_return': market_data.get('real_estate_roi', '5-8%'),
                'priority': 'medium',
                'actions': [
                    'Étudier marchés locatifs rentables',
                    'Optimiser financement bancaire',
                    'Déléguer gestion locative'
                ]
            })

        return strategies

    def _calculate_freedom_timeline(self, wealth_gaps: Dict, strategies: List[Dict], current_wealth: Dict) -> Dict:
        """Calcule la timeline réaliste vers liberté financière"""
        monthly_surplus = current_wealth.get('monthly_surplus', 500)
        net_worth_gap = wealth_gaps.get('net_worth_gap', 400000)

        # Calcul simplifié avec croissance composée
        if monthly_surplus > 0:
            annual_savings = monthly_surplus * 12
            # Avec croissance 7% annuelle
            years_needed = max(1, int(net_worth_gap / (annual_savings * 1.07)))
        else:
            years_needed = 25  # Par défaut si pas d'épargne

        timeline = {
            'years_needed': min(years_needed, 30),  # Max 30 ans
            'monthly_savings': monthly_surplus,
            'roi_needed': 0.07,
            'milestones': [
                {
                    'year': 2,
                    'target': 'Fonds d\'urgence constitué',
                    'amount': current_wealth.get('monthly_expenses', 2500) * 6
                },
                {
                    'year': 5,
                    'target': 'Premier palier patrimoine',
                    'amount': 100000
                },
                {
                    'year': 10,
                    'target': 'Mi-parcours liberté financière',
                    'amount': net_worth_gap // 2
                }
            ]
        }

        return timeline

    def _recommend_tax_optimizations(self, country: str, current_wealth: Dict) -> List[Dict]:
        """Recommande optimisations fiscales par pays"""
        market_data = self.wealth_markets.get(country, {})
        tax_tools = market_data.get('tax_optimization', ['compte standard'])

        optimizations = []

        for tool in tax_tools[:3]:  # TOP 3 outils
            optimizations.append({
                'tool': tool,
                'description': f'Optimisation fiscale via {tool}',
                'annual_benefit': '1000-3000€',
                'eligibility': 'selon revenus',
                'complexity': 'medium'
            })

        return optimizations

    def _get_economic_outlook(self, country: str) -> Dict:
        """Perspectives économiques par pays"""
        outlooks = {
            'france': {
                'inflation_forecast': '2-3%',
                'interest_rates_trend': 'stable',
                'real_estate_outlook': 'modéré',
                'stock_market_outlook': 'positif'
            },
            'usa': {
                'inflation_forecast': '2-4%',
                'interest_rates_trend': 'rising',
                'real_estate_outlook': 'mixed',
                'stock_market_outlook': 'optimiste'
            }
        }

        return outlooks.get(country, outlooks['france'])

    def get_supported_markets(self) -> List[str]:
        """Retourne la liste des marchés financiers supportés"""
        return list(self.wealth_markets.keys())

    def get_investment_strategies(self) -> List[str]:
        """Retourne la liste des stratégies d'investissement"""
        return list(self.investment_strategies.keys())

    def get_algorithm_info(self) -> Dict:
        """Informations détaillées sur l'algorithme Wealth"""
        base_stats = self.get_algorithm_stats()

        wealth_stats = {
            'supported_markets': len(self.wealth_markets),
            'investment_strategies': len(self.investment_strategies),
            'wealth_criteria': len([c for c in self.get_specific_criteria() if c in ['current_monthly_income', 'target_monthly_expenses']]),
            'specialization': 'Financial Freedom & Wealth Intelligence'
        }

        return {**base_stats, **wealth_stats}
