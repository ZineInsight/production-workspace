"""
🇩🇪 GERMANY RESIDENTS ALGORITHM
Algorithme de matching pour résidents allemands cherchant relocation domestique

Architecture standardisée : filtres pré-scoring + critères pondérés + méthode get_recommendations()
"""

import json
import logging
from typing import Dict, List, Tuple, Any
from pathlib import Path

class GermanyResidentsAlgorithm:
    def __init__(self, cities_data_path: str):
        """
        Initialise l'algorithme Germany Residents avec données des villes

        Args:
            cities_data_path: Chemin vers villes_germany_residents.json
        """
        self.version = "1.0.0"  # ⚠️ OBLIGATOIRE pour health check
        self.cities_data = self.load_cities_data(cities_data_path)
        self.criteria_weights_base = self.get_base_criteria_weights_germany()

        # Filtres régionaux/linguistiques disponibles
        self.regional_filters = {
            "southern_germany": ["munich", "stuttgart", "nuremberg", "karlsruhe", "mannheim", "augsburg"],
            "western_germany": ["cologne", "frankfurt", "dusseldorf", "dortmund", "essen", "duisburg", "bochum", "wuppertal", "bielefeld", "bonn", "munster", "wiesbaden", "gelsenkirchen", "monchengladbach", "aachen"],
            "northern_germany": ["hamburg", "hannover", "braunschweig", "kiel"],
            "eastern_germany": ["berlin", "leipzig", "dresden", "chemnitz", "halle"]
        }

        self.language_filters = {
            "german_native": "all_cities",
            "german_learning": "all_cities",
            "english_priority": ["berlin", "munich", "hamburg", "frankfurt", "cologne", "dusseldorf"],
            "multilingual_comfort": "all_cities"
        }

    def load_cities_data(self, file_path: str) -> Dict:
        """Charge les données des villes depuis le fichier JSON"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            logging.error(f"Fichier de données non trouvé : {file_path}")
            raise
        except json.JSONDecodeError as e:
            logging.error(f"Erreur décodage JSON : {e}")
            raise

    def get_base_criteria_weights_germany(self) -> Dict[str, float]:
        """
        Poids de base des critères pour l'Allemagne
        Adaptés aux priorités des résidents allemands
        """
        return {
            # 💰 Facteurs Économiques (35%)
            "cost_of_living": 0.12,
            "housing_affordability": 0.15,
            "income_tax_burden": 0.05,
            "local_tax": 0.03,

            # 💼 Facteurs Professionnels (20%)
            "job_market": 0.08,
            "tech_industry": 0.06,
            "remote_work_friendly": 0.06,

            # 🚊 Mobilité et Infrastructure (15%)
            "public_transport": 0.08,
            "walkability": 0.04,
            "car_dependency": 0.03,

            # 🏫 Éducation et Santé (12%)
            "school_quality": 0.04,
            "university_access": 0.03,
            "healthcare_access": 0.03,
            "hospital_quality": 0.02,

            # 🌍 Qualité de Vie (10%)
            "climate_rating": 0.04,
            "weather_consistency": 0.02,
            "urban_density": 0.02,
            "suburb_quality": 0.02,

            # 🎭 Culture et Social (5%)
            "cultural_scene": 0.02,
            "restaurant_diversity": 0.01,
            "nightlife": 0.02,

            # 🛡️ Sécurité et Risques (2%)
            "natural_disaster_risk": 0.01,
            "flood_risk": 0.005,
            "heat_wave_risk": 0.005,

            # 🗣️ Facteurs Linguistiques (1%)
            "german_language_score": 0.005,
            "english_friendly_score": 0.005
        }

    def apply_regional_language_filters(self, cities_list: List[Dict], user_profile: Dict) -> List[Dict]:
        """
        Applique les filtres régionaux et linguistiques AVANT le scoring
        Innovation UK/Canada 2025 : Performance x3 avec filtrage pré-scoring

        Args:
            cities_list: Liste complète des villes
            user_profile: Profil utilisateur avec préférences

        Returns:
            Liste filtrée des villes pertinentes
        """
        filtered_cities = cities_list.copy()

        # 🗺️ Filtre Régional
        region_preference = user_profile.get('germany_region_preference', 'region_flexible')
        if region_preference != 'region_flexible' and region_preference in self.regional_filters:
            target_cities = self.regional_filters[region_preference]
            filtered_cities = [city for city in filtered_cities if city['id'] in target_cities]
            logging.info(f"Filtre régional '{region_preference}': {len(filtered_cities)} villes retenues")

        # 🗣️ Filtre Linguistique
        language_comfort = user_profile.get('germany_language_comfort', 'multilingual_comfort')
        if language_comfort == 'english_priority':
            english_friendly_cities = self.language_filters['english_priority']
            filtered_cities = [city for city in filtered_cities if city['id'] in english_friendly_cities]
            logging.info(f"Filtre linguistique anglophone: {len(filtered_cities)} villes retenues")

        return filtered_cities

    def adapt_weights_to_user_profile(self, base_weights: Dict[str, float], user_profile: Dict) -> Dict[str, float]:
        """
        Adapte les poids des critères selon le profil utilisateur

        Args:
            base_weights: Poids de base des critères
            user_profile: Réponses du questionnaire utilisateur

        Returns:
            Poids ajustés selon le profil
        """
        adjusted_weights = base_weights.copy()

        # 🎯 Priorité principale
        main_priority = user_profile.get('germany_main_priority', '')
        if main_priority == 'cost_optimization':
            adjusted_weights['cost_of_living'] *= 2.0
            adjusted_weights['housing_affordability'] *= 2.2
            adjusted_weights['income_tax_burden'] *= 2.5
            adjusted_weights['local_tax'] *= 2.0

        elif main_priority == 'career_growth':
            adjusted_weights['job_market'] *= 2.5
            adjusted_weights['tech_industry'] *= 2.2
            adjusted_weights['remote_work_friendly'] *= 1.8

        elif main_priority == 'quality_life':
            adjusted_weights['climate_rating'] *= 2.0
            adjusted_weights['urban_density'] *= 1.8
            adjusted_weights['suburb_quality'] *= 2.0
            adjusted_weights['public_transport'] *= 1.5

        elif main_priority == 'family_education':
            adjusted_weights['school_quality'] *= 2.5
            adjusted_weights['suburb_quality'] *= 2.0
            adjusted_weights['healthcare_access'] *= 1.8
            adjusted_weights['natural_disaster_risk'] *= 1.5

        elif main_priority == 'culture_lifestyle':
            adjusted_weights['cultural_scene'] *= 2.5
            adjusted_weights['restaurant_diversity'] *= 2.0
            adjusted_weights['nightlife'] *= 2.0

        # 💶 Budget logement
        budget_range = user_profile.get('germany_budget_range', '')
        if budget_range == 'budget_low':
            adjusted_weights['cost_of_living'] *= 2.0
            adjusted_weights['housing_affordability'] *= 2.5
        elif budget_range == 'budget_premium':
            adjusted_weights['cost_of_living'] *= 0.5
            adjusted_weights['cultural_scene'] *= 1.5
            adjusted_weights['restaurant_diversity'] *= 1.5

        # 💻 Style de travail
        work_style = user_profile.get('germany_work_style', '')
        if work_style == 'full_remote':
            adjusted_weights['remote_work_friendly'] *= 2.0
            adjusted_weights['cost_of_living'] *= 1.5
        elif work_style == 'startup_dynamic':
            adjusted_weights['tech_industry'] *= 2.0
            adjusted_weights['job_market'] *= 1.5

        # 🚊 Transport priorité
        transport_priority = user_profile.get('germany_transport_priority', '')
        if transport_priority == 'public_transport_fan':
            adjusted_weights['public_transport'] *= 2.5
            adjusted_weights['car_dependency'] *= 0.3
        elif transport_priority == 'walkable_city':
            adjusted_weights['walkability'] *= 2.5
            adjusted_weights['urban_density'] *= 0.8
        elif transport_priority == 'car_friendly':
            adjusted_weights['car_dependency'] *= 0.3  # Inversé : plus de car_dependency = moins bon score

        # 📊 Sensibilité fiscale
        tax_sensitivity = user_profile.get('germany_tax_sensitivity', '')
        if tax_sensitivity == 'tax_optimization':
            adjusted_weights['income_tax_burden'] *= 2.5
            adjusted_weights['local_tax'] *= 2.0
            adjusted_weights['church_tax'] = 0.02  # Ajout critère church_tax
        elif tax_sensitivity == 'services_priority':
            adjusted_weights['healthcare_access'] *= 1.8
            adjusted_weights['school_quality'] *= 1.5
            adjusted_weights['public_transport'] *= 1.5

        # 🎯 Focus carrière
        career_focus = user_profile.get('germany_career_focus', '')
        if career_focus == 'tech_innovation':
            adjusted_weights['tech_industry'] *= 2.5
            adjusted_weights['job_market'] *= 1.5
        elif career_focus == 'finance_banking':
            adjusted_weights['job_market'] *= 2.0
            # Frankfurt bonus implicite via données
        elif career_focus == 'automotive_industry':
            # Stuttgart, Munich bonus via données
            adjusted_weights['job_market'] *= 1.8

        # 🗣️ Confort linguistique
        language_comfort = user_profile.get('germany_language_comfort', '')
        if language_comfort == 'english_priority':
            adjusted_weights['english_friendly_score'] *= 5.0
        elif language_comfort == 'german_native':
            adjusted_weights['german_language_score'] *= 2.0

        return adjusted_weights

    def calculate_city_score(self, city: Dict, user_weights: Dict[str, float]) -> float:
        """
        Calcule le score d'une ville selon les poids utilisateur

        Args:
            city: Données de la ville
            user_weights: Poids ajustés au profil utilisateur

        Returns:
            Score final de la ville (0.0 à 1.0)
        """
        city_scores = city.get('scores', {})
        weighted_score = 0.0
        total_weight = 0.0

        for criterion, weight in user_weights.items():
            if criterion in city_scores:
                criterion_score = city_scores[criterion]
                weighted_score += criterion_score * weight
                total_weight += weight

        # Normalisation
        if total_weight > 0:
            final_score = weighted_score / total_weight
        else:
            final_score = 0.0

        return min(max(final_score, 0.0), 1.0)  # Borné entre 0 et 1

    def get_recommendations(self, questionnaire_responses: Dict, top_n: int = 3) -> Dict:
        """
        Interface standardisée pour obtenir les recommandations
        Compatible avec main.py et architecture globale

        Args:
            questionnaire_responses: Réponses du questionnaire utilisateur
            top_n: Nombre de recommandations à retourner

        Returns:
            Dict avec format : {"status": "success", "recommendations": [...]}
        """
        try:
            # Extraction des villes depuis les données chargées
            cities_list = self.cities_data.get('cities', [])
            if not cities_list:
                return {
                    "status": "error",
                    "message": "Aucune donnée de ville disponible"
                }

            # 🔥 INNOVATION : Filtrage pré-scoring (Performance x3)
            filtered_cities = self.apply_regional_language_filters(cities_list, questionnaire_responses)

            if not filtered_cities:
                # Fallback : si aucune ville après filtrage, prendre toutes
                filtered_cities = cities_list
                logging.warning("Aucune ville après filtrage - utilisation de toutes les villes")

            # Adaptation des poids selon profil utilisateur
            user_weights = self.adapt_weights_to_user_profile(
                self.criteria_weights_base,
                questionnaire_responses
            )

            # Calcul des scores pour villes filtrées
            city_scores = []
            for city in filtered_cities:
                score = self.calculate_city_score(city, user_weights)
                city_scores.append({
                    "city": city['name'],
                    "region": city['region'],
                    "country": "Germany",
                    "score_percentage": round(score * 100, 1),
                    "population": city.get('population', 0),
                    "coordinates": city.get('coordinates', {}),
                    "city_id": city['id']
                })

            # Tri et sélection du top N
            city_scores.sort(key=lambda x: x['score_percentage'], reverse=True)
            top_recommendations = city_scores[:top_n]

            logging.info(f"Germany Algorithm: {len(top_recommendations)} recommandations générées")

            return {
                "status": "success",
                "recommendations": top_recommendations,
                "algorithm_version": self.version,
                "total_cities_analyzed": len(filtered_cities),
                "filter_applied": len(filtered_cities) != len(cities_list)
            }

        except Exception as e:
            logging.error(f"Erreur dans GermanyResidentsAlgorithm: {str(e)}")
            return {
                "status": "error",
                "message": f"Erreur algorithme Germany: {str(e)}"
            }

    def get_cities_count(self) -> int:
        """Retourne le nombre de villes disponibles"""
        return len(self.cities_data.get('cities', []))

    def get_criteria_list(self) -> List[str]:
        """Retourne la liste des critères disponibles"""
        return list(self.criteria_weights_base.keys())

    def get_health_status(self) -> Dict:
        """Retourne le statut de santé de l'algorithme"""
        return {
            "status": "healthy",
            "version": self.version,
            "cities_count": self.get_cities_count(),
            "criteria_count": len(self.get_criteria_list())
        }
