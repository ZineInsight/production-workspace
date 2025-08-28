"""
🇺🇸 ALGO-USA-RESIDENTS.PY - ALGORITHME MATCHING VILLES USA
===========================================================
Algorithme ultra performant pour matcher Américains avec leurs 3 villes idéales
Author: Revolutionary Team | Version: 1.0.0 - USA Domestic Matching
OBJECTIF: Recommandations précises basées sur profil utilisateur et priorités
"""

import json
import math
from typing import Dict, List, Tuple
from dataclasses import dataclass
import logging

# Configuration logging
logger = logging.getLogger(__name__)

import json
import math
from typing import Dict, List, Tuple
from dataclasses import dataclass
from flask import Flask, request, jsonify
from flask_cors import CORS
import logging

# Configuration logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class UserProfile:
    """Profil utilisateur USA avec pondérations personnalisées"""
    main_priority: str
    budget_tier: str
    work_situation: str
    climate_preference: str
    lifestyle_density: str
    tax_philosophy: str
    disaster_tolerance: str
    transport_preference: str
    education_priority: str
    social_scene: str
    criteria_weights: Dict[str, float]

class USAResidentsAlgorithm:
    """🎯 Algorithme de matching ultra sophistiqué pour résidents USA"""

    def __init__(self, cities_data_path: str):
        """Initialise l'algorithme avec les données des villes"""
        self.cities_data = self.load_cities_data(cities_data_path)
        self.criteria_weights_base = self.get_base_criteria_weights()

    def load_cities_data(self, data_path: str) -> Dict:
        """Charge les données des 50 villes USA"""
        with open(data_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def get_base_criteria_weights(self) -> Dict[str, float]:
        """Poids de base pour chaque critère (avant personnalisation)"""
        return {
            # Critères financiers (impact budget quotidien)
            "cost_of_living": 1.0,
            "housing_affordability": 1.0,
            "state_tax_burden": 0.8,
            "sales_tax": 0.6,
            "property_tax": 0.7,

            # Critères climatiques (confort quotidien)
            "climate_rating": 0.9,
            "weather_consistency": 0.7,

            # Critères professionnels (carrière/revenus)
            "job_market": 1.0,
            "tech_industry": 0.8,
            "remote_work_friendly": 0.7,

            # Critères urbains/lifestyle (quotidien)
            "urban_density": 0.8,
            "suburb_quality": 0.8,
            "walkability": 0.7,
            "public_transport": 0.6,
            "car_dependency": 0.6,

            # Critères éducation/famille (futur)
            "school_quality": 0.9,
            "university_access": 0.6,

            # Critères risques (sécurité/stress)
            "natural_disaster_risk": 0.8,
            "hurricane_risk": 0.7,
            "earthquake_risk": 0.6,

            # Critères santé (bien-être)
            "healthcare_access": 0.8,
            "hospital_quality": 0.7,

            # Critères culturels (épanouissement)
            "cultural_scene": 0.7,
            "restaurant_diversity": 0.6,
            "nightlife": 0.5
        }

    def create_user_profile(self, questionnaire_responses: Dict) -> UserProfile:
        """🧠 Crée profil utilisateur personnalisé à partir des réponses"""

        # Extraction des réponses
        main_priority = questionnaire_responses.get('usa_main_priority')
        budget_tier = questionnaire_responses.get('usa_monthly_budget')
        work_situation = questionnaire_responses.get('usa_work_situation')
        climate_pref = questionnaire_responses.get('usa_climate_preference')
        lifestyle_density = questionnaire_responses.get('usa_lifestyle_density')
        tax_philosophy = questionnaire_responses.get('usa_tax_philosophy')
        disaster_tolerance = questionnaire_responses.get('usa_disaster_tolerance')
        transport_pref = questionnaire_responses.get('usa_transport_preference')
        education_priority = questionnaire_responses.get('usa_education_priority')
        social_scene = questionnaire_responses.get('usa_social_scene')

        # 🎯 CALCUL PONDÉRATIONS PERSONNALISÉES
        weights = self.criteria_weights_base.copy()

        # === BOOST PRIORITÉ PRINCIPALE ===
        if main_priority == 'career_growth':
            weights['job_market'] *= 2.0
            weights['tech_industry'] *= 1.8
            weights['remote_work_friendly'] *= 1.5
            weights['university_access'] *= 1.3
        elif main_priority == 'cost_optimization':
            weights['cost_of_living'] *= 2.2
            weights['housing_affordability'] *= 2.0
            weights['state_tax_burden'] *= 1.8
            weights['property_tax'] *= 1.5
        elif main_priority == 'lifestyle_upgrade':
            weights['climate_rating'] *= 1.8
            weights['cultural_scene'] *= 1.7
            weights['restaurant_diversity'] *= 1.5
            weights['nightlife'] *= 1.3
        elif main_priority == 'family_focus':
            weights['school_quality'] *= 2.0
            weights['suburb_quality'] *= 1.8
            weights['healthcare_access'] *= 1.6
            weights['natural_disaster_risk'] *= 1.4

        # === ADAPTATION BUDGET ===
        if budget_tier == 'budget_tight':
            weights['cost_of_living'] *= 1.8
            weights['housing_affordability'] *= 1.8
            weights['state_tax_burden'] *= 1.5
        elif budget_tier == 'budget_premium':
            weights['cultural_scene'] *= 1.4
            weights['restaurant_diversity'] *= 1.3
            weights['tech_industry'] *= 1.2

        # === SITUATION PROFESSIONNELLE ===
        if work_situation == 'remote_full':
            weights['cost_of_living'] *= 1.5
            weights['climate_rating'] *= 1.4
            weights['job_market'] *= 0.6  # Moins important
        elif work_situation == 'job_search':
            weights['job_market'] *= 1.8
            weights['tech_industry'] *= 1.6
            weights['university_access'] *= 1.2

        # === PRÉFÉRENCES CLIMATIQUES ===
        if climate_pref == 'warm_sunny':
            weights['climate_rating'] *= 1.6
            weights['weather_consistency'] *= 1.4
        elif climate_pref == 'four_seasons':
            weights['cultural_scene'] *= 1.2
            weights['climate_rating'] *= 1.3

        # === MODE DE VIE URBAIN ===
        if lifestyle_density == 'downtown_urban':
            weights['urban_density'] *= 1.7
            weights['walkability'] *= 1.6
            weights['public_transport'] *= 1.5
            weights['cultural_scene'] *= 1.3
        elif lifestyle_density == 'family_suburbs':
            weights['suburb_quality'] *= 1.8
            weights['school_quality'] *= 1.5
            weights['car_dependency'] *= 1.2

        # === PHILOSOPHIE FISCALE ===
        if tax_philosophy == 'no_state_tax':
            weights['state_tax_burden'] *= 2.0
            weights['cost_of_living'] *= 1.3
        elif tax_philosophy == 'services_priority':
            weights['school_quality'] *= 1.4
            weights['healthcare_access'] *= 1.3
            weights['public_transport'] *= 1.2

        # === TOLÉRANCE RISQUES ===
        if disaster_tolerance == 'risk_averse':
            weights['natural_disaster_risk'] *= 1.8
            weights['hurricane_risk'] *= 1.6
            weights['earthquake_risk'] *= 1.4

        # === TRANSPORT ===
        if transport_pref == 'car_free_dream':
            weights['walkability'] *= 1.8
            weights['public_transport'] *= 1.7
            weights['urban_density'] *= 1.4
        elif transport_pref == 'car_essential':
            weights['car_dependency'] *= 1.2
            weights['suburb_quality'] *= 1.2

        # === ÉDUCATION ===
        if education_priority == 'top_schools_essential':
            weights['school_quality'] *= 1.9
            weights['university_access'] *= 1.4
            weights['suburb_quality'] *= 1.3

        # === SCÈNE SOCIALE ===
        if social_scene == 'foodie_culture':
            weights['restaurant_diversity'] *= 1.6
            weights['cultural_scene'] *= 1.3
        elif social_scene == 'nightlife_entertainment':
            weights['nightlife'] *= 1.7
            weights['cultural_scene'] *= 1.4
            weights['urban_density'] *= 1.2

        return UserProfile(
            main_priority=main_priority,
            budget_tier=budget_tier,
            work_situation=work_situation,
            climate_preference=climate_pref,
            lifestyle_density=lifestyle_density,
            tax_philosophy=tax_philosophy,
            disaster_tolerance=disaster_tolerance,
            transport_preference=transport_pref,
            education_priority=education_priority,
            social_scene=social_scene,
            criteria_weights=weights
        )

    def calculate_city_score(self, city_data: Dict, user_profile: UserProfile) -> float:
        """🧮 Calcule le score total d'une ville pour un profil utilisateur"""

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

    def apply_advanced_bonuses(self, city_data: Dict, base_score: float, user_profile: UserProfile) -> float:
        """🚀 Applique des bonus avancés basés sur des combinaisons spéciales"""

        bonus_score = base_score
        city_scores = city_data['scores']

        # === BONUS SYNERGIES ===

        # Bonus "Tech Hub Complete" (Austin, Seattle, Denver style)
        if (city_scores.get('tech_industry', 0) > 0.8 and
            city_scores.get('job_market', 0) > 0.8 and
            city_scores.get('remote_work_friendly', 0) > 0.8 and
            user_profile.main_priority == 'career_growth'):
            bonus_score *= 1.15

        # Bonus "Perfect Family Package" (banlieues + écoles + sécurité)
        if (city_scores.get('suburb_quality', 0) > 0.8 and
            city_scores.get('school_quality', 0) > 0.8 and
            city_scores.get('natural_disaster_risk', 0) > 0.8 and
            user_profile.main_priority == 'family_focus'):
            bonus_score *= 1.12

        # Bonus "Financial Paradise" (taxes + coût de la vie)
        if (city_scores.get('state_tax_burden', 0) > 0.9 and
            city_scores.get('cost_of_living', 0) > 0.8 and
            city_scores.get('housing_affordability', 0) > 0.7 and
            user_profile.main_priority == 'cost_optimization'):
            bonus_score *= 1.18

        # Bonus "Cultural Hotspot" (scène + restaurants + nightlife)
        if (city_scores.get('cultural_scene', 0) > 0.8 and
            city_scores.get('restaurant_diversity', 0) > 0.8 and
            city_scores.get('nightlife', 0) > 0.7 and
            user_profile.main_priority == 'lifestyle_upgrade'):
            bonus_score *= 1.10

        # Bonus "Car-Free Paradise" (walkable + transport + dense)
        if (city_scores.get('walkability', 0) > 0.8 and
            city_scores.get('public_transport', 0) > 0.7 and
            city_scores.get('urban_density', 0) > 0.7 and
            user_profile.transport_preference == 'car_free_dream'):
            bonus_score *= 1.08

        # === MALUS DEAL-BREAKERS ===

        # Malus budget serré mais ville chère
        if (user_profile.budget_tier == 'budget_tight' and
            city_scores.get('cost_of_living', 1.0) < 0.6):
            bonus_score *= 0.85

        # Malus risque-averse mais zone à risques
        if (user_profile.disaster_tolerance == 'risk_averse' and
            city_scores.get('natural_disaster_risk', 1.0) < 0.6):
            bonus_score *= 0.80

        # Malus famille priorité mais écoles moyennes
        if (user_profile.main_priority == 'family_focus' and
            city_scores.get('school_quality', 1.0) < 0.6):
            bonus_score *= 0.88

        return min(bonus_score, 1.0)  # Cap à 1.0

    def get_top_recommendations(self, questionnaire_responses: Dict, top_n: int = 3) -> List[Dict]:
        """🏆 Retourne le TOP N des villes recommandées"""

        # Créer profil utilisateur
        user_profile = self.create_user_profile(questionnaire_responses)

        city_scores = []

        # Calculer score pour chaque ville
        for city in self.cities_data['cities']:
            base_score = self.calculate_city_score(city, user_profile)
            final_score = self.apply_advanced_bonuses(city, base_score, user_profile)

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
                'state': city_score['city_data']['state'],
                'score_percentage': city_score['score_percentage'],
                'population': city_score['city_data']['population'],
                'coordinates': city_score['city_data']['coordinates'],
                'top_strengths': self.get_city_strengths(city_score['city_data'], user_profile),
                'potential_concerns': self.get_city_concerns(city_score['city_data'], user_profile),
                'why_recommended': self.generate_recommendation_reason(city_score['city_data'], user_profile)
            }
            top_recommendations.append(recommendation)

        return top_recommendations

    def get_city_strengths(self, city_data: Dict, user_profile: UserProfile) -> List[str]:
        """💪 Identifie les points forts d'une ville pour ce profil"""
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
                strength_text = self.get_criterion_description(criterion, score)
                strengths.append(strength_text)

        return strengths[:3]  # Max 3 points forts

    def get_city_concerns(self, city_data: Dict, user_profile: UserProfile) -> List[str]:
        """⚠️ Identifie les points d'attention d'une ville pour ce profil"""
        concerns = []
        scores = city_data['scores']
        weights = user_profile.criteria_weights

        # Critères importants pour l'utilisateur mais faibles pour la ville
        for criterion, weight in weights.items():
            if weight > 1.2 and criterion in scores:  # Critère important
                score = scores[criterion]
                if score < 0.5:  # Score faible
                    concern_text = self.get_concern_description(criterion, score)
                    concerns.append(concern_text)

        return concerns[:2]  # Max 2 préoccupations

    def generate_recommendation_reason(self, city_data: Dict, user_profile: UserProfile) -> str:
        """📝 Génère une explication personnalisée de pourquoi cette ville est recommandée"""

        city_name = city_data['name']
        state = city_data['state']

        if user_profile.main_priority == 'career_growth':
            return f"{city_name}, {state} excelle pour votre croissance professionnelle avec un marché de l'emploi dynamique et un écosystème tech développé."
        elif user_profile.main_priority == 'cost_optimization':
            return f"{city_name}, {state} optimise vos finances avec un coût de la vie avantageux et une fiscalité favorable."
        elif user_profile.main_priority == 'lifestyle_upgrade':
            return f"{city_name}, {state} élève votre qualité de vie grâce à son climat agréable et sa scène culturelle vibrante."
        elif user_profile.main_priority == 'family_focus':
            return f"{city_name}, {state} est parfaite pour votre famille avec d'excellentes écoles et des quartiers sûrs."
        else:
            return f"{city_name}, {state} correspond parfaitement à vos critères personnalisés."

    def get_criterion_description(self, criterion: str, score: float) -> str:
        """📊 Description human-friendly d'un critère fort"""
        descriptions = {
            'cost_of_living': f"Coût de la vie très abordable ({score*100:.0f}%)",
            'job_market': f"Marché de l'emploi excellent ({score*100:.0f}%)",
            'tech_industry': f"Hub technologique majeur ({score*100:.0f}%)",
            'climate_rating': f"Climat exceptionnel ({score*100:.0f}%)",
            'cultural_scene': f"Scène culturelle vibrante ({score*100:.0f}%)",
            'school_quality': f"Écoles publiques excellentes ({score*100:.0f}%)",
            'walkability': f"Très accessible à pied ({score*100:.0f}%)",
            'state_tax_burden': f"Taxes d'état très favorables ({score*100:.0f}%)",
            # Ajouter plus selon besoins...
        }
        return descriptions.get(criterion, f"{criterion} excellent ({score*100:.0f}%)")

    def get_concern_description(self, criterion: str, score: float) -> str:
        """⚠️ Description human-friendly d'un point d'attention"""
        concerns = {
            'cost_of_living': f"Coût de la vie élevé ({score*100:.0f}%)",
            'natural_disaster_risk': f"Risques naturels présents ({score*100:.0f}%)",
            'public_transport': f"Transports publics limités ({score*100:.0f}%)",
            'school_quality': f"Écoles publiques moyennes ({score*100:.0f}%)",
            'climate_rating': f"Climat difficile ({score*100:.0f}%)",
            # Ajouter plus selon besoins...
        }
        return concerns.get(criterion, f"{criterion} à améliorer ({score*100:.0f}%)")

# Fonction pour être utilisé dans main.py
def create_usa_residents_algorithm():
    """Factory pour créer l'instance de l'algorithme USA"""
    return USAResidentsAlgorithm('/var/www/Revolutionnary/platform/backend/data_v2/villes_usa_residents.json')
