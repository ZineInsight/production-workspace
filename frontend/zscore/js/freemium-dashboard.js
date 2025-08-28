/**
 * 💰 FREEMIUM DASHBOARD MANAGER
 * ============================
 * Système de paywalls intelligents pour le dashboard freemium
 * Gère l'affichage, les limitations et les conversions premium
 */

class FreemiumDashboard {
    constructor() {
        this.userLimitations = null;
        this.paywallModals = new Map();
        this.userTier = 'free';

        // Types de paywalls disponibles
        this.paywallTypes = {
            GUIDE_UNLOCK: 'guide_unlock',
            COUNTRY_ACCESS: 'country_access',
            UNLIMITED_ANALYSES: 'unlimited',
            PREMIUM_INSIGHTS: 'premium_insights',
            EXPORT_PDF: 'export_pdf'
        };

        console.log('💰 Freemium Dashboard Manager initialized');
        this.init();
    }

    /**
     * 🚀 INITIALISATION DU DASHBOARD
     */
    async init() {
        // Vérifier les retours de paiement dans l'URL
        this.handlePaymentReturn();

        // Charger les limitations utilisateur
        await this.loadUserLimitations();
    }

    /**
     * 💳 GÉRER LES RETOURS DE PAIEMENT
     */
    handlePaymentReturn() {
        const urlParams = new URLSearchParams(window.location.search);
        const paymentStatus = urlParams.get('payment');
        const sessionId = urlParams.get('session_id');

        if (paymentStatus === 'success' && sessionId) {
            console.log('🎉 Payment successful!', sessionId);

            // 📊 Google Analytics - Payment Success
            if (typeof window.trackDashboardEvent === 'function') {
                window.trackDashboardEvent('payment_success', 'Conversion', sessionId, 1);
            }

            this.showSuccessNotification('Paiement réussi ! Votre accès premium est maintenant activé.');

            // Nettoyer l'URL
            window.history.replaceState({}, document.title, window.location.pathname);

        } else if (paymentStatus === 'cancelled') {
            console.log('❌ Payment cancelled');

            // 📊 Google Analytics - Payment Cancelled
            if (typeof window.trackDashboardEvent === 'function') {
                window.trackDashboardEvent('payment_cancelled', 'Conversion', 'user_cancelled', 0);
            }

            this.showErrorNotification('Paiement annulé. Vous pouvez réessayer à tout moment.');

            // Nettoyer l'URL
            window.history.replaceState({}, document.title, window.location.pathname);
        }
    }

    /**
     * 📊 CHARGER LES LIMITATIONS UTILISATEUR
     */
    async loadUserLimitations() {
        try {
            const response = await window.ZineInsightAPI.request('/auth/dashboard/limitations');

            if (response.success) {
                this.userLimitations = response.limitations;
                this.userTier = response.user_tier;

                console.log('✅ User limitations loaded:', this.userLimitations);

                // Appliquer les limitations à l'interface
                this.applyDashboardLimitations();

                // Afficher les CTAs si nécessaire
                if (this.userLimitations.show_upgrade_cta) {
                    this.showUpgradeCTA();
                }

            } else {
                console.warn('⚠️ Could not load user limitations');
            }

        } catch (error) {
            console.error('❌ Failed to load user limitations:', error);
        }
    }

    /**
     * 🎯 APPLIQUER LES LIMITATIONS DASHBOARD
     */
    applyDashboardLimitations() {
        if (!this.userLimitations) return;

        // Limiter les analyses restantes
        this.updateAnalysesCounter();

        // Masquer/afficher les pays selon l'accès
        this.applyCountryLimitations();

        // Ajouter des overlays paywall sur le contenu premium
        this.addPaywallOverlays();

        // Personnaliser l'interface selon le tier
        this.customizeUIForTier();
    }

    /**
     * 🔢 METTRE À JOUR LE COMPTEUR D'ANALYSES
     */
    updateAnalysesCounter() {
        const analysesRemaining = this.userLimitations.analyses_remaining;

        // 📊 Google Analytics - User Tier Status
        if (typeof window.trackDashboardEvent === 'function') {
            window.trackDashboardEvent('dashboard_load', 'User Status', `Analyses: ${analysesRemaining}`, analysesRemaining);
        }

        // Trouver les éléments d'analyses dans le dashboard
        const analysisButtons = document.querySelectorAll('[data-action="run-analysis"]');

        analysisButtons.forEach(button => {
            if (analysesRemaining === 0) {
                button.disabled = true;
                button.innerHTML = '🔒 Upgrade pour plus d\'analyses';
                button.onclick = () => {
                    // 📊 Google Analytics - Analysis Limit Hit
                    if (typeof window.trackPaywallEvent === 'function') {
                        window.trackPaywallEvent('unlimited_analyses', 'limit_reached', 'analysis_button');
                    }
                    this.showPaywall(this.paywallTypes.UNLIMITED_ANALYSES);
                };
            } else if (analysesRemaining > 0) {
                button.innerHTML = `🎯 Analyser (${analysesRemaining} restantes)`;
            } else {
                button.innerHTML = '🎯 Analyser (Illimité)';
            }
        });
    }

    /**
     * 🌍 APPLIQUER LIMITATIONS PAYS
     */
    applyCountryLimitations() {
        const accessibleCountries = this.userLimitations.countries_accessible;

        if (accessibleCountries === "all") return; // Accès complet

        // Trouver les sélecteurs de pays
        const countryOptions = document.querySelectorAll('[data-country]');

        countryOptions.forEach(option => {
            const countryCode = option.dataset.country;

            if (!accessibleCountries.includes(countryCode)) {
                // Ajouter un overlay paywall
                option.classList.add('locked-country');
                option.onclick = (e) => {
                    e.preventDefault();
                    this.showPaywall(this.paywallTypes.COUNTRY_ACCESS, countryCode);
                };

                // Ajouter l'icône lock
                if (!option.querySelector('.lock-icon')) {
                    const lockIcon = document.createElement('div');
                    lockIcon.className = 'lock-icon';
                    lockIcon.innerHTML = '🔒';
                    option.appendChild(lockIcon);
                }
            }
        });
    }

    /**
     * 🎭 AJOUTER OVERLAYS PAYWALL
     */
    addPaywallOverlays() {
        // Guides premium
        const guideElements = document.querySelectorAll('[data-guide-id]');
        guideElements.forEach(guide => {
            const guideId = guide.dataset.guideId;
            const hasAccess = this.checkGuideAccess(guideId);

            if (!hasAccess) {
                this.addPaywallOverlay(guide, this.paywallTypes.GUIDE_UNLOCK, guideId);
            }
        });

        // Insights IA
        const insightElements = document.querySelectorAll('[data-insight="premium"]');
        if (!this.userLimitations.insights_ai) {
            insightElements.forEach(insight => {
                this.addPaywallOverlay(insight, this.paywallTypes.PREMIUM_INSIGHTS);
            });
        }

        // Export PDF
        const exportButtons = document.querySelectorAll('[data-action="export-pdf"]');
        if (this.userLimitations.pdf_exports === 0) {
            exportButtons.forEach(button => {
                button.onclick = (e) => {
                    e.preventDefault();
                    this.showPaywall(this.paywallTypes.EXPORT_PDF);
                };
                button.innerHTML = '📄 Export PDF (2.99€)';
            });
        }
    }

    /**
     * 🎨 PERSONNALISER L'UI SELON LE TIER
     */
    customizeUIForTier() {
        const tierBadge = document.querySelector('.user-tier-badge');
        if (tierBadge) {
            tierBadge.textContent = this.userTier.charAt(0).toUpperCase() + this.userTier.slice(1);
            tierBadge.className = `user-tier-badge tier-${this.userTier}`;
        }

        // Ajouter les badges premium où nécessaire
        const premiumFeatures = document.querySelectorAll('[data-premium="true"]');
        premiumFeatures.forEach(feature => {
            if (this.userTier === 'free') {
                const badge = document.createElement('span');
                badge.className = 'premium-badge';
                badge.textContent = '✨ Premium';
                feature.appendChild(badge);
            }
        });
    }

    /**
     * 🔒 AJOUTER OVERLAY PAYWALL À UN ÉLÉMENT
     */
    addPaywallOverlay(element, paywallType, resourceId = null) {
        // Créer l'overlay
        const overlay = document.createElement('div');
        overlay.className = 'paywall-overlay';
        overlay.innerHTML = `
            <div class="paywall-overlay-content">
                <div class="paywall-icon">🔒</div>
                <div class="paywall-title">Contenu Premium</div>
                <div class="paywall-description">Débloquez ce contenu exclusif</div>
                <button class="paywall-unlock-btn" data-paywall="${paywallType}" data-resource="${resourceId}">
                    ✨ Débloquer
                </button>
            </div>
        `;

        // Positionner l'overlay
        element.style.position = 'relative';
        element.appendChild(overlay);

        // Event listener
        const unlockBtn = overlay.querySelector('.paywall-unlock-btn');
        unlockBtn.onclick = () => this.showPaywall(paywallType, resourceId);
    }

    /**
     * ✅ VÉRIFIER ACCÈS GUIDE
     */
    checkGuideAccess(guideId) {
        if (this.userTier === 'pro') return true;
        if (this.userLimitations.guides_unlocked === 'all') return true;

        const purchasedGuides = this.userLimitations.purchased_guides || [];
        return purchasedGuides.includes(`guide_${guideId}`);
    }

    /**
     * 💰 AFFICHER MODAL PAYWALL
     */
    async showPaywall(paywallType, resourceId = null) {
        try {
            console.log(`💰 Paywall triggered: ${paywallType} for resource: ${resourceId}`);

            // 📊 Google Analytics - Paywall View
            if (typeof window.trackPaywallEvent === 'function') {
                window.trackPaywallEvent(paywallType, 'view', resourceId);
            }

            // Vérifier d'abord l'accès
            const accessCheck = await window.ZineInsightAPI.request('/auth/paywall/check-access', 'POST', {
                paywall_type: paywallType,
                resource_id: resourceId
            });

            if (accessCheck.access_result.has_access) {
                console.log('✅ User already has access');
                return;
            }

            // Créer la session paywall
            const sessionResponse = await window.ZineInsightAPI.request('/auth/paywall/create-session', 'POST', {
                paywall_type: paywallType,
                resource_id: resourceId,
                metadata: {
                    source: 'dashboard',
                    timestamp: new Date().toISOString()
                }
            });

            if (sessionResponse.success) {
                this.displayPaywallModal(sessionResponse.paywall_data, sessionResponse.session_id);
            }

        } catch (error) {
            console.error('❌ Failed to show paywall:', error);
        }
    }

    /**
     * 🎭 AFFICHER MODAL PAYWALL
     */
    displayPaywallModal(paywallData, sessionId) {
        const modalHTML = `
            <div id="paywall-modal-${sessionId}" class="paywall-modal-overlay">
                <div class="paywall-modal-container">
                    <div class="paywall-modal-header">
                        <h2>${paywallData.title}</h2>
                        <button class="close-modal" onclick="window.FreemiumDashboard.closePaywallModal('${sessionId}', '${paywallData.paywall_type}', true)">×</button>
                    </div>

                    <div class="paywall-content">
                        <div class="paywall-description">${paywallData.description}</div>

                        <div class="paywall-price">
                            <span class="price-amount">${(paywallData.price / 100).toFixed(2)}€</span>
                            <span class="price-currency">${paywallData.currency.toUpperCase()}</span>
                        </div>

                        <div class="paywall-features">
                            <h4>✨ Inclus dans cet upgrade :</h4>
                            <ul>
                                ${paywallData.features.map(feature => `<li>✅ ${feature}</li>`).join('')}
                            </ul>
                        </div>

                        <div class="paywall-actions">
                            <button class="btn-paywall-purchase" onclick="window.FreemiumDashboard.processPaywallPayment('${sessionId}', '${paywallData.paywall_type}')">
                                💳 Débloquer maintenant
                            </button>
                            <button class="btn-paywall-cancel" onclick="window.FreemiumDashboard.closePaywallModal('${sessionId}', '${paywallData.paywall_type}', true)">
                                Peut-être plus tard
                            </button>
                        </div>

                        <div class="paywall-guarantee">
                            🔒 Paiement sécurisé • 🔄 Remboursement 30 jours • ⚡ Accès immédiat
                        </div>
                    </div>
                </div>
            </div>
        `;

        document.body.insertAdjacentHTML('beforeend', modalHTML);

        // Animation d'ouverture
        requestAnimationFrame(() => {
            document.getElementById(`paywall-modal-${sessionId}`).classList.add('show');
        });

        // Stocker la référence
        this.paywallModals.set(sessionId, paywallData);
    }

    /**
     * 💳 TRAITER PAIEMENT PAYWALL
     */
    async processPaywallPayment(sessionId, paywallType) {
        try {
            console.log(`🚀 Processing payment for: ${paywallType}`);

            // 📊 Google Analytics - Purchase Intent
            if (typeof window.trackPaywallEvent === 'function') {
                window.trackPaywallEvent(paywallType, 'purchase_intent', sessionId);
            }

            // 🔥 NOUVEAU : Utiliser les vraies routes de paiement
            const paywallData = this.paywallModals.get(sessionId);

            // Créer une session de checkout Stripe
            const checkoutResponse = await window.ZineInsightAPI.request('/api/payments/create-checkout-session', 'POST', {
                paywall_type: paywallType,
                user_id: 'current_user', // TODO: Récupérer le vrai user ID
                resource_id: sessionId
            });

            if (checkoutResponse.success) {
                console.log('🛒 Checkout session created, redirecting...');

                // Rediriger vers Stripe Checkout (ou mock checkout en dev)
                window.location.href = checkoutResponse.checkout_url;

            } else {
                throw new Error(checkoutResponse.error || 'Checkout session creation failed');
            }

        } catch (error) {
            console.error('❌ Paywall payment failed:', error);

            // 📊 Google Analytics - Payment Error
            if (typeof window.trackPaywallEvent === 'function') {
                window.trackPaywallEvent(paywallType, 'payment_error', sessionId);
            }

            // Afficher une notification d'erreur
            this.showErrorNotification('Erreur lors du traitement du paiement. Veuillez réessayer.');
        }
    }

    /**
     * ❌ FERMER MODAL PAYWALL
     */
    closePaywallModal(sessionId, paywallType = null, isDismissal = false) {
        const modal = document.getElementById(`paywall-modal-${sessionId}`);
        if (modal) {
            // 📊 Google Analytics - Modal Close
            if (isDismissal && paywallType && typeof window.trackPaywallEvent === 'function') {
                window.trackPaywallEvent(paywallType, 'dismiss', sessionId);
            }

            modal.classList.remove('show');
            setTimeout(() => {
                modal.remove();
                this.paywallModals.delete(sessionId);
            }, 300);
        }
    }

    /**
     * 🎉 NOTIFICATION SUCCÈS
     */
    showSuccessNotification(message) {
        // Si c'est un paywallType, utiliser le message par défaut
        if (typeof message !== 'string') {
            const messages = {
                [this.paywallTypes.GUIDE_UNLOCK]: 'Guide débloqué ! 📖',
                [this.paywallTypes.COUNTRY_ACCESS]: 'Accès pays débloqué ! 🌍',
                [this.paywallTypes.UNLIMITED_ANALYSES]: 'Analyses illimitées activées ! 🚀',
                [this.paywallTypes.PREMIUM_INSIGHTS]: 'Insights IA débloqués ! 🧠',
                [this.paywallTypes.EXPORT_PDF]: 'Export PDF disponible ! 📄'
            };
            message = messages[message] || 'Fonctionnalité débloquée !';
        }

        const notification = document.createElement('div');
        notification.className = 'success-notification';
        notification.innerHTML = `
            <div class="success-content">
                <div class="success-icon">✅</div>
                <h3>Succès !</h3>
                <p>${message}</p>
            </div>
        `;

        document.body.appendChild(notification);

        setTimeout(() => {
            notification.remove();
        }, 4000);
    }

    /**
     * ❌ NOTIFICATION D'ERREUR
     */
    showErrorNotification(message) {
        const notification = document.createElement('div');
        notification.className = 'error-notification';
        notification.innerHTML = `
            <div class="error-content">
                <div class="error-icon">❌</div>
                <h3>Erreur</h3>
                <p>${message}</p>
            </div>
        `;

        document.body.appendChild(notification);

        setTimeout(() => {
            notification.remove();
        }, 5000);
    }

    /**
     * 📈 AFFICHER CTA UPGRADE
     */
    showUpgradeCTA() {
        // Ajouter une bannière upgrade discrète
        const ctaBanner = document.createElement('div');
        ctaBanner.className = 'upgrade-cta-banner';
        ctaBanner.innerHTML = `
            <div class="cta-content">
                <span class="cta-text">✨ Débloquez tout le potentiel de votre dashboard</span>
                <button class="cta-upgrade-btn" onclick="window.FreemiumDashboard.showPaywall('${this.paywallTypes.PREMIUM_INSIGHTS}')">
                    Upgrade vers Pro
                </button>
            </div>
            <button class="cta-close" onclick="this.parentElement.style.display='none'">×</button>
        `;

        // Insérer en haut du dashboard
        const dashboard = document.querySelector('.dashboard-container');
        if (dashboard) {
            dashboard.insertBefore(ctaBanner, dashboard.firstChild);
        }
    }
}

/**
 * 🌟 INSTANCE GLOBALE
 */
window.FreemiumDashboard = new FreemiumDashboard();

console.log('💰 Freemium Dashboard System ready!');
