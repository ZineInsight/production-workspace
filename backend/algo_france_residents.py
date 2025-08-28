"""
🇫🇷 ALGO-FRANCE-RESIDENTS.PY - ALGORITHME MATCHING VILLES FRANCE
================================================================
Algorithme ultra performant pour matcher Français avec leurs 3 villes idéales
Author: Revolutionary Team | Version: 1.0.0 - France Domestic Matching
OBJECTIF: Recommandations précises basées sur profils français et priorités culturelles
"""

import json
import math
from typing import Dict, List, Tuple
from dataclasses import dataclass
import logging

# Configuration logging
logger = logging.getLogger(__name__)

@dataclass
class UserProfileFrance:
    """Profil utilisateur France avec pondérations spécifiquement françaises"""
    main_priority: str           # career_growth, cost_optimization, lifestyle_upgrade, family_focus
    age_profile: str            # student_young, young_active, established_active, senior_comfort
    monthly_budget: str         # budget_tight, budget_balanced, budget_comfortable, budget_premium
    work_situation: str         # stable_cdi, job_search, full_remote, freelance_independent
    housing_preference: str     # downtown_apartment, suburban_house, transport_connected, budget_priority
    transport_preference: str   # walk_bike_priority, public_transport_fan, car_essential, multimodal_flexible
    climate_preference: str     # mediterranean_sun, four_seasons, oceanic_mild, climate_adaptable
    social_scene: str          # gastronomy_culture, cultural_events, nightlife_dynamic, quiet_homebody
    family_situation: str      # single_no_children, couple_no_children, young_children, teen_students
    deal_breaker: str         # cost_too_high, depressing_climate, no_job_opportunities, pollution_degraded
    criteria_weights: Dict[str, float]

class FranceResidentsAlgorithm:
    """🎯 Algorithme de matching ultra sophistiqué pour résidents France"""

    def __init__(self, cities_data_path: str):
        """Initialise l'algorithme avec les données des 50 villes françaises"""
        self.cities_data = self.load_cities_data(cities_data_path)
        self.criteria_weights_base = self.get_base_criteria_weights_france()

    def load_cities_data(self, data_path: str) -> Dict:
        """Charge les données des 50 villes françaises"""
        with open(data_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def get_base_criteria_weights_france(self) -> Dict[str, float]:
        """Poids de base adaptés au marché et à la mentalité française"""
        return {
            # Critères financiers (moins critique qu'USA grâce système social)
            "cost_of_living": 1.0,
            "housing_affordability": 1.0,
            "income_tax_burden": 0.6,      # Moins prioritaire qu'aux USA
            "local_tax": 0.5,
            "property_tax": 0.5,

            # Critères climatiques (importance culturelle française)
            "climate_rating": 1.1,         # Plus important qu'aux USA
            "weather_consistency": 0.8,

            # Critères professionnels (adaptation marché français)
            "job_market": 0.9,
            "tech_industry": 0.7,          # Moins central qu'aux USA
            "remote_work_friendly": 0.6,

            # Critères urbains/transport (priorité française transport public)
            "urban_density": 0.7,
            "suburb_quality": 0.8,
            "public_transport": 0.9,       # Plus important qu'aux USA
            "walkability": 0.8,
            "car_dependency": 0.8,         # Inversé : moins de voiture = mieux

            # Critères éducation/famille (système français)
            "school_quality": 0.9,
            "university_access": 0.7,

            # Critères risques (spécificités françaises)
            "natural_disaster_risk": 0.7,
            "flood_risk": 0.6,             # Remplace hurricane_risk
            "heat_wave_risk": 0.7,         # Remplace earthquake_risk

            # Critères santé (système de santé français)
            "healthcare_access": 0.7,      # Moins critique (sécurité sociale)
            "hospital_quality": 0.6,

            # Critères culturels (ADN français fort)
            "cultural_scene": 0.9,         # Plus important qu'aux USA
            "restaurant_diversity": 0.8,   # Gastronomie = priorité française
            "nightlife": 0.6
        }

    def create_user_profile_france(self, questionnaire_responses: Dict) -> UserProfileFrance:
        """🧠 Crée profil utilisateur français personnalisé à partir des réponses"""

        # Extraction des réponses spécifiques France
        main_priority = questionnaire_responses.get('france_main_priority')
        age_profile = questionnaire_responses.get('france_age_profile')
        monthly_budget = questionnaire_responses.get('france_monthly_budget')
        work_situation = questionnaire_responses.get('france_work_situation')
        housing_preference = questionnaire_responses.get('france_housing_preference')
        transport_preference = questionnaire_responses.get('france_transport_preference')
        climate_preference = questionnaire_responses.get('france_climate_preference')
        social_scene = questionnaire_responses.get('france_social_scene')
        family_situation = questionnaire_responses.get('france_family_situation')
        deal_breaker = questionnaire_responses.get('france_deal_breaker')

        # 🎯 CALCUL PONDÉRATIONS PERSONNALISÉES FRANCE
        weights = self.criteria_weights_base.copy()

        # === BOOST PRIORITÉ PRINCIPALE ===
        if main_priority == 'career_growth':
            weights['job_market'] *= 2.0
            weights['tech_industry'] *= 1.8
            weights['university_access'] *= 1.5
            weights['cultural_scene'] *= 1.3  # Networking culturel français
        elif main_priority == 'cost_optimization':
            weights['cost_of_living'] *= 2.2
            weights['housing_affordability'] *= 2.0
            weights['public_transport'] *= 1.5  # Économie transport
            weights['income_tax_burden'] *= 1.4
        elif main_priority == 'lifestyle_upgrade':
            weights['climate_rating'] *= 1.9
            weights['cultural_scene'] *= 1.8
            weights['restaurant_diversity'] *= 1.6
            weights['walkability'] *= 1.3
        elif main_priority == 'family_focus':
            weights['school_quality'] *= 2.1
            weights['suburb_quality'] *= 1.9
            weights['healthcare_access'] *= 1.6
            weights['natural_disaster_risk'] *= 1.5

        # === ADAPTATION PROFIL ÂGE ===
        if age_profile == 'student_young':
            weights['cost_of_living'] *= 1.8
            weights['university_access'] *= 1.7
            weights['public_transport'] *= 1.5
            weights['nightlife'] *= 1.4
        elif age_profile == 'young_active':
            weights['job_market'] *= 1.6
            weights['cultural_scene'] *= 1.5
            weights['nightlife'] *= 1.3
            weights['tech_industry'] *= 1.4
        elif age_profile == 'established_active':
            weights['school_quality'] *= 1.6
            weights['suburb_quality'] *= 1.5
            weights['healthcare_access'] *= 1.3
            weights['property_tax'] *= 1.2
        elif age_profile == 'senior_comfort':
            weights['healthcare_access'] *= 1.8
            weights['climate_rating'] *= 1.6
            weights['cultural_scene'] *= 1.4
            weights['walkability'] *= 1.3

        # === ADAPTATION BUDGET EUROS ===
        if monthly_budget == 'budget_tight':  # < 1500€
            weights['cost_of_living'] *= 1.9
            weights['housing_affordability'] *= 1.8
            weights['public_transport'] *= 1.6
        elif monthly_budget == 'budget_balanced':  # 1500-2500€
            weights['cost_of_living'] *= 1.3
            weights['job_market'] *= 1.2
            weights['public_transport'] *= 1.2
        elif monthly_budget == 'budget_comfortable':  # 2500-4000€
            weights['cultural_scene'] *= 1.4
            weights['restaurant_diversity'] *= 1.3
            weights['school_quality'] *= 1.2
        elif monthly_budget == 'budget_premium':  # > 4000€
            weights['cultural_scene'] *= 1.5
            weights['restaurant_diversity'] *= 1.4
            weights['suburb_quality'] *= 1.3

        # === SITUATION PROFESSIONNELLE FRANÇAISE ===
        if work_situation == 'stable_cdi':
            weights['cost_of_living'] *= 1.4
            weights['climate_rating'] *= 1.3
            weights['cultural_scene'] *= 1.2
        elif work_situation == 'job_search':
            weights['job_market'] *= 1.9
            weights['tech_industry'] *= 1.6
            weights['university_access'] *= 1.3
        elif work_situation == 'full_remote':
            weights['cost_of_living'] *= 1.6
            weights['climate_rating'] *= 1.5
            weights['cultural_scene'] *= 1.3
        elif work_situation == 'freelance_independent':
            weights['tech_industry'] *= 1.5
            weights['cultural_scene'] *= 1.4
            weights['restaurant_diversity'] *= 1.2

        # === PRÉFÉRENCE LOGEMENT ===
        if housing_preference == 'downtown_apartment':
            weights['urban_density'] *= 1.7
            weights['walkability'] *= 1.6
            weights['cultural_scene'] *= 1.4
            weights['public_transport'] *= 1.3
        elif housing_preference == 'suburban_house':
            weights['suburb_quality'] *= 1.8
            weights['school_quality'] *= 1.5
            weights['car_dependency'] *= 1.2
        elif housing_preference == 'transport_connected':
            weights['public_transport'] *= 1.8
            weights['walkability'] *= 1.4
            weights['suburb_quality'] *= 1.3
        elif housing_preference == 'budget_priority':
            weights['housing_affordability'] *= 1.9
            weights['cost_of_living'] *= 1.6
            weights['public_transport'] *= 1.4

        # === TRANSPORT FRANÇAIS ===
        if transport_preference == 'walk_bike_priority':
            weights['walkability'] *= 1.9
            weights['urban_density'] *= 1.6
            weights['public_transport'] *= 1.4
            weights['car_dependency'] *= 1.8  # Inversé
        elif transport_preference == 'public_transport_fan':
            weights['public_transport'] *= 1.8
            weights['urban_density'] *= 1.4
            weights['walkability'] *= 1.3
        elif transport_preference == 'car_essential':
            weights['suburb_quality'] *= 1.4
            weights['car_dependency'] *= 0.6  # Paradoxal : besoin voiture mais ville doit le permettre
        elif transport_preference == 'multimodal_flexible':
            weights['public_transport'] *= 1.3
            weights['walkability'] *= 1.2
            weights['car_dependency'] *= 1.1

        # === CLIMAT FRANÇAIS ===
        if climate_preference == 'mediterranean_sun':
            weights['climate_rating'] *= 1.8
            weights['weather_consistency'] *= 1.5
            weights['heat_wave_risk'] *= 1.2
        elif climate_preference == 'four_seasons':
            weights['weather_consistency'] *= 1.4
            weights['natural_disaster_risk'] *= 1.2
        elif climate_preference == 'oceanic_mild':
            weights['climate_rating'] *= 1.4
            weights['natural_disaster_risk'] *= 1.3
            weights['heat_wave_risk'] *= 1.4

        # === SCÈNE SOCIALE FRANÇAISE ===
        if social_scene == 'gastronomy_culture':
            weights['restaurant_diversity'] *= 1.7
            weights['cultural_scene'] *= 1.4
        elif social_scene == 'cultural_events':
            weights['cultural_scene'] *= 1.8
            weights['university_access'] *= 1.3
        elif social_scene == 'nightlife_dynamic':
            weights['nightlife'] *= 1.8
            weights['urban_density'] *= 1.4
            weights['cultural_scene'] *= 1.3
        elif social_scene == 'quiet_homebody':
            weights['suburb_quality'] *= 1.5
            weights['natural_disaster_risk'] *= 1.3
            weights['cost_of_living'] *= 1.2

        # === SITUATION FAMILIALE ===
        if family_situation == 'single_no_children':
            weights['cost_of_living'] *= 1.3
            weights['nightlife'] *= 1.4
            weights['cultural_scene'] *= 1.3
        elif family_situation == 'couple_no_children':
            weights['cultural_scene'] *= 1.4
            weights['restaurant_diversity'] *= 1.3
            weights['climate_rating'] *= 1.2
        elif family_situation == 'young_children':
            weights['school_quality'] *= 1.9
            weights['suburb_quality'] *= 1.6
            weights['healthcare_access'] *= 1.4
            weights['natural_disaster_risk'] *= 1.3
        elif family_situation == 'teen_students':
            weights['school_quality'] *= 1.7
            weights['university_access'] *= 1.5
            weights['public_transport'] *= 1.3
            weights['cultural_scene'] *= 1.2

        return UserProfileFrance(
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

    def calculate_city_score_france(self, city_data: Dict, user_profile: UserProfileFrance) -> float:
        """🧮 Calcule le score total d'une ville française pour un profil utilisateur"""

        total_score = 0.0
        total_weight = 0.0

        for criterion, city_value in city_data['scores'].items():
            if criterion in user_profile.criteria_weights:
                weight = user_profile.criteria_weights[criterion]

                # Score pondéré pour ce critère
                criterion_score = city_value * weight
                total_score += criterion_score
                total_weight += weight

        # Score normalisé (0.0 à 1.0)
        normalized_score = total_score / total_weight if total_weight > 0 else 0.0

        return normalized_score

    def apply_france_bonuses(self, city_data: Dict, base_score: float, user_profile: UserProfileFrance) -> float:
        """🚀 Applique des bonus/malus spécifiquement français"""

        bonus_score = base_score
        city_scores = city_data['scores']

        # === BONUS SYNERGIES FRANÇAISES ===

        # Bonus "Perfection Parisienne" (tech + culture + transport)
        if (city_scores.get('tech_industry', 0) > 0.8 and
            city_scores.get('cultural_scene', 0) > 0.9 and
            city_scores.get('public_transport', 0) > 0.9 and
            user_profile.main_priority == 'career_growth'):
            bonus_score *= 1.18

        # Bonus "Méditerranéen Idéal" (climat + culture + coût)
        if (city_scores.get('climate_rating', 0) > 0.8 and
            city_scores.get('cultural_scene', 0) > 0.7 and
            city_scores.get('cost_of_living', 0) > 0.6 and
            user_profile.climate_preference == 'mediterranean_sun'):
            bonus_score *= 1.15

        # Bonus "Famille Équilibrée" (écoles + banlieue + santé + transport)
        if (city_scores.get('school_quality', 0) > 0.8 and
            city_scores.get('suburb_quality', 0) > 0.7 and
            city_scores.get('healthcare_access', 0) > 0.8 and
            city_scores.get('public_transport', 0) > 0.7 and
            user_profile.family_situation in ['young_children', 'teen_students']):
            bonus_score *= 1.14

        # Bonus "Gastronome Culturel" (restaurants + culture + qualité)
        if (city_scores.get('restaurant_diversity', 0) > 0.8 and
            city_scores.get('cultural_scene', 0) > 0.8 and
            user_profile.social_scene == 'gastronomy_culture'):
            bonus_score *= 1.12

        # Bonus "Étudiant Optimisé" (coût + université + transport + vie)
        if (city_scores.get('cost_of_living', 0) > 0.7 and
            city_scores.get('university_access', 0) > 0.8 and
            city_scores.get('public_transport', 0) > 0.7 and
            city_scores.get('nightlife', 0) > 0.6 and
            user_profile.age_profile == 'student_young'):
            bonus_score *= 1.13

        # === MALUS DEAL-BREAKERS FRANÇAIS ===

        # Malus budget serré + ville chère
        if (user_profile.monthly_budget == 'budget_tight' and
            city_scores.get('cost_of_living', 1.0) < 0.5):
            bonus_score *= 0.80

        # Malus climat priorité + climat difficile
        if (user_profile.deal_breaker == 'depressing_climate' and
            city_scores.get('climate_rating', 1.0) < 0.5):
            bonus_score *= 0.75

        # Malus recherche emploi + marché faible
        if (user_profile.work_situation == 'job_search' and
            city_scores.get('job_market', 1.0) < 0.6):
            bonus_score *= 0.85

        # Malus famille + écoles moyennes
        if (user_profile.family_situation in ['young_children', 'teen_students'] and
            city_scores.get('school_quality', 1.0) < 0.6):
            bonus_score *= 0.87

        # Malus transport public priorité + transport faible
        if (user_profile.transport_preference in ['walk_bike_priority', 'public_transport_fan'] and
            city_scores.get('public_transport', 1.0) < 0.5):
            bonus_score *= 0.90

        return min(bonus_score, 1.0)  # Cap à 1.0

    def get_top_recommendations_france(self, questionnaire_responses: Dict, top_n: int = 3) -> List[Dict]:
        """🏆 Retourne le TOP N des villes françaises recommandées"""

        # Créer profil utilisateur français
        user_profile = self.create_user_profile_france(questionnaire_responses)

        city_scores = []

        # Calculer score pour chaque ville française
        for city in self.cities_data['cities']:
            base_score = self.calculate_city_score_france(city, user_profile)
            final_score = self.apply_france_bonuses(city, base_score, user_profile)

            city_scores.append({
                'city_data': city,
                'base_score': base_score,
                'final_score': final_score,
                'score_percentage': round(final_score * 100, 1)
            })

        # Trier par score final
        city_scores.sort(key=lambda x: x['final_score'], reverse=True)

        # Retourner TOP N avec informations détaillées
        top_recommendations = []
        for i, city_score in enumerate(city_scores[:top_n]):
            recommendation = {
                'rank': i + 1,
                'city': city_score['city_data']['name'],
                'region': city_score['city_data']['region'],
                'score_percentage': city_score['score_percentage'],
                'population': city_score['city_data']['population'],
                'coordinates': city_score['city_data']['coordinates'],
                'top_strengths': self.get_city_strengths_france(city_score['city_data'], user_profile),
                'potential_concerns': self.get_city_concerns_france(city_score['city_data'], user_profile),
                'why_recommended': self.generate_recommendation_reason_france(city_score['city_data'], user_profile)
            }
            top_recommendations.append(recommendation)

        return top_recommendations

    def get_city_strengths_france(self, city_data: Dict, user_profile: UserProfileFrance) -> List[str]:
        """💪 Identifie les points forts d'une ville française pour ce profil"""
        strengths = []
        scores = city_data['scores']
        weights = user_profile.criteria_weights

        # Trouve les critères avec meilleur score ET importance pour l'utilisateur
        weighted_criteria = []
        for criterion, score in scores.items():
            if criterion in weights:
                weighted_importance = score * weights[criterion]
                weighted_criteria.append((criterion, score, weighted_importance))

        # Top 3 critères pondérés
        top_criteria = sorted(weighted_criteria, key=lambda x: x[2], reverse=True)[:3]

        for criterion, score, _ in top_criteria:
            if score > 0.8:  # Seulement les vraiment excellents
                strength_text = self.get_criterion_description_france(criterion, score)
                strengths.append(strength_text)

        return strengths[:3]  # Max 3 points forts

    def get_city_concerns_france(self, city_data: Dict, user_profile: UserProfileFrance) -> List[str]:
        """⚠️ Identifie les points d'attention d'une ville française pour ce profil"""
        concerns = []
        scores = city_data['scores']
        weights = user_profile.criteria_weights

        # Critères importants pour l'utilisateur mais faibles pour la ville
        for criterion, weight in weights.items():
            if weight > 1.2 and criterion in scores:  # Critère important
                score = scores[criterion]
                if score < 0.5:  # Score faible
                    concern_text = self.get_concern_description_france(criterion, score)
                    concerns.append(concern_text)

        return concerns[:2]  # Max 2 préoccupations

    def generate_recommendation_reason_france(self, city_data: Dict, user_profile: UserProfileFrance) -> str:
        """📝 Génère une explication personnalisée française"""

        city_name = city_data['name']
        region = city_data['region']

        if user_profile.main_priority == 'career_growth':
            return f"{city_name} ({region}) booste votre carrière avec un marché de l'emploi dynamique et un écosystème professionnel développé."
        elif user_profile.main_priority == 'cost_optimization':
            return f"{city_name} ({region}) optimise vos finances avec un excellent rapport qualité-prix et un coût de la vie maîtrisé."
        elif user_profile.main_priority == 'lifestyle_upgrade':
            return f"{city_name} ({region}) sublime votre quotidien grâce à son climat agréable et sa richesse culturelle."
        elif user_profile.main_priority == 'family_focus':
            return f"{city_name} ({region}) chouchoute votre famille avec d'excellentes écoles et un cadre de vie sécurisé."
        else:
            return f"{city_name} ({region}) correspond parfaitement à vos attentes personnalisées."

    def get_criterion_description_france(self, criterion: str, score: float) -> str:
        """📊 Description française d'un critère fort"""
        descriptions = {
            'cost_of_living': f"Coût de la vie très avantageux ({score*100:.0f}%)",
            'job_market': f"Marché de l'emploi excellent ({score*100:.0f}%)",
            'tech_industry': f"Écosystème tech dynamique ({score*100:.0f}%)",
            'climate_rating': f"Climat exceptionnel ({score*100:.0f}%)",
            'cultural_scene': f"Vie culturelle vibrante ({score*100:.0f}%)",
            'school_quality': f"Écoles publiques excellentes ({score*100:.0f}%)",
            'public_transport': f"Transports publics remarquables ({score*100:.0f}%)",
            'restaurant_diversity': f"Gastronomie exceptionnelle ({score*100:.0f}%)",
            'walkability': f"Très agréable à pied ({score*100:.0f}%)",
            'healthcare_access': f"Accès santé optimal ({score*100:.0f}%)",
        }
        return descriptions.get(criterion, f"{criterion} excellent ({score*100:.0f}%)")

    def get_concern_description_france(self, criterion: str, score: float) -> str:
        """⚠️ Description française d'un point d'attention"""
        concerns = {
            'cost_of_living': f"Coût de la vie élevé ({score*100:.0f}%)",
            'housing_affordability': f"Logement peu abordable ({score*100:.0f}%)",
            'public_transport': f"Transports publics limités ({score*100:.0f}%)",
            'job_market': f"Marché de l'emploi restreint ({score*100:.0f}%)",
            'climate_rating': f"Climat difficile ({score*100:.0f}%)",
            'school_quality': f"Écoles publiques moyennes ({score*100:.0f}%)",
        }
        return concerns.get(criterion, f"{criterion} à améliorer ({score*100:.0f}%)")

# Fonction factory pour être utilisé dans main.py
def create_france_residents_algorithm():
    """Factory pour créer l'instance de l'algorithme France"""
    return FranceResidentsAlgorithm('/var/www/Revolutionnary/platform/backend/data_v2/villes_france_residents.json')
