/**
 * 🇧🇷 QUESTIONS-DATA-BR-RESIDENTS.JS - QUESTIONNAIRE RELOCATION DOMESTIQUE BRÉSIL
 * ==================================================================================
 * 12 questions OPTIMALES pour résidents/expats cherchant nouvelle ville au Brésil
 * Author: Revolutionary Team | Version: 1.0.0 - Brazil Domestic + Expat Focus
 * OBJECTIF: Recommandations basées sur profils réels des relocations brésiliennes
 */

// 🏠 QUESTIONS CENTRÉES BESOINS RELOCATION BRÉSIL
window.QUESTIONS_DATA_BRAZIL = {
    "brazil_residents": [

        // ===== 1. PRÉFÉRENCE RÉGIONALE BRÉSIL =====
        {
            "id": "brazil_regional_preference",
            "title": "🗺️ Quelle région du Brésil vous attire le plus ?",
            "title_en": "🗺️ Which region of Brazil attracts you most?",
            "category": "geography",
            "type": "single",
            "description": "Choisissez votre zone géographique préférée au Brésil",
            "description_en": "Choose your preferred geographical area in Brazil",
            "weight": 8,
            "options": [
                {
                    "value": "any_region",
                    "icon": "🇧🇷",
                    "title": "Ouvert à toutes les régions",
                    "title_en": "Open to all regions",
                    "description": "Je suis flexible, recommandez-moi partout au Brésil",
                    "description_en": "I'm flexible, recommend anywhere in Brazil"
                },
                {
                    "value": "sudeste",
                    "icon": "🏙️",
                    "title": "Sudeste",
                    "title_en": "Southeast",
                    "description": "São Paulo, Rio de Janeiro, Belo Horizonte, Vitória",
                    "description_en": "São Paulo, Rio de Janeiro, Belo Horizonte, Vitória"
                },
                {
                    "value": "sul",
                    "icon": "🌲",
                    "title": "Sud",
                    "title_en": "South",
                    "description": "Porto Alegre, Curitiba, Florianópolis",
                    "description_en": "Porto Alegre, Curitiba, Florianópolis"
                },
                {
                    "value": "nordeste",
                    "icon": "🏖️",
                    "title": "Nordeste",
                    "title_en": "Northeast",
                    "description": "Salvador, Recife, Fortaleza, Natal",
                    "description_en": "Salvador, Recife, Fortaleza, Natal"
                },
                {
                    "value": "centro_oeste",
                    "icon": "🌾",
                    "title": "Centre-Ouest",
                    "title_en": "Center-West",
                    "description": "Brasília, Goiânia, Campo Grande, Cuiabá",
                    "description_en": "Brasília, Goiânia, Campo Grande, Cuiabá"
                },
                {
                    "value": "norte",
                    "icon": "🌳",
                    "title": "Nord",
                    "title_en": "North",
                    "description": "Manaus, Belém - Région amazonienne",
                    "description_en": "Manaus, Belém - Amazon region"
                }
            ]
        },

        // ===== 2. PRIORITÉ LIFESTYLE =====
        {
            "id": "brazil_lifestyle_priority",
            "title": "🎯 Quelle est votre priorité #1 pour cette relocation ?",
            "title_en": "🎯 What is your #1 priority for this relocation?",
            "category": "life_priority",
            "type": "single",
            "description": "Définissez votre objectif principal",
            "description_en": "Define your main objective",
            "weight": 9,
            "options": [
                {
                    "value": "balanced_lifestyle",
                    "icon": "⚖️",
                    "title": "Équilibre vie-travail",
                    "title_en": "Work-life balance",
                    "description": "Harmonie entre carrière et vie personnelle",
                    "description_en": "Harmony between career and personal life"
                },
                {
                    "value": "career_growth",
                    "icon": "🚀",
                    "title": "Développement professionnel",
                    "title_en": "Professional development",
                    "description": "Opportunités d'emploi, salaires, networking",
                    "description_en": "Job opportunities, salaries, networking"
                },
                {
                    "value": "cost_optimization",
                    "icon": "💰",
                    "title": "Optimiser mon budget",
                    "title_en": "Optimize my budget",
                    "description": "Coût de la vie abordable, logement pas cher",
                    "description_en": "Affordable cost of living, cheap housing"
                },
                {
                    "value": "lifestyle_upgrade",
                    "icon": "🌴",
                    "title": "Améliorer ma qualité de vie",
                    "title_en": "Improve my quality of life",
                    "description": "Climat, plages, culture, gastronomie",
                    "description_en": "Climate, beaches, culture, gastronomy"
                },
                {
                    "value": "safety_priority",
                    "icon": "🛡️",
                    "title": "Prioriser la sécurité",
                    "title_en": "Prioritize safety",
                    "description": "Ville sûre, quartiers tranquilles",
                    "description_en": "Safe city, quiet neighborhoods"
                }
            ]
        },

        // ===== 3. ENVIRONNEMENT DE TRAVAIL =====
        {
            "id": "brazil_work_environment",
            "title": "💼 Quel type d'environnement professionnel recherchez-vous ?",
            "title_en": "💼 What type of professional environment are you looking for?",
            "category": "career",
            "type": "single",
            "description": "Décrivez votre situation professionnelle idéale",
            "description_en": "Describe your ideal professional situation",
            "weight": 7,
            "options": [
                {
                    "value": "flexible_opportunity",
                    "icon": "🌟",
                    "title": "Opportunités flexibles",
                    "title_en": "Flexible opportunities",
                    "description": "Ouvert à différents secteurs et entreprises",
                    "description_en": "Open to different sectors and companies"
                },
                {
                    "value": "tech_startup",
                    "icon": "💻",
                    "title": "Tech & Startups",
                    "title_en": "Tech & Startups",
                    "description": "Innovation, technologie, écosystème startup",
                    "description_en": "Innovation, technology, startup ecosystem"
                },
                {
                    "value": "corporate_environment",
                    "icon": "🏢",
                    "title": "Grandes entreprises",
                    "title_en": "Large corporations",
                    "description": "Multinationales, stabilité, structure",
                    "description_en": "Multinationals, stability, structure"
                },
                {
                    "value": "freelance_remote",
                    "icon": "🏠",
                    "title": "Freelance/Télétravail",
                    "title_en": "Freelance/Remote work",
                    "description": "Indépendance, travail à distance",
                    "description_en": "Independence, remote work"
                },
                {
                    "value": "public_sector",
                    "icon": "🏛️",
                    "title": "Secteur public",
                    "title_en": "Public sector",
                    "description": "Fonction publique, administration, éducation",
                    "description_en": "Civil service, administration, education"
                }
            ]
        },

        // ===== 4. BUDGET MENSUEL =====
        {
            "id": "brazil_budget_range",
            "title": "💰 Quel est votre budget mensuel total au Brésil ?",
            "title_en": "💰 What is your total monthly budget in Brazil?",
            "category": "budget",
            "type": "single",
            "description": "Budget incluant logement, transport, nourriture, loisirs",
            "description_en": "Budget including housing, transport, food, leisure",
            "weight": 8,
            "options": [
                {
                    "value": "budget_tight",
                    "icon": "🎯",
                    "title": "R$ 2 000 - 4 000",
                    "title_en": "R$ 2,000 - 4,000",
                    "description": "Budget serré, priorité aux essentiels",
                    "description_en": "Tight budget, priority to essentials"
                },
                {
                    "value": "budget_comfortable",
                    "icon": "💚",
                    "title": "R$ 4 000 - 7 000",
                    "title_en": "R$ 4,000 - 7,000",
                    "description": "Confortable, quelques extras possibles",
                    "description_en": "Comfortable, some extras possible"
                },
                {
                    "value": "budget_generous",
                    "icon": "💎",
                    "title": "R$ 7 000 - 12 000",
                    "title_en": "R$ 7,000 - 12,000",
                    "description": "Généreux, choix de qualité",
                    "description_en": "Generous, quality choices"
                },
                {
                    "value": "budget_premium",
                    "icon": "👑",
                    "title": "R$ 12 000+",
                    "title_en": "R$ 12,000+",
                    "description": "Premium, aucune contrainte budgétaire",
                    "description_en": "Premium, no budget constraints"
                }
            ]
        },

        // ===== 5. SCÈNE SOCIALE =====
        {
            "id": "brazil_social_scene",
            "title": "🎉 Quelle ambiance sociale vous correspond le mieux ?",
            "title_en": "🎉 Which social atmosphere suits you best?",
            "category": "social",
            "type": "single",
            "description": "Décrivez votre style de vie sociale idéal",
            "description_en": "Describe your ideal social lifestyle",
            "weight": 6,
            "options": [
                {
                    "value": "mixed_social",
                    "icon": "🎭",
                    "title": "Mixte et varié",
                    "title_en": "Mixed and varied",
                    "description": "Un peu de tout : calme et animation",
                    "description_en": "A bit of everything: calm and lively"
                },
                {
                    "value": "active_social",
                    "icon": "🎪",
                    "title": "Vie sociale active",
                    "title_en": "Active social life",
                    "description": "Sorties, événements, networking actif",
                    "description_en": "Outings, events, active networking"
                },
                {
                    "value": "quiet_community",
                    "icon": "🏡",
                    "title": "Communauté tranquille",
                    "title_en": "Quiet community",
                    "description": "Relations de proximité, ambiance paisible",
                    "description_en": "Close relationships, peaceful atmosphere"
                },
                {
                    "value": "cultural_scene",
                    "icon": "🎨",
                    "title": "Scène culturelle riche",
                    "title_en": "Rich cultural scene",
                    "description": "Arts, musique, théâtre, festivals",
                    "description_en": "Arts, music, theater, festivals"
                },
                {
                    "value": "expat_community",
                    "icon": "🌍",
                    "title": "Communauté internationale",
                    "title_en": "International community",
                    "description": "Expats, diversité culturelle",
                    "description_en": "Expats, cultural diversity"
                }
            ]
        },

        // ===== 6. PRÉFÉRENCE CLIMATIQUE =====
        {
            "id": "brazil_climate_preference",
            "title": "🌡️ Quel climat brésilien vous plaît le plus ?",
            "title_en": "🌡️ Which Brazilian climate appeals to you most?",
            "category": "climate",
            "type": "single",
            "description": "Choisissez votre climat idéal au Brésil",
            "description_en": "Choose your ideal climate in Brazil",
            "weight": 7,
            "options": [
                {
                    "value": "warm_weather",
                    "icon": "☀️",
                    "title": "Chaud toute l'année",
                    "title_en": "Warm year-round",
                    "description": "Climat tropical, chaleur constante",
                    "description_en": "Tropical climate, constant warmth"
                },
                {
                    "value": "subtropical_mild",
                    "icon": "🌤️",
                    "title": "Subtropical modéré",
                    "title_en": "Moderate subtropical",
                    "description": "Saisons marquées, températures douces",
                    "description_en": "Distinct seasons, mild temperatures"
                },
                {
                    "value": "coastal_breeze",
                    "icon": "🌊",
                    "title": "Côtier avec brise",
                    "title_en": "Coastal with breeze",
                    "description": "Proximité océan, air marin rafraîchissant",
                    "description_en": "Ocean proximity, refreshing sea air"
                },
                {
                    "value": "mountain_fresh",
                    "icon": "⛰️",
                    "title": "Montagnard frais",
                    "title_en": "Fresh mountain",
                    "description": "Altitude, températures plus fraîches",
                    "description_en": "Altitude, cooler temperatures"
                },
                {
                    "value": "climate_flexible",
                    "icon": "🌈",
                    "title": "Flexible sur le climat",
                    "title_en": "Climate flexible",
                    "description": "Je m'adapte à tous les climats",
                    "description_en": "I adapt to all climates"
                }
            ]
        },

        // ===== 7. PRIORITÉS CULTURELLES =====
        {
            "id": "brazil_culture_priorities",
            "title": "🎭 Quelle est votre approche de la culture brésilienne ?",
            "title_en": "🎭 What is your approach to Brazilian culture?",
            "category": "culture",
            "type": "single",
            "description": "Comment voulez-vous vivre la culture locale ?",
            "description_en": "How do you want to experience local culture?",
            "weight": 6,
            "options": [
                {
                    "value": "embrace_local",
                    "icon": "🇧🇷",
                    "title": "Embrasser la culture locale",
                    "title_en": "Embrace local culture",
                    "description": "Intégration complète, traditions brésiliennes",
                    "description_en": "Complete integration, Brazilian traditions"
                },
                {
                    "value": "cultural_balance",
                    "icon": "⚖️",
                    "title": "Équilibre culturel",
                    "title_en": "Cultural balance",
                    "description": "Mélange culture locale et internationale",
                    "description_en": "Mix of local and international culture"
                },
                {
                    "value": "international_focus",
                    "icon": "🌍",
                    "title": "Orientation internationale",
                    "title_en": "International focus",
                    "description": "Environnement cosmopolite, diversité",
                    "description_en": "Cosmopolitan environment, diversity"
                },
                {
                    "value": "gradual_integration",
                    "icon": "📈",
                    "title": "Intégration progressive",
                    "title_en": "Gradual integration",
                    "description": "Adaptation étape par étape",
                    "description_en": "Step-by-step adaptation"
                }
            ]
        },

        // ===== 8. CONFORT AVEC LA LANGUE =====
        {
            "id": "brazil_language_comfort",
            "title": "🗣️ Quel est votre niveau avec le portugais brésilien ?",
            "title_en": "🗣️ What is your level with Brazilian Portuguese?",
            "category": "language",
            "type": "single",
            "description": "Évaluez votre aisance avec la langue locale",
            "description_en": "Assess your comfort with the local language",
            "weight": 5,
            "options": [
                {
                    "value": "fluent_portuguese",
                    "icon": "🎯",
                    "title": "Courant en portugais",
                    "title_en": "Fluent in Portuguese",
                    "description": "Je parle déjà couramment",
                    "description_en": "I already speak fluently"
                },
                {
                    "value": "basic_portuguese",
                    "icon": "📚",
                    "title": "Notions de base",
                    "title_en": "Basic knowledge",
                    "description": "Quelques mots, je peux me débrouiller",
                    "description_en": "A few words, I can get by"
                },
                {
                    "value": "learning_portuguese",
                    "icon": "🎓",
                    "title": "En apprentissage",
                    "title_en": "Learning",
                    "description": "J'apprends activement le portugais",
                    "description_en": "I'm actively learning Portuguese"
                },
                {
                    "value": "no_portuguese",
                    "icon": "🔤",
                    "title": "Pas de portugais",
                    "title_en": "No Portuguese",
                    "description": "Je ne parle pas portugais du tout",
                    "description_en": "I don't speak Portuguese at all"
                }
            ]
        },

        // ===== 9. PRÉFÉRENCE LOGEMENT =====
        {
            "id": "brazil_housing_preference",
            "title": "🏠 Quel type de logement vous attire ?",
            "title_en": "🏠 What type of housing appeals to you?",
            "category": "housing",
            "type": "single",
            "description": "Décrivez votre logement idéal au Brésil",
            "description_en": "Describe your ideal housing in Brazil",
            "weight": 7,
            "options": [
                {
                    "value": "apartment",
                    "icon": "🏢",
                    "title": "Appartement en centre-ville",
                    "title_en": "City center apartment",
                    "description": "Pratique, proche de tout, sécurisé",
                    "description_en": "Convenient, close to everything, secure"
                },
                {
                    "value": "suburban_house",
                    "icon": "🏡",
                    "title": "Maison en banlieue",
                    "title_en": "Suburban house",
                    "description": "Espace, jardin, quartier résidentiel",
                    "description_en": "Space, garden, residential neighborhood"
                },
                {
                    "value": "beachfront_property",
                    "icon": "🏖️",
                    "title": "Propriété face à la mer",
                    "title_en": "Beachfront property",
                    "description": "Vue océan, accès plage direct",
                    "description_en": "Ocean view, direct beach access"
                },
                {
                    "value": "gated_community",
                    "icon": "🏘️",
                    "title": "Résidence sécurisée",
                    "title_en": "Gated community",
                    "description": "Condominium fermé, équipements",
                    "description_en": "Gated condominium, amenities"
                },
                {
                    "value": "flexible_housing",
                    "icon": "🎯",
                    "title": "Flexible sur le type",
                    "title_en": "Flexible on type",
                    "description": "Ouvert à différentes options",
                    "description_en": "Open to different options"
                }
            ]
        },

        // ===== 10. STYLE DE TRANSPORT =====
        {
            "id": "brazil_transport_style",
            "title": "🚗 Comment préférez-vous vous déplacer ?",
            "title_en": "🚗 How do you prefer to get around?",
            "category": "transport",
            "type": "single",
            "description": "Choisissez votre mode de transport principal",
            "description_en": "Choose your main mode of transport",
            "weight": 6,
            "options": [
                {
                    "value": "public_transport",
                    "icon": "🚇",
                    "title": "Transport public",
                    "title_en": "Public transport",
                    "description": "Métro, bus, économique et écologique",
                    "description_en": "Metro, bus, economical and ecological"
                },
                {
                    "value": "own_car",
                    "icon": "🚗",
                    "title": "Voiture personnelle",
                    "title_en": "Personal car",
                    "description": "Liberté, flexibilité, autonomie",
                    "description_en": "Freedom, flexibility, autonomy"
                },
                {
                    "value": "walking_cycling",
                    "icon": "🚶‍♂️",
                    "title": "À pied / Vélo",
                    "title_en": "Walking / Bike",
                    "description": "Santé, proximité, mobilité douce",
                    "description_en": "Health, proximity, soft mobility"
                },
                {
                    "value": "ride_sharing",
                    "icon": "📱",
                    "title": "Uber / Apps de transport",
                    "title_en": "Uber / Transport apps",
                    "description": "Pratique, sans contrainte de possession",
                    "description_en": "Convenient, no ownership constraints"
                },
                {
                    "value": "mixed_transport",
                    "icon": "🔄",
                    "title": "Transport mixte",
                    "title_en": "Mixed transport",
                    "description": "Combinaison selon les besoins",
                    "description_en": "Combination according to needs"
                }
            ]
        },

        // ===== 11. PRIORITÉS SÉCURITÉ =====
        {
            "id": "brazil_safety_priorities",
            "title": "🛡️ Quelle est votre approche de la sécurité ?",
            "title_en": "🛡️ What is your approach to safety?",
            "category": "security",
            "type": "single",
            "description": "Comment évaluez-vous l'importance de la sécurité ?",
            "description_en": "How do you assess the importance of safety?",
            "weight": 8,
            "options": [
                {
                    "value": "safety_paramount",
                    "icon": "🚨",
                    "title": "Sécurité prioritaire",
                    "title_en": "Safety paramount",
                    "description": "Maximum sécurité, peu de compromis",
                    "description_en": "Maximum safety, few compromises"
                },
                {
                    "value": "reasonable_caution",
                    "icon": "⚖️",
                    "title": "Prudence raisonnable",
                    "title_en": "Reasonable caution",
                    "description": "Équilibre sécurité et liberté",
                    "description_en": "Balance safety and freedom"
                },
                {
                    "value": "local_adaptation",
                    "icon": "🎯",
                    "title": "Adaptation locale",
                    "title_en": "Local adaptation",
                    "description": "Apprendre les codes locaux de sécurité",
                    "description_en": "Learn local safety codes"
                },
                {
                    "value": "community_safety",
                    "icon": "👥",
                    "title": "Sécurité communautaire",
                    "title_en": "Community safety",
                    "description": "Quartier solidaire, voisinage actif",
                    "description_en": "Supportive neighborhood, active community"
                }
            ]
        },

        // ===== 12. CULTURE ALIMENTAIRE =====
        {
            "id": "brazil_food_culture",
            "title": "🍽️ Quelle est votre relation avec la cuisine brésilienne ?",
            "title_en": "🍽️ What is your relationship with Brazilian cuisine?",
            "category": "food",
            "type": "single",
            "description": "Comment envisagez-vous la gastronomie locale ?",
            "description_en": "How do you envision local gastronomy?",
            "weight": 5,
            "options": [
                {
                    "value": "local_cuisine",
                    "icon": "🇧🇷",
                    "title": "Cuisine locale exclusive",
                    "title_en": "Exclusive local cuisine",
                    "description": "Feijoada, açaí, cuisine régionale",
                    "description_en": "Feijoada, açaí, regional cuisine"
                },
                {
                    "value": "food_adventure",
                    "icon": "🎯",
                    "title": "Aventure culinaire",
                    "title_en": "Culinary adventure",
                    "description": "Explorer toutes les saveurs brésiliennes",
                    "description_en": "Explore all Brazilian flavors"
                },
                {
                    "value": "international_food",
                    "icon": "🌍",
                    "title": "Cuisine internationale",
                    "title_en": "International cuisine",
                    "description": "Variété, restaurants du monde entier",
                    "description_en": "Variety, restaurants from around the world"
                },
                {
                    "value": "healthy_eating",
                    "icon": "🥗",
                    "title": "Alimentation saine",
                    "title_en": "Healthy eating",
                    "description": "Fruits tropicaux, produits frais, équilibre",
                    "description_en": "Tropical fruits, fresh products, balance"
                },
                {
                    "value": "food_flexible",
                    "icon": "🔄",
                    "title": "Flexible sur la nourriture",
                    "title_en": "Food flexible",
                    "description": "Je m'adapte à ce qui est disponible",
                    "description_en": "I adapt to what's available"
                }
            ]
        }

    ] // Fin brazil_residents
}; // Fin QUESTIONS_DATA_BRAZIL

// ===== INTÉGRATION GLOBALE =====
window.QUESTIONS_DATA = window.QUESTIONS_DATA || {};
window.QUESTIONS_DATA.brazil_residents = window.QUESTIONS_DATA_BRAZIL.brazil_residents;
window.QUESTIONS_DATA.brazil = window.QUESTIONS_DATA_BRAZIL.brazil_residents;

// 🎯 VALIDATION ET LOGS
console.log('🇧🇷 Brazil questions data loaded - 12 questions avec clés matchées pour l\'algorithme');
console.log('🇧🇷 Questions keys:', window.QUESTIONS_DATA_BRAZIL.brazil_residents.map(q => q.id));
console.log('✅ Total questions Brazil Residents:', window.QUESTIONS_DATA_BRAZIL.brazil_residents.length);

// Export pour compatibilité
if (typeof module !== 'undefined' && module.exports) {
    module.exports = window.QUESTIONS_DATA_BRAZIL;
}
