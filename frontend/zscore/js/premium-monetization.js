/* ====================================
   🚀 PREMIUM MONETIZATION JAVASCRIPT
   Enterprise-Level Conversion Optimization
   Built by Claude Sonnet 3.5 Premium
==================================== */

// ===== REVOLUTIONARY MONETIZATION MANAGER ===== //
class PremiumMonetizationEngine {
    constructor() {
        this.conversionOptimizations = new Map();
        this.userBehaviorTracking = new Map();
        this.urgencyTimers = new Map();
        this.animationQueue = [];
        this.isInitialized = false;

        // Configuration des prix dynamiques
        this.pricingConfig = {
            guide_premium: {
                originalPrice: 29.99,
                currentPrice: 9.99,
                urgencyDiscount: 0.67,
                stockRemaining: 73
            },
            multi_pays: {
                currentPrice: 4.99,
                popularityBoost: 847
            },
            bundle_ultimate: {
                originalPrice: 49.98,
                currentPrice: 14.99,
                savings: 0.70
            }
        };

        this.init();
    }

    // 🚀 INITIALISATION RÉVOLUTIONNAIRE
    async init() {
        if (this.isInitialized) return;

        console.log('🎯 Initializing Premium Monetization Engine...');

        try {
            // Attendre que le DOM soit prêt
            await this.waitForDOM();

            // Initialiser tous les modules
            await Promise.all([
                this.initializeSuccessBanner(),
                this.initializeCountdownTimer(),
                this.initializeBehaviorTracking(),
                this.initializeConversionOptimizations(),
                this.initializePremiumAnimations(),
                this.initializeUrgencyElements()
            ]);

            // Démarrer les systèmes de conversion
            this.startConversionEngines();

            this.isInitialized = true;
            console.log('✅ Premium Monetization Engine Ready!');

        } catch (error) {
            console.error('❌ Monetization Engine initialization failed:', error);
        }
    }

    // ⏳ ATTENDRE LE DOM
    waitForDOM() {
        return new Promise((resolve) => {
            if (document.readyState === 'loading') {
                document.addEventListener('DOMContentLoaded', resolve);
            } else {
                resolve();
            }
        });
    }

    // 🎉 BANNIÈRE DE SUCCÈS ANIMÉE
    async initializeSuccessBanner() {
        const banner = document.getElementById('successBanner');
        if (!banner) return;

        // Animation d'entrée spectaculaire
        banner.style.transform = 'translateY(-100px)';
        banner.style.opacity = '0';

        // Démarrer l'animation après un délai
        setTimeout(() => {
            banner.style.transition = 'all 0.8s cubic-bezier(0.4, 0, 0.2, 1)';
            banner.style.transform = 'translateY(0)';
            banner.style.opacity = '1';
        }, 300);

        // Animer les statistiques
        setTimeout(() => {
            this.animateStatCounters();
        }, 1200);

        // Effet de particules
        setTimeout(() => {
            this.createSuccessParticles(banner);
        }, 1500);
    }

    // 🔢 ANIMATION DES COMPTEURS
    animateStatCounters() {
        const counters = [
            { id: 'questionsCount', target: 150, suffix: '+' },
            { id: 'citiesAnalyzed', target: 541, suffix: '' },
            { id: 'compatibilityScore', target: 94, suffix: '%' }
        ];

        counters.forEach(({ id, target, suffix }) => {
            const element = document.getElementById(id);
            if (!element) return;

            let current = 0;
            const increment = target / 60; // 60 frames pour 1 seconde
            const timer = setInterval(() => {
                current += increment;
                if (current >= target) {
                    current = target;
                    clearInterval(timer);
                }
                element.textContent = Math.floor(current) + suffix;
            }, 16); // ~60fps
        });
    }

    // ✨ PARTICULES DE SUCCÈS
    createSuccessParticles(container) {
        const particleCount = 15;
        for (let i = 0; i < particleCount; i++) {
            setTimeout(() => {
                this.createParticle(container);
            }, i * 100);
        }
    }

    createParticle(container) {
        const particle = document.createElement('div');
        particle.innerHTML = ['🎉', '⭐', '🎯', '🚀', '💎'][Math.floor(Math.random() * 5)];

        Object.assign(particle.style, {
            position: 'absolute',
            fontSize: '1.5rem',
            pointerEvents: 'none',
            zIndex: '1000',
            left: Math.random() * container.offsetWidth + 'px',
            top: Math.random() * container.offsetHeight + 'px',
            animation: 'particleFloat 3s ease-out forwards'
        });

        container.appendChild(particle);

        // Supprimer après l'animation
        setTimeout(() => {
            particle.remove();
        }, 3000);

        // Ajouter le CSS de l'animation si nécessaire
        this.ensureParticleCSS();
    }

    ensureParticleCSS() {
        if (!document.querySelector('#particleAnimation')) {
            const style = document.createElement('style');
            style.id = 'particleAnimation';
            style.textContent = `
                @keyframes particleFloat {
                    0% {
                        transform: translateY(0) scale(0);
                        opacity: 0;
                    }
                    20% {
                        transform: translateY(-20px) scale(1);
                        opacity: 1;
                    }
                    100% {
                        transform: translateY(-150px) scale(0);
                        opacity: 0;
                    }
                }
            `;
            document.head.appendChild(style);
        }
    }

    // ⏰ COMPTE À REBOURS D'URGENCE
    initializeCountdownTimer() {
        const timer = document.getElementById('countdownTimer');
        if (!timer) return;

        // Définir une fin d'offre (24h à partir de maintenant)
        const endTime = new Date().getTime() + (24 * 60 * 60 * 1000);

        const updateCountdown = () => {
            const now = new Date().getTime();
            const timeLeft = endTime - now;

            if (timeLeft > 0) {
                const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
                const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

                const hoursEl = document.getElementById('hours');
                const minutesEl = document.getElementById('minutes');
                const secondsEl = document.getElementById('seconds');

                if (hoursEl) hoursEl.textContent = hours.toString().padStart(2, '0');
                if (minutesEl) minutesEl.textContent = minutes.toString().padStart(2, '0');
                if (secondsEl) secondsEl.textContent = seconds.toString().padStart(2, '0');

                // Effet visuel quand il reste moins d'une heure
                if (timeLeft < 3600000) { // 1 heure en ms
                    timer.classList.add('critical-time');
                }
            } else {
                // Temps écoulé - renouveler l'offre
                this.renewOffer();
            }
        };

        // Mettre à jour toutes les secondes
        this.urgencyTimers.set('countdown', setInterval(updateCountdown, 1000));
        updateCountdown(); // Exécution immédiate
    }

    // 🔄 RENOUVELER L'OFFRE
    renewOffer() {
        const timer = document.getElementById('countdownTimer');
        if (timer) {
            timer.classList.add('offer-renewed');

            // Flash d'animation
            setTimeout(() => {
                timer.classList.remove('offer-renewed');
                // Redémarrer avec 24h
                this.initializeCountdownTimer();
            }, 2000);
        }
    }

    // 📊 SUIVI DU COMPORTEMENT UTILISATEUR
    initializeBehaviorTracking() {
        // Tracker le temps passé sur la page
        this.startTime = Date.now();

        // Tracker les hovers sur les CTA
        document.querySelectorAll('.tier-cta').forEach(button => {
            let hoverStartTime;

            button.addEventListener('mouseenter', () => {
                hoverStartTime = Date.now();
                this.triggerHoverOptimizations(button);
            });

            button.addEventListener('mouseleave', () => {
                if (hoverStartTime) {
                    const hoverDuration = Date.now() - hoverStartTime;
                    this.trackBehavior('cta_hover', {
                        product: button.dataset.product,
                        duration: hoverDuration
                    });
                }
            });
        });

        // Tracker le scroll
        let scrollTimeout;
        window.addEventListener('scroll', () => {
            clearTimeout(scrollTimeout);
            scrollTimeout = setTimeout(() => {
                this.trackScrollBehavior();
            }, 150);
        });

        // Tracker les clics
        document.addEventListener('click', (e) => {
            if (e.target.closest('[data-action="purchase"]')) {
                const product = e.target.closest('[data-action="purchase"]').dataset.product;
                this.trackBehavior('purchase_intent', { product });
                this.triggerPurchaseOptimizations(product);
            }
        });
    }

    // 🎯 OPTIMISATIONS AU HOVER
    triggerHoverOptimizations(button) {
        // Effet de glow intensifié
        button.style.boxShadow = '0 25px 50px rgba(102, 126, 234, 0.8)';

        // Micro-animation de la tier
        const tier = button.closest('.premium-tier');
        if (tier) {
            tier.style.transform = 'translateY(-12px) scale(1.03)';
        }

        // Montrer des éléments cachés de valeur
        this.showHiddenValueProps(tier);
    }

    // 💎 MONTRER LES PROPOSITIONS DE VALEUR CACHÉES
    showHiddenValueProps(tier) {
        const hiddenValue = tier.querySelector('.hidden-value');
        if (hiddenValue) {
            hiddenValue.classList.add('revealed');
        }
    }

    // 🛒 OPTIMISATIONS À L'ACHAT
    triggerPurchaseOptimizations(product) {
        // Vibrer le bouton si supporté
        if (navigator.vibrate) {
            navigator.vibrate([50, 30, 50]);
        }

        // Montrer une modal de confirmation premium
        this.showPremiumConfirmation(product);

        // Déclencher des animations d'urgence
        this.intensifyUrgency();
    }

    // ⚡ INTENSIFIER L'URGENCE
    intensifyUrgency() {
        // Faire clignoter le stock
        const stockIndicator = document.querySelector('.stock-indicator');
        if (stockIndicator) {
            stockIndicator.classList.add('critical-stock');

            setTimeout(() => {
                stockIndicator.classList.remove('critical-stock');
            }, 5000);
        }

        // Réduire légèrement le stock
        const stockText = document.querySelector('.stock-text strong');
        if (stockText) {
            const current = parseInt(stockText.textContent);
            if (current > 50) {
                stockText.textContent = current - Math.floor(Math.random() * 3 + 1);
            }
        }
    }

    // 📈 TRACKER LE COMPORTEMENT
    trackBehavior(event, data) {
        const behaviorData = {
            event,
            data,
            timestamp: Date.now(),
            timeOnPage: Date.now() - this.startTime,
            userAgent: navigator.userAgent.substring(0, 100)
        };

        this.userBehaviorTracking.set(event + '_' + Date.now(), behaviorData);

        // En production, envoyer à ton analytics
        console.log('📊 Behavior tracked:', behaviorData);
    }

    // 📜 TRACKER LE SCROLL
    trackScrollBehavior() {
        const scrollPercent = Math.round((window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100);

        if (scrollPercent > 80 && !this.userBehaviorTracking.has('scroll_80')) {
            this.trackBehavior('scroll_80', { percentage: scrollPercent });
            this.triggerScrollOptimizations();
        }
    }

    // 🎯 OPTIMISATIONS AU SCROLL
    triggerScrollOptimizations() {
        // Montrer une floating CTA
        this.showFloatingCTA();

        // Intensifier les animations
        document.querySelectorAll('.premium-tier').forEach(tier => {
            tier.classList.add('scroll-revealed');
        });
    }

    // 🎈 CTA FLOTTANT
    showFloatingCTA() {
        if (document.querySelector('.floating-cta')) return; // Déjà affiché

        const floatingCTA = document.createElement('div');
        floatingCTA.className = 'floating-cta';
        floatingCTA.innerHTML = `
            <div class="floating-content">
                <div class="floating-text">
                    <!-- TEMP DÉSACTIVÉ - Marketing urgent à réactiver si besoin :
                    <strong>🔥 Dernière chance !</strong>
                    <span>Guide à -67% expire bientôt</span>
                    -->
                    <strong>🎯 Guide Personnalisé</strong>
                    <span>Recommandations adaptées à votre profil</span>
                </div>
                <button class="floating-btn" data-action="purchase" data-product="guide_premium">
                    <!-- TEMP DÉSACTIVÉ - Prix urgent : Débloquer 9,99€ -->
                    Obtenir le Guide
                </button>
            </div>
            <button class="floating-close">×</button>
        `;

        document.body.appendChild(floatingCTA);

        // Animation d'entrée
        setTimeout(() => {
            floatingCTA.classList.add('show');
        }, 100);

        // Fermeture
        floatingCTA.querySelector('.floating-close').addEventListener('click', () => {
            floatingCTA.classList.remove('show');
            setTimeout(() => floatingCTA.remove(), 300);
        });

        // Auto-fermeture après 10 secondes
        setTimeout(() => {
            if (floatingCTA.classList.contains('show')) {
                floatingCTA.click();
            }
        }, 10000);

        // Ajouter le CSS si nécessaire
        this.ensureFloatingCSS();
    }

    // 🎨 CSS POUR LE CTA FLOTTANT
    ensureFloatingCSS() {
        if (!document.querySelector('#floatingCTACSS')) {
            const style = document.createElement('style');
            style.id = 'floatingCTACSS';
            style.textContent = `
                .floating-cta {
                    position: fixed;
                    bottom: 20px;
                    right: 20px;
                    background: linear-gradient(135deg, #667eea, #764ba2);
                    color: white;
                    padding: 16px 20px;
                    border-radius: 16px;
                    box-shadow: 0 20px 40px rgba(102, 126, 234, 0.4);
                    z-index: 10000;
                    transform: translateX(400px);
                    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
                    max-width: 300px;
                    backdrop-filter: blur(20px);
                }

                .floating-cta.show {
                    transform: translateX(0);
                }

                .floating-content {
                    display: flex;
                    align-items: center;
                    gap: 16px;
                }

                .floating-text {
                    display: flex;
                    flex-direction: column;
                    gap: 4px;
                }

                .floating-text strong {
                    font-size: 0.9rem;
                }

                .floating-text span {
                    font-size: 0.8rem;
                    opacity: 0.9;
                }

                .floating-btn {
                    background: rgba(255, 255, 255, 0.2);
                    border: 1px solid rgba(255, 255, 255, 0.3);
                    color: white;
                    padding: 8px 16px;
                    border-radius: 12px;
                    font-weight: 600;
                    font-size: 0.85rem;
                    cursor: pointer;
                    transition: all 0.2s ease;
                    white-space: nowrap;
                }

                .floating-btn:hover {
                    background: rgba(255, 255, 255, 0.3);
                    transform: scale(1.05);
                }

                .floating-close {
                    position: absolute;
                    top: 8px;
                    right: 8px;
                    background: none;
                    border: none;
                    color: white;
                    font-size: 1.2rem;
                    cursor: pointer;
                    opacity: 0.7;
                    transition: opacity 0.2s ease;
                }

                .floating-close:hover {
                    opacity: 1;
                }

                @media (max-width: 768px) {
                    .floating-cta {
                        bottom: 10px;
                        right: 10px;
                        left: 10px;
                        max-width: none;
                    }

                    .floating-content {
                        flex-direction: column;
                        text-align: center;
                        gap: 12px;
                    }
                }
            `;
            document.head.appendChild(style);
        }
    }

    // 🎭 ANIMATIONS PREMIUM
    initializePremiumAnimations() {
        // Observer d'intersection pour les animations au scroll
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animated-in');
                }
            });
        }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

        // Observer tous les tiers
        document.querySelectorAll('.premium-tier').forEach(tier => {
            observer.observe(tier);
        });

        // Animations des badges
        this.animateBadges();

        // Animations de fond
        this.createBackgroundEffects();
    }

    // 🏷️ ANIMER LES BADGES
    animateBadges() {
        const badges = document.querySelectorAll('.tier-badge');
        badges.forEach((badge, index) => {
            setTimeout(() => {
                badge.style.animation = 'badgeEntrance 0.6s cubic-bezier(0.4, 0, 0.2, 1) forwards';
            }, index * 200);
        });

        // Ajouter le CSS d'animation
        if (!document.querySelector('#badgeAnimations')) {
            const style = document.createElement('style');
            style.id = 'badgeAnimations';
            style.textContent = `
                @keyframes badgeEntrance {
                    0% {
                        transform: translateY(-30px) scale(0);
                        opacity: 0;
                    }
                    50% {
                        transform: translateY(10px) scale(1.2);
                    }
                    100% {
                        transform: translateY(0) scale(1);
                        opacity: 1;
                    }
                }

                .critical-time .digit-group {
                    animation: criticalPulse 0.5s ease-in-out infinite alternate;
                }

                @keyframes criticalPulse {
                    0% { background: #dc2626; }
                    100% { background: #b91c1c; }
                }

                .critical-stock {
                    animation: stockAlert 0.3s ease-in-out 5;
                }

                @keyframes stockAlert {
                    0%, 100% { transform: scale(1); }
                    50% { transform: scale(1.05); }
                }

                .scroll-revealed {
                    animation: revealOnScroll 0.8s cubic-bezier(0.4, 0, 0.2, 1);
                }

                @keyframes revealOnScroll {
                    0% {
                        transform: translateY(30px) scale(0.95);
                        opacity: 0.7;
                    }
                    100% {
                        transform: translateY(0) scale(1);
                        opacity: 1;
                    }
                }
            `;
            document.head.appendChild(style);
        }
    }

    // 🌟 EFFETS DE FOND
    createBackgroundEffects() {
        // Créer des éléments de fond flottants
        const backgroundContainer = document.createElement('div');
        backgroundContainer.className = 'floating-elements';
        backgroundContainer.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: -1;
            overflow: hidden;
        `;

        // Créer plusieurs éléments flottants
        for (let i = 0; i < 6; i++) {
            const element = document.createElement('div');
            element.className = 'floating-element';
            element.style.cssText = `
                position: absolute;
                width: ${Math.random() * 100 + 50}px;
                height: ${Math.random() * 100 + 50}px;
                background: linear-gradient(135deg,
                    rgba(102, 126, 234, 0.1),
                    rgba(118, 75, 162, 0.1));
                border-radius: 50%;
                left: ${Math.random() * 100}%;
                top: ${Math.random() * 100}%;
                animation: float ${Math.random() * 20 + 10}s linear infinite;
            `;
            backgroundContainer.appendChild(element);
        }

        document.body.appendChild(backgroundContainer);

        // CSS pour l'animation flottante
        if (!document.querySelector('#floatingElements')) {
            const style = document.createElement('style');
            style.id = 'floatingElements';
            style.textContent = `
                @keyframes float {
                    0% { transform: translateY(0) rotate(0deg); }
                    50% { transform: translateY(-50px) rotate(180deg); }
                    100% { transform: translateY(0) rotate(360deg); }
                }
            `;
            document.head.appendChild(style);
        }
    }

    // ⚡ ÉLÉMENTS D'URGENCE
    initializeUrgencyElements() {
        // Décrémenter le stock périodiquement
        setInterval(() => {
            this.updateStockNumbers();
        }, 30000); // Toutes les 30 secondes

        // Montrer des notifications d'achat fictives
        setInterval(() => {
            this.showPurchaseNotification();
        }, 45000); // Toutes les 45 secondes
    }

    // 📉 METTRE À JOUR LE STOCK
    updateStockNumbers() {
        const stockText = document.querySelector('.stock-text strong');
        if (stockText) {
            const current = parseInt(stockText.textContent);
            if (current > 45) {
                const decrease = Math.floor(Math.random() * 2 + 1);
                stockText.textContent = current - decrease;

                // Animation de décrémentation
                stockText.parentElement.classList.add('stock-updated');
                setTimeout(() => {
                    stockText.parentElement.classList.remove('stock-updated');
                }, 1000);
            }
        }
    }

    // 🔔 NOTIFICATION D'ACHAT
    showPurchaseNotification() {
        if (document.querySelector('.purchase-notification')) return;

        const notification = document.createElement('div');
        notification.className = 'purchase-notification';

        const names = ['Sarah M.', 'Pierre L.', 'Julie D.', 'Marc R.', 'Emma T.'];
        const cities = ['Paris → Toronto', 'Lyon → Melbourne', 'Marseille → Vancouver', 'Nice → Sydney'];

        const randomName = names[Math.floor(Math.random() * names.length)];
        const randomCity = cities[Math.floor(Math.random() * cities.length)];

        notification.innerHTML = `
            <div class="notification-content">
                <div class="notification-avatar">👤</div>
                <div class="notification-text">
                    <strong>${randomName}</strong> vient d'acheter le Guide Expatriation
                    <span class="notification-location">${randomCity}</span>
                </div>
            </div>
        `;

        document.body.appendChild(notification);

        // Animation d'entrée
        setTimeout(() => {
            notification.classList.add('show');
        }, 100);

        // Auto-suppression
        setTimeout(() => {
            notification.classList.remove('show');
            setTimeout(() => notification.remove(), 300);
        }, 4000);

        // Ajouter le CSS si nécessaire
        this.ensureNotificationCSS();
    }

    // 🎨 CSS POUR LES NOTIFICATIONS
    ensureNotificationCSS() {
        if (!document.querySelector('#notificationCSS')) {
            const style = document.createElement('style');
            style.id = 'notificationCSS';
            style.textContent = `
                .purchase-notification {
                    position: fixed;
                    top: 100px;
                    left: 20px;
                    background: rgba(255, 255, 255, 0.95);
                    backdrop-filter: blur(20px);
                    border: 1px solid rgba(34, 197, 94, 0.3);
                    border-radius: 12px;
                    padding: 16px;
                    box-shadow: 0 10px 25px rgba(34, 197, 94, 0.2);
                    z-index: 9999;
                    transform: translateX(-400px);
                    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
                    max-width: 280px;
                }

                .purchase-notification.show {
                    transform: translateX(0);
                }

                .notification-content {
                    display: flex;
                    align-items: center;
                    gap: 12px;
                }

                .notification-avatar {
                    font-size: 1.5rem;
                }

                .notification-text {
                    display: flex;
                    flex-direction: column;
                    gap: 2px;
                }

                .notification-text strong {
                    color: #374151;
                    font-size: 0.9rem;
                }

                .notification-location {
                    color: #6b7280;
                    font-size: 0.8rem;
                }

                .stock-updated {
                    animation: stockPulse 0.5s ease-out;
                }

                @keyframes stockPulse {
                    0% { transform: scale(1); }
                    50% { transform: scale(1.1); color: #dc2626; }
                    100% { transform: scale(1); }
                }

                @media (max-width: 768px) {
                    .purchase-notification {
                        left: 10px;
                        right: 10px;
                        max-width: none;
                    }
                }
            `;
            document.head.appendChild(style);
        }
    }

    // 🚀 DÉMARRER LES MOTEURS DE CONVERSION
    startConversionEngines() {
        // Démarrer la surveillance des performances
        this.startPerformanceMonitoring();

        // Optimiser selon l'heure
        this.optimizeByTimeOfDay();

        // Démarrer les tests A/B automatiques
        this.startAutomatedTesting();

        console.log('🎯 All conversion engines started!');
    }

    // 📊 SURVEILLANCE DES PERFORMANCES
    startPerformanceMonitoring() {
        // Mesurer les métriques de performance
        if ('performance' in window) {
            const perfObserver = new PerformanceObserver((list) => {
                list.getEntries().forEach((entry) => {
                    if (entry.entryType === 'navigation') {
                        console.log('📈 Page Load Time:', entry.loadEventEnd - entry.loadEventStart + 'ms');
                    }
                });
            });

            perfObserver.observe({ entryTypes: ['navigation'] });
        }
    }

    // 🕐 OPTIMISER SELON L'HEURE
    optimizeByTimeOfDay() {
        const hour = new Date().getHours();

        if (hour >= 18 && hour <= 23) {
            // Soirée - intensifier l'urgence
            this.intensifyEveningOptimizations();
        } else if (hour >= 9 && hour <= 17) {
            // Journée de travail - focus sur la praticité
            this.optimizeForWorkingHours();
        }
    }

    // 🌙 OPTIMISATIONS DU SOIR
    intensifyEveningOptimizations() {
        // Ajouter plus d'urgence le soir
        document.querySelectorAll('.limited-offer').forEach(element => {
            element.innerHTML = '<i data-lucide="clock"></i> <span>Se termine ce soir !</span>';
        });
    }

    // 💼 OPTIMISATIONS HEURES DE BUREAU
    optimizeForWorkingHours() {
        // Mettre l'accent sur la planification
        const descriptions = document.querySelectorAll('.tier-description');
        descriptions.forEach(desc => {
            if (desc.textContent.includes('blueprint')) {
                desc.innerHTML += ' <strong>• Planifiez votre projet</strong>';
            }
        });
    }

    // 🧪 TESTS A/B AUTOMATIQUES
    startAutomatedTesting() {
        // Tester différentes variantes de prix
        if (Math.random() < 0.5) {
            this.applyPricingVariant('high_anchor');
        } else {
            this.applyPricingVariant('scarcity_focus');
        }
    }

    // 💰 APPLIQUER VARIANTE DE PRIX
    applyPricingVariant(variant) {
        console.log(`🧪 Testing pricing variant: ${variant}`);

        if (variant === 'high_anchor') {
            // Augmenter le prix d'ancrage
            const originalPrices = document.querySelectorAll('.original-price');
            originalPrices.forEach(price => {
                price.innerHTML = 'Valeur réelle: <strike>39,99€</strike>';
            });
        } else if (variant === 'scarcity_focus') {
            // Focus sur la rareté
            const stockText = document.querySelector('.stock-text');
            if (stockText) {
                stockText.innerHTML = 'Plus que <strong style="color: #dc2626;">23 guides</strong> à prix réduit';
            }
        }
    }

    // 🔧 MÉTHODES UTILITAIRES

    // Nettoyer à la destruction
    destroy() {
        this.urgencyTimers.forEach(timer => clearInterval(timer));
        this.urgencyTimers.clear();
        this.userBehaviorTracking.clear();
        this.conversionOptimizations.clear();

        // Supprimer les éléments créés dynamiquement
        document.querySelectorAll('.floating-cta, .purchase-notification, .floating-elements').forEach(el => el.remove());

        console.log('🧹 Monetization Engine cleaned up');
    }
}

// ===== INITIALISATION GLOBALE ===== //
let premiumMonetization;

// Initialiser quand la page est prête
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        premiumMonetization = new PremiumMonetizationEngine();
    });
} else {
    premiumMonetization = new PremiumMonetizationEngine();
}

// Nettoyer avant le déchargement
window.addEventListener('beforeunload', () => {
    if (premiumMonetization) {
        premiumMonetization.destroy();
    }
});

// Export global pour debugging
window.PremiumMonetization = premiumMonetization;

console.log('💎 Premium Monetization System Loaded - Ready to Convert!');
