#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🇦🇺 AUSTRALIA RESIDENTS ALGORITHM
Hybrid approach: Smart recommendations for both Australian residents and international expats
NO visa/language filtering - focus on lifestyle, climate, work preferences matching
"""

import json
from typing import Dict, List, Tuple, Any, Optional
import logging
from pathlib import Path

class AustraliaResidentsAlgorithm:
    """
    Hybrid algorithm for Australian city recommendations.
    Works intelligently for both:
    - Australian residents looking to relocate within Australia
    - International expats considering Australian cities

    Key features:
    - No visa/language barriers assumed
    - Climate-based filtering (tropical, temperate, mediterranean, cooler)
    - Lifestyle matching (beach, city, outdoor, cultural, regional)
    - Work environment alignment (corporate, tech, government, tourism, remote, mining)
    - Budget-conscious recommendations with AUD ranges
    """

    def __init__(self, cities_data_path: str):
        """Initialize the Australia Residents Algorithm"""
        self.version = "1.0.0"
        self.cities_data_path = cities_data_path
        self.cities_data = self.load_cities_data(cities_data_path)
        self.criteria_weights_base = self.get_base_criteria_weights_australia()

        # Climate zones for filtering
        self.climate_zones = {
            "tropical_warm": ["darwin", "cairns", "townsville", "gold_coast"],
            "temperate_mild": ["melbourne", "adelaide", "hobart", "canberra", "geelong"],
            "mediterranean_dry": ["perth"],
            "cooler_alpine": ["hobart", "canberra", "toowoomba"],
            "climate_flexible": []  # No filtering
        }

        # Lifestyle zones for pre-filtering
        self.lifestyle_zones = {
            "beach_coastal": ["sydney", "gold_coast", "perth", "newcastle", "wollongong", "cairns", "townsville", "geelong"],
            "city_business": ["sydney", "melbourne", "brisbane", "perth", "adelaide", "canberra"],
            "outdoor_adventure": ["darwin", "cairns", "hobart", "townsville", "toowoomba"],
            "arts_culture": ["melbourne", "sydney", "adelaide", "canberra", "hobart"],
            "relaxed_regional": ["toowoomba", "geelong", "wollongong", "newcastle", "townsville"]
        }

        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.logger.info(f"🇦🇺 Australia Residents Algorithm v{self.version} initialized with {len(self.cities_data)} cities")

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

    def get_base_criteria_weights_australia(self) -> Dict[str, float]:
        """
        Base criteria weights optimized for Australian lifestyle priorities.
        Balanced for both residents and expats, with Australian-specific priorities.
        """
        return {
            "cost_of_living": 0.12,           # Important for budget planning
            "job_opportunities": 0.11,         # Career prospects
            "housing_affordability": 0.10,    # Housing is major concern in Australia
            "climate_weather": 0.09,           # Climate is key for Australia choices
            "outdoor_activities": 0.08,        # Outdoor lifestyle is Australian priority
            "beaches_coastline": 0.07,         # Coastal access highly valued
            "work_life_balance": 0.07,         # Australian work culture priority
            "safety_security": 0.06,           # Generally high across Australia
            "healthcare_quality": 0.06,        # Medicare system consideration
            "public_transport": 0.05,          # Varies greatly by city
            "cultural_diversity": 0.05,        # Multicultural appeal
            "food_scene": 0.04,               # Coffee culture, dining
            "education_quality": 0.04,         # Schools and unis
            "environmental_quality": 0.04,     # Clean air, green spaces
            "nightlife_entertainment": 0.04,   # Social scene
            "family_friendliness": 0.04,       # Family considerations
            "wildlife_nature": 0.04,          # Unique Australian wildlife
            "internet_connectivity": 0.03,     # Digital infrastructure
            "startup_ecosystem": 0.03,         # Innovation scene
            "international_connectivity": 0.03, # Flight connections
            "sports_facilities": 0.03,         # Active lifestyle
            "business_networking": 0.03,       # Professional opportunities
            "arts_culture": 0.03,             # Cultural scene
            "shopping_retail": 0.02,          # Consumer conveniences
            "student_life": 0.02,             # University experience
            "retirement_suitability": 0.02,   # Senior living
            "tourism_attractions": 0.02       # Local experiences
        }

    def apply_hybrid_filters(self, cities_list: List[Dict], user_profile: Dict) -> List[Dict]:
        """
        Apply intelligent pre-filtering based on climate and lifestyle preferences.
        Hybrid approach: Doesn't exclude too aggressively, allows flexibility.
        """
        filtered_cities = cities_list.copy()

        # Climate filtering (if specific preference)
        climate_pref = user_profile.get('australia_climate_preference')
        if climate_pref and climate_pref != 'climate_flexible':
            climate_cities = self.climate_zones.get(climate_pref, [])
            if climate_cities:
                # Keep cities in preferred climate zones, but also include flexible options
                filtered_cities = [city for city in filtered_cities
                                 if city['id'] in climate_cities or
                                    city['scores'].get('climate_weather', 0) > 0.8]

        # Lifestyle pre-filtering (soft filter - increases weight rather than excludes)
        lifestyle_pref = user_profile.get('australia_lifestyle_priority')
        if lifestyle_pref:
            preferred_cities = self.lifestyle_zones.get(lifestyle_pref, [])
            # Mark preferred cities for bonus scoring later
            for city in filtered_cities:
                city['_lifestyle_bonus'] = 1.1 if city['id'] in preferred_cities else 1.0

        # Budget filtering (exclude cities that are clearly out of range)
        budget_pref = user_profile.get('australia_budget_range')
        if budget_pref:
            budget_thresholds = {
                'budget_tight': 0.6,      # Need affordable cities
                'budget_moderate': 0.4,   # Mid-range acceptable
                'budget_comfortable': 0.2, # Can handle more expensive
                'budget_premium': 0.0     # No budget constraints
            }

            min_affordability = budget_thresholds.get(budget_pref, 0.0)
            filtered_cities = [city for city in filtered_cities
                             if city['scores'].get('cost_of_living', 0) >= min_affordability]

        self.logger.info(f"🇦🇺 Hybrid filtering: {len(cities_list)} → {len(filtered_cities)} cities")
        return filtered_cities

    def adapt_weights_to_user_profile(self, base_weights: Dict[str, float], user_profile: Dict) -> Dict[str, float]:
        """
        Adapt criteria weights based on user responses.
        Intelligent weight adjustment for hybrid resident/expat approach.
        """
        adapted_weights = base_weights.copy()

        # Lifestyle priority adjustments
        lifestyle_pref = user_profile.get('australia_lifestyle_priority')
        if lifestyle_pref == 'beach_coastal':
            adapted_weights['beaches_coastline'] *= 2.0
            adapted_weights['outdoor_activities'] *= 1.5
            adapted_weights['climate_weather'] *= 1.3
        elif lifestyle_pref == 'city_business':
            adapted_weights['job_opportunities'] *= 1.8
            adapted_weights['business_networking'] *= 1.6
            adapted_weights['public_transport'] *= 1.4
            adapted_weights['nightlife_entertainment'] *= 1.3
        elif lifestyle_pref == 'outdoor_adventure':
            adapted_weights['outdoor_activities'] *= 2.2
            adapted_weights['wildlife_nature'] *= 1.8
            adapted_weights['environmental_quality'] *= 1.5
        elif lifestyle_pref == 'arts_culture':
            adapted_weights['arts_culture'] *= 2.0
            adapted_weights['cultural_diversity'] *= 1.6
            adapted_weights['food_scene'] *= 1.4
        elif lifestyle_pref == 'relaxed_regional':
            adapted_weights['work_life_balance'] *= 1.8
            adapted_weights['cost_of_living'] *= 1.5
            adapted_weights['family_friendliness'] *= 1.4

        # Climate importance
        climate_pref = user_profile.get('australia_climate_preference')
        if climate_pref and climate_pref != 'climate_flexible':
            adapted_weights['climate_weather'] *= 1.6

        # Work environment adjustments
        work_env = user_profile.get('australia_work_environment')
        if work_env == 'corporate_cbd':
            adapted_weights['job_opportunities'] *= 1.7
            adapted_weights['business_networking'] *= 1.5
            adapted_weights['public_transport'] *= 1.3
        elif work_env == 'tech_startup':
            adapted_weights['startup_ecosystem'] *= 2.0
            adapted_weights['internet_connectivity'] *= 1.5
        elif work_env == 'government_public':
            adapted_weights['job_opportunities'] *= 1.4
            adapted_weights['work_life_balance'] *= 1.3
        elif work_env == 'tourism_hospitality':
            adapted_weights['tourism_attractions'] *= 1.8
            adapted_weights['beaches_coastline'] *= 1.4
            adapted_weights['cultural_diversity'] *= 1.3
        elif work_env == 'remote_flexible':
            adapted_weights['internet_connectivity'] *= 1.6
            adapted_weights['cost_of_living'] *= 1.4
            adapted_weights['work_life_balance'] *= 1.3
        elif work_env == 'mining_resources':
            adapted_weights['job_opportunities'] *= 1.5
            adapted_weights['cost_of_living'] *= 1.3  # FIFO lifestyle consideration

        # Budget considerations
        budget_pref = user_profile.get('australia_budget_range')
        if budget_pref in ['budget_tight', 'budget_moderate']:
            adapted_weights['cost_of_living'] *= 1.8
            adapted_weights['housing_affordability'] *= 1.6

        # Housing preferences
        housing_pref = user_profile.get('australia_housing_preference')
        if housing_pref == 'apartment_city':
            adapted_weights['public_transport'] *= 1.4
            adapted_weights['nightlife_entertainment'] *= 1.3
        elif housing_pref == 'house_suburbs':
            adapted_weights['family_friendliness'] *= 1.5
            adapted_weights['safety_security'] *= 1.3
        elif housing_pref == 'waterfront_premium':
            adapted_weights['beaches_coastline'] *= 1.8
            adapted_weights['tourism_attractions'] *= 1.3

        # Transport priority
        transport_pref = user_profile.get('australia_transport_priority')
        if transport_pref == 'transport_essential':
            adapted_weights['public_transport'] *= 2.0
        elif transport_pref == 'cycling_walkable':
            adapted_weights['environmental_quality'] *= 1.4
            adapted_weights['work_life_balance'] *= 1.3

        # Social scene preferences
        social_pref = user_profile.get('australia_social_scene')
        if social_pref == 'nightlife_vibrant':
            adapted_weights['nightlife_entertainment'] *= 1.8
            adapted_weights['cultural_diversity'] *= 1.3
        elif social_pref == 'cafe_culture':
            adapted_weights['food_scene'] *= 1.6
            adapted_weights['arts_culture'] *= 1.3
        elif social_pref == 'sports_community':
            adapted_weights['sports_facilities'] *= 1.7
        elif social_pref == 'multicultural_diverse':
            adapted_weights['cultural_diversity'] *= 1.8
            adapted_weights['food_scene'] *= 1.4
        elif social_pref == 'quiet_peaceful':
            adapted_weights['safety_security'] *= 1.4
            adapted_weights['environmental_quality'] *= 1.3

        # Nature access importance
        nature_pref = user_profile.get('australia_nature_access')
        if nature_pref == 'nature_essential':
            adapted_weights['wildlife_nature'] *= 2.0
            adapted_weights['outdoor_activities'] *= 1.8
            adapted_weights['environmental_quality'] *= 1.5
        elif nature_pref == 'beaches_priority':
            adapted_weights['beaches_coastline'] *= 2.2
            adapted_weights['outdoor_activities'] *= 1.5
        elif nature_pref == 'urban_focus':
            adapted_weights['nightlife_entertainment'] *= 1.4
            adapted_weights['cultural_diversity'] *= 1.3
            adapted_weights['public_transport'] *= 1.3

        # Family situation adjustments
        family_situation = user_profile.get('australia_family_situation')
        if family_situation == 'family_kids':
            adapted_weights['family_friendliness'] *= 2.0
            adapted_weights['education_quality'] *= 1.8
            adapted_weights['safety_security'] *= 1.5
        elif family_situation == 'couple_no_kids':
            adapted_weights['nightlife_entertainment'] *= 1.4
            adapted_weights['food_scene'] *= 1.3
        elif family_situation in ['single_social', 'single_independent']:
            adapted_weights['nightlife_entertainment'] *= 1.3
            adapted_weights['cultural_diversity'] *= 1.3
        elif family_situation == 'empty_nesters':
            adapted_weights['retirement_suitability'] *= 1.8
            adapted_weights['healthcare_quality'] *= 1.5
            adapted_weights['arts_culture'] *= 1.4

        # Education priority
        education_pref = user_profile.get('australia_education_priority')
        if education_pref == 'education_critical':
            adapted_weights['education_quality'] *= 2.0
            adapted_weights['family_friendliness'] *= 1.4
        elif education_pref == 'university_access':
            adapted_weights['education_quality'] *= 1.6
            adapted_weights['student_life'] *= 1.8
        elif education_pref == 'training_skills':
            adapted_weights['job_opportunities'] *= 1.4

        # Connectivity needs
        connectivity_pref = user_profile.get('australia_connectivity_need')
        if connectivity_pref == 'international_hub':
            adapted_weights['international_connectivity'] *= 2.0
            adapted_weights['cultural_diversity'] *= 1.4
        elif connectivity_pref == 'domestic_travel':
            adapted_weights['tourism_attractions'] *= 1.3

        # Career stage adjustments
        career_stage = user_profile.get('australia_career_stage')
        if career_stage == 'career_building':
            adapted_weights['job_opportunities'] *= 1.7
            adapted_weights['business_networking'] *= 1.5
        elif career_stage == 'career_established':
            adapted_weights['work_life_balance'] *= 1.4
            adapted_weights['cultural_diversity'] *= 1.3
        elif career_stage == 'entrepreneur_startup':
            adapted_weights['startup_ecosystem'] *= 2.0
            adapted_weights['business_networking'] *= 1.6
        elif career_stage == 'work_life_balance':
            adapted_weights['work_life_balance'] *= 2.0
            adapted_weights['outdoor_activities'] *= 1.5
        elif career_stage == 'semi_retired':
            adapted_weights['retirement_suitability'] *= 1.8
            adapted_weights['healthcare_quality'] *= 1.4
        elif career_stage == 'student_studying':
            adapted_weights['student_life'] *= 2.0
            adapted_weights['education_quality'] *= 1.6
            adapted_weights['cost_of_living'] *= 1.5

        # Normalize weights to sum to 1
        total_weight = sum(adapted_weights.values())
        for criteria in adapted_weights:
            adapted_weights[criteria] = adapted_weights[criteria] / total_weight

        return adapted_weights

    def calculate_city_score(self, city: Dict, adapted_weights: Dict[str, float]) -> float:
        """
        Calculate weighted score for a city based on adapted weights.
        Includes lifestyle bonus from filtering.
        """
        total_score = 0.0

        for criteria, weight in adapted_weights.items():
            city_score = city['scores'].get(criteria, 0.0)
            total_score += city_score * weight

        # Apply lifestyle bonus if applicable
        lifestyle_bonus = city.get('_lifestyle_bonus', 1.0)
        total_score *= lifestyle_bonus

        return min(total_score, 1.0)  # Cap at 1.0

    def get_recommendations(self, questionnaire_responses: Dict, top_n: int = 3) -> Dict:
        """
        Main method to get city recommendations.
        Standardized interface for main.py integration.

        Returns: {"status": "success", "recommendations": [...]}
        """
        try:
            self.logger.info(f"🇦🇺 Processing Australia recommendations request")

            # Apply hybrid filtering (climate, lifestyle, budget)
            filtered_cities = self.apply_hybrid_filters(self.cities_data, questionnaire_responses)

            if not filtered_cities:
                return {
                    "status": "error",
                    "message": "No cities match your criteria. Please adjust your preferences.",
                    "recommendations": []
                }

            # Adapt weights based on user profile
            adapted_weights = self.adapt_weights_to_user_profile(
                self.criteria_weights_base,
                questionnaire_responses
            )

            # Calculate scores for filtered cities
            scored_cities = []
            for city in filtered_cities:
                score = self.calculate_city_score(city, adapted_weights)
                scored_cities.append({
                    'city': city['name'],
                    'state': city['state'],
                    'score_percentage': score * 100,
                    'population': city['population'],
                    'coordinates': city['coordinates'],
                    'top_criteria': self.get_top_criteria_for_city(city, adapted_weights)
                })

            # Sort by score and return top recommendations
            scored_cities.sort(key=lambda x: x['score_percentage'], reverse=True)
            top_recommendations = scored_cities[:top_n]

            self.logger.info(f"🇦🇺 Returning {len(top_recommendations)} Australia recommendations")

            return {
                "status": "success",
                "recommendations": top_recommendations,
                "total_cities_analyzed": len(filtered_cities),
                "algorithm_version": self.version,
                "approach": "hybrid_residents_expats"
            }

        except Exception as e:
            self.logger.error(f"Error in Australia recommendations: {str(e)}")
            return {
                "status": "error",
                "message": f"An error occurred: {str(e)}",
                "recommendations": []
            }

    def get_top_criteria_for_city(self, city: Dict, weights: Dict[str, float], top_n: int = 3) -> List[Dict]:
        """Get the top criteria that make this city appealing"""
        criteria_scores = []

        for criteria, weight in weights.items():
            city_score = city['scores'].get(criteria, 0.0)
            weighted_contribution = city_score * weight

            criteria_scores.append({
                'criteria': criteria.replace('_', ' ').title(),
                'score': round(city_score * 100, 1),
                'contribution': round(weighted_contribution * 100, 2)
            })

        # Sort by contribution and return top criteria
        criteria_scores.sort(key=lambda x: x['contribution'], reverse=True)
        return criteria_scores[:top_n]

    def get_health_check(self) -> Dict:
        """Health check for the algorithm"""
        return {
            "status": "healthy",
            "cities_loaded": len(self.cities_data),
            "algorithm_version": self.version,
            "approach": "hybrid_residents_expats",
            "features": [
                "climate_filtering",
                "lifestyle_matching",
                "budget_awareness",
                "work_environment_alignment",
                "no_visa_language_barriers"
            ]
        }

# Test the algorithm if run directly
if __name__ == "__main__":
    # Test with sample data
    test_cities_path = "/var/www/Revolutionnary/platform/backend/data_v2/villes_australia_residents.json"
    algo = AustraliaResidentsAlgorithm(test_cities_path)

    # Test profile - Beach lifestyle, temperate climate, tech work
    test_profile = {
        "australia_lifestyle_priority": "beach_coastal",
        "australia_climate_preference": "temperate_mild",
        "australia_work_environment": "tech_startup",
        "australia_budget_range": "budget_comfortable",
        "australia_housing_preference": "apartment_city",
        "australia_transport_priority": "transport_helpful",
        "australia_social_scene": "cafe_culture",
        "australia_nature_access": "beaches_priority",
        "australia_family_situation": "couple_no_kids",
        "australia_education_priority": "education_moderate",
        "australia_connectivity_need": "international_hub",
        "australia_career_stage": "career_building"
    }

    result = algo.get_recommendations(test_profile)
    print(f"🇦🇺 Australia Algorithm Test Result:")
    print(f"Status: {result['status']}")
    if result['status'] == 'success':
        for i, rec in enumerate(result['recommendations'][:3], 1):
            print(f"{i}. {rec['city']}, {rec['state']} - {rec['score_percentage']:.1f}%")

    # Health check test
    health = algo.get_health_check()
    print(f"\nHealth Check: {health}")
