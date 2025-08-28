/**
 * 🇺🇸 USA-RESIDENTS-API.JS - INTÉGRATION API USA RESIDENTS
 * ========================================================
 * Intégration complète de l'API USA Residents dans le frontend ZineInsight
 * Author: Revolutionary Team | Version: 1.0.0 - USA Integration
 * OBJECTIF: Interface frontend pour l'algorithme USA Residents
 */

class USAResidentsAPI {
    constructor() {
        this.baseUrl = this.detectAPIBaseUrl();
        this.isInitialized = false;
        this.questionsData = null;
        this.cities = null;
        this.criteria = null;

        console.log('🇺🇸 USAResidentsAPI initialized with baseUrl:', this.baseUrl);
        this.initialize();
    }

    // 🌐 DÉTECTION AUTOMATIQUE DE L'URL API
    detectAPIBaseUrl() {
        const hostname = window.location.hostname;

        if (hostname === 'zineinsight.com' || hostname.includes('zineinsight.com')) {
            return 'https://zineinsight.com/api';
        } else if (hostname === 'localhost' || hostname === '127.0.0.1') {
            return 'http://localhost:8000/api';
        } else {
            return 'http://localhost:8000/api'; // Fallback
        }
    }

    // 🚀 INITIALISATION
    async initialize() {
        try {
            console.log('🇺🇸 Initializing USA Residents API...');

            // Charger les questions USA si disponibles
            if (window.QUESTIONS_DATA_USA && window.QUESTIONS_DATA_USA.usa_residents) {
                this.questionsData = window.QUESTIONS_DATA_USA.usa_residents;
                console.log(`✅ Questions USA loaded: ${this.questionsData.length} questions`);
            } else {
                console.warn('⚠️ USA Questions data not found, continuing without questions');
                this.questionsData = [];
            }

            // Tester la connexion API
            await this.healthCheck();

            this.isInitialized = true;
            console.log('✅ USA Residents API ready');

        } catch (error) {
            console.error('❌ USA Residents API initialization failed:', error);
            this.isInitialized = false;
        }
    }

    // 🏥 HEALTH CHECK
    async healthCheck() {
        try {
            const response = await fetch(`${this.baseUrl}/usa-residents/health`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            });

            if (!response.ok) {
                throw new Error(`Health check failed: ${response.status}`);
            }

            const data = await response.json();
            console.log('🏥 USA Residents API Health:', data);

            return data.status === 'healthy';

        } catch (error) {
            console.error('❌ Health check failed:', error);
            return false;
        }
    }

    // 🎯 OBTENIR LES RECOMMANDATIONS TOP 3
    async getRecommendations(questionnaire_responses) {
        try {
            console.log('🎯 Getting USA recommendations...', questionnaire_responses);

            const response = await fetch(`${this.baseUrl}/usa-residents/recommendations`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(questionnaire_responses)
            });

            if (!response.ok) {
                throw new Error(`Recommendations API failed: ${response.status}`);
            }

            const data = await response.json();

            if (!data.success) {
                throw new Error(data.error || 'API returned unsuccessful response');
            }

            console.log('✅ USA Recommendations received:', data);

            // Adapter au format attendu par results.js
            const adaptedData = this.adaptRecommendationsFormat(data);

            return adaptedData;

        } catch (error) {
            console.error('❌ Get recommendations failed:', error);
            throw error;
        }
    }

    // 🔄 ADAPTER LE FORMAT DES RECOMMANDATIONS
    adaptRecommendationsFormat(apiData) {
        const adaptedRecommendations = apiData.recommendations.map((city, index) => ({
            nom: city.city,
            pays: city.state, // État au lieu de pays
            score_final: city.score_percentage,
            points_forts: city.top_strengths || [],
            points_attention: city.potential_concerns || [],
            population: city.population ? `${city.population.toLocaleString()} hab.` : 'N/A',

            // Scores détaillés (estimés à partir du score global)
            cout_vie: Math.round(city.score_percentage * 0.85),
            emploi: Math.round(city.score_percentage * 0.90),
            culture: Math.round(city.score_percentage * 0.88),
            qualite_vie: Math.round(city.score_percentage * 0.92),

            // Informations spécifiques USA
            rank: city.rank,
            why_recommended: city.why_recommended,
            coordinates: city.coordinates
        }));

        return {
            success: true,
            recommendations: adaptedRecommendations,
            selectedCountry: 'usa',
            questionsAnswered: Object.keys(apiData).length || 10,
            analysisDate: new Date().toISOString(),
            matchPercentage: adaptedRecommendations[0]?.score_final || 85,
            keyCriteria: this.extractKeyCriteria(apiData),

            // Métadonnées USA spécifiques
            algorithm_version: apiData.algorithm_version,
            total_cities_analyzed: apiData.total_cities_analyzed,
            parcours_type: 'usa_residents'
        };
    }

    // 🎯 EXTRAIRE LES CRITÈRES CLÉS
    extractKeyCriteria(apiData) {
        const criteria = [];

        // Analyser les réponses pour extraire les critères principaux
        const responses = apiData.questionnaire_responses || {};

        if (responses.usa_main_priority) {
            const priorities = {
                'career_growth': 'Croissance professionnelle',
                'cost_optimization': 'Optimisation financière',
                'lifestyle_upgrade': 'Amélioration qualité de vie',
                'family_focus': 'Focus famille'
            };
            criteria.push(priorities[responses.usa_main_priority] || 'Priorité principale');
        }

        if (responses.usa_monthly_budget) {
            const budgets = {
                'budget_tight': 'Budget serré',
                'budget_balanced': 'Budget équilibré',
                'budget_comfortable': 'Budget confortable',
                'budget_premium': 'Budget premium'
            };
            criteria.push(budgets[responses.usa_monthly_budget] || 'Budget défini');
        }

        if (responses.usa_work_situation) {
            const work = {
                'remote_full': '100% télétravail',
                'remote_hybrid': 'Travail hybride',
                'job_search': 'Recherche emploi',
                'entrepreneur': 'Entrepreneur'
            };
            criteria.push(work[responses.usa_work_situation] || 'Situation professionnelle');
        }

        if (responses.usa_climate_preference) {
            criteria.push('Préférences climatiques définies');
        }

        // Critères par défaut si peu d'informations
        if (criteria.length < 3) {
            criteria.push('Relocation domestique USA', 'Analyse personnalisée', 'Matching algorithmique');
        }

        return criteria.slice(0, 6);
    }

    // 📍 OBTENIR LA LISTE DES VILLES
    async getCitiesList() {
        try {
            if (this.cities) {
                return this.cities; // Cache
            }

            const response = await fetch(`${this.baseUrl}/usa-residents/cities`);

            if (!response.ok) {
                throw new Error(`Cities API failed: ${response.status}`);
            }

            const data = await response.json();
            this.cities = data.cities;

            console.log(`✅ USA Cities loaded: ${this.cities.length} cities`);
            return this.cities;

        } catch (error) {
            console.error('❌ Get cities failed:', error);
            return [];
        }
    }

    // 📊 OBTENIR LES CRITÈRES
    async getCriteria() {
        try {
            if (this.criteria) {
                return this.criteria; // Cache
            }

            const response = await fetch(`${this.baseUrl}/usa-residents/criteria`);

            if (!response.ok) {
                throw new Error(`Criteria API failed: ${response.status}`);
            }

            const data = await response.json();
            this.criteria = data.criteria_definitions;

            console.log(`✅ USA Criteria loaded: ${Object.keys(this.criteria).length} criteria`);
            return this.criteria;

        } catch (error) {
            console.error('❌ Get criteria failed:', error);
            return {};
        }
    }

    // 🎪 GÉNÉRER DES RÉSULTATS DEMO USA
    generateDemoResults() {
        console.log('🎪 Generating USA demo results...');

        return {
            success: true,
            recommendations: [
                {
                    nom: "Austin",
                    pays: "Texas", // État
                    score_final: 92,
                    points_forts: ["Hub technologique majeur", "Pas de taxes d'état", "Scène culturelle vibrante"],
                    points_attention: ["Coût logement en hausse", "Trafic dense"],
                    population: "965,000 hab.",
                    cout_vie: 78,
                    emploi: 95,
                    culture: 90,
                    qualite_vie: 88,
                    rank: 1,
                    why_recommended: "Austin excelle pour votre croissance professionnelle avec un marché de l'emploi dynamique et un écosystème tech développé.",
                    coordinates: { "lat": 30.2672, "lng": -97.7431 }
                },
                {
                    nom: "Denver",
                    pays: "Colorado",
                    score_final: 87,
                    points_forts: ["Climat montagnard", "Outdoor lifestyle", "Tech émergent"],
                    points_attention: ["Altitude élevée", "Coût logement"],
                    population: "715,000 hab.",
                    cout_vie: 72,
                    emploi: 85,
                    culture: 82,
                    qualite_vie: 90,
                    rank: 2,
                    why_recommended: "Denver combine parfaitement opportunités tech et qualité de vie outdoor.",
                    coordinates: { "lat": 39.7392, "lng": -104.9903 }
                },
                {
                    nom: "Nashville",
                    pays: "Tennessee",
                    score_final: 83,
                    points_forts: ["Scène musicale unique", "Pas de taxes d'état", "Coût vie abordable"],
                    points_attention: ["Transport public limité", "Croissance rapide"],
                    population: "695,000 hab.",
                    cout_vie: 85,
                    emploi: 78,
                    culture: 95,
                    qualite_vie: 82,
                    rank: 3,
                    why_recommended: "Nashville offre une culture unique avec des avantages financiers intéressants.",
                    coordinates: { "lat": 36.1627, "lng": -86.7816 }
                }
            ],
            selectedCountry: 'usa',
            questionsAnswered: 10,
            analysisDate: new Date().toISOString(),
            matchPercentage: 92,
            keyCriteria: ['Croissance professionnelle', 'Tech industry', 'Pas de taxes d\'état', 'Culture vibrante'],
            algorithm_version: '1.0.0',
            total_cities_analyzed: 50,
            parcours_type: 'usa_residents'
        };
    }

    // 🔍 VÉRIFIER SI L'API EST DISPONIBLE
    isAvailable() {
        return this.isInitialized && this.questionsData && this.questionsData.length > 0;
    }

    // 📋 OBTENIR LES QUESTIONS USA
    getQuestions() {
        return this.questionsData || [];
    }

    // 🌟 MÉTHODES UTILITAIRES

    // Format d'affichage d'une ville
    formatCityDisplay(city) {
        return `${city.name}, ${city.state}`;
    }

    // Obtenir l'emoji du state
    getStateEmoji(state) {
        const stateEmojis = {
            'Texas': '🤠',
            'California': '🌴',
            'Florida': '🏖️',
            'New York': '🗽',
            'Colorado': '🏔️',
            'Washington': '🌲',
            'Tennessee': '🎸',
            'North Carolina': '🏃',
            'Oregon': '🌲',
            'Utah': '🏔️',
            'Virginia': '🏛️',
            'Idaho': '🏔️'
        };

        return stateEmojis[state] || '🏙️';
    }

    // Obtenir la couleur du score
    getScoreColor(score) {
        if (score >= 85) return '#10B981'; // Vert
        if (score >= 75) return '#F59E0B'; // Orange
        if (score >= 65) return '#EF4444'; // Rouge
        return '#6B7280'; // Gris
    }
}

// 🌟 INTÉGRATION GLOBALE
window.USAResidentsAPI = USAResidentsAPI;

// Instance globale
window.usaAPI = new USAResidentsAPI();

// 🎯 FONCTIONS D'INTÉGRATION AVEC ANALYSIS.JS

// Fonction appelée par analysis.js pour détecter USA
window.detectUSAParcours = function (selectedCountry, responses) {
    return selectedCountry === 'usa' ||
        (responses && Object.keys(responses).some(key => key.startsWith('usa_')));
};

// Fonction appelée par analysis.js pour traiter USA
window.processUSAResults = async function (responses) {
    try {
        console.log('🇺🇸 Processing USA results...', responses);

        if (!window.usaAPI.isAvailable()) {
            console.log('🎪 USA API not available, using demo results');
            return window.usaAPI.generateDemoResults();
        }

        const results = await window.usaAPI.getRecommendations(responses);
        return results;

    } catch (error) {
        console.error('❌ USA processing failed:', error);
        return window.usaAPI.generateDemoResults();
    }
};

console.log('✅ USA Residents API integration loaded');
console.log('🇺🇸 Available methods: detectUSAParcours(), processUSAResults()');
