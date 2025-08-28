/**
 * 🇫🇷 QUESTIONS-DATA-FR-RESIDENTS.JS - QUESTIONNAIRE RELOCATION DOMESTIQUE FRANCE
 * ================================================================================
 * 10 questions OPTIMALES pour Français cherchant nouvelle ville française
 * Author: Revolutionary Team | Version: 1.0.0 - France Domestic Focus
 * OBJECTIF: Recommandations basées sur profils réels des relocations françaises
 */

// 🏠 QUESTIONS CENTRÉES BESOINS RELOCATION FRANCE
window.QUESTIONS_DATA_FRANCE = {
    "france_residents": [

        // ===== 1. MOTIVATION/PRIORITÉ PRINCIPALE - ACCROCHE ÉMOTIONNELLE =====
        {
            "id": "france_main_priority",
            "title": "🎯 Qu'est-ce qui vous pousse VRAIMENT à changer de ville ?",
            "title_en": "🎯 What REALLY drives you to change cities?",
            "category": "life_priority",
            "type": "single",
            "description": "Identifie ce qui compte vraiment pour votre nouveau départ",
            "description_en": "Identifies what truly matters for your new beginning",
            "weight": 9,
            "options": [
                {
                    "value": "career_growth",
                    "icon": "🏃‍♂️",
                    "title": "Saisir une opportunité pro/études",
                    "title_en": "Seize a professional/study opportunity",
                    "description": "Emploi, formation, évolution professionnelle",
                    "description_en": "Job, training, professional development",
                    "boost_criteria": ["job_market", "tech_industry", "university_access"]
                },
                {
                    "value": "cost_optimization",
                    "icon": "💰",
                    "title": "Réduire mes dépenses, gagner en pouvoir d'achat",
                    "title_en": "Reduce my expenses, gain purchasing power",
                    "description": "Coût de vie, logement abordable, optimisation budget",
                    "description_en": "Cost of living, affordable housing, budget optimization",
                    "boost_criteria": ["cost_of_living", "housing_affordability", "income_tax_burden"]
                },
                {
                    "value": "lifestyle_upgrade",
                    "icon": "🌟",
                    "title": "Trouver un cadre de vie plus épanouissant",
                    "title_en": "Find a more fulfilling living environment",
                    "description": "Climat, culture, bien-être, qualité de vie",
                    "description_en": "Climate, culture, well-being, quality of life",
                    "boost_criteria": ["climate_rating", "cultural_scene", "restaurant_diversity"]
                },
                {
                    "value": "family_focus",
                    "icon": "👨‍👩‍👧‍👦",
                    "title": "Offrir un meilleur environnement à ma famille",
                    "title_en": "Provide a better environment for my family",
                    "description": "Écoles, sécurité, cadre familial, avenir enfants",
                    "description_en": "Schools, security, family environment, children's future",
                    "boost_criteria": ["school_quality", "suburb_quality", "healthcare_access"]
                },
                {
                    "value": "exploration_focus",
                    "icon": "🆕",
                    "title": "Explorer, découvrir, changer d'air",
                    "title_en": "Explore, discover, change scenery",
                    "description": "Aventure, nouveauté, expérience de vie",
                    "description_en": "Adventure, novelty, life experience",
                    "boost_criteria": ["cultural_scene", "restaurant_diversity", "nightlife"]
                }
            ]
        },

        // ===== 2. PROFIL PERSONNEL - SITUATION DE VIE =====
        {
            "id": "france_age_profile",
            "title": "👤 Comment décririez-vous votre situation actuelle ?",
            "title_en": "👤 How would you describe your current situation?",
            "category": "personal_profile",
            "type": "single",
            "description": "Adapte les recommandations à votre étape de vie",
            "description_en": "Adapts recommendations to your life stage",
            "weight": 8,
            "options": [
                {
                    "value": "student_young",
                    "icon": "🎓",
                    "title": "Étudiant ou débutant dans la vie active",
                    "title_en": "Student or beginner in working life",
                    "description": "Formation, premier emploi, découverte du monde professionnel",
                    "description_en": "Training, first job, discovering the professional world",
                    "boost_criteria": ["university_access", "cost_of_living", "public_transport", "nightlife"]
                },
                {
                    "value": "young_active",
                    "icon": "🚀",
                    "title": "Jeune professionnel qui se construit",
                    "title_en": "Young professional building their career",
                    "description": "Carrière en développement, networking, ambitions",
                    "description_en": "Developing career, networking, ambitions",
                    "boost_criteria": ["job_market", "tech_industry", "cultural_scene", "nightlife"]
                },
                {
                    "value": "established_active",
                    "icon": "💼",
                    "title": "Professionnel établi avec responsabilités",
                    "title_en": "Established professional with responsibilities",
                    "description": "Stabilité acquise, famille, projets d'investissement",
                    "description_en": "Acquired stability, family, investment projects",
                    "boost_criteria": ["school_quality", "suburb_quality", "healthcare_access", "property_tax"]
                },
                {
                    "value": "senior_comfort",
                    "icon": "🏡",
                    "title": "En recherche de tranquillité et confort",
                    "title_en": "Seeking tranquility and comfort",
                    "description": "Bien-être, santé, qualité de vie, sérénité",
                    "description_en": "Well-being, health, quality of life, serenity",
                    "boost_criteria": ["healthcare_access", "climate_rating", "cultural_scene", "walkability"]
                }
            ]
        },

        // ===== 3. BUDGET RÉALISTE - FINANCES =====
        {
            "id": "france_monthly_budget",
            "title": "💰 Quel budget total mensuel pouvez-vous consacrer à votre nouvelle vie ?",
            "title_en": "💰 What total monthly budget can you dedicate to your new life?",
            "category": "financial",
            "type": "single",
            "description": "Filtre les villes selon vos moyens financiers réels",
            "description_en": "Filters cities according to your real financial means",
            "weight": 9,
            "options": [
                {
                    "value": "budget_tight",
                    "icon": "💸",
                    "title": "Économe : Moins de 1000€/mois",
                    "title_en": "Economical: Less than 1000€/month",
                    "description": "Priorité absolue aux villes les plus abordables",
                    "description_en": "Absolute priority to the most affordable cities",
                    "boost_criteria": ["cost_of_living", "housing_affordability", "public_transport"]
                },
                {
                    "value": "budget_balanced",
                    "icon": "⚖️",
                    "title": "Modéré : 1000-1800€/mois",
                    "title_en": "Moderate: 1000-1800€/month",
                    "description": "Bon rapport qualité-prix recherché",
                    "description_en": "Good value for money sought",
                    "boost_criteria": ["cost_of_living", "job_market", "public_transport"]
                },
                {
                    "value": "budget_comfortable",
                    "icon": "💼",
                    "title": "Confortable : 1800-3000€/mois",
                    "title_en": "Comfortable: 1800-3000€/month",
                    "description": "Qualité de vie avant économies",
                    "description_en": "Quality of life before savings",
                    "boost_criteria": ["cultural_scene", "restaurant_diversity", "school_quality"]
                },
                {
                    "value": "budget_premium",
                    "icon": "💎",
                    "title": "Flexible : Plus de 3000€/mois",
                    "title_en": "Flexible: More than 3000€/month",
                    "description": "Budget non-contraignant, priorité au meilleur",
                    "description_en": "Non-constraining budget, priority to the best",
                    "boost_criteria": ["cultural_scene", "restaurant_diversity", "suburb_quality", "healthcare_access"]
                }
            ]
        },

        // ===== 4. SITUATION PROFESSIONNELLE - TRAVAIL =====
        {
            "id": "france_work_situation",
            "title": "💼 Où en êtes-vous côté travail/études ?",
            "title_en": "💼 Where are you in terms of work/studies?",
            "category": "professional",
            "type": "single",
            "description": "Oriente selon vos besoins professionnels et étudiants",
            "description_en": "Guides according to your professional and student needs",
            "weight": 8,
            "options": [
                {
                    "value": "student_studies",
                    "icon": "📚",
                    "title": "Encore en études, je prépare mon avenir",
                    "title_en": "Still studying, preparing for my future",
                    "description": "Étudiant, formations, stage, alternance",
                    "description_en": "Student, training, internship, work-study",
                    "boost_criteria": ["university_access", "student_life", "cost_of_living", "public_transport"]
                },
                {
                    "value": "stable_job",
                    "icon": "🏢",
                    "title": "J'ai un travail stable, je peux déménager",
                    "title_en": "I have a stable job, I can relocate",
                    "description": "CDI, fonctionnaire, sécurité acquise",
                    "description_en": "Permanent contract, civil servant, acquired security",
                    "boost_criteria": ["cost_of_living", "climate_rating", "cultural_scene"]
                },
                {
                    "value": "job_search",
                    "icon": "🔍",
                    "title": "Je cherche du boulot, j'ai besoin d'opportunités",
                    "title_en": "I'm looking for work, I need opportunities",
                    "description": "Recherche active, marché dynamique essentiel",
                    "description_en": "Active search, dynamic market essential",
                    "boost_criteria": ["job_market", "tech_industry", "university_access"]
                },
                {
                    "value": "remote_flexible",
                    "icon": "💻",
                    "title": "Télétravail/freelance, libre géographiquement",
                    "title_en": "Remote work/freelance, geographically free",
                    "description": "Liberté totale, priorité qualité de vie",
                    "description_en": "Total freedom, priority to quality of life",
                    "boost_criteria": ["cost_of_living", "climate_rating", "cultural_scene", "remote_work_friendly"]
                }
            ]
        },

        // ===== 5. TYPE DE LOGEMENT - HABITAT =====
        {
            "id": "france_housing_preference",
            "title": "🏠 Quel type de logement vous fait rêver ?",
            "title_en": "🏠 What type of housing makes you dream?",
            "category": "housing",
            "type": "single",
            "description": "Définit votre mode de vie résidentiel",
            "description_en": "Defines your residential lifestyle",
            "weight": 7,
            "options": [
                {
                    "value": "downtown_apartment",
                    "icon": "🏙️",
                    "title": "Appartement centre-ville, tout à pied",
                    "title_en": "Downtown apartment, everything on foot",
                    "description": "Vie urbaine, proximité, énergie de la ville",
                    "description_en": "Urban life, proximity, city energy",
                    "boost_criteria": ["urban_density", "walkability", "cultural_scene", "restaurant_diversity"]
                },
                {
                    "value": "suburban_house",
                    "icon": "🌳",
                    "title": "Maison avec jardin en périphérie paisible",
                    "title_en": "House with garden in peaceful suburbs",
                    "description": "Espace, calme, vie familiale",
                    "description_en": "Space, calm, family life",
                    "boost_criteria": ["suburb_quality", "school_quality", "car_dependency", "natural_disaster_risk"]
                },
                {
                    "value": "transport_connected",
                    "icon": "🚇",
                    "title": "Proche transports, équilibre ville/nature",
                    "title_en": "Close to transport, city/nature balance",
                    "description": "Flexibilité, connexions, compromise intelligent",
                    "description_en": "Flexibility, connections, smart compromise",
                    "boost_criteria": ["public_transport", "suburb_quality", "walkability"]
                },
                {
                    "value": "budget_priority",
                    "icon": "💸",
                    "title": "Le moins cher possible, je privilégie l'économie",
                    "title_en": "As cheap as possible, I prioritize economy",
                    "description": "Budget serré, logement fonctionnel",
                    "description_en": "Tight budget, functional housing",
                    "boost_criteria": ["housing_affordability", "cost_of_living", "public_transport"]
                }
            ]
        },

        // ===== 6. TRANSPORT QUOTIDIEN - MOBILITÉ =====
        {
            "id": "france_transport_preference",
            "title": "🚗 Quel est votre mode de transport idéal ?",
            "title_en": "🚗 What is your ideal mode of transport?",
            "category": "mobility",
            "type": "single",
            "description": "Optimise selon vos habitudes de déplacement",
            "description_en": "Optimizes according to your travel habits",
            "weight": 7,
            "options": [
                {
                    "value": "walk_bike_priority",
                    "icon": "🚶",
                    "title": "Tout à pied + vélo, voiture exceptionnelle",
                    "title_en": "Everything on foot + bike, car exceptional",
                    "description": "Écologique, santé, proximité services",
                    "description_en": "Ecological, health, proximity to services",
                    "boost_criteria": ["walkability", "urban_density", "public_transport", "car_dependency"]
                },
                {
                    "value": "public_transport_fan",
                    "icon": "🚇",
                    "title": "Transports publics efficaces, écologique",
                    "title_en": "Efficient public transport, ecological",
                    "description": "Metro, bus, tram, connexions urbaines",
                    "description_en": "Metro, bus, tram, urban connections",
                    "boost_criteria": ["public_transport", "urban_density", "walkability"]
                },
                {
                    "value": "car_essential",
                    "icon": "🚗",
                    "title": "Voiture indispensable, je privilégie la liberté",
                    "title_en": "Car essential, I prioritize freedom",
                    "description": "Autonomie, périphérie, mobilité totale",
                    "description_en": "Autonomy, periphery, total mobility",
                    "boost_criteria": ["suburb_quality", "car_dependency", "cost_of_living"]
                },
                {
                    "value": "multimodal_flexible",
                    "icon": "🔄",
                    "title": "Mix selon besoins, flexibilité maximale",
                    "title_en": "Mix according to needs, maximum flexibility",
                    "description": "Adaptabilité, options multiples",
                    "description_en": "Adaptability, multiple options",
                    "boost_criteria": ["public_transport", "walkability", "car_dependency"]
                }
            ]
        },

        // ===== 7. CLIMAT IDÉAL - MÉTÉO =====
        {
            "id": "france_climate_preference",
            "title": "🌤️ Quel climat vous rendrait le plus heureux ?",
            "title_en": "🌤️ What climate would make you happiest?",
            "category": "climate",
            "type": "single",
            "description": "Influence votre bien-être quotidien",
            "description_en": "Influences your daily well-being",
            "weight": 6,
            "options": [
                {
                    "value": "mediterranean_sun",
                    "icon": "☀️",
                    "title": "Soleil méditerranéen, chaleur et luminosité",
                    "title_en": "Mediterranean sun, warmth and brightness",
                    "description": "Sud, PACA, Occitanie, joie de vivre",
                    "description_en": "South, PACA, Occitanie, joy of living",
                    "boost_criteria": ["climate_rating", "weather_consistency", "heat_wave_risk"]
                },
                {
                    "value": "four_seasons",
                    "icon": "🍂",
                    "title": "Quatre saisons marquées, j'aime la variété",
                    "title_en": "Four marked seasons, I like variety",
                    "description": "Continental, Est, changements rythmés",
                    "description_en": "Continental, East, rhythmic changes",
                    "boost_criteria": ["weather_consistency", "natural_disaster_risk"]
                },
                {
                    "value": "oceanic_mild",
                    "icon": "🌊",
                    "title": "Océanique doux, tempéré sans extrême",
                    "title_en": "Mild oceanic, temperate without extremes",
                    "description": "Bretagne, Normandie, Loire, modération",
                    "description_en": "Brittany, Normandy, Loire, moderation",
                    "boost_criteria": ["climate_rating", "natural_disaster_risk", "heat_wave_risk"]
                },
                {
                    "value": "climate_adaptable",
                    "icon": "🤷",
                    "title": "Peu importe, je m'adapte facilement",
                    "title_en": "Doesn't matter, I adapt easily",
                    "description": "Priorité autres critères que météo",
                    "description_en": "Priority on other criteria than weather",
                    "boost_criteria": ["climate_rating"]
                }
            ]
        },

        // ===== 8. VIE CULTURELLE - SORTIES =====
        {
            "id": "france_social_scene",
            "title": "🎭 Qu'est-ce qui anime vos soirées et week-ends ?",
            "title_en": "🎭 What brings your evenings and weekends to life?",
            "category": "lifestyle",
            "type": "single",
            "description": "Privilégie votre épanouissement social",
            "description_en": "Prioritizes your social fulfillment",
            "weight": 6,
            "options": [
                {
                    "value": "gastronomy_culture",
                    "icon": "🍽️",
                    "title": "Gastronomie et bons restaurants",
                    "title_en": "Gastronomy and good restaurants",
                    "description": "Foodie, terroir, art culinaire français",
                    "description_en": "Foodie, terroir, French culinary art",
                    "boost_criteria": ["restaurant_diversity", "cultural_scene"]
                },
                {
                    "value": "cultural_events",
                    "icon": "🎨",
                    "title": "Musées, théâtres, événements culturels",
                    "title_en": "Museums, theaters, cultural events",
                    "description": "Art, spectacles, patrimoine, enrichissement",
                    "description_en": "Art, shows, heritage, enrichment",
                    "boost_criteria": ["cultural_scene", "university_access"]
                },
                {
                    "value": "nightlife_dynamic",
                    "icon": "🍻",
                    "title": "Bars, clubs, vie nocturne dynamique",
                    "title_en": "Bars, clubs, dynamic nightlife",
                    "description": "Sorties, rencontres, énergie urbaine",
                    "description_en": "Outings, meetings, urban energy",
                    "boost_criteria": ["nightlife", "urban_density", "cultural_scene"]
                },
                {
                    "value": "quiet_homebody",
                    "icon": "🏠",
                    "title": "Tranquillité à la maison, je sors peu",
                    "title_en": "Tranquility at home, I rarely go out",
                    "description": "Calme, nature, vie simple",
                    "description_en": "Calm, nature, simple life",
                    "boost_criteria": ["suburb_quality", "natural_disaster_risk", "cost_of_living"]
                }
            ]
        },

        // ===== 9. SITUATION FAMILIALE - ENFANTS =====
        {
            "id": "france_family_situation",
            "title": "👨‍👩‍👧‍👦 Quelle est votre situation familiale ?",
            "title_en": "👨‍👩‍👧‍👦 What is your family situation?",
            "category": "family",
            "type": "single",
            "description": "Adapte selon vos responsabilités familiales",
            "description_en": "Adapts according to your family responsibilities",
            "weight": 7,
            "options": [
                {
                    "value": "single_no_children",
                    "icon": "🎒",
                    "title": "Célibataire sans enfants, liberté totale",
                    "title_en": "Single without children, total freedom",
                    "description": "Flexibilité maximale, choix personnels",
                    "description_en": "Maximum flexibility, personal choices",
                    "boost_criteria": ["cost_of_living", "nightlife", "cultural_scene"]
                },
                {
                    "value": "couple_no_children",
                    "icon": "💑",
                    "title": "Couple sans enfants, projets à deux",
                    "title_en": "Couple without children, projects for two",
                    "description": "Vie à deux, loisirs, investissement",
                    "description_en": "Life for two, leisure, investment",
                    "boost_criteria": ["cultural_scene", "restaurant_diversity", "climate_rating"]
                },
                {
                    "value": "young_children",
                    "icon": "👶",
                    "title": "Jeunes enfants, écoles primaires importantes",
                    "title_en": "Young children, primary schools important",
                    "description": "Crèches, écoles, environnement familial",
                    "description_en": "Daycare, schools, family environment",
                    "boost_criteria": ["school_quality", "suburb_quality", "healthcare_access", "natural_disaster_risk"]
                },
                {
                    "value": "teen_students",
                    "icon": "🎓",
                    "title": "Enfants ados/étudiants, lycées/universités cruciaux",
                    "title_en": "Teenage/student children, high schools/universities crucial",
                    "description": "Éducation supérieure, orientation, avenir",
                    "description_en": "Higher education, guidance, future",
                    "boost_criteria": ["school_quality", "university_access", "public_transport", "cultural_scene"]
                }
            ]
        },

        // ===== 10. DEAL-BREAKER - CRITÈRE ÉLIMINATOIRE =====
        {
            "id": "france_deal_breaker",
            "title": "⚠️ Quel critère est absolument non-négociable pour vous ?",
            "title_en": "⚠️ Which criterion is absolutely non-negotiable for you?",
            "category": "elimination",
            "type": "single",
            "description": "Critère éliminatoire pour éviter les mauvaises surprises",
            "description_en": "Elimination criterion to avoid bad surprises",
            "weight": 8,
            "options": [
                {
                    "value": "cost_too_high",
                    "icon": "💸",
                    "title": "Coût de la vie trop élevé pour mon budget",
                    "title_en": "Cost of living too high for my budget",
                    "description": "Budget dépassé, stress financier",
                    "description_en": "Budget exceeded, financial stress",
                    "penalty_criteria": ["cost_of_living", "housing_affordability"]
                },
                {
                    "value": "depressing_climate",
                    "icon": "🌧️",
                    "title": "Climat déprimant (pluie, froid, grisaille)",
                    "title_en": "Depressing climate (rain, cold, gloom)",
                    "description": "Moral affecté par la météo",
                    "description_en": "Morale affected by weather",
                    "penalty_criteria": ["climate_rating", "weather_consistency"]
                },
                {
                    "value": "no_job_opportunities",
                    "icon": "🚫",
                    "title": "Manque d'opportunités professionnelles",
                    "title_en": "Lack of professional opportunities",
                    "description": "Carrière bloquée, stagnation",
                    "description_en": "Blocked career, stagnation",
                    "penalty_criteria": ["job_market", "tech_industry"]
                },
                {
                    "value": "pollution_degraded",
                    "icon": "🏭",
                    "title": "Pollution ou environnement dégradé",
                    "title_en": "Pollution or degraded environment",
                    "description": "Santé, qualité de vie, futur enfants",
                    "description_en": "Health, quality of life, children's future",
                    "penalty_criteria": ["natural_disaster_risk", "healthcare_access"]
                }
            ]
        }
    ],

    // 🗂️ MAPPING CRITÈRES → QUESTIONS
    "criteria_mapping": {
        "cost_of_living": "Coût de la vie général",
        "housing_affordability": "Logement abordable",
        "climate_rating": "Qualité du climat",
        "weather_consistency": "Stabilité météo",
        "job_market": "Marché de l'emploi",
        "tech_industry": "Secteur technologique",
        "remote_work_friendly": "Télétravail friendly",
        "urban_density": "Densité urbaine équilibrée",
        "suburb_quality": "Qualité banlieues",
        "income_tax_burden": "Charge fiscale",
        "local_tax": "Taxes locales",
        "property_tax": "Taxe foncière",
        "school_quality": "Qualité écoles",
        "university_access": "Accès universités",
        "natural_disaster_risk": "Sécurité catastrophes",
        "flood_risk": "Risque inondations",
        "heat_wave_risk": "Risque canicules",
        "public_transport": "Transports publics",
        "walkability": "Accessibilité piétonne",
        "car_dependency": "Dépendance automobile",
        "healthcare_access": "Accès santé",
        "hospital_quality": "Qualité hôpitaux",
        "cultural_scene": "Scène culturelle",
        "restaurant_diversity": "Diversité restaurants",
        "nightlife": "Vie nocturne"
    },
    "algorithm_notes": "Système conçu pour matcher priorités relocation domestique française"
};

// 🔗 INTÉGRATION DANS LE SYSTÈME PRINCIPAL
if (typeof window.QUESTIONS_DATA === 'undefined') {
    window.QUESTIONS_DATA = {};
}
window.QUESTIONS_DATA.france_residents = window.QUESTIONS_DATA_FRANCE.france_residents;
// Alias pour compatibilité avec analysis.js
window.QUESTIONS_DATA.france = window.QUESTIONS_DATA_FRANCE.france_residents;

console.log("✅ France Residents Questions Data loaded - 10 questions, 25 criteria mapping");
