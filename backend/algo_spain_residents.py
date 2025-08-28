#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🇪🇸 SPAIN RESIDENTS ALGORITHM
Hybrid approach: Smart recommendations for both Spanish residents and international expats
NO visa/language filtering - focus on lifestyle, climate, work-life balance, culture
"""

import json
import logging
from datetime import datetime
from typing import Dict, List, Tuple, Any, Optional
from pathlib import Path

class SpainResidentsAlgorithm:
    """
    Hybrid algorithm for Spanish city recommendations.
    Works intelligently for both:
    - Spanish residents looking to relocate within Spain
    - International expats considering Spanish cities

    Key features:
    - No visa/language barriers assumed
    - Climate-based filtering (hot sunny, mediterranean, continental, oceanic, tropical)
    - Lifestyle matching (coastal, urban, andalusian, islands, rural)
    - Work environment alignment (startup, corporate, remote, tourism, international)
    - Budget-conscious recommendations with EUR ranges
    - Spanish culture integration (siesta, gastronomy, social rhythms)
    """

    def __init__(self, cities_data_path: str):
        """Initialize the Spain Residents Algorithm"""
        self.version = "1.0.0"
        self.cities_data_path = cities_data_path
        self.cities_data = self.load_cities_data(cities_data_path)
        self.criteria_weights_base = self.get_base_criteria_weights_spain()

        # Climate zones for filtering (matching questions-data-es-residents.js)
        self.climate_zones = {
            "hot_sunny": ["sevilla", "cordoba", "murcia", "alicante", "elche"],
            "mediterranean_mild": ["barcelona", "valencia", "palma", "malaga", "hospitalet", "alicante", "elche"],
            "continental_seasons": ["madrid", "zaragoza", "valladolid"],
            "oceanic_fresh": ["bilbao", "santander", "vigo", "gijon", "vitoria"],
            "tropical_eternal": ["las_palmas"],
            "climate_flexible": []  # No filtering
        }

        # Lifestyle zones for pre-filtering (matching questions)
        self.lifestyle_zones = {
            "mediterranean_coastal": ["barcelona", "valencia", "alicante", "malaga", "palma"],
            "city_culture": ["madrid", "barcelona", "sevilla", "valencia", "bilbao"],  # NEW
            "andalusian_charm": ["sevilla", "cordoba", "granada", "malaga"],
            "basque_mountain": ["bilbao", "vitoria"],  # NEW (was basque_authentic)
            "island_paradise": ["palma", "las_palmas"]  # NEW (was islands_paradise)
        }

        # Work environment zones (matching questions-data-es-residents.js)
        self.work_zones = {
            "business_hub": ["madrid", "barcelona", "bilbao"],  # NEW (was corporate_international)
            "tech_startup": ["madrid", "barcelona", "valencia", "bilbao"],
            "tourism_service": ["palma", "las_palmas", "malaga", "sevilla", "alicante"],
            "remote_digital": ["valencia", "malaga", "palma", "las_palmas", "santander", "vigo"],
            "local_business": ["cordoba", "granada", "murcia", "valladolid", "gijon", "elche"]
        }

        # Budget zones (EUR monthly ranges - matching JS questions)
        self.budget_zones = {
            "budget_tight": ["murcia", "cordoba", "granada", "valladolid", "gijon", "elche", "vigo"],
            "budget_moderate": ["valencia", "zaragoza", "sevilla", "alicante", "santander", "vitoria"],
            "budget_comfortable": ["madrid", "barcelona", "bilbao", "malaga", "palma"],
            "budget_premium": ["madrid", "barcelona", "hospitalet"]
        }

        # Social life zones (matching JS questions)
        self.social_zones = {
            "nightlife_tapas": ["madrid", "barcelona", "sevilla", "valencia"],
            "cultural_festivals": ["sevilla", "granada", "cordoba", "valencia", "madrid"],
            "beach_social": ["valencia", "barcelona", "alicante", "palma", "malaga", "las_palmas"],
            "expat_community": ["madrid", "barcelona", "valencia", "palma", "malaga"],
            "family_oriented": ["vitoria", "santander", "valladolid", "gijon", "elche"]
        }

        # Transport zones (matching JS exactly)
        self.transport_zones = {
            "public_metro": ["madrid", "barcelona", "valencia", "sevilla", "bilbao"],  # NEW (was metro_efficient)
            "walking_cycling": ["sevilla", "valencia", "vitoria", "santander", "cordoba"],  # NEW (was bike_walkable)
            "car_flexibility": ["murcia", "elche", "cordoba", "valladolid", "gijon"],  # NEW (was car_essential)
            "mixed_transport": ["madrid", "barcelona", "valencia", "zaragoza"]  # NEW (was mixed_flexible)
        }

        # Housing zones (NEW - matching JS housing questions)
        self.housing_zones = {
            "city_center_piso": ["madrid", "barcelona", "sevilla", "valencia", "bilbao"],
            "coastal_apartment": ["valencia", "barcelona", "alicante", "malaga", "palma", "las_palmas"],
            "suburban_house": ["vitoria", "santander", "valladolid", "gijon", "zaragoza"],
            "historic_charm": ["sevilla", "cordoba", "granada", "toledo" if "toledo" in [c['id'] for c in self.cities_data] else "cordoba"]
        }

        # Gastronomy zones (NEW - matching JS gastronomy questions)
        self.gastronomy_zones = {
            "cosmopolitan_dining": ["madrid", "barcelona", "valencia", "bilbao"],
            "traditional_tapas": ["sevilla", "granada", "cordoba", "madrid"],
            "basque_cuisine": ["bilbao", "vitoria"],
            "coastal_seafood": ["valencia", "barcelona", "santander", "vigo", "las_palmas"]
        }

        # Rhythm zones (NEW - matching JS rhythm questions)
        self.rhythm_zones = {
            "fast_business": ["madrid", "barcelona", "bilbao"],
            "traditional_siesta": ["sevilla", "cordoba", "granada", "murcia"],
            "coastal_relaxed": ["valencia", "malaga", "alicante", "palma", "las_palmas"],
            "flexible_remote": ["valencia", "malaga", "palma", "santander", "vigo"]
        }

        # Seasonal zones (NEW - matching JS seasonal questions)
        self.seasonal_zones = {
            "perfect_summer": ["sevilla", "cordoba", "murcia", "alicante"],
            "mild_winter": ["las_palmas", "palma", "malaga", "alicante"],
            "spring_autumn": ["madrid", "barcelona", "valencia", "bilbao"],
            "year_round": ["las_palmas", "palma", "valencia"]
        }

        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.logger.info(f"🇪🇸 Spain Residents Algorithm v{self.version} initialized with {len(self.cities_data)} cities")

    def load_cities_data(self, file_path: str) -> List[Dict]:
        """Load cities data from JSON file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return data.get('cities', [])
        except FileNotFoundError:
            self.logger.error(f"Cities data file not found: {file_path}")
            return []
        except json.JSONDecodeError as e:
            self.logger.error(f"JSON decode error: {e}")
            return []

    def get_base_criteria_weights_spain(self) -> Dict[str, float]:
        """
        Base criteria weights optimized for Spanish lifestyle priorities.
        Balanced for both residents and expats, with Spanish-specific priorities.
        """
        return {
            "cost_of_living": 0.12,           # Important for budget planning
            "housing_affordability": 0.11,    # Housing accessibility crucial
            "climate_rating": 0.10,           # Climate is key for Spain choice
            "cultural_scene": 0.09,           # Rich Spanish culture priority
            "work_life_balance": 0.08,        # Spanish lifestyle balance
            "job_market": 0.08,               # Career opportunities
            "restaurant_diversity": 0.07,     # Gastronomy is Spanish passion
            "public_transport": 0.06,         # City mobility important
            "walkability": 0.06,              # Pedestrian-friendly cities
            "nightlife": 0.05,                # Spanish social life
            "healthcare_access": 0.05,        # Quality healthcare system
            "weather_consistency": 0.05,      # Stable weather appeal
            "remote_work_friendly": 0.05,     # Digital nomad friendly
            "tech_industry": 0.04,            # Growing tech scene
            "safety_security": 0.04,          # General safety level
            "university_access": 0.04,        # Education access
            "suburb_quality": 0.04,           # Residential quality
            "school_quality": 0.04,           # Family education
            "hospital_quality": 0.04,         # Medical facilities
            "natural_disaster_risk": 0.03,    # Safety from disasters
            "flood_risk": 0.03,               # Weather-related risks
            "heat_wave_risk": 0.03,           # Summer heat management
            "urban_density": 0.03,            # Space and density preference
            "car_dependency": 0.03,           # Transportation needs
            "income_tax_burden": 0.02,        # Tax considerations
            "local_tax": 0.02,                # Local taxation
            "council_tax": 0.02,              # Municipal taxes
            "spanish_language_score": 0.01    # Spanish language environment
        }

    def apply_climate_lifestyle_filters(self, cities_list: List[Dict], user_responses: Dict) -> List[Dict]:
        """
        Apply climate and lifestyle pre-filtering based on user preferences.
        This dramatically improves recommendation precision by filtering BEFORE scoring.
        """
        filtered_cities = cities_list.copy()

        # Climate filtering
        climate_pref = user_responses.get('spain_climate')
        if climate_pref and climate_pref != "climate_flexible":
            if climate_pref in self.climate_zones:
                climate_city_ids = self.climate_zones[climate_pref]
                filtered_cities = [city for city in filtered_cities if city['id'] in climate_city_ids]
                self.logger.info(f"🌡️ Climate filter '{climate_pref}': {len(filtered_cities)} cities remaining")

        # Lifestyle filtering
        lifestyle_pref = user_responses.get('spain_lifestyle')
        if lifestyle_pref and lifestyle_pref in self.lifestyle_zones:
            lifestyle_city_ids = self.lifestyle_zones[lifestyle_pref]
            # Keep cities that match lifestyle OR are very flexible
            lifestyle_filtered = [city for city in filtered_cities if city['id'] in lifestyle_city_ids]
            if len(lifestyle_filtered) >= 3:  # Ensure minimum recommendations
                filtered_cities = lifestyle_filtered
                self.logger.info(f"🏖️ Lifestyle filter '{lifestyle_pref}': {len(filtered_cities)} cities remaining")

        # Budget filtering (soft filter - expand if too restrictive)
        budget_pref = user_responses.get('spain_budget_comfort')
        if budget_pref and budget_pref in self.budget_zones:
            budget_city_ids = self.budget_zones[budget_pref]
            budget_filtered = [city for city in filtered_cities if city['id'] in budget_city_ids]

            if len(budget_filtered) >= 3:
                filtered_cities = budget_filtered
                self.logger.info(f"💰 Budget filter '{budget_pref}': {len(filtered_cities)} cities remaining")
            else:
                self.logger.info(f"💰 Budget filter too restrictive, keeping broader selection")

        # Work environment filtering
        work_pref = user_responses.get('spain_work_environment')
        if work_pref and work_pref in self.work_zones:
            work_city_ids = self.work_zones[work_pref]
            work_filtered = [city for city in filtered_cities if city['id'] in work_city_ids]

            if len(work_filtered) >= 3:  # Changé de 2 à 3 pour garantir 3 villes minimum
                filtered_cities = work_filtered
                self.logger.info(f"💼 Work filter '{work_pref}': {len(filtered_cities)} cities remaining")

        # Social life filtering (soft)
        social_pref = user_responses.get('spain_social_life')
        if social_pref and social_pref in self.social_zones:
            social_city_ids = self.social_zones[social_pref]
            social_filtered = [city for city in filtered_cities if city['id'] in social_city_ids]

            if len(social_filtered) >= 2:
                # Soft social filtering - mix filtered + some others
                all_social_ids = set(social_city_ids)
                enhanced_filtered = [city for city in filtered_cities
                                   if city['id'] in all_social_ids]
                if len(enhanced_filtered) >= 2:
                    filtered_cities = enhanced_filtered[:6]  # Keep top matches + some variety
                    self.logger.info(f"🎉 Social filter '{social_pref}': {len(filtered_cities)} cities remaining")

        # Transport filtering (NEW)
        transport_pref = user_responses.get('spain_transport')
        if transport_pref and transport_pref in self.transport_zones:
            transport_city_ids = self.transport_zones[transport_pref]
            transport_filtered = [city for city in filtered_cities if city['id'] in transport_city_ids]
            if len(transport_filtered) >= 2:
                filtered_cities = transport_filtered
                self.logger.info(f"🚇 Transport filter '{transport_pref}': {len(filtered_cities)} cities remaining")

        # Housing filtering (NEW)
        housing_pref = user_responses.get('spain_housing')
        if housing_pref and housing_pref in self.housing_zones:
            housing_city_ids = self.housing_zones[housing_pref]
            housing_filtered = [city for city in filtered_cities if city['id'] in housing_city_ids]
            if len(housing_filtered) >= 2:
                filtered_cities = housing_filtered
                self.logger.info(f"🏠 Housing filter '{housing_pref}': {len(filtered_cities)} cities remaining")

        # Gastronomy filtering (NEW)
        gastronomy_pref = user_responses.get('spain_gastronomy')
        if gastronomy_pref and gastronomy_pref in self.gastronomy_zones:
            gastronomy_city_ids = self.gastronomy_zones[gastronomy_pref]
            gastronomy_filtered = [city for city in filtered_cities if city['id'] in gastronomy_city_ids]
            if len(gastronomy_filtered) >= 2:
                filtered_cities = gastronomy_filtered
                self.logger.info(f"🍽️ Gastronomy filter '{gastronomy_pref}': {len(filtered_cities)} cities remaining")

        # Rhythm filtering (NEW)
        rhythm_pref = user_responses.get('spain_rhythm')
        if rhythm_pref and rhythm_pref in self.rhythm_zones:
            rhythm_city_ids = self.rhythm_zones[rhythm_pref]
            rhythm_filtered = [city for city in filtered_cities if city['id'] in rhythm_city_ids]
            if len(rhythm_filtered) >= 2:
                filtered_cities = rhythm_filtered
                self.logger.info(f"⏰ Rhythm filter '{rhythm_pref}': {len(filtered_cities)} cities remaining")

        # Seasonal filtering (NEW)
        seasonal_pref = user_responses.get('spain_seasonal')
        if seasonal_pref and seasonal_pref in self.seasonal_zones:
            seasonal_city_ids = self.seasonal_zones[seasonal_pref]
            seasonal_filtered = [city for city in filtered_cities if city['id'] in seasonal_city_ids]
            if len(seasonal_filtered) >= 2:
                filtered_cities = seasonal_filtered
                self.logger.info(f"🌞 Seasonal filter '{seasonal_pref}': {len(filtered_cities)} cities remaining")

        return filtered_cities

    def adapt_criteria_weights(self, base_weights: Dict[str, float], user_responses: Dict) -> Dict[str, float]:
        """
        Dynamically adapt criteria weights based on Spanish user preferences.
        Reflects Spanish priorities and lifestyle choices.
        """
        adapted_weights = base_weights.copy()

        # Lifestyle priorities adaptation
        lifestyle = user_responses.get('spain_lifestyle', '')
        if lifestyle == 'mediterranean_coastal':
            adapted_weights['climate_rating'] *= 1.4
            adapted_weights['beaches_coastline'] = adapted_weights.get('beaches_coastline', 0.03) * 2.0
            adapted_weights['tourism_attractions'] = adapted_weights.get('tourism_attractions', 0.02) * 1.5

        elif lifestyle == 'urban_cosmopolitan':
            adapted_weights['job_market'] *= 1.3
            adapted_weights['cultural_scene'] *= 1.3
            adapted_weights['public_transport'] *= 1.4
            adapted_weights['nightlife'] *= 1.3

        elif lifestyle == 'andalusian_charm':
            adapted_weights['cultural_scene'] *= 1.5
            adapted_weights['cost_of_living'] *= 1.3  # More affordable
            adapted_weights['climate_rating'] *= 1.2
            adapted_weights['work_life_balance'] *= 1.4

        # Professional environment adaptation
        work_env = user_responses.get('spain_work_environment', '')
        if work_env == 'tech_startup':
            adapted_weights['tech_industry'] *= 2.0
            adapted_weights['job_market'] *= 1.4
            adapted_weights['remote_work_friendly'] *= 1.3

        elif work_env == 'remote_digital':
            adapted_weights['remote_work_friendly'] *= 2.0
            adapted_weights['internet_connectivity'] = adapted_weights.get('internet_connectivity', 0.03) * 1.8
            adapted_weights['cost_of_living'] *= 1.3
            adapted_weights['climate_rating'] *= 1.2

        elif work_env == 'corporate_international':
            adapted_weights['job_market'] *= 1.5
            adapted_weights['business_networking'] = adapted_weights.get('business_networking', 0.03) * 1.8
            adapted_weights['international_connectivity'] = adapted_weights.get('international_connectivity', 0.03) * 1.6

        # Social preferences adaptation
        social = user_responses.get('spain_social_life', '')
        if social == 'nightlife_tapas':
            adapted_weights['restaurant_diversity'] *= 1.5
            adapted_weights['nightlife'] *= 1.8
            adapted_weights['cultural_scene'] *= 1.3
            adapted_weights['walkability'] *= 1.2

        elif social == 'cultural_festivals':
            adapted_weights['cultural_scene'] *= 1.8
            adapted_weights['arts_culture'] = adapted_weights.get('arts_culture', 0.03) * 1.6
            adapted_weights['tourism_attractions'] = adapted_weights.get('tourism_attractions', 0.02) * 1.4

        elif social == 'beach_social':
            adapted_weights['climate_rating'] *= 1.4
            adapted_weights['tourism_attractions'] = adapted_weights.get('tourism_attractions', 0.02) * 1.6
            adapted_weights['outdoor_activities'] = adapted_weights.get('outdoor_activities', 0.04) * 1.5

        # Transport preferences (updated to match JS values)
        transport = user_responses.get('spain_transport', '')
        if transport == 'public_metro':  # NEW (was metro_efficient)
            adapted_weights['public_transport'] *= 1.6
            adapted_weights['walkability'] *= 1.3
            adapted_weights['car_dependency'] *= 0.7

        elif transport == 'walking_cycling':  # NEW (was bike_walkable)
            adapted_weights['walkability'] *= 1.4
            adapted_weights['environmental_quality'] = adapted_weights.get('environmental_quality', 0.04) * 1.3
            adapted_weights['car_dependency'] *= 0.6

        elif transport == 'car_flexibility':  # NEW (was car_essential)
            adapted_weights['car_dependency'] *= 0.5  # Lower is better for car dependency
            adapted_weights['public_transport'] *= 0.8

        elif transport == 'mixed_transport':  # NEW
            adapted_weights['public_transport'] *= 1.2
            adapted_weights['walkability'] *= 1.1
            adapted_weights['car_dependency'] *= 0.8

        # Housing preferences (NEW - matching JS housing questions)
        housing = user_responses.get('spain_housing', '')
        if housing == 'city_center_piso':
            adapted_weights['housing_affordability'] *= 1.4
            adapted_weights['cultural_scene'] *= 1.3
        elif housing == 'coastal_apartment':
            adapted_weights['beaches_coastline'] = adapted_weights.get('beaches_coastline', 0.03) * 1.8
            adapted_weights['climate_rating'] *= 1.3
        elif housing == 'suburban_house':
            adapted_weights['family_friendliness'] = adapted_weights.get('family_friendliness', 0.05) * 1.4
            adapted_weights['cost_of_living'] *= 1.2
        elif housing == 'historic_charm':
            adapted_weights['cultural_scene'] *= 1.5
            adapted_weights['historical_sites'] = adapted_weights.get('historical_sites', 0.04) * 1.6

        # Gastronomy preferences (NEW - matching JS gastronomy questions)
        gastronomy = user_responses.get('spain_gastronomy', '')
        if gastronomy == 'cosmopolitan_dining':
            adapted_weights['restaurant_diversity'] *= 1.5
            adapted_weights['cultural_scene'] *= 1.2
        elif gastronomy == 'traditional_tapas':
            adapted_weights['cultural_authenticity'] = adapted_weights.get('cultural_authenticity', 0.05) * 1.6
            adapted_weights['restaurant_diversity'] *= 1.3
        elif gastronomy == 'basque_cuisine':
            adapted_weights['restaurant_diversity'] *= 1.4
            adapted_weights['cultural_uniqueness'] = adapted_weights.get('cultural_uniqueness', 0.04) * 1.5
        elif gastronomy == 'coastal_seafood':
            adapted_weights['beaches_coastline'] = adapted_weights.get('beaches_coastline', 0.03) * 1.4
            adapted_weights['restaurant_diversity'] *= 1.3

        # Rhythm preferences (NEW - matching JS rhythm questions)
        rhythm = user_responses.get('spain_rhythm', '')
        if rhythm == 'fast_business':
            adapted_weights['job_market'] *= 1.4
            adapted_weights['tech_industry'] = adapted_weights.get('tech_industry', 0.05) * 1.3
        elif rhythm == 'traditional_siesta':
            adapted_weights['work_life_balance'] *= 1.5
            adapted_weights['cultural_scene'] *= 1.3
        elif rhythm == 'coastal_relaxed':
            adapted_weights['work_life_balance'] *= 1.4
            adapted_weights['beaches_coastline'] = adapted_weights.get('beaches_coastline', 0.03) * 1.3
        elif rhythm == 'flexible_remote':
            adapted_weights['internet_speed'] = adapted_weights.get('internet_speed', 0.04) * 1.4
            adapted_weights['work_life_balance'] *= 1.2

        # Seasonal preferences (NEW - matching JS seasonal questions)
        seasonal = user_responses.get('spain_seasonal', '')
        if seasonal == 'perfect_summer':
            adapted_weights['climate_rating'] *= 1.6
            adapted_weights['sunshine_hours'] = adapted_weights.get('sunshine_hours', 0.03) * 1.5
        elif seasonal == 'mild_winter':
            adapted_weights['climate_rating'] *= 1.4
            adapted_weights['winter_temperature'] = adapted_weights.get('winter_temperature', 0.03) * 1.6
        elif seasonal == 'spring_autumn':
            adapted_weights['climate_rating'] *= 1.2
            adapted_weights['seasonal_variety'] = adapted_weights.get('seasonal_variety', 0.02) * 1.4
        elif seasonal == 'year_round':
            adapted_weights['climate_rating'] *= 1.5
            adapted_weights['weather_stability'] = adapted_weights.get('weather_stability', 0.03) * 1.4

        return adapted_weights

    def calculate_city_score(self, city: Dict, adapted_weights: Dict[str, float]) -> float:
        """
        Calculate weighted score for a Spanish city.
        Spanish-optimized scoring with cultural considerations.
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
        🇪🇸 Main recommendation method for Spanish cities.
        Returns top city matches with Spanish cultural context.

        STANDARDIZED API METHOD - Compatible with main.py integration
        """
        try:
            # Step 1: Apply intelligent pre-filtering
            filtered_cities = self.apply_climate_lifestyle_filters(self.cities_data, questionnaire_responses)

            if not filtered_cities:
                self.logger.warning("⚠️ No cities match filters, using all cities")
                filtered_cities = self.cities_data

            # Step 2: Adapt weights to Spanish user preferences
            adapted_weights = self.adapt_criteria_weights(self.criteria_weights_base, questionnaire_responses)

            # Step 3: Score each city
            scored_cities = []
            for city in filtered_cities:
                score = self.calculate_city_score(city, adapted_weights)
                scored_cities.append({
                    "city": city['name'],
                    "region": city['region'],
                    "population": city['population'],
                    "score": score,
                    "score_percentage": min(100, max(0, score * 100))  # Normalize to 0-100
                })

            # Step 4: Sort by score and get top recommendations
            scored_cities.sort(key=lambda x: x['score'], reverse=True)
            top_recommendations = scored_cities[:top_n]

            # Step 5: Add Spanish cultural insights
            for rec in top_recommendations:
                rec['insights'] = self.generate_spanish_insights(rec, questionnaire_responses)

            self.logger.info(f"🇪🇸 Generated {len(top_recommendations)} Spanish city recommendations")

            return {
                "status": "success",
                "recommendations": top_recommendations,
                "total_cities_analyzed": len(filtered_cities),
                "algorithm_version": self.version,
                "country": "Spain"
            }

        except Exception as e:
            self.logger.error(f"❌ Error generating Spanish recommendations: {e}")
            return {
                "status": "error",
                "error": str(e),
                "recommendations": [],
                "algorithm_version": self.version
            }

    def generate_spanish_insights(self, recommendation: Dict, user_responses: Dict) -> Dict:
        """Generate Spanish cultural insights for each recommendation"""
        city_name = recommendation['city'].lower()
        insights = {}

        # Spanish lifestyle insights
        if city_name in ['madrid']:
            insights['lifestyle'] = "Vie urbaine intense avec rythme madrilène authentique"
            insights['culture'] = "Capital culturel avec musées, théâtres et vie nocturne légendaire"
        elif city_name in ['barcelona']:
            insights['lifestyle'] = "Cosmopolite méditerranéen avec culture catalane unique"
            insights['culture'] = "Art, architecture Gaudí et plages urbaines"
        elif city_name in ['sevilla', 'córdoba', 'granada']:
            insights['lifestyle'] = "Charme andalou avec siesta et rythme traditionnel"
            insights['culture'] = "Flamenco, architecture mauresque et gastronomie authentique"
        elif city_name in ['valencia']:
            insights['lifestyle'] = "Équilibre parfait entre mer, culture et modernité"
            insights['culture'] = "Paella originale, Cité des Arts et plages proches"
        elif city_name in ['bilbao', 'vitoria']:
            insights['lifestyle'] = "Qualité de vie basque avec climat océanique"
            insights['culture'] = "Culture basque unique, gastronomie raffinée"
        elif city_name in ['palma', 'las palmas']:
            insights['lifestyle'] = "Paradise insulaire avec climat tropical/méditerranéen"
            insights['culture'] = "Mix culture espagnole et influence internationale"

        # Climate insights based on user preferences
        climate_pref = user_responses.get('spain_climate', '')
        if climate_pref == 'hot_sunny' and city_name in ['sevilla', 'córdoba']:
            insights['climate'] = "Parfait pour amateurs de chaleur intense et soleil constant"
        elif climate_pref == 'mediterranean_mild' and city_name in ['barcelona', 'valencia']:
            insights['climate'] = "Climat méditerranéen idéal toute l'année"
        elif climate_pref == 'oceanic_fresh' and city_name in ['bilbao', 'santander']:
            insights['climate'] = "Fraîcheur océanique, parfait pour éviter la chaleur"

        return insights

    # Legacy compatibility methods for older integration patterns
    def get_top_recommendations_spain(self, responses: Dict, top_n: int = 3):
        """Legacy method name for backward compatibility"""
        return self.get_recommendations(responses, top_n)

    def get_health_check(self) -> Dict:
        """Health check method for API compatibility"""
        try:
            return {
                'status': 'healthy',
                'algorithm_version': self.version,
                'cities_loaded': len(self.cities_data),
                'country': 'Spain',
                'zones_available': {
                    'climate_zones': len(self.climate_zones),
                    'lifestyle_zones': len(self.lifestyle_zones),
                    'budget_zones': len(self.budget_zones),
                    'work_zones': len(self.work_zones),
                    'social_zones': len(self.social_zones),
                    'transport_zones': len(self.transport_zones),
                    'housing_zones': len(self.housing_zones),
                    'gastronomy_zones': len(self.gastronomy_zones),
                    'rhythm_zones': len(self.rhythm_zones),
                    'seasonal_zones': len(self.seasonal_zones)
                },
                'last_check': datetime.now().isoformat()
            }
        except Exception as e:
            return {
                'status': 'unhealthy',
                'error': str(e),
                'cities_loaded': 0,
                'algorithm_version': self.version
            }

# Additional utility functions for Spanish-specific features

def get_spanish_cultural_score(city_id: str) -> Dict[str, float]:
    """Return Spanish cultural scores for specific cities"""
    cultural_profiles = {
        "madrid": {"flamenco": 0.8, "tapas": 0.9, "nightlife": 0.95, "museums": 1.0},
        "barcelona": {"modernist": 1.0, "mediterranean": 0.9, "international": 0.95, "beaches": 0.8},
        "sevilla": {"flamenco": 1.0, "moorish": 0.95, "traditional": 1.0, "heat": 0.9},
        "valencia": {"paella": 1.0, "modern": 0.8, "coastal": 0.9, "festivals": 0.85},
        "bilbao": {"basque": 1.0, "gastronomy": 0.95, "mountains": 0.8, "industry": 0.7}
    }

    return cultural_profiles.get(city_id, {})

def validate_spanish_questionnaire(responses: Dict) -> Dict:
    """Validate and clean Spanish questionnaire responses"""
    required_fields = [
        'spain_lifestyle', 'spain_climate', 'spain_work_environment',
        'spain_budget', 'spain_social_life'
    ]

    validation_result = {
        "valid": True,
        "missing_fields": [],
        "warnings": []
    }

    for field in required_fields:
        if field not in responses:
            validation_result["missing_fields"].append(field)
            validation_result["valid"] = False

    return validation_result
