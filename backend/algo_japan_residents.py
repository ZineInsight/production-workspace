"""
🇯🇵 ALGO-JAPAN-RESIDENTS.PY - ALGORITHME MATCHING VILLES JAPON
================================================================
Algorithme ultra performant pour matcher Japonais avec leurs 3 villes idéales
Author: Revolutionary Team | Version: 1.0.0 - Japan Domestic Matching
OBJECTIF: Recommandations précises basées sur profils japonais et réalités régionales
"""

import json
import logging
from typing import Dict, List, Tuple
from dataclasses import dataclass

# Configuration logging
logger = logging.getLogger(__name__)

@dataclass
class UserProfileJapan:
    """Profil utilisateur Japon avec pondérations spécifiquement japonaises"""
    region_preference: str       # any_region, kanto, kansai, chubu, kyushu, hokkaido_tohoku
    main_priority: str           # career_tokyo, work_life_balance, traditional_culture, cost_optimization
    age_profile: str            # new_graduate, young_professional, mid_career, pre_retirement
    monthly_budget: str         # budget_student, budget_balanced, budget_comfortable, budget_premium
    work_situation: str         # salaryman, tech_startup, freelance_remote, job_hunting
    transport_preference: str   # jr_priority, metro_urban, bicycle_friendly, car_acceptable
    housing_preference: str     # city_manshion, suburban_house, station_proximity, price_priority
    climate_preference: str     # four_seasons, mild_winter, cool_summer, climate_flexible
    social_scene: str          # izakaya_traditional, modern_nightlife, arts_culture, quiet_residential
    family_situation: str      # single_independent, couple_no_children, young_family, school_age_family
    disaster_tolerance: str    # earthquake_prepared, typhoon_acceptable, tsunami_avoid, all_risks_ok
    deal_breaker: str         # tokyo_too_expensive, isolated_countryside, limited_job_market, language_barrier
    criteria_weights: Dict[str, float]

class JapanResidentsAlgorithm:
    """🇯🇵 Algorithme de recommandation pour résidents japonais"""

    def __init__(self, cities_data_path: str):
        """Initialise l'algorithme avec les données des 30 principales villes japonaises"""
        self.version = "1.0.0"
        self.cities_data = self.load_cities_data(cities_data_path)
        self.criteria_weights_base = self.get_base_criteria_weights_japan()

    def load_cities_data(self, data_path: str) -> Dict:
        """Charge les données des 30 villes japonaises"""
        try:
            with open(data_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            logger.info(f"🇯🇵 Données Japon chargées: {len(data['cities'])} villes")
            return data
        except Exception as e:
            logger.error(f"❌ Erreur chargement données Japon: {e}")
            raise

    def get_base_criteria_weights_japan(self) -> Dict[str, float]:
        """Pondérations de base pour les 27 critères japonais"""
        return {
            # 💰 ÉCONOMIE (5 critères)
            'cost_of_living': 8.5,
            'housing_affordability': 8.0,
            'income_tax_burden': 6.0,
            'local_tax': 5.5,
            'council_tax': 5.0,

            # 💼 EMPLOI (3 critères)
            'job_market': 9.0,
            'tech_industry': 7.5,
            'remote_work_friendly': 7.0,

            # 🚊 TRANSPORT (3 critères)
            'public_transport': 8.5,  # JR/Métro crucial au Japon
            'walkability': 7.5,
            'car_dependency': 6.5,

            # 🏠 LOGEMENT (3 critères)
            'urban_density': 7.0,
            'suburb_quality': 7.5,
            'climate_rating': 7.0,

            # 🎓 ÉDUCATION (2 critères)
            'school_quality': 8.0,
            'university_access': 7.0,

            # ⚡ RISQUES NATURELS (4 critères) - Spécial Japon
            'natural_disaster_risk': 8.0,  # Séismes prioritaires
            'flood_risk': 7.0,
            'heat_wave_risk': 6.5,
            'weather_consistency': 6.5,

            # 🏥 SANTÉ (2 critères)
            'healthcare_access': 8.0,
            'hospital_quality': 7.5,

            # 🎭 CULTURE (3 critères)
            'cultural_scene': 7.5,
            'restaurant_diversity': 7.0,
            'nightlife': 6.5,

            # 🗣️ LANGUES (2 critères)
            'english_language_score': 6.0,
            'traditional_culture_score': 7.5  # Important au Japon
        }

    def create_user_profile_japan(self, questionnaire_responses: Dict) -> UserProfileJapan:
        """Crée un profil utilisateur à partir des réponses au questionnaire"""
        return UserProfileJapan(
            region_preference=questionnaire_responses.get('japan_region_preference', 'any_region'),
            main_priority=questionnaire_responses.get('japan_main_priority', 'career_tokyo'),
            age_profile=questionnaire_responses.get('japan_age_profile', 'young_professional'),
            monthly_budget=questionnaire_responses.get('japan_monthly_budget', 'budget_balanced'),
            work_situation=questionnaire_responses.get('japan_work_situation', 'salaryman'),
            transport_preference=questionnaire_responses.get('japan_transport_preference', 'jr_priority'),
            housing_preference=questionnaire_responses.get('japan_housing_preference', 'city_manshion'),
            climate_preference=questionnaire_responses.get('japan_climate_preference', 'four_seasons'),
            social_scene=questionnaire_responses.get('japan_social_scene', 'izakaya_traditional'),
            family_situation=questionnaire_responses.get('japan_family_situation', 'single_independent'),
            disaster_tolerance=questionnaire_responses.get('japan_disaster_tolerance', 'earthquake_prepared'),
            deal_breaker=questionnaire_responses.get('japan_deal_breaker', 'tokyo_too_expensive'),
            criteria_weights=self.criteria_weights_base.copy()
        )

    def apply_regional_filters(self, cities_list: List[Dict], user_profile: UserProfileJapan) -> List[Dict]:
        """Filtre régional AVANT scoring pour performance optimisée"""
        if user_profile.region_preference == 'any_region':
            return cities_list

        region_mapping = {
            'kanto': ['kanto'],
            'kansai': ['kansai'],
            'chubu': ['chubu'],
            'kyushu': ['kyushu'],
            'hokkaido_tohoku': ['hokkaido', 'tohoku', 'okinawa']  # Régions périphériques
        }

        target_regions = region_mapping.get(user_profile.region_preference, [])
        if not target_regions:
            return cities_list

        filtered_cities = [
            city for city in cities_list
            if city.get('regional_location', '') in target_regions
        ]

        logger.info(f"🗺️ Filtre régional {user_profile.region_preference}: {len(filtered_cities)} villes gardées")
        return filtered_cities

    def apply_budget_filters(self, cities_list: List[Dict], user_profile: UserProfileJapan) -> List[Dict]:
        """Filtre budget - Éliminer Tokyo/Yokohama si budget insuffisant"""
        expensive_cities = ['tokyo', 'yokohama', 'kamakura']  # Villes très chères

        if user_profile.monthly_budget in ['budget_student', 'budget_balanced']:  # < ¥500K
            filtered_cities = [
                city for city in cities_list
                if city.get('id', '') not in expensive_cities
            ]
            logger.info(f"💰 Filtre budget {user_profile.monthly_budget}: Élimination villes chères, {len(filtered_cities)} gardées")
            return filtered_cities

        return cities_list

    def apply_deal_breaker_filters(self, cities_list: List[Dict], user_profile: UserProfileJapan) -> List[Dict]:
        """Filtres négatifs selon deal breaker"""
        if user_profile.deal_breaker == 'tokyo_too_expensive':
            # Éliminer villes coût vie < 0.4 (très chères)
            return [city for city in cities_list if city['scores'].get('cost_of_living', 0) >= 0.4]

        elif user_profile.deal_breaker == 'isolated_countryside':
            # Éliminer petites villes < 200K habitants
            return [city for city in cities_list if city.get('population', 0) >= 200000]

        elif user_profile.deal_breaker == 'limited_job_market':
            # Éliminer villes job_market < 0.6
            return [city for city in cities_list if city['scores'].get('job_market', 0) >= 0.6]

        elif user_profile.deal_breaker == 'language_barrier':
            # Garder villes avec english_language_score > 0.4 ou grandes villes
            return [city for city in cities_list
                   if city['scores'].get('english_language_score', 0) >= 0.4
                   or city.get('population', 0) >= 1000000]

        return cities_list

    def adjust_weights_by_priority(self, user_profile: UserProfileJapan) -> None:
        """Ajuste les pondérations selon priorité principale - VERSION EXTREME"""
        if user_profile.main_priority == 'career_tokyo':
            user_profile.criteria_weights['job_market'] *= 4.0          # 2.0 → 4.0
            user_profile.criteria_weights['tech_industry'] *= 3.5       # 1.8 → 3.5
            user_profile.criteria_weights['public_transport'] *= 3.0    # 1.6 → 3.0
            user_profile.criteria_weights['cost_of_living'] *= 0.3      # 0.6 → 0.3 (pénalité forte)
            user_profile.criteria_weights['suburb_quality'] *= 0.4      # Nouveau: anti-suburb

        elif user_profile.main_priority == 'work_life_balance':
            user_profile.criteria_weights['remote_work_friendly'] *= 4.0 # 1.9 → 4.0
            user_profile.criteria_weights['suburb_quality'] *= 3.5      # 1.7 → 3.5
            user_profile.criteria_weights['urban_density'] *= 0.3       # Pénalité forte densité
            user_profile.criteria_weights['climate_rating'] *= 2.5      # 1.4 → 2.5
            user_profile.criteria_weights['job_market'] *= 0.5          # Moins critique
            user_profile.criteria_weights['tech_industry'] *= 0.4       # Anti-tech stress

        elif user_profile.main_priority == 'traditional_culture':
            user_profile.criteria_weights['traditional_culture_score'] *= 4.5 # 2.2 → 4.5
            user_profile.criteria_weights['cultural_scene'] *= 3.5      # 1.8 → 3.5
            user_profile.criteria_weights['restaurant_diversity'] *= 2.5 # 1.4 → 2.5
            user_profile.criteria_weights['tech_industry'] *= 0.3       # 0.7 → 0.3 (forte pénalité)
            user_profile.criteria_weights['nightlife'] *= 0.4           # Anti-nightlife moderne

        elif user_profile.main_priority == 'cost_optimization':
            user_profile.criteria_weights['cost_of_living'] *= 4.0      # 2.1 → 4.0
            user_profile.criteria_weights['housing_affordability'] *= 4.0 # 2.0 → 4.0
            user_profile.criteria_weights['local_tax'] *= 3.0           # 1.5 → 3.0
            user_profile.criteria_weights['job_market'] *= 0.4          # 0.8 → 0.4 (compromis fort)
            user_profile.criteria_weights['cultural_scene'] *= 0.5      # Moins prioritaire
            user_profile.criteria_weights['restaurant_diversity'] *= 0.5 # Luxe non nécessaire

    def adjust_weights_by_age_work(self, user_profile: UserProfileJapan) -> None:
        """Ajuste selon âge et situation professionnelle - VERSION EXTREME"""
        # Ajustement par âge - PLUS EXTREME
        if user_profile.age_profile == 'new_graduate':
            user_profile.criteria_weights['nightlife'] *= 3.0           # 1.6 → 3.0
            user_profile.criteria_weights['university_access'] *= 2.5   # 1.4 → 2.5
            user_profile.criteria_weights['cost_of_living'] *= 3.5      # 1.8 → 3.5 (crucial étudiant)
            user_profile.criteria_weights['healthcare_access'] *= 0.4   # 0.8 → 0.4 (moins critique jeune)
            user_profile.criteria_weights['suburb_quality'] *= 0.3      # Anti-banlieue jeune

        elif user_profile.age_profile == 'pre_retirement':
            user_profile.criteria_weights['healthcare_access'] *= 4.0   # 2.0 → 4.0
            user_profile.criteria_weights['hospital_quality'] *= 3.5    # 1.8 → 3.5
            user_profile.criteria_weights['cultural_scene'] *= 2.5      # 1.6 → 2.5
            user_profile.criteria_weights['nightlife'] *= 0.2           # Anti-nightlife retraité
            user_profile.criteria_weights['tech_industry'] *= 0.2       # Plus pertinent
            user_profile.criteria_weights['job_market'] *= 0.3          # Moins critique

        # Ajustement situation professionnelle - PLUS EXTREME
        if user_profile.work_situation == 'tech_startup':
            user_profile.criteria_weights['tech_industry'] *= 4.0       # Nouveau multiplicateur fort
            user_profile.criteria_weights['nightlife'] *= 2.5           # Vie sociale tech
            user_profile.criteria_weights['traditional_culture_score'] *= 0.4 # Anti-traditionnel
            user_profile.criteria_weights['suburb_quality'] *= 0.3      # Vie urbaine

        elif user_profile.work_situation == 'freelance_remote':
            user_profile.criteria_weights['remote_work_friendly'] *= 4.0 # Crucial
            user_profile.criteria_weights['cost_of_living'] *= 3.5      # Budget serré
            user_profile.criteria_weights['public_transport'] *= 0.4    # Moins critique si remote
            user_profile.criteria_weights['job_market'] *= 0.3          # Non pertinent

        elif user_profile.work_situation == 'job_hunting':
            user_profile.criteria_weights['job_market'] *= 4.5          # CRUCIAL
            user_profile.criteria_weights['tech_industry'] *= 3.0       # Opportunités
            user_profile.criteria_weights['public_transport'] *= 3.0    # Mobilité
            user_profile.criteria_weights['cost_of_living'] *= 2.5      # Budget limité
            user_profile.criteria_weights['nightlife'] *= 0.4           # Moins prioritaire
            user_profile.criteria_weights['restaurant_diversity'] *= 0.4 # Economies

    def adjust_weights_by_lifestyle(self, user_profile: UserProfileJapan) -> None:
        """Ajuste selon transport, logement, climat, social, famille - VERSION EXTREME"""
        # Transport - PLUS EXTREME
        if user_profile.transport_preference == 'jr_priority':
            user_profile.criteria_weights['public_transport'] *= 3.5    # 2.0 → 3.5
            user_profile.criteria_weights['car_dependency'] *= 0.2      # Forte pénalité voiture
        elif user_profile.transport_preference == 'bicycle_friendly':
            user_profile.criteria_weights['walkability'] *= 3.0         # 1.8 → 3.0
            user_profile.criteria_weights['car_dependency'] *= 2.5      # 1.6 → 2.5
            user_profile.criteria_weights['urban_density'] *= 2.0       # 1.3 → 2.0
            user_profile.criteria_weights['public_transport'] *= 0.5    # Moins critique

        # Logement - PLUS EXTREME
        if user_profile.housing_preference == 'suburban_house':
            user_profile.criteria_weights['suburb_quality'] *= 3.5      # 2.0 → 3.5
            user_profile.criteria_weights['urban_density'] *= 0.2       # Éviter densité forte
            user_profile.criteria_weights['nightlife'] *= 0.3           # Anti-nightlife
        elif user_profile.housing_preference == 'price_priority':
            user_profile.criteria_weights['housing_affordability'] *= 4.0 # 1.9 → 4.0
            user_profile.criteria_weights['cost_of_living'] *= 3.5      # 1.7 → 3.5
            user_profile.criteria_weights['restaurant_diversity'] *= 0.4 # Économies
            user_profile.criteria_weights['nightlife'] *= 0.4           # Économies

        # Climat - PLUS EXTREME
        if user_profile.climate_preference == 'cool_summer':
            user_profile.criteria_weights['heat_wave_risk'] *= 4.0      # 1.8 → 4.0 (crucial)
            user_profile.criteria_weights['climate_rating'] *= 3.0     # 1.6 → 3.0
        elif user_profile.climate_preference == 'mild_winter':
            user_profile.criteria_weights['climate_rating'] *= 2.5     # 1.5 → 2.5

        # Social - PLUS EXTREME
        if user_profile.social_scene == 'izakaya_traditional':
            user_profile.criteria_weights['traditional_culture_score'] *= 4.0 # 1.8 → 4.0
            user_profile.criteria_weights['cultural_scene'] *= 3.0     # 1.5 → 3.0
            user_profile.criteria_weights['nightlife'] *= 0.3          # Anti-nightlife moderne
        elif user_profile.social_scene == 'modern_nightlife':
            user_profile.criteria_weights['nightlife'] *= 4.0          # 2.0 → 4.0
            user_profile.criteria_weights['restaurant_diversity'] *= 3.0 # 1.6 → 3.0
            user_profile.criteria_weights['traditional_culture_score'] *= 0.3 # Anti-traditionnel
        elif user_profile.social_scene == 'quiet_residential':
            user_profile.criteria_weights['suburb_quality'] *= 3.5     # 1.7 → 3.5
            user_profile.criteria_weights['urban_density'] *= 0.2      # 1.5 → 0.2 (forte pénalité)
            user_profile.criteria_weights['nightlife'] *= 0.2          # 0.5 → 0.2 (très anti)

        # Famille - PLUS EXTREME
        if user_profile.family_situation == 'young_family':
            user_profile.criteria_weights['school_quality'] *= 4.0     # 2.0 → 4.0
            user_profile.criteria_weights['suburb_quality'] *= 3.5     # 1.8 → 3.5
            user_profile.criteria_weights['healthcare_access'] *= 3.0  # 1.6 → 3.0
            user_profile.criteria_weights['nightlife'] *= 0.2          # 0.6 → 0.2 (très anti)
            user_profile.criteria_weights['restaurant_diversity'] *= 0.4 # Économies famille
        elif user_profile.family_situation == 'school_age_family':
            user_profile.criteria_weights['school_quality'] *= 4.5     # 2.2 → 4.5 (CRUCIAL)
            user_profile.criteria_weights['university_access'] *= 3.0  # 1.6 → 3.0
            user_profile.criteria_weights['suburb_quality'] *= 3.5     # 1.8 → 3.5
            user_profile.criteria_weights['nightlife'] *= 0.2          # Très faible priorité
            user_profile.criteria_weights['cost_of_living'] *= 2.0     # Frais éducation

    def adjust_weights_by_disaster_tolerance(self, user_profile: UserProfileJapan) -> None:
        """Ajuste selon tolérance risques naturels"""
        if user_profile.disaster_tolerance == 'tsunami_avoid':
            user_profile.criteria_weights['natural_disaster_risk'] *= 2.0
            user_profile.criteria_weights['flood_risk'] *= 1.8
        elif user_profile.disaster_tolerance == 'earthquake_prepared':
            user_profile.criteria_weights['natural_disaster_risk'] *= 1.4
        elif user_profile.disaster_tolerance == 'all_risks_ok':
            user_profile.criteria_weights['natural_disaster_risk'] *= 0.8
            user_profile.criteria_weights['flood_risk'] *= 0.8

    def calculate_city_score(self, city: Dict, user_profile: UserProfileJapan) -> float:
        """Calcule le score pondéré pour une ville (0-100)"""
        total_score = 0.0
        total_weight = 0.0

        for criterion, weight in user_profile.criteria_weights.items():
            if criterion in city['scores']:
                criterion_score = city['scores'][criterion]  # 0.0-1.0
                total_score += criterion_score * weight
                total_weight += weight

        return (total_score / total_weight) * 100 if total_weight > 0 else 0

    def get_city_strengths(self, city: Dict, top_n: int = 3) -> List[Dict]:
        """Identifie les points forts d'une ville"""
        scores = city['scores']
        sorted_criteria = sorted(scores.items(), key=lambda x: x[1], reverse=True)

        criteria_names = {
            'job_market': 'Marché de l\'emploi',
            'cultural_scene': 'Scène culturelle',
            'public_transport': 'Transport public',
            'traditional_culture_score': 'Culture traditionnelle',
            'cost_of_living': 'Coût de la vie',
            'tech_industry': 'Industrie tech',
            'healthcare_access': 'Accès aux soins'
        }

        return [
            {
                'criterion': criteria_names.get(criterion, criterion),
                'score': round(score * 100)
            }
            for criterion, score in sorted_criteria[:top_n] if score >= 0.7
        ]

    def generate_match_explanation(self, city: Dict, user_profile: UserProfileJapan) -> str:
        """Génère une explication personnalisée du match"""
        explanations = []

        if user_profile.main_priority == 'career_tokyo' and city['scores'].get('job_market', 0) >= 0.8:
            explanations.append("Excellent marché de l'emploi pour votre carrière")

        if user_profile.main_priority == 'traditional_culture' and city['scores'].get('traditional_culture_score', 0) >= 0.8:
            explanations.append("Riche culture traditionnelle japonaise")

        if user_profile.monthly_budget in ['budget_student', 'budget_balanced'] and city['scores'].get('cost_of_living', 0) >= 0.7:
            explanations.append("Coût de la vie adapté à votre budget")

        if user_profile.transport_preference == 'jr_priority' and city['scores'].get('public_transport', 0) >= 0.8:
            explanations.append("Excellente connectivité JR/Shinkansen")

        return " • ".join(explanations) if explanations else "Bon équilibre général selon vos critères"

    def get_recommendations(self, questionnaire_responses: Dict, top_n: int = 3) -> Dict:
        """Interface standardisée pour obtenir les recommandations"""
        try:
            # 1. Création profil utilisateur
            user_profile = self.create_user_profile_japan(questionnaire_responses)
            logger.info(f"🇯🇵 Profil créé: {user_profile.main_priority}, région {user_profile.region_preference}")

            # 2. Filtres pré-scoring pour performance
            cities_list = self.cities_data['cities'].copy()
            cities_list = self.apply_regional_filters(cities_list, user_profile)
            cities_list = self.apply_budget_filters(cities_list, user_profile)
            cities_list = self.apply_deal_breaker_filters(cities_list, user_profile)

            logger.info(f"🔍 Après filtrage: {len(cities_list)} villes à analyser")

            # 3. Ajustement des pondérations
            self.adjust_weights_by_priority(user_profile)
            self.adjust_weights_by_age_work(user_profile)
            self.adjust_weights_by_lifestyle(user_profile)
            self.adjust_weights_by_disaster_tolerance(user_profile)

            # 4. Calcul des scores pour chaque ville filtrée
            scored_cities = []
            for city in cities_list:
                score = self.calculate_city_score(city, user_profile)
                scored_cities.append({
                    **city,
                    'score': score
                })

            # 5. Tri et sélection du top N
            top_cities = sorted(scored_cities, key=lambda x: x['score'], reverse=True)[:top_n]

            logger.info(f"🏆 Top {len(top_cities)} villes sélectionnées")

            # 6. Format de réponse standardisé UK
            return {
                "status": "success",
                "recommendations": [
                    {
                        "city": city['name'],
                        "region": city['region'],
                        "score_percentage": round(city['score']),
                        "population": city['population'],
                        "coordinates": city['coordinates'],
                        "regional_location": city['regional_location'],
                        "top_strengths": self.get_city_strengths(city),
                        "match_explanation": self.generate_match_explanation(city, user_profile)
                    }
                    for city in top_cities
                ],
                "total_analyzed": len(cities_list),
                "algorithm_version": self.version,
                "user_profile_summary": {
                    "priority": user_profile.main_priority,
                    "region": user_profile.region_preference,
                    "budget": user_profile.monthly_budget
                }
            }

        except Exception as e:
            logger.error(f"❌ Erreur algorithme Japon: {e}")
            return {
                "status": "error",
                "message": f"Erreur lors du calcul des recommandations: {str(e)}",
                "algorithm_version": self.version
            }

    def get_health_status(self) -> Dict:
        """Status de santé de l'algorithme pour health check"""
        try:
            cities_count = len(self.cities_data['cities'])
            criteria_count = len(self.criteria_weights_base)

            return {
                "status": "healthy",
                "version": self.version,
                "cities_loaded": cities_count,
                "criteria_count": criteria_count,
                "last_updated": self.cities_data.get('metadata', {}).get('last_updated', 'unknown')
            }
        except Exception as e:
            return {
                "status": "error",
                "version": self.version,
                "error": str(e)
            }
