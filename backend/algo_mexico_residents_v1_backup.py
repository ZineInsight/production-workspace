#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🇲🇽 MEXICO RESIDENTS ALGORITHM - Revolutionary Platform
===========================================================

Algorithme intelligent pour recommandations de villes mexicaines
Approche hybride résidents/expats avec 100% mapping JS ↔ Python

Pattern Revolutionary avec 10 zones géographiques mexicaines
Garantit 3 villes minimum avec filtrage intelligent
"""

import json
import logging
import os
from typing import Dict, List, Any, Tuple
from collections import defaultdict

# Configuration du logging
logger = logging.getLogger(__name__)

class MexicoResidentsAlgorithm:
    """
    Algorithme de recommandation de villes mexicaines
    Méthode scientifique avec zones géographiques et scoring culturel
    """

    def __init__(self):
        """Initialise l'algorithme avec les données JSON"""
        self.cities = []
        self.load_cities_data()

        # 🗺️ 10 ZONES GÉOGRAPHIQUES MEXICAINES
        self.mexico_zones = {
            'central_metropolis': {
                'cities': ['Mexico City', 'Guadalajara', 'Monterrey', 'Puebla', 'Toluca'],
                'description': 'Métropoles du centre industriel et financier'
            },
            'riviera_maya': {
                'cities': ['Cancún', 'Playa del Carmen', 'Tulum', 'Cozumel'],
                'description': 'Côte caraïbe - Paradis touristique et expat'
            },
            'pacific_coast': {
                'cities': ['Puerto Vallarta', 'Mazatlán', 'Acapulco'],
                'description': 'Côte pacifique - Plages et stations balnéaires'
            },
            'colonial_heritage': {
                'cities': ['San Miguel de Allende', 'Morelia', 'Querétaro', 'Guanajuato'],
                'description': 'Villes coloniales - Histoire et architecture'
            },
            'yucatan_peninsula': {
                'cities': ['Mérida', 'Campeche'],
                'description': 'Péninsule du Yucatan - Culture maya et sécurité'
            },
            'oaxaca_cultural': {
                'cities': ['Oaxaca'],
                'description': 'Culture indigène et gastronomie authentique'
            },
            'northern_business': {
                'cities': ['Tijuana', 'León'],
                'description': 'Nord industriel - Business et proximité USA'
            }
        }

    def load_cities_data(self):
        """Charge les données JSON des villes mexicaines"""
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            json_file = os.path.join(script_dir, 'data_v2', 'villes_mexico_residents.json')

            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.cities = data.get('cities', [])

            logger.info(f"🇲🇽 Loaded {len(self.cities)} Mexican cities")

        except Exception as e:
            logger.error(f"❌ Error loading Mexico cities data: {e}")
            self.cities = []

    def calculate_city_score(self, city: Dict[str, Any], preferences: Dict[str, Any]) -> Tuple[float, Dict[str, float]]:
        """
        NOUVEAU SYSTÈME DE SCORING MEXICO - Inspiré de l'Espagne
        Calcule le score d'une ville mexicaine avec normalisation 0-1

        Returns:
            tuple: (score_normalized, detail_scores)
        """
        detail_scores = {}
        total_weighted_score = 0
        max_possible_score = 0

        # Définition des critères avec leurs poids et scores max
        criteria_config = [
            ('lifestyle', 'mexico_lifestyle_priority', 9, self._score_lifestyle_preference),
            ('climate', 'mexico_climate_preference', 8, self._score_climate),
            ('work', 'mexico_work_environment', 8, self._score_work_environment),
            ('budget', 'mexico_budget_comfort', 7, self._score_budget_comfort),
            ('social', 'mexico_social_life', 7, self._score_social_life),
            ('transport', 'mexico_transport_priority', 6, self._score_transport),
            ('housing', 'mexico_housing_type', 6, self._score_housing_type),
            ('gastronomy', 'mexico_food_culture', 5, self._score_food_culture),
            ('pace', 'mexico_pace_of_life', 5, self._score_pace_of_life),
            ('safety', 'mexico_safety_priority', 8, self._score_safety_priority)
        ]

        try:
            for criterion_name, pref_key, weight, scoring_func in criteria_config:
                # Score normalisé 0-1 pour ce critère
                criterion_score = scoring_func(city, preferences.get(pref_key))

                # Score pondéré
                weighted_score = criterion_score * weight
                detail_scores[criterion_name] = weighted_score
                total_weighted_score += weighted_score
                max_possible_score += weight

        except Exception as e:
            logger.error(f"❌ Error calculating score for {city.get('name', 'Unknown')}: {e}")

        # Normalisation finale 0-1 (comme l'Espagne)
        normalized_score = total_weighted_score / max_possible_score if max_possible_score > 0 else 0

        return normalized_score, detail_scores

    def _score_lifestyle_preference(self, city: Dict, preference: str) -> float:
        """Score style de vie mexicain avec 100% mapping"""
        if not preference:
            return 0.5

        scores = {
            'cosmopolitan_city': {
                'Mexico City': 1.0, 'Guadalajara': 0.9, 'Monterrey': 0.9,
                'Puebla': 0.7, 'Toluca': 0.6, 'León': 0.6, 'Querétaro': 0.7,
                'Tijuana': 0.8, 'default': 0.3
            },
            'beach_paradise': {
                'Cancún': 1.0, 'Puerto Vallarta': 0.95, 'Playa del Carmen': 0.9,
                'Tulum': 0.9, 'Mazatlán': 0.8, 'Cozumel': 0.85, 'Acapulco': 0.7,
                'default': 0.2
            },
            'colonial_charm': {
                'San Miguel de Allende': 1.0, 'Oaxaca': 0.95, 'Morelia': 0.9,
                'Guanajuato': 0.9, 'Campeche': 0.8, 'Puebla': 0.8,
                'Querétaro': 0.7, 'default': 0.3
            },
            'expat_friendly': {
                'Playa del Carmen': 1.0, 'San Miguel de Allende': 0.95, 'Mérida': 0.9,
                'Puerto Vallarta': 0.9, 'Cancún': 0.8, 'Tulum': 0.8,
                'Mazatlán': 0.7, 'default': 0.4
            },
            'traditional_mexican': {
                'Oaxaca': 1.0, 'Morelia': 0.9, 'Puebla': 0.85, 'Campeche': 0.8,
                'Guanajuato': 0.8, 'Mérida': 0.75, 'default': 0.5
            }
        }

        city_name = city.get('name', '')
        return scores.get(preference, {}).get(city_name, scores.get(preference, {}).get('default', 0.5))

    def _score_climate(self, city: Dict, preference: str) -> float:
        """Score climat mexicain selon préférences - OPTIMISÉ"""
        if not preference or preference == 'climate_flexible':
            return 0.8  # Score plus généreux pour flexible

        climate_zones = {
            'tropical_coastal': ['Cancún', 'Playa del Carmen', 'Tulum', 'Cozumel', 'Puerto Vallarta', 'Mazatlán', 'Acapulco'],
            'desert_dry': ['Tijuana', 'León', 'Monterrey'],
            'temperate_highland': ['Mexico City', 'Guadalajara', 'Toluca', 'San Miguel de Allende', 'Morelia', 'Querétaro', 'Guanajuato'],
            'subtropical_warm': ['Mérida', 'Campeche', 'Oaxaca', 'Puebla']
        }

        city_name = city.get('name', '')

        for climate_type, cities in climate_zones.items():
            if climate_type == preference and city_name in cities:
                return 0.95  # Score excellent pour correspondance parfaite
            elif city_name in cities:
                # Bonus pour climats adjacents compatibles
                if preference == 'tropical_coastal' and climate_type == 'subtropical_warm':
                    return 0.7  # Mérida compatible avec tropical
                elif preference == 'temperate_highland' and climate_type == 'subtropical_warm':
                    return 0.6  # Oaxaca compatible avec tempéré
                else:
                    return 0.4

        return 0.6  # Score par défaut plus généreux

    def _score_work_environment(self, city: Dict, preference: str) -> float:
        """Score environnement professionnel mexicain"""
        if not preference or preference == 'flexible_opportunity':
            return 0.6

        work_scores = {
            'business_corporate': {
                'Mexico City': 1.0, 'Monterrey': 0.95, 'Guadalajara': 0.9,
                'Tijuana': 0.8, 'León': 0.7, 'Querétaro': 0.7,
                'default': 0.3
            },
            'remote_digital': {
                'Playa del Carmen': 1.0, 'Mérida': 0.9, 'San Miguel de Allende': 0.9,
                'Puerto Vallarta': 0.8, 'Tulum': 0.8, 'Oaxaca': 0.7,
                'default': 0.5
            },
            'tourism_hospitality': {
                'Cancún': 1.0, 'Puerto Vallarta': 0.95, 'Playa del Carmen': 0.9,
                'Tulum': 0.85, 'Mazatlán': 0.8, 'Acapulco': 0.7,
                'default': 0.3
            },
            'entrepreneurship': {
                'Mexico City': 0.9, 'Guadalajara': 0.85, 'Monterrey': 0.8,
                'Playa del Carmen': 0.7, 'Mérida': 0.6, 'default': 0.4
            }
        }

        city_name = city.get('name', '')
        return work_scores.get(preference, {}).get(city_name, work_scores.get(preference, {}).get('default', 0.5))

    def _score_budget_comfort(self, city: Dict, preference: str) -> float:
        """Score budget en pesos mexicains - OPTIMISÉ"""
        if not preference or preference == 'budget_flexible':
            return 0.8  # Score plus généreux pour flexible

        # Coût de la vie par ville (basé sur les données réelles) - RÉAJUSTÉ
        cost_levels = {
            'peso_economico': ['Oaxaca', 'Campeche', 'Mérida', 'Puebla', 'Morelia', 'León', 'Guanajuato'],
            'peso_medio': ['Guadalajara', 'Querétaro', 'Toluca', 'Mazatlán', 'Puerto Vallarta', 'Acapulco'],  # Ajout Puerto Vallarta
            'peso_alto': ['Mexico City', 'Monterrey', 'Tijuana', 'Playa del Carmen'],  # Playa del Carmen plus accessible
            'peso_lujo': ['Cancún', 'Tulum', 'San Miguel de Allende', 'Cozumel']
        }

        city_name = city.get('name', '')

        for budget_level, cities in cost_levels.items():
            if budget_level == preference and city_name in cities:
                return 0.95  # Score très élevé pour correspondance parfaite
            elif city_name in cities:
                # Score plus indulgent pour budget adjacent
                if preference == 'peso_medio' and budget_level in ['peso_economico', 'peso_alto']:
                    return 0.75  # Bon score pour budget proche
                elif preference == 'peso_alto' and budget_level == 'peso_medio':
                    return 0.80  # Puerto Vallarta accessible avec budget élevé
                else:
                    return 0.5

        return 0.6  # Score par défaut plus généreux

    def _score_social_life(self, city: Dict, preference: str) -> float:
        """Score vie sociale mexicaine"""
        if not preference or preference == 'mixed_social':
            return 0.6

        social_scores = {
            'nightlife_fiesta': {
                'Cancún': 1.0, 'Acapulco': 0.9, 'Puerto Vallarta': 0.85,
                'Mexico City': 0.8, 'Playa del Carmen': 0.8, 'Tijuana': 0.7,
                'default': 0.4
            },
            'cultural_explorer': {
                'Mexico City': 1.0, 'Oaxaca': 0.95, 'Guadalajara': 0.9,
                'Puebla': 0.8, 'Morelia': 0.75, 'Guanajuato': 0.8,
                'default': 0.5
            },
            'expat_network': {
                'San Miguel de Allende': 1.0, 'Playa del Carmen': 0.95, 'Mérida': 0.9,
                'Puerto Vallarta': 0.85, 'Tulum': 0.8, 'Cancún': 0.7,
                'default': 0.3
            },
            'family_oriented': {
                'Mérida': 1.0, 'Querétaro': 0.9, 'Morelia': 0.85,
                'Guadalajara': 0.8, 'Campeche': 0.8, 'León': 0.7,
                'default': 0.6
            }
        }

        city_name = city.get('name', '')
        return social_scores.get(preference, {}).get(city_name, social_scores.get(preference, {}).get('default', 0.5))

    def _score_transport(self, city: Dict, preference: str) -> float:
        """Score transport mexicain - OPTIMISÉ"""
        if not preference or preference == 'mixed_transport':
            return 0.8  # Score plus généreux pour flexible

        transport_scores = {
            'public_metro': {
                'Mexico City': 1.0, 'Guadalajara': 0.8, 'Monterrey': 0.7,
                'default': 0.3
            },
            'walking_cycling': {
                'San Miguel de Allende': 1.0, 'Playa del Carmen': 0.9, 'Oaxaca': 0.8,
                'Mérida': 0.8, 'Tulum': 0.9, 'Puerto Vallarta': 0.7,  # Bonus Puerto Vallarta
                'default': 0.5
            },
            'car_necessary': {
                'Tijuana': 0.9, 'León': 0.8, 'Toluca': 0.8,
                'Monterrey': 0.7, 'Guadalajara': 0.7, 'default': 0.7  # Plus généreux
            },
            'ride_sharing': {
                'Mexico City': 1.0, 'Guadalajara': 0.9, 'Monterrey': 0.8,
                'Cancún': 0.9, 'Puerto Vallarta': 0.8, 'Playa del Carmen': 0.8,  # Bonus zones touristiques
                'default': 0.6
            }
        }

        city_name = city.get('name', '')
        return transport_scores.get(preference, {}).get(city_name, transport_scores.get(preference, {}).get('default', 0.6))

    def _score_housing_type(self, city: Dict, preference: str) -> float:
        """Score type de logement mexicain - OPTIMISÉ"""
        if not preference or preference == 'flexible_housing':
            return 0.8  # Score plus généreux pour flexible

        housing_scores = {
            'city_center_apartment': {
                'Mexico City': 1.0, 'Guadalajara': 0.9, 'Monterrey': 0.8,
                'Puebla': 0.8, 'Oaxaca': 0.8, 'Puerto Vallarta': 0.7,  # Bonus Puerto Vallarta
                'default': 0.5
            },
            'beach_condo': {
                'Cancún': 1.0, 'Playa del Carmen': 0.95, 'Puerto Vallarta': 0.9,
                'Mazatlán': 0.85, 'Tulum': 0.85, 'Cozumel': 0.9,
                'default': 0.2
            },
            'colonial_house': {
                'San Miguel de Allende': 1.0, 'Morelia': 0.9, 'Oaxaca': 0.85,
                'Campeche': 0.85, 'Guanajuato': 0.85, 'Mérida': 0.8,
                'Puebla': 0.7,  # Bonus Puebla
                'default': 0.5
            },
            'gated_community': {
                'Mérida': 1.0, 'Querétaro': 0.9, 'Playa del Carmen': 0.85,
                'Puerto Vallarta': 0.85, 'Monterrey': 0.8, 'Cancún': 0.8,  # Bonus zones sûres
                'default': 0.6
            }
        }

        city_name = city.get('name', '')
        return housing_scores.get(preference, {}).get(city_name, housing_scores.get(preference, {}).get('default', 0.6))

    def _score_food_culture(self, city: Dict, preference: str) -> float:
        """Score culture gastronomique mexicaine"""
        if not preference or preference == 'food_flexible':
            return 0.7

        food_scores = {
            'street_food_authentic': {
                'Oaxaca': 1.0, 'Mexico City': 0.95, 'Puebla': 0.9,
                'Guadalajara': 0.85, 'Mérida': 0.8, 'default': 0.6
            },
            'fine_dining_modern': {
                'Mexico City': 1.0, 'Guadalajara': 0.8, 'Monterrey': 0.7,
                'Puerto Vallarta': 0.7, 'Cancún': 0.6, 'default': 0.3
            },
            'international_fusion': {
                'Playa del Carmen': 1.0, 'Cancún': 0.9, 'Puerto Vallarta': 0.8,
                'Mexico City': 0.8, 'San Miguel de Allende': 0.7, 'default': 0.4
            },
            'regional_specialties': {
                'Oaxaca': 1.0, 'Mérida': 0.9, 'Puebla': 0.85,
                'Campeche': 0.8, 'Morelia': 0.7, 'default': 0.6
            }
        }

        city_name = city.get('name', '')
        return food_scores.get(preference, {}).get(city_name, food_scores.get(preference, {}).get('default', 0.6))

    def _score_pace_of_life(self, city: Dict, preference: str) -> float:
        """Score rythme de vie mexicain"""
        if not preference or preference == 'flexible_pace':
            return 0.6

        pace_scores = {
            'dynamic_hustle': {
                'Mexico City': 1.0, 'Monterrey': 0.9, 'Guadalajara': 0.8,
                'Tijuana': 0.8, 'León': 0.7, 'default': 0.3
            },
            'relaxed_mañana': {
                'Tulum': 1.0, 'San Miguel de Allende': 0.9, 'Oaxaca': 0.85,
                'Mérida': 0.8, 'Campeche': 0.8, 'default': 0.6
            },
            'siesta_balance': {
                'Mérida': 1.0, 'Oaxaca': 0.9, 'Campeche': 0.85,
                'Morelia': 0.8, 'Guanajuato': 0.7, 'default': 0.7
            },
            'seasonal_rhythm': {
                'Puerto Vallarta': 1.0, 'Mazatlán': 0.9, 'Cancún': 0.8,
                'Acapulco': 0.8, 'Playa del Carmen': 0.7, 'default': 0.4
            }
        }

        city_name = city.get('name', '')
        return pace_scores.get(preference, {}).get(city_name, pace_scores.get(preference, {}).get('default', 0.5))

    def _score_safety_priority(self, city: Dict, preference: str) -> float:
        """Score sécurité mexicaine - critère essentiel"""
        if not preference or preference == 'flexible_security':
            return city.get('safety_score', 5) / 10.0  # Score de base

        # Index de sécurité réaliste par ville
        safety_index = {
            'maximum_security': {
                'Mérida': 1.0, 'Campeche': 0.95, 'Querétaro': 0.9,
                'San Miguel de Allende': 0.85, 'Puerto Vallarta': 0.8,
                'default': 0.3
            },
            'reasonable_caution': {
                'Guadalajara': 0.9, 'Monterrey': 0.8, 'Playa del Carmen': 0.85,
                'León': 0.8, 'Morelia': 0.7, 'default': 0.6
            },
            'local_knowledge': {
                'Mexico City': 0.8, 'Oaxaca': 0.75, 'Puebla': 0.7,
                'Guanajuato': 0.7, 'default': 0.6
            },
            'community_trust': {
                'San Miguel de Allende': 0.95, 'Mérida': 0.9, 'Playa del Carmen': 0.8,
                'Puerto Vallarta': 0.8, 'Tulum': 0.7, 'default': 0.5
            }
        }

        city_name = city.get('name', '')
        return safety_index.get(preference, {}).get(city_name, safety_index.get(preference, {}).get('default', 0.5))

    def get_recommendations(self, preferences: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Génère les recommandations de villes mexicaines
        Garantit 3 villes minimum avec filtrage intelligent

        Args:
            preferences: Dictionnaire des préférences utilisateur

        Returns:
            List[Dict]: Top 3 villes recommandées minimum
        """
        if not self.cities:
            logger.error("❌ No Mexican cities data available")
            return []

        try:
            # Calcul des scores pour toutes les villes
            scored_cities = []
            for city in self.cities:
                normalized_score, details = self.calculate_city_score(city, preferences)
                scored_cities.append({
                    'city': city,
                    'score': normalized_score,
                    'score_percentage': min(100, max(0, normalized_score * 100)),  # COMME L'ESPAGNE !
                    'details': details,
                    'zone': self._get_city_zone(city.get('name', ''))
                })

            # Tri par score décroissant
            scored_cities.sort(key=lambda x: x['score'], reverse=True)            # Filtrage intelligent pour garantir 3 villes
            recommendations = self._apply_intelligent_filtering(scored_cities, preferences)

            # Validation finale - garantit 3 villes minimum
            if len(recommendations) < 3:
                logger.warning(f"⚠️ Only {len(recommendations)} cities after filtering, adding top cities")
                while len(recommendations) < 3 and len(recommendations) < len(scored_cities):
                    for city_data in scored_cities:
                        if city_data not in recommendations:
                            recommendations.append(city_data)
                            break

            # Format final des résultats
            formatted_results = []
            for i, rec in enumerate(recommendations[:3]):  # Top 3 garanti
                city_data = rec['city']
                formatted_results.append({
                    'rank': i + 1,
                    'nom': city_data.get('name', ''),  # Utilisez 'nom' pour compatibilité frontend
                    'name': city_data.get('name', ''),  # Garde aussi 'name' pour compatibilité
                    'score': round(rec['score_percentage'], 2),  # SCORE EN POURCENTAGE !
                    'score_final': round(rec['score_percentage'], 2),  # Alias pour compatibilité
                    'score_percentage': round(rec['score_percentage'], 2),  # Format Espagne
                    'details': rec['details'],
                    'zone': rec['zone'],
                    'highlights': self._generate_highlights(city_data, preferences),
                    'points_forts': self._generate_highlights(city_data, preferences),  # Alias français
                    'why_recommended': self._generate_recommendation_reason(city_data, preferences, rec['details']),
                    'population': city_data.get('population', 'Non disponible'),
                    'cout_vie': city_data.get('cost_of_living', 5) * 1000,  # Conversion pour affichage
                    'emploi': city_data.get('employment_rate', None),
                    'region': city_data.get('region', ''),
                    'country': 'Mexico'
                })

            logger.info(f"🇲🇽 Generated {len(formatted_results)} Mexican city recommendations")
            return formatted_results

        except Exception as e:
            logger.error(f"❌ Error generating Mexico recommendations: {e}")
            return []

    def _get_city_zone(self, city_name: str) -> str:
        """Détermine la zone géographique d'une ville"""
        for zone, data in self.mexico_zones.items():
            if city_name in data['cities']:
                return zone
        return 'other'

    def _apply_intelligent_filtering(self, scored_cities: List[Dict], preferences: Dict) -> List[Dict]:
        """
        Applique un filtrage intelligent pour diversité géographique et culturelle
        Garantit 3 villes minimum
        """
        # Filtrage par environnement de travail - CRITIQUE
        work_pref = preferences.get('mexico_work_environment')
        if work_pref and work_pref != 'flexible_opportunity':
            work_filtered = []
            for city_data in scored_cities:
                work_score = self._score_work_environment(city_data['city'], work_pref)
                if work_score >= 0.6:  # Seuil adapté pour le Mexique
                    work_filtered.append(city_data)

            # GARANTIE 3 VILLES - Fix critique du pattern Espagne
            if len(work_filtered) >= 3:
                scored_cities = work_filtered

        # Filtrage par sécurité si priorité élevée
        safety_pref = preferences.get('mexico_safety_priority')
        if safety_pref == 'maximum_security':
            safety_filtered = []
            for city_data in scored_cities:
                safety_score = self._score_safety_priority(city_data['city'], safety_pref)
                if safety_score >= 0.7:  # Seuil élevé pour sécurité max
                    safety_filtered.append(city_data)

            if len(safety_filtered) >= 3:
                scored_cities = safety_filtered

        # Diversification géographique
        final_recommendations = []
        used_zones = set()

        for city_data in scored_cities:
            zone = city_data['zone']
            if len(final_recommendations) < 2:  # 2 premières sans restriction
                final_recommendations.append(city_data)
                used_zones.add(zone)
            elif zone not in used_zones or len(final_recommendations) >= 5:  # Diversité ou limite
                final_recommendations.append(city_data)
                used_zones.add(zone)

            if len(final_recommendations) >= 5:  # Maximum 5 recommandations
                break

        return final_recommendations

    def _generate_highlights(self, city: Dict, preferences: Dict) -> List[str]:
        """Génère les points forts d'une ville mexicaine"""
        highlights = []
        city_name = city.get('name', '')

        # Points forts spécifiques par ville
        city_highlights = {
            'Mexico City': ['🏛️ Capitale culturelle', '💼 Hub économique', '🚇 Métro développé'],
            'Guadalajara': ['🎵 Berceau des mariachis', '💻 Silicon Valley mexicain', '🌮 Tequila authentique'],
            'Monterrey': ['🏭 Centre industriel', '🏔️ Montagnes spectaculaires', '💰 Salaires élevés'],
            'Cancún': ['🏖️ Plages de rêve', '🌍 Hub expat', '✈️ Aéroport international'],
            'Puerto Vallarta': ['🌊 Baie pittoresque', '🎭 Scène artistique', '🏡 Communauté expat'],
            'Mérida': ['🛡️ Ville la plus sûre', '🏛️ Architecture coloniale', '🌡️ Climat tropical'],
            'San Miguel de Allende': ['🎨 Patrimoine UNESCO', '🌍 Expats américains', '🎭 Festivals culturels'],
            'Oaxaca': ['🍫 Capitale gastronomique', '🎨 Artisanat indigène', '🏛️ Architecture zapotèque'],
            'Playa del Carmen': ['🏖️ Plages caraïbes', '💻 Nomades numériques', '🌴 Style de vie détendu']
        }

        highlights = city_highlights.get(city_name, ['🇲🇽 Charme mexicain authentique'])

        # Ajouter des highlights basés sur les préférences
        budget_pref = preferences.get('mexico_budget_comfort')
        if budget_pref == 'peso_economico' and city.get('cost_of_living', 5) <= 4:
            highlights.append('💰 Coût de vie abordable')

        return highlights[:3]  # Maximum 3 highlights

    def _generate_recommendation_reason(self, city: Dict, preferences: Dict, details: Dict) -> str:
        """Génère la raison de recommandation personnalisée"""
        city_name = city.get('name', '')
        reasons = []

        # Raison basée sur le lifestyle
        lifestyle_pref = preferences.get('mexico_lifestyle_priority')
        lifestyle_reasons = {
            'cosmopolitan_city': f"Métropole dynamique parfaite pour l'urbain moderne",
            'beach_paradise': f"Paradis balnéaire avec plages de classe mondiale",
            'colonial_charm': f"Architecture coloniale et patrimoine historique unique",
            'expat_friendly': f"Communauté internationale accueillante et services adaptés",
            'traditional_mexican': f"Culture mexicaine authentique et traditions vivantes"
        }

        if lifestyle_pref in lifestyle_reasons:
            reasons.append(lifestyle_reasons[lifestyle_pref])

        # Raison basée sur le travail
        work_pref = preferences.get('mexico_work_environment')
        if work_pref == 'remote_digital' and details.get('work', 0) > 40:
            reasons.append("Ecosystem digital nomad développé")
        elif work_pref == 'business_corporate' and details.get('work', 0) > 45:
            reasons.append("Centre d'affaires majeur du Mexique")

        # Raison de sécurité
        safety_pref = preferences.get('mexico_safety_priority')
        if safety_pref == 'maximum_security' and details.get('safety', 0) > 35:
            reasons.append("Sécurité excellente pour tranquillité d'esprit")

        return ' • '.join(reasons) if reasons else f"Destination mexicaine adaptée à votre profil"

# Point d'entrée de l'algorithme
def get_mexico_recommendations(preferences: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Point d'entrée principal pour les recommandations mexicaines

    Args:
        preferences: Dictionnaire des préférences utilisateur

    Returns:
        List[Dict]: Recommandations de villes mexicaines
    """
    algorithm = MexicoResidentsAlgorithm()
    return algorithm.get_recommendations(preferences)

# Interface de test
if __name__ == "__main__":
    # Test avec profil exemple
    test_preferences = {
        'mexico_lifestyle_priority': 'expat_friendly',
        'mexico_climate_preference': 'tropical_coastal',
        'mexico_work_environment': 'remote_digital',
        'mexico_budget_comfort': 'peso_medio',
        'mexico_social_life': 'mixed_social',
        'mexico_transport_priority': 'mixed_transport',
        'mexico_housing_type': 'flexible_housing',
        'mexico_food_culture': 'food_flexible',
        'mexico_pace_of_life': 'flexible_pace',
        'mexico_safety_priority': 'reasonable_caution'
    }

    print("🇲🇽 MEXICO ALGORITHM TEST")
    print("=" * 50)

    recommendations = get_mexico_recommendations(test_preferences)

    for i, rec in enumerate(recommendations, 1):
        print(f"\n{i}. {rec['name']} (Score: {rec['score']})")
        print(f"   Zone: {rec['zone']}")
        print(f"   Raison: {rec['why_recommended']}")
        print(f"   Points forts: {' • '.join(rec['highlights'])}")
