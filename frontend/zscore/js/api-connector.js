/**
 * 🔗 API CONNECTOR - Bridge entre SPA et Backend
 * =============================================
 * Connecteur intelligent pour tous tes APIs backend
 */

class APIConnector {
    constructor() {
        // Attendre que la configuration environnement soit prête
        this.environmentConfig = null;
        this.isConfigured = false;

        // Configuration par défaut
        this.config = {
            // Gateway principal (sera adapté selon l'environnement)
            gateway: '/api',

            // Services spécialisés
            endpoints: {
                // ZScore APIs
                zscore: {
                    calculate: '/calculate-score',
                    questions: '/questions',
                    countries: '/countries',
                    guides: '/guides'
                },

                // SkillGraph APIs
                skillgraph: {
                    analyze: '/analyze-career',
                    profiles: '/career-profiles',
                    matches: '/skill-matches'
                },

                // Payment APIs
                payment: {
                    config: '/stripe-config',
                    session: '/create-payment-session',
                    confirm: '/confirm-payment',
                    webhook: '/stripe-webhook'
                },

                // User APIs
                user: {
                    profile: '/user-profile',
                    session: '/user-session',
                    preferences: '/user-preferences',
                    history: '/user-history'
                }
            }
        };

        // 🎯 Request configurations
        this.requestConfig = {
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'X-Client': 'ZineInsight-SPA-Revolutionary'
            },
            timeout: 30000
        };

        // 🎯 Cache système
        this.cache = new Map();
        this.cacheTimeout = 5 * 60 * 1000; // 5 minutes

        console.log('🔗 API Connector initialized - waiting for environment config...');

        // Écouter la configuration d'environnement
        this.initializeWhenReady();
    }

    /**
     * 🎯 INITIALISATION ADAPTÉE À L'ENVIRONNEMENT
     */
    async initializeWhenReady() {
        // Si la config environnement existe déjà
        if (window.environmentConfig) {
            this.configureFromEnvironment(window.environmentConfig);
            return;
        }

        // Sinon, attendre l'événement
        window.addEventListener('environmentConfigured', (event) => {
            this.configureFromEnvironment(event.detail);
        });
    }

    configureFromEnvironment(environmentConfig) {
        this.environmentConfig = environmentConfig;

        // Adapter la configuration selon l'environnement
        this.config.gateway = environmentConfig.getApiUrl('');
        this.requestConfig.timeout = environmentConfig.getTimeout();

        // Adapter le cache selon l'environnement
        if (!environmentConfig.shouldUseCache()) {
            this.cacheTimeout = 0; // Désactiver le cache en dev
        }

        this.isConfigured = true;
        console.log(`✅ API Connector configured for ${environmentConfig.environment}`);
        console.log(`🌐 API Base URL: ${this.config.gateway}`);
    }

    /**
     * 🎯 CONSTRUCTION D'URL ADAPTÉE
     */
    buildURL(endpoint) {
        // Attendre que la configuration soit prête
        if (!this.isConfigured && window.environmentConfig) {
            this.configureFromEnvironment(window.environmentConfig);
        }

        // Si l'endpoint commence par '/', c'est relatif au gateway
        if (endpoint.startsWith('/')) {
            // Enlever le '/' final du gateway s'il existe
            const baseUrl = this.config.gateway.endsWith('/')
                ? this.config.gateway.slice(0, -1)
                : this.config.gateway;
            return `${baseUrl}${endpoint}`;
        }

        // Sinon, c'est une URL complète
        return endpoint;
    }

    /**
     * 🎯 MÉTHODE GÉNÉRIQUE POUR TOUS LES APPELS API
     */
    async request(endpoint, method = 'GET', data = null, options = {}) {
        try {
            const url = this.buildURL(endpoint);
            const cacheKey = `${method}:${url}:${JSON.stringify(data)}`;

            // Vérification cache pour GET requests
            if (method === 'GET' && this.cache.has(cacheKey)) {
                const cached = this.cache.get(cacheKey);
                if (Date.now() - cached.timestamp < this.cacheTimeout) {
                    console.log('📦 Cache hit:', endpoint);
                    return cached.data;
                }
            }

            const config = {
                method,
                ...this.requestConfig,
                ...options
            };

            if (data && ['POST', 'PUT', 'PATCH'].includes(method)) {
                config.body = JSON.stringify(data);
            }

            console.log(`🚀 API Request: ${method} ${url}`);
            const response = await fetch(url, config);

            if (!response.ok) {
                throw new Error(`API Error: ${response.status} ${response.statusText}`);
            }

            const result = await response.json();

            // Cache pour GET requests réussis
            if (method === 'GET') {
                this.cache.set(cacheKey, {
                    data: result,
                    timestamp: Date.now()
                });
            }

            console.log('✅ API Success:', endpoint);
            return result;

        } catch (error) {
            console.error(`❌ API Error [${endpoint}]:`, error);
            throw error;
        }
    }

    /**
     * 🎯 ZSCORE METHODS
     */
    async calculateZScore(answers, country = null) {
        const payload = {
            answers,
            selectedCountry: country,
            timestamp: new Date().toISOString()
        };

        return this.request(this.config.endpoints.zscore.calculate, 'POST', payload);
    }

    async getQuestions() {
        return this.request(this.config.endpoints.zscore.questions);
    }

    async getCountries() {
        return this.request(this.config.endpoints.zscore.countries);
    }

    async getGuideData(country) {
        return this.request(`${this.config.endpoints.zscore.guides}/${country}`);
    }

    /**
     * 🧠 SKILLGRAPH METHODS
     */
    async analyzeCareer(questionnaire, country = 'france') {
        const payload = {
            questionnaire,
            country,
            timestamp: new Date().toISOString()
        };

        return this.request(this.config.endpoints.skillgraph.analyze, 'POST', payload);
    }

    async getCareerProfiles() {
        return this.request(this.config.endpoints.skillgraph.profiles);
    }

    async getSkillMatches(skills) {
        const payload = { skills };
        return this.request(this.config.endpoints.skillgraph.matches, 'POST', payload);
    }

    /**
     * 💳 PAYMENT METHODS
     */
    async createPaymentSession(tier, productData = null) {
        const payload = {
            tier,
            productData,
            timestamp: new Date().toISOString(),
            clientInfo: {
                userAgent: navigator.userAgent,
                language: navigator.language,
                timezone: Intl.DateTimeFormat().resolvedOptions().timeZone
            }
        };

        return this.request(this.config.endpoints.payment.createSession, 'POST', payload);
    }

    async verifyPayment(sessionId) {
        const payload = { session_id: sessionId };
        return this.request(this.config.endpoints.payment.verify, 'POST', payload);
    }

    /**
     * 👤 USER METHODS
     */
    async getUserSession() {
        return this.request(this.config.endpoints.user.session);
    }

    async updateUserPreferences(preferences) {
        const payload = { preferences };
        return this.request(this.config.endpoints.user.preferences, 'PUT', payload);
    }

    async getUserHistory() {
        return this.request(this.config.endpoints.user.history);
    }

    /**
     * 🛠️ UTILITY METHODS
     */
    clearCache() {
        this.cache.clear();
        console.log('🗑️ API Cache cleared');
    }

    getCacheStats() {
        return {
            size: this.cache.size,
            entries: Array.from(this.cache.keys())
        };
    }

    /**
     * 🎯 BATCH REQUESTS - Pour optimiser les performances
     */
    async batchRequest(requests) {
        console.log('📦 Batch request:', requests.length, 'calls');

        const promises = requests.map(req =>
            this.request(req.endpoint, req.method || 'GET', req.data || null)
                .catch(error => ({ error: error.message, endpoint: req.endpoint }))
        );

        const results = await Promise.all(promises);

        console.log('✅ Batch completed');
        return results;
    }

    /**
     * 📊 MONITORING & ANALYTICS
     */
    trackAPICall(endpoint, method, duration, success) {
        // Log pour monitoring
        console.log(`📊 API Call: ${method} ${endpoint} - ${duration}ms - ${success ? 'SUCCESS' : 'FAILED'}`);

        // Ici tu pourrais envoyer à ton système de monitoring
        if (window.gtag) {
            window.gtag('event', 'api_call', {
                endpoint,
                method,
                duration,
                success
            });
        }
    }

    /**
     * 🔄 RETRY MECHANISM
     */
    async requestWithRetry(endpoint, method = 'GET', data = null, maxRetries = 3) {
        for (let attempt = 1; attempt <= maxRetries; attempt++) {
            try {
                return await this.request(endpoint, method, data);
            } catch (error) {
                console.warn(`⚠️ API attempt ${attempt}/${maxRetries} failed:`, error.message);

                if (attempt === maxRetries) {
                    throw error;
                }

                // Délai exponentiel entre les tentatives
                await new Promise(resolve => setTimeout(resolve, Math.pow(2, attempt) * 1000));
            }
        }
    }
}

/**
 * 🌟 GLOBAL API INSTANCE
 */
window.ZineInsightAPI = new ZineInsightAPIConnector();

// Export pour modules ES6
export default ZineInsightAPIConnector;

console.log('🔗 API Connector loaded and ready!');
