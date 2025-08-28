"""
🇬🇧 ALGO-UK-RESIDENTS.PY - ALGORITHME MATCHING VILLES UK
================================================================
Algorithme ultra performant pour matcher Britanniques avec leurs 3 villes idéales
Author: Revolutionary Team | Version: 1.0.0 - UK Domestic Matching
OBJECTIF: Recommandations précises basées sur profils britanniques et réalités régionales
"""

import json
import logging
from typing import Dict, List, Tuple
from dataclasses import dataclass

# Configuration logging
logger = logging.getLogger(__name__)

@dataclass
class UserProfileUK:
    """Profil utilisateur UK avec pondérations spécifiquement britanniques"""
    region_preference: str       # any_region, london_southeast, northern_england, scotland, wales, central_england
    language_preference: str     # english_only, welsh_friendly, language_flexible
    main_priority: str           # career_growth, cost_optimization, lifestyle_upgrade, family_focus
    age_profile: str            # student_young, young_professional, established_professional, pre_retirement
    monthly_budget: str         # budget_tight, budget_balanced, budget_comfortable, budget_premium
    work_situation: str         # stable_employment, job_search, full_remote, freelance_entrepreneur
    housing_preference: str     # city_centre_flat, suburban_house, transport_connected, budget_priority
    transport_preference: str   # walk_cycle_priority, public_transport_fan, car_essential, multimodal_flexible
    climate_preference: str     # mild_southern, maritime_western, continental_northern, climate_adaptable
    social_scene: str          # pubs_traditional, arts_culture, cosmopolitan_dining, quiet_countryside
    family_situation: str      # single_no_children, couple_no_children, young_family, teen_family
    deal_breaker: str         # cost_too_high, poor_transport, limited_job_market, social_isolation
    criteria_weights: Dict[str, float]

class UKResidentsAlgorithm:
    """�🇧 Algorithme de recommandation pour résidents UK"""

    def __init__(self, cities_data_path: str):
        """Initialise l'algorithme avec les données des 30 principales villes britanniques"""
        self.version = "1.0.0"
        self.cities_data = self.load_cities_data(cities_data_path)
        self.criteria_weights_base = self.get_base_criteria_weights_uk()

    def load_cities_data(self, data_path: str) -> Dict:
        """Charge les données des 30 villes britanniques"""
        try:
            with open(data_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            logger.info(f"🇬🇧 Données UK chargées: {len(data['cities'])} villes")
            return data
        except Exception as e:
            logger.error(f"❌ Erreur chargement données UK: {e}")
            return {"cities": [], "metadata": {}, "criteria_definitions": {}}

    def get_base_criteria_weights_uk(self) -> Dict[str, float]:
        """Poids de base adaptés au marché et à la mentalité britannique"""
        return {
            "cost_of_living": 1.0,
            "housing_affordability": 1.2,      # Housing crisis UK très important
            "income_tax_burden": 0.8,
            "local_tax": 0.7,
            "council_tax": 0.9,                # Council tax spécifique UK
            "climate_rating": 0.8,             # Climat moins déterminant qu'ailleurs
            "weather_consistency": 0.6,
            "job_market": 1.0,
            "tech_industry": 0.8,
            "remote_work_friendly": 0.9,      # Post-Brexit, post-COVID important
            "urban_density": 0.7,
            "suburb_quality": 1.0,            # Suburban dream britannique
            "public_transport": 1.1,          # Très important, surtout Londres
            "walkability": 0.8,
            "car_dependency": 0.7,            # Variable selon région
            "school_quality": 1.0,            # Système éducatif public crucial
            "university_access": 0.8,
            "natural_disaster_risk": 0.9,
            "flood_risk": 0.8,                # Inondations problème UK
            "heat_wave_risk": 0.6,            # Moins problématique
            "healthcare_access": 1.1,         # NHS absolument critique
            "hospital_quality": 0.9,
            "cultural_scene": 0.8,
            "restaurant_diversity": 0.7,
            "nightlife": 0.6,
            "english_language_score": 0.5,    # Score environnement anglophone
            "welsh_language_score": 0.3       # Score environnement gallois
        }

    def create_user_profile_uk(self, questionnaire_responses: Dict) -> UserProfileUK:
        """🧠 Crée profil utilisateur britannique personnalisé à partir des réponses"""

        # Extraction des réponses spécifiques UK
        region_preference = questionnaire_responses.get('uk_region_preference')
        language_preference = questionnaire_responses.get('uk_language_preference')
        main_priority = questionnaire_responses.get('uk_main_priority')
        age_profile = questionnaire_responses.get('uk_age_profile')
        monthly_budget = questionnaire_responses.get('uk_monthly_budget')
        work_situation = questionnaire_responses.get('uk_work_situation')
        housing_preference = questionnaire_responses.get('uk_housing_preference')
        transport_preference = questionnaire_responses.get('uk_transport_preference')
        climate_preference = questionnaire_responses.get('uk_climate_preference')
        social_scene = questionnaire_responses.get('uk_social_scene')
        family_situation = questionnaire_responses.get('uk_family_situation')
        deal_breaker = questionnaire_responses.get('uk_deal_breaker')

        # 🎯 CALCUL PONDÉRATIONS PERSONNALISÉES UK
        weights = self.criteria_weights_base.copy()

        # === BOOST PRÉFÉRENCES LINGUISTIQUES ===
        if language_preference == 'welsh_friendly':
            weights['welsh_language_score'] *= 3.0
            weights['english_language_score'] *= 1.2
        elif language_preference == 'english_only':
            weights['english_language_score'] *= 1.5
            weights['welsh_language_score'] *= 0.2
        # language_flexible: pas de modification

        # === BOOST PRIORITÉ PRINCIPALE ===
        if main_priority == 'career_growth':
            weights['job_market'] *= 1.8
            weights['tech_industry'] *= 1.6
            weights['remote_work_friendly'] *= 1.4
            weights['university_access'] *= 1.2
        elif main_priority == 'cost_optimization':
            weights['cost_of_living'] *= 1.8
            weights['housing_affordability'] *= 1.7
            weights['council_tax'] *= 1.6
            weights['local_tax'] *= 1.3
        elif main_priority == 'lifestyle_upgrade':
            weights['climate_rating'] *= 1.5
            weights['cultural_scene'] *= 1.4
            weights['walkability'] *= 1.3
            weights['restaurant_diversity'] *= 1.2
        elif main_priority == 'family_focus':
            weights['school_quality'] *= 1.8
            weights['suburb_quality'] *= 1.6
            weights['healthcare_access'] *= 1.5
            weights['natural_disaster_risk'] *= 1.3

        # === ADAPTATION PROFIL ÂGE UK ===
        if age_profile == 'student_young':
            weights['university_access'] *= 1.7
            weights['cost_of_living'] *= 1.6
            weights['public_transport'] *= 1.4
            weights['nightlife'] *= 1.3
            weights['cultural_scene'] *= 1.2
        elif age_profile == 'young_professional':
            weights['job_market'] *= 1.5
            weights['tech_industry'] *= 1.4
            weights['nightlife'] *= 1.2
            weights['restaurant_diversity'] *= 1.2
        elif age_profile == 'established_professional':
            weights['suburb_quality'] *= 1.4
            weights['school_quality'] *= 1.3
            weights['healthcare_access'] *= 1.2
            weights['car_dependency'] *= 0.8
        elif age_profile == 'pre_retirement':
            weights['healthcare_access'] *= 1.7
            weights['climate_rating'] *= 1.5
            weights['cost_of_living'] *= 1.3
            weights['natural_disaster_risk'] *= 1.3
            weights['nightlife'] *= 0.5

        # === ADAPTATION BUDGET £ ===
        if monthly_budget == 'budget_tight':
            weights['cost_of_living'] *= 1.8
            weights['housing_affordability'] *= 1.7
            weights['council_tax'] *= 1.5
            weights['public_transport'] *= 1.4
        elif monthly_budget == 'budget_balanced':
            weights['cost_of_living'] *= 1.3
            weights['housing_affordability'] *= 1.2
        elif monthly_budget == 'budget_comfortable':
            weights['suburb_quality'] *= 1.3
            weights['school_quality'] *= 1.2
        elif monthly_budget == 'budget_premium':
            weights['cultural_scene'] *= 1.4
            weights['restaurant_diversity'] *= 1.3

        # === SITUATION PROFESSIONNELLE UK ===
        if work_situation == 'stable_employment':
            weights['healthcare_access'] *= 1.2
            weights['suburb_quality'] *= 1.2
        elif work_situation == 'job_search':
            weights['job_market'] *= 1.9
            weights['tech_industry'] *= 1.5
            weights['university_access'] *= 1.2
        elif work_situation == 'full_remote':
            weights['remote_work_friendly'] *= 1.6
            weights['cost_of_living'] *= 1.4
            weights['climate_rating'] *= 1.3
            weights['job_market'] *= 0.6
        elif work_situation == 'freelance_entrepreneur':
            weights['tech_industry'] *= 1.5
            weights['cultural_scene'] *= 1.3
            weights['remote_work_friendly'] *= 1.2

        # === PRÉFÉRENCE LOGEMENT UK ===
        if housing_preference == 'city_centre_flat':
            weights['public_transport'] *= 1.6
            weights['walkability'] *= 1.5
            weights['cultural_scene'] *= 1.4
            weights['nightlife'] *= 1.3
            weights['car_dependency'] *= 1.4
        elif housing_preference == 'suburban_house':
            weights['suburb_quality'] *= 1.7
            weights['school_quality'] *= 1.4
            weights['car_dependency'] *= 0.6
        elif housing_preference == 'transport_connected':
            weights['public_transport'] *= 1.8
            weights['walkability'] *= 1.3
            weights['car_dependency'] *= 1.3
        elif housing_preference == 'budget_priority':
            weights['housing_affordability'] *= 1.8
            weights['cost_of_living'] *= 1.5

        # === TRANSPORT UK ===
        if transport_preference == 'walk_cycle_priority':
            weights['walkability'] *= 1.8
            weights['car_dependency'] *= 1.6
            weights['public_transport'] *= 1.3
        elif transport_preference == 'public_transport_fan':
            weights['public_transport'] *= 1.9
            weights['car_dependency'] *= 1.5
            weights['walkability'] *= 1.2
        elif transport_preference == 'car_essential':
            weights['car_dependency'] *= 0.4
            weights['suburb_quality'] *= 1.3
        elif transport_preference == 'multimodal_flexible':
            weights['public_transport'] *= 1.3
            weights['walkability'] *= 1.2

        # === CLIMAT UK ===
        if climate_preference == 'mild_southern':
            weights['climate_rating'] *= 1.6
            weights['weather_consistency'] *= 1.4
        elif climate_preference == 'maritime_western':
            weights['climate_rating'] *= 1.3
            weights['weather_consistency'] *= 1.2
        elif climate_preference == 'continental_northern':
            weights['climate_rating'] *= 1.2
        # climate_adaptable: pas de boost

        # === SCÈNE SOCIALE UK ===
        if social_scene == 'pubs_traditional':
            weights['cultural_scene'] *= 1.3
            weights['suburb_quality'] *= 1.2
        elif social_scene == 'arts_culture':
            weights['cultural_scene'] *= 1.7
            weights['university_access'] *= 1.3
            weights['nightlife'] *= 1.2
        elif social_scene == 'cosmopolitan_dining':
            weights['restaurant_diversity'] *= 1.6
            weights['cultural_scene'] *= 1.3
            weights['nightlife'] *= 1.2
        elif social_scene == 'quiet_countryside':
            weights['suburb_quality'] *= 1.6
            weights['natural_disaster_risk'] *= 1.4
            weights['nightlife'] *= 0.6

        # === SITUATION FAMILIALE UK ===
        if family_situation == 'single_no_children':
            weights['nightlife'] *= 1.4
            weights['cultural_scene'] *= 1.3
            weights['restaurant_diversity'] *= 1.2
            weights['school_quality'] *= 0.5
        elif family_situation == 'couple_no_children':
            weights['restaurant_diversity'] *= 1.3
            weights['cultural_scene'] *= 1.2
            weights['school_quality'] *= 0.6
        elif family_situation == 'young_family':
            weights['school_quality'] *= 1.8
            weights['suburb_quality'] *= 1.6
            weights['healthcare_access'] *= 1.5
            weights['natural_disaster_risk'] *= 1.4
            weights['nightlife'] *= 0.5
        elif family_situation == 'teen_family':
            weights['school_quality'] *= 1.7
            weights['university_access'] *= 1.5
            weights['suburb_quality'] *= 1.3
            weights['healthcare_access'] *= 1.2

        return UserProfileUK(
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

    def apply_regional_language_filters(self, cities_list: List[Dict], user_profile: UserProfileUK) -> List[Dict]:
        """🗺️ Applique filtres régionaux et linguistiques AVANT le scoring"""

        filtered_cities = []

        for city in cities_list:
            city_region_location = city.get('regional_location', 'unknown')
            city_country = city.get('country', 'England')
            city_language = city.get('primary_language', 'english')

            # === FILTRAGE RÉGIONAL ===
            region_match = True
            if user_profile.region_preference == 'london_southeast':
                region_match = city_region_location == 'southern_england' and city.get('name') in ['London', 'Reading', 'Oxford', 'Bath', 'Brighton']
            elif user_profile.region_preference == 'northern_england':
                region_match = city_region_location == 'northern_england'
            elif user_profile.region_preference == 'scotland':
                region_match = city_country == 'Scotland'
            elif user_profile.region_preference == 'wales':
                region_match = city_country == 'Wales'
            elif user_profile.region_preference == 'central_england':
                region_match = city_region_location == 'central_england'
            # 'any_region' accepte tout

            # === FILTRAGE LINGUISTIQUE ===
            language_match = True
            if user_profile.language_preference == 'welsh_friendly':
                language_match = city_language in ['bilingual'] or city_country == 'Wales'
            elif user_profile.language_preference == 'english_only':
                language_match = city_language == 'english' and city_country != 'Wales'
            # 'language_flexible' accepte tout

            # Garder la ville si elle passe les filtres
            if region_match and language_match:
                filtered_cities.append(city)
                logger.debug(f"✅ {city['name']} - Region: {city_region_location}, Country: {city_country}, Language: {city_language}")
            else:
                logger.debug(f"❌ {city['name']} filtré - Region: {city_region_location}, Country: {city_country}")

        logger.info(f"🔍 Filtrage régional/linguistique UK: {len(filtered_cities)}/{len(cities_list)} villes conservées")
        return filtered_cities

    def calculate_city_score_uk(self, city_data: Dict, user_profile: UserProfileUK) -> float:
        """🧮 Calcule le score total d'une ville britannique pour un profil utilisateur"""

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

    def apply_uk_bonuses(self, city_data: Dict, base_score: float, user_profile: UserProfileUK) -> float:
        """🚀 Applique des bonus/malus spécifiquement britanniques"""

        bonus_score = base_score
        city_scores = city_data['scores']

        # === BONUS SYNERGIES UK ===

        # Bonus "London Financial Hub"
        if (city_data['name'] == 'London' and
            city_scores.get('tech_industry', 0) > 0.9 and
            city_scores.get('job_market', 0) > 0.9 and
            user_profile.main_priority == 'career_growth'):
            bonus_score *= 1.20
            logger.debug(f"🏦 Bonus London Financial Hub appliqué")

        # Bonus "Student Paradise UK" (Cambridge, Oxford, Edinburgh)
        if (city_scores.get('university_access', 0) > 0.9 and
            city_scores.get('cultural_scene', 0) > 0.8 and
            user_profile.age_profile == 'student_young'):
            bonus_score *= 1.15
            logger.debug(f"🎓 Bonus Student Paradise UK appliqué: {city_data['name']}")

        # Bonus "Family Haven UK" (suburban + schools + NHS)
        if (city_scores.get('school_quality', 0) > 0.8 and
            city_scores.get('suburb_quality', 0) > 0.75 and
            city_scores.get('healthcare_access', 0) > 0.8 and
            user_profile.family_situation in ['young_family', 'teen_family']):
            bonus_score *= 1.12
            logger.debug(f"👨‍👩‍👧‍👦 Bonus Family Haven UK appliqué: {city_data['name']}")

        # Bonus "Northern Powerhouse" (Manchester, Leeds, Liverpool tech/jobs)
        if (city_data['name'] in ['Manchester', 'Leeds', 'Liverpool'] and
            city_scores.get('job_market', 0) > 0.7 and
            city_scores.get('cost_of_living', 0) > 0.65 and
            user_profile.main_priority in ['career_growth', 'cost_optimization']):
            bonus_score *= 1.10
            logger.debug(f"🏭 Bonus Northern Powerhouse appliqué: {city_data['name']}")

        # Bonus "Welsh Bilingual" (Cardiff, Swansea pour welsh_friendly)
        if (city_data['country'] == 'Wales' and
            city_data.get('primary_language') == 'bilingual' and
            user_profile.language_preference == 'welsh_friendly'):
            bonus_score *= 1.15
            logger.debug(f"🏴󠁧󠁢󠁷󠁬󠁳󠁿 Bonus Welsh Bilingual appliqué: {city_data['name']}")

        # === MALUS DEAL-BREAKERS UK ===

        # Malus budget serré + London/Oxford/Cambridge
        if (user_profile.monthly_budget == 'budget_tight' and
            city_data['name'] in ['London', 'Oxford', 'Cambridge'] and
            city_scores.get('housing_affordability', 1.0) < 0.4):
            bonus_score *= 0.5
            logger.debug(f"💸 Malus ville trop chère UK appliqué: {city_data['name']}")

        # Malus transport public insuffisant + public_transport_fan
        if (user_profile.deal_breaker == 'poor_transport' and
            city_scores.get('public_transport', 1.0) < 0.6):
            bonus_score *= 0.6
            logger.debug(f"🚫 Malus transport insuffisant appliqué: {city_data['name']}")

        # Malus recherche emploi + marché faible
        if (user_profile.work_situation == 'job_search' and
            city_scores.get('job_market', 1.0) < 0.65):
            bonus_score *= 0.7
            logger.debug(f"📉 Malus marché emploi faible UK appliqué: {city_data['name']}")

        return min(bonus_score, 1.0)  # Cap à 1.0

    def get_top_recommendations_uk(self, questionnaire_responses: Dict, top_n: int = 3) -> List[Dict]:
        """🏆 Retourne les top N recommandations de villes britanniques"""

        try:
            # Créer profil utilisateur
            user_profile = self.create_user_profile_uk(questionnaire_responses)
            logger.info(f"🇬🇧 Profil UK créé: {user_profile.main_priority}, {user_profile.age_profile}")
            logger.info(f"🗺️ Filtres: région={user_profile.region_preference}, langue={user_profile.language_preference}")

            # ÉTAPE 1: Appliquer filtres régionaux et linguistiques
            all_cities = self.cities_data.get('cities', [])
            filtered_cities = self.apply_regional_language_filters(all_cities, user_profile)

            if len(filtered_cities) == 0:
                logger.warning("❌ Aucune ville ne correspond aux filtres régionaux/linguistiques UK")
                return []

            # ÉTAPE 2: Calculer scores pour les villes filtrées
            city_scores = []
            for city in filtered_cities:
                # Score de base
                base_score = self.calculate_city_score_uk(city, user_profile)

                # Appliquer bonus/malus
                final_score = self.apply_uk_bonuses(city, base_score, user_profile)

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
                    'country': city_data['country'],
                    'score_percentage': round(score * 100, 1),
                    'population': city_data.get('population', 'N/A'),
                    'coordinates': city_data.get('coordinates', {}),
                    'primary_language': city_data.get('primary_language', 'english'),
                    'regional_location': city_data.get('regional_location', 'unknown'),
                    'strengths': self.get_city_strengths_uk(city_data, user_profile),
                    'concerns': self.get_city_concerns_uk(city_data, user_profile),
                    'recommendation_reason': self.generate_recommendation_reason_uk(city_data, user_profile),
                    'rank': i + 1
                }
                recommendations.append(recommendation)

            logger.info(f"🏆 Top {len(recommendations)} recommandations UK générées (sur {len(filtered_cities)} villes filtrées)")
            return recommendations

        except Exception as e:
            logger.error(f"❌ Erreur génération recommandations UK: {e}")
            return []

    def get_city_strengths_uk(self, city_data: Dict, user_profile: UserProfileUK) -> List[str]:
        """💪 Identifie les forces principales d'une ville britannique"""

        strengths = []
        scores = city_data['scores']

        # Forces basées sur les scores élevés et spécificités UK
        if scores.get('cost_of_living', 0) > 0.7:
            strengths.append("Coût de la vie raisonnable")
        if scores.get('housing_affordability', 0) > 0.6:
            strengths.append("Logement abordable")
        if scores.get('job_market', 0) > 0.8:
            strengths.append("Marché du travail dynamique")
        if scores.get('tech_industry', 0) > 0.7:
            strengths.append("Secteur tech développé")
        if scores.get('public_transport', 0) > 0.8:
            strengths.append("Excellents transports publics")
        if scores.get('school_quality', 0) > 0.8:
            strengths.append("Écoles de qualité supérieure")
        if scores.get('healthcare_access', 0) > 0.8:
            strengths.append("Excellent accès NHS")
        if scores.get('cultural_scene', 0) > 0.8:
            strengths.append("Scène culturelle vibrante")
        if scores.get('walkability', 0) > 0.8:
            strengths.append("Très marchable")
        if scores.get('university_access', 0) > 0.8:
            strengths.append("Proximité universités prestigieuses")

        return strengths[:4]  # Top 4 forces

    def get_city_concerns_uk(self, city_data: Dict, user_profile: UserProfileUK) -> List[str]:
        """⚠️ Identifie les préoccupations potentielles d'une ville britannique"""

        concerns = []
        scores = city_data['scores']

        # Préoccupations basées sur les scores faibles et problématiques UK
        if scores.get('cost_of_living', 1.0) < 0.4:
            concerns.append("Coût de la vie élevé")
        if scores.get('housing_affordability', 1.0) < 0.4:
            concerns.append("Logement très cher")
        if scores.get('council_tax', 1.0) < 0.5:
            concerns.append("Council tax élevé")
        if scores.get('job_market', 1.0) < 0.6:
            concerns.append("Marché du travail limité")
        if scores.get('public_transport', 1.0) < 0.6:
            concerns.append("Transport public insuffisant")
        if scores.get('climate_rating', 1.0) < 0.5:
            concerns.append("Climat difficile")

        return concerns[:3]  # Top 3 préoccupations

    def generate_recommendation_reason_uk(self, city_data: Dict, user_profile: UserProfileUK) -> str:
        """📝 Génère une raison personnalisée pour une recommandation britannique"""

        city_name = city_data['name']
        main_priority = user_profile.main_priority

        if main_priority == 'career_growth':
            return f"{city_name} offre d'excellentes opportunités de carrière avec un marché du travail dynamique."
        elif main_priority == 'cost_optimization':
            return f"{city_name} présente un coût de la vie raisonnable avec des options de logement abordables."
        elif main_priority == 'lifestyle_upgrade':
            return f"{city_name} combine qualité de vie et offre culturelle dans un cadre britannique authentique."
        elif main_priority == 'family_focus':
            return f"{city_name} excelle pour les familles avec d'excellentes écoles et l'accès NHS de qualité."
        else:
            return f"{city_name} répond parfaitement à vos critères de relocation au Royaume-Uni."

    def get_recommendations(self, questionnaire_responses: Dict, top_n: int = 3) -> Dict:
        """🏆 API principale: retourne les recommandations UK sous format standardisé"""
        try:
            # Obtenir les recommandations top N
            raw_recommendations = self.get_top_recommendations_uk(questionnaire_responses, top_n)

            if not raw_recommendations:
                return {
                    'status': 'error',
                    'recommendations': [],
                    'message': 'Aucune recommandation disponible pour vos critères UK'
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
                    'primary_language': rec.get('primary_language', 'english'),
                    'top_strengths': rec.get('strengths', []),
                    'concerns': rec.get('concerns', []),
                    'why_recommended': rec.get('recommendation_reason', f"{rec['city']} is perfect for your UK profile.")
                }
                formatted_recommendations.append(formatted_rec)

            return {
                'status': 'success',
                'recommendations': formatted_recommendations,
                'total_cities_analyzed': len(self.cities_data['cities']),
                'algorithm_version': self.version,
                'filters_applied': {
                    'regional_preference': questionnaire_responses.get('uk_region_preference', 'any_region'),
                    'language_preference': questionnaire_responses.get('uk_language_preference', 'english_only')
                }
            }

        except Exception as e:
            logger.error(f"❌ Erreur get_recommendations UK: {e}")
            return {
                'status': 'error',
                'recommendations': [],
                'message': f'Erreur calcul recommandations UK: {str(e)}'
            }

# Fonction factory pour être utilisé dans main.py
def create_uk_residents_algorithm():
    """Factory pour créer l'instance de l'algorithme UK"""
    return UKResidentsAlgorithm('/var/www/Revolutionnary/platform/backend/data_v2/villes_uk_residents.json')
