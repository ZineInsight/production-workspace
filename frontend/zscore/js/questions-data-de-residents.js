// 🇩🇪 QUESTIONS SPÉCIFIQUES ALLEMAGNE RESIDENTS
// Ciblé pour résidents allemands cherchant relocation domestique
// Architecture standardisée : 12 questions avec filtres régionaux/linguistiques

window.QUESTIONS_DATA_GERMANY = {
    "germany_residents": [
        {
            "id": "germany_main_priority",
            "title": "🎯 Quelle est votre priorité principale pour votre nouvelle vie en Allemagne ?",
            "title_en": "🎯 What is your main priority for your new life in Germany?",
            "category": "life_priority",
            "type": "single",
            "weight": 9,
            "options": [
                {
                    "value": "career_growth",
                    "icon": "🏃‍♂️",
                    "title": "Booster ma carrière",
                    "title_en": "Boost my career",
                    "description": "Opportunités pro, secteur tech, networking",
                    "description_en": "Professional opportunities, tech sector, networking"
                },
                {
                    "value": "cost_optimization",
                    "icon": "💰",
                    "title": "Optimiser mes finances",
                    "title_en": "Optimize my finances",
                    "description": "Coût de vie, logement abordable, taxes",
                    "description_en": "Cost of living, affordable housing, taxes"
                },
                {
                    "value": "quality_life",
                    "icon": "🌳",
                    "title": "Améliorer ma qualité de vie",
                    "title_en": "Improve my quality of life",
                    "description": "Équilibre travail-vie, environnement, bien-être",
                    "description_en": "Work-life balance, environment, well-being"
                },
                {
                    "value": "family_education",
                    "icon": "👨‍👩‍👧‍👦",
                    "title": "Famille et éducation",
                    "title_en": "Family and education",
                    "description": "Écoles, sécurité, environnement familial",
                    "description_en": "Schools, security, family environment"
                },
                {
                    "value": "culture_lifestyle",
                    "icon": "🎭",
                    "title": "Culture et lifestyle",
                    "title_en": "Culture and lifestyle",
                    "description": "Vie culturelle, restaurants, sorties",
                    "description_en": "Cultural life, restaurants, outings"
                }
            ]
        },
        {
            "id": "germany_region_preference",
            "title": "🗺️ Quelle région d'Allemagne vous attire le plus ?",
            "title_en": "🗺️ Which region of Germany attracts you most?",
            "category": "geography",
            "type": "single",
            "weight": 8,
            "options": [
                {
                    "value": "southern_germany",
                    "icon": "🏔️",
                    "title": "Sud (Bayern, Baden-Württemberg)",
                    "title_en": "South (Bavaria, Baden-Württemberg)",
                    "description": "Munich, Stuttgart, Nuremberg - Montagnes, technologie",
                    "description_en": "Munich, Stuttgart, Nuremberg - Mountains, technology"
                },
                {
                    "value": "western_germany",
                    "icon": "🏭",
                    "title": "Ouest (NRW, Hesse, Rhénanie)",
                    "title_en": "West (NRW, Hesse, Rhineland)",
                    "description": "Cologne, Frankfurt, Düsseldorf - Finance, industrie",
                    "description_en": "Cologne, Frankfurt, Düsseldorf - Finance, industry"
                },
                {
                    "value": "northern_germany",
                    "icon": "🌊",
                    "title": "Nord (Hamburg, Bremen, Schleswig)",
                    "title_en": "North (Hamburg, Bremen, Schleswig)",
                    "description": "Hamburg, Hannover, Kiel - Ports, commerce",
                    "description_en": "Hamburg, Hannover, Kiel - Ports, commerce"
                },
                {
                    "value": "eastern_germany",
                    "icon": "🏛️",
                    "title": "Est (Berlin, Saxe, Brandeburg)",
                    "title_en": "East (Berlin, Saxony, Brandenburg)",
                    "description": "Berlin, Leipzig, Dresden - Histoire, startup",
                    "description_en": "Berlin, Leipzig, Dresden - History, startup"
                },
                {
                    "value": "region_flexible",
                    "icon": "🎯",
                    "title": "Flexible selon opportunités",
                    "title_en": "Flexible according to opportunities",
                    "description": "Je privilégie autres critères",
                    "description_en": "I prioritize other criteria"
                }
            ]
        },
        {
            "id": "germany_budget_range",
            "title": "💶 Quel est votre budget logement mensuel envisagé ?",
            "title_en": "💶 What is your envisioned monthly housing budget?",
            "category": "budget",
            "type": "single",
            "weight": 8,
            "options": [
                {
                    "value": "budget_low",
                    "icon": "💡",
                    "title": "600-900€/mois",
                    "title_en": "600-900€/month",
                    "description": "Recherche maximum d'économies",
                    "description_en": "Looking for maximum savings"
                },
                {
                    "value": "budget_medium",
                    "icon": "🏠",
                    "title": "900-1500€/mois",
                    "title_en": "900-1500€/month",
                    "description": "Équilibre coût/qualité",
                    "description_en": "Cost/quality balance"
                },
                {
                    "value": "budget_high",
                    "icon": "🏆",
                    "title": "1500-2500€/mois",
                    "title_en": "1500-2500€/month",
                    "description": "Confort et localisation privilégiés",
                    "description_en": "Comfort and location prioritized"
                },
                {
                    "value": "budget_premium",
                    "icon": "💎",
                    "title": "2500€+/mois",
                    "title_en": "2500€+/month",
                    "description": "Budget généreux, meilleur possible",
                    "description_en": "Generous budget, best possible"
                }
            ]
        },
        {
            "id": "germany_work_style",
            "title": "💻 Quel est votre mode de travail idéal ?",
            "title_en": "💻 What is your ideal work style?",
            "category": "work",
            "type": "single",
            "weight": 7,
            "options": [
                {
                    "value": "full_office",
                    "icon": "🏢",
                    "title": "Bureau traditionnel",
                    "title_en": "Traditional office",
                    "description": "Présentiel, entreprise établie",
                    "description_en": "In-person, established company"
                },
                {
                    "value": "hybrid_modern",
                    "icon": "🔄",
                    "title": "Hybride moderne",
                    "title_en": "Modern hybrid",
                    "description": "Télétravail + bureau, flexibilité",
                    "description_en": "Remote work + office, flexibility"
                },
                {
                    "value": "full_remote",
                    "icon": "🏡",
                    "title": "100% remote",
                    "title_en": "100% remote",
                    "description": "Travail à distance, indépendance géographique",
                    "description_en": "Remote work, geographical independence"
                },
                {
                    "value": "startup_dynamic",
                    "icon": "🚀",
                    "title": "Environnement startup",
                    "title_en": "Startup environment",
                    "description": "Dynamique, innovation, croissance",
                    "description_en": "Dynamic, innovation, growth"
                }
            ]
        },
        {
            "id": "germany_transport_priority",
            "title": "🚊 Quelle est votre priorité en transport ?",
            "title_en": "🚊 What is your priority in transportation?",
            "category": "mobility",
            "type": "single",
            "weight": 7,
            "options": [
                {
                    "value": "public_transport_fan",
                    "icon": "🚇",
                    "title": "Transport public excellent",
                    "title_en": "Excellent public transport",
                    "description": "S-Bahn, U-Bahn, tramway efficaces",
                    "description_en": "Efficient S-Bahn, U-Bahn, tramway"
                },
                {
                    "value": "walkable_city",
                    "icon": "🚶‍♂️",
                    "title": "Ville piétonne",
                    "title_en": "Walkable city",
                    "description": "Tout accessible à pied/vélo",
                    "description_en": "Everything accessible by foot/bike"
                },
                {
                    "value": "car_friendly",
                    "icon": "🚗",
                    "title": "Voiture pratique",
                    "title_en": "Car friendly",
                    "description": "Parking, autoroutes, flexibilité",
                    "description_en": "Parking, highways, flexibility"
                },
                {
                    "value": "mixed_mobility",
                    "icon": "🔀",
                    "title": "Mobilité mixte",
                    "title_en": "Mixed mobility",
                    "description": "Combine tous les modes selon besoin",
                    "description_en": "Combines all modes according to need"
                }
            ]
        },
        {
            "id": "germany_tax_sensitivity",
            "title": "📊 Quelle est votre sensibilité aux taxes allemandes ?",
            "title_en": "📊 What is your sensitivity to German taxes?",
            "category": "taxation",
            "type": "single",
            "weight": 6,
            "options": [
                {
                    "value": "tax_optimization",
                    "icon": "💼",
                    "title": "Optimisation fiscale",
                    "title_en": "Tax optimization",
                    "description": "Minimiser impôts, Kirchensteuer, taxes locales",
                    "description_en": "Minimize taxes, Kirchensteuer, local taxes"
                },
                {
                    "value": "moderate_tax",
                    "icon": "⚖️",
                    "title": "Taxation modérée",
                    "title_en": "Moderate taxation",
                    "description": "Acceptable si services publics de qualité",
                    "description_en": "Acceptable if quality public services"
                },
                {
                    "value": "services_priority",
                    "icon": "🏥",
                    "title": "Services avant taxes",
                    "title_en": "Services before taxes",
                    "description": "Priorise santé, éducation, infrastructure",
                    "description_en": "Prioritizes health, education, infrastructure"
                },
                {
                    "value": "tax_indifferent",
                    "icon": "🤷‍♂️",
                    "title": "Peu important",
                    "title_en": "Not important",
                    "description": "Autres critères plus importants",
                    "description_en": "Other criteria more important"
                }
            ]
        },
        {
            "id": "germany_lifestyle_preference",
            "title": "🎭 Quel lifestyle vous correspond en Allemagne ?",
            "title_en": "🎭 What lifestyle suits you in Germany?",
            "category": "lifestyle",
            "type": "single",
            "weight": 6,
            "options": [
                {
                    "value": "urban_cosmopolitan",
                    "icon": "🌆",
                    "title": "Urbain cosmopolite",
                    "title_en": "Urban cosmopolitan",
                    "description": "Métropole, diversité, énergie",
                    "description_en": "Metropolis, diversity, energy"
                },
                {
                    "value": "cultural_traditional",
                    "icon": "🏰",
                    "title": "Culturel traditionnel",
                    "title_en": "Cultural traditional",
                    "description": "Histoire, architecture, tradition allemande",
                    "description_en": "History, architecture, German tradition"
                },
                {
                    "value": "balanced_suburban",
                    "icon": "🏡",
                    "title": "Équilibré résidentiel",
                    "title_en": "Balanced residential",
                    "description": "Banlieue qualité, famille, tranquillité",
                    "description_en": "Quality suburbs, family, tranquility"
                },
                {
                    "value": "dynamic_nightlife",
                    "icon": "🍺",
                    "title": "Dynamique nocturne",
                    "title_en": "Dynamic nightlife",
                    "description": "Bars, clubs, restaurants, sorties",
                    "description_en": "Bars, clubs, restaurants, outings"
                }
            ]
        },
        {
            "id": "germany_climate_preference",
            "title": "🌤️ Quel climat allemand préférez-vous ?",
            "title_en": "🌤️ Which German climate do you prefer?",
            "category": "climate",
            "type": "single",
            "weight": 5,
            "options": [
                {
                    "value": "mild_southern",
                    "icon": "☀️",
                    "title": "Doux du sud",
                    "title_en": "Mild southern",
                    "description": "Bayern, Baden-Württemberg - Plus chaud",
                    "description_en": "Bavaria, Baden-Württemberg - Warmer"
                },
                {
                    "value": "oceanic_western",
                    "icon": "🌦️",
                    "title": "Océanique de l'ouest",
                    "title_en": "Western oceanic",
                    "description": "NRW, Rhénanie - Tempéré, humide",
                    "description_en": "NRW, Rhineland - Temperate, humid"
                },
                {
                    "value": "continental_eastern",
                    "icon": "❄️",
                    "title": "Continental de l'est",
                    "title_en": "Eastern continental",
                    "description": "Berlin, Saxe - Contrastes saisonniers",
                    "description_en": "Berlin, Saxony - Seasonal contrasts"
                },
                {
                    "value": "climate_adaptive",
                    "icon": "🌈",
                    "title": "Je m'adapte",
                    "title_en": "I adapt",
                    "description": "Le climat n'est pas un facteur",
                    "description_en": "Climate is not a factor"
                }
            ]
        },
        {
            "id": "germany_language_comfort",
            "title": "🗣️ Quel est votre niveau de confort linguistique ?",
            "title_en": "🗣️ What is your level of linguistic comfort?",
            "category": "language",
            "type": "single",
            "weight": 6,
            "options": [
                {
                    "value": "german_native",
                    "icon": "🇩🇪",
                    "title": "Allemand natif/courant",
                    "title_en": "Native/fluent German",
                    "description": "Aucune barrière linguistique",
                    "description_en": "No language barrier"
                },
                {
                    "value": "german_learning",
                    "icon": "📚",
                    "title": "Allemand en apprentissage",
                    "title_en": "Learning German",
                    "description": "Base solide, en progression",
                    "description_en": "Solid foundation, progressing"
                },
                {
                    "value": "english_priority",
                    "icon": "🇬🇧",
                    "title": "Préférence anglophone",
                    "title_en": "English preference",
                    "description": "Environnement international/anglophone",
                    "description_en": "International/English environment"
                },
                {
                    "value": "multilingual_comfort",
                    "icon": "🌍",
                    "title": "Multilingue flexible",
                    "title_en": "Flexible multilingual",
                    "description": "Confortable avec plusieurs langues",
                    "description_en": "Comfortable with multiple languages"
                }
            ]
        },
        {
            "id": "germany_career_focus",
            "title": "🎯 Quelle est votre orientation professionnelle prioritaire ?",
            "title_en": "🎯 What is your priority career focus?",
            "category": "career",
            "type": "single",
            "weight": 7,
            "options": [
                {
                    "value": "tech_innovation",
                    "icon": "💻",
                    "title": "Tech & Innovation",
                    "title_en": "Tech & Innovation",
                    "description": "Startups, digital, nouvelles technologies",
                    "description_en": "Startups, digital, new technologies"
                },
                {
                    "value": "industry_manufacturing",
                    "icon": "�",
                    "title": "Industrie & Manufacturing",
                    "title_en": "Industry & Manufacturing",
                    "description": "Automobile, ingénierie, production",
                    "description_en": "Automotive, engineering, production"
                },
                {
                    "value": "finance_business",
                    "icon": "�",
                    "title": "Finance & Business",
                    "title_en": "Finance & Business",
                    "description": "Banque, conseil, commerce",
                    "description_en": "Banking, consulting, commerce"
                },
                {
                    "value": "research_academia",
                    "icon": "🔬",
                    "title": "Recherche & Académique",
                    "title_en": "Research & Academic",
                    "description": "Universités, R&D, sciences",
                    "description_en": "Universities, R&D, sciences"
                }
            ]
        },
        {
            "id": "germany_housing_priority",
            "title": "🏠 Quelle est votre priorité en matière de logement ?",
            "title_en": "🏠 What is your housing priority?",
            "category": "housing",
            "type": "single",
            "weight": 8,
            "options": [
                {
                    "value": "city_center",
                    "icon": "�",
                    "title": "Centre-ville accessible",
                    "title_en": "Accessible city center",
                    "description": "Proximité transports, services, travail",
                    "description_en": "Close to transport, services, work"
                },
                {
                    "value": "suburban_family",
                    "icon": "🏡",
                    "title": "Banlieue familiale",
                    "title_en": "Family suburb",
                    "description": "Calme, espaces verts, écoles",
                    "description_en": "Quiet, green spaces, schools"
                },
                {
                    "value": "modern_districts",
                    "icon": "🏗️",
                    "title": "Quartiers modernes",
                    "title_en": "Modern districts",
                    "description": "Nouvelles constructions, équipements récents",
                    "description_en": "New construction, recent facilities"
                },
                {
                    "value": "historic_charm",
                    "icon": "🏰",
                    "title": "Charme historique",
                    "title_en": "Historic charm",
                    "description": "Architecture traditionnelle, patrimoine",
                    "description_en": "Traditional architecture, heritage"
                }
            ]
        },
        {
            "id": "germany_social_priorities",
            "title": "👥 Quelles sont vos priorités sociales ?",
            "title_en": "👥 What are your social priorities?",
            "category": "social",
            "type": "single",
            "weight": 6,
            "options": [
                {
                    "value": "international_community",
                    "icon": "🌍",
                    "title": "Communauté internationale",
                    "title_en": "International community",
                    "description": "Expats, diversité culturelle",
                    "description_en": "Expats, cultural diversity"
                },
                {
                    "value": "local_integration",
                    "icon": "🇩🇪",
                    "title": "Intégration locale",
                    "title_en": "Local integration",
                    "description": "Culture allemande, communautés locales",
                    "description_en": "German culture, local communities"
                },
                {
                    "value": "professional_network",
                    "icon": "💼",
                    "title": "Réseau professionnel",
                    "title_en": "Professional network",
                    "description": "Collègues, opportunités business",
                    "description_en": "Colleagues, business opportunities"
                },
                {
                    "value": "balanced_lifestyle",
                    "icon": "⚖️",
                    "title": "Équilibre vie privée",
                    "title_en": "Work-life balance",
                    "description": "Famille, loisirs, bien-être",
                    "description_en": "Family, leisure, well-being"
                }
            ]
        }
    ]
};

// ⚠️ OBLIGATOIRE - Alias pour compatibilité avec analysis.js
window.QUESTIONS_DATA = window.QUESTIONS_DATA || {};
window.QUESTIONS_DATA.germany_residents = window.QUESTIONS_DATA_GERMANY.germany_residents;
window.QUESTIONS_DATA.germany = window.QUESTIONS_DATA_GERMANY.germany_residents;
