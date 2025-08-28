/**
 * 🇯🇵 QUESTIONS-DATA-JP-RESIDENTS.JS - QUESTIONNAIRE RELOCATION DOMESTIQUE JAPON
 * ================================================================================
 * 12 questions OPTIMALES pour Japonais cherchant nouvelle ville au Japon
 * Author: Revolutionary Team | Version: 1.0.0 - Japan Domestic Focus
 * OBJECTIF: Recommandations basées sur profils réels des relocations japonaises
 */

// 🏠 QUESTIONS CENTRÉES BESOINS RELOCATION JAPON
window.QUESTIONS_DATA_JAPAN = {
    "japan_residents": [

        // ===== 0A. PRÉFÉRENCE RÉGIONALE JAPON =====
        {
            "id": "japan_region_preference",
            "title": "🗺️ Quelle région du Japon vous attire le plus ?",
            "title_en": "🗺️ Which region of Japan attracts you most?",
            "category": "geography",
            "type": "single",
            "description": "Choisissez votre zone géographique préférée au Japon",
            "description_en": "Choose your preferred geographical area in Japan",
            "weight": 8,
            "options": [
                {
                    "value": "any_region",
                    "icon": "🇯🇵",
                    "title": "Ouvert à toutes les régions",
                    "title_en": "Open to all regions",
                    "description": "Je suis flexible, recommandez-moi partout au Japon",
                    "description_en": "I'm flexible, recommend anywhere in Japan"
                },
                {
                    "value": "kanto",
                    "icon": "🏙️",
                    "title": "Région Kanto",
                    "title_en": "Kanto Region",
                    "description": "Tokyo, Yokohama, Kawasaki, Saitama, Chiba",
                    "description_en": "Tokyo, Yokohama, Kawasaki, Saitama, Chiba"
                },
                {
                    "value": "kansai",
                    "icon": "🏛️",
                    "title": "Région Kansai",
                    "title_en": "Kansai Region",
                    "description": "Osaka, Kyoto, Kobe, Nara - Culture traditionnelle",
                    "description_en": "Osaka, Kyoto, Kobe, Nara - Traditional culture"
                },
                {
                    "value": "chubu",
                    "icon": "🏔️",
                    "title": "Région Chubu",
                    "title_en": "Chubu Region",
                    "description": "Nagoya, Kanazawa, Shizuoka, Gifu, Toyama",
                    "description_en": "Nagoya, Kanazawa, Shizuoka, Gifu, Toyama"
                },
                {
                    "value": "kyushu",
                    "icon": "🌋",
                    "title": "Kyushu",
                    "title_en": "Kyushu",
                    "description": "Fukuoka, Kumamoto, Kagoshima - Startup scene",
                    "description_en": "Fukuoka, Kumamoto, Kagoshima - Startup scene"
                },
                {
                    "value": "hokkaido_tohoku",
                    "icon": "❄️",
                    "title": "Hokkaido & Tohoku",
                    "title_en": "Hokkaido & Tohoku",
                    "description": "Sapporo, Sendai, Akita - Qualité de vie nordique",
                    "description_en": "Sapporo, Sendai, Akita - Northern quality of life"
                }
            ]
        },

        // ===== 1. PRIORITÉ PRINCIPALE JAPON =====
        {
            "id": "japan_main_priority",
            "title": "🎯 Quelle est votre priorité principale pour votre relocation au Japon ?",
            "title_en": "🎯 What is your main priority for your relocation in Japan?",
            "category": "life_priority",
            "type": "single",
            "description": "Votre motivation #1 pour changer de ville au Japon",
            "description_en": "Your #1 motivation for changing cities in Japan",
            "weight": 9,
            "options": [
                {
                    "value": "career_tokyo",
                    "icon": "💼",
                    "title": "Booster ma carrière à Tokyo/grandes villes",
                    "title_en": "Boost my career in Tokyo/big cities",
                    "description": "Opportunités emploi, networking, salaires élevés",
                    "description_en": "Job opportunities, networking, high salaries"
                },
                {
                    "value": "work_life_balance",
                    "icon": "⚖️",
                    "title": "Améliorer mon work-life balance",
                    "title_en": "Improve my work-life balance",
                    "description": "Moins d'heures sup, plus de temps personnel",
                    "description_en": "Fewer overtime hours, more personal time"
                },
                {
                    "value": "traditional_culture",
                    "icon": "🏯",
                    "title": "Vivre la culture traditionnelle japonaise",
                    "title_en": "Experience traditional Japanese culture",
                    "description": "Temples, artisanat, modes de vie authentiques",
                    "description_en": "Temples, craftsmanship, authentic lifestyles"
                },
                {
                    "value": "cost_optimization",
                    "icon": "💰",
                    "title": "Réduire mes coûts de vie",
                    "title_en": "Reduce my cost of living",
                    "description": "Logement abordable, vie moins chère qu'à Tokyo",
                    "description_en": "Affordable housing, cheaper life than Tokyo"
                }
            ]
        },

        // ===== 2. PROFIL D'ÂGE JAPON =====
        {
            "id": "japan_age_profile",
            "title": "👤 Quel est votre profil d'âge et situation de vie ?",
            "title_en": "👤 What is your age profile and life situation?",
            "category": "demographics",
            "type": "single",
            "description": "Votre tranche d'âge pour adapter les recommandations",
            "description_en": "Your age range to adapt recommendations",
            "weight": 7,
            "options": [
                {
                    "value": "new_graduate",
                    "icon": "🎓",
                    "title": "Nouveau diplômé (22-25 ans)",
                    "title_en": "New graduate (22-25 years)",
                    "description": "Premier emploi, découverte vie active",
                    "description_en": "First job, discovering active life"
                },
                {
                    "value": "young_professional",
                    "icon": "🏃‍♂️",
                    "title": "Young professional (26-35 ans)",
                    "title_en": "Young professional (26-35 years)",
                    "description": "Carrière en développement, énergie, ambitions",
                    "description_en": "Developing career, energy, ambitions"
                },
                {
                    "value": "mid_career",
                    "icon": "💼",
                    "title": "Mi-carrière établie (36-50 ans)",
                    "title_en": "Established mid-career (36-50 years)",
                    "description": "Expérience solide, recherche équilibre et qualité",
                    "description_en": "Solid experience, seeking balance and quality"
                },
                {
                    "value": "pre_retirement",
                    "icon": "🌸",
                    "title": "Pré-retraite (50+ ans)",
                    "title_en": "Pre-retirement (50+ years)",
                    "description": "Sérénité, santé, culture, slow living",
                    "description_en": "Serenity, health, culture, slow living"
                }
            ]
        },

        // ===== 3. BUDGET MENSUEL JAPON =====
        {
            "id": "japan_monthly_budget",
            "title": "💰 Quel est votre budget mensuel total (logement + vie) ?",
            "title_en": "💰 What is your total monthly budget (housing + living)?",
            "category": "financial",
            "type": "single",
            "description": "Budget réaliste pour votre nouveau mode de vie",
            "description_en": "Realistic budget for your new lifestyle",
            "weight": 8,
            "options": [
                {
                    "value": "budget_student",
                    "icon": "💸",
                    "title": "¥200K-300K par mois",
                    "title_en": "¥200K-300K per month",
                    "description": "Étudiant, débutant, vie simple",
                    "description_en": "Student, beginner, simple life"
                },
                {
                    "value": "budget_balanced",
                    "icon": "💴",
                    "title": "¥300K-500K par mois",
                    "title_en": "¥300K-500K per month",
                    "description": "Équilibré, confortable sans excès",
                    "description_en": "Balanced, comfortable without excess"
                },
                {
                    "value": "budget_comfortable",
                    "icon": "💵",
                    "title": "¥500K-800K par mois",
                    "title_en": "¥500K-800K per month",
                    "description": "Aisé, choix multiples, loisirs inclus",
                    "description_en": "Well-off, multiple choices, leisure included"
                },
                {
                    "value": "budget_premium",
                    "icon": "💎",
                    "title": "¥800K+ par mois",
                    "title_en": "¥800K+ per month",
                    "description": "Premium, Tokyo central accessible",
                    "description_en": "Premium, central Tokyo accessible"
                }
            ]
        },

        // ===== 4. SITUATION TRAVAIL =====
        {
            "id": "japan_work_situation",
            "title": "💼 Quelle est votre situation professionnelle actuelle ?",
            "title_en": "💼 What is your current professional situation?",
            "category": "professional",
            "type": "single",
            "description": "Type d'emploi pour orienter vers les bonnes villes",
            "description_en": "Job type to guide towards the right cities",
            "weight": 8,
            "options": [
                {
                    "value": "salaryman",
                    "icon": "👔",
                    "title": "Salaryman traditionnel",
                    "title_en": "Traditional salaryman",
                    "description": "Grande entreprise, bureau fixe, hiérarchie",
                    "description_en": "Large company, fixed office, hierarchy"
                },
                {
                    "value": "tech_startup",
                    "icon": "💻",
                    "title": "IT/Tech/Startup",
                    "title_en": "IT/Tech/Startup",
                    "description": "Technologie, innovation, environnement dynamique",
                    "description_en": "Technology, innovation, dynamic environment"
                },
                {
                    "value": "freelance_remote",
                    "icon": "🏠",
                    "title": "Freelance/Télétravail",
                    "title_en": "Freelance/Remote work",
                    "description": "Autonomie géographique, flexibilité horaire",
                    "description_en": "Geographic autonomy, schedule flexibility"
                },
                {
                    "value": "job_hunting",
                    "icon": "🔍",
                    "title": "En recherche d'emploi",
                    "title_en": "Job hunting",
                    "description": "Changement carrière, opportunités à saisir",
                    "description_en": "Career change, opportunities to seize"
                }
            ]
        },

        // ===== 5. PRÉFÉRENCE TRANSPORT =====
        {
            "id": "japan_transport_preference",
            "title": "🚊 Quel type de transport privilégiez-vous au quotidien ?",
            "title_en": "🚊 What type of transport do you prioritize daily?",
            "category": "mobility",
            "type": "single",
            "description": "Mode de déplacement principal souhaité",
            "description_en": "Desired main mode of transportation",
            "weight": 7,
            "options": [
                {
                    "value": "jr_priority",
                    "icon": "🚄",
                    "title": "JR/Shinkansen prioritaire",
                    "title_en": "JR/Shinkansen priority",
                    "description": "Mobilité nationale, voyages, connexions rapides",
                    "description_en": "National mobility, travel, fast connections"
                },
                {
                    "value": "metro_urban",
                    "icon": "🚇",
                    "title": "Métro urbain dense",
                    "title_en": "Dense urban metro",
                    "description": "Tokyo/Osaka, transport en commun intensif",
                    "description_en": "Tokyo/Osaka, intensive public transport"
                },
                {
                    "value": "bicycle_friendly",
                    "icon": "🚲",
                    "title": "Vélo + marche à pied",
                    "title_en": "Bike + walking",
                    "description": "Écologique, santé, distances courtes",
                    "description_en": "Ecological, health, short distances"
                },
                {
                    "value": "car_acceptable",
                    "icon": "🚗",
                    "title": "Voiture acceptable",
                    "title_en": "Car acceptable",
                    "description": "Flexibilité, banlieues, régions moins denses",
                    "description_en": "Flexibility, suburbs, less dense regions"
                }
            ]
        },

        // ===== 6. PRÉFÉRENCE LOGEMENT =====
        {
            "id": "japan_housing_preference",
            "title": "🏠 Quel type de logement recherchez-vous ?",
            "title_en": "🏠 What type of housing are you looking for?",
            "category": "housing",
            "type": "single",
            "description": "Style de vie résidentiel souhaité",
            "description_en": "Desired residential lifestyle",
            "weight": 7,
            "options": [
                {
                    "value": "city_manshion",
                    "icon": "🏢",
                    "title": "Manshion centre-ville",
                    "title_en": "City center mansion",
                    "description": "Appartement moderne, commodités, vie urbaine",
                    "description_en": "Modern apartment, amenities, urban life"
                },
                {
                    "value": "suburban_house",
                    "icon": "🏘️",
                    "title": "Maison banlieue résidentielle",
                    "title_en": "Suburban residential house",
                    "description": "Espace, jardin, tranquillité familiale",
                    "description_en": "Space, garden, family tranquility"
                },
                {
                    "value": "station_proximity",
                    "icon": "🚉",
                    "title": "Proximité gare prioritaire",
                    "title_en": "Station proximity priority",
                    "description": "Mobilité facile, moins de 10min à pied",
                    "description_en": "Easy mobility, less than 10min walk"
                },
                {
                    "value": "price_priority",
                    "icon": "💰",
                    "title": "Prix abordable prioritaire",
                    "title_en": "Affordable price priority",
                    "description": "Budget optimisé, compromis sur localisation",
                    "description_en": "Optimized budget, compromise on location"
                }
            ]
        },

        // ===== 7. PRÉFÉRENCE CLIMAT =====
        {
            "id": "japan_climate_preference",
            "title": "🌤️ Quel climat vous convient le mieux ?",
            "title_en": "🌤️ Which climate suits you best?",
            "category": "environment",
            "type": "single",
            "description": "Conditions météorologiques préférées",
            "description_en": "Preferred weather conditions",
            "weight": 7,
            "options": [
                {
                    "value": "four_seasons",
                    "icon": "🌸",
                    "title": "Quatre saisons distinctes",
                    "title_en": "Four distinct seasons",
                    "description": "Sakura, été chaud, automne coloré, hiver neigeux",
                    "description_en": "Sakura, hot summer, colorful autumn, snowy winter"
                },
                {
                    "value": "mild_winter",
                    "icon": "🌊",
                    "title": "Hiver doux",
                    "title_en": "Mild winter",
                    "description": "Sud du Japon, côtes, températures clémentes",
                    "description_en": "Southern Japan, coasts, mild temperatures"
                },
                {
                    "value": "cool_summer",
                    "icon": "🏔️",
                    "title": "Été supportable",
                    "title_en": "Bearable summer",
                    "description": "Hokkaido, montagnes, chaleur modérée",
                    "description_en": "Hokkaido, mountains, moderate heat"
                },
                {
                    "value": "climate_flexible",
                    "icon": "🌏",
                    "title": "Je m'adapte au climat",
                    "title_en": "I adapt to climate",
                    "description": "Priorité aux autres critères",
                    "description_en": "Priority to other criteria"
                }
            ]
        },

        // ===== 8. SCÈNE SOCIALE =====
        {
            "id": "japan_social_scene",
            "title": "🍻 Quelle ambiance sociale vous attire ?",
            "title_en": "🍻 What social atmosphere attracts you?",
            "category": "lifestyle",
            "type": "single",
            "description": "Type de vie sociale et sorties préférées",
            "description_en": "Type of social life and preferred outings",
            "weight": 7,
            "options": [
                {
                    "value": "izakaya_traditional",
                    "icon": "🏮",
                    "title": "Izakaya & culture traditionnelle",
                    "title_en": "Izakaya & traditional culture",
                    "description": "Sake, nomikai, festivals, vie de quartier",
                    "description_en": "Sake, nomikai, festivals, neighborhood life"
                },
                {
                    "value": "modern_nightlife",
                    "icon": "🌃",
                    "title": "Nightlife moderne international",
                    "title_en": "Modern international nightlife",
                    "description": "Bars branchés, clubs, scène cosmopolite",
                    "description_en": "Trendy bars, clubs, cosmopolitan scene"
                },
                {
                    "value": "arts_culture",
                    "icon": "🎭",
                    "title": "Arts, musées, spectacles",
                    "title_en": "Arts, museums, shows",
                    "description": "Expositions, théâtre, concerts, culture raffinée",
                    "description_en": "Exhibitions, theater, concerts, refined culture"
                },
                {
                    "value": "quiet_residential",
                    "icon": "🌿",
                    "title": "Calme résidentiel",
                    "title_en": "Quiet residential",
                    "description": "Tranquillité, nature, vie de famille paisible",
                    "description_en": "Tranquility, nature, peaceful family life"
                }
            ]
        },

        // ===== 9. SITUATION FAMILIALE =====
        {
            "id": "japan_family_situation",
            "title": "👨‍👩‍👧‍👦 Quelle est votre situation familiale ?",
            "title_en": "👨‍👩‍👧‍👦 What is your family situation?",
            "category": "family",
            "type": "single",
            "description": "Composition familiale pour adapter les services",
            "description_en": "Family composition to adapt services",
            "weight": 8,
            "options": [
                {
                    "value": "single_independent",
                    "icon": "🧑‍💼",
                    "title": "Célibataire indépendant",
                    "title_en": "Independent single",
                    "description": "Liberté, mobilité, choix personnels",
                    "description_en": "Freedom, mobility, personal choices"
                },
                {
                    "value": "couple_no_children",
                    "icon": "👫",
                    "title": "Couple sans enfants",
                    "title_en": "Couple without children",
                    "description": "Vie à deux, sorties, projets communs",
                    "description_en": "Life as a couple, outings, shared projects"
                },
                {
                    "value": "young_family",
                    "icon": "👶",
                    "title": "Jeune famille (0-12 ans)",
                    "title_en": "Young family (0-12 years)",
                    "description": "Bébés, enfants, services familiaux, sécurité",
                    "description_en": "Babies, children, family services, safety"
                },
                {
                    "value": "school_age_family",
                    "icon": "🎒",
                    "title": "Famille enfants scolarisés",
                    "title_en": "Family with school-age children",
                    "description": "Écoles, activités, éducation, stabilité",
                    "description_en": "Schools, activities, education, stability"
                }
            ]
        },

        // ===== 10. TOLÉRANCE RISQUES NATURELS =====
        {
            "id": "japan_disaster_tolerance",
            "title": "⚡ Quelle est votre tolérance aux risques naturels ?",
            "title_en": "⚡ What is your tolerance for natural risks?",
            "category": "safety",
            "type": "single",
            "description": "Acceptation des aléas naturels japonais",
            "description_en": "Acceptance of Japanese natural hazards",
            "weight": 7,
            "options": [
                {
                    "value": "earthquake_prepared",
                    "icon": "🏗️",
                    "title": "Séismes OK si bien préparé",
                    "title_en": "Earthquakes OK if well prepared",
                    "description": "Normes antisismiques, kits d'urgence, sensibilisation",
                    "description_en": "Seismic standards, emergency kits, awareness"
                },
                {
                    "value": "typhoon_acceptable",
                    "icon": "🌀",
                    "title": "Typhons supportables",
                    "title_en": "Typhoons bearable",
                    "description": "Prévisibles, préparation possible, courte durée",
                    "description_en": "Predictable, preparation possible, short duration"
                },
                {
                    "value": "tsunami_avoid",
                    "icon": "🌊",
                    "title": "Éviter les zones tsunami",
                    "title_en": "Avoid tsunami zones",
                    "description": "Priorité régions intérieures, altitude",
                    "description_en": "Priority inland regions, altitude"
                },
                {
                    "value": "all_risks_ok",
                    "icon": "⚖️",
                    "title": "Tous risques acceptables",
                    "title_en": "All risks acceptable",
                    "description": "Priorité autres critères, confiance préparation",
                    "description_en": "Priority other criteria, trust in preparation"
                }
            ]
        },

        // ===== 11. DEAL BREAKER =====
        {
            "id": "japan_deal_breaker",
            "title": "❌ Qu'est-ce qui vous ferait absolument fuir une ville ?",
            "title_en": "❌ What would make you absolutely avoid a city?",
            "category": "constraints",
            "type": "single",
            "description": "Votre critère rédhibitoire principal",
            "description_en": "Your main deal-breaker criterion",
            "weight": 8,
            "options": [
                {
                    "value": "tokyo_too_expensive",
                    "icon": "💸",
                    "title": "Tokyo trop cher",
                    "title_en": "Tokyo too expensive",
                    "description": "Coût vie/logement prohibitif, budget serré",
                    "description_en": "Prohibitive living/housing costs, tight budget"
                },
                {
                    "value": "isolated_countryside",
                    "icon": "🏔️",
                    "title": "Campagne trop isolée",
                    "title_en": "Too isolated countryside",
                    "description": "Manque services, transports, opportunités",
                    "description_en": "Lack of services, transport, opportunities"
                },
                {
                    "value": "limited_job_market",
                    "icon": "💼",
                    "title": "Peu d'opportunités emploi",
                    "title_en": "Limited job opportunities",
                    "description": "Marché travail restreint, pas d'évolution",
                    "description_en": "Restricted job market, no advancement"
                },
                {
                    "value": "language_barrier",
                    "icon": "🗣️",
                    "title": "Barrière culturelle forte",
                    "title_en": "Strong cultural barrier",
                    "description": "Dialecte local fort, communauté fermée",
                    "description_en": "Strong local dialect, closed community"
                }
            ]
        }

    ] // Fin japan_residents
}; // Fin QUESTIONS_DATA_JAPAN

// ===== ALIAS POUR ANALYSIS.JS - OBLIGATOIRE =====
window.QUESTIONS_DATA = window.QUESTIONS_DATA || {};
window.QUESTIONS_DATA.japan_residents = window.QUESTIONS_DATA_JAPAN.japan_residents;
window.QUESTIONS_DATA.japan = window.QUESTIONS_DATA_JAPAN.japan_residents;
