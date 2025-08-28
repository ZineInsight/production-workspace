/**
 * 🎯 CONFIGURATION SIMPLE - ZineInsight Revolutionary
 * =================================================
 * Configuration ultra-simple : Frontend → Ton site production
 */

class SimpleConfig {
    constructor() {
        this.config = this.getConfig();
        console.log('🎯 Simple config loaded:', this.config.note);
    }

    getConfig() {
        // Détection simple
        const port = window.location.port;

        if (port === '3000') {
            // Frontend révolutionnaire → Ton site production
            return {
                apiBaseUrl: 'http://localhost:8000',
                environment: 'revolutionary',
                debug: true,
                timeout: 15000,
                note: 'Frontend révolutionnaire connecté à ton site production'
            };
        } else {
            // Production ou autre
            return {
                apiBaseUrl: '',  // Même domaine - API via Nginx
                environment: 'production',
                debug: false,
                timeout: 10000,
                note: 'Production mode - API via Nginx'
            };
        }
    }

    getApiUrl(endpoint = '') {
        // Nettoyage de l'endpoint
        const cleanEndpoint = endpoint.startsWith('/') ? endpoint : '/' + endpoint;
        return `${this.config.apiBaseUrl}${cleanEndpoint}`;
    }

    // API directe vers ton site
    async callYourSite(endpoint, options = {}) {
        const url = this.getApiUrl(endpoint);

        console.log(`🔄 Calling your site: ${url}`);

        try {
            const response = await fetch(url, {
                ...options,
                mode: 'cors',
                headers: {
                    'Content-Type': 'application/json',
                    ...options.headers
                }
            });

            if (!response.ok) {
                throw new Error(`HTTP ${response.status}: ${response.statusText}`);
            }

            const data = await response.json();
            console.log('✅ Response from your site:', data);
            return data;

        } catch (error) {
            console.error('❌ Error calling your site:', error);
            throw error;
        }
    }
}

// Export global
window.SimpleConfig = new SimpleConfig();
