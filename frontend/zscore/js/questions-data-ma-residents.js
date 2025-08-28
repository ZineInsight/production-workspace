/**
 * 🇲🇦 QUESTIONS-DATA-MA-RESIDENTS.JS - QUESTIONNAIRE RELOCATION DOMESTIQUE MAROC
 * ==================================================================================
 * 12 questions OPTIMALES pour Marocains/résidents cherchant nouvelle ville au Maroc
 * Author: Revolutionary Team | Version: 1.0.0 - Morocco Domestic Focus
 * OBJECTIF: Recommandations basées sur 25 villes + 27 critères spécifiques Maroc
 * INCLUSIVITÉ: Questions neutres pour résidents ET expats potentiels
 */

// 🏠 QUESTIONS CENTRÉES BESOINS RELOCATION MAROC
window.QUESTIONS_DATA_MOROCCO = {
    "morocco_residents": [

        // ===== 0A. PRÉFÉRENCE RÉGIONALE MAROC =====
        {
            "id": "morocco_region_preference",
            "title": "🗺️ Quelle région du Maroc vous attire le plus ?",
            "title_en": "🗺️ Which region of Morocco attracts you the most?",
            "category": "geography",
            "type": "single",
            "description": "Choisissez votre zone géographique préférée au Maroc",
            "description_en": "Choose your preferred geographical area in Morocco",
            "weight": 8,
            "options": [
                {
                    "value": "any_region",
                    "icon": "🇲🇦",
                    "title": "Ouvert à toutes les régions",
                    "title_en": "Open to all regions",
                    "description": "Je suis flexible, recommandez-moi partout au Maroc",
                    "description_en": "I'm flexible, recommend me anywhere in Morocco"
                },
                {
                    "value": "atlantic_coast",
                    "icon": "🌊",
                    "title": "Côte Atlantique",
                    "title_en": "Atlantic Coast",
                    "description": "Casablanca, Rabat, Agadir, Mohammedia, El Jadida",
                    "description_en": "Casablanca, Rabat, Agadir, Mohammedia, El Jadida"
                },
                {
                    "value": "mediterranean",
                    "icon": "🏖️",
                    "title": "Méditerranée",
                    "title_en": "Mediterranean",
                    "description": "Tanger, Tétouan, Al Hoceïma, Nador, Larache",
                    "description_en": "Tangier, Tetouan, Al Hoceima, Nador, Larache"
                },
                {
                    "value": "imperial_cities",
                    "icon": "🏛️",
                    "title": "Villes Impériales",
                    "title_en": "Imperial Cities",
                    "description": "Fès, Meknès, Marrakech - patrimoine et tradition",
                    "description_en": "Fez, Meknes, Marrakech - heritage and tradition"
                },
                {
                    "value": "atlas_mountains",
                    "icon": "🏔️",
                    "title": "Atlas et Rif",
                    "title_en": "Atlas and Rif",
                    "description": "Ifrane, Chefchaouen, Béni Mellal, Khénifra",
                    "description_en": "Ifrane, Chefchaouen, Beni Mellal, Khenifra"
                },
                {
                    "value": "sahara_gateway",
                    "icon": "🏜️",
                    "title": "Portes du Sahara",
                    "title_en": "Sahara Gateway",
                    "description": "Ouarzazate, Errachidia, Laâyoune - désert et aventure",
                    "description_en": "Ouarzazate, Errachidia, Laayoune - desert and adventure"
                }
            ]
        },

        // ===== 0B. ENVIRONNEMENT SOUHAITÉ =====
        {
            "id": "morocco_environment_type",
            "title": "🏙️ Quel type d'environnement vous correspond le mieux ?",
            "category": "lifestyle",
            "type": "single",
            "description": "Style de vie et d'environnement préféré",
            "weight": 7,
            "options": [
                {
                    "value": "major_metropolis",
                    "icon": "🏙️",
                    "title": "Grande métropole moderne",
                    "description": "Business, gratte-ciels, vie urbaine intense"
                },
                {
                    "value": "coastal_relaxed",
                    "icon": "🌅",
                    "title": "Ville côtière détendue",
                    "description": "Plages, climat océanique, rythme apaisé"
                },
                {
                    "value": "mountain_nature",
                    "icon": "🌲",
                    "title": "Ville montagnarde nature",
                    "description": "Air pur, forêts, activités outdoor"
                },
                {
                    "value": "heritage_authentic",
                    "icon": "🕌",
                    "title": "Ville patrimoniale authentique",
                    "description": "Médina, souks, architecture traditionnelle"
                },
                {
                    "value": "balanced_modern",
                    "icon": "⚖️",
                    "title": "Équilibre moderne-traditionnel",
                    "description": "Mix parfait entre innovation et héritage"
                }
            ]
        },

        // ===== 1. MOTIVATION/PRIORITÉ PRINCIPALE =====
        {
            "id": "morocco_main_priority",
            "title": "🎯 Qu'est-ce qui vous pousse VRAIMENT à changer de ville ?",
            "title_en": "🎯 What REALLY drives you to change cities?",
            "category": "life_priority",
            "type": "single",
            "description": "Identifie ce qui compte vraiment pour votre nouveau départ",
            "description_en": "Identify what truly matters for your fresh start",
            "weight": 9,
            "options": [
                {
                    "value": "career_growth",
                    "icon": "🚀",
                    "title": "Saisir une opportunité professionnelle",
                    "title_en": "Seize a professional opportunity",
                    "description": "Emploi, startup, secteur dynamique, networking",
                    "description_en": "Job, startup, dynamic sector, networking",
                    "boost_criteria": ["job_opportunities", "tech_scene", "business_environment"]
                },
                {
                    "value": "cost_optimization",
                    "icon": "💰",
                    "title": "Optimiser mon coût de la vie",
                    "title_en": "Optimize my cost of living",
                    "description": "Logement abordable, prix quotidiens, pouvoir d'achat",
                    "description_en": "Affordable housing, daily prices, purchasing power",
                    "boost_criteria": ["cost_of_living", "housing_availability"]
                },
                {
                    "value": "lifestyle_upgrade",
                    "icon": "🌟",
                    "title": "Améliorer ma qualité de vie",
                    "title_en": "Improve my quality of life",
                    "description": "Climat, culture, bien-être, épanouissement",
                    "description_en": "Climate, culture, wellbeing, personal growth",
                    "boost_criteria": ["climate_quality", "cultural_scene", "air_quality"]
                },
                {
                    "value": "family_focus",
                    "icon": "👨‍👩‍👧‍👦",
                    "title": "Offrir un meilleur environnement à ma famille",
                    "title_en": "Provide a better environment for my family",
                    "description": "Éducation, sécurité, espaces verts, communauté",
                    "description_en": "Education, safety, green spaces, community",
                    "boost_criteria": ["family_friendliness", "education_quality", "safety_security"]
                },
                {
                    "value": "international_connections",
                    "icon": "🌍",
                    "title": "Développer mes connexions internationales",
                    "title_en": "Develop my international connections",
                    "description": "Business global, échanges Europe, opportunités export",
                    "description_en": "Global business, European exchanges, export opportunities",
                    "boost_criteria": ["international_connectivity", "european_proximity_advantage"]
                }
            ]
        },

        // ===== 2. PROFIL D'ÂGE ET ÉTAPE DE VIE =====
        {
            "id": "morocco_age_profile",
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
                    "title_en": "Student/Young graduate (18-25 years)",
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
                    "value": "senior_mature",
                    "icon": "🌻",
                    "title": "Senior/Mature (50+ ans)",
                    "title_en": "Senior/Mature (50+ years)",
                    "description": "Confort, tranquillité, santé, sagesse",
                    "description_en": "Comfort, tranquility, health, wisdom"
                }
            ]
        },

        // ===== 3. BUDGET LOGEMENT MENSUEL DH =====
        {
            "id": "morocco_monthly_budget",
            "title": "💳 Quel est votre budget logement mensuel ?",
            "title_en": "💳 What is your monthly housing budget?",
            "category": "financial",
            "type": "single",
            "weight": 8,
            "options": [
                {
                    "value": "budget_tight",
                    "icon": "💸",
                    "title": "Budget serré (< 5,000 DH/mois)",
                    "title_en": "Tight budget (< 5,000 DH/month)",
                    "description": "Colocation, zones populaires, priorité au prix",
                    "description_en": "Shared housing, popular areas, price priority"
                },
                {
                    "value": "budget_balanced",
                    "icon": "💰",
                    "title": "Budget équilibré (5,000 - 10,000 DH/mois)",
                    "title_en": "Balanced budget (5,000 - 10,000 DH/month)",
                    "description": "Appartement 1-2 chambres, quartiers moyens",
                    "description_en": "1-2 bedroom apartment, middle neighborhoods"
                },
                {
                    "value": "budget_comfortable",
                    "icon": "🏠",
                    "title": "Budget confortable (10,000 - 20,000 DH/mois)",
                    "title_en": "Comfortable budget (10,000 - 20,000 DH/month)",
                    "description": "Villa/grand appartement, bons quartiers",
                    "description_en": "Villa/large apartment, good neighborhoods"
                },
                {
                    "value": "budget_premium",
                    "icon": "🏛️",
                    "title": "Budget premium (20,000+ DH/mois)",
                    "title_en": "Premium budget (20,000+ DH/month)",
                    "description": "Logement haut de gamme, quartiers prestigieux",
                    "description_en": "High-end housing, prestigious neighborhoods"
                }
            ]
        },

        // ===== 4. SCÈNE CULTURELLE PRIORITAIRE =====
        {
            "id": "morocco_cultural_priority",
            "title": "🎭 Quel type de scène culturelle vous attire ?",
            "title_en": "🎭 What type of cultural scene attracts you?",
            "category": "culture",
            "type": "single",
            "weight": 7,
            "options": [
                {
                    "value": "modern_business",
                    "icon": "🏢",
                    "title": "Moderne et business",
                    "title_en": "Modern and business",
                    "description": "Centres d'affaires, innovation, networking international",
                    "description_en": "Business centers, innovation, international networking"
                },
                {
                    "value": "traditional_heritage",
                    "icon": "🕌",
                    "title": "Traditionnelle et patrimoine",
                    "title_en": "Traditional and heritage",
                    "description": "Médinas, artisanat, culture amazigh, histoire millénaire",
                    "description_en": "Medinas, craftsmanship, Berber culture, ancient history"
                },
                {
                    "value": "artistic_bohemian",
                    "icon": "🎨",
                    "title": "Artistique et bohème",
                    "title_en": "Artistic and bohemian",
                    "description": "Galeries, festivals, créativité, scène alternative",
                    "description_en": "Galleries, festivals, creativity, alternative scene"
                },
                {
                    "value": "cosmopolitan_mix",
                    "icon": "🌍",
                    "title": "Cosmopolite et éclectique",
                    "title_en": "Cosmopolitan and eclectic",
                    "description": "Mix cultures, diversité, ouverture au monde",
                    "description_en": "Cultural mix, diversity, openness to the world"
                }
            ]
        },

        // ===== 5. ACTIVITÉS PRIORITAIRES =====
        {
            "id": "morocco_activity_priority",
            "title": "🎯 Quelles activités sont prioritaires dans votre quotidien ?",
            "title_en": "🎯 What activities are priorities in your daily life?",
            "category": "lifestyle",
            "type": "single",
            "weight": 6,
            "options": [
                {
                    "value": "nature_sports",
                    "icon": "🏃‍♂️",
                    "title": "Nature et sports",
                    "title_en": "Nature and sports",
                    "description": "Randonnée, surf, montagne, air pur, activités outdoor",
                    "description_en": "Hiking, surfing, mountains, fresh air, outdoor activities"
                },
                {
                    "value": "nightlife_social",
                    "icon": "🌃",
                    "title": "Vie nocturne et sociale",
                    "title_en": "Nightlife and social",
                    "description": "Restaurants, cafés, sorties, rencontres, animation",
                    "description_en": "Restaurants, cafes, outings, meetings, entertainment"
                },
                {
                    "value": "family_education",
                    "icon": "👨‍👩‍👧‍👦",
                    "title": "Famille et éducation",
                    "title_en": "Family and education",
                    "description": "Écoles qualité, espaces enfants, sécurité, communauté",
                    "description_en": "Quality schools, children's spaces, safety, community"
                },
                {
                    "value": "culture_learning",
                    "icon": "📚",
                    "title": "Culture et apprentissage",
                    "title_en": "Culture and learning",
                    "description": "Musées, universités, formations, enrichissement personnel",
                    "description_en": "Museums, universities, training, personal enrichment"
                }
            ]
        },

        // ===== 6. ENVIRONNEMENT DE TRAVAIL =====
        {
            "id": "morocco_work_environment",
            "title": "💼 Quel environnement de travail vous correspond ?",
            "title_en": "💼 What work environment suits you?",
            "category": "professional",
            "type": "single",
            "weight": 7,
            "options": [
                {
                    "value": "tech_startup",
                    "icon": "💻",
                    "title": "Tech et startup",
                    "title_en": "Tech and startup",
                    "description": "Innovation, digital, écosystème entrepreneurial",
                    "description_en": "Innovation, digital, entrepreneurial ecosystem"
                },
                {
                    "value": "business_finance",
                    "icon": "📈",
                    "title": "Business et finance",
                    "title_en": "Business and finance",
                    "description": "Grandes entreprises, banques, consulting, corporate",
                    "description_en": "Large companies, banks, consulting, corporate"
                },
                {
                    "value": "government_public",
                    "icon": "🏛️",
                    "title": "Secteur public et administration",
                    "title_en": "Public sector and administration",
                    "description": "Ministères, institutions, fonction publique",
                    "description_en": "Ministries, institutions, civil service"
                },
                {
                    "value": "tourism_services",
                    "icon": "🏨",
                    "title": "Tourisme et services",
                    "title_en": "Tourism and services",
                    "description": "Hôtellerie, restauration, guides, événementiel",
                    "description_en": "Hospitality, restaurants, guides, events"
                },
                {
                    "value": "traditional_commerce",
                    "icon": "🛒",
                    "title": "Commerce traditionnel",
                    "title_en": "Traditional commerce",
                    "description": "Import-export, artisanat, marchés, négoce",
                    "description_en": "Import-export, crafts, markets, trading"
                }
            ]
        },

        // ===== 7. PRIORITÉ NATURE/ENVIRONNEMENT =====
        {
            "id": "morocco_nature_priority",
            "title": "🌿 Quel accès à la nature est essentiel pour vous ?",
            "title_en": "🌿 What access to nature is essential for you?",
            "category": "environment",
            "type": "single",
            "weight": 6,
            "options": [
                {
                    "value": "beach_ocean",
                    "icon": "🏖️",
                    "title": "Plages et océan",
                    "title_en": "Beaches and ocean",
                    "description": "Surf, baignade, sports nautiques, air marin",
                    "description_en": "Surfing, swimming, water sports, sea air"
                },
                {
                    "value": "mountains_hiking",
                    "icon": "⛰️",
                    "title": "Montagnes et randonnée",
                    "title_en": "Mountains and hiking",
                    "description": "Atlas, Rif, trekking, air pur, panoramas",
                    "description_en": "Atlas, Rif, trekking, fresh air, panoramas"
                },
                {
                    "value": "parks_gardens",
                    "icon": "🌳",
                    "title": "Parcs et espaces verts",
                    "title_en": "Parks and green spaces",
                    "description": "Jardins urbains, détente, jogging, pique-nique",
                    "description_en": "Urban gardens, relaxation, jogging, picnics"
                },
                {
                    "value": "urban_modern",
                    "icon": "🏙️",
                    "title": "Environnement urbain moderne",
                    "title_en": "Modern urban environment",
                    "description": "La nature n'est pas ma priorité, je préfère la ville",
                    "description_en": "Nature isn't my priority, I prefer the city"
                }
            ]
        },

        // ===== 8. CONNEXIONS PRIORITAIRES =====
        {
            "id": "morocco_connections_priority",
            "title": "🌐 Quelles connexions sont importantes pour vous ?",
            "title_en": "🌐 What connections are important to you?",
            "category": "connectivity",
            "type": "single",
            "weight": 6,
            "options": [
                {
                    "value": "international_europe",
                    "icon": "✈️",
                    "title": "International et Europe",
                    "title_en": "International and Europe",
                    "description": "Aéroports, liaisons européennes, business global",
                    "description_en": "Airports, European connections, global business"
                },
                {
                    "value": "national_major",
                    "icon": "🚄",
                    "title": "Connexions nationales majeures",
                    "title_en": "Major national connections",
                    "description": "TGV, autoroutes, liaisons grandes villes marocaines",
                    "description_en": "High-speed rail, highways, major Moroccan cities"
                },
                {
                    "value": "local_regional",
                    "icon": "🚌",
                    "title": "Transport local et régional",
                    "title_en": "Local and regional transport",
                    "description": "Transports urbains, connexions régionales quotidiennes",
                    "description_en": "Urban transport, daily regional connections"
                },
                {
                    "value": "minimal_connectivity",
                    "icon": "🏡",
                    "title": "Connectivité minimale",
                    "title_en": "Minimal connectivity",
                    "description": "Je privilégie la tranquillité à l'accessibilité",
                    "description_en": "I prioritize tranquility over accessibility"
                }
            ]
        },

        // ===== 9. AUTHENTICITÉ VS MODERNITÉ =====
        {
            "id": "morocco_authenticity_balance",
            "title": "⚖️ Quel équilibre souhaitez-vous entre tradition et modernité ?",
            "title_en": "⚖️ What balance do you want between tradition and modernity?",
            "category": "culture",
            "type": "single",
            "weight": 6,
            "options": [
                {
                    "value": "maximum_authentic",
                    "icon": "🕌",
                    "title": "Maximum d'authenticité",
                    "title_en": "Maximum authenticity",
                    "description": "Souks traditionnels, médinas, artisanat, culture amazigh",
                    "description_en": "Traditional souks, medinas, crafts, Berber culture"
                },
                {
                    "value": "balanced_heritage",
                    "icon": "🏛️",
                    "title": "Équilibre patrimoine-modernité",
                    "title_en": "Heritage-modernity balance",
                    "description": "Respect traditions avec infrastructures modernes",
                    "description_en": "Respect traditions with modern infrastructure"
                },
                {
                    "value": "modern_comfort",
                    "icon": "🏢",
                    "title": "Confort moderne prioritaire",
                    "title_en": "Modern comfort priority",
                    "description": "Centres commerciaux, technologie, standardisation",
                    "description_en": "Shopping centers, technology, standardization"
                },
                {
                    "value": "international_standards",
                    "icon": "🌍",
                    "title": "Standards internationaux",
                    "title_en": "International standards",
                    "description": "Mode de vie occidental, globalisation, uniformité",
                    "description_en": "Western lifestyle, globalization, uniformity"
                }
            ]
        },

        // ===== 10. CLIMAT ET QUALITÉ DE L'AIR =====
        {
            "id": "morocco_climate_priority",
            "title": "🌤️ Quel climat et qualité d'air privilégiez-vous ?",
            "title_en": "🌤️ What climate and air quality do you prioritize?",
            "category": "environment",
            "type": "single",
            "weight": 5,
            "options": [
                {
                    "value": "ocean_fresh",
                    "icon": "🌊",
                    "title": "Climat océanique frais",
                    "title_en": "Fresh oceanic climate",
                    "description": "Brise marine, températures modérées, humidité",
                    "description_en": "Sea breeze, moderate temperatures, humidity"
                },
                {
                    "value": "mountain_pure",
                    "icon": "🏔️",
                    "title": "Air pur de montagne",
                    "title_en": "Pure mountain air",
                    "description": "Altitude, air non pollué, fraîcheur naturelle",
                    "description_en": "Altitude, unpolluted air, natural freshness"
                },
                {
                    "value": "desert_dry",
                    "icon": "🏜️",
                    "title": "Climat désertique sec",
                    "title_en": "Dry desert climate",
                    "description": "Faible humidité, ciel dégagé, chaleur sèche",
                    "description_en": "Low humidity, clear skies, dry heat"
                },
                {
                    "value": "climate_flexible",
                    "icon": "🌡️",
                    "title": "Flexible sur le climat",
                    "title_en": "Flexible about climate",
                    "description": "Le climat n'est pas un critère déterminant",
                    "description_en": "Climate is not a determining factor"
                }
            ]
        },

        // ===== 11. PRIORITÉ SANTÉ ET SÉCURITÉ =====
        {
            "id": "morocco_health_safety",
            "title": "🏥 Quelle importance donnez-vous à la santé et sécurité ?",
            "title_en": "🏥 How important are health and safety to you?",
            "category": "wellbeing",
            "type": "single",
            "weight": 6,
            "options": [
                {
                    "value": "healthcare_priority",
                    "icon": "🏥",
                    "title": "Soins de santé excellents",
                    "title_en": "Excellent healthcare",
                    "description": "Hôpitaux modernes, spécialistes, urgences 24h/7j",
                    "description_en": "Modern hospitals, specialists, 24/7 emergency care"
                },
                {
                    "value": "safety_priority",
                    "icon": "🔒",
                    "title": "Sécurité maximale",
                    "title_en": "Maximum security",
                    "description": "Faible criminalité, quartiers sûrs, police présente",
                    "description_en": "Low crime, safe neighborhoods, police presence"
                },
                {
                    "value": "balanced_wellbeing",
                    "icon": "⚖️",
                    "title": "Équilibre santé-sécurité",
                    "title_en": "Health-safety balance",
                    "description": "Standards décents sans excès de précautions",
                    "description_en": "Decent standards without excessive precautions"
                },
                {
                    "value": "risk_tolerant",
                    "icon": "🤷‍♂️",
                    "title": "Tolérant aux risques",
                    "title_en": "Risk tolerant",
                    "description": "Privilégie autres critères, accepte imperfections",
                    "description_en": "Prioritizes other criteria, accepts imperfections"
                }
            ]
        },

        // ===== 12. DYNAMISME ÉCONOMIQUE =====
        {
            "id": "morocco_economic_dynamism",
            "title": "📈 Quel niveau de dynamisme économique recherchez-vous ?",
            "title_en": "📈 What level of economic dynamism are you looking for?",
            "category": "economic",
            "type": "single",
            "weight": 7,
            "options": [
                {
                    "value": "high_growth",
                    "icon": "🚀",
                    "title": "Croissance rapide et innovation",
                    "title_en": "Rapid growth and innovation",
                    "description": "Startups, investissements, création d'emplois, boom économique",
                    "description_en": "Startups, investments, job creation, economic boom"
                },
                {
                    "value": "stable_established",
                    "icon": "🏢",
                    "title": "Économie stable et établie",
                    "title_en": "Stable and established economy",
                    "description": "Grandes entreprises, emplois sûrs, croissance modérée",
                    "description_en": "Large companies, secure jobs, moderate growth"
                },
                {
                    "value": "emerging_potential",
                    "icon": "🌱",
                    "title": "Potentiel émergent",
                    "title_en": "Emerging potential",
                    "description": "Secteurs en développement, opportunités à saisir",
                    "description_en": "Developing sectors, opportunities to seize"
                },
                {
                    "value": "traditional_local",
                    "icon": "🛒",
                    "title": "Économie traditionnelle locale",
                    "title_en": "Traditional local economy",
                    "description": "Commerce local, artisanat, rythme paisible",
                    "description_en": "Local commerce, crafts, peaceful pace"
                }
            ]
        }
    ]
};

// ===== ALIAS POUR ANALYSIS.JS - OBLIGATOIRE =====
window.QUESTIONS_DATA = window.QUESTIONS_DATA || {};
window.QUESTIONS_DATA.morocco_residents = window.QUESTIONS_DATA_MOROCCO.morocco_residents;
window.QUESTIONS_DATA.morocco = window.QUESTIONS_DATA_MOROCCO.morocco_residents;
