/**
 * 🌐 ZINEINSIGHT API CLIENT - Dashboard Analytics
 * ==============================================
 * Client API pour connecter le dashboard aux données dynamiques
 */

class ZineInsightAPI {
    constructor() {
        this.baseUrl = 'http://localhost:8000/api';
        this.authToken = this.getAuthToken();
    }

    /**
     * 🔐 Récupérer le token d'authentification depuis localStorage
     */
    getAuthToken() {
        return localStorage.getItem('auth_token') || localStorage.getItem('zineinsight_token');
    }

    /**
     * 🔧 Headers par défaut avec authentification
     */
    getHeaders() {
        const headers = {
            'Content-Type': 'application/json'
        };

        if (this.authToken) {
            headers['Authorization'] = `Bearer ${this.authToken}`;
        }

        return headers;
    }

    /**
     * 🌐 Requête générique avec gestion d'erreurs
     */
    async request(endpoint, options = {}) {
        try {
            const url = endpoint.startsWith('http') ? endpoint : `${this.baseUrl}${endpoint}`;

            const response = await fetch(url, {
                ...options,
                headers: {
                    ...this.getHeaders(),
                    ...(options.headers || {})
                }
            });

            if (!response.ok) {
                throw new Error(`HTTP ${response.status}: ${response.statusText}`);
            }

            return await response.json();
        } catch (error) {
            console.error('🔥 ZineInsight API Error:', error);
            throw error;
        }
    }

    /**
     * 👤 Récupérer la session utilisateur actuelle
     */
    async getUserSession() {
        try {
            const response = await this.request('/auth/me');
            return response.user || null;
        } catch (error) {
            console.warn('👤 User session not available:', error.message);
            return null;
        }
    }

    /**
     * 📊 Récupérer les analytics utilisateur pour le dashboard
     */
    async getUserAnalytics() {
        try {
            const response = await this.request('/auth/user-analytics');
            return response;
        } catch (error) {
            console.warn('📊 Analytics not available:', error.message);
            return null;
        }
    }

    /**
     * 🎯 Récupérer les résultats d'un service spécifique
     */
    async getUserResults(service) {
        if (!['zscore', 'skillgraph', 'wealth'].includes(service)) {
            throw new Error('Service must be zscore, skillgraph, or wealth');
        }

        try {
            const response = await this.request(`/auth/user-results/${service}`);
            return response;
        } catch (error) {
            console.warn(`🎯 ${service} results not available:`, error.message);
            return null;
        }
    }

    /**
     * 💾 Sauvegarder une analyse dans l'historique
     */
    async saveAnalysis(service, results, score, questionnaire = {}) {
        try {
            const data = {
                service,
                results,
                score,
                questionnaire
            };

            const response = await this.request('/auth/save-analysis', {
                method: 'POST',
                body: JSON.stringify(data)
            });

            return response;
        } catch (error) {
            console.warn('💾 Could not save analysis:', error.message);
            return null;
        }
    }

    /**
     * 🏙️ Lancer une analyse ZScore
     */
    async runZScoreAnalysis(questionnaire, preferences = {}) {
        try {
            const data = {
                questionnaire,
                preferences,
                country: questionnaire.country || 'world'
            };

            const response = await this.request('/calculate', {
                method: 'POST',
                body: JSON.stringify(data)
            });

            return response;
        } catch (error) {
            console.error('🏙️ ZScore analysis failed:', error);
            throw error;
        }
    }

    /**
     * 💼 Lancer une analyse SkillGraph
     */
    async runSkillGraphAnalysis(questionnaire) {
        try {
            const response = await this.request('/career', {
                method: 'POST',
                body: JSON.stringify(questionnaire)
            });

            return response;
        } catch (error) {
            console.error('💼 SkillGraph analysis failed:', error);
            throw error;
        }
    }

    /**
     * 💰 Lancer une analyse Wealth
     */
    async runWealthAnalysis(questionnaire) {
        try {
            const response = await this.request('/wealth', {
                method: 'POST',
                body: JSON.stringify(questionnaire)
            });

            return response;
        } catch (error) {
            console.error('💰 Wealth analysis failed:', error);
            throw error;
        }
    }

    /**
     * 🔐 Connexion utilisateur
     */
    async login(email, password) {
        try {
            const response = await this.request('/auth/login', {
                method: 'POST',
                body: JSON.stringify({ email, password })
            });

            if (response.success && response.token) {
                this.authToken = response.token;
                localStorage.setItem('zineinsight_token', response.token);
            }

            return response;
        } catch (error) {
            console.error('🔐 Login failed:', error);
            throw error;
        }
    }

    /**
     * 📝 Inscription utilisateur
     */
    async register(email, password, name) {
        try {
            const response = await this.request('/auth/register', {
                method: 'POST',
                body: JSON.stringify({ email, password, name })
            });

            return response;
        } catch (error) {
            console.error('📝 Registration failed:', error);
            throw error;
        }
    }

    /**
     * 🚪 Déconnexion
     */
    async logout() {
        try {
            await this.request('/auth/logout', {
                method: 'POST',
                body: JSON.stringify({ session_id: this.authToken })
            });

            this.authToken = null;
            localStorage.removeItem('zineinsight_token');
            localStorage.removeItem('auth_token');

            return { success: true };
        } catch (error) {
            console.warn('🚪 Logout error:', error);
            // Clear tokens anyway
            this.authToken = null;
            localStorage.removeItem('zineinsight_token');
            localStorage.removeItem('auth_token');
            return { success: true };
        }
    }

    /**
     * 🔍 Vérifier si l'utilisateur est connecté
     */
    isAuthenticated() {
        return !!this.authToken;
    }

    /**
     * 💳 Vérifier les limites d'usage
     */
    async checkUsage(service) {
        try {
            const response = await this.request('/auth/check-usage', {
                method: 'POST',
                body: JSON.stringify({ service })
            });

            return response;
        } catch (error) {
            console.warn('💳 Usage check failed:', error);
            return null;
        }
    }
}

// 🌐 Instance globale
window.ZineInsightAPI = new ZineInsightAPI();

// 📊 Auto-chargement si DOM ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        console.log('🌐 ZineInsight API Client ready');
    });
} else {
    console.log('🌐 ZineInsight API Client ready');
}
