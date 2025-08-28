/**
 * 🇨🇦 QUESTIONS-DATA-CA-RESIDENTS.JS - QUESTIONNAIRE RELOCATION DOMESTIQUE CANADA
 * ================================================================================
 * 10 questions OPTIMALES pour Canadiens cherchant nouvelle ville canadienne
 * Author: Revolutionary Team | Version: 1.0.0 - Canada Domestic Focus
 * OBJECTIF: Recommandations basées sur profils réels des relocations canadiennes
 */

// 🏠 QUESTIONS CENTRÉES BESOINS RELOCATION CANADA
window.QUESTIONS_DATA_CANADA = {
    "canada_residents": [

        // ===== 0A. PRÉFÉRENCE RÉGIONALE CANADA =====
        {
            "id": "canada_region_preference",
            "title": "🗺️ Quelle région du Canada vous attire le plus ?",
            "title_en": "🗺️ Which region of Canada attracts you the most?",
            "category": "geography",
            "type": "single",
            "description": "Choisissez votre zone géographique préférée au Canada",
            "description_en": "Choose your preferred geographic area in Canada",
            "weight": 6,
            "options": [
                {
                    "value": "any_region",
                    "icon": "🇨🇦",
                    "title": "Ouvert à toutes les régions",
                    "title_en": "Open to all regions",
                    "description": "Je suis flexible, recommandez-moi partout au Canada",
                    "description_en": "I'm flexible, recommend me anywhere in Canada"
                },
                {
                    "value": "eastern_canada",
                    "icon": "🏛️",
                    "title": "Canada de l'Est (ON, QC, Maritimes)",
                    "title_en": "Eastern Canada (ON, QC, Maritimes)",
                    "description": "Ontario, Québec, provinces Atlantiques",
                    "description_en": "Ontario, Quebec, Atlantic provinces"
                },
                {
                    "value": "western_canada",
                    "icon": "🏔️",
                    "title": "Canada de l'Ouest (BC, AB, SK, MB)",
                    "title_en": "Western Canada (BC, AB, SK, MB)",
                    "description": "Colombie-Britannique, Alberta, Prairies",
                    "description_en": "British Columbia, Alberta, Prairies"
                },
                {
                    "value": "ontario_quebec_only",
                    "icon": "🏙️",
                    "title": "Uniquement Ontario et Québec",
                    "title_en": "Only Ontario and Quebec",
                    "description": "Les deux plus grandes provinces",
                    "description_en": "The two largest provinces"
                },
                {
                    "value": "avoid_quebec",
                    "icon": "🚫",
                    "title": "Éviter le Québec",
                    "title_en": "Avoid Quebec",
                    "description": "Préférence pour les provinces anglophones",
                    "description_en": "Preference for English-speaking provinces"
                }
            ]
        },

        // ===== 0B. PRÉFÉRENCE LINGUISTIQUE =====
        {
            "id": "canada_language_preference",
            "title": "🗣️ Dans quelle langue préférez-vous vivre au quotidien ?",
            "title_en": "🗣️ What language do you prefer to live in daily?",
            "category": "language",
            "type": "single",
            "description": "Environnement linguistique souhaité pour votre nouvelle ville",
            "description_en": "Desired linguistic environment for your new city",
            "weight": 7,
            "options": [
                {
                    "value": "bilingual_comfortable",
                    "icon": "🌐",
                    "title": "Bilingue - les deux me vont",
                    "title_en": "Bilingual - both work for me",
                    "description": "Confortable en français ET anglais",
                    "description_en": "Comfortable in French AND English"
                },
                {
                    "value": "primarily_english",
                    "icon": "🇬🇧",
                    "title": "Principalement anglophone",
                    "title_en": "Mainly English-speaking",
                    "description": "Préférence pour environnement anglophone",
                    "description_en": "Preference for English-speaking environment"
                },
                {
                    "value": "primarily_french",
                    "icon": "🇫🇷",
                    "title": "Principalement francophone",
                    "title_en": "Mainly French-speaking",
                    "description": "Préférence pour environnement francophone",
                    "description_en": "Preference for French-speaking environment"
                },
                {
                    "value": "english_only",
                    "icon": "🗨️",
                    "title": "Anglais uniquement",
                    "title_en": "English only",
                    "description": "Je ne parle que l'anglais",
                    "description_en": "I only speak English"
                },
                {
                    "value": "french_only",
                    "icon": "💬",
                    "title": "Français uniquement",
                    "title_en": "French only",
                    "description": "Je ne parle que le français",
                    "description_en": "I only speak French"
                }
            ]
        },

        // ===== 1. MOTIVATION/PRIORITÉ PRINCIPALE - ACCROCHE ÉMOTIONNELLE =====
        {
            "id": "canada_main_priority",
            "title": "🎯 Qu'est-ce qui vous pousse VRAIMENT à changer de ville ?",
            "title_en": "🎯 What REALLY drives you to change cities?",
            "category": "life_priority",
            "type": "single",
            "description": "Identifie ce qui compte vraiment pour votre nouveau départ",
            "description_en": "Identify what really matters for your fresh start",
            "weight": 9,
            "options": [
                {
                    "value": "career_growth",
                    "icon": "🏃‍♂️",
                    "title": "Saisir une opportunité pro/études",
                    "title_en": "Seize a professional/study opportunity",
                    "description": "Emploi, formation, évolution professionnelle",
                    "description_en": "Employment, training, professional development",
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
                    "description": "Climat, nature, bien-être, qualité de vie",
                    "description_en": "Climate, nature, well-being, quality of life",
                    "boost_criteria": ["climate_rating", "cultural_scene", "natural_disaster_risk"]
                },
                {
                    "value": "family_focus",
                    "icon": "👨‍👩‍👧‍👦",
                    "title": "Offrir un meilleur environnement à ma famille",
                    "title_en": "Provide a better environment for my family",
                    "description": "Écoles, soins de santé, sécurité, avenir enfants",
                    "description_en": "Schools, healthcare, safety, children's future",
                    "boost_criteria": ["school_quality", "suburb_quality", "healthcare_access"]
                }
            ]
        },

        // ===== 2. PROFIL D'ÂGE ET ÉTAPE DE VIE =====
        {
            "id": "canada_age_profile",
            "title": "👤 À quelle étape de votre vie êtes-vous ?",
            "title_en": "👤 What stage of your life are you at?",
            "category": "demographics",
            "type": "single",
            "description": "Votre étape de vie influence vos priorités de relocation",
            "description_en": "Your life stage influences your relocation priorities",
            "weight": 7,
            "options": [
                {
                    "value": "student_young",
                    "icon": "🎓",
                    "title": "Étudiant/Jeune diplômé (18-25 ans)",
                    "title_en": "Student/Recent graduate (18-25 years)",
                    "description": "Université, premier job, vie sociale, budget serré",
                    "description_en": "University, first job, social life, tight budget"
                },
                {
                    "value": "young_professional",
                    "icon": "🚀",
                    "title": "Jeune professionnel (26-35 ans)",
                    "title_en": "Young professional (26-35 years)",
                    "description": "Carrière en construction, liberté, opportunités",
                    "description_en": "Career building, freedom, opportunities"
                },
                {
                    "value": "established_professional",
                    "icon": "💼",
                    "title": "Professionnel établi (36-50 ans)",
                    "title_en": "Established professional (36-50 years)",
                    "description": "Carrière stable, équilibre vie-travail, famille possible",
                    "description_en": "Stable career, work-life balance, possible family"
                },
                {
                    "value": "pre_retirement",
                    "icon": "🏡",
                    "title": "Pré-retraite/Retraité (50+ ans)",
                    "title_en": "Pre-retirement/Retired (50+ years)",
                    "description": "Confort, tranquillité, soins de santé, sérénité",
                    "description_en": "Comfort, tranquility, healthcare, serenity"
                }
            ]
        },

        // ===== 3. BUDGET LOGEMENT MENSUEL CAD =====
        {
            "id": "canada_monthly_budget",
            "title": "💳 Quel est votre budget logement mensuel ?",
            "title_en": "💳 What is your monthly housing budget?",
            "category": "financial",
            "type": "single",
            "description": "Budget mensuel pour logement (loyer/hypothèque)",
            "description_en": "Monthly budget for housing (rent/mortgage)",
            "weight": 8,
            "options": [
                {
                    "value": "budget_tight",
                    "icon": "💸",
                    "title": "Budget serré (< 1,500$ CAD/mois)",
                    "title_en": "Tight budget (< $1,500 CAD/month)",
                    "description": "Colocation, appartements économiques, villes abordables",
                    "description_en": "Roommates, budget apartments, affordable cities"
                },
                {
                    "value": "budget_balanced",
                    "icon": "💰",
                    "title": "Budget équilibré (1,500$ - 2,500$ CAD/mois)",
                    "title_en": "Balanced budget ($1,500 - $2,500 CAD/month)",
                    "description": "1-2 chambres, quartiers résidentiels moyens",
                    "description_en": "1-2 bedrooms, average residential neighborhoods"
                },
                {
                    "value": "budget_comfortable",
                    "icon": "🏠",
                    "title": "Budget confortable (2,500$ - 4,000$ CAD/mois)",
                    "title_en": "Comfortable budget ($2,500 - $4,000 CAD/month)",
                    "description": "Maison/grand appartement, bons quartiers",
                    "description_en": "House/large apartment, good neighborhoods"
                },
                {
                    "value": "budget_premium",
                    "icon": "🏛️",
                    "title": "Budget premium (4,000$+ CAD/mois)",
                    "title_en": "Premium budget ($4,000+ CAD/month)",
                    "description": "Logement haut de gamme, quartiers prestigieux",
                    "description_en": "High-end housing, prestigious neighborhoods"
                }
            ]
        },

        // ===== 4. SITUATION PROFESSIONNELLE =====
        {
            "id": "canada_work_situation",
            "title": "💻 Quelle est votre situation professionnelle ?",
            "title_en": "💻 What is your professional situation?",
            "category": "work",
            "type": "single",
            "description": "Votre situation professionnelle influence vos priorités de ville",
            "description_en": "Your professional situation influences your city priorities",
            "weight": 8,
            "options": [
                {
                    "value": "stable_employment",
                    "icon": "✅",
                    "title": "Emploi stable/permanent",
                    "title_en": "Stable/permanent employment",
                    "description": "CDI, fonction publique, grande entreprise établie",
                    "description_en": "Permanent contract, public service, established large company"
                },
                {
                    "value": "job_search",
                    "icon": "🔍",
                    "title": "Recherche d'emploi active",
                    "title_en": "Active job search",
                    "description": "Marché du travail dynamique prioritaire",
                    "description_en": "Dynamic job market is priority"
                },
                {
                    "value": "full_remote",
                    "icon": "🏠",
                    "title": "100% télétravail",
                    "title_en": "100% remote work",
                    "description": "Liberté géographique, infrastructure internet importante",
                    "description_en": "Geographic freedom, important internet infrastructure"
                },
                {
                    "value": "entrepreneur",
                    "icon": "🚀",
                    "title": "Entrepreneur/Freelance",
                    "title_en": "Entrepreneur/Freelance",
                    "description": "Écosystème startup, networking, coworking",
                    "description_en": "Startup ecosystem, networking, coworking"
                }
            ]
        },

        // ===== 5. TYPE DE LOGEMENT ET QUARTIER =====
        {
            "id": "canada_housing_preference",
            "title": "🏠 Quel type de logement et quartier préférez-vous ?",
            "title_en": "🏠 What type of housing and neighborhood do you prefer?",
            "category": "housing",
            "type": "single",
            "description": "Type de logement et environnement souhaité",
            "description_en": "Desired housing type and environment",
            "weight": 7,
            "options": [
                {
                    "value": "downtown_condo",
                    "icon": "🏢",
                    "title": "Condo centre-ville",
                    "title_en": "Downtown condo",
                    "description": "À pied du bureau, restaurants, vie urbaine intense",
                    "description_en": "Walking distance to office, restaurants, intense urban life"
                },
                {
                    "value": "suburban_house",
                    "icon": "🏡",
                    "title": "Maison de banlieue",
                    "title_en": "Suburban house",
                    "description": "Jardin, garage, tranquillité, écoles de quartier",
                    "description_en": "Garden, garage, tranquility, neighborhood schools"
                },
                {
                    "value": "transport_connected",
                    "icon": "🚇",
                    "title": "Connecté aux transports",
                    "title_en": "Connected to transport",
                    "description": "Métro/train proche, équilibre ville-banlieue",
                    "description_en": "Metro/train nearby, city-suburb balance"
                },
                {
                    "value": "budget_priority",
                    "icon": "💵",
                    "title": "Priorité au prix",
                    "title_en": "Price priority",
                    "description": "Meilleur rapport qualité-prix, emplacement flexible",
                    "description_en": "Best value for money, flexible location"
                }
            ]
        },

        // ===== 6. TRANSPORT QUOTIDIEN =====
        {
            "id": "canada_transport_preference",
            "title": "🚗 Comment souhaitez-vous vous déplacer au quotidien ?",
            "title_en": "🚗 How do you want to get around daily?",
            "category": "transport",
            "type": "single",
            "description": "Mode de transport privilégié pour vos déplacements",
            "description_en": "Preferred mode of transport for your daily commute",
            "weight": 6,
            "options": [
                {
                    "value": "walk_bike_priority",
                    "icon": "🚶",
                    "title": "Marche + Vélo prioritaires",
                    "title_en": "Walking + Biking priority",
                    "description": "Quartiers piétonniers, tout accessible à pied/vélo",
                    "description_en": "Pedestrian neighborhoods, everything accessible on foot/bike"
                },
                {
                    "value": "public_transport_fan",
                    "icon": "🚇",
                    "title": "Transport public excellent",
                    "title_en": "Excellent public transport",
                    "description": "Métro, bus, train efficaces et étendus",
                    "description_en": "Efficient and extensive metro, bus, train"
                },
                {
                    "value": "car_essential",
                    "icon": "🚗",
                    "title": "Voiture indispensable",
                    "title_en": "Car essential",
                    "description": "Stationnement facile, liberté de mouvement",
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

        // ===== 7. CLIMAT PRÉFÉRÉ =====
        {
            "id": "canada_climate_preference",
            "title": "🌡️ Quel climat canadien vous attire le plus ?",
            "title_en": "🌡️ Which Canadian climate attracts you most?",
            "category": "climate",
            "type": "single",
            "description": "Climat préféré selon les régions canadiennes",
            "description_en": "Preferred climate according to Canadian regions",
            "weight": 6,
            "options": [
                {
                    "value": "mild_coastal",
                    "icon": "🌊",
                    "title": "Côtier tempéré (Vancouver, Victoria)",
                    "title_en": "Mild coastal (Vancouver, Victoria)",
                    "description": "Hivers doux, étés frais, beaucoup de pluie",
                    "description_en": "Mild winters, cool summers, lots of rain"
                },
                {
                    "value": "continental_four_seasons",
                    "icon": "🍂",
                    "title": "Continental 4 saisons (Toronto, Montréal)",
                    "title_en": "Continental 4 seasons (Toronto, Montreal)",
                    "description": "Vrais hivers avec neige, étés chauds",
                    "description_en": "Real winters with snow, hot summers"
                },
                {
                    "value": "prairie_dry",
                    "icon": "☀️",
                    "title": "Sec des Prairies (Calgary, Edmonton)",
                    "title_en": "Prairie dry (Calgary, Edmonton)",
                    "description": "Hivers froids mais secs, étés chauds, soleil",
                    "description_en": "Cold but dry winters, hot summers, sunshine"
                },
                {
                    "value": "climate_adaptable",
                    "icon": "🔄",
                    "title": "Je m'adapte",
                    "title_en": "I adapt",
                    "description": "Le climat n'est pas déterminant",
                    "description_en": "Climate is not a determining factor"
                }
            ]
        },

        // ===== 8. SCÈNE SOCIALE ET CULTURELLE =====
        {
            "id": "canada_social_scene",
            "title": "🎭 Quelle scène sociale et culturelle vous intéresse ?",
            "title_en": "🎭 What social and cultural scene interests you?",
            "category": "lifestyle",
            "type": "single",
            "description": "Type d'activités sociales et culturelles préférées",
            "description_en": "Preferred type of social and cultural activities",
            "weight": 5,
            "options": [
                {
                    "value": "outdoor_sports",
                    "icon": "⛷️",
                    "title": "Sports et plein air",
                    "title_en": "Sports and outdoors",
                    "description": "Ski, randonnée, vélo, sports d'hiver, nature",
                    "description_en": "Skiing, hiking, biking, winter sports, nature"
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
                    "value": "dining_nightlife",
                    "icon": "🍽️",
                    "title": "Gastronomie et vie nocturne",
                    "title_en": "Gastronomy and nightlife",
                    "description": "Restaurants variés, bars, scène culinaire",
                    "description_en": "Varied restaurants, bars, culinary scene"
                },
                {
                    "value": "quiet_community",
                    "icon": "🏘️",
                    "title": "Communauté tranquille",
                    "title_en": "Quiet community",
                    "description": "Vie de quartier, événements familiaux, calme",
                    "description_en": "Neighborhood life, family events, calm"
                }
            ]
        },

        // ===== 9. SITUATION FAMILIALE =====
        {
            "id": "canada_family_situation",
            "title": "👨‍👩‍👧‍👦 Quelle est votre situation familiale ?",
            "title_en": "👨‍👩‍👧‍👦 What is your family situation?",
            "category": "family",
            "type": "single",
            "description": "Situation familiale actuelle et besoins associés",
            "description_en": "Current family situation and associated needs",
            "weight": 7,
            "options": [
                {
                    "value": "single_no_children",
                    "icon": "👤",
                    "title": "Célibataire sans enfants",
                    "title_en": "Single without children",
                    "description": "Flexibilité maximale, priorité vie sociale et carrière",
                    "description_en": "Maximum flexibility, priority on social life and career"
                },
                {
                    "value": "couple_no_children",
                    "icon": "👫",
                    "title": "Couple sans enfants",
                    "title_en": "Couple without children",
                    "description": "Vie à deux, projets communs, équilibre travail-loisirs",
                    "description_en": "Life as a couple, common projects, work-leisure balance"
                },
                {
                    "value": "young_family",
                    "icon": "👶",
                    "title": "Famille avec jeunes enfants (0-12 ans)",
                    "title_en": "Family with young children (0-12 years)",
                    "description": "Écoles primaires, parcs, sécurité, services pédiatriques",
                    "description_en": "Elementary schools, parks, safety, pediatric services"
                },
                {
                    "value": "teen_family",
                    "icon": "🎒",
                    "title": "Famille avec adolescents (13+ ans)",
                    "title_en": "Family with teenagers (13+ years)",
                    "description": "Écoles secondaires, activités ados, préparation université",
                    "description_en": "High schools, teen activities, university preparation"
                }
            ]
        },

        // ===== 10. DEAL-BREAKER =====
        {
            "id": "canada_deal_breaker",
            "title": "❌ Qu'est-ce qui vous ferait absolument éviter une ville ?",
            "title_en": "❌ What would make you absolutely avoid a city?",
            "category": "constraints",
            "type": "single",
            "description": "Critère éliminatoire absolu pour votre choix",
            "description_en": "Absolute elimination criteria for your choice",
            "weight": 8,
            "options": [
                {
                    "value": "cost_too_high",
                    "icon": "💸",
                    "title": "Coût de la vie trop élevé",
                    "title_en": "Cost of living too high",
                    "description": "Logement hors budget, épicerie chère, taxes importantes",
                    "description_en": "Housing over budget, expensive groceries, high taxes"
                },
                {
                    "value": "harsh_winter",
                    "icon": "🥶",
                    "title": "Hiver trop rigoureux",
                    "title_en": "Winter too harsh",
                    "description": "Températures extrêmes (-30°C+), hivers trop longs",
                    "description_en": "Extreme temperatures (-30°C+), winters too long"
                },
                {
                    "value": "limited_job_market",
                    "icon": "📉",
                    "title": "Marché du travail limité",
                    "title_en": "Limited job market",
                    "description": "Peu d'opportunités, économie stagnante",
                    "description_en": "Few opportunities, stagnant economy"
                },
                {
                    "value": "isolation_boredom",
                    "icon": "😴",
                    "title": "Isolement et ennui",
                    "title_en": "Isolation and boredom",
                    "description": "Ville trop petite, manque d'activités",
                    "description_en": "City too small, lack of activities"
                }
            ]
        }
    ]
};

// 🔗 Alias pour l'intégration avec analysis.js
if (typeof window.QUESTIONS_DATA === 'undefined') {
    window.QUESTIONS_DATA = {};
}

window.QUESTIONS_DATA.canada_residents = window.QUESTIONS_DATA_CANADA.canada_residents;
window.QUESTIONS_DATA.canada = window.QUESTIONS_DATA_CANADA.canada_residents;

console.log('🇨🇦 Questions Canada Residents chargées:', window.QUESTIONS_DATA_CANADA.canada_residents.length, 'questions');
