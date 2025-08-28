/**
 * 🚀 ZineInsight Revolutionary - Core JavaScript
 * ============================================================================
 * Système central pour orchestrer tous les composants
 * ============================================================================
 */

class ZineInsightCore {
    constructor() {
        this.version = '1.0.0';
        this.initialized = false;
        this.components = new Map();
        this.events = new Map();

        console.log('🚀 ZineInsight Revolutionary Core initializing...');
        this.init();
    }

    /**
     * Initialisation du système central
     */
    async init() {
        try {
            await this.loadComponents();
            await this.setupEventSystem();
            await this.initializeUI();

            this.initialized = true;
            console.log('✅ ZineInsight Revolutionary Core initialized successfully');
            this.emit('core:initialized');

        } catch (error) {
            console.error('❌ Core initialization failed:', error);
        }
    }

    /**
     * Chargement des composants
     */
    async loadComponents() {
        const componentsToLoad = [
            'apiConnector',
            'paymentSystem',
            'dashboardManager',
            'particleSystem',
            'animationEngine'
        ];

        for (const componentName of componentsToLoad) {
            try {
                if (window[componentName]) {
                    this.components.set(componentName, window[componentName]);
                    console.log(`📦 Component loaded: ${componentName}`);
                } else {
                    console.warn(`⚠️ Component not found: ${componentName}`);
                }
            } catch (error) {
                console.error(`❌ Failed to load component ${componentName}:`, error);
            }
        }
    }

    /**
     * Configuration du système d'événements
     */
    setupEventSystem() {
        // Événements globaux de l'application
        this.on('user:login', this.handleUserLogin.bind(this));
        this.on('user:logout', this.handleUserLogout.bind(this));
        this.on('payment:success', this.handlePaymentSuccess.bind(this));
        this.on('dashboard:show', this.handleDashboardShow.bind(this));
        this.on('error:critical', this.handleCriticalError.bind(this));

        console.log('🔗 Event system configured');
    }

    /**
     * Initialisation de l'interface utilisateur
     */
    initializeUI() {
        // Gestion des boutons principaux
        this.setupMainButtons();

        // Gestion du scroll et animations
        this.setupScrollHandlers();

        // Gestion responsive
        this.setupResponsiveHandlers();

        console.log('🎨 UI system initialized');
    }

    /**
     * Configuration des boutons principaux
     */
    setupMainButtons() {
        // Bouton ZScore
        const zscoreBtn = document.querySelector('.zscore-cta');
        if (zscoreBtn) {
            zscoreBtn.addEventListener('click', (e) => {
                e.preventDefault();
                this.emit('zscore:calculate');
            });
        }

        // Bouton Dashboard
        const dashboardBtn = document.querySelector('.dashboard-cta');
        if (dashboardBtn) {
            dashboardBtn.addEventListener('click', (e) => {
                e.preventDefault();
                this.emit('dashboard:show');
            });
        }

        // Boutons Premium
        const premiumBtns = document.querySelectorAll('[data-plan]');
        premiumBtns.forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                const plan = btn.dataset.plan;
                this.emit('payment:start', { plan });
            });
        });
    }

    /**
     * Gestion du scroll et animations
     */
    setupScrollHandlers() {
        let ticking = false;

        window.addEventListener('scroll', () => {
            if (!ticking) {
                requestAnimationFrame(() => {
                    this.handleScroll();
                    ticking = false;
                });
                ticking = true;
            }
        });
    }

    /**
     * Gestion du scroll
     */
    handleScroll() {
        const scrollY = window.scrollY;
        const windowHeight = window.innerHeight;

        // Parallax effects
        const parallaxElements = document.querySelectorAll('.parallax');
        parallaxElements.forEach(element => {
            const speed = element.dataset.speed || 0.5;
            element.style.transform = `translateY(${scrollY * speed}px)`;
        });

        // Animation on scroll
        const animateElements = document.querySelectorAll('.animate-on-scroll');
        animateElements.forEach(element => {
            const elementTop = element.offsetTop;
            const elementHeight = element.offsetHeight;

            if (scrollY + windowHeight > elementTop + elementHeight * 0.1) {
                element.classList.add('animated');
            }
        });
    }

    /**
     * Gestion responsive
     */
    setupResponsiveHandlers() {
        const mediaQuery = window.matchMedia('(max-width: 768px)');

        const handleMediaQuery = (e) => {
            if (e.matches) {
                this.emit('ui:mobile');
                document.body.classList.add('mobile-view');
            } else {
                this.emit('ui:desktop');
                document.body.classList.remove('mobile-view');
            }
        };

        mediaQuery.addListener(handleMediaQuery);
        handleMediaQuery(mediaQuery);
    }

    /**
     * Gestionnaires d'événements
     */
    handleUserLogin(data) {
        console.log('👤 User logged in:', data);
        document.body.classList.add('user-logged-in');

        // Charger les données utilisateur
        if (this.components.has('apiConnector')) {
            this.components.get('apiConnector').loadUserData(data.userId);
        }
    }

    handleUserLogout() {
        console.log('👤 User logged out');
        document.body.classList.remove('user-logged-in');

        // Nettoyer les données
        this.clearUserData();
    }

    handlePaymentSuccess(data) {
        console.log('💳 Payment successful:', data);

        // Activer les fonctionnalités premium
        document.body.classList.add('premium-user');

        // Afficher le dashboard
        this.emit('dashboard:show');

        // Notification de succès
        this.showNotification('🎉 Paiement réussi ! Bienvenue dans Premium !', 'success');
    }

    handleDashboardShow() {
        console.log('📊 Showing dashboard');

        if (this.components.has('dashboardManager')) {
            this.components.get('dashboardManager').show();
        }
    }

    handleCriticalError(error) {
        console.error('🚨 Critical error:', error);
        this.showNotification('❌ Une erreur critique est survenue', 'error');
    }

    /**
     * Système d'événements
     */
    on(event, callback) {
        if (!this.events.has(event)) {
            this.events.set(event, []);
        }
        this.events.get(event).push(callback);
    }

    emit(event, data = null) {
        if (this.events.has(event)) {
            this.events.get(event).forEach(callback => {
                try {
                    callback(data);
                } catch (error) {
                    console.error(`Error in event handler for ${event}:`, error);
                }
            });
        }
    }

    off(event, callback) {
        if (this.events.has(event)) {
            const callbacks = this.events.get(event);
            const index = callbacks.indexOf(callback);
            if (index > -1) {
                callbacks.splice(index, 1);
            }
        }
    }

    /**
     * Utilitaires
     */
    showNotification(message, type = 'info') {
        // Créer une notification toast
        const notification = document.createElement('div');
        notification.className = `notification notification-${type}`;
        notification.innerHTML = `
            <div class="notification-content">
                <span class="notification-message">${message}</span>
                <button class="notification-close">&times;</button>
            </div>
        `;

        // Ajouter au DOM
        document.body.appendChild(notification);

        // Animation d'entrée
        setTimeout(() => {
            notification.classList.add('show');
        }, 100);

        // Auto-suppression
        setTimeout(() => {
            notification.classList.remove('show');
            setTimeout(() => {
                if (notification.parentNode) {
                    notification.parentNode.removeChild(notification);
                }
            }, 300);
        }, 5000);

        // Bouton fermer
        const closeBtn = notification.querySelector('.notification-close');
        closeBtn.addEventListener('click', () => {
            notification.classList.remove('show');
            setTimeout(() => {
                if (notification.parentNode) {
                    notification.parentNode.removeChild(notification);
                }
            }, 300);
        });
    }

    clearUserData() {
        // Nettoyer le localStorage
        const keysToRemove = ['userSession', 'userPreferences', 'dashboardData'];
        keysToRemove.forEach(key => {
            localStorage.removeItem(key);
        });

        // Réinitialiser les composants
        this.components.forEach((component, name) => {
            if (typeof component.reset === 'function') {
                component.reset();
            }
        });
    }

    /**
     * API publique
     */
    getComponent(name) {
        return this.components.get(name);
    }

    isInitialized() {
        return this.initialized;
    }

    getVersion() {
        return this.version;
    }

    /**
     * Debug et monitoring
     */
    getDebugInfo() {
        return {
            version: this.version,
            initialized: this.initialized,
            components: Array.from(this.components.keys()),
            events: Array.from(this.events.keys()),
            userAgent: navigator.userAgent,
            timestamp: new Date().toISOString()
        };
    }
}

// Initialisation globale
window.ZineInsightCore = ZineInsightCore;

// Auto-initialisation au chargement du DOM
document.addEventListener('DOMContentLoaded', () => {
    if (!window.zineCore) {
        window.zineCore = new ZineInsightCore();
    }
});

// Export pour les modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = ZineInsightCore;
}
