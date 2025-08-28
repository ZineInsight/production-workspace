"""
🇲🇦 ALGO-MOROCCO-RESIDENTS.PY - ALGORITHME MATCHING VILLES MAROC
==================================================================
Algorithme ultra performant pour matcher Marocains/résidents avec leurs 3 villes idéales
Author: Revolutionary Team | Version: 1.0.0 - Morocco Domestic Matching
OBJECTIF: Recommandations précises basées sur 25 villes + 27 critères spécifiques Maroc
INCLUSIVITÉ: Algorithme neutre pour résidents ET expats potentiels
"""

import json
import logging
from typing import Dict, List, Tuple
from dataclasses import dataclass

# Configuration logging
logger = logging.getLogger(__name__)

@dataclass
class UserProfileMorocco:
    """Profil utilisateur Maroc avec pondérations spécifiquement marocaines"""
    region_preference: str          # any_region, atlantic_coast, mediterranean, imperial_cities, atlas_mountains, sahara_gateway
    environment_type: str           # major_metropolis, coastal_relaxed, mountain_nature, heritage_authentic, balanced_modern
    main_priority: str              # career_growth, cost_optimization, lifestyle_upgrade, family_focus, international_connections
    age_profile: str               # student_young, young_professional, established_professional, senior_mature
    monthly_budget: str            # budget_tight, budget_balanced, budget_comfortable, budget_premium
    cultural_priority: str         # modern_business, traditional_heritage, artistic_bohemian, cosmopolitan_mix
    activity_priority: str         # nature_sports, nightlife_social, family_education, culture_learning
    work_environment: str          # tech_startup, business_finance, government_public, tourism_services, traditional_commerce
    nature_priority: str           # beach_ocean, mountains_hiking, parks_gardens, urban_modern
    connections_priority: str      # international_europe, national_major, local_regional, minimal_connectivity
    authenticity_balance: str      # maximum_authentic, balanced_heritage, modern_comfort, international_standards
    climate_priority: str          # ocean_fresh, mountain_pure, desert_dry, climate_flexible
    health_safety: str            # healthcare_priority, safety_priority, balanced_wellbeing, risk_tolerant
    economic_dynamism: str        # high_growth, stable_established, emerging_potential, traditional_local
    criteria_weights: Dict[str, float]

class MoroccoResidentsAlgorithm:
    """🇲🇦 Algorithme de recommandation pour résidents Maroc"""

    def __init__(self, cities_data_path: str):
        """Initialise l'algorithme avec les données des 25 villes marocaines stratégiques"""
        self.version = "1.0.0"  # OBLIGATOIRE pour health check
        self.cities_data = self.load_cities_data(cities_data_path)
        self.criteria_weights_base = self.get_base_criteria_weights_morocco()

    def load_cities_data(self, data_path: str) -> Dict:
        """Charge les données des 25 villes marocaines"""
        try:
            with open(data_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            logger.info(f"🇲🇦 Données Maroc chargées: {len(data['cities'])} villes")
            return data
        except Exception as e:
            logger.error(f"❌ Erreur chargement données Maroc: {e}")
            return {"cities": [], "metadata": {}, "criteria_definitions": {}}

    def get_base_criteria_weights_morocco(self) -> Dict[str, float]:
        """Pondérations de base adaptées au marché et à la réalité marocaine"""
        return {
            # 💰 ÉCONOMIE (5 critères) - Priorité haute économie émergente
            'cost_of_living': 9.0,                    # Très important pouvoir d'achat
            'job_opportunities': 8.5,                 # Emploi crucial
            'salary_potential': 8.0,                  # Évolution salariale importante
            'housing_availability': 7.5,              # Logement accessible
            'public_transport': 6.5,                  # Infrastructure variable

            # 🏥 SANTÉ ET SÉCURITÉ (2 critères) - Priorité haute stabilité
            'healthcare_quality': 7.5,                # Soins médicaux importants
            'safety_security': 8.5,                   # Stabilité prioritaire Maroc

            # 🎓 ÉDUCATION ET FAMILLE (2 critères) - Très valorisé culture marocaine
            'education_quality': 8.0,                 # Éducation très valorisée
            'family_friendliness': 7.5,               # Structure familiale forte

            # 🎭 CULTURE ET LIFESTYLE (4 critères)
            'cultural_scene': 7.5,                    # Richesse culturelle
            'nightlife': 6.0,                         # Moins prioritaire culture locale
            'youth_scene': 6.5,                       # Dynamisme jeunes
            'sports_recreation': 6.5,                 # Activités loisirs

            # 🌍 CONNECTIVITÉ (2 critères) - Spécial position géographique Maroc
            'international_connectivity': 7.0,        # Business international
            'language_diversity': 6.5,                # Multilinguisme atout

            # 🌿 ENVIRONNEMENT (4 critères)
            'climate_quality': 7.0,                   # Climat méditerranéen/atlantique
            'air_quality': 7.0,                       # Qualité environnementale
            'nature_access': 6.5,                     # Espaces naturels
            'beach_access': 6.0,                      # Accès côtes
            'mountain_access': 6.0,                   # Accès Atlas/Rif

            # 💼 BUSINESS ET TECH (3 critères)
            'business_environment': 7.0,              # Écosystème économique
            'startup_ecosystem': 6.5,                 # Innovation émergente
            'tech_scene': 6.0,                        # Secteur tech en développement

            # 🇲🇦 CRITÈRES SPÉCIFIQUES MAROC (4 critères uniques)
            'european_proximity_advantage': 6.5,      # Position géostratégique unique
            'berber_culture_presence': 5.5,          # Patrimoine amazigh
            'french_language_usage': 6.0,            # Héritage francophone business
            'traditional_markets_souks': 6.5         # Authenticité et commerce traditionnel
        }

    def create_user_profile_morocco(self, questionnaire_responses: Dict) -> UserProfileMorocco:
        """🧠 Crée profil utilisateur marocain personnalisé à partir des réponses"""

        # Extraction réponses questionnaire Maroc
        region_preference = questionnaire_responses.get('morocco_region_preference', 'any_region')
        environment_type = questionnaire_responses.get('morocco_environment_type', 'balanced_modern')
        main_priority = questionnaire_responses.get('morocco_main_priority', 'career_growth')
        age_profile = questionnaire_responses.get('morocco_age_profile', 'young_professional')
        monthly_budget = questionnaire_responses.get('morocco_monthly_budget', 'budget_balanced')
        cultural_priority = questionnaire_responses.get('morocco_cultural_priority', 'cosmopolitan_mix')
        activity_priority = questionnaire_responses.get('morocco_activity_priority', 'culture_learning')
        work_environment = questionnaire_responses.get('morocco_work_environment', 'business_finance')
        nature_priority = questionnaire_responses.get('morocco_nature_priority', 'urban_modern')
        connections_priority = questionnaire_responses.get('morocco_connections_priority', 'national_major')
        authenticity_balance = questionnaire_responses.get('morocco_authenticity_balance', 'balanced_heritage')
        climate_priority = questionnaire_responses.get('morocco_climate_priority', 'climate_flexible')
        health_safety = questionnaire_responses.get('morocco_health_safety', 'balanced_wellbeing')
        economic_dynamism = questionnaire_responses.get('morocco_economic_dynamism', 'stable_established')

        # Initialiser pondérations de base
        weights = self.criteria_weights_base.copy()

        # === PRIORITÉ PRINCIPALE MAROC ===
        if main_priority == 'career_growth':
            weights['job_opportunities'] *= 1.8
            weights['salary_potential'] *= 1.6
            weights['business_environment'] *= 1.5
            weights['tech_scene'] *= 1.4
        elif main_priority == 'cost_optimization':
            weights['cost_of_living'] *= 1.9
            weights['housing_availability'] *= 1.7
        elif main_priority == 'lifestyle_upgrade':
            weights['climate_quality'] *= 1.6
            weights['cultural_scene'] *= 1.5
            weights['air_quality'] *= 1.4
        elif main_priority == 'family_focus':
            weights['family_friendliness'] *= 1.8
            weights['education_quality'] *= 1.7
            weights['safety_security'] *= 1.6
            weights['healthcare_quality'] *= 1.4
        elif main_priority == 'international_connections':
            weights['international_connectivity'] *= 1.8
            weights['european_proximity_advantage'] *= 1.6
            weights['language_diversity'] *= 1.4

        # === PROFIL D'ÂGE MAROC ===
        if age_profile == 'student_young':
            weights['cost_of_living'] *= 1.6
            weights['youth_scene'] *= 1.5
            weights['education_quality'] *= 1.4
            weights['nightlife'] *= 1.3
        elif age_profile == 'young_professional':
            weights['job_opportunities'] *= 1.4
            weights['salary_potential'] *= 1.3
            weights['nightlife'] *= 1.2
            weights['cultural_scene'] *= 1.2
        elif age_profile == 'established_professional':
            weights['business_environment'] *= 1.4
            weights['family_friendliness'] *= 1.3
            weights['healthcare_quality'] *= 1.2
        elif age_profile == 'senior_mature':
            weights['healthcare_quality'] *= 1.6
            weights['safety_security'] *= 1.5
            weights['climate_quality'] *= 1.3
            weights['air_quality'] *= 1.3

        # === BUDGET MENSUEL DH ===
        if monthly_budget == 'budget_tight':  # < 5000 DH
            weights['cost_of_living'] *= 1.8
            weights['housing_availability'] *= 1.6
        elif monthly_budget == 'budget_balanced':  # 5000-10000 DH
            weights['cost_of_living'] *= 1.3
            weights['housing_availability'] *= 1.2
        elif monthly_budget == 'budget_comfortable':  # 10000-20000 DH
            weights['cultural_scene'] *= 1.2
            weights['business_environment'] *= 1.2
        # budget_premium: pas de constraint coût

        # === PRIORITÉ CULTURELLE MAROC ===
        if cultural_priority == 'modern_business':
            weights['business_environment'] *= 1.6
            weights['tech_scene'] *= 1.4
            weights['international_connectivity'] *= 1.3
        elif cultural_priority == 'traditional_heritage':
            weights['traditional_markets_souks'] *= 1.7
            weights['berber_culture_presence'] *= 1.6
            weights['cultural_scene'] *= 1.4
        elif cultural_priority == 'artistic_bohemian':
            weights['cultural_scene'] *= 1.7
            weights['traditional_markets_souks'] *= 1.3
            weights['nightlife'] *= 1.2
        elif cultural_priority == 'cosmopolitan_mix':
            weights['language_diversity'] *= 1.5
            weights['international_connectivity'] *= 1.3
            weights['cultural_scene'] *= 1.2

        # === ENVIRONNEMENT DE TRAVAIL MAROC ===
        if work_environment == 'tech_startup':
            weights['tech_scene'] *= 1.8
            weights['startup_ecosystem'] *= 1.7
            weights['business_environment'] *= 1.4
        elif work_environment == 'business_finance':
            weights['business_environment'] *= 1.6
            weights['international_connectivity'] *= 1.4
            weights['salary_potential'] *= 1.3
        elif work_environment == 'government_public':
            weights['safety_security'] *= 1.4
            weights['healthcare_quality'] *= 1.3
            weights['education_quality'] *= 1.2
        elif work_environment == 'tourism_services':
            weights['cultural_scene'] *= 1.5
            weights['traditional_markets_souks'] *= 1.4
            weights['beach_access'] *= 1.3
        elif work_environment == 'traditional_commerce':
            weights['traditional_markets_souks'] *= 1.6
            weights['cost_of_living'] *= 1.3
            weights['business_environment'] *= 1.2

        # === PRIORITÉ NATURE MAROC ===
        if nature_priority == 'beach_ocean':
            weights['beach_access'] *= 1.8
            weights['climate_quality'] *= 1.4
            weights['air_quality'] *= 1.3
        elif nature_priority == 'mountains_hiking':
            weights['mountain_access'] *= 1.8
            weights['air_quality'] *= 1.5
            weights['nature_access'] *= 1.4
        elif nature_priority == 'parks_gardens':
            weights['nature_access'] *= 1.6
            weights['family_friendliness'] *= 1.3
            weights['air_quality'] *= 1.2
        # urban_modern: pas de boost nature

        # === CONNEXIONS PRIORITAIRES MAROC ===
        if connections_priority == 'international_europe':
            weights['international_connectivity'] *= 1.7
            weights['european_proximity_advantage'] *= 1.8
            weights['french_language_usage'] *= 1.3
        elif connections_priority == 'national_major':
            weights['public_transport'] *= 1.4
            weights['business_environment'] *= 1.2
        elif connections_priority == 'local_regional':
            weights['public_transport'] *= 1.3
            weights['traditional_markets_souks'] *= 1.2

        # === ÉQUILIBRE AUTHENTICITÉ MAROC ===
        if authenticity_balance == 'maximum_authentic':
            weights['traditional_markets_souks'] *= 1.7
            weights['berber_culture_presence'] *= 1.6
            weights['cultural_scene'] *= 1.3
        elif authenticity_balance == 'balanced_heritage':
            weights['cultural_scene'] *= 1.3
            weights['traditional_markets_souks'] *= 1.2
            weights['business_environment'] *= 1.2
        elif authenticity_balance == 'modern_comfort':
            weights['business_environment'] *= 1.4
            weights['tech_scene'] *= 1.3
            weights['international_connectivity'] *= 1.2
        elif authenticity_balance == 'international_standards':
            weights['international_connectivity'] *= 1.5
            weights['european_proximity_advantage'] *= 1.4
            weights['tech_scene'] *= 1.3

        # === CLIMAT PRIORITAIRE MAROC ===
        if climate_priority == 'ocean_fresh':
            weights['beach_access'] *= 1.4
            weights['climate_quality'] *= 1.3
        elif climate_priority == 'mountain_pure':
            weights['mountain_access'] *= 1.5
            weights['air_quality'] *= 1.4
        elif climate_priority == 'desert_dry':
            weights['nature_access'] *= 1.3
            weights['air_quality'] *= 1.2

        # === SANTÉ ET SÉCURITÉ MAROC ===
        if health_safety == 'healthcare_priority':
            weights['healthcare_quality'] *= 1.7
            weights['safety_security'] *= 1.3
        elif health_safety == 'safety_priority':
            weights['safety_security'] *= 1.8
            weights['family_friendliness'] *= 1.3
        elif health_safety == 'balanced_wellbeing':
            weights['healthcare_quality'] *= 1.2
            weights['safety_security'] *= 1.2

        # === DYNAMISME ÉCONOMIQUE MAROC ===
        if economic_dynamism == 'high_growth':
            weights['startup_ecosystem'] *= 1.6
            weights['tech_scene'] *= 1.5
            weights['job_opportunities'] *= 1.4
        elif economic_dynamism == 'stable_established':
            weights['business_environment'] *= 1.4
            weights['salary_potential'] *= 1.2
        elif economic_dynamism == 'emerging_potential':
            weights['job_opportunities'] *= 1.3
            weights['business_environment'] *= 1.2
        elif economic_dynamism == 'traditional_local':
            weights['traditional_markets_souks'] *= 1.4
            weights['cost_of_living'] *= 1.3

        return UserProfileMorocco(
            region_preference=region_preference,
            environment_type=environment_type,
            main_priority=main_priority,
            age_profile=age_profile,
            monthly_budget=monthly_budget,
            cultural_priority=cultural_priority,
            activity_priority=activity_priority,
            work_environment=work_environment,
            nature_priority=nature_priority,
            connections_priority=connections_priority,
            authenticity_balance=authenticity_balance,
            climate_priority=climate_priority,
            health_safety=health_safety,
            economic_dynamism=economic_dynamism,
            criteria_weights=weights
        )

    def apply_regional_filters(self, cities_list: List[Dict], user_profile: UserProfileMorocco) -> List[Dict]:
        """🗺️ Applique filtres régionaux AVANT scoring pour performance optimisée x3"""

        if user_profile.region_preference == 'any_region':
            return cities_list

        # Mapping régions Maroc → régions administratives JSON
        region_mapping = {
            'atlantic_coast': ['Grand Casablanca-Settat', 'Rabat-Salé-Kénitra', 'Souss-Massa'],
            'mediterranean': ['Tanger-Tétouan-Al Hoceïma', 'Oriental'],
            'imperial_cities': ['Fès-Meknès', 'Marrakech-Safi'],
            'atlas_mountains': ['Béni Mellal-Khénifra', 'Fès-Meknès'],  # Ifrane, Khénifra, Chefchaouen
            'sahara_gateway': ['Drâa-Tafilalet', 'Laâyoune-Sakia El Hamra']
        }

        target_regions = region_mapping.get(user_profile.region_preference, [])
        if not target_regions:
            return cities_list

        filtered_cities = [
            city for city in cities_list
            if city.get('region', '') in target_regions
        ]

        logger.info(f"🗺️ Filtre régional Maroc {user_profile.region_preference}: {len(filtered_cities)} villes gardées sur {len(cities_list)}")
        return filtered_cities

    def calculate_city_score_morocco(self, city_data: Dict, user_profile: UserProfileMorocco) -> float:
        """🧮 Calcule score pondéré d'une ville marocaine selon profil utilisateur"""

        city_scores = city_data.get('scores', {})
        criteria_weights = user_profile.criteria_weights

        total_weighted_score = 0.0
        total_weight = 0.0

        # Parcourir tous les critères et calculer score pondéré
        for criterion, weight in criteria_weights.items():
            if criterion in city_scores:
                score = city_scores[criterion]
                weighted_score = score * weight
                total_weighted_score += weighted_score
                total_weight += weight

        # Normaliser le score final
        if total_weight > 0:
            final_score = total_weighted_score / total_weight
        else:
            final_score = 0.0

        # Assurer score entre 0.0 et 1.0
        final_score = max(0.0, min(1.0, final_score))

        return final_score

    def apply_morocco_bonuses(self, city_data: Dict, base_score: float, user_profile: UserProfileMorocco) -> float:
        """🎯 Applique bonus/malus spécifiques à la réalité marocaine"""

        bonus_score = base_score
        city_scores = city_data.get('scores', {})
        city_name = city_data.get('name', '')
        city_id = city_data.get('id', '')

        # === BONUS SPÉCIFIQUES MAROC ===

        # Bonus Business International + Casablanca/Tanger
        if (user_profile.main_priority == 'international_connections' and
            city_id in ['casablanca', 'tangier'] and
            city_scores.get('international_connectivity', 0) > 0.85):
            bonus_score *= 1.3
            logger.debug(f"🌍 Bonus business international Maroc: {city_name}")

        # Bonus Culture Traditionnelle + Villes Impériales
        if (user_profile.cultural_priority == 'traditional_heritage' and
            city_id in ['marrakech', 'fes', 'meknes'] and
            city_scores.get('traditional_markets_souks', 0) > 0.85):
            bonus_score *= 1.4
            logger.debug(f"🕌 Bonus patrimoine traditionnel Maroc: {city_name}")

        # Bonus Plage + Villes Côtières
        if (user_profile.nature_priority == 'beach_ocean' and
            city_scores.get('beach_access', 0) > 0.8):
            bonus_score *= 1.3
            logger.debug(f"🏖️ Bonus accès plage Maroc: {city_name}")

        # Bonus Montagne + Villes Atlas/Rif
        if (user_profile.nature_priority == 'mountains_hiking' and
            city_id in ['ifrane', 'chefchaouen', 'beni_mellal'] and
            city_scores.get('mountain_access', 0) > 0.8):
            bonus_score *= 1.4
            logger.debug(f"🏔️ Bonus accès montagne Maroc: {city_name}")

        # Bonus Tech/Startup + Casablanca/Rabat
        if (user_profile.work_environment == 'tech_startup' and
            city_id in ['casablanca', 'rabat'] and
            city_scores.get('tech_scene', 0) > 0.7):
            bonus_score *= 1.2
            logger.debug(f"💻 Bonus tech scene Maroc: {city_name}")

        # Bonus Éducation + Ifrane/Rabat/Fès
        if (user_profile.main_priority == 'family_focus' and
            city_id in ['ifrane', 'rabat', 'fes'] and
            city_scores.get('education_quality', 0) > 0.85):
            bonus_score *= 1.3
            logger.debug(f"🎓 Bonus éducation excellence Maroc: {city_name}")

        # === MALUS RÉALISTES MAROC ===

        # Malus budget serré + Casablanca (coût vie élevé)
        if (user_profile.monthly_budget == 'budget_tight' and
            city_id == 'casablanca' and
            city_scores.get('cost_of_living', 1.0) < 0.7):
            bonus_score *= 0.7
            logger.debug(f"💸 Malus budget serré Casablanca: {city_name}")

        # Malus montagne souhaitée + villes sans accès montagne
        if (user_profile.nature_priority == 'mountains_hiking' and
            city_scores.get('mountain_access', 1.0) < 0.4):
            bonus_score *= 0.6
            logger.debug(f"⛰️ Malus pas d'accès montagne: {city_name}")

        # Malus plage souhaitée + villes intérieures
        if (user_profile.nature_priority == 'beach_ocean' and
            city_scores.get('beach_access', 1.0) < 0.3):
            bonus_score *= 0.6
            logger.debug(f"🚫 Malus pas d'accès plage: {city_name}")

        # Malus connexions Europe + villes Sud/intérieur
        if (user_profile.connections_priority == 'international_europe' and
            city_scores.get('european_proximity_advantage', 1.0) < 0.5):
            bonus_score *= 0.8
            logger.debug(f"🇪🇺 Malus éloignement Europe: {city_name}")

        return min(bonus_score, 1.0)  # Cap à 1.0

    def get_city_strengths_morocco(self, city_data: Dict, user_profile: UserProfileMorocco) -> List[str]:
        """💪 Identifie les forces principales d'une ville marocaine"""

        strengths = []
        scores = city_data['scores']
        city_name = city_data['name']

        # Forces basées sur scores élevés et spécificités Maroc
        if scores.get('cost_of_living', 0) > 0.75:
            strengths.append("Coût de la vie abordable")
        if scores.get('job_opportunities', 0) > 0.8:
            strengths.append("Marché du travail dynamique")
        if scores.get('safety_security', 0) > 0.85:
            strengths.append("Excellente sécurité")
        if scores.get('cultural_scene', 0) > 0.85:
            strengths.append("Richesse culturelle exceptionnelle")
        if scores.get('beach_access', 0) > 0.85:
            strengths.append("Accès plages de qualité")
        if scores.get('mountain_access', 0) > 0.85:
            strengths.append("Proximité montagne Atlas/Rif")
        if scores.get('international_connectivity', 0) > 0.8:
            strengths.append("Connectivité internationale")
        if scores.get('european_proximity_advantage', 0) > 0.8:
            strengths.append("Proximité stratégique Europe")
        if scores.get('traditional_markets_souks', 0) > 0.85:
            strengths.append("Souks authentiques et vivants")
        if scores.get('berber_culture_presence', 0) > 0.8:
            strengths.append("Riche patrimoine amazigh")
        if scores.get('education_quality', 0) > 0.85:
            strengths.append("Excellence éducative")
        if scores.get('healthcare_quality', 0) > 0.8:
            strengths.append("Qualité des soins médicaux")

        return strengths[:4]  # Max 4 forces principales

    def get_city_concerns_morocco(self, city_data: Dict, user_profile: UserProfileMorocco) -> List[str]:
        """⚠️ Identifie les défis potentiels d'une ville marocaine"""

        concerns = []
        scores = city_data['scores']

        # Préoccupations basées sur scores faibles
        if scores.get('cost_of_living', 1.0) < 0.6:
            concerns.append("Coût de la vie élevé")
        if scores.get('air_quality', 1.0) < 0.7:
            concerns.append("Qualité de l'air à surveiller")
        if scores.get('public_transport', 1.0) < 0.6:
            concerns.append("Transport public limité")
        if scores.get('job_opportunities', 1.0) < 0.6:
            concerns.append("Marché du travail restreint")
        if scores.get('tech_scene', 1.0) < 0.5:
            concerns.append("Écosystème tech peu développé")
        if scores.get('nightlife', 1.0) < 0.6:
            concerns.append("Vie nocturne limitée")

        return concerns[:3]  # Max 3 préoccupations

    def generate_recommendation_reason_morocco(self, city_data: Dict, user_profile: UserProfileMorocco) -> str:
        """✨ Génère raison personnalisée pour recommandation ville marocaine"""

        city_name = city_data['name']
        scores = city_data['scores']

        reasons = []

        # Raisons basées sur priorité principale
        if user_profile.main_priority == 'career_growth':
            if scores.get('job_opportunities', 0) > 0.8:
                reasons.append(f"marché du travail très dynamique")
        elif user_profile.main_priority == 'international_connections':
            if scores.get('international_connectivity', 0) > 0.8:
                reasons.append(f"excellente connectivité internationale")
        elif user_profile.main_priority == 'family_focus':
            if scores.get('family_friendliness', 0) > 0.8:
                reasons.append(f"environnement très favorable aux familles")
        elif user_profile.main_priority == 'cost_optimization':
            if scores.get('cost_of_living', 0) > 0.75:
                reasons.append(f"coût de la vie très abordable")

        # Raisons spécifiques Maroc
        if scores.get('traditional_markets_souks', 0) > 0.85:
            reasons.append(f"souks authentiques exceptionnels")
        if scores.get('beach_access', 0) > 0.85:
            reasons.append(f"accès privilégié aux plages")
        if scores.get('mountain_access', 0) > 0.85:
            reasons.append(f"proximité montagnes Atlas/Rif")
        if scores.get('berber_culture_presence', 0) > 0.8:
            reasons.append(f"riche patrimoine amazigh")

        if reasons:
            return f"{city_name} vous convient parfaitement pour son {', '.join(reasons[:2])}."
        else:
            return f"{city_name} offre un excellent équilibre pour votre profil marocain."

    def get_recommendations(self, questionnaire_responses: Dict, top_n: int = 3) -> Dict:
        """🏆 Interface standardisée pour main.py - Retourne top N recommandations villes Maroc"""

        try:
            # Créer profil utilisateur Maroc
            user_profile = self.create_user_profile_morocco(questionnaire_responses)
            logger.info(f"🇲🇦 Profil Maroc créé: {user_profile.main_priority}, {user_profile.age_profile}")
            logger.info(f"🗺️ Filtre régional: {user_profile.region_preference}")

            # ÉTAPE 1: Appliquer filtre régional (performance x3)
            all_cities = self.cities_data.get('cities', [])
            filtered_cities = self.apply_regional_filters(all_cities, user_profile)

            if len(filtered_cities) == 0:
                logger.warning("❌ Aucune ville ne correspond au filtre régional Maroc")
                return {
                    'status': 'error',
                    'recommendations': [],
                    'message': 'Aucune ville trouvée pour vos critères régionaux'
                }

            # ÉTAPE 2: Calculer scores pour villes filtrées
            city_scores = []
            for city in filtered_cities:
                # Score de base pondéré
                base_score = self.calculate_city_score_morocco(city, user_profile)

                # Appliquer bonus/malus Maroc
                final_score = self.apply_morocco_bonuses(city, base_score, user_profile)

                city_scores.append({
                    'city_data': city,
                    'score': final_score
                })

            # Trier par score décroissant
            city_scores.sort(key=lambda x: x['score'], reverse=True)

            # ÉTAPE 3: Générer recommandations finales format standardisé
            recommendations = []
            for i, city_score in enumerate(city_scores[:top_n]):
                city_data = city_score['city_data']
                score = city_score['score']

                recommendation = {
                    'city': city_data['name'],
                    'region': city_data['region'],
                    'score_percentage': round(score * 100, 1),
                    'population': city_data.get('population', 'N/A'),
                    'coordinates': city_data.get('coordinates', []),
                    'economic_zone': city_data.get('economic_zone', 'general'),
                    'strengths': self.get_city_strengths_morocco(city_data, user_profile),
                    'concerns': self.get_city_concerns_morocco(city_data, user_profile),
                    'why_recommended': self.generate_recommendation_reason_morocco(city_data, user_profile),
                    'rank': i + 1
                }
                recommendations.append(recommendation)

            logger.info(f"🏆 Top {len(recommendations)} recommandations Maroc générées (sur {len(filtered_cities)} villes filtrées)")

            return {
                'status': 'success',
                'recommendations': recommendations,
                'total_cities_analyzed': len(filtered_cities),
                'algorithm_version': self.version,
                'filters_applied': {
                    'regional_preference': user_profile.region_preference,
                    'main_priority': user_profile.main_priority,
                    'budget_range': user_profile.monthly_budget
                }
            }

        except Exception as e:
            logger.error(f"❌ Erreur get_recommendations Maroc: {e}")
            return {
                'status': 'error',
                'recommendations': [],
                'message': f'Erreur calcul recommandations Maroc: {str(e)}'
            }

# Fonction factory pour main.py
def create_morocco_residents_algorithm():
    """Factory pour créer l'instance de l'algorithme Maroc"""
    return MoroccoResidentsAlgorithm('/var/www/Revolutionnary/platform/backend/data_v2/villes_morocco_residents.json')
