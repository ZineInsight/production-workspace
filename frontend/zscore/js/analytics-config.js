/**
 * 📊 CONFIGURATION GOOGLE ANALYTICS 4
 * Revolutionary Platform - Analytics Config
 */

window.AnalyticsConfig = {
    // 🎯 ID de mesure Google Tag - REAL ID
    measurementId: 'AW-17478118908', // ✅ Real Google Tag ID

    // 🏷️ Événements personnalisés pour le freemium
    events: {
        // Paywalls
        PAYWALL_VIEW: 'paywall_view',
        PAYWALL_DISMISS: 'paywall_dismiss',
        PAYWALL_UPGRADE_CLICK: 'paywall_upgrade_click',
        PAYWALL_PURCHASE_INTENT: 'paywall_purchase_intent',
        PAYWALL_PAYMENT_ERROR: 'paywall_payment_error',

        // Dashboard interactions
        DASHBOARD_LOAD: 'dashboard_load',
        ANALYSIS_LIMIT_REACHED: 'analysis_limit_reached',
        COUNTRY_ACCESS_BLOCKED: 'country_access_blocked',
        EXPORT_BLOCKED: 'export_blocked',

        // Conversions
        PURCHASE: 'purchase',
        SUBSCRIPTION_START: 'subscription_start',
        TRIAL_START: 'trial_start'
    },

    // 💰 Types de paywalls pour le tracking
    paywallTypes: {
        GUIDE_UNLOCK: 'guide_unlock',
        COUNTRY_ACCESS: 'country_access',
        UNLIMITED_ANALYSES: 'unlimited_analyses',
        PREMIUM_INSIGHTS: 'premium_insights',
        EXPORT_PDF: 'export_pdf'
    },

    // 🎨 Catégories d'événements
    categories: {
        PAYWALL: 'Paywall',
        DASHBOARD: 'Dashboard',
        USER_ENGAGEMENT: 'User Engagement',
        CONVERSION: 'Conversion',
        PREMIUM_FEATURES: 'Premium Features'
    },

    // 🔧 Configuration avancée
    config: {
        // Anonymiser les IPs
        anonymize_ip: true,
        // Respecter Do Not Track
        respect_dnt: true,
        // Délai avant envoi des événements (ms)
        send_page_view: true,
        // Custom dimensions
        custom_parameters: {
            user_tier: 'custom_parameter_1',
            feature_accessed: 'custom_parameter_2',
            paywall_type: 'custom_parameter_3'
        }
    }
};

// 📊 Fonction helper pour tracker facilement
window.trackFreemiumEvent = function (eventName, parameters = {}) {
    if (typeof gtag === 'undefined') {
        console.warn('🚫 Google Analytics not loaded');
        return;
    }

    // Ajouter des paramètres par défaut
    const defaultParams = {
        timestamp: new Date().toISOString(),
        page_location: window.location.href,
        user_tier: window.FreemiumDashboard?.userTier || 'unknown'
    };

    const eventParams = { ...defaultParams, ...parameters };

    console.log(`📊 GA4 Event: ${eventName}`, eventParams);
    gtag('event', eventName, eventParams);
};

console.log('📊 Analytics Config loaded for Revolutionary Platform');
