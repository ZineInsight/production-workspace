/**
 * 💳 STRIPE PAYMENT INTEGRATION - Revolutionary Edition
 * ====================================================
 * Intégration Stripe moderne et sécurisée pour ta SPA
 */

class ZineInsightPayment {
    constructor() {
        // 🎯 Configuration Stripe
        this.stripe = null;
        this.elements = null;
        this.card = null;

        // État du paiement
        this.paymentState = {
            processing: false,
            sessionId: null,
            clientSecret: null,
            selectedTier: null
        };

        // Configuration des tiers
        this.tiers = {
            tier_2_pays: {
                name: 'Pays Complet',
                price: 1499, // 14.99 EUR
                priceFormatted: '14,99€',
                currency: 'eur',
                features: [
                    'Simulations illimitées',
                    'Toutes les villes du pays',
                    'Guides complets',
                    'Export PDF professionnel',
                    'Comparaisons détaillées'
                ]
            },
            tier_3_monde: {
                name: 'Monde Entier',
                price: 3999, // 39.99 EUR
                priceFormatted: '39,99€',
                currency: 'eur',
                features: [
                    'Simulations illimitées',
                    '201 villes mondiales',
                    'Tous les guides pays',
                    'Exports PDF illimités',
                    'Analyses croisées multicritères',
                    'Accès nouvelles villes en premier'
                ]
            }
        };

        console.log('💳 Payment system initialized');
        this.initializeStripe();
    }

    /**
     * 🚀 INITIALISER STRIPE
     */
    async initializeStripe() {
        try {
            // Vérifier si Stripe est chargé
            if (typeof Stripe === 'undefined') {
                await this.loadStripeScript();
            }

            // Récupérer la clé publique depuis l'API
            const config = await window.ZineInsightAPI.request('/api/stripe-config');

            if (!config.public_key) {
                throw new Error('Stripe public key not found');
            }

            this.stripe = Stripe(config.public_key);
            console.log('✅ Stripe initialized successfully');

        } catch (error) {
            console.error('❌ Stripe initialization failed:', error);
        }
    }

    /**
     * 📜 CHARGER SCRIPT STRIPE
     */
    async loadStripeScript() {
        return new Promise((resolve, reject) => {
            if (document.querySelector('script[src*="stripe.com"]')) {
                resolve();
                return;
            }

            const script = document.createElement('script');
            script.src = 'https://js.stripe.com/v3/';
            script.onload = resolve;
            script.onerror = reject;
            document.head.appendChild(script);
        });
    }

    /**
     * 💳 OUVRIR MODAL DE PAIEMENT
     */
    openPaymentModal(tier = 'tier_2_pays', additionalData = {}) {
        const tierConfig = this.tiers[tier];
        if (!tierConfig) {
            console.error('❌ Invalid tier:', tier);
            return;
        }

        this.paymentState.selectedTier = tier;

        // Créer le modal HTML
        const modalHTML = `
            <div id="payment-modal" class="payment-modal-overlay">
                <div class="payment-modal-container">
                    <div class="payment-modal-header">
                        <h2>🚀 Finaliser votre commande</h2>
                        <button class="close-modal" onclick="window.ZineInsightPayment.closeModal()">×</button>
                    </div>

                    <div class="payment-product-summary">
                        <div class="product-info">
                            <h3>${tierConfig.name}</h3>
                            <div class="product-price">${tierConfig.priceFormatted}</div>
                            <div class="product-features">
                                ${tierConfig.features.map(feature => `
                                    <div class="feature-item">✅ ${feature}</div>
                                `).join('')}
                            </div>
                        </div>
                    </div>

                    <div class="payment-form-container">
                        <div class="payment-tabs">
                            <button class="tab-btn active" data-tab="stripe">💳 Carte bancaire</button>
                        </div>

                        <div id="stripe-payment" class="payment-tab active">
                            <form id="payment-form" class="payment-form">
                                <div class="form-group">
                                    <label for="customer-email">Email</label>
                                    <input type="email" id="customer-email" placeholder="votre@email.com" required>
                                </div>

                                <div class="form-group">
                                    <label for="customer-name">Nom complet</label>
                                    <input type="text" id="customer-name" placeholder="Votre nom complet" required>
                                </div>

                                <div class="form-group">
                                    <label>Informations de carte</label>
                                    <div id="card-element" class="card-element">
                                        <!-- Stripe Elements injectera ici -->
                                    </div>
                                    <div id="card-errors" class="card-errors"></div>
                                </div>

                                <button type="submit" id="pay-button" class="pay-button">
                                    <span id="pay-button-text">Payer ${tierConfig.priceFormatted}</span>
                                    <div id="loading-spinner" class="loading-spinner hidden"></div>
                                </button>
                            </form>
                        </div>
                    </div>

                    <div class="payment-security">
                        <p>🔒 Paiement 100% sécurisé • Vos données sont chiffrées • Satisfaction garantie 30 jours</p>
                    </div>
                </div>
            </div>
        `;

        // Injecter dans le DOM
        document.body.insertAdjacentHTML('beforeend', modalHTML);

        // Initialiser Stripe Elements
        this.initializeStripeElements();

        // Ajouter les event listeners
        this.setupPaymentEventListeners(additionalData);

        // Animation d'ouverture
        requestAnimationFrame(() => {
            document.getElementById('payment-modal').classList.add('show');
        });
    }

    /**
     * 🎯 INITIALISER STRIPE ELEMENTS
     */
    async initializeStripeElements() {
        if (!this.stripe) {
            await this.initializeStripe();
        }

        if (!this.stripe) {
            console.error('❌ Stripe not available');
            return;
        }

        this.elements = this.stripe.elements({
            fonts: [
                {
                    cssSrc: 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap'
                }
            ]
        });

        // Style pour les éléments Stripe
        const style = {
            base: {
                fontSize: '16px',
                color: '#1a1a1a',
                fontFamily: '"Inter", system-ui, sans-serif',
                fontSmoothing: 'antialiased',
                '::placeholder': {
                    color: '#8e8e93'
                }
            },
            invalid: {
                iconColor: '#ff3b30',
                color: '#ff3b30'
            }
        };

        this.card = this.elements.create('card', {
            style: style,
            hidePostalCode: false
        });

        this.card.mount('#card-element');

        // Gestion des erreurs
        this.card.on('change', (event) => {
            const displayError = document.getElementById('card-errors');
            if (event.error) {
                displayError.textContent = event.error.message;
                displayError.classList.add('show');
            } else {
                displayError.textContent = '';
                displayError.classList.remove('show');
            }
        });

        console.log('✅ Stripe Elements initialized');
    }

    /**
     * 🎯 SETUP EVENT LISTENERS
     */
    setupPaymentEventListeners(additionalData) {
        const form = document.getElementById('payment-form');
        if (!form) return;

        form.addEventListener('submit', async (event) => {
            event.preventDefault();
            await this.processPayment(additionalData);
        });

        // Fermeture modal avec Escape
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                this.closeModal();
            }
        }, { once: true });

        // Fermeture modal en cliquant à l'extérieur
        const overlay = document.getElementById('payment-modal');
        overlay?.addEventListener('click', (e) => {
            if (e.target === overlay) {
                this.closeModal();
            }
        });
    }

    /**
     * 🚀 TRAITEMENT DU PAIEMENT
     */
    async processPayment(additionalData = {}) {
        if (this.paymentState.processing) return;

        this.paymentState.processing = true;
        this.updatePaymentUI(true);

        try {
            const email = document.getElementById('customer-email')?.value;
            const name = document.getElementById('customer-name')?.value;

            if (!email || !name) {
                throw new Error('Email et nom requis');
            }

            // 1. Créer la session de paiement
            console.log('🚀 Creating payment session...');
            const sessionResponse = await window.ZineInsightAPI.createPaymentSession(
                this.paymentState.selectedTier,
                {
                    email,
                    name,
                    ...additionalData
                }
            );

            if (sessionResponse.error) {
                throw new Error(sessionResponse.error);
            }

            // 2. Méthode Stripe Checkout (redirect)
            if (sessionResponse.checkout_url) {
                console.log('🔄 Redirecting to Stripe Checkout...');
                window.location.href = sessionResponse.checkout_url;
                return;
            }

            // 3. Méthode Payment Intent (inline)
            if (sessionResponse.client_secret) {
                console.log('💳 Processing inline payment...');
                await this.processInlinePayment(sessionResponse.client_secret, { email, name });
                return;
            }

            throw new Error('Invalid payment session response');

        } catch (error) {
            console.error('❌ Payment failed:', error);
            this.showPaymentError(error.message);
        } finally {
            this.paymentState.processing = false;
            this.updatePaymentUI(false);
        }
    }

    /**
     * 💳 PAIEMENT INLINE (avec Payment Intent)
     */
    async processInlinePayment(clientSecret, customerInfo) {
        const { error, paymentIntent } = await this.stripe.confirmCardPayment(
            clientSecret,
            {
                payment_method: {
                    card: this.card,
                    billing_details: {
                        name: customerInfo.name,
                        email: customerInfo.email
                    }
                }
            }
        );

        if (error) {
            throw new Error(error.message);
        }

        if (paymentIntent.status === 'succeeded') {
            console.log('✅ Payment succeeded!');
            this.handlePaymentSuccess(paymentIntent);
        } else {
            throw new Error('Payment not completed');
        }
    }

    /**
     * ✅ GESTION SUCCÈS PAIEMENT
     */
    handlePaymentSuccess(paymentIntent) {
        // Fermer le modal
        this.closeModal();

        // Afficher notification de succès
        this.showSuccessNotification();

        // Redirection ou activation des fonctionnalités premium
        setTimeout(() => {
            // Ici tu peux activer les fonctionnalités premium
            // ou rediriger vers la page de succès
            window.location.href = '/success?payment_intent=' + paymentIntent.id;
        }, 2000);
    }

    /**
     * ❌ GESTION ERREUR PAIEMENT
     */
    showPaymentError(message) {
        const errorDiv = document.getElementById('card-errors');
        if (errorDiv) {
            errorDiv.textContent = message;
            errorDiv.classList.add('show');
        }

        // Aussi montrer une notification globale
        if (window.ZineInsightApp) {
            window.ZineInsightApp.showNotification(message, 'error');
        }
    }

    /**
     * 🎉 NOTIFICATION SUCCÈS
     */
    showSuccessNotification() {
        const notification = `
            <div class="success-notification">
                <div class="success-content">
                    <div class="success-icon">✅</div>
                    <h3>Paiement confirmé !</h3>
                    <p>Vos fonctionnalités premium sont maintenant actives.</p>
                </div>
            </div>
        `;

        document.body.insertAdjacentHTML('beforeend', notification);

        setTimeout(() => {
            document.querySelector('.success-notification')?.remove();
        }, 3000);
    }

    /**
     * 🎯 UPDATE UI PENDANT LE PAIEMENT
     */
    updatePaymentUI(processing) {
        const button = document.getElementById('pay-button');
        const buttonText = document.getElementById('pay-button-text');
        const spinner = document.getElementById('loading-spinner');

        if (button) {
            button.disabled = processing;

            if (processing) {
                buttonText?.classList.add('hidden');
                spinner?.classList.remove('hidden');
            } else {
                buttonText?.classList.remove('hidden');
                spinner?.classList.add('hidden');
            }
        }
    }

    /**
     * ❌ FERMER MODAL
     */
    closeModal() {
        const modal = document.getElementById('payment-modal');
        if (modal) {
            modal.classList.remove('show');
            setTimeout(() => {
                modal.remove();

                // Cleanup Stripe elements
                if (this.card) {
                    this.card.unmount();
                    this.card = null;
                }
                this.elements = null;

                // Reset state
                this.paymentState = {
                    processing: false,
                    sessionId: null,
                    clientSecret: null,
                    selectedTier: null
                };

            }, 300);
        }
    }

    /**
     * 💰 MÉTHODES RAPIDES POUR DIFFÉRENTS TIERS
     */
    buyCountryPack(country = null) {
        this.openPaymentModal('tier_2_pays', { selectedCountry: country });
    }

    buyWorldPack() {
        this.openPaymentModal('tier_3_monde', { selectedCountry: 'world' });
    }

    /**
     * 🔍 VÉRIFICATION STATUT PAIEMENT
     */
    async verifyPaymentStatus(sessionId) {
        try {
            const response = await window.ZineInsightAPI.verifyPayment(sessionId);
            return response;
        } catch (error) {
            console.error('❌ Payment verification failed:', error);
            return { status: 'error', error: error.message };
        }
    }
}

/**
 * 🌟 GLOBAL PAYMENT INSTANCE
 */
window.ZineInsightPayment = new ZineInsightPayment();

console.log('💳 Payment system ready!');
