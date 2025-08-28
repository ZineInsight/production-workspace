/**
 * 🇺🇸 QUESTIONS-DATA-USA-RESIDENTS.JS - QUESTIONNAIRE RELOCATION DOMESTIQUE
 * =========================================================================
 * 10 questions OPTIMALES pour Américains cherchant nouvelle ville US
 * Author: Revolutionary Team | Version: 1.0.0 - USA Domestic Focus
 * OBJECTIF: Recommandations basées sur priorités réelles des relocations US
 */

// 🏠 QUESTIONS CENTRÉES BESOINS RELOCATION USA
window.QUESTIONS_DATA_USA = {
    "usa_residents": [

        // ===== 1. MOTIVATION/PRIORITÉ PRINCIPALE - ACCROCHE ÉMOTIONNELLE =====
        {
            "id": "usa_main_priority",
            "title": "🎯 Quelle est votre priorité #1 pour cette relocation ?",
            "title_en": "🎯 What is your #1 priority for this relocation?",
            "category": "life_priority",
            "type": "single",
            "description": "Identifie ce qui compte vraiment pour votre nouveau départ",
            "description_en": "Identifies what really matters for your new beginning",
            "weight": 9,
            "options": [
                {
                    "value": "career_growth",
                    "icon": "🚀",
                    "title": "Booster ma carrière",
                    "title_en": "Boost my career",
                    "description": "Opportunités d'emploi, networking, industries en croissance",
                    "description_en": "Job opportunities, networking, growing industries",
                    "boost_criteria": ["job_market", "tech_industry", "remote_work_friendly"]
                },
                {
                    "value": "cost_optimization",
                    "icon": "💰",
                    "title": "Optimiser mes finances",
                    "title_en": "Optimize my finances",
                    "description": "Coût de la vie, taxes, maximiser mon pouvoir d'achat",
                    "description_en": "Cost of living, taxes, maximize my purchasing power",
                    "boost_criteria": ["cost_of_living", "housing_affordability", "state_tax_burden"]
                },
                {
                    "value": "lifestyle_upgrade",
                    "icon": "🌟",
                    "title": "Améliorer ma qualité de vie",
                    "title_en": "Improve my quality of life",
                    "description": "Climat, culture, loisirs, bien-être personnel",
                    "description_en": "Climate, culture, leisure, personal well-being",
                    "boost_criteria": ["climate_rating", "cultural_scene", "restaurant_diversity"]
                },
                {
                    "value": "family_focus",
                    "icon": "👨‍👩‍👧‍👦",
                    "title": "Privilégier ma famille",
                    "title_en": "Prioritize my family",
                    "description": "Écoles, sécurité, quartiers familiaux, communauté",
                    "description_en": "Schools, security, family neighborhoods, community",
                    "boost_criteria": ["school_quality", "suburb_quality", "healthcare_access"]
                }
            ]
        },

        // ===== 2. BUDGET RÉALISTE - CONTRAINTE CONCRÈTE =====
        {
            "id": "usa_monthly_budget",
            "title": "💳 Quel est votre budget mensuel TOTAL réaliste ?",
            "title_en": "💳 What is your realistic TOTAL monthly budget?",
            "category": "financial_constraint",
            "type": "single",
            "description": "Incluant logement, transport, nourriture, loisirs - soyez honnête",
            "description_en": "Including housing, transportation, food, leisure - be honest",
            "weight": 10,
            "options": [
                {
                    "value": "budget_tight",
                    "icon": "🏦",
                    "title": "$2,000-3,500/mois - Maximiser économies",
                    "title_en": "$2,000-3,500/month - Maximize savings",
                    "description": "Villes abordables, faible coût de la vie prioritaire",
                    "description_en": "Affordable cities, low cost of living priority",
                    "boost_criteria": ["cost_of_living", "housing_affordability", "state_tax_burden"]
                },
                {
                    "value": "budget_balanced",
                    "icon": "⚖️",
                    "title": "$3,500-5,500/mois - Équilibre qualité/prix",
                    "title_en": "$3,500-5,500/month - Quality/price balance",
                    "description": "Bon rapport qualité-prix, pas les plus chères",
                    "description_en": "Good value for money, not the most expensive",
                    "boost_criteria": ["cost_of_living", "job_market", "cultural_scene"]
                },
                {
                    "value": "budget_comfortable",
                    "icon": "🏡",
                    "title": "$5,500-8,000/mois - Confort privilégié",
                    "title_en": "$5,500-8,000/month - Comfort prioritized",
                    "description": "Qualité prime sur prix, mais budget limité",
                    "description_en": "Quality over price, but limited budget",
                    "boost_criteria": ["suburb_quality", "school_quality", "healthcare_access"]
                },
                {
                    "value": "budget_premium",
                    "icon": "💎",
                    "title": "$8,000+/mois - Expérience premium",
                    "title_en": "$8,000+/month - Premium experience",
                    "description": "Le meilleur disponible, budget non-contraignant",
                    "description_en": "The best available, non-constraining budget",
                    "boost_criteria": ["cultural_scene", "restaurant_diversity", "tech_industry"]
                }
            ]
        },

        // ===== 3. SITUATION PROFESSIONNELLE - RÉALITÉ TRAVAIL =====
        {
            "id": "usa_work_situation",
            "title": "💼 Comment envisagez-vous votre situation professionnelle ?",
            "title_en": "💼 How do you envision your professional situation?",
            "category": "professional_constraint",
            "type": "single",
            "description": "Détermine l'importance du marché de l'emploi local",
            "description_en": "Determines the importance of the local job market",
            "weight": 8,
            "options": [
                {
                    "value": "remote_full",
                    "icon": "🏠",
                    "title": "100% télétravail confirmé",
                    "title_en": "100% confirmed remote work",
                    "description": "Job sécurisé, liberté géographique totale",
                    "description_en": "Secure job, total geographical freedom",
                    "boost_criteria": ["cost_of_living", "climate_rating", "cultural_scene"]
                },
                {
                    "value": "remote_hybrid",
                    "icon": "🔄",
                    "title": "Hybride/flexible",
                    "title_en": "Hybrid/flexible",
                    "description": "Télétravail partiel, déplacements occasionnels",
                    "description_en": "Partial remote work, occasional travel",
                    "boost_criteria": ["remote_work_friendly", "public_transport", "tech_industry"]
                },
                {
                    "value": "job_search",
                    "icon": "🎯",
                    "title": "Cherche nouvel emploi",
                    "title_en": "Looking for new job",
                    "description": "Besoin d'un marché de l'emploi dynamique",
                    "description_en": "Need a dynamic job market",
                    "boost_criteria": ["job_market", "tech_industry", "university_access"]
                },
                {
                    "value": "entrepreneur",
                    "icon": "🚀",
                    "title": "Entrepreneur/Freelance",
                    "title_en": "Entrepreneur/Freelance",
                    "description": "Business indépendant, networking important",
                    "description_en": "Independent business, networking important",
                    "boost_criteria": ["tech_industry", "cultural_scene", "remote_work_friendly"]
                }
            ]
        },

        // ===== 4. PRÉFÉRENCES CLIMATIQUES - CONFORT QUOTIDIEN =====
        {
            "id": "usa_climate_preference",
            "title": "🌡️ Quel climat vous fait vibrer au quotidien ?",
            "title_en": "🌡️ What climate makes you thrive daily?",
            "category": "lifestyle_preference",
            "type": "single",
            "description": "Le climat affecte votre humeur et vos activités quotidiennes",
            "description_en": "Climate affects your mood and daily activities",
            "weight": 7,
            "options": [
                {
                    "value": "warm_sunny",
                    "icon": "☀️",
                    "title": "Chaud et ensoleillé toute l'année",
                    "title_en": "Warm and sunny year-round",
                    "description": "Floride, Arizona, Sud Californie vibes",
                    "description_en": "Florida, Arizona, Southern California vibes",
                    "boost_criteria": ["climate_rating", "weather_consistency"]
                },
                {
                    "value": "four_seasons",
                    "icon": "🍂",
                    "title": "Quatre saisons distinctes",
                    "title_en": "Four distinct seasons",
                    "description": "Automne coloré, neige hivernale, printemps fleuri",
                    "description_en": "Colorful fall, winter snow, blooming spring",
                    "boost_criteria": ["climate_rating", "cultural_scene"]
                },
                {
                    "value": "mild_temperate",
                    "icon": "🌤️",
                    "title": "Doux et tempéré",
                    "title_en": "Mild and temperate",
                    "description": "Ni trop chaud ni trop froid, stable",
                    "description_en": "Neither too hot nor too cold, stable",
                    "boost_criteria": ["weather_consistency", "climate_rating"]
                },
                {
                    "value": "climate_flexible",
                    "icon": "🌍",
                    "title": "Je m'adapte facilement",
                    "title_en": "I adapt easily",
                    "description": "Le climat n'est pas un facteur décisif",
                    "description_en": "Climate is not a deciding factor",
                    "boost_criteria": ["job_market", "cost_of_living"]
                }
            ]
        },

        // ===== 5. MODE DE VIE URBAIN - ENVIRONNEMENT QUOTIDIEN =====
        {
            "id": "usa_lifestyle_density",
            "title": "🏙️ Dans quel environnement vous épanouissez-vous ?",
            "title_en": "🏙️ In what environment do you thrive?",
            "category": "lifestyle_preference",
            "type": "single",
            "description": "Votre environnement idéal pour le quotidien",
            "description_en": "Your ideal environment for daily life",
            "weight": 6,
            "options": [
                {
                    "value": "downtown_urban",
                    "icon": "🌆",
                    "title": "Centre-ville dynamique",
                    "title_en": "Dynamic downtown",
                    "description": "Gratte-ciels, tout à pied, énergie urbaine 24/7",
                    "description_en": "Skyscrapers, walkable, urban energy 24/7",
                    "boost_criteria": ["urban_density", "walkability", "public_transport"]
                },
                {
                    "value": "trendy_neighborhoods",
                    "icon": "🎨",
                    "title": "Quartiers branchés",
                    "title_en": "Trendy neighborhoods",
                    "description": "Cafés artisanaux, galleries, vie de quartier",
                    "description_en": "Artisan cafés, galleries, neighborhood life",
                    "boost_criteria": ["cultural_scene", "restaurant_diversity", "walkability"]
                },
                {
                    "value": "family_suburbs",
                    "icon": "🏡",
                    "title": "Banlieues familiales",
                    "title_en": "Family suburbs",
                    "description": "Maisons avec jardin, tranquillité, communauté",
                    "description_en": "Houses with gardens, tranquility, community",
                    "boost_criteria": ["suburb_quality", "school_quality", "car_dependency"]
                },
                {
                    "value": "small_town_charm",
                    "icon": "🌾",
                    "title": "Charme petite ville",
                    "title_en": "Small town charm",
                    "description": "Tout le monde se connaît, rythme paisible",
                    "description_en": "Everyone knows everyone, peaceful pace",
                    "boost_criteria": ["cost_of_living", "natural_disaster_risk", "healthcare_access"]
                }
            ]
        },

        // ===== 6. ATTITUDE FISCALE - RÉALITÉ ÉCONOMIQUE =====
        {
            "id": "usa_tax_philosophy",
            "title": "💸 Quelle est votre philosophie sur les taxes d'État ?",
            "title_en": "💸 What is your philosophy on state taxes?",
            "category": "financial_philosophy",
            "type": "single",
            "description": "Balance entre taxes faibles et services publics",
            "description_en": "Balance between low taxes and public services",
            "weight": 6,
            "options": [
                {
                    "value": "no_state_tax",
                    "icon": "🚫",
                    "title": "Zéro taxe d'État = priorité",
                    "title_en": "Zero state tax = priority",
                    "description": "Texas, Floride, Nevada - garder mon argent",
                    "description_en": "Texas, Florida, Nevada - keep my money",
                    "boost_criteria": ["state_tax_burden", "cost_of_living"]
                },
                {
                    "value": "low_tax_preferred",
                    "icon": "📉",
                    "title": "Taxes faibles privilégiées",
                    "title_en": "Low taxes preferred",
                    "description": "Accepte taxes modérées si autres avantages",
                    "description_en": "Accept moderate taxes if other advantages",
                    "boost_criteria": ["state_tax_burden", "property_tax", "job_market"]
                },
                {
                    "value": "balanced_services",
                    "icon": "⚖️",
                    "title": "Balance taxes/services",
                    "title_en": "Balance taxes/services",
                    "description": "OK payer si bonnes écoles, infrastructures",
                    "description_en": "OK to pay if good schools, infrastructure",
                    "boost_criteria": ["school_quality", "public_transport", "healthcare_access"]
                },
                {
                    "value": "services_priority",
                    "icon": "🏥",
                    "title": "Services publics prioritaires",
                    "title_en": "Public services priority",
                    "description": "Taxes élevées OK si excellents services",
                    "description_en": "High taxes OK if excellent services",
                    "boost_criteria": ["school_quality", "healthcare_access", "public_transport"]
                }
            ]
        },

        // ===== 7. RISQUES NATURELS - SÉCURITÉ/ASSURANCES =====
        {
            "id": "usa_disaster_tolerance",
            "title": "🌪️ Votre tolérance aux risques naturels ?",
            "title_en": "🌪️ Your tolerance for natural risks?",
            "category": "safety_preference",
            "type": "single",
            "description": "Impacts assurances, stress, préparation d'urgence",
            "description_en": "Impacts insurance, stress, emergency preparation",
            "weight": 5,
            "options": [
                {
                    "value": "risk_averse",
                    "icon": "🛡️",
                    "title": "Risque minimal exigé",
                    "title_en": "Minimal risk required",
                    "description": "Éviter ouragans, tornades, tremblements de terre",
                    "description_en": "Avoid hurricanes, tornadoes, earthquakes",
                    "boost_criteria": ["natural_disaster_risk", "hurricane_risk", "earthquake_risk"]
                },
                {
                    "value": "manageable_risk",
                    "icon": "⚠️",
                    "title": "Risques gérables acceptés",
                    "title_en": "Manageable risks accepted",
                    "description": "OK avec préparation et assurances adéquates",
                    "description_en": "OK with adequate preparation and insurance",
                    "boost_criteria": ["natural_disaster_risk", "healthcare_access"]
                },
                {
                    "value": "weather_excitement",
                    "icon": "⛈️",
                    "title": "J'aime la nature dramatique",
                    "title_en": "I love dramatic nature",
                    "description": "Ouragans/tornades = excitant, pas effrayant",
                    "description_en": "Hurricanes/tornadoes = exciting, not scary",
                    "boost_criteria": ["climate_rating", "cost_of_living"]
                },
                {
                    "value": "risk_irrelevant",
                    "icon": "🤷",
                    "title": "Risques pas décisifs",
                    "title_en": "Risks not decisive",
                    "description": "Autres facteurs plus importants",
                    "description_en": "Other factors more important",
                    "boost_criteria": ["job_market", "cultural_scene"]
                }
            ]
        },

        // ===== 8. TRANSPORT/MOBILITÉ - RÉALITÉ QUOTIDIENNE =====
        {
            "id": "usa_transport_preference",
            "title": "🚗 Comment envisagez-vous vos déplacements quotidiens ?",
            "title_en": "🚗 How do you envision your daily transportation?",
            "category": "mobility_preference",
            "type": "single",
            "description": "Impact budget, temps, style de vie quotidien",
            "description_en": "Impacts budget, time, daily lifestyle",
            "weight": 5,
            "options": [
                {
                    "value": "car_free_dream",
                    "icon": "🚶",
                    "title": "Vivre sans voiture",
                    "title_en": "Live without a car",
                    "description": "Marche, vélo, transports publics uniquement",
                    "description_en": "Walking, biking, public transport only",
                    "boost_criteria": ["walkability", "public_transport", "urban_density"]
                },
                {
                    "value": "public_transport",
                    "icon": "🚇",
                    "title": "Transports publics + marche",
                    "title_en": "Public transport + walking",
                    "description": "Voiture pour week-ends/urgences seulement",
                    "description_en": "Car for weekends/emergencies only",
                    "boost_criteria": ["public_transport", "walkability", "cultural_scene"]
                },
                {
                    "value": "car_convenient",
                    "icon": "🚙",
                    "title": "Voiture pratique mais pas unique",
                    "title_en": "Car convenient but not exclusive",
                    "description": "Mix transport selon besoins",
                    "description_en": "Mix transport according to needs",
                    "boost_criteria": ["suburb_quality", "public_transport"]
                },
                {
                    "value": "car_essential",
                    "icon": "🛻",
                    "title": "Voiture indispensable",
                    "title_en": "Car essential",
                    "description": "American way, liberté totale de mouvement",
                    "description_en": "American way, total freedom of movement",
                    "boost_criteria": ["car_dependency", "cost_of_living", "suburb_quality"]
                }
            ]
        },

        // ===== 9. ÉDUCATION/FAMILLE - INVESTISSEMENT FUTUR =====
        {
            "id": "usa_education_priority",
            "title": "🎓 Quelle importance accordez-vous à l'éducation ?",
            "title_en": "🎓 How much importance do you place on education?",
            "category": "family_planning",
            "type": "single",
            "description": "Écoles publiques, universités, développement personnel",
            "description_en": "Public schools, universities, personal development",
            "weight": 4,
            "options": [
                {
                    "value": "top_schools_essential",
                    "icon": "🏆",
                    "title": "Écoles top niveau exigées",
                    "title_en": "Top-level schools required",
                    "description": "Enfants présents/futurs - excellence académique",
                    "description_en": "Current/future children - academic excellence",
                    "boost_criteria": ["school_quality", "university_access", "suburb_quality"]
                },
                {
                    "value": "good_schools_preferred",
                    "icon": "📚",
                    "title": "Bonnes écoles privilégiées",
                    "title_en": "Good schools preferred",
                    "description": "Équilibre qualité/coût éducation",
                    "description_en": "Quality/cost education balance",
                    "boost_criteria": ["school_quality", "cost_of_living"]
                },
                {
                    "value": "university_access",
                    "icon": "🎯",
                    "title": "Accès universités important",
                    "title_en": "University access important",
                    "description": "Formation continue, opportunités adultes",
                    "description_en": "Continuing education, adult opportunities",
                    "boost_criteria": ["university_access", "cultural_scene"]
                },
                {
                    "value": "education_flexible",
                    "icon": "🌐",
                    "title": "Éducation pas priorité actuelle",
                    "title_en": "Education not current priority",
                    "description": "Autres facteurs plus décisifs maintenant",
                    "description_en": "Other factors more decisive now",
                    "boost_criteria": ["job_market", "nightlife", "cultural_scene"]
                }
            ]
        },

        // ===== 10. VIE SOCIALE/CULTURELLE - ÉPANOUISSEMENT PERSONNEL =====
        {
            "id": "usa_social_scene",
            "title": "🎭 Quel type de scène sociale vous anime ?",
            "title_en": "🎭 What type of social scene excites you?",
            "category": "lifestyle_fulfillment",
            "type": "single",
            "description": "Votre épanouissement social et culturel",
            "description_en": "Your social and cultural fulfillment",
            "weight": 6,
            "options": [
                {
                    "value": "foodie_culture",
                    "icon": "🍜",
                    "title": "Scène culinaire diversifiée",
                    "title_en": "Diverse culinary scene",
                    "description": "Restaurants ethniques, food trucks, gastronomie",
                    "description_en": "Ethnic restaurants, food trucks, gastronomy",
                    "boost_criteria": ["restaurant_diversity", "cultural_scene"]
                },
                {
                    "value": "nightlife_entertainment",
                    "icon": "🍻",
                    "title": "Vie nocturne dynamique",
                    "title_en": "Dynamic nightlife",
                    "description": "Bars, clubs, concerts, événements nocturnes",
                    "description_en": "Bars, clubs, concerts, nighttime events",
                    "boost_criteria": ["nightlife", "cultural_scene", "urban_density"]
                },
                {
                    "value": "arts_culture",
                    "icon": "🎨",
                    "title": "Arts et culture",
                    "title_en": "Arts and culture",
                    "description": "Musées, théâtres, galeries, festivals",
                    "description_en": "Museums, theaters, galleries, festivals",
                    "boost_criteria": ["cultural_scene", "university_access"]
                },
                {
                    "value": "quiet_community",
                    "icon": "☕",
                    "title": "Communauté tranquille",
                    "title_en": "Quiet community",
                    "description": "Cercles restreints, activités calmes",
                    "description_en": "Close circles, calm activities",
                    "boost_criteria": ["suburb_quality", "cost_of_living", "natural_disaster_risk"]
                }
            ]
        }
    ]
};

// 🎯 SYSTÈME DE SCORING POUR ALGORITHME USA RESIDENTS
window.USA_SCORING_SYSTEM = {
    "version": "1.0.0",
    "total_questions": 10,
    "max_weight": 10,
    "criteria_mapping": {
        // Critères financiers
        "cost_of_living": "Coût de la vie global",
        "housing_affordability": "Accessibilité logement",
        "state_tax_burden": "Charge fiscale d'État",
        "sales_tax": "Taxe sur ventes",
        "property_tax": "Taxe foncière",

        // Critères climatiques
        "climate_rating": "Qualité du climat",
        "weather_consistency": "Consistance météo",

        // Critères professionnels
        "job_market": "Marché de l'emploi",
        "tech_industry": "Industrie technologique",
        "remote_work_friendly": "Télétravail friendly",

        // Critères urbains/lifestyle
        "urban_density": "Densité urbaine",
        "suburb_quality": "Qualité banlieues",
        "walkability": "Marchabilité",
        "public_transport": "Transports publics",
        "car_dependency": "Dépendance voiture",

        // Critères éducation/famille
        "school_quality": "Qualité écoles",
        "university_access": "Accès universités",

        // Critères risques
        "natural_disaster_risk": "Risques naturels",
        "hurricane_risk": "Risque ouragans",
        "earthquake_risk": "Risque séismes",

        // Critères santé
        "healthcare_access": "Accès soins de santé",
        "hospital_quality": "Qualité hôpitaux",

        // Critères culturels
        "cultural_scene": "Scène culturelle",
        "restaurant_diversity": "Diversité culinaire",
        "nightlife": "Vie nocturne"
    },
    "algorithm_notes": "Système conçu pour matcher les priorités de relocation domestique américaine"
};

// 🔗 INTÉGRATION DANS LE SYSTÈME PRINCIPAL
if (typeof window.QUESTIONS_DATA === 'undefined') {
    window.QUESTIONS_DATA = {};
}
window.QUESTIONS_DATA.usa_residents = window.QUESTIONS_DATA_USA.usa_residents;
// Alias pour compatibilité avec analysis.js
window.QUESTIONS_DATA.usa = window.QUESTIONS_DATA_USA.usa_residents;

console.log("✅ USA Residents Questions Data loaded - 10 questions, 25 criteria mapping");
