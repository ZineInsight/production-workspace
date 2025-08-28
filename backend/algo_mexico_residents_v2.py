#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🇲🇽 MEXICO RESIDENTS ALGORITHM V2 - Revolutionary Platform
============================================================

Algorithme intelligent pour recommandations de villes mexicaines
Structure basée sur Spain avec utilisation complète des 27 critères JSON

Pattern Revolutionary avec zones géographiques mexicaines
Garantit 3 villes minimum avec filtrage intelligent
"""

import json
import logging
import os
from typing import Dict, List, Any, Tuple
from collections import defaultdict

class MexicoResidentsAlgorithm:
    """
    Algorithme de recommandation de villes mexicaines
    Méthode scientifique avec zones géographiques et scoring sur 27 critères JSON
    """

    def __init__(self):
        """Initialise l'algorithme avec les données JSON"""
        self.version = "2.0.0"

        # Chargement des données JSON (27 critères)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_file = os.path.join(current_dir, "data_v2", "villes_mexico_residents.json")
        self.cities_data = self.load_cities_data(data_file)

        # 🗺️ ZONES GÉOGRAPHIQUES MEXICAINES (basées sur les questions JS)

        # Zones de style de vie (mexico_lifestyle_preference)
        self.lifestyle_zones = {
            "cosmopolitan_city": ["mexico_city", "guadalajara", "monterrey", "puebla", "tijuana"],
            "beach_paradise": ["cancun", "puerto_vallarta", "playa_del_carmen", "tulum", "mazatlan", "cozumel", "acapulco"],
            "colonial_charm": ["san_miguel_de_allende", "oaxaca", "morelia", "guanajuato", "campeche", "queretaro"],
            "expat_friendly": ["playa_del_carmen", "san_miguel_de_allende", "merida", "puerto_vallarta", "cancun", "tulum"]
        }

        # Zones climatiques (mexico_climate_preference)
        self.climate_zones = {
            "tropical_warm": ["cancun", "playa_del_carmen", "tulum", "cozumel", "merida", "campeche"],
            "temperate_mild": ["guadalajara", "puebla", "morelia", "san_miguel_de_allende", "queretaro", "guanajuato"],
            "mountain_fresh": ["mexico_city", "toluca", "puebla", "san_miguel_de_allende", "morelia"],
            "coastal_breeze": ["puerto_vallarta", "mazatlan", "acapulco", "cancun", "playa_del_carmen"]
        }

        # Zones de travail (mexico_work_environment)
        self.work_zones = {
            "tech_startup": ["mexico_city", "guadalajara", "monterrey", "puebla", "tijuana", "queretaro"],
            "remote_digital": ["playa_del_carmen", "tulum", "puerto_vallarta", "san_miguel_de_allende", "merida"],
            "traditional_business": ["mexico_city", "monterrey", "guadalajara", "puebla", "leon", "queretaro"],
            "tourism_hospitality": ["cancun", "playa_del_carmen", "puerto_vallarta", "tulum", "mazatlan", "acapulco"]
        }

        # Zones de budget (mexico_budget_comfort)
        self.budget_zones = {
            "budget_conscious": ["oaxaca", "merida", "campeche", "morelia", "puebla", "leon"],
            "moderate_spending": ["guadalajara", "queretaro", "puerto_vallarta", "mazatlan", "toluca"],
            "comfortable_premium": ["mexico_city", "monterrey", "san_miguel_de_allende", "playa_del_carmen"],
            "luxury_lifestyle": ["cancun", "tulum", "acapulco", "mexico_city", "monterrey"]
        }

        # Zones sociales (mexico_social_life)
        self.social_zones = {
            "vibrant_nightlife": ["mexico_city", "cancun", "playa_del_carmen", "puerto_vallarta", "guadalajara", "acapulco"],
            "cultural_events": ["mexico_city", "guadalajara", "oaxaca", "puebla", "morelia", "guanajuato"],
            "expat_community": ["san_miguel_de_allende", "playa_del_carmen", "puerto_vallarta", "merida", "tulum"],
            "local_immersion": ["oaxaca", "merida", "campeche", "morelia", "guanajuato", "puebla"]
        }

        # Zones de transport (mexico_transport_priority)
        self.transport_zones = {
            "metro_system": ["mexico_city", "guadalajara", "monterrey"],
            "walkable_compact": ["san_miguel_de_allende", "playa_del_carmen", "campeche", "oaxaca", "guanajuato"],
            "car_friendly": ["tijuana", "leon", "queretaro", "toluca", "puebla"],
            "bike_transit": ["mexico_city", "guadalajara", "playa_del_carmen", "tulum", "oaxaca"]
        }

        # Zones de logement (mexico_housing_type)
        self.housing_zones = {
            "modern_apartment": ["mexico_city", "guadalajara", "monterrey", "puebla", "tijuana", "queretaro"],
            "beachfront_condo": ["cancun", "playa_del_carmen", "puerto_vallarta", "mazatlan", "acapulco", "cozumel"],
            "colonial_house": ["san_miguel_de_allende", "oaxaca", "morelia", "campeche", "guanajuato", "puebla"],
            "expat_compound": ["san_miguel_de_allende", "playa_del_carmen", "puerto_vallarta", "merida", "tulum"]
        }

        # Zones gastronomiques (mexico_food_culture)
        self.gastronomy_zones = {
            "street_food_paradise": ["mexico_city", "oaxaca", "puebla", "guadalajara", "merida"],
            "fine_dining_scene": ["mexico_city", "guadalajara", "monterrey", "cancun", "puerto_vallarta"],
            "traditional_regional": ["oaxaca", "merida", "puebla", "morelia", "campeche", "guanajuato"],
            "international_fusion": ["mexico_city", "playa_del_carmen", "cancun", "tijuana", "san_miguel_de_allende"]
        }

        # Zones de rythme de vie (mexico_pace_of_life)
        self.pace_zones = {
            "fast_metropolitan": ["mexico_city", "monterrey", "guadalajara", "tijuana"],
            "relaxed_coastal": ["puerto_vallarta", "mazatlan", "playa_del_carmen", "tulum", "campeche"],
            "cultural_tranquil": ["san_miguel_de_allende", "oaxaca", "morelia", "guanajuato", "merida"],
            "balanced_modern": ["queretaro", "puebla", "leon", "cancun", "toluca"]
        }

        # Zones de sécurité (mexico_safety_priority)
        self.safety_zones = {
            "maximum_security": ["merida", "campeche", "queretaro", "san_miguel_de_allende", "playa_del_carmen"],
            "tourist_safe": ["cancun", "playa_del_carmen", "puerto_vallarta", "tulum", "cozumel"],
            "urban_cautious": ["mexico_city", "guadalajara", "monterrey", "puebla", "oaxaca"],
            "adventure_flexible": ["tulum", "oaxaca", "mazatlan", "morelia", "guanajuato"]
        }

        # 🎯 POIDS DES 27 CRITÈRES JSON (noms EXACTS du JSON)
        self.criteria_weights_base = {
            # Critères principaux (poids élevés) - NOMS JSON EXACTS
            "cost_of_living": 0.08,           # Budget très important
            "safety_security": 0.07,          # Sécurité cruciale au Mexique
            "air_quality": 0.06,              # Pollution importante
            "climate_comfort": 0.06,          # Climat très varié
            "job_opportunities": 0.05,        # Opportunités économiques
            "housing_affordability": 0.05,    # Accessibilité logement

            # Critères moyens (poids modérés) - NOMS JSON EXACTS
            "healthcare_quality": 0.05,       # Santé importante
            "public_transport": 0.04,         # Mobilité urbaine
            "cultural_scene": 0.04,           # Richesse culturelle
            "nightlife_entertainment": 0.04,  # Divertissement
            "internet_speed": 0.04,           # Numérique/télétravail
            "expat_community": 0.04,          # Intégration expats

            # Critères spécifiques (poids moyens-bas) - NOMS JSON EXACTS
            "beach_access": 0.04,             # Côtes mexicaines
            "food_scene": 0.04,               # Gastronomie riche
            "natural_beauty": 0.03,           # Qualité de vie/espaces verts
            "education_quality": 0.03,        # Système éducatif
            "walkability": 0.03,             # Mobilité urbaine/qualité de vie
            "coworking_spaces": 0.03,         # Espaces de travail modernes
            "language_barrier": 0.03,         # Facilité d'intégration linguistique

            # Critères complémentaires (poids bas) - NOMS JSON EXACTS
            "outdoor_activities": 0.03,       # Sports/nature
            "historical_heritage": 0.03,      # Patrimoine
            "dining_variety": 0.03,           # Animation gastronomique
            "diversity_inclusion": 0.02,      # Mixité sociale
            "entrepreneurship": 0.02,         # Secteur innovation/startup
            "bureaucracy_ease": 0.02,         # Facilité administrative
            "walkability": 0.02,              # Mobilité piétonne
            "shopping_options": 0.02,         # Services et commerces
            "salary_level": 0.02              # Niveau de salaires
        }

        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.logger.info(f"🇲🇽 Mexico Residents Algorithm v{self.version} initialized with {len(self.cities_data)} cities")

    def load_cities_data(self, file_path: str) -> List[Dict]:
        """Load cities data from JSON file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return data if isinstance(data, list) else data.get('cities', [])
        except FileNotFoundError:
            self.logger.error(f"❌ Cities data file not found: {file_path}")
            return []
        except json.JSONDecodeError as e:
            self.logger.error(f"❌ Error parsing cities data: {e}")
            return []

    def apply_climate_lifestyle_filters(self, cities_list: List[Dict], user_responses: Dict) -> List[Dict]:
        """
        Apply climate and lifestyle pre-filtering based on Mexican user preferences.
        Améliore drastiquement la précision en filtrant AVANT le scoring.
        """
        filtered_cities = cities_list.copy()

        # Filtrage climatique
        climate_pref = user_responses.get('mexico_climate_preference')
        if climate_pref and climate_pref != "climate_flexible":
            if climate_pref in self.climate_zones:
                climate_city_ids = self.climate_zones[climate_pref]
                filtered_cities = [city for city in filtered_cities if city['id'] in climate_city_ids]
                self.logger.info(f"🌡️ Climate filter '{climate_pref}': {len(filtered_cities)} cities remaining")

        # Filtrage style de vie
        lifestyle_pref = user_responses.get('mexico_lifestyle_preference')
        if lifestyle_pref and lifestyle_pref in self.lifestyle_zones:
            lifestyle_city_ids = self.lifestyle_zones[lifestyle_pref]
            lifestyle_filtered = [city for city in filtered_cities if city['id'] in lifestyle_city_ids]
            if len(lifestyle_filtered) >= 3:  # Assurer minimum de recommandations
                filtered_cities = lifestyle_filtered
                self.logger.info(f"🏖️ Lifestyle filter '{lifestyle_pref}': {len(filtered_cities)} cities remaining")

        # Filtrage environnement de travail
        work_pref = user_responses.get('mexico_work_environment')
        if work_pref and work_pref in self.work_zones:
            work_city_ids = self.work_zones[work_pref]
            work_filtered = [city for city in filtered_cities if city['id'] in work_city_ids]
            if len(work_filtered) >= 3:
                filtered_cities = work_filtered
                self.logger.info(f"💼 Work filter '{work_pref}': {len(filtered_cities)} cities remaining")

        # Filtrage budget (soft)
        budget_pref = user_responses.get('mexico_budget_comfort')
        if budget_pref and budget_pref in self.budget_zones:
            budget_city_ids = self.budget_zones[budget_pref]
            budget_filtered = [city for city in filtered_cities if city['id'] in budget_city_ids]
            if len(budget_filtered) >= 2:
                filtered_cities = budget_filtered
                self.logger.info(f"💰 Budget filter '{budget_pref}': {len(filtered_cities)} cities remaining")

        # Filtrage vie sociale (soft)
        social_pref = user_responses.get('mexico_social_life')
        if social_pref and social_pref in self.social_zones:
            social_city_ids = self.social_zones[social_pref]
            social_filtered = [city for city in filtered_cities if city['id'] in social_city_ids]
            if len(social_filtered) >= 2:
                filtered_cities = social_filtered[:6]  # Garder variété
                self.logger.info(f"🎉 Social filter '{social_pref}': {len(filtered_cities)} cities remaining")

        # Filtrage transport
        transport_pref = user_responses.get('mexico_transport_priority')
        if transport_pref and transport_pref in self.transport_zones:
            transport_city_ids = self.transport_zones[transport_pref]
            transport_filtered = [city for city in filtered_cities if city['id'] in transport_city_ids]
            if len(transport_filtered) >= 2:
                filtered_cities = transport_filtered
                self.logger.info(f"🚇 Transport filter '{transport_pref}': {len(filtered_cities)} cities remaining")

        # Filtrage logement
        housing_pref = user_responses.get('mexico_housing_type')
        if housing_pref and housing_pref in self.housing_zones:
            housing_city_ids = self.housing_zones[housing_pref]
            housing_filtered = [city for city in filtered_cities if city['id'] in housing_city_ids]
            if len(housing_filtered) >= 2:
                filtered_cities = housing_filtered
                self.logger.info(f"🏠 Housing filter '{housing_pref}': {len(filtered_cities)} cities remaining")

        # Filtrage sécurité (important au Mexique)
        safety_pref = user_responses.get('mexico_safety_priority')
        if safety_pref and safety_pref in self.safety_zones:
            safety_city_ids = self.safety_zones[safety_pref]
            safety_filtered = [city for city in filtered_cities if city['id'] in safety_city_ids]
            if len(safety_filtered) >= 2:
                filtered_cities = safety_filtered
                self.logger.info(f"🛡️ Safety filter '{safety_pref}': {len(filtered_cities)} cities remaining")

        return filtered_cities

    def adapt_criteria_weights(self, base_weights: Dict[str, float], user_responses: Dict) -> Dict[str, float]:
        """
        Adapte dynamiquement les poids des critères selon les préférences mexicaines.
        Reflète les priorités spécifiques au contexte mexicain.
        """
        adapted_weights = base_weights.copy()

        # Adaptation style de vie - NOMS JSON EXACTS
        lifestyle = user_responses.get('mexico_lifestyle_preference', '')
        if lifestyle == 'beach_paradise':
            adapted_weights['climate_comfort'] *= 1.4
            adapted_weights['beach_access'] *= 2.0
            adapted_weights['outdoor_activities'] *= 1.5
            adapted_weights['walkability'] *= 1.3

        elif lifestyle == 'cosmopolitan_city':
            adapted_weights['job_opportunities'] *= 1.3
            adapted_weights['cultural_scene'] *= 1.3
            adapted_weights['public_transport'] *= 1.4
            adapted_weights['nightlife_entertainment'] *= 1.3
            adapted_weights['entrepreneurship'] *= 1.4

        elif lifestyle == 'colonial_charm':
            adapted_weights['historical_heritage'] *= 1.8
            adapted_weights['cultural_scene'] *= 1.5
            adapted_weights['cost_of_living'] *= 1.2  # Plus abordable
            adapted_weights['walkability'] *= 1.4

        elif lifestyle == 'expat_friendly':
            adapted_weights['expat_community'] *= 2.0
            adapted_weights['language_barrier'] *= 0.7  # Moins important (inverse)
            adapted_weights['healthcare_quality'] *= 1.3
            adapted_weights['internet_speed'] *= 1.4

        # Adaptation environnement de travail - NOMS JSON EXACTS
        work_env = user_responses.get('mexico_work_environment', '')
        if work_env == 'tech_startup':
            adapted_weights['entrepreneurship'] *= 2.0
            adapted_weights['job_opportunities'] *= 1.4
            adapted_weights['internet_speed'] *= 1.5
            adapted_weights['coworking_spaces'] *= 1.4

        elif work_env == 'remote_digital':
            adapted_weights['internet_speed'] *= 2.0
            adapted_weights['walkability'] *= 1.6
            adapted_weights['cost_of_living'] *= 1.3
            adapted_weights['expat_community'] *= 1.3

        elif work_env == 'tourism_hospitality':
            adapted_weights['beach_access'] *= 1.5
            adapted_weights['cultural_scene'] *= 1.3
            adapted_weights['nightlife_entertainment'] *= 1.4
            adapted_weights['food_scene'] *= 1.3

        # Adaptation budget - NOMS JSON EXACTS
        budget = user_responses.get('mexico_budget_comfort', '')
        if budget == 'budget_conscious':
            adapted_weights['cost_of_living'] *= 1.6
            adapted_weights['housing_affordability'] *= 1.5
            adapted_weights['bureaucracy_ease'] *= 1.3

        elif budget == 'luxury_lifestyle':
            adapted_weights['healthcare_quality'] *= 1.4
            adapted_weights['cultural_scene'] *= 1.3
            adapted_weights['nightlife_entertainment'] *= 1.3
            adapted_weights['shopping_options'] *= 1.4

        # Adaptation sécurité (critique au Mexique) - NOMS JSON EXACTS
        safety = user_responses.get('mexico_safety_priority', '')
        if safety == 'maximum_security':
            adapted_weights['safety_security'] *= 2.0
            adapted_weights['healthcare_quality'] *= 1.3

        elif safety == 'urban_cautious':
            adapted_weights['safety_security'] *= 1.5
            adapted_weights['public_transport'] *= 1.2

        # Adaptation climat - NOMS JSON EXACTS
        climate = user_responses.get('mexico_climate_preference', '')
        if climate == 'tropical_warm':
            adapted_weights['climate_comfort'] *= 1.5
            adapted_weights['beach_access'] *= 1.3

        elif climate == 'mountain_fresh':
            adapted_weights['air_quality'] *= 1.4
            adapted_weights['natural_beauty'] *= 1.3

        return adapted_weights

    def calculate_city_score(self, city: Dict, adapted_weights: Dict[str, float]) -> float:
        """
        Calculate weighted score for a Mexican city using JSON criteria.
        Scoring mexicain optimisé avec considérations culturelles.
        """
        total_score = 0.0

        for criterion, weight in adapted_weights.items():
            if criterion in city['scores']:
                criterion_score = city['scores'][criterion]
                weighted_score = criterion_score * weight
                total_score += weighted_score

        return total_score

    def get_recommendations(self, questionnaire_responses: Dict, top_n: int = 3) -> Dict:
        """
        🇲🇽 Main recommendation method for Mexican cities.
        Returns top city matches with Mexican cultural context.

        STANDARDIZED API METHOD - Compatible with main.py integration
        """
        try:
            # Étape 1: Appliquer le pré-filtrage intelligent
            filtered_cities = self.apply_climate_lifestyle_filters(self.cities_data, questionnaire_responses)

            if not filtered_cities:
                self.logger.warning("⚠️ No cities match filters, using all cities")
                filtered_cities = self.cities_data

            # Étape 2: Adapter les poids aux préférences mexicaines
            adapted_weights = self.adapt_criteria_weights(self.criteria_weights_base, questionnaire_responses)

            # Étape 3: Scorer chaque ville
            scored_cities = []
            for city in filtered_cities:
                score = self.calculate_city_score(city, adapted_weights)
                scored_cities.append({
                    "city": city['name'],
                    "region": city['region'],
                    "population": city['population'],
                    "description": city.get('description', ''),
                    "score_percentage": round(score * 100, 1),  # Convertir en pourcentage
                    "reasons": self._generate_reasons(city, questionnaire_responses),
                    "pros": city.get('pros', []),
                    "cons": city.get('cons', [])
                })

            # Étape 4: Trier et limiter
            scored_cities.sort(key=lambda x: x['score_percentage'], reverse=True)
            top_cities = scored_cities[:top_n]

            # Étape 5: Statistiques et logs
            self.logger.info(f"🇲🇽 Mexico recommendations generated: {len(top_cities)} cities")
            for i, city in enumerate(top_cities, 1):
                self.logger.info(f"  {i}. {city['city']}: {city['score_percentage']}%")

            return {
                "success": True,
                "recommendations": top_cities,
                "total_cities_analyzed": len(filtered_cities),
                "algorithm_version": self.version
            }

        except Exception as e:
            self.logger.error(f"❌ Error in Mexican recommendations: {e}")
            return {
                "success": False,
                "error": str(e),
                "recommendations": [],
                "algorithm_version": self.version
            }

    def _generate_reasons(self, city: Dict, user_responses: Dict) -> List[str]:
        """
        Generate personalized reasons why this Mexican city matches the user.
        Raisons personnalisées basées sur le profil utilisateur.
        """
        reasons = []
        scores = city.get('scores', {})

        # Raisons basées sur le style de vie - NOMS JSON EXACTS
        lifestyle = user_responses.get('mexico_lifestyle_preference', '')
        if lifestyle == 'beach_paradise' and scores.get('beach_access', 0) > 0.7:
            reasons.append("🏖️ Accès privilégié aux plus belles plages du Mexique")

        if lifestyle == 'colonial_charm' and scores.get('historical_heritage', 0) > 0.7:
            reasons.append("🏛️ Architecture coloniale exceptionnelle et patrimoine riche")

        if lifestyle == 'cosmopolitan_city' and scores.get('cultural_scene', 0) > 0.7:
            reasons.append("🎭 Scène culturelle dynamique et vie urbaine stimulante")

        if lifestyle == 'expat_friendly' and scores.get('expat_community', 0) > 0.7:
            reasons.append("🌍 Communauté expat établie et services adaptés")

        # Raisons économiques - NOMS JSON EXACTS
        if scores.get('cost_of_living', 0) > 0.7:
            reasons.append("💰 Coût de la vie avantageux et pouvoir d'achat optimal")

        if scores.get('job_opportunities', 0) > 0.7:
            reasons.append("💼 Marché du travail dynamique et opportunités professionnelles")

        # Raisons qualité de vie - NOMS JSON EXACTS
        if scores.get('climate_comfort', 0) > 0.8:
            reasons.append("☀️ Climat idéal toute l'année")

        if scores.get('safety_security', 0) > 0.7:
            reasons.append("🛡️ Environnement sûr et tranquille")

        if scores.get('healthcare_quality', 0) > 0.7:
            reasons.append("🏥 Accès excellent aux soins de santé")

        # S'assurer qu'on a au moins 2-3 raisons - NOMS JSON EXACTS
        if len(reasons) < 2:
            if scores.get('walkability', 0) > 0.6:
                reasons.append("⚖️ Ville agréable et marchable au quotidien")
            if scores.get('food_scene', 0) > 0.6:
                reasons.append("🌮 Gastronomie mexicaine authentique et diversifiée")

        return reasons[:4]  # Limiter à 4 raisons maximum


# Instance globale pour l'API
mexico_algorithm = MexicoResidentsAlgorithm()

def get_mexico_recommendations(questionnaire_responses: Dict, top_n: int = 3) -> Dict:
    """
    🇲🇽 API function for Mexico recommendations
    Interface standardisée pour l'intégration main.py
    """
    return mexico_algorithm.get_recommendations(questionnaire_responses, top_n)

def get_mexico_cities() -> List[Dict]:
    """
    🇲🇽 API function to get all Mexican cities
    Interface pour récupérer la liste des villes
    """
    return [{
        "id": city['id'],
        "name": city['name'],
        "region": city['region'],
        "population": city['population'],
        "description": city.get('description', '')
    } for city in mexico_algorithm.cities_data]

def get_mexico_criteria() -> List[str]:
    """
    🇲🇽 API function to get all Mexican criteria
    Interface pour récupérer la liste des critères
    """
    return list(mexico_algorithm.criteria_weights_base.keys())

if __name__ == "__main__":
    # Test de l'algorithme
    test_responses = {
        'mexico_lifestyle_preference': 'beach_paradise',
        'mexico_climate_preference': 'tropical_warm',
        'mexico_work_environment': 'remote_digital',
        'mexico_budget_comfort': 'moderate_spending',
        'mexico_safety_priority': 'tourist_safe'
    }

    result = get_mexico_recommendations(test_responses, 5)
    print("🇲🇽 MEXICO ALGORITHM V2 TEST")
    print("=" * 40)
    print(f"Success: {result['success']}")
    print(f"Cities analyzed: {result.get('total_cities_analyzed', 0)}")
    print("\nTop recommendations:")
    for i, city in enumerate(result.get('recommendations', []), 1):
        print(f"{i}. {city['city']} ({city['region']}) - {city['score_percentage']}%")
        for reason in city['reasons'][:2]:
            print(f"   • {reason}")
        print()
