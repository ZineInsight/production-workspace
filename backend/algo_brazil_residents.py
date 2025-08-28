"""
🇧🇷 ALGO-BRAZIL-RESIDENTS.PY - ALGORITHME MATCHING VILLES BRÉSIL
=================================================================
Algorithme ultra performant pour matcher résidents/expats avec leurs 3 villes brésiliennes idéales
Author: Revolutionary Team | Version: 1.0.0 - Brazil Domestic + Expat Matching
OBJECTIF: Maximiser la DIVERSITÉ des recommandations entre profils similaires
"""

import json
import logging
from typing import Dict, List, Tuple
from dataclasses import dataclass

# Configuration logging
logger = logging.getLogger(__name__)

@dataclass
class UserProfileBrazil:
    """Profil utilisateur Brésil avec pondérations spécifiquement brésiliennes"""
    region_preference: str      # any_region, sudeste, sul, nordeste, centro_oeste, norte
    main_priority: str          # career_growth, cost_optimization, lifestyle_upgrade, safety_priority, family_focus
    age_profile: str           # student_young, young_professional, established_professional, pre_retirement
    monthly_budget: str        # budget_tight, budget_balanced, budget_comfortable, budget_premium
    work_situation: str        # stable_employment, job_search, full_remote, freelance_entrepreneur
    housing_preference: str    # city_center_apartment, suburban_house, beachfront_living, budget_priority
    transport_preference: str  # walk_bike_priority, public_transport_fan, car_essential, multimodal_flexible
    climate_preference: str    # tropical_warm, subtropical_mild, highland_fresh, climate_adaptable
    lifestyle_scene: str       # beach_carnival_culture, urban_cosmopolitan, nature_eco_tourism, sustainable_quality, historical_cultural
    safety_vs_culture: str     # safety_absolute_priority, safety_important_balance, culture_with_precautions, culture_absolute_priority
    family_situation: str      # single_no_children, couple_no_children, young_family, teen_family
    deal_breaker: str         # cost_too_high, safety_too_low, no_job_opportunities, climate_unbearable, social_isolation, no_deal_breaker
    criteria_weights: Dict[str, float]

class BrazilResidentsAlgorithm:
    """🇧🇷 Algorithme de recommandation pour résidents/expats Brésil"""

    def __init__(self, cities_data_path: str):
        """Initialise l'algorithme avec les données des 25 principales villes brésiliennes"""
        self.version = "1.0.0"
        self.cities_data = self.load_cities_data(cities_data_path)
        self.criteria_weights_base = self.get_base_criteria_weights_brazil()
        self.regional_mappings = self.get_regional_mappings()

    def load_cities_data(self, data_path: str) -> Dict:
        """Charge les données des 25 villes brésiliennes"""
        try:
            with open(data_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            logger.info(f"🇧🇷 Données Brésil chargées: {len(data['cities'])} villes")
            return data
        except Exception as e:
            logger.error(f"❌ Erreur chargement données Brésil: {e}")
            return {"cities": [], "metadata": {}, "criteria_definitions": {}}

    def get_base_criteria_weights_brazil(self) -> Dict[str, float]:
        """Poids de base adaptés au marché et à la mentalité brésilienne"""
        return {
            # Économique - Important mais varié selon région
            "cost_of_living": 1.0,
            "housing_affordability": 1.1,      # Logement crucial toutes classes
            "job_opportunities": 1.0,
            "salary_level": 0.9,
            "income_tax_burden": 0.7,          # Moins focus que Europe
            "entrepreneurship": 0.8,

            # Géographique/Climat - Très important Brésil
            "climate_comfort": 1.0,
            "beach_access": 0.9,               # Important mais pas universel
            "natural_beauty": 0.8,
            "flood_risk": 0.7,
            "heat_wave_risk": 0.6,

            # Sécurité/Social - CRITIQUE Brésil
            "safety_security": 1.3,            # Préoccupation majeure
            "healthcare_quality": 1.0,         # SUS + privé important
            "education_quality": 1.0,
            "diversity_inclusion": 0.8,

            # Transport/Urbain - Varié selon ville
            "public_transport": 0.9,
            "walkability": 0.8,
            "air_quality": 0.7,
            "urban_density": 0.7,

            # Culture/Lifestyle - ADN brésilien
            "cultural_scene": 1.0,
            "nightlife_entertainment": 0.8,
            "food_scene": 1.0,                 # Gastronomie importante
            "carnival_culture": 0.7,           # Pas universel mais typique
            "shopping_options": 0.6,
            "historical_heritage": 0.6,

            # Tech/Digital - En développement
            "internet_speed": 0.8,
            "coworking_spaces": 0.7,

            # Spécifique Brésil
            "portuguese_language": 0.0         # Pas discriminant (tous à 1.0)
        }

    def get_regional_mappings(self) -> Dict[str, List[str]]:
        """Mapping régions → villes pour filtres pré-scoring"""
        return {
            "sudeste": ["sao_paulo", "rio_de_janeiro", "belo_horizonte", "campinas", "vitoria", "ribeirao_preto"],
            "sul": ["porto_alegre", "curitiba", "florianopolis", "londrina"],
            "nordeste": ["salvador", "recife", "fortaleza", "natal", "joao_pessoa", "aracaju", "maceio", "teresina", "sao_luis"],
            "centro_oeste": ["brasilia", "goiania", "campo_grande", "cuiaba"],
            "norte": ["manaus", "belem"]
        }

    def create_user_profile_brazil(self, questionnaire_responses: Dict) -> UserProfileBrazil:
        """🧠 Crée profil utilisateur brésilien personnalisé à partir des réponses"""

        # Extraction des réponses spécifiques Brésil
        region_preference = questionnaire_responses.get('brazil_region_preference', 'any_region')
        main_priority = questionnaire_responses.get('brazil_main_priority', 'lifestyle_upgrade')
        age_profile = questionnaire_responses.get('brazil_age_profile', 'young_professional')
        monthly_budget = questionnaire_responses.get('brazil_monthly_budget', 'budget_balanced')
        work_situation = questionnaire_responses.get('brazil_work_situation', 'stable_employment')
        housing_preference = questionnaire_responses.get('brazil_housing_preference', 'city_center_apartment')
        transport_preference = questionnaire_responses.get('brazil_transport_preference', 'multimodal_flexible')
        climate_preference = questionnaire_responses.get('brazil_climate_preference', 'climate_adaptable')
        lifestyle_scene = questionnaire_responses.get('brazil_lifestyle_scene', 'urban_cosmopolitan')
        safety_vs_culture = questionnaire_responses.get('brazil_safety_vs_culture', 'safety_important_balance')
        family_situation = questionnaire_responses.get('brazil_family_situation', 'single_no_children')
        deal_breaker = questionnaire_responses.get('brazil_deal_breaker', 'no_deal_breaker')

        # Calcul pondérations dynamiques basées sur profil
        dynamic_weights = self.calculate_dynamic_weights_brazil(questionnaire_responses)

        return UserProfileBrazil(
            region_preference=region_preference,
            main_priority=main_priority,
            age_profile=age_profile,
            monthly_budget=monthly_budget,
            work_situation=work_situation,
            housing_preference=housing_preference,
            transport_preference=transport_preference,
            climate_preference=climate_preference,
            lifestyle_scene=lifestyle_scene,
            safety_vs_culture=safety_vs_culture,
            family_situation=family_situation,
            deal_breaker=deal_breaker,
            criteria_weights=dynamic_weights
        )

    def calculate_dynamic_weights_brazil(self, responses: Dict) -> Dict[str, float]:
        """🎯 Calcule pondérations dynamiques pour maximiser diversité recommandations"""

        weights = self.criteria_weights_base.copy()

        # ===== PRIORITÉ PRINCIPALE - BOOST MAJEUR =====
        main_priority = responses.get('brazil_main_priority', 'lifestyle_upgrade')

        if main_priority == "career_growth":
            # Profil A: Jeune Pro Tech → São Paulo, Campinas, BH
            weights["job_opportunities"] = 1.5
            weights["salary_level"] = 1.3
            weights["entrepreneurship"] = 1.2
            weights["coworking_spaces"] = 1.1
            weights["internet_speed"] = 1.1

        elif main_priority == "cost_optimization":
            # Budget serré → Nordeste, intérieur
            weights["cost_of_living"] = 1.6
            weights["housing_affordability"] = 1.4
            weights["salary_level"] = 0.7  # Accepte salaires plus bas

        elif main_priority == "lifestyle_upgrade":
            # Profil D: Remote + Beach → Natal, João Pessoa, Maceió
            weights["beach_access"] = 1.4
            weights["climate_comfort"] = 1.2
            weights["cultural_scene"] = 1.1
            weights["food_scene"] = 1.1

        elif main_priority == "safety_priority":
            # Profil C: Famille → Curitiba, Floripa, Brasília
            weights["safety_security"] = 1.8
            weights["education_quality"] = 1.3
            weights["healthcare_quality"] = 1.2
            weights["urban_density"] = 0.8  # Préfère moins dense

        elif main_priority == "family_focus":
            weights["education_quality"] = 1.4
            weights["healthcare_quality"] = 1.3
            weights["safety_security"] = 1.3
            weights["cultural_scene"] = 0.8

        # ===== RÉGION - AMPLIFICATION GÉOGRAPHIQUE =====
        region_pref = responses.get('brazil_region_preference', 'any_region')
        if region_pref == "nordeste":
            weights["beach_access"] = weights.get("beach_access", 1.0) * 1.3
            weights["carnival_culture"] = weights.get("carnival_culture", 1.0) * 1.4
            weights["cost_of_living"] = weights.get("cost_of_living", 1.0) * 1.2
        elif region_pref == "sul":
            # Profil B: Sul → Porto Alegre, Curitiba, Floripa
            weights["safety_security"] = weights.get("safety_security", 1.0) * 1.2
            weights["education_quality"] = weights.get("education_quality", 1.0) * 1.2
            weights["climate_comfort"] = weights.get("climate_comfort", 1.0) * 1.1

        # ===== BUDGET - EXCLUSIONS RÉALISTES =====
        budget = responses.get('brazil_monthly_budget', 'budget_balanced')
        if budget == "budget_tight":  # R$ 1.000-2.000
            weights["cost_of_living"] = weights.get("cost_of_living", 1.0) * 1.5
            weights["housing_affordability"] = weights.get("housing_affordability", 1.0) * 1.4
        elif budget == "budget_premium":  # R$ 8.000+
            weights["cultural_scene"] = weights.get("cultural_scene", 1.0) * 1.2
            weights["nightlife_entertainment"] = weights.get("nightlife_entertainment", 1.0) * 1.2

        # ===== WORK SITUATION - DIFFÉRENCIATION PRO =====
        work_sit = responses.get('brazil_work_situation', 'stable_employment')
        if work_sit == "freelance_entrepreneur":
            weights["entrepreneurship"] = weights.get("entrepreneurship", 1.0) * 1.4
            weights["coworking_spaces"] = weights.get("coworking_spaces", 1.0) * 1.3
        elif work_sit == "full_remote":
            weights["internet_speed"] = weights.get("internet_speed", 1.0) * 1.3
            weights["cost_of_living"] = weights.get("cost_of_living", 1.0) * 1.2

        # ===== LIFESTYLE - AMPLIFICATION CULTURELLE =====
        lifestyle = responses.get('brazil_lifestyle_scene', 'urban_cosmopolitan')
        if lifestyle == "beach_carnival_culture":
            weights["beach_access"] = weights.get("beach_access", 1.0) * 1.5
            weights["carnival_culture"] = weights.get("carnival_culture", 1.0) * 1.6
            weights["nightlife_entertainment"] = weights.get("nightlife_entertainment", 1.0) * 1.3
        elif lifestyle == "urban_cosmopolitan":
            weights["cultural_scene"] = weights.get("cultural_scene", 1.0) * 1.3
            weights["food_scene"] = weights.get("food_scene", 1.0) * 1.3
            weights["job_opportunities"] = weights.get("job_opportunities", 1.0) * 1.2

        # ===== SÉCURITÉ VS CULTURE - ARBITRAGE CRITIQUE =====
        safety_culture = responses.get('brazil_safety_vs_culture', 'safety_important_balance')
        if safety_culture == "safety_absolute_priority":
            weights["safety_security"] = weights.get("safety_security", 1.0) * 1.6
            weights["cultural_scene"] = weights.get("cultural_scene", 1.0) * 0.7
        elif safety_culture == "culture_absolute_priority":
            weights["cultural_scene"] = weights.get("cultural_scene", 1.0) * 1.5
            weights["carnival_culture"] = weights.get("carnival_culture", 1.0) * 1.4
            weights["safety_security"] = weights.get("safety_security", 1.0) * 0.8

        return weights

    def apply_regional_filters_brazil(self, cities_list: List[Dict], user_profile: UserProfileBrazil) -> List[Dict]:
        """🗺️ Filtre régional pré-scoring pour maximiser diversité"""

        if user_profile.region_preference == "any_region":
            return cities_list  # Toutes les 25 villes

        # Filtre selon région choisie
        region_cities = self.regional_mappings.get(user_profile.region_preference, [])
        filtered_cities = [city for city in cities_list if city['id'] in region_cities]

        logger.info(f"🗺️ Filtre régional {user_profile.region_preference}: {len(filtered_cities)} villes")
        return filtered_cities

    def apply_deal_breakers_brazil(self, cities_list: List[Dict], user_profile: UserProfileBrazil) -> List[Dict]:
        """❌ Exclusions absolues selon deal breakers"""

        if user_profile.deal_breaker == "no_deal_breaker":
            return cities_list

        filtered_cities = []

        for city in cities_list:
            exclude_city = False

            if user_profile.deal_breaker == "cost_too_high":
                # Exclut villes avec cost_of_living < 0.5 (trop chères)
                if city['scores']['cost_of_living'] < 0.5:
                    exclude_city = True

            elif user_profile.deal_breaker == "safety_too_low":
                # Exclut villes avec safety_security < 0.6
                if city['scores']['safety_security'] < 0.6:
                    exclude_city = True

            elif user_profile.deal_breaker == "no_job_opportunities":
                # Exclut villes avec job_opportunities < 0.6
                if city['scores']['job_opportunities'] < 0.6:
                    exclude_city = True

            elif user_profile.deal_breaker == "climate_unbearable":
                # Exclut selon préférence climatique
                if user_profile.climate_preference == "subtropical_mild":
                    # Refuse trop chaud (heat_wave_risk < 0.7)
                    if city['scores']['heat_wave_risk'] < 0.7:
                        exclude_city = True

            elif user_profile.deal_breaker == "social_isolation":
                # Exclut petites villes (population < 500k)
                if city.get('population', 0) < 500000:
                    exclude_city = True

            if not exclude_city:
                filtered_cities.append(city)

        logger.info(f"❌ Deal breaker {user_profile.deal_breaker}: {len(filtered_cities)}/{len(cities_list)} villes restantes")
        return filtered_cities

    def calculate_city_score_brazil(self, city: Dict, user_profile: UserProfileBrazil) -> float:
        """🎯 Calcule score ville avec amplifications pour diversité"""

        total_score = 0.0
        total_weight = 0.0

        # Score de base pondéré
        for criterion, weight in user_profile.criteria_weights.items():
            if criterion in city['scores']:
                city_value = city['scores'][criterion]
                weighted_score = city_value * weight
                total_score += weighted_score
                total_weight += weight

        base_score = total_score / total_weight if total_weight > 0 else 0.0

        # ===== AMPLIFICATIONS PERSONNALITÉ =====
        amplified_score = base_score

        # Budget amplifie coût de la vie
        if user_profile.monthly_budget == "budget_tight":
            if city['scores']['cost_of_living'] >= 0.7:  # Nordeste abordable
                amplified_score *= 1.3
        elif user_profile.monthly_budget == "budget_premium":
            if city['id'] in ['sao_paulo', 'rio_de_janeiro', 'florianopolis']:
                amplified_score *= 1.2

        # Climat amplifie selon préférence
        if user_profile.climate_preference == "tropical_warm":
            if city['region'] in ['Bahia', 'Ceará', 'Pernambuco', 'Rio Grande do Norte', 'Paraíba', 'Alagoas']:
                amplified_score *= 1.2
        elif user_profile.climate_preference == "subtropical_mild":
            if city['region'] in ['Rio Grande do Sul', 'Santa Catarina', 'Paraná']:
                amplified_score *= 1.2

        # Lifestyle amplifie
        if user_profile.lifestyle_scene == "beach_carnival_culture":
            if city['scores']['beach_access'] >= 0.9 and city['scores']['carnival_culture'] >= 0.8:
                amplified_score *= 1.3

        # ===== BONUS ANTI-CONVERGENCE =====
        # Pénalise légèrement les villes trop populaires pour forcer diversité
        popular_penalties = {
            "sao_paulo": 0.95,     # -5%
            "rio_de_janeiro": 0.95, # -5%
            "brasilia": 0.97       # -3%
        }

        diversity_score = amplified_score * popular_penalties.get(city['id'], 1.0)

        return min(diversity_score, 1.0)  # Cap à 1.0

    def get_recommendations(self, questionnaire_responses: Dict, top_n: int = 3) -> Dict:
        """🎯 Interface standardisée - Retourne top 3 villes personnalisées"""

        try:
            # Création profil utilisateur
            user_profile = self.create_user_profile_brazil(questionnaire_responses)

            # Chargement villes
            all_cities = self.cities_data.get('cities', [])
            if not all_cities:
                return {"status": "error", "message": "Aucune donnée de ville disponible"}

            # ÉTAPE 1: Filtres pré-scoring
            filtered_cities = self.apply_regional_filters_brazil(all_cities, user_profile)
            filtered_cities = self.apply_deal_breakers_brazil(filtered_cities, user_profile)

            if not filtered_cities:
                return {"status": "error", "message": "Aucune ville ne correspond à vos critères"}

            # ÉTAPE 2: Scoring personnalisé
            scored_cities = []
            for city in filtered_cities:
                score = self.calculate_city_score_brazil(city, user_profile)
                scored_cities.append({
                    "city": city['name'],
                    "city_id": city['id'],
                    "region": city['region'],
                    "population": city['population'],
                    "score_percentage": int(score * 100),
                    "coordinates": city['coordinates'],
                    "detailed_scores": city['scores']
                })

            # ÉTAPE 3: Sélection top N
            scored_cities.sort(key=lambda x: x['score_percentage'], reverse=True)
            top_recommendations = scored_cities[:top_n]

            logger.info(f"🇧🇷 Recommandations générées: {len(top_recommendations)} villes pour profil {user_profile.main_priority}")

            return {
                "status": "success",
                "recommendations": top_recommendations,
                "total_cities_analyzed": len(filtered_cities),
                "user_profile_summary": {
                    "region": user_profile.region_preference,
                    "priority": user_profile.main_priority,
                    "budget": user_profile.monthly_budget,
                    "lifestyle": user_profile.lifestyle_scene
                }
            }

        except Exception as e:
            logger.error(f"❌ Erreur génération recommandations Brésil: {e}")
            return {"status": "error", "message": f"Erreur technique: {str(e)}"}

    # ===== MÉTHODES UTILITAIRES =====

    def get_cities_count(self) -> int:
        """Retourne le nombre de villes disponibles"""
        return len(self.cities_data.get('cities', []))

    def get_criteria_list(self) -> List[str]:
        """Retourne la liste des critères disponibles"""
        return list(self.criteria_weights_base.keys())

    def health_check(self) -> Dict:
        """Health check pour monitoring"""
        return {
            "status": "healthy",
            "cities_loaded": self.get_cities_count(),
            "criteria_count": len(self.get_criteria_list()),
            "version": self.version,
            "regions_supported": list(self.regional_mappings.keys())
        }
