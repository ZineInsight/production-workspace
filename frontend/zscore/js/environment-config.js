/**
 * 🎯 CONFIGURATION ENVIRONNEMENT AUTOMATIQUE
 * ==========================================
 * Détecte automatiquement l'environnement et configure les APIs
 */

class EnvironmentConfig {
    constructor() {
        this.environment = this.detectEnvironment();
        this.config = this.getConfigForEnvironment();

        console.log(`🎯 Environment detected: ${this.environment}`);
        console.log(`🔗 API Base URL: ${this.config.apiBaseUrl}`);
    }

    detectEnvironment() {
        const hostname = window.location.hostname;
        const port = window.location.port;

        // Production - FORCÉ VERS TON SERVEUR
        if (hostname === 'zineinsight.com' || hostname.includes('zineinsight')) {
            return 'direct_production';  // Force vers ton serveur !
        }

        // Connexion directe : Frontend sur port 3000 → Ton site sur port 8000
        if (port === '3000') {
            // Détecter si le backend DEV (9000) est disponible
            return 'revolutionary_dev';  // Notre nouveau backend !
        }

        // Development - Backend révolutionnaire sur port 9000
        if (port === '9000') {
            return 'revolutionary_backend';
        }
        if (port === '8000') {
            return 'development_mock';
        }

        // Local avec site production
        if (hostname === 'localhost' && port === '8000') {
            return 'local_production';
        }

        // Default
        return 'development_bridge';
    }

    getConfigForEnvironment() {
        const configs = {
            production: {
                apiBaseUrl: 'http://91.99.237.55:8000/api',  // TON SERVEUR !
                wsUrl: 'wss://zineinsight.com/ws',
                environment: 'production',
                debug: true,  // Debug activé pour voir les erreurs
                cacheEnabled: false,  // Pas de cache pour les tests
                timeout: 10000
            },

            revolutionary_dev: {
                apiBaseUrl: 'http://localhost:8000/api',  // BACKEND REVOLUTIONARY SUR PORT 8000 !
                wsUrl: 'ws://localhost:8000/ws',
                environment: 'revolutionary_dev',
                debug: true,
                cacheEnabled: false,
                timeout: 15000,
                note: '🚀 Connected to Revolutionary Backend DEV sur port 8000'
            },

            revolutionary_backend: {
                apiBaseUrl: 'http://localhost:9000',  // Backend révolutionnaire direct
                wsUrl: 'ws://localhost:9000/ws',
                environment: 'revolutionary_backend',
                debug: true,
                cacheEnabled: false,
                timeout: 15000,
                note: '⚡ Revolutionary Backend Direct Access'
            },

            direct_production: {
                apiBaseUrl: 'https://zineinsight.com/api',  // MÊME DOMAINE AVEC PROXY NGINX !
                wsUrl: 'wss://zineinsight.com/ws',
                environment: 'production',
                debug: true,
                cacheEnabled: false,
                timeout: 15000,
                note: 'Production avec proxy nginx vers backend local'
            },

            development_bridge: {
                apiBaseUrl: 'http://localhost:5001/api',  // Bridge API
                wsUrl: 'ws://localhost:5001/ws',
                environment: 'development',
                debug: true,
                cacheEnabled: false,
                timeout: 30000,
                note: 'Connected to production bridge'
            },

            development_mock: {
                apiBaseUrl: 'http://localhost:5000/api',  // Mock API
                wsUrl: 'ws://localhost:5000/ws',
                environment: 'development',
                debug: true,
                cacheEnabled: false,
                timeout: 15000,
                note: 'Connected to mock API'
            },

            local_production: {
                apiBaseUrl: '/api',  // Même site
                wsUrl: 'ws://localhost:8000/ws',
                environment: 'local_production',
                debug: true,
                cacheEnabled: true,
                timeout: 15000,
                note: 'Direct connection to local production'
            }
        };

        return configs[this.environment] || configs.development_bridge;
    }

    getApiUrl(endpoint = '') {
        return `${this.config.apiBaseUrl}${endpoint}`;
    }

    isProduction() {
        return this.environment === 'production';
    }

    isDevelopment() {
        return this.environment.includes('development');
    }

    shouldUseCache() {
        return this.config.cacheEnabled;
    }

    getTimeout() {
        return this.config.timeout;
    }

    enableDebugLogs() {
        return this.config.debug;
    }

    /**
     * Test de connectivité automatique
     */
    async testConnectivity() {
        try {
            // Test avec l'endpoint health qui existe vraiment
            const testUrl = `${this.config.apiBaseUrl}/health`; // Endpoint qui existe
            console.log(`🔍 Testing connectivity to: ${testUrl}`);

            const response = await fetch(testUrl, {
                method: 'GET',
                timeout: 5000
            });

            if (response.ok) {
                const data = await response.json();
                console.log('✅ API connectivity test passed');
                console.log('📊 API Status:', data);
                return { success: true, data };
            } else {
                throw new Error(`HTTP ${response.status}`);
            }

        } catch (error) {
            console.warn('⚠️ API connectivity test failed:', error.message);
            return { success: false, error: error.message };
        }
    }

    /**
     * Configuration adaptative basée sur les tests
     */
    async adaptConfiguration() {
        const connectivityTest = await this.testConnectivity();

        if (!connectivityTest.success) {
            console.warn('🔄 Primary API failed, trying fallbacks...');

            // Essayer des configurations alternatives
            const fallbacks = [
                'http://localhost:8000/api',  // Production locale (priorité)
                '/api',  // Relative (nginx proxy)
                'http://localhost:5000/api'   // Mock (fallback final)
            ];

            for (const fallbackUrl of fallbacks) {
                try {
                    const response = await fetch(`${fallbackUrl}/health`, { timeout: 3000 });
                    if (response.ok) {
                        console.log(`✅ Fallback API found: ${fallbackUrl}`);
                        this.config.apiBaseUrl = fallbackUrl;
                        return true;
                    }
                } catch (e) {
                    continue;
                }
            }

            console.error('❌ No working API found');
            return false;
        }

        return true;
    }

    /**
     * Informations de debug
     */
    getDebugInfo() {
        return {
            environment: this.environment,
            config: this.config,
            urls: {
                api: this.config.apiBaseUrl,
                websocket: this.config.wsUrl,
                current_page: window.location.href
            },
            browser: {
                userAgent: navigator.userAgent,
                language: navigator.language,
                cookieEnabled: navigator.cookieEnabled
            },
            timestamp: new Date().toISOString()
        };
    }
}

// Instance globale
window.environmentConfig = new EnvironmentConfig();

// Auto-test au chargement
document.addEventListener('DOMContentLoaded', async () => {
    console.log('🔧 Running environment configuration...');

    const adapted = await window.environmentConfig.adaptConfiguration();
    if (adapted) {
        console.log('✅ Environment configuration complete');
    } else {
        console.warn('⚠️ Environment configuration had issues');
    }

    // Debug info si en développement
    if (window.environmentConfig.enableDebugLogs()) {
        console.log('🐛 Debug Info:', window.environmentConfig.getDebugInfo());
    }

    // Émettre un événement pour que les autres modules puissent réagir
    window.dispatchEvent(new CustomEvent('environmentConfigured', {
        detail: window.environmentConfig
    }));
});

// Export pour les modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = EnvironmentConfig;
}
