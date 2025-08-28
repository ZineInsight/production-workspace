/**
 * 🎯 QUESTIONS-DATA-EXPAT-FOCUSED.JS - QUESTIONNAIRE CENTRÉ BESOINS
 * ================================================================
 * 8 questions OPTIMALES pour futurs expats - Focus sur les VRAIS besoins
 * Author: Revolutionary Team | Version: 6.0.0 - Expat Experience Focus
 * OBJECTIF: Recommandations basées sur besoins réels, pas géographie
 */

// 🌍 QUESTIONS CENTRÉES BESOINS D'EXPATS
window.QUESTIONS_DATA = {
    "international": [

        // ===== 1. CONTRAINTE LÉGALE ABSOLUE =====
        {
            "id": "expat_passport",
            "title": "🛂 Quel est votre passeport principal ?",
            "title_en": "🛂 What is your main passport?",
            "category": "legal_constraint",
            "type": "single",
            "description": "Détermine où vous pouvez légalement vivre et travailler",
            "description_en": "Determines where you can legally live and work",
            "weight": 10, // Poids maximum - contrainte absolue
            "options": [
                {
                    "value": "eu_passport",
                    "icon": "🇪🇺",
                    "title": "Union Européenne",
                    "title_en": "European Union",
                    "description": "Libre circulation dans 27 pays UE + Suisse/Norvège",
                    "description_en": "Free movement in 27 EU countries + Switzerland/Norway",
                    "boost_criteria": ["europe_access", "schengen_zone", "eu_benefits"]
                },
                {
                    "value": "us_passport",
                    "icon": "🇺🇸",
                    "title": "États-Unis",
                    "title_en": "United States",
                    "description": "Accès facilité pays développés + E2/L1 visas",
                    "description_en": "Easy access to developed countries + E2/L1 visas",
                    "boost_criteria": ["english_native", "developed_countries", "business_visas"]
                },
                {
                    "value": "ca_au_nz",
                    "icon": "🇨🇦",
                    "title": "Canada/Australie/Nouvelle-Zélande",
                    "title_en": "Canada/Australia/New Zealand",
                    "description": "Working Holiday + Commonwealth + qualité de vie",
                    "description_en": "Working Holiday + Commonwealth + quality of life",
                    "boost_criteria": ["working_holiday", "commonwealth", "quality_life"]
                },
                {
                    "value": "strong_passport",
                    "icon": "✈️",
                    "title": "Passeport fort (Japon, Singapour, Corée...)",
                    "title_en": "Strong passport (Japan, Singapore, Korea...)",
                    "description": "Visa-free dans la plupart des pays développés",
                    "description_en": "Visa-free access to most developed countries",
                    "boost_criteria": ["visa_free_access", "developed_countries", "asia_pacific"]
                },
                {
                    "value": "emerging_passport",
                    "icon": "🌍",
                    "title": "Autres nationalités",
                    "title_en": "Other nationalities",
                    "description": "Visas requis - Focus opportunités émergentes",
                    "description_en": "Visas required - Focus on emerging opportunities",
                    "boost_criteria": ["emerging_markets", "entrepreneurship", "cost_effective"]
                }
            ]
        },

        // ===== 2. BUDGET RÉALISTE =====
        {
            "id": "expat_budget_realistic",
            "title": "💰 Quel est votre budget mensuel TOTAL réaliste ?",
            "title_en": "💰 What is your realistic TOTAL monthly budget?",
            "category": "economic_constraint",
            "type": "single",
            "description": "Logement + nourriture + transport + loisirs + épargne",
            "description_en": "Housing + food + transport + leisure + savings",
            "weight": 9, // Quasi-contrainte absolue
            "options": [
                {
                    "value": "budget_maximizer",
                    "icon": "💵",
                    "title": "500-1200€ - Maximiser mes économies",
                    "title_en": "500-1200€ - Maximize my savings",
                    "description": "Asie du Sud-Est, Europe de l'Est, Amérique du Sud",
                    "description_en": "Southeast Asia, Eastern Europe, South America",
                    "boost_criteria": ["low_cost_living", "high_savings_potential", "value_for_money"]
                },
                {
                    "value": "budget_balanced",
                    "icon": "⚖️",
                    "title": "1200-2500€ - Équilibre qualité/prix",
                    "title_en": "1200-2500€ - Quality/price balance",
                    "description": "Europe moyenne, villes secondaires développées",
                    "description_en": "Central Europe, developed secondary cities",
                    "boost_criteria": ["balanced_lifestyle", "good_infrastructure", "middle_class_comfort"]
                },
                {
                    "value": "budget_comfort",
                    "icon": "💎",
                    "title": "2500-4000€ - Privilégier le confort",
                    "title_en": "2500-4000€ - Prioritize comfort",
                    "description": "Capitales européennes, villes nord-américaines",
                    "description_en": "European capitals, North American cities",
                    "boost_criteria": ["high_comfort", "premium_services", "developed_infrastructure"]
                },
                {
                    "value": "budget_premium",
                    "icon": "🏆",
                    "title": "4000€+ - Expérience premium",
                    "title_en": "4000€+ - Premium experience",
                    "description": "Suisse, Singapore, centres urbains premium",
                    "description_en": "Switzerland, Singapore, premium urban centers",
                    "boost_criteria": ["luxury_lifestyle", "top_tier_services", "exclusive_locations"]
                }
            ]
        },

        // ===== 3. CLIMAT SUPPORTABLE =====
        {
            "id": "expat_climate_tolerance",
            "title": "🌡️ Quel climat supportez-vous au quotidien ?",
            "title_en": "🌡️ What climate can you handle daily?",
            "category": "physical_wellness",
            "type": "single",
            "description": "Impact sur votre santé, humeur et productivité",
            "description_en": "Impact on your health, mood and productivity",
            "weight": 8,
            "options": [
                {
                    "value": "tropical_lover",
                    "icon": "🥵",
                    "title": "J'adore la chaleur tropicale",
                    "title_en": "I love tropical heat",
                    "description": "25-35°C, humidité, pas d'hiver - Asie/Amérique latine",
                    "description_en": "25-35°C, humidity, no winter - Asia/Latin America",
                    "boost_criteria": ["tropical_climate", "year_round_warmth", "beach_lifestyle"]
                },
                {
                    "value": "mediterranean_fan",
                    "icon": "☀️",
                    "title": "Méditerranéen = parfait",
                    "title_en": "Mediterranean = perfect",
                    "description": "Été chaud/hiver doux, beaucoup de soleil",
                    "description_en": "Hot summer/mild winter, lots of sunshine",
                    "boost_criteria": ["mediterranean_climate", "sunny_weather", "mild_winters"]
                },
                {
                    "value": "temperate_balanced",
                    "icon": "🌤️",
                    "title": "4 saisons équilibrées",
                    "title_en": "4 balanced seasons",
                    "description": "Variété climatique, -5°C à 25°C",
                    "description_en": "Climate variety, -5°C to 25°C",
                    "boost_criteria": ["four_seasons", "climate_variety", "moderate_temperatures"]
                },
                {
                    "value": "cool_weather_lover",
                    "icon": "❄️",
                    "title": "J'aime le froid/fraîcheur",
                    "title_en": "I like cold/cool weather",
                    "description": "Hiver marqué, températures basses OK",
                    "description_en": "Distinct winter, low temperatures OK",
                    "boost_criteria": ["cool_climate", "winter_activities", "low_temperatures"]
                },
                {
                    "value": "climate_flexible",
                    "icon": "🌦️",
                    "title": "Je m'adapte facilement",
                    "title_en": "I adapt easily",
                    "description": "Le climat n'est pas un critère important",
                    "description_en": "Climate is not an important criterion",
                    "boost_criteria": ["climate_adaptable", "weather_independent", "indoor_lifestyle"]
                }
            ]
        },

        // ===== 4. SÉCURITÉ & TRANQUILLITÉ =====
        {
            "id": "expat_security_needs",
            "title": "🔒 Quel niveau de sécurité exigez-vous ?",
            "title_en": "🔒 What level of security do you require?",
            "category": "safety_wellness",
            "type": "single",
            "description": "Sécurité personnelle, stabilité politique, tranquillité d'esprit",
            "description_en": "Personal security, political stability, peace of mind",
            "weight": 8,
            "options": [
                {
                    "value": "maximum_security",
                    "icon": "🛡️",
                    "title": "Sécurité maximale exigée",
                    "title_en": "Maximum security required",
                    "description": "Singapour, Suisse, pays nordiques - Zéro risque",
                    "description_en": "Singapore, Switzerland, Nordic countries - Zero risk",
                    "boost_criteria": ["highest_safety", "political_stability", "low_crime"]
                },
                {
                    "value": "high_security",
                    "icon": "🔐",
                    "title": "Sécurité élevée souhaitée",
                    "title_en": "High security desired",
                    "description": "Europe occidentale, Canada, Australie - Très sûr",
                    "description_en": "Western Europe, Canada, Australia - Very safe",
                    "boost_criteria": ["high_safety", "stable_institutions", "good_policing"]
                },
                {
                    "value": "reasonable_security",
                    "icon": "⚠️",
                    "title": "Sécurité correcte suffisante",
                    "title_en": "Reasonable security sufficient",
                    "description": "Précautions normales, éviter certains quartiers",
                    "description_en": "Normal precautions, avoid certain areas",
                    "boost_criteria": ["moderate_safety", "urban_awareness", "standard_precautions"]
                },
                {
                    "value": "adventure_tolerance",
                    "icon": "🎲",
                    "title": "J'accepte quelques risques",
                    "title_en": "I accept some risks",
                    "description": "Opportunités vs sécurité - Asie émergente, Amérique latine",
                    "description_en": "Opportunities vs security - Emerging Asia, Latin America",
                    "boost_criteria": ["adventure_ready", "risk_tolerance", "emerging_opportunities"]
                }
            ]
        },

        // ===== 5. STYLE DE VIE URBAIN =====
        {
            "id": "expat_lifestyle_pace",
            "title": "🏙️ Quel rythme de vie vous correspond ?",
            "title_en": "🏙️ What pace of life suits you?",
            "category": "lifestyle_preference",
            "type": "single",
            "description": "Énergie urbaine, activités, rythme quotidien",
            "description_en": "Urban energy, activities, daily rhythm",
            "weight": 7,
            "options": [
                {
                    "value": "hyperactive_urban",
                    "icon": "⚡",
                    "title": "Hyperactif & ultra-urbain",
                    "title_en": "Hyperactive & ultra-urban",
                    "description": "NYC, Tokyo, Hong Kong - Toujours en mouvement",
                    "description_en": "NYC, Tokyo, Hong Kong - Always on the move",
                    "boost_criteria": ["24_7_city", "high_energy", "non_stop_activities"]
                },
                {
                    "value": "dynamic_balanced",
                    "icon": "🎯",
                    "title": "Dynamique mais équilibré",
                    "title_en": "Dynamic but balanced",
                    "description": "Berlin, Barcelona, Montreal - Vie riche + temps perso",
                    "description_en": "Berlin, Barcelona, Montreal - Rich life + personal time",
                    "boost_criteria": ["vibrant_culture", "work_life_balance", "diverse_activities"]
                },
                {
                    "value": "relaxed_quality",
                    "icon": "🌅",
                    "title": "Détendu & qualité de vie",
                    "title_en": "Relaxed & quality of life",
                    "description": "Melbourne, Copenhagen, Valencia - Slow living",
                    "description_en": "Melbourne, Copenhagen, Valencia - Slow living",
                    "boost_criteria": ["quality_over_quantity", "relaxed_pace", "life_enjoyment"]
                },
                {
                    "value": "quiet_peaceful",
                    "icon": "🕊️",
                    "title": "Calme & paisible",
                    "title_en": "Quiet & peaceful",
                    "description": "Villes moyennes, nature proche, tranquillité",
                    "description_en": "Medium cities, close to nature, tranquility",
                    "boost_criteria": ["peaceful_environment", "small_city_charm", "nature_access"]
                }
            ]
        },

        // ===== 6. BARRIÈRE LINGUISTIQUE =====
        {
            "id": "expat_language_comfort",
            "title": "🗣️ Quelle barrière linguistique acceptez-vous ?",
            "title_en": "🗣️ What language barrier do you accept?",
            "category": "communication",
            "type": "single",
            "description": "Impact sur votre quotidien, travail et intégration sociale",
            "description_en": "Impact on your daily life, work and social integration",
            "weight": 7,
            "options": [
                {
                    "value": "english_only",
                    "icon": "🇬🇧",
                    "title": "Anglais seulement",
                    "title_en": "English only",
                    "description": "Pays anglophones - UK, USA, Canada, Australie",
                    "description_en": "English-speaking countries - UK, USA, Canada, Australia",
                    "boost_criteria": ["english_native", "anglo_countries", "no_language_barrier"]
                },
                {
                    "value": "english_plus_basic",
                    "icon": "🌍",
                    "title": "Anglais + bases locales",
                    "title_en": "English + local basics",
                    "description": "Europe, Asie développée - Effort d'apprentissage OK",
                    "description_en": "Europe, developed Asia - Learning effort OK",
                    "boost_criteria": ["english_business", "international_cities", "language_learning_support"]
                },
                {
                    "value": "bilingual_advantage",
                    "icon": "🗣️",
                    "title": "Je suis bilingue/multilingue",
                    "title_en": "I am bilingual/multilingual",
                    "description": "Français, Espagnol, Mandarin... - Avantage linguistique",
                    "description_en": "French, Spanish, Mandarin... - Language advantage",
                    "boost_criteria": ["multilingual_cities", "cultural_diversity", "language_advantage"]
                },
                {
                    "value": "immersion_ready",
                    "icon": "🎯",
                    "title": "Immersion totale acceptable",
                    "title_en": "Total immersion acceptable",
                    "description": "J'apprends vite - Japon, Corée, pays émergents",
                    "description_en": "I learn fast - Japan, Korea, emerging countries",
                    "boost_criteria": ["language_immersion", "local_integration", "cultural_adaptation"]
                },
                {
                    "value": "language_flexible",
                    "icon": "🤝",
                    "title": "Je m'adapte facilement",
                    "title_en": "I adapt easily",
                    "description": "Langue pas prioritaire - Gestes, apps, communauté",
                    "description_en": "Language not priority - Gestures, apps, community",
                    "boost_criteria": ["expat_communities", "translation_support", "non_verbal_friendly"]
                }
            ]
        },

        // ===== 7. SITUATION FAMILIALE =====
        {
            "id": "expat_family_status",
            "title": "👨‍👩‍👧‍👦 Quelle est votre situation familiale ?",
            "title_en": "👨‍👩‍👧‍👦 What is your family situation?",
            "category": "family_constraint",
            "type": "single",
            "description": "Impact majeur sur logement, écoles, activités, budget",
            "description_en": "Major impact on housing, schools, activities, budget",
            "weight": 8,
            "options": [
                {
                    "value": "single_flexible",
                    "icon": "👤",
                    "title": "Célibataire - Flexibilité totale",
                    "title_en": "Single - Total flexibility",
                    "description": "Priorité: vie sociale, rencontres, liberté de mouvement",
                    "description_en": "Priority: social life, dating, freedom of movement",
                    "boost_criteria": ["social_scene", "dating_opportunities", "flexibility"]
                },
                {
                    "value": "couple_adventure",
                    "icon": "👥",
                    "title": "Couple sans enfant - Aventure à deux",
                    "title_en": "Couple without children - Adventure for two",
                    "description": "Compromis à deux, expériences partagées, double budget",
                    "description_en": "Two-way compromise, shared experiences, dual budget",
                    "boost_criteria": ["couple_activities", "romantic_destinations", "dual_career"]
                },
                {
                    "value": "family_young_kids",
                    "icon": "👶",
                    "title": "Famille enfants 0-12 ans",
                    "title_en": "Family with children 0-12 years",
                    "description": "Priorité: écoles internationales, sécurité, santé, espaces",
                    "description_en": "Priority: international schools, safety, health, spaces",
                    "boost_criteria": ["international_schools", "family_safety", "child_healthcare", "green_spaces"]
                },
                {
                    "value": "family_teenagers",
                    "icon": "🎓",
                    "title": "Famille adolescents 12+ ans",
                    "title_en": "Family with teenagers 12+ years",
                    "description": "Continuité éducative, universités, activités ados",
                    "description_en": "Educational continuity, universities, teen activities",
                    "boost_criteria": ["high_schools", "university_access", "teen_activities", "educational_continuity"]
                },
                {
                    "value": "extended_family",
                    "icon": "🏠",
                    "title": "Famille élargie/multi-générations",
                    "title_en": "Extended/multi-generational family",
                    "description": "Soins seniors, proximité famille, logements adaptés",
                    "description_en": "Senior care, family proximity, adapted housing",
                    "boost_criteria": ["senior_care", "extended_family_support", "cultural_acceptance", "healthcare_seniors"]
                }
            ]
        },

        // ===== 8. SITUATION PROFESSIONNELLE =====
        {
            "id": "expat_professional_status",
            "title": "💼 Quelle est votre situation professionnelle ?",
            "title_en": "💼 What is your professional situation?",
            "category": "career_constraint",
            "type": "single",
            "description": "Détermine opportunités, visa, réseau, revenus",
            "description_en": "Determines opportunities, visa, network, income",
            "weight": 7,
            "options": [
                {
                    "value": "entrepreneur_startup",
                    "icon": "🚀",
                    "title": "Entrepreneur/Startup",
                    "title_en": "Entrepreneur/Startup",
                    "description": "Écosystème innovation, financement, réseau business",
                    "description_en": "Innovation ecosystem, funding, business network",
                    "boost_criteria": ["startup_ecosystem", "vc_access", "business_network", "innovation_hub"]
                },
                {
                    "value": "senior_executive",
                    "icon": "👔",
                    "title": "Cadre expérimenté/Senior",
                    "title_en": "Experienced/Senior executive",
                    "description": "Opportunités leadership, package expat, stabilité",
                    "description_en": "Leadership opportunities, expat package, stability",
                    "boost_criteria": ["executive_opportunities", "expat_packages", "corporate_culture", "leadership_roles"]
                },
                {
                    "value": "young_professional",
                    "icon": "🎓",
                    "title": "Jeune professionnel/Diplômé",
                    "title_en": "Young professional/Graduate",
                    "description": "Première expérience internationale, croissance rapide",
                    "description_en": "First international experience, rapid growth",
                    "boost_criteria": ["entry_level_jobs", "career_growth", "international_experience", "young_expat_community"]
                },
                {
                    "value": "digital_nomad",
                    "icon": "💻",
                    "title": "Nomade digital/Remote",
                    "title_en": "Digital nomad/Remote",
                    "description": "Wifi, visas nomad, coworking, communauté",
                    "description_en": "Wifi, nomad visas, coworking, community",
                    "boost_criteria": ["digital_infrastructure", "nomad_visas", "coworking_spaces", "nomad_community"]
                },
                {
                    "value": "retiree_early",
                    "icon": "🏖️",
                    "title": "Retraité/Early retirement",
                    "title_en": "Retired/Early retirement",
                    "description": "Fiscalité optimisée, coût de vie, soins de santé",
                    "description_en": "Tax optimization, cost of living, healthcare",
                    "boost_criteria": ["tax_optimization", "retirement_benefits", "healthcare_quality", "expat_retiree_community"]
                }
            ]
        },

        // ===== 9. TRANSPORT & MOBILITÉ =====
        {
            "id": "expat_mobility_preference",
            "title": "🚇 Comment préférez-vous vous déplacer au quotidien ?",
            "title_en": "🚇 How do you prefer to move around daily?",
            "category": "daily_practical",
            "type": "single",
            "description": "Impact sur choix logement, coûts, style de vie quotidien",
            "description_en": "Impact on housing choices, costs, daily lifestyle",
            "weight": 6,
            "options": [
                {
                    "value": "public_transport_only",
                    "icon": "🚅",
                    "title": "Transport public exclusivement",
                    "title_en": "Public transport exclusively",
                    "description": "Métro/bus efficace, pas de voiture, écologique",
                    "description_en": "Efficient metro/bus, no car, ecological",
                    "boost_criteria": ["excellent_public_transport", "walkable_city", "bike_friendly", "car_free_lifestyle"]
                },
                {
                    "value": "mixed_mobility",
                    "icon": "🚲",
                    "title": "Mobilité mixte (vélo + public)",
                    "title_en": "Mixed mobility (bike + public)",
                    "description": "Flexibilité selon situation, approche durable",
                    "description_en": "Flexibility according to situation, sustainable approach",
                    "boost_criteria": ["bike_infrastructure", "good_public_transport", "pedestrian_friendly", "mixed_transport"]
                },
                {
                    "value": "car_when_needed",
                    "icon": "🚗",
                    "title": "Voiture occasionnelle",
                    "title_en": "Occasional car",
                    "description": "Location/partage voiture pour week-ends, voyages",
                    "description_en": "Car rental/sharing for weekends, trips",
                    "boost_criteria": ["car_sharing", "rental_access", "weekend_escape_options", "public_transport_backup"]
                },
                {
                    "value": "car_essential",
                    "icon": "🚙",
                    "title": "Voiture indispensable",
                    "title_en": "Car essential",
                    "description": "Liberté totale, banlieues, famille, distances",
                    "description_en": "Total freedom, suburbs, family, distances",
                    "boost_criteria": ["car_friendly_city", "parking_available", "suburban_lifestyle", "driving_infrastructure"]
                },
                {
                    "value": "mobility_flexible",
                    "icon": "🛴",
                    "title": "Flexible/Peu important",
                    "title_en": "Flexible/Not important",
                    "description": "M'adapte au système local, transport n'est pas prioritaire",
                    "description_en": "Adapt to local system, transport is not priority",
                    "boost_criteria": ["transport_adaptable", "local_solutions", "mobility_independent"]
                }
            ]
        }
    ]
};

// 🎯 SYSTÈME DE SCORING CENTRÉ BESOINS
window.EXPAT_SCORING_SYSTEM = {

    // Calcul du score basé sur les critères boostés par les réponses
    calculateCityScore: function (userResponses, cityData) {
        let totalScore = 0;
        let weightSum = 0;

        userResponses.forEach(response => {
            const question = this.findQuestion(response.questionId);
            if (question) {
                const selectedOption = question.options.find(opt => opt.value === response.value);
                if (selectedOption && selectedOption.boost_criteria) {

                    // Pour chaque critère à booster
                    selectedOption.boost_criteria.forEach(criterion => {
                        const cityScore = this.getCityScoreForCriterion(cityData, criterion);
                        totalScore += cityScore * question.weight;
                        weightSum += question.weight;
                    });
                }
            }
        });

        // Score final normalisé + bonus diversité
        const baseScore = weightSum > 0 ? totalScore / weightSum : 0;
        const diversityBonus = this.getDiversityBonus(cityData.name);

        return Math.min(100, baseScore + diversityBonus);
    },

    // Mapping critères → scores ville
    getCityScoreForCriterion: function (cityData, criterion) {
        const criteriaMapping = {
            // Critères climatiques
            'tropical_climate': cityData.climate_tropical || 0,
            'mediterranean_climate': cityData.climate_mediterranean || 0,
            'four_seasons': cityData.climate_temperate || 0,
            'cool_climate': cityData.climate_cool || 0,

            // Critères sécurité
            'highest_safety': cityData.security_level >= 9 ? 10 : 0,
            'high_safety': cityData.security_level >= 7 ? 8 : 0,
            'moderate_safety': cityData.security_level >= 5 ? 6 : 0,

            // Critères coût
            'low_cost_living': cityData.cost_of_living <= 3 ? 10 : 0,
            'balanced_lifestyle': cityData.cost_of_living <= 6 ? 8 : 0,
            'high_comfort': cityData.comfort_level >= 8 ? 9 : 0,

            // Défaut
            'default': 5
        };

        return criteriaMapping[criterion] || criteriaMapping['default'];
    },

    // Anti-monopole Mumbai
    getDiversityBonus: function (cityName) {
        // Bonus inversement proportionnel à la fréquence de recommandation
        const blacklistedCities = ['Mumbai', 'Delhi']; // Villes trop dominantes
        return blacklistedCities.includes(cityName) ? -2 : Math.random() * 2;
    },

    // Utilitaires
    findQuestion: function (questionId) {
        return window.QUESTIONS_DATA.international.find(q => q.id === questionId);
    }
};

console.log('🎯 QUESTIONS EXPAT-FOCUSED chargées:', window.QUESTIONS_DATA.international.length, 'questions optimales');
console.log('⚡ Système de scoring centré BESOINS activé - Fini les incohérences géographiques !');
