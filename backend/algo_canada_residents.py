"""
🇨🇦 ALGO-CANADA-RESIDENTS.PY - ALGORITHME MATCHING VILLES CANADA
================================================================
Algorithme ultra performant pour matcher Canadiens avec leurs 3 villes idéales
Author: Revolutionary Team | Version: 1.0.0 - Canada Domestic Matching
OBJECTIF: Recommandations précises basées sur profils canadiens et réalités provinciales
"""

import json
import logging
from typing import Dict, List, Tuple
from dataclasses import dataclass

# Configuration logging
logger = logging.getLogger(__name__)

@dataclass
class UserProfileCanada:
    """Profil utilisateur Canada avec pondérations spécifiquement canadiennes"""
    region_preference: str       # any_region, eastern_canada, western_canada, ontario_quebec_only, avoid_quebec
    language_preference: str     # bilingual_comfortable, primarily_english, primarily_french, english_only, french_only
    main_priority: str           # career_growth, cost_optimization, lifestyle_upgrade, family_focus
    age_profile: str            # student_young, young_professional, established_professional, pre_retirement
    monthly_budget: str         # budget_tight, budget_balanced, budget_comfortable, budget_premium
    work_situation: str         # stable_employment, job_search, full_remote, entrepreneur
    housing_preference: str     # downtown_condo, suburban_house, transport_connected, budget_priority
    transport_preference: str   # walk_bike_priority, public_transport_fan, car_essential, multimodal_flexible
    climate_preference: str     # mild_coastal, continental_four_seasons, prairie_dry, climate_adaptable
    social_scene: str          # outdoor_sports, arts_culture, dining_nightlife, quiet_community
    family_situation: str      # single_no_children, couple_no_children, young_family, teen_family
    deal_breaker: str         # cost_too_high, harsh_winter, limited_job_market, isolation_boredom
    criteria_weights: Dict[str, float]

class CanadaResidentsAlgorithm:
    """🎯 Algorithme de matching ultra sophistiqué pour résidents Canada"""

    def __init__(self, cities_data_path: str):
        """Initialise l'algorithme avec les données des 30 principales villes canadiennes"""
        self.cities_data = self.load_cities_data(cities_data_path)
        self.criteria_weights_base = self.get_base_criteria_weights_canada()

    def load_cities_data(self, data_path: str) -> Dict:
        """Charge les données des 30 villes canadiennes"""
        try:
            with open(data_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            logger.info(f"🇨🇦 Données Canada chargées: {len(data['cities'])} villes")
            return data
        except Exception as e:
            logger.error(f"❌ Erreur chargement données Canada: {e}")
            return {"cities": [], "metadata": {}, "criteria_definitions": {}}

    def get_base_criteria_weights_canada(self) -> Dict[str, float]:
        """Poids de base adaptés au marché et à la mentalité canadienne"""
        return {
            "cost_of_living": 1.0,
            "housing_affordability": 1.0,
            "income_tax_burden": 0.7,          # Taxes importantes au Canada
            "local_tax": 0.6,
            "property_tax": 0.6,
            "climate_rating": 1.2,            # Climat très important au Canada
            "weather_consistency": 0.8,
            "job_market": 0.9,
            "tech_industry": 0.7,
            "remote_work_friendly": 0.8,      # Important post-COVID
            "urban_density": 0.7,
            "suburb_quality": 0.9,            # Banlieues très importantes au Canada
            "public_transport": 0.8,
            "walkability": 0.7,
            "car_dependency": 0.8,            # Voiture souvent nécessaire
            "school_quality": 0.9,            # Système éducation publique important
            "university_access": 0.7,
            "natural_disaster_risk": 0.8,
            "flood_risk": 0.7,
            "heat_wave_risk": 0.6,            # Moins problématique qu'ailleurs
            "healthcare_access": 0.9,         # Système santé public crucial
            "hospital_quality": 0.8,
            "cultural_scene": 0.7,
            "restaurant_diversity": 0.7,
            "nightlife": 0.6,
            "french_language_score": 0.5,     # Nouveau critère linguistique
            "english_language_score": 0.5     # Nouveau critère linguistique
        }

    def create_user_profile_canada(self, questionnaire_responses: Dict) -> UserProfileCanada:
        """🧠 Crée profil utilisateur canadien personnalisé à partir des réponses"""

        # Extraction des réponses spécifiques Canada
        region_preference = questionnaire_responses.get('canada_region_preference')
        language_preference = questionnaire_responses.get('canada_language_preference')
        main_priority = questionnaire_responses.get('canada_main_priority')
        age_profile = questionnaire_responses.get('canada_age_profile')
        monthly_budget = questionnaire_responses.get('canada_monthly_budget')
        work_situation = questionnaire_responses.get('canada_work_situation')
        housing_preference = questionnaire_responses.get('canada_housing_preference')
        transport_preference = questionnaire_responses.get('canada_transport_preference')
        climate_preference = questionnaire_responses.get('canada_climate_preference')
        social_scene = questionnaire_responses.get('canada_social_scene')
        family_situation = questionnaire_responses.get('canada_family_situation')
        deal_breaker = questionnaire_responses.get('canada_deal_breaker')

        # 🎯 CALCUL PONDÉRATIONS PERSONNALISÉES CANADA
        weights = self.criteria_weights_base.copy()

        # === BOOST PRÉFÉRENCES LINGUISTIQUES ===
        if language_preference == 'primarily_french' or language_preference == 'french_only':
            weights['french_language_score'] *= 2.5
            weights['english_language_score'] *= 0.3
        elif language_preference == 'primarily_english' or language_preference == 'english_only':
            weights['english_language_score'] *= 2.5
            weights['french_language_score'] *= 0.3
        elif language_preference == 'bilingual_comfortable':
            weights['french_language_score'] *= 1.2
            weights['english_language_score'] *= 1.2

        # === BOOST PRIORITÉ PRINCIPALE ===
        if main_priority == 'career_growth':
            weights['job_market'] *= 1.8
            weights['tech_industry'] *= 1.6
            weights['remote_work_friendly'] *= 1.4
            weights['university_access'] *= 1.2
        elif main_priority == 'cost_optimization':
            weights['cost_of_living'] *= 1.8
            weights['housing_affordability'] *= 1.7
            weights['income_tax_burden'] *= 1.5
            weights['local_tax'] *= 1.3
            weights['property_tax'] *= 1.3
        elif main_priority == 'lifestyle_upgrade':
            weights['climate_rating'] *= 1.7
            weights['cultural_scene'] *= 1.5
            weights['restaurant_diversity'] *= 1.4
            weights['walkability'] *= 1.3
            weights['natural_disaster_risk'] *= 1.2
        elif main_priority == 'family_focus':
            weights['school_quality'] *= 1.8
            weights['suburb_quality'] *= 1.6
            weights['healthcare_access'] *= 1.5
            weights['natural_disaster_risk'] *= 1.3
            weights['hospital_quality'] *= 1.2

        # === ADAPTATION PROFIL ÂGE ===
        if age_profile == 'student_young':
            weights['university_access'] *= 1.6
            weights['cost_of_living'] *= 1.5
            weights['public_transport'] *= 1.4
            weights['cultural_scene'] *= 1.3
            weights['nightlife'] *= 1.3
        elif age_profile == 'young_professional':
            weights['job_market'] *= 1.5
            weights['tech_industry'] *= 1.4
            weights['nightlife'] *= 1.3
            weights['restaurant_diversity'] *= 1.2
        elif age_profile == 'established_professional':
            weights['suburb_quality'] *= 1.4
            weights['school_quality'] *= 1.3
            weights['healthcare_access'] *= 1.2
            weights['car_dependency'] *= 0.8  # Moins préoccupant
        elif age_profile == 'pre_retirement':
            weights['healthcare_access'] *= 1.6
            weights['hospital_quality'] *= 1.5
            weights['climate_rating'] *= 1.4
            weights['natural_disaster_risk'] *= 1.3
            weights['cost_of_living'] *= 1.2
            weights['nightlife'] *= 0.6

        # === ADAPTATION BUDGET CAD ===
        if monthly_budget == 'budget_tight':
            weights['cost_of_living'] *= 1.8
            weights['housing_affordability'] *= 1.7
            weights['public_transport'] *= 1.4  # Moins cher que voiture
        elif monthly_budget == 'budget_balanced':
            weights['cost_of_living'] *= 1.3
            weights['housing_affordability'] *= 1.2
        elif monthly_budget == 'budget_comfortable':
            weights['suburb_quality'] *= 1.3
            weights['school_quality'] *= 1.2
        elif monthly_budget == 'budget_premium':
            weights['cultural_scene'] *= 1.4
            weights['restaurant_diversity'] *= 1.3
            weights['urban_density'] *= 1.2

        # === SITUATION PROFESSIONNELLE CANADIENNE ===
        if work_situation == 'stable_employment':
            weights['healthcare_access'] *= 1.2
            weights['suburb_quality'] *= 1.2
        elif work_situation == 'job_search':
            weights['job_market'] *= 1.8
            weights['tech_industry'] *= 1.5
            weights['university_access'] *= 1.2  # Réseau professionnel
        elif work_situation == 'full_remote':
            weights['remote_work_friendly'] *= 1.6
            weights['cost_of_living'] *= 1.4
            weights['climate_rating'] *= 1.3
            weights['job_market'] *= 0.7  # Moins important
        elif work_situation == 'entrepreneur':
            weights['tech_industry'] *= 1.5
            weights['cultural_scene'] *= 1.3
            weights['remote_work_friendly'] *= 1.2

        # === PRÉFÉRENCE LOGEMENT CANADIEN ===
        if housing_preference == 'downtown_condo':
            weights['urban_density'] *= 1.5
            weights['public_transport'] *= 1.4
            weights['walkability'] *= 1.4
            weights['cultural_scene'] *= 1.3
            weights['car_dependency'] *= 1.3  # Pouvoir éviter la voiture
        elif housing_preference == 'suburban_house':
            weights['suburb_quality'] *= 1.6
            weights['school_quality'] *= 1.4
            weights['car_dependency'] *= 0.7  # Voiture acceptée
        elif housing_preference == 'transport_connected':
            weights['public_transport'] *= 1.6
            weights['walkability'] *= 1.3
            weights['car_dependency'] *= 1.2
        elif housing_preference == 'budget_priority':
            weights['housing_affordability'] *= 1.7
            weights['cost_of_living'] *= 1.5

        # === TRANSPORT CANADIEN ===
        if transport_preference == 'walk_bike_priority':
            weights['walkability'] *= 1.7
            weights['urban_density'] *= 1.4
            weights['car_dependency'] *= 1.5
        elif transport_preference == 'public_transport_fan':
            weights['public_transport'] *= 1.8
            weights['urban_density'] *= 1.3
            weights['car_dependency'] *= 1.4
        elif transport_preference == 'car_essential':
            weights['car_dependency'] *= 0.5  # Pas un problème
            weights['suburb_quality'] *= 1.3
        elif transport_preference == 'multimodal_flexible':
            weights['public_transport'] *= 1.2
            weights['walkability'] *= 1.2

        # === CLIMAT CANADIEN ===
        if climate_preference == 'mild_coastal':
            weights['climate_rating'] *= 1.8
            weights['weather_consistency'] *= 1.5
            weights['heat_wave_risk'] *= 1.3
        elif climate_preference == 'continental_four_seasons':
            weights['climate_rating'] *= 1.3
            weights['weather_consistency'] *= 1.2
        elif climate_preference == 'prairie_dry':
            weights['climate_rating'] *= 1.4
            weights['weather_consistency'] *= 1.6
        # climate_adaptable: pas de boost particulier

        # === SCÈNE SOCIALE CANADIENNE ===
        if social_scene == 'outdoor_sports':
            weights['climate_rating'] *= 1.4
            weights['natural_disaster_risk'] *= 1.2
        elif social_scene == 'arts_culture':
            weights['cultural_scene'] *= 1.7
            weights['university_access'] *= 1.3
        elif social_scene == 'dining_nightlife':
            weights['restaurant_diversity'] *= 1.6
            weights['nightlife'] *= 1.5
            weights['urban_density'] *= 1.3
        elif social_scene == 'quiet_community':
            weights['suburb_quality'] *= 1.5
            weights['natural_disaster_risk'] *= 1.3
            weights['nightlife'] *= 0.7

        # === SITUATION FAMILIALE CANADIENNE ===
        if family_situation == 'single_no_children':
            weights['nightlife'] *= 1.4
            weights['cultural_scene'] *= 1.3
            weights['restaurant_diversity'] *= 1.2
            weights['school_quality'] *= 0.6
        elif family_situation == 'couple_no_children':
            weights['restaurant_diversity'] *= 1.3
            weights['cultural_scene'] *= 1.2
            weights['school_quality'] *= 0.7
        elif family_situation == 'young_family':
            weights['school_quality'] *= 1.7
            weights['suburb_quality'] *= 1.5
            weights['healthcare_access'] *= 1.4
            weights['natural_disaster_risk'] *= 1.4
            weights['nightlife'] *= 0.6
        elif family_situation == 'teen_family':
            weights['school_quality'] *= 1.6
            weights['university_access'] *= 1.4
            weights['suburb_quality'] *= 1.3
            weights['cultural_scene'] *= 1.2

        return UserProfileCanada(
            region_preference=region_preference,
            language_preference=language_preference,
            main_priority=main_priority,
            age_profile=age_profile,
            monthly_budget=monthly_budget,
            work_situation=work_situation,
            housing_preference=housing_preference,
            transport_preference=transport_preference,
            climate_preference=climate_preference,
            social_scene=social_scene,
            family_situation=family_situation,
            deal_breaker=deal_breaker,
            criteria_weights=weights
        )

    def calculate_city_score_canada(self, city_data: Dict, user_profile: UserProfileCanada) -> float:
        """🧮 Calcule le score total d'une ville canadienne pour un profil utilisateur"""

        total_score = 0.0
        total_weight = 0.0

        for criterion, city_value in city_data['scores'].items():
            if criterion in user_profile.criteria_weights:
                weight = user_profile.criteria_weights[criterion]
                total_score += city_value * weight
                total_weight += weight

        # Score normalisé (0.0 à 1.0)
        normalized_score = total_score / total_weight if total_weight > 0 else 0.0

        return normalized_score

    def apply_canada_bonuses(self, city_data: Dict, base_score: float, user_profile: UserProfileCanada) -> float:
        """🚀 Applique des bonus/malus spécifiquement canadiens"""

        bonus_score = base_score
        city_scores = city_data['scores']

        # === BONUS SYNERGIES CANADIENNES ===

        # Bonus "Hub Tech Canadien" (Toronto/Vancouver tech)
        if (city_scores.get('tech_industry', 0) > 0.8 and
            city_scores.get('job_market', 0) > 0.8 and
            city_scores.get('university_access', 0) > 0.8 and
            user_profile.main_priority == 'career_growth'):
            bonus_score *= 1.15
            logger.debug(f"🚀 Bonus Hub Tech Canadien appliqué: {city_data['name']}")

        # Bonus "Côte Ouest Paradis" (climat + qualité vie + outdoor)
        if (city_scores.get('climate_rating', 0) > 0.75 and
            city_scores.get('weather_consistency', 0) > 0.6 and
            user_profile.climate_preference == 'mild_coastal' and
            user_profile.social_scene == 'outdoor_sports'):
            bonus_score *= 1.18
            logger.debug(f"🌊 Bonus Côte Ouest Paradis appliqué: {city_data['name']}")

        # Bonus "Famille Parfaite Canada" (écoles + banlieue + santé)
        if (city_scores.get('school_quality', 0) > 0.75 and
            city_scores.get('suburb_quality', 0) > 0.75 and
            city_scores.get('healthcare_access', 0) > 0.8 and
            user_profile.family_situation in ['young_family', 'teen_family']):
            bonus_score *= 1.12
            logger.debug(f"👨‍👩‍👧‍👦 Bonus Famille Parfaite Canada appliqué: {city_data['name']}")

        # Bonus "Étudiant Optimal Canada" (coût + université + transport)
        if (city_scores.get('cost_of_living', 0) > 0.65 and
            city_scores.get('university_access', 0) > 0.8 and
            city_scores.get('public_transport', 0) > 0.6 and
            user_profile.age_profile == 'student_young'):
            bonus_score *= 1.10
            logger.debug(f"🎓 Bonus Étudiant Optimal Canada appliqué: {city_data['name']}")

        # Bonus "Retraité Confortable" (santé + climat + coût)
        if (city_scores.get('healthcare_access', 0) > 0.8 and
            city_scores.get('climate_rating', 0) > 0.6 and
            city_scores.get('cost_of_living', 0) > 0.6 and
            user_profile.age_profile == 'pre_retirement'):
            bonus_score *= 1.08
            logger.debug(f"🏡 Bonus Retraité Confortable appliqué: {city_data['name']}")

        # === MALUS DEAL-BREAKERS CANADIENS ===

        # Malus budget serré + ville chère
        if (user_profile.monthly_budget == 'budget_tight' and
            city_scores.get('housing_affordability', 1.0) < 0.4):
            bonus_score *= 0.6
            logger.debug(f"💸 Malus ville trop chère appliqué: {city_data['name']}")

        # Malus hiver rigoureux + préférence climat doux
        if (user_profile.deal_breaker == 'harsh_winter' and
            city_scores.get('climate_rating', 1.0) < 0.4):
            bonus_score *= 0.5
            logger.debug(f"🥶 Malus hiver rigoureux appliqué: {city_data['name']}")

        # Malus recherche emploi + marché faible
        if (user_profile.work_situation == 'job_search' and
            city_scores.get('job_market', 1.0) < 0.6):
            bonus_score *= 0.7
            logger.debug(f"📉 Malus marché emploi faible appliqué: {city_data['name']}")

        # Malus isolement + petite ville
        if (user_profile.deal_breaker == 'isolation_boredom' and
            city_data.get('population', 0) < 200000):
            bonus_score *= 0.8
            logger.debug(f"😴 Malus isolement appliqué: {city_data['name']}")

        return min(bonus_score, 1.0)  # Cap à 1.0

    def apply_regional_language_filters(self, cities_list: List[Dict], user_profile: UserProfileCanada) -> List[Dict]:
        """🗺️ Applique filtres régionaux et linguistiques AVANT le scoring"""

        filtered_cities = []

        for city in cities_list:
            city_region = city.get('region', 'unknown')
            city_province = city.get('province', '')
            city_language = city.get('primary_language', 'english')

            # === FILTRAGE RÉGIONAL ===
            region_match = True
            if user_profile.region_preference == 'eastern_canada':
                region_match = city_region == 'eastern_canada'
            elif user_profile.region_preference == 'western_canada':
                region_match = city_region == 'western_canada'
            elif user_profile.region_preference == 'ontario_quebec_only':
                region_match = city_province in ['Ontario', 'Quebec']
            elif user_profile.region_preference == 'avoid_quebec':
                region_match = city_province != 'Quebec'
            # 'any_region' accepte tout

            # === FILTRAGE LINGUISTIQUE STRICT ===
            language_match = True
            if user_profile.language_preference == 'french_only':
                language_match = city_language in ['french', 'bilingual']
            elif user_profile.language_preference == 'english_only':
                language_match = city_language in ['english', 'bilingual']
            # Autres préférences linguistiques: pas de filtrage strict, juste pondération

            # Garder la ville si elle passe les filtres
            if region_match and language_match:
                filtered_cities.append(city)
                logger.debug(f"✅ {city['name']} - Region: {city_region}, Language: {city_language}")
            else:
                logger.debug(f"❌ {city['name']} filtré - Region: {city_region}, Language: {city_language}")

        logger.info(f"🔍 Filtrage régional/linguistique: {len(filtered_cities)}/{len(cities_list)} villes conservées")
        return filtered_cities

    def get_top_recommendations_canada(self, questionnaire_responses: Dict, top_n: int = 3) -> List[Dict]:
        """🏆 Retourne les top N recommandations de villes canadiennes"""

        try:
            # Créer profil utilisateur
            user_profile = self.create_user_profile_canada(questionnaire_responses)
            logger.info(f"🇨🇦 Profil Canada créé: {user_profile.main_priority}, {user_profile.age_profile}")
            logger.info(f"🗺️ Filtres: région={user_profile.region_preference}, langue={user_profile.language_preference}")

            # ÉTAPE 1: Appliquer filtres régionaux et linguistiques
            all_cities = self.cities_data.get('cities', [])
            filtered_cities = self.apply_regional_language_filters(all_cities, user_profile)

            if len(filtered_cities) == 0:
                logger.warning("❌ Aucune ville ne correspond aux filtres régionaux/linguistiques")
                return []

            # ÉTAPE 2: Calculer scores pour les villes filtrées
            city_scores = []
            for city in filtered_cities:
                # Score de base
                base_score = self.calculate_city_score_canada(city, user_profile)

                # Appliquer bonus/malus
                final_score = self.apply_canada_bonuses(city, base_score, user_profile)

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
                    'province': city_data['province'],
                    'score_percentage': round(score * 100, 1),
                    'population': city_data.get('population', 'N/A'),
                    'coordinates': city_data.get('coordinates', {}),
                    'primary_language': city_data.get('primary_language', 'english'),
                    'region': city_data.get('region', 'unknown'),
                    'strengths': self.get_city_strengths_canada(city_data, user_profile),
                    'concerns': self.get_city_concerns_canada(city_data, user_profile),
                    'recommendation_reason': self.generate_recommendation_reason_canada(city_data, user_profile),
                    'rank': i + 1
                }
                recommendations.append(recommendation)

            logger.info(f"🏆 Top {len(recommendations)} recommandations Canada générées (sur {len(filtered_cities)} villes filtrées)")
            return recommendations

        except Exception as e:
            logger.error(f"❌ Erreur génération recommandations Canada: {e}")
            return []

    def get_city_strengths_canada(self, city_data: Dict, user_profile: UserProfileCanada) -> List[str]:
        """💪 Identifie les forces principales d'une ville canadienne"""

        strengths = []
        scores = city_data['scores']

        # Forces basées sur les scores élevés
        if scores.get('cost_of_living', 0) > 0.7:
            strengths.append("Coût de la vie abordable")
        if scores.get('housing_affordability', 0) > 0.6:
            strengths.append("Logement accessible")
        if scores.get('job_market', 0) > 0.8:
            strengths.append("Marché du travail dynamique")
        if scores.get('tech_industry', 0) > 0.7:
            strengths.append("Secteur technologique développé")
        if scores.get('climate_rating', 0) > 0.7:
            strengths.append("Climat agréable")
        if scores.get('public_transport', 0) > 0.7:
            strengths.append("Excellent transport public")
        if scores.get('school_quality', 0) > 0.8:
            strengths.append("Écoles de qualité supérieure")
        if scores.get('healthcare_access', 0) > 0.8:
            strengths.append("Accès aux soins de santé excellent")
        if scores.get('cultural_scene', 0) > 0.7:
            strengths.append("Scène culturelle vibrante")
        if scores.get('walkability', 0) > 0.7:
            strengths.append("Quartiers très marchables")

        return strengths[:4]  # Top 4 forces

    def get_city_concerns_canada(self, city_data: Dict, user_profile: UserProfileCanada) -> List[str]:
        """⚠️ Identifie les préoccupations potentielles d'une ville canadienne"""

        concerns = []
        scores = city_data['scores']

        # Préoccupations basées sur les scores faibles
        if scores.get('cost_of_living', 1.0) < 0.4:
            concerns.append("Coût de la vie élevé")
        if scores.get('housing_affordability', 1.0) < 0.3:
            concerns.append("Logement très cher")
        if scores.get('climate_rating', 1.0) < 0.4:
            concerns.append("Climat rigoureux")
        if scores.get('job_market', 1.0) < 0.6:
            concerns.append("Marché du travail limité")
        if scores.get('public_transport', 1.0) < 0.5:
            concerns.append("Transport public insuffisant")
        if scores.get('car_dependency', 1.0) < 0.4:
            concerns.append("Dépendance élevée à la voiture")

        return concerns[:3]  # Top 3 préoccupations

    def generate_recommendation_reason_canada(self, city_data: Dict, user_profile: UserProfileCanada) -> str:
        """📝 Génère une raison personnalisée pour une recommandation canadienne"""

        city_name = city_data['name']
        main_priority = user_profile.main_priority

        if main_priority == 'career_growth':
            return f"{city_name} offre un marché du travail dynamique avec d'excellentes opportunités de carrière dans votre secteur."
        elif main_priority == 'cost_optimization':
            return f"{city_name} présente un coût de la vie raisonnable avec des options de logement abordables."
        elif main_priority == 'lifestyle_upgrade':
            return f"{city_name} combine un climat agréable avec une riche offre culturelle et de loisirs."
        elif main_priority == 'family_focus':
            return f"{city_name} excelle pour les familles avec d'excellentes écoles et des quartiers sûrs."
        else:
            return f"{city_name} répond parfaitement à vos critères de relocation au Canada."

# Fonction factory pour être utilisé dans main.py
def create_canada_residents_algorithm():
    """Factory pour créer l'instance de l'algorithme Canada"""
    return CanadaResidentsAlgorithm('/var/www/Revolutionnary/platform/backend/data_v2/villes_canada_residents.json')
