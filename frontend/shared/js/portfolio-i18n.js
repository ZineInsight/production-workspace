/**
 * Portfolio I18n System for ZineInsight
 * Handles translations between French and English
 */

class PortfolioI18n {
    constructor() {
        this.currentLanguage = 'fr'; // Default language  
        this.translations = {
            fr: {
                // Navigation
                nav: {
                    brand: "ZineInsight",
                    tagline: "Data Analytics",
                    about: "À propos",
                    portfolio: "Portfolio",
                    packages: "Packages & Tarifs",
                    contact: "Contact"
                },

                // Hero Section
                hero: {
                    badge: "🚀 Expert Power BI & Data Analytics",
                    title: "Transformez vos données en décisions gagnantes",
                    subtitle: "Spécialiste Power BI pour PME • Dashboards qui boostent votre business • Formations sur-mesure • Résultats garantis sous 7 jours",
                    cta: "Dashboard gratuit",
                    cta_secondary: "Voir mes réalisations"
                },

                // Services Section
                services: {
                    badge: "🎯 Mes Services",
                    title: "Dashboards Power BI qui Boostent Votre Business",
                    subtitle: "Solutions sur-mesure pour PME ambitieuses"
                },

                // Service 1 - Simple Dashboard
                service1: {
                    title: "Dashboard Simple",
                    subtitle: "Dashboard essentiel pour PME. Visualisez vos KPIs clés et prenez des décisions éclairées rapidement.",
                    perfect_for: "📦 Parfait pour :",
                    feature1: "Suivi chiffre d'affaires mensuel",
                    feature2: "Gestion des stocks",
                    feature3: "Performance commerciale",
                    feature4: "KPIs essentiels PME",
                    deliverables: "🎯 Livrables inclus :",
                    deliverable1: "Dashboard Power BI avec 3-5 visuels clés",
                    deliverable2: "Connexion 1-2 sources de données",
                    deliverable3: "Guide utilisateur simple",
                    deliverable4: "Formation de base (1h)",
                    price: "900-1350€",
                    delivery: "Livraison 2-3 jours"
                },

                // Service 2 - Standard Dashboard
                service2: {
                    title: "Dashboard Standard",
                    subtitle: "Solution complète pour PME qui veulent analyser leurs données en profondeur et optimiser leurs performances.",
                    perfect_for: "📦 Parfait pour :",
                    feature1: "Analyse multi-sources (CRM, comptabilité, Excel)",
                    feature2: "Suivi performance clients",
                    feature3: "Pilotage complet de l'activité",
                    feature4: "Tableaux de bord interactifs",
                    deliverables: "🎯 Livrables inclus :",
                    deliverable1: "Dashboard avancé avec 6-10 visuels interactifs",
                    deliverable2: "Connexion 3-4 sources de données",
                    deliverable3: "Filtres croisés et analyse détaillée",
                    deliverable4: "Formation équipe (2h) + documentation",
                    price: "1800-2250€",
                    delivery: "Livraison 4-5 jours",
                    cta: "Devis gratuit"
                },

                // Service 3 - Complex Dashboard
                service3: {
                    title: "Dashboard Complexe",
                    subtitle: "Solution avancée pour PME ambitieuses qui veulent un avantage concurrentiel durable avec leurs données.",
                    perfect_for: "📦 Parfait pour :",
                    feature1: "Analyse prédictive et tendances",
                    feature2: "Alertes automatiques intelligentes",
                    feature3: "Formation équipe complète",
                    feature4: "Intégration 5+ sources de données",
                    deliverables: "🎯 Livrables inclus :",
                    deliverable1: "Dashboard multi-niveaux (direction, managers, équipes)",
                    deliverable2: "Connexion automatisée 5+ sources",
                    deliverable3: "Alertes intelligentes + notifications automatiques",
                    deliverable4: "Formation complète équipe (4h) + support 1 mois",
                    deliverable5: "Documentation technique complète",
                    price: "2700-3600€",
                    delivery: "Livraison 6-8 jours",
                    cta: "Devis gratuit"
                }
            },

            en: {
                // Navigation
                nav: {
                    brand: "ZineInsight",
                    tagline: "Data Analytics",
                    about: "About",
                    portfolio: "Portfolio", 
                    packages: "Packages & Pricing",
                    contact: "Contact"
                },

                // Hero Section
                hero: {
                    badge: "🚀 Power BI & Data Analytics Expert",
                    title: "Transform your data into winning decisions",
                    subtitle: "Power BI Specialist for SMEs • Dashboards that boost your business • Custom training • Results guaranteed in 7 days",
                    cta: "Free dashboard",
                    cta_secondary: "See my work"
                },

                // Services Section
                services: {
                    badge: "🎯 My Services",
                    title: "Power BI Dashboards that Boost Your Business",
                    subtitle: "Custom solutions for ambitious SMEs"
                },

                // Service 1 - Simple Dashboard
                service1: {
                    title: "Simple Dashboard",
                    subtitle: "Essential dashboard for SMEs. Visualize your key KPIs and make informed decisions quickly.",
                    perfect_for: "📦 Perfect for:",
                    feature1: "Monthly revenue tracking",
                    feature2: "Stock management",
                    feature3: "Sales performance",
                    feature4: "Essential SME KPIs",
                    deliverables: "🎯 Included deliverables:",
                    deliverable1: "Power BI dashboard with 3-5 key visuals",
                    deliverable2: "Connection to 1-2 data sources",
                    deliverable3: "Simple user guide",
                    deliverable4: "Basic training (1h)",
                    price: "€900-1350",
                    delivery: "2-3 days delivery"
                },

                // Service 2 - Standard Dashboard
                service2: {
                    title: "Standard Dashboard",
                    subtitle: "Complete solution for SMEs who want to analyze their data in depth and optimize their performance.",
                    perfect_for: "📦 Perfect for:",
                    feature1: "Multi-source analysis (CRM, accounting, Excel)",
                    feature2: "Customer performance tracking",
                    feature3: "Complete activity management",
                    feature4: "Interactive dashboards",
                    deliverables: "🎯 Included deliverables:",
                    deliverable1: "Advanced dashboard with 6-10 interactive visuals",
                    deliverable2: "Connection to 3-4 data sources",
                    deliverable3: "Cross-filters and detailed analysis",
                    deliverable4: "Team training (2h) + documentation",
                    price: "€1800-2250",
                    delivery: "4-5 days delivery",
                    cta: "Free quote"
                },

                // Service 3 - Complex Dashboard
                service3: {
                    title: "Complex Dashboard",
                    subtitle: "Advanced solution for ambitious SMEs who want a lasting competitive advantage with their data.",
                    perfect_for: "📦 Perfect for:",
                    feature1: "Predictive analysis and trends",
                    feature2: "Smart automatic alerts",
                    feature3: "Complete team training",
                    feature4: "5+ data sources integration",
                    deliverables: "🎯 Included deliverables:",
                    deliverable1: "Multi-level dashboard (management, managers, teams)",
                    deliverable2: "Automated connection to 5+ sources",
                    deliverable3: "Smart alerts + automatic notifications",
                    deliverable4: "Complete team training (4h) + 1 month support",
                    deliverable5: "Complete technical documentation",
                    price: "€2700-3600",
                    delivery: "6-8 days delivery",
                    cta: "Free quote"
                }
            }
        };

        this.init();
    }

    init() {
        // Apply saved language preference
        const savedLang = localStorage.getItem('portfolio-language');
        if (savedLang && this.translations[savedLang]) {
            this.currentLanguage = savedLang;
        }

        // Set up language switcher
        this.setupLanguageSwitcher();
        
        // Apply translations
        this.applyTranslations();
    }

    setupLanguageSwitcher() {
        const frBtn = document.getElementById('lang-fr');
        const enBtn = document.getElementById('lang-en');

        console.log('Setting up language switcher...', { frBtn, enBtn });

        if (frBtn && enBtn) {
            // Set initial active state
            if (this.currentLanguage === 'fr') {
                frBtn.classList.add('active');
                enBtn.classList.remove('active');
            } else {
                enBtn.classList.add('active');
                frBtn.classList.remove('active');
            }

            // Add click listeners
            frBtn.addEventListener('click', () => {
                console.log('FR button clicked');
                this.switchLanguage('fr');
            });
            enBtn.addEventListener('click', () => {
                console.log('EN button clicked');
                this.switchLanguage('en');
            });
            
            console.log('Language switcher set up successfully!');
        } else {
            console.error('Language buttons not found!', { frBtn, enBtn });
        }
    }

    switchLanguage(language) {
        console.log('Switching to language:', language);
        
        if (this.translations[language]) {
            this.currentLanguage = language;
            localStorage.setItem('portfolio-language', language);
            
            console.log('Language switched to:', language);
            
            // Update button states
            const frBtn = document.getElementById('lang-fr');
            const enBtn = document.getElementById('lang-en');
            
            if (frBtn && enBtn) {
                if (language === 'fr') {
                    frBtn.classList.add('active');
                    enBtn.classList.remove('active');
                } else {
                    enBtn.classList.add('active');
                    frBtn.classList.remove('active');
                }
                console.log('Button states updated');
            }

            // Apply new translations
            this.applyTranslations();
            console.log('Translations applied');
        } else {
            console.error('Translation not found for language:', language);
        }
    }

    applyTranslations() {
        const elements = document.querySelectorAll('[data-i18n]');
        const currentTranslations = this.translations[this.currentLanguage];

        elements.forEach(element => {
            const key = element.getAttribute('data-i18n');
            const translation = this.getNestedTranslation(currentTranslations, key);
            
            if (translation) {
                element.textContent = translation;
            }
        });
    }

    getNestedTranslation(translations, key) {
        const keys = key.split('.');
        let result = translations;
        
        for (const k of keys) {
            if (result && typeof result === 'object' && k in result) {
                result = result[k];
            } else {
                return null;
            }
        }
        
        return typeof result === 'string' ? result : null;
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    console.log('Portfolio i18n system loading...');
    window.portfolioI18n = new PortfolioI18n();
    console.log('Portfolio i18n system loaded!');
});
