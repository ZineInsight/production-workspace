/**
 * 🍪 ZINEINSIGHT GLOBAL COOKIES MANAGEMENT SYSTEM
 * Système de gestion des cookies RGPD unifié pour tout le site ZineInsight
 * Version: 2.0 - Global Implementation
 */

class ZineInsightCookies {
    constructor() {
        this.config = {
            essential: true,    // Toujours true - requis pour le fonctionnement
            preferences: false, // Préférences utilisateur (langue, thème)
            analytics: false    // Analytics et améliorations
        };
        
        this.bannerShown = false;
        this.init();
    }

    init() {
        // Injecter le HTML des cookies dans le DOM
        this.injectCookiesHTML();
        
        // Vérifier le consentement existant
        this.checkCookiesConsent();
        
        // Setup des événements
        this.setupEventListeners();
        
        console.log('🍪 ZineInsight Global Cookies System - Initialized');
    }

    injectCookiesHTML() {
        // Créer le HTML du banner de cookies avec data-i18n
        const cookiesBanner = `
            <div class="cookies-banner" id="cookiesBanner">
                <div class="cookies-content">
                    <div class="cookies-info">
                        <div class="cookies-icon">🍪</div>
                        <div class="cookies-text">
                            <h3 data-i18n="cookies.title">Nous respectons votre vie privée</h3>
                            <p data-i18n="cookies.description">
                                Nous utilisons des cookies essentiels pour sauvegarder vos préférences (langue, thème) et
                                améliorer votre expérience. Aucun tracking publicitaire.
                            </p>
                        </div>
                    </div>
                    <div class="cookies-actions">
                        <button class="btn btn-ghost btn-sm" onclick="window.zineInsightCookies.rejectCookies()" data-i18n="cookies.refuse">
                            Refuser
                        </button>
                        <button class="btn btn-secondary btn-sm" onclick="window.zineInsightCookies.customizeCookies()" data-i18n="cookies.customize">
                            Personnaliser
                        </button>
                        <button class="btn btn-primary btn-sm" onclick="window.zineInsightCookies.acceptCookies()" data-i18n="cookies.accept">
                            Accepter tout
                        </button>
                    </div>
                </div>
            </div>
        `;

        // Créer le HTML du modal de personnalisation avec data-i18n
        const cookiesModal = `
            <div class="cookies-modal-overlay" id="cookiesModalOverlay">
                <div class="cookies-modal">
                    <div class="modal-header">
                        <h2 data-i18n="cookies.settings_title">Paramètres des cookies</h2>
                        <button class="modal-close" onclick="window.zineInsightCookies.closeCookiesModal()">
                            ✕
                        </button>
                    </div>
                    <div class="modal-content">
                        <div class="cookie-category">
                            <div class="category-header">
                                <div class="category-info">
                                    <h3 data-i18n="cookies.essential">Cookies essentiels</h3>
                                    <p data-i18n="cookies.essential_desc">Nécessaires au fonctionnement du site (langue, sécurité)</p>
                                </div>
                                <div class="toggle-switch">
                                    <input type="checkbox" id="essential" checked disabled>
                                    <label for="essential"></label>
                                </div>
                            </div>
                        </div>
                        <div class="cookie-category">
                            <div class="category-header">
                                <div class="category-info">
                                    <h3 data-i18n="cookies.preferences">Cookies de préférences</h3>
                                    <p data-i18n="cookies.preferences_desc">Sauvegarde vos choix (langue, thème, paramètres)</p>
                                </div>
                                <div class="toggle-switch">
                                    <input type="checkbox" id="preferences" checked>
                                    <label for="preferences"></label>
                                </div>
                            </div>
                        </div>
                        <div class="cookie-category">
                            <div class="category-header">
                                <div class="category-info">
                                    <h3 data-i18n="cookies.analytics">Cookies analytiques</h3>
                                    <p data-i18n="cookies.analytics_desc">Nous aident à améliorer le site (anonymisés)</p>
                                </div>
                                <div class="toggle-switch">
                                    <input type="checkbox" id="analytics">
                                    <label for="analytics"></label>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button class="btn btn-ghost" onclick="window.zineInsightCookies.closeCookiesModal()" data-i18n="cookies.cancel">
                            Annuler
                        </button>
                        <button class="btn btn-primary" onclick="window.zineInsightCookies.saveCookiesPreferences()" data-i18n="cookies.save">
                            Sauvegarder
                        </button>
                    </div>
                </div>
            </div>
        `;

        // Injecter dans le DOM
        document.body.insertAdjacentHTML('beforeend', cookiesBanner);
        document.body.insertAdjacentHTML('beforeend', cookiesModal);
        
        // Appliquer les traductions après injection
        setTimeout(() => {
            this.updateTranslations();
        }, 100);
    }

    updateTranslations() {
        // Appliquer les traductions si le système i18n est disponible
        if (window.portfolioI18n && typeof window.portfolioI18n.applyTranslations === 'function') {
            console.log('🌍 Applying cookies translations...');
            window.portfolioI18n.applyTranslations();
        } else {
            console.log('⚠️ Portfolio i18n not available for cookies translation');
        }
    }

    checkCookiesConsent() {
        const consent = localStorage.getItem('cookies-consent');
        const consentData = consent ? JSON.parse(consent) : null;

        if (!consentData || !consentData.timestamp ||
            (Date.now() - consentData.timestamp) > (365 * 24 * 60 * 60 * 1000)) {
            // Afficher le banner si pas de consentement ou expiré (1 an)
            this.showCookiesBanner();
        } else {
            // Appliquer les préférences sauvegardées
            Object.assign(this.config, consentData.preferences);
            this.applyCookiesSettings();
        }
    }

    showCookiesBanner() {
        const banner = document.getElementById('cookiesBanner');
        if (banner) {
            banner.style.display = 'block';
            setTimeout(() => banner.classList.add('show'), 100);
            this.bannerShown = true;
        }
    }

    hideCookiesBanner() {
        const banner = document.getElementById('cookiesBanner');
        if (banner) {
            banner.classList.remove('show');
            setTimeout(() => banner.style.display = 'none', 300);
            this.bannerShown = false;
        }
    }

    acceptCookies() {
        this.config.essential = true;
        this.config.preferences = true;
        this.config.analytics = true;

        this.saveCookiesConsent();
        this.applyCookiesSettings();
        this.hideCookiesBanner();

        this.showToast(this.getTranslation('cookies.accepted_toast'), 'success');
    }

    rejectCookies() {
        this.config.essential = true;
        this.config.preferences = false;
        this.config.analytics = false;

        this.saveCookiesConsent();
        this.applyCookiesSettings();
        this.hideCookiesBanner();

        this.showToast(this.getTranslation('cookies.rejected_toast'), 'info');
    }

    customizeCookies() {
        // Mettre à jour les checkboxes du modal
        const essential = document.getElementById('essential');
        const preferences = document.getElementById('preferences');
        const analytics = document.getElementById('analytics');
        
        if (essential) essential.checked = this.config.essential;
        if (preferences) preferences.checked = this.config.preferences;
        if (analytics) analytics.checked = this.config.analytics;

        // Afficher le modal
        const overlay = document.getElementById('cookiesModalOverlay');
        if (overlay) {
            overlay.style.display = 'flex';
            setTimeout(() => overlay.classList.add('active'), 10);
        }
    }

    closeCookiesModal() {
        const overlay = document.getElementById('cookiesModalOverlay');
        if (overlay) {
            overlay.classList.remove('active');
            setTimeout(() => overlay.style.display = 'none', 300);
        }
    }

    saveCookiesPreferences() {
        // Récupérer les valeurs des checkboxes
        const essential = document.getElementById('essential');
        const preferences = document.getElementById('preferences');
        const analytics = document.getElementById('analytics');
        
        if (essential) this.config.essential = essential.checked;
        if (preferences) this.config.preferences = preferences.checked;
        if (analytics) this.config.analytics = analytics.checked;

        this.saveCookiesConsent();
        this.applyCookiesSettings();
        this.closeCookiesModal();
        this.hideCookiesBanner();

        this.showToast(this.getTranslation('cookies.saved_toast'), 'success');
    }

    saveCookiesConsent() {
        const consentData = {
            timestamp: Date.now(),
            preferences: { ...this.config },
            version: '2.0'
        };

        if (this.config.preferences) {
            localStorage.setItem('cookies-consent', JSON.stringify(consentData));
        } else {
            // Utiliser sessionStorage pour essential-only
            sessionStorage.setItem('cookies-consent-session', JSON.stringify(consentData));
            localStorage.removeItem('cookies-consent');
            localStorage.removeItem('preferred-language');
        }
    }

    applyCookiesSettings() {
        // Appliquer les cookies de préférences
        if (!this.config.preferences) {
            // Nettoyer le stockage lié aux préférences
            localStorage.removeItem('preferred-language');
            // Remettre à la langue par défaut si nécessaire
            if (typeof setLanguage === 'function') {
                setLanguage('fr');
            }
        }

        // Appliquer les cookies analytiques
        if (this.config.analytics) {
            console.log('📊 Analytics cookies enabled');
            // Ici vous pouvez initialiser Google Analytics, etc.
        } else {
            console.log('🚫 Analytics cookies disabled');
        }

        // Afficher le statut actuel dans la console
        console.log('🍪 Cookies Status:', this.config);
    }

    setupEventListeners() {
        // Fermer le modal en cliquant sur l'overlay
        document.addEventListener('click', (e) => {
            if (e.target.id === 'cookiesModalOverlay') {
                this.closeCookiesModal();
            }
        });

        // Fermer le modal avec la touche Escape
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                this.closeCookiesModal();
            }
        });

        // Écouter les changements de langue pour mettre à jour les traductions
        document.addEventListener('languageChanged', () => {
            console.log('🌍 Language changed - updating cookies translations');
            setTimeout(() => {
                this.updateTranslations();
            }, 100);
        });
    }

    showToast(message, type = 'info') {
        // Créer l'élément toast
        const toast = document.createElement('div');
        toast.className = `toast toast-${type}`;
        toast.innerHTML = `
            <div class="toast-content">
                <span class="toast-icon">${type === 'success' ? '✅' : '💡'}</span>
                <span class="toast-message">${message}</span>
            </div>
        `;

        // Ajouter au DOM
        document.body.appendChild(toast);

        // Afficher avec animation
        setTimeout(() => toast.classList.add('show'), 10);

        // Supprimer automatiquement
        setTimeout(() => {
            toast.classList.remove('show');
            setTimeout(() => document.body.removeChild(toast), 300);
        }, 3000);
    }

    // Méthode publique pour vérifier le consentement
    hasConsent(type = 'preferences') {
        return this.config[type] || false;
    }

    // Méthode publique pour obtenir la configuration actuelle
    getConfig() {
        return { ...this.config };
    }

    // Méthode pour obtenir les traductions depuis le système i18n
    getTranslation(key) {
        if (window.portfolioI18n && typeof window.portfolioI18n.getTranslation === 'function') {
            return window.portfolioI18n.getTranslation(key) || key;
        }
        // Fallback en français si le système i18n n'est pas disponible
        const fallbackTranslations = {
            'cookies.accepted_toast': 'Cookies acceptés ! Merci de nous faire confiance 🍪✨',
            'cookies.rejected_toast': 'Seuls les cookies essentiels sont activés 🛡️',
            'cookies.saved_toast': 'Préférences sauvegardées ! 🎯'
        };
        return fallbackTranslations[key] || key;
    }

    // Méthode pour mettre à jour les traductions après changement de langue
    updateTranslations() {
        if (window.portfolioI18n && typeof window.portfolioI18n.applyTranslations === 'function') {
            window.portfolioI18n.applyTranslations();
        }
    }
}

// Initialisation automatique quand le DOM est prêt
function initZineInsightCookies() {
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => {
            window.zineInsightCookies = new ZineInsightCookies();
        });
    } else {
        window.zineInsightCookies = new ZineInsightCookies();
    }
}

// Auto-initialisation
initZineInsightCookies();

// Export pour usage module (si nécessaire)
if (typeof module !== 'undefined' && module.exports) {
    module.exports = ZineInsightCookies;
}
