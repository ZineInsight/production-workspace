/**
 * 🎯 API CONNECTOR SIMPLE - ZineInsight Revolutionary
 * ================================================
 * Connexion directe à ton site production - Ultra simple !
 */

class SimpleAPI {
    constructor() {
        this.config = window.SimpleConfig?.config || {
            apiBaseUrl: 'http://localhost:8000',
            timeout: 15000
        };

        console.log('🚀 Simple API initialized');
    }

    // Méthode générale pour appeler ton site
    async call(endpoint, data = null) {
        const url = `${this.config.apiBaseUrl}${endpoint}`;

        const options = {
            method: data ? 'POST' : 'GET',
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json'
            }
        };

        if (data) {
            options.body = JSON.stringify(data);
        }

        console.log(`🔄 API Call: ${options.method} ${url}`, data || '');

        try {
            const response = await fetch(url, options);

            // Essayer de parser en JSON, sinon retourner le texte
            let result;
            const text = await response.text();
            try {
                result = JSON.parse(text);
            } catch {
                result = { raw: text, success: false };
            }

            console.log(`📊 API Response (${response.status}):`, result);
            return { success: response.ok, data: result, status: response.status };

        } catch (error) {
            console.error('❌ API Error:', error);
            return { success: false, error: error.message, data: null };
        }
    }

    // ZScore spécifique
    async calculateZScore(params = {}) {
        console.log('🎯 Calculating ZScore with your production APIs...');

        // Essayer différents endpoints possibles
        const endpoints = [
            '/api/calculate',        // NOUVEAU BACKEND RÉVOLUTIONNAIRE !
            '/api/calculate-score',  // Ancien endpoint
            '/api/zscore',
            '/zscore/calculate',
            '/calculate-score'
        ];

        for (const endpoint of endpoints) {
            const result = await this.call(endpoint, params);
            if (result.success) {
                console.log(`✅ ZScore success via: ${endpoint}`);
                return result.data;
            }
        }

        // Si aucun endpoint ne marche, simulation pour démo
        console.log('🎭 Using demo mode - No API endpoint found');
        return this.mockZScore(params);
    }

    // Mock ZScore pour démo
    mockZScore(params) {
        const cities = [
            { name: 'Lisbonne', country: 'Portugal', score: 9.4, reason: 'Coût de vie optimal, climat parfait' },
            { name: 'Berlin', country: 'Allemagne', score: 9.1, reason: 'Opportunités tech, culture vibrante' },
            { name: 'Austin', country: 'USA', score: 8.9, reason: 'Hub technologique, pas de taxes' },
            { name: 'Montréal', country: 'Canada', score: 8.7, reason: 'Qualité de vie, facilité immigration' },
            { name: 'Barcelone', country: 'Espagne', score: 8.5, reason: 'Mer, climat, coût de vie raisonnable' }
        ];

        return {
            success: true,
            total_cities: cities.length,
            cities: cities,
            params: params,
            note: 'Simulation - Connectez vos vraies APIs pour des résultats réels'
        };
    }

    // Test de connectivité
    async testConnection() {
        console.log('🧪 Testing connection to your site...');

        const result = await this.call('/api/health');
        if (!result.success) {
            // Essayer juste la racine
            const homeResult = await this.call('/');
            return {
                siteOnline: homeResult.success,
                apiAvailable: false,
                message: homeResult.success ?
                    'Site accessible mais pas d\'API détectée' :
                    'Site non accessible'
            };
        }

        return {
            siteOnline: true,
            apiAvailable: true,
            message: 'API disponible !'
        };
    }
}

// Export global
window.SimpleAPI = new SimpleAPI();

// Helper pour l'utiliser facilement
window.ZScore = {
    calculate: (params) => window.SimpleAPI.calculateZScore(params),
    test: () => window.SimpleAPI.testConnection()
};
