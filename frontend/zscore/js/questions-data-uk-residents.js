/**
 * 🇬🇧 QUESTIONS-DATA-UK-RESIDENTS.JS - QUESTIONNAIRE RELOCATION DOMESTIQUE UK
 * ================================================================================
 * 12 questions OPTIMALES pour Britanniques cherchant nouvelle ville UK
 * Author: Revolutionary Team | Version: 1.0.0 - UK Domestic Focus
 * OBJECTIF: Recommandations basées sur profils réels des relocations britanniques
 */

// 🏠 QUESTIONS CENTRÉES BESOINS RELOCATION UK
window.QUESTIONS_DATA_UK = {
    "uk_residents": [

        // ===== 0A. PRÉFÉRENCE RÉGIONALE UK =====
        {
            "id": "uk_region_preference",
            "title": "🗺️ Quelle région du Royaume-Uni vous attire le plus ?",
            "title_en": "🗺️ Which region of the United Kingdom attracts you the most?",
            "category": "geography",
            "type": "single",
            "description": "Choisissez votre zone géographique préférée au UK",
            "description_en": "Choose your preferred geographical area in the UK",
            "weight": 7,
            "options": [
                {
                    "value": "any_region",
                    "icon": "🇬🇧",
                    "title": "Ouvert à toutes les régions",
                    "title_en": "Open to all regions",
                    "description": "Je suis flexible, recommandez-moi partout au UK",
                    "description_en": "I'm flexible, recommend anywhere in the UK"
                },
                {
                    "value": "london_southeast",
                    "icon": "🏛️",
                    "title": "Londres et Sud-Est",
                    "title_en": "London and South East",
                    "description": "Greater London, Surrey, Kent, Sussex",
                    "description_en": "Greater London, Surrey, Kent, Sussex"
                },
                {
                    "value": "northern_england",
                    "icon": "🏭",
                    "title": "Nord de l'Angleterre",
                    "title_en": "Northern England",
                    "description": "Manchester, Liverpool, Leeds, Sheffield, Newcastle",
                    "description_en": "Manchester, Liverpool, Leeds, Sheffield, Newcastle"
                },
                {
                    "value": "scotland",
                    "icon": "🏔️",
                    "title": "Écosse",
                    "title_en": "Scotland",
                    "description": "Glasgow, Edinburgh, Aberdeen, Highlands",
                    "description_en": "Glasgow, Edinburgh, Aberdeen, Highlands"
                },
                {
                    "value": "wales",
                    "icon": "🐉",
                    "title": "Pays de Galles",
                    "title_en": "Wales",
                    "description": "Cardiff, Swansea, Newport, Bangor",
                    "description_en": "Cardiff, Swansea, Newport, Bangor"
                },
                {
                    "value": "central_england",
                    "icon": "🏘️",
                    "title": "Centre de l'Angleterre",
                    "title_en": "Central England",
                    "description": "Birmingham, Midlands, Nottingham, Leicester",
                    "description_en": "Birmingham, Midlands, Nottingham, Leicester"
                }
            ]
        },

        // ===== 0B. PRÉFÉRENCE LINGUISTIQUE UK =====
        {
            "id": "uk_language_preference",
            "title": "🗣️ Dans quelle langue préférez-vous vivre au quotidien ?",
            "title_en": "🗣️ In which language do you prefer to live daily?",
            "category": "language",
            "type": "single",
            "description": "Environnement linguistique souhaité pour votre nouvelle ville",
            "description_en": "Desired linguistic environment for your new city",
            "weight": 5,
            "options": [
                {
                    "value": "english_only",
                    "icon": "🇬🇧",
                    "title": "Anglais uniquement",
                    "title_en": "English only",
                    "description": "Environnement 100% anglophone",
                    "description_en": "100% English-speaking environment"
                },
                {
                    "value": "welsh_friendly",
                    "icon": "🏴󠁧󠁢󠁷󠁬󠁳󠁿",
                    "title": "Ouvert au gallois",
                    "title_en": "Open to Welsh",
                    "description": "Confortable avec bilinguisme anglais-gallois",
                    "description_en": "Comfortable with English-Welsh bilingualism"
                },
                {
                    "value": "language_flexible",
                    "icon": "🌐",
                    "title": "Très flexible",
                    "title_en": "Very flexible",
                    "description": "La langue n'est pas un critère important",
                    "description_en": "Language is not an important criterion"
                }
            ]
        },

        // ===== 1. MOTIVATION/PRIORITÉ PRINCIPALE =====
        {
            "id": "uk_main_priority",
            "title": "🎯 Qu'est-ce qui vous pousse VRAIMENT à changer de ville ?",
            "title_en": "🎯 What REALLY drives you to change cities?",
            "category": "life_priority",
            "type": "single",
            "description": "Identifie ce qui compte vraiment pour votre nouveau départ",
            "description_en": "Identifies what really matters for your fresh start",
            "weight": 9,
            "options": [
                {
                    "value": "career_growth",
                    "icon": "🚀",
                    "title": "Saisir une opportunité professionnelle",
                    "title_en": "Seize a professional opportunity",
                    "description": "Emploi, promotion, secteur dynamique, networking",
                    "description_en": "Job, promotion, dynamic sector, networking",
                    "boost_criteria": ["job_market", "tech_industry", "university_access"]
                },
                {
                    "value": "cost_optimization",
                    "icon": "💰",
                    "title": "Réduire mes coûts, gagner en pouvoir d'achat",
                    "title_en": "Reduce costs, gain purchasing power",
                    "description": "Logement abordable, council tax, coût de la vie",
                    "description_en": "Affordable housing, council tax, cost of living",
                    "boost_criteria": ["cost_of_living", "housing_affordability", "council_tax"]
                },
                {
                    "value": "lifestyle_upgrade",
                    "icon": "🌟",
                    "title": "Améliorer ma qualité de vie",
                    "title_en": "Improve my quality of life",
                    "description": "Climat, culture, espaces verts, bien-être",
                    "description_en": "Climate, culture, green spaces, wellbeing",
                    "boost_criteria": ["climate_rating", "cultural_scene", "walkability"]
                },
                {
                    "value": "family_focus",
                    "icon": "👨‍👩‍👧‍👦",
                    "title": "Offrir un meilleur environnement à ma famille",
                    "title_en": "Provide a better environment for my family",
                    "description": "Écoles, NHS, sécurité, communautés familiales",
                    "description_en": "Schools, NHS, safety, family communities",
                    "boost_criteria": ["school_quality", "suburb_quality", "healthcare_access"]
                }
            ]
        },

        // ===== 2. PROFIL D'ÂGE ET ÉTAPE DE VIE =====
        {
            "id": "uk_age_profile",
            "title": "👤 À quelle étape de votre vie êtes-vous ?",
            "title_en": "👤 What stage of life are you at?",
            "category": "demographics",
            "type": "single",
            "weight": 7,
            "options": [
                {
                    "value": "student_young",
                    "icon": "🎓",
                    "title": "Étudiant/Jeune diplômé (18-25 ans)",
                    "title_en": "Student/Graduate (18-25 years)",
                    "description": "Université, premier job, vie sociale, budget étudiant",
                    "description_en": "University, first job, social life, student budget"
                },
                {
                    "value": "young_professional",
                    "icon": "💼",
                    "title": "Jeune professionnel (26-35 ans)",
                    "title_en": "Young professional (26-35 years)",
                    "description": "Carrière en développement, indépendance, opportunités",
                    "description_en": "Developing career, independence, opportunities"
                },
                {
                    "value": "established_professional",
                    "icon": "🏡",
                    "title": "Professionnel établi (36-50 ans)",
                    "title_en": "Established professional (36-50 years)",
                    "description": "Carrière stable, équilibre vie-travail, famille",
                    "description_en": "Stable career, work-life balance, family"
                },
                {
                    "value": "pre_retirement",
                    "icon": "🌻",
                    "title": "Pré-retraite/Retraité (50+ ans)",
                    "title_en": "Pre-retirement/Retired (50+ years)",
                    "description": "Confort, tranquillité, NHS, pensions",
                    "description_en": "Comfort, tranquility, NHS, pensions"
                }
            ]
        },

        // ===== 3. BUDGET LOGEMENT MENSUEL £ =====
        {
            "id": "uk_monthly_budget",
            "title": "💳 Quel est votre budget logement mensuel ?",
            "title_en": "💳 What is your monthly housing budget?",
            "category": "financial",
            "type": "single",
            "weight": 8,
            "options": [
                {
                    "value": "budget_tight",
                    "icon": "💸",
                    "title": "Budget serré (< £800/mois)",
                    "title_en": "Tight budget (< £800/month)",
                    "description": "Colocation, zones abordables, priorité au prix",
                    "description_en": "Flatshare, affordable areas, price priority"
                },
                {
                    "value": "budget_balanced",
                    "icon": "💰",
                    "title": "Budget équilibré (£800 - £1,500/mois)",
                    "title_en": "Balanced budget (£800 - £1,500/month)",
                    "description": "Appartement 1-2 chambres, quartiers moyens",
                    "description_en": "1-2 bedroom flat, average neighborhoods"
                },
                {
                    "value": "budget_comfortable",
                    "icon": "🏠",
                    "title": "Budget confortable (£1,500 - £2,500/mois)",
                    "title_en": "Comfortable budget (£1,500 - £2,500/month)",
                    "description": "Maison/grand appartement, bons quartiers",
                    "description_en": "House/large flat, good neighborhoods"
                },
                {
                    "value": "budget_premium",
                    "icon": "🏛️",
                    "title": "Budget premium (£2,500+/mois)",
                    "title_en": "Premium budget (£2,500+/month)",
                    "description": "Logement haut de gamme, quartiers prestigieux",
                    "description_en": "High-end housing, prestigious areas"
                }
            ]
        },

        // ===== 4. SITUATION PROFESSIONNELLE =====
        {
            "id": "uk_work_situation",
            "title": "💻 Quelle est votre situation professionnelle ?",
            "title_en": "💻 What is your professional situation?",
            "category": "work",
            "type": "single",
            "weight": 8,
            "options": [
                {
                    "value": "stable_employment",
                    "icon": "✅",
                    "title": "Emploi stable/permanent",
                    "title_en": "Stable/permanent employment",
                    "description": "Contrat permanent, fonction publique, grande entreprise",
                    "description_en": "Permanent contract, civil service, large company"
                },
                {
                    "value": "job_search",
                    "icon": "🔍",
                    "title": "Recherche d'emploi active",
                    "title_en": "Active job search",
                    "description": "Marché du travail dynamique prioritaire",
                    "description_en": "Dynamic job market priority"
                },
                {
                    "value": "full_remote",
                    "icon": "🏠",
                    "title": "100% télétravail",
                    "title_en": "100% remote work",
                    "description": "Liberté géographique, infrastructure internet",
                    "description_en": "Geographic freedom, internet infrastructure"
                },
                {
                    "value": "freelance_entrepreneur",
                    "icon": "🚀",
                    "title": "Freelance/Entrepreneur",
                    "title_en": "Freelance/Entrepreneur",
                    "description": "Écosystème startup, networking, coworking",
                    "description_en": "Startup ecosystem, networking, coworking"
                }
            ]
        },

        // ===== 5. TYPE DE LOGEMENT PRÉFÉRÉ =====
        {
            "id": "uk_housing_preference",
            "title": "🏠 Quel type de logement et quartier préférez-vous ?",
            "title_en": "🏠 What type of housing and neighborhood do you prefer?",
            "category": "housing",
            "type": "single",
            "weight": 7,
            "options": [
                {
                    "value": "city_centre_flat",
                    "icon": "🏢",
                    "title": "Appartement centre-ville",
                    "title_en": "City centre flat",
                    "description": "Marche au bureau, pubs, vie urbaine intense",
                    "description_en": "Walk to office, pubs, intense urban life"
                },
                {
                    "value": "suburban_house",
                    "icon": "🏡",
                    "title": "Maison de banlieue",
                    "title_en": "Suburban house",
                    "description": "Jardin, garage, tranquillité, bonnes écoles",
                    "description_en": "Garden, garage, tranquility, good schools"
                },
                {
                    "value": "transport_connected",
                    "icon": "🚇",
                    "title": "Connecté aux transports",
                    "title_en": "Transport connected",
                    "description": "Tube/train proche, équilibre ville-banlieue",
                    "description_en": "Tube/train nearby, city-suburb balance"
                },
                {
                    "value": "budget_priority",
                    "icon": "💵",
                    "title": "Priorité au prix",
                    "title_en": "Price priority",
                    "description": "Meilleur rapport qualité-prix, flexible sur zone",
                    "description_en": "Best value for money, flexible on area"
                }
            ]
        },

        // ===== 6. TRANSPORT QUOTIDIEN =====
        {
            "id": "uk_transport_preference",
            "title": "🚗 Comment souhaitez-vous vous déplacer au quotidien ?",
            "title_en": "🚗 How do you wish to get around daily?",
            "category": "transport",
            "type": "single",
            "weight": 6,
            "options": [
                {
                    "value": "walk_cycle_priority",
                    "icon": "🚶",
                    "title": "Marche + Vélo prioritaires",
                    "title_en": "Walking + Cycling priority",
                    "description": "Quartiers piétonniers, cycle lanes, tout accessible",
                    "description_en": "Pedestrian areas, cycle lanes, everything accessible"
                },
                {
                    "value": "public_transport_fan",
                    "icon": "🚇",
                    "title": "Transports publics excellents",
                    "title_en": "Excellent public transport",
                    "description": "Tube, bus, trains efficaces et étendus",
                    "description_en": "Tube, buses, efficient and extensive trains"
                },
                {
                    "value": "car_essential",
                    "icon": "🚗",
                    "title": "Voiture indispensable",
                    "title_en": "Car essential",
                    "description": "Parking facile, liberté de mouvement",
                    "description_en": "Easy parking, freedom of movement"
                },
                {
                    "value": "multimodal_flexible",
                    "icon": "🔄",
                    "title": "Multimodal flexible",
                    "title_en": "Flexible multimodal",
                    "description": "Voiture + transports selon les besoins",
                    "description_en": "Car + transport according to needs"
                }
            ]
        },

        // ===== 7. CLIMAT PRÉFÉRÉ UK =====
        {
            "id": "uk_climate_preference",
            "title": "🌡️ Quel climat britannique vous convient le mieux ?",
            "title_en": "🌡️ Which British climate suits you best?",
            "category": "climate",
            "type": "single",
            "weight": 5,
            "options": [
                {
                    "value": "mild_southern",
                    "icon": "☀️",
                    "title": "Doux du Sud (Londres, Brighton)",
                    "title_en": "Mild Southern (London, Brighton)",
                    "description": "Hivers plus doux, étés plus chauds, moins de pluie",
                    "description_en": "Milder winters, warmer summers, less rain"
                },
                {
                    "value": "maritime_western",
                    "icon": "🌊",
                    "title": "Maritime de l'Ouest (Cardiff, Bristol)",
                    "title_en": "Maritime Western (Cardiff, Bristol)",
                    "description": "Tempéré océanique, pluie fréquente mais douce",
                    "description_en": "Oceanic temperate, frequent but mild rain"
                },
                {
                    "value": "continental_northern",
                    "icon": "❄️",
                    "title": "Continental du Nord (Manchester, Edinburgh)",
                    "title_en": "Continental Northern (Manchester, Edinburgh)",
                    "description": "Hivers plus froids, étés frais, variations saisonnières",
                    "description_en": "Colder winters, cool summers, seasonal variations"
                },
                {
                    "value": "climate_adaptable",
                    "icon": "🔄",
                    "title": "Je m'adapte facilement",
                    "title_en": "I adapt easily",
                    "description": "Le climat britannique ne me dérange pas",
                    "description_en": "British climate doesn't bother me"
                }
            ]
        },

        // ===== 8. VIE SOCIALE ET CULTURELLE =====
        {
            "id": "uk_social_scene",
            "title": "🎭 Quelle scène sociale et culturelle vous attire ?",
            "title_en": "🎭 Which social and cultural scene attracts you?",
            "category": "lifestyle",
            "type": "single",
            "weight": 5,
            "options": [
                {
                    "value": "pubs_traditional",
                    "icon": "🍺",
                    "title": "Pubs et culture traditionnelle",
                    "title_en": "Pubs and traditional culture",
                    "description": "Pubs locaux, communauté, événements de quartier",
                    "description_en": "Local pubs, community, neighborhood events"
                },
                {
                    "value": "arts_culture",
                    "icon": "🎨",
                    "title": "Arts et culture",
                    "title_en": "Arts and culture",
                    "description": "Théâtres, musées, festivals, scène artistique",
                    "description_en": "Theaters, museums, festivals, artistic scene"
                },
                {
                    "value": "cosmopolitan_dining",
                    "icon": "🍽️",
                    "title": "Gastronomie cosmopolite",
                    "title_en": "Cosmopolitan dining",
                    "description": "Restaurants variés, food scene, cuisine internationale",
                    "description_en": "Varied restaurants, food scene, international cuisine"
                },
                {
                    "value": "quiet_countryside",
                    "icon": "🌳",
                    "title": "Tranquillité champêtre",
                    "title_en": "Countryside tranquility",
                    "description": "Nature proche, calme, air pur, vie slower",
                    "description_en": "Nature nearby, calm, fresh air, slower life"
                }
            ]
        },

        // ===== 9. SITUATION FAMILIALE =====
        {
            "id": "uk_family_situation",
            "title": "👨‍👩‍👧‍👦 Quelle est votre situation familiale ?",
            "title_en": "👨‍👩‍👧‍👦 What is your family situation?",
            "category": "family",
            "type": "single",
            "weight": 7,
            "options": [
                {
                    "value": "single_no_children",
                    "icon": "👤",
                    "title": "Célibataire sans enfants",
                    "title_en": "Single without children",
                    "description": "Flexibilité maximale, priorité carrière et social",
                    "description_en": "Maximum flexibility, career and social priority"
                },
                {
                    "value": "couple_no_children",
                    "icon": "💑",
                    "title": "Couple sans enfants",
                    "title_en": "Couple without children",
                    "description": "Vie à deux, projets communs, équilibre travail-loisirs",
                    "description_en": "Life as couple, shared projects, work-leisure balance"
                },
                {
                    "value": "young_family",
                    "icon": "👶",
                    "title": "Famille avec jeunes enfants (0-11 ans)",
                    "title_en": "Family with young children (0-11 years)",
                    "description": "Primary schools, parcs, NHS pédiatrie, safe areas",
                    "description_en": "Primary schools, parks, NHS pediatrics, safe areas"
                },
                {
                    "value": "teen_family",
                    "icon": "🎒",
                    "title": "Famille avec adolescents (12+ ans)",
                    "title_en": "Family with teenagers (12+ years)",
                    "description": "Secondary schools, A-levels, préparation université",
                    "description_en": "Secondary schools, A-levels, university preparation"
                }
            ]
        },

        // ===== 10. DEAL-BREAKER UK =====
        {
            "id": "uk_deal_breaker",
            "title": "❌ Qu'est-ce qui vous ferait absolument éviter une ville ?",
            "title_en": "❌ What would absolutely make you avoid a city?",
            "category": "constraints",
            "type": "single",
            "weight": 8,
            "options": [
                {
                    "value": "cost_too_high",
                    "icon": "💸",
                    "title": "Coût de la vie trop élevé",
                    "title_en": "Cost of living too high",
                    "description": "Logement hors budget, council tax élevé",
                    "description_en": "Housing over budget, high council tax"
                },
                {
                    "value": "poor_transport",
                    "icon": "🚫",
                    "title": "Transports publics insuffisants",
                    "title_en": "Insufficient public transport",
                    "description": "Pas de tube/train, dépendance voiture obligatoire",
                    "description_en": "No tube/train, mandatory car dependency"
                },
                {
                    "value": "limited_job_market",
                    "icon": "📉",
                    "title": "Marché du travail limité",
                    "title_en": "Limited job market",
                    "description": "Peu d'opportunités dans mon secteur",
                    "description_en": "Few opportunities in my sector"
                },
                {
                    "value": "social_isolation",
                    "icon": "😴",
                    "title": "Isolement social",
                    "title_en": "Social isolation",
                    "description": "Manque d'activités, communauté fermée",
                    "description_en": "Lack of activities, closed community"
                }
            ]
        }
    ]
};

// 🔗 Alias pour l'intégration avec analysis.js
if (typeof window.QUESTIONS_DATA === 'undefined') {
    window.QUESTIONS_DATA = {};
}

window.QUESTIONS_DATA.uk_residents = window.QUESTIONS_DATA_UK.uk_residents;
window.QUESTIONS_DATA.uk = window.QUESTIONS_DATA_UK.uk_residents;

console.log('🇬🇧 Questions UK Residents chargées:', window.QUESTIONS_DATA_UK.uk_residents.length, 'questions');
