#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🇹🇭 THAILAND RESIDENTS ALGORITHM
Revolutionary Platform - Pattern UK 2025 Standardized
Inclusive algorithm for Thailand residents seeking new cities within Thailand
30 cities, 27 criteria, 12 questions - Regional filtering with tropical innovations
"""

import json
import logging
from typing import Dict, List, Any, Optional
from dataclasses import dataclass

# Configuration logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class UserProfileThailand:
    """🇹🇭 Profil utilisateur Thailand avec critères inclusifs"""
    region_preference: str           # Q1 - Filtrage géographique 5 régions
    main_priority: str               # Q2 - Priorité vie principale
    monthly_budget: str              # Q3 - Budget THB mensuel
    work_environment: str            # Q4 - Environnement professionnel
    climate_adaptation: str          # Q5 - Adaptation climat tropical
    transport_preferences: List[str] # Q6 - Mobilité (multiple)
    essential_services: List[str]    # Q7 - Services essentiels (multiple)
    cultural_interests: List[str]    # Q8 - Intérêts culturels (multiple)
    social_scene: str                # Q9 - Vie sociale
    street_food_importance: str      # Q10 - Street food (signature Thailand)
    nature_urban_balance: str        # Q11 - Équilibre nature/ville
    deal_breakers: List[str]         # Q12 - Éléments rédhibitoires (multiple)
    criteria_weights: Dict[str, float]  # Poids calculés dynamiquement

class ThailandResidentsAlgorithm:
    """🇹🇭 Algorithme de recommandation pour résidents Thailand"""

    def __init__(self, cities_data_path: str):
        """Initialise l'algorithme avec les données des 30 villes thailand"""
        self.version = "1.0.0"  # ⚠️ OBLIGATOIRE pour health check
        self.cities_data = self.load_cities_data(cities_data_path)
        self.criteria_weights_base = self.get_base_criteria_weights_thailand()
        logger.info(f"🇹🇭 ThailandResidentsAlgorithm v{self.version} initialisé")

    def load_cities_data(self, data_path: str) -> Dict:
        """Charge les données des 30 villes thailand"""
        try:
            with open(data_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            logger.info(f"🇹🇭 Données Thailand chargées: {len(data['cities'])} villes")
            return data
        except Exception as e:
            logger.error(f"❌ Erreur chargement données Thailand: {e}")
            return {"cities": [], "metadata": {}, "criteria_definitions": {}}

    def get_base_criteria_weights_thailand(self) -> Dict[str, float]:
        """⚖️ Poids de base des 27 critères Thailand (24 actifs + 3 exclus)"""
        return {
            # 💰 Critères Économiques
            "cost_of_living": 1.0,
            "job_opportunities": 1.0,
            "salary_potential": 1.0,
            "housing_availability": 1.0,

            # 🏗️ Critères Infrastructure
            "public_transport": 1.0,
            "healthcare_quality": 1.0,
            "education_quality": 1.0,
            "international_connectivity": 1.0,

            # 🌍 Critères Environnement
            "climate_quality": 1.0,
            "air_quality": 1.0,
            "nature_access": 1.0,
            "beach_access": 1.0,
            "mountain_access": 1.0,
            "tropical_climate_adaptation": 1.0,  # 🌡️ Thailand-spécifique

            # 🎭 Critères Socioculturels
            "cultural_scene": 1.0,
            "nightlife": 1.0,
            "youth_scene": 1.0,
            "sports_recreation": 1.0,
            "family_friendliness": 1.0,
            "street_food_culture": 1.0,  # 🍜 Thailand signature

            # 💼 Critères Business
            "business_environment": 1.0,
            "startup_ecosystem": 1.0,
            "tech_scene": 1.0,

            # 🛡️ Critères Sécurité
            "safety_security": 1.0,

            # ❌ Critères exclus (non-inclusifs)
            # "language_diversity": 0.0,        # Exclus pour inclusivité
            # "visa_business_friendliness": 0.0, # Exclus pour inclusivité
            # "expat_community_presence": 0.0,   # Exclus pour inclusivité
        }

    def create_user_profile_thailand(self, questionnaire_responses: Dict) -> UserProfileThailand:
        """🧠 Crée profil utilisateur thailand à partir des réponses"""

        # Extraction réponses questionnaire
        region_preference = questionnaire_responses.get('thailand_region_preference', 'region_flexible')
        main_priority = questionnaire_responses.get('thailand_main_priority', 'balanced_lifestyle')
        monthly_budget = questionnaire_responses.get('thailand_budget_monthly', 'budget_moderate')
        work_environment = questionnaire_responses.get('thailand_work_environment', 'freelance_remote')
        climate_adaptation = questionnaire_responses.get('thailand_climate_adaptation', 'climate_adaptable')

        # Questions multiples (listes)
        transport_preferences = questionnaire_responses.get('thailand_mobility_transport', ['public_transport'])
        essential_services = questionnaire_responses.get('thailand_essential_services', ['all_essential'])
        cultural_interests = questionnaire_responses.get('thailand_cultural_interests', ['temples_heritage'])
        deal_breakers = questionnaire_responses.get('thailand_deal_breakers', ['no_dealbreakers'])

        social_scene = questionnaire_responses.get('thailand_social_scene', 'mixed_balanced')
        street_food_importance = questionnaire_responses.get('thailand_street_food_importance', 'food_moderate')
        nature_urban_balance = questionnaire_responses.get('thailand_nature_urban_balance', 'urban_green')

        # Initialiser poids de base
        weights = self.criteria_weights_base.copy()

        # === AJUSTEMENTS PAR PRIORITÉ PRINCIPALE ===
        if main_priority == 'career_growth':
            weights['job_opportunities'] *= 1.8
            weights['business_environment'] *= 1.6
            weights['startup_ecosystem'] *= 1.5
            weights['tech_scene'] *= 1.4
            weights['salary_potential'] *= 1.3
        elif main_priority == 'cultural_immersion':
            weights['cultural_scene'] *= 1.9
            weights['street_food_culture'] *= 1.7
            weights['sports_recreation'] *= 1.4
            weights['nature_access'] *= 1.2
        elif main_priority == 'family_life':
            weights['family_friendliness'] *= 1.8
            weights['education_quality'] *= 1.7
            weights['healthcare_quality'] *= 1.6
            weights['safety_security'] *= 1.5
            weights['housing_availability'] *= 1.3
        elif main_priority == 'social_nightlife':
            weights['nightlife'] *= 1.9
            weights['youth_scene'] *= 1.6
            weights['cultural_scene'] *= 1.3
        elif main_priority == 'balanced_lifestyle':
            # Équilibré - pas de boost majeur
            weights['climate_quality'] *= 1.2
            weights['tropical_climate_adaptation'] *= 1.2

        # === AJUSTEMENTS PAR BUDGET THB ===
        if monthly_budget == 'budget_tight':  # 20-40K THB
            weights['cost_of_living'] *= 1.9
            weights['housing_availability'] *= 1.6
            weights['street_food_culture'] *= 1.4
        elif monthly_budget == 'budget_luxury':  # 120K+ THB
            weights['cost_of_living'] *= 0.6  # Moins important
            weights['international_connectivity'] *= 1.4
            weights['healthcare_quality'] *= 1.3

        # === AJUSTEMENTS TRAVAIL ===
        if work_environment == 'corporate_business':
            weights['business_environment'] *= 1.7
            weights['international_connectivity'] *= 1.5
            weights['public_transport'] *= 1.3
        elif work_environment == 'startup_tech':
            weights['startup_ecosystem'] *= 1.8
            weights['tech_scene'] *= 1.7
            weights['youth_scene'] *= 1.3
        elif work_environment == 'freelance_remote':
            weights['tropical_climate_adaptation'] *= 1.4
            weights['cost_of_living'] *= 1.3
            weights['nature_access'] *= 1.2

        # === AJUSTEMENTS CLIMAT TROPICAL (Innovation Thailand) ===
        if climate_adaptation == 'climate_lover':
            weights['tropical_climate_adaptation'] *= 1.8
            weights['beach_access'] *= 1.4
            weights['air_quality'] *= 1.2
        elif climate_adaptation == 'climate_moderate':
            weights['mountain_access'] *= 1.6
            weights['air_quality'] *= 1.4
            weights['nature_access'] *= 1.3
        elif climate_adaptation == 'climate_sensitive':
            weights['air_quality'] *= 2.0
            weights['mountain_access'] *= 1.7
            weights['tropical_climate_adaptation'] *= 1.5

        # === AJUSTEMENTS TRANSPORT ===
        if 'public_transport' in transport_preferences:
            weights['public_transport'] *= 1.6
        if 'motorbike' in transport_preferences:
            # Thailand-spécifique - moins de besoin transport public
            weights['public_transport'] *= 0.8
        if 'walking_cycling' in transport_preferences:
            weights['air_quality'] *= 1.4
            weights['nature_access'] *= 1.2

        # === AJUSTEMENTS SERVICES ===
        if 'healthcare_quality' in essential_services:
            weights['healthcare_quality'] *= 1.7
        if 'education_schools' in essential_services:
            weights['education_quality'] *= 1.7
        if 'safety_security' in essential_services:
            weights['safety_security'] *= 1.7

        # === AJUSTEMENTS CULTURE ===
        if 'temples_heritage' in cultural_interests:
            weights['cultural_scene'] *= 1.5
        if 'sports_recreation' in cultural_interests:
            weights['sports_recreation'] *= 1.6
        if 'nature_outdoor' in cultural_interests:
            weights['nature_access'] *= 1.5
            weights['mountain_access'] *= 1.3

        # === AJUSTEMENTS SOCIAL ===
        if social_scene == 'university_youth':
            weights['youth_scene'] *= 1.7
            weights['education_quality'] *= 1.3
        elif social_scene == 'nightlife_party':
            weights['nightlife'] *= 1.8
            weights['youth_scene'] *= 1.4
        elif social_scene == 'family_community':
            weights['family_friendliness'] *= 1.6
            weights['safety_security'] *= 1.4

        # === AJUSTEMENTS STREET FOOD (Innovation Thailand) ===
        if street_food_importance == 'food_essential':
            weights['street_food_culture'] *= 2.0  # BOOST MAJEUR
        elif street_food_importance == 'food_important':
            weights['street_food_culture'] *= 1.6
        elif street_food_importance == 'food_careful':
            weights['street_food_culture'] *= 0.7
        elif street_food_importance == 'food_restaurants':
            weights['street_food_culture'] *= 0.3  # MALUS street food

        # === AJUSTEMENTS NATURE/VILLE ===
        if nature_urban_balance == 'pure_nature':
            weights['nature_access'] *= 1.8
            weights['mountain_access'] *= 1.5
            weights['air_quality'] *= 1.4
        elif nature_urban_balance == 'beach_paradise':
            weights['beach_access'] *= 2.0
            weights['sports_recreation'] *= 1.4
        elif nature_urban_balance == 'mountain_fresh':
            weights['mountain_access'] *= 1.9
            weights['air_quality'] *= 1.6
            weights['tropical_climate_adaptation'] *= 1.3
        elif nature_urban_balance == 'full_urban':
            weights['business_environment'] *= 1.4
            weights['public_transport'] *= 1.3
            weights['nightlife'] *= 1.2

        # === AJUSTEMENTS DEAL BREAKERS ===
        if 'pollution_air' in deal_breakers:
            weights['air_quality'] *= 2.5  # CRITIQUE
        if 'high_cost' in deal_breakers:
            weights['cost_of_living'] *= 2.2
        if 'poor_transport' in deal_breakers:
            weights['public_transport'] *= 2.0
        if 'safety_concerns' in deal_breakers:
            weights['safety_security'] *= 2.3

        return UserProfileThailand(
            region_preference=region_preference,
            main_priority=main_priority,
            monthly_budget=monthly_budget,
            work_environment=work_environment,
            climate_adaptation=climate_adaptation,
            transport_preferences=transport_preferences,
            essential_services=essential_services,
            cultural_interests=cultural_interests,
            social_scene=social_scene,
            street_food_importance=street_food_importance,
            nature_urban_balance=nature_urban_balance,
            deal_breakers=deal_breakers,
            criteria_weights=weights
        )

    def apply_regional_filters(self, cities_list: List[Dict], user_profile: UserProfileThailand) -> List[Dict]:
        """🗺️ Applique filtres régionaux Thailand AVANT scoring (Performance Boost)"""

        # Pas de filtre régional pour ces préférences
        if user_profile.region_preference in ['region_flexible', 'any_region']:
            return cities_list

        filtered_cities = []

        for city in cities_list:
            city_region = city.get('region', 'Unknown')

            # Mapping région preference → région JSON
            region_match = False

            if user_profile.region_preference == 'central_plains':
                region_match = city_region == 'Central Plains'
            elif user_profile.region_preference == 'northern_mountains':
                region_match = city_region == 'Northern Mountains'
            elif user_profile.region_preference == 'southern_beaches':
                region_match = city_region == 'Southern Beaches'
            elif user_profile.region_preference == 'eastern_seaboard':
                region_match = city_region == 'Eastern Seaboard'
            elif user_profile.region_preference == 'northeast_isan':
                region_match = city_region == 'Northeast Isan'

            if region_match:
                filtered_cities.append(city)

        logger.info(f"🔍 Filtrage régional Thailand: {len(filtered_cities)}/{len(cities_list)} villes conservées")
        return filtered_cities

    def calculate_city_score_thailand(self, city: Dict, user_profile: UserProfileThailand) -> float:
        """🧮 Calcule le score d'une ville thailand selon le profil utilisateur"""

        city_scores = city.get('scores', {})
        total_score = 0.0
        total_weight = 0.0

        for criterion, weight in user_profile.criteria_weights.items():
            if weight > 0 and criterion in city_scores:
                criterion_score = city_scores[criterion]
                weighted_score = criterion_score * weight
                total_score += weighted_score
                total_weight += weight

        if total_weight == 0:
            return 0.0

        return total_score / total_weight

    def apply_thailand_bonuses(self, city: Dict, base_score: float, user_profile: UserProfileThailand) -> float:
        """🎯 Applique bonus/malus Thailand-spécifiques"""

        final_score = base_score
        city_scores = city.get('scores', {})
        city_name = city.get('name', 'Unknown')

        # === BONUS STREET FOOD EXCEPTIONAL ===
        if user_profile.street_food_importance == 'food_essential':
            street_food_score = city_scores.get('street_food_culture', 0)
            if street_food_score >= 0.95:  # Paradise culinaire
                final_score *= 1.15
                logger.info(f"🍜 BONUS Street Food Paradise: {city_name} (+15%)")

        # === BONUS CLIMAT TROPICAL PARFAIT ===
        if user_profile.climate_adaptation == 'climate_lover':
            tropical_score = city_scores.get('tropical_climate_adaptation', 0)
            if tropical_score >= 0.9:
                final_score *= 1.12
                logger.info(f"🌡️ BONUS Climat Tropical Parfait: {city_name} (+12%)")

        # === BONUS NATURE ACCESS EXCEPTIONAL ===
        if user_profile.nature_urban_balance in ['pure_nature', 'beach_paradise', 'mountain_fresh']:
            nature_score = city_scores.get('nature_access', 0)
            beach_score = city_scores.get('beach_access', 0)
            mountain_score = city_scores.get('mountain_access', 0)

            if user_profile.nature_urban_balance == 'beach_paradise' and beach_score >= 0.95:
                final_score *= 1.18
                logger.info(f"🏖️ BONUS Beach Paradise: {city_name} (+18%)")
            elif user_profile.nature_urban_balance == 'mountain_fresh' and mountain_score >= 0.9:
                final_score *= 1.16
                logger.info(f"🏔️ BONUS Mountain Fresh: {city_name} (+16%)")
            elif nature_score >= 0.9:
                final_score *= 1.10
                logger.info(f"🌿 BONUS Nature Access: {city_name} (+10%)")

        # === MALUS AIR QUALITY POUR SENSIBLES ===
        if user_profile.climate_adaptation == 'climate_sensitive':
            air_quality = city_scores.get('air_quality', 1.0)
            if air_quality < 0.6:
                final_score *= 0.85
                logger.info(f"💨 MALUS Air Quality: {city_name} (-15%)")

        # === BONUS BUSINESS CAPITAL ===
        if user_profile.work_environment == 'corporate_business':
            economic_zone = city.get('economic_zone', '')
            if economic_zone == 'business_capital':  # Bangkok
                final_score *= 1.20
                logger.info(f"🏢 BONUS Business Capital: {city_name} (+20%)")

        return min(final_score, 1.0)  # Cap à 1.0

    def get_city_strengths_thailand(self, city_data: Dict, user_profile: UserProfileThailand) -> List[str]:
        """💪 Identifie les forces principales d'une ville thailand"""

        strengths = []
        scores = city_data['scores']
        city_name = city_data['name']

        # Strengths génériques par score élevé
        if scores.get('street_food_culture', 0) >= 0.95:
            strengths.append("Paradise culinaire street food")
        if scores.get('beach_access', 0) >= 0.9:
            strengths.append("Accès plages paradisiaques")
        if scores.get('mountain_access', 0) >= 0.9:
            strengths.append("Accès montagne exceptionnel")
        if scores.get('cultural_scene', 0) >= 0.9:
            strengths.append("Richesse culturelle temples/heritage")
        if scores.get('tropical_climate_adaptation', 0) >= 0.9:
            strengths.append("Infrastructure tropical parfaite")
        if scores.get('cost_of_living', 0) >= 0.9:
            strengths.append("Très économique")
        if scores.get('business_environment', 0) >= 0.85:
            strengths.append("Écosystème business dynamique")
        if scores.get('safety_security', 0) >= 0.9:
            strengths.append("Sécurité excellente")
        if scores.get('nature_access', 0) >= 0.9:
            strengths.append("Nature/parcs nationaux proches")

        return strengths[:4]  # Top 4 strengths

    def get_city_concerns_thailand(self, city_data: Dict, user_profile: UserProfileThailand) -> List[str]:
        """⚠️ Identifie les préoccupations potentielles d'une ville thailand"""

        concerns = []
        scores = city_data['scores']

        # Concerns par scores faibles
        if scores.get('air_quality', 1.0) < 0.6:
            concerns.append("Qualité air dégradée")
        if scores.get('cost_of_living', 1.0) < 0.6:
            concerns.append("Coût de la vie élevé")
        if scores.get('public_transport', 1.0) < 0.6:
            concerns.append("Transport public limité")
        if scores.get('job_opportunities', 1.0) < 0.6:
            concerns.append("Marché emploi restreint")
        if scores.get('healthcare_quality', 1.0) < 0.7:
            concerns.append("Qualité santé moyenne")
        if scores.get('international_connectivity', 1.0) < 0.6:
            concerns.append("Connectivité internationale limitée")

        return concerns[:3]  # Top 3 concerns

    def generate_recommendation_reason_thailand(self, city_data: Dict, user_profile: UserProfileThailand) -> str:
        """📝 Génère raison personnalisée pour recommandation thailand"""

        city_name = city_data['name']
        main_priority = user_profile.main_priority

        if main_priority == 'career_growth':
            return f"{city_name} offre d'excellentes opportunités de carrière dans un environnement business dynamique."
        elif main_priority == 'cultural_immersion':
            return f"{city_name} vous plongera dans l'authentique culture thai avec temples, festivals et patrimoine."
        elif main_priority == 'family_life':
            return f"{city_name} combine sécurité, écoles de qualité et environnement family-friendly."
        elif main_priority == 'social_nightlife':
            return f"{city_name} propose une vie nocturne vibrante avec bars, restaurants et événements sociaux."
        else:
            return f"{city_name} offre l'équilibre parfait pour votre nouvelle vie en Thailande."

    def get_top_recommendations_thailand(self, questionnaire_responses: Dict, top_n: int = 3) -> List[Dict]:
        """🏆 Retourne les top N recommandations de villes thailand"""

        try:
            # Créer profil utilisateur
            user_profile = self.create_user_profile_thailand(questionnaire_responses)
            logger.info(f"🇹🇭 Profil Thailand créé: {user_profile.main_priority}, région={user_profile.region_preference}")

            # ÉTAPE 1: Appliquer filtres régionaux
            all_cities = self.cities_data.get('cities', [])
            filtered_cities = self.apply_regional_filters(all_cities, user_profile)

            if len(filtered_cities) == 0:
                logger.warning("❌ Aucune ville ne correspond aux filtres régionaux Thailand")
                return []

            # ÉTAPE 2: Calculer scores pour les villes filtrées
            city_scores = []
            for city in filtered_cities:
                # Score de base
                base_score = self.calculate_city_score_thailand(city, user_profile)

                # Appliquer bonus/malus Thailand
                final_score = self.apply_thailand_bonuses(city, base_score, user_profile)

                city_scores.append({
                    'city_data': city,
                    'score': final_score
                })

            # Trier par score décroissant
            city_scores.sort(key=lambda x: x['score'], reverse=True)

            # Générer recommandations finales
            recommendations = []
            for i, city_score in enumerate(city_scores[:top_n]):
                city_data = city_score['city_data']
                score = city_score['score']

                recommendation = {
                    'city': city_data['name'],
                    'region': city_data['region'],
                    'score_percentage': round(score * 100, 1),
                    'population': city_data.get('population', 'N/A'),
                    'coordinates': city_data.get('coordinates', {}),
                    'economic_zone': city_data.get('economic_zone', 'unknown'),
                    'strengths': self.get_city_strengths_thailand(city_data, user_profile),
                    'concerns': self.get_city_concerns_thailand(city_data, user_profile),
                    'recommendation_reason': self.generate_recommendation_reason_thailand(city_data, user_profile),
                    'rank': i + 1
                }
                recommendations.append(recommendation)

            logger.info(f"🏆 Top {len(recommendations)} recommandations Thailand générées (sur {len(filtered_cities)} villes filtrées)")
            return recommendations

        except Exception as e:
            logger.error(f"❌ Erreur génération recommandations Thailand: {e}")
            return []

    def get_recommendations(self, questionnaire_responses: Dict, top_n: int = 3) -> Dict:
        """🏆 Interface standardisée UK 2025 - API principale Thailand"""

        try:
            # Obtenir les recommandations top N
            raw_recommendations = self.get_top_recommendations_thailand(questionnaire_responses, top_n)

            if not raw_recommendations:
                return {
                    'status': 'error',
                    'recommendations': [],
                    'message': 'Aucune recommandation disponible pour vos critères Thailand'
                }

            # Formatter pour l'API standardisée
            formatted_recommendations = []
            for rec in raw_recommendations:
                formatted_rec = {
                    'city': rec['city'],
                    'region': rec['region'],
                    'score_percentage': rec['score_percentage'],
                    'population': rec['population'],
                    'coordinates': rec.get('coordinates', {}),
                    'economic_zone': rec.get('economic_zone', 'unknown'),
                    'strengths': rec.get('strengths', []),
                    'concerns': rec.get('concerns', []),
                    'why_recommended': rec.get('recommendation_reason', f"{rec['city']} is perfect for your Thailand profile.")
                }
                formatted_recommendations.append(formatted_rec)

            return {
                'status': 'success',
                'recommendations': formatted_recommendations,
                'total_cities_analyzed': len(self.cities_data['cities']),
                'algorithm_version': self.version,
                'filters_applied': {
                    'regional_preference': questionnaire_responses.get('thailand_region_preference', 'region_flexible'),
                    'main_priority': questionnaire_responses.get('thailand_main_priority', 'balanced_lifestyle')
                }
            }

        except Exception as e:
            logger.error(f"❌ Erreur get_recommendations Thailand: {e}")
            return {
                'status': 'error',
                'recommendations': [],
                'message': f'Erreur calcul recommandations Thailand: {str(e)}'
            }


# Test de l'algorithme si exécuté directement
if __name__ == "__main__":
    # Test avec données d'exemple
    test_cities_path = "/var/www/Revolutionnary/platform/backend/data_v2/villes_thailand_residents.json"
    algo = ThailandResidentsAlgorithm(test_cities_path)

    # Profil test - Street food lover, tropical climate, beaches
    test_profile = {
        "thailand_region_preference": "southern_beaches",
        "thailand_main_priority": "cultural_immersion",
        "thailand_budget_monthly": "budget_comfortable",
        "thailand_work_environment": "freelance_remote",
        "thailand_climate_adaptation": "climate_lover",
        "thailand_mobility_transport": ["motorbike", "taxi_grab"],
        "thailand_essential_services": ["healthcare_quality"],
        "thailand_cultural_interests": ["temples_heritage", "sports_recreation"],
        "thailand_social_scene": "mixed_balanced",
        "thailand_street_food_importance": "food_essential",
        "thailand_nature_urban_balance": "beach_paradise",
        "thailand_deal_breakers": ["no_dealbreakers"]
    }

    result = algo.get_recommendations(test_profile)
    print(f"🇹🇭 Thailand Algorithm Test Result:")
    print(f"Status: {result['status']}")
    if result['status'] == 'success':
        for i, rec in enumerate(result['recommendations'][:3], 1):
            print(f"{i}. {rec['city']}, {rec['region']} - {rec['score_percentage']}%")
            print(f"   Strengths: {', '.join(rec['top_strengths'][:2])}")
    else:
        print(f"Error: {result['message']}")
