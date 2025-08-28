#!/usr/bin/env python3
"""
Quick test to verify Thailand algorithm strengths mapping fix
"""

from algo_thailand_residents import ThailandResidentsAlgorithm

# Test responses
test_responses = {
    'thailand_region_preference': 'region_flexible',
    'thailand_main_priority': 'cuisine_culture',
    'business_activities': 'digital_nomad',
    'climate_preference': 'tropical_hot'
}

print("=== Quick Thailand Algorithm Test ===")

# Initialize algorithm
algo = ThailandResidentsAlgorithm('data_v2/villes_thailand_residents.json')

# Get recommendations
result = algo.get_recommendations(test_responses)

if result['status'] == 'success':
    print(f"✓ Success! {len(result['recommendations'])} recommendations")

    # Check first recommendation
    first_rec = result['recommendations'][0]
    print(f"\n🏆 Top recommendation: {first_rec['city']} ({first_rec['score_percentage']}%)")

    # Check strengths key
    if 'strengths' in first_rec:
        print(f"✓ Has 'strengths' key: {len(first_rec['strengths'])} strengths")
        print(f"📋 Strengths: {first_rec['strengths']}")
    else:
        print("❌ Missing 'strengths' key")
        print(f"Available keys: {list(first_rec.keys())}")

    # Check for old key
    if 'top_strengths' in first_rec:
        print("⚠️ Still has old 'top_strengths' key")
else:
    print(f"❌ Error: {result}")
