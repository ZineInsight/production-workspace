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
                    contact: "Contact",
                    dashboards: "Dashboards Power BI",
                    quote: "Devis Gratuit",
                    zscore: "ZScore IA"
                },

                // Hero Section
                hero: {
                    badge: "🚀 Expert Power BI & Data Analytics",
                    title: "De la donnée brute à la décision stratégique",
                    subtitle: "10 ans Finance Corporate + Formation Le Wagon Data Science =\nDes dashboards Power BI qui transforment vos données en décisions rentables.",
                    cta: "Audit gratuit de vos données",
                    cta_secondary: "Voir mes réalisations",
                    stats: {
                        delivery: "Livraison garantie",
                        price: "À partir de",
                        specialty: "Spécialiste"
                    }
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
                    delivery: "Livraison 2-3 jours",
                    cta: "Devis gratuit"
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
                },

                // Portfolio Section
                portfolio: {
                    badge: "🚀 Portfolio",
                    title: "Dashboards Power BI & Data Analytics",
                    subtitle: "Applications concrètes développées avec focus sur le ROI business",
                    project1: {
                        title: "Dashboard E-commerce Power BI",
                        description: "Dashboard complet pour e-commerce : CA, ROI, performance produits.",
                        tech1: "Power BI",
                        tech2: "BigQuery",
                        tech3: "E-commerce KPIs",
                        tech4: "ROI Tracking",
                        cta1: "Voir le dashboard",
                        cta2: "Voir le code"
                    },
                    project2: {
                        title: "ZScore Analytics IA / Projet Signature Le Wagon",
                        description: "Simulation à l'aide d'algorithmes pour trouver sa ville idéale.",
                        tech1: "Power BI",
                        tech2: "Scoring IA",
                        badge1: "Simulation Gratuite",
                        badge2: "12 marchés",
                        cta1: "Faire une Simulation",
                        cta2: "Voir le code"
                    },
                    project3: {
                        title: "Dashboard Enterprise / Finance",
                        description: "Dashboard Finance. Etude des risques systèmiques. Conformité réglementaire.",
                        tech1: "Power BI",
                        tech2: "BigQuery",
                        badge1: "Résultats Financiers",
                        badge2: "Etude des risques",
                        cta1: "Voir le dashboard",
                        cta2: "Voir le code"
                    }
                },

                // Testimonials Section
                testimonials: {
                    badge: "💬 Témoignages",
                    title: "Ce que disent les dirigeants PME",
                    subtitle: "Résultats concrets et gains de temps mesurables avec les dashboards Power BI",
                    testimonial1: {
                        text: "Notre suivi des ventes en temps réel nous a fait gagner 2 jours par mois sur les rapports. On voit tout d'un coup d'œil maintenant.",
                        name: "Patrick D.",
                        role: "Gérant SARL - Bâtiment",
                        impact: "Suivi des ventes"
                    },
                    testimonial2: {
                        text: "Fini les tableaux Excel interminables. Nos commerciaux voient leurs objectifs et résultats d'un simple clic. Formation en 2h, c'était parfait.",
                        name: "Marie L.",
                        role: "Directrice - Services B2B",
                        impact: "Suivi des équipes"
                    },
                    testimonial3: {
                        text: "Le tableau de bord nous permet de mieux suivre nos ventes et d'anticiper nos besoins. Nous avons réduit nos ruptures et gagné en sérénité dans la gestion des stocks.",
                        name: "Jean R.",
                        role: "PDG PME - Distribution",
                        impact: "gestion des stocks"
                    }
                },

                // Technology Section
                technology: {
                    badge: "💡 Technologie",
                    title: "Pourquoi choisir Power BI pour vos dashboards business ?",
                    subtitle: "La solution de référence pour transformer vos données en avantage concurrentiel",
                    advantage1: {
                        title: "Écosystème Microsoft",
                        description: "Intégration native avec Office 365, Teams, SharePoint, Azure. Vos équipes utilisent déjà ces outils quotidiennement.",
                        feature1: "Sécurité enterprise (SSO, AD)",
                        feature2: "Collaboration Teams native",
                        feature3: "Gouvernance centralisée"
                    },
                    advantage2: {
                        title: "Performance & Vitesse",
                        description: "Moteur de calcul ultra-rapide, refresh automatique, gestion de millions de lignes sans problème.",
                        feature1: "Refresh automatique planifié",
                        feature2: "Cache intelligent",
                        feature3: "Compression optimisée"
                    },
                    advantage3: {
                        title: "Connectivité Universelle",
                        description: "Plus de 200 connecteurs natifs : SQL, Excel, APIs REST, Google Analytics, Salesforce, BigQuery...",
                        feature1: "BigQuery, PostgreSQL, MySQL",
                        feature2: "APIs REST et Web scraping",
                        feature3: "Excel, CSV, JSON"
                    },
                    advantage4: {
                        title: "Mobile & Cloud",
                        description: "Dashboards responsives, apps mobiles natives, publication cloud avec partage sécurisé.",
                        feature1: "Apps iOS/Android natives",
                        feature2: "Partage sécurisé par liens",
                        feature3: "Alertes push sur mobile"
                    }
                },

                // Contact Section
                contact: {
                    badge: "📧 Contact",
                    title: "Travaillons ensemble",
                    subtitle: "Vous avez un projet data ? Une analyse à réaliser ? Discutons de vos besoins en Data Analytics",
                    card: {
                        title: "Projets Data Analytics",
                        description: "Pipelines data, APIs, tableaux de bord, algorithmes d'analyse"
                    },
                    email: {
                        label: "Email professionnel"
                    },
                    form: {
                        project_placeholder: "Sélectionnez votre besoin",
                        option1: "Analytics & Dashboards",
                        option2: "Pipeline Data & APIs",
                        option3: "Consulting Data Strategy",
                        option4: "Autre projet data",
                        message_label: "Décrivez votre projet",
                        message_placeholder: "Décrivez vos besoins en data analysis, ou tout autre projet data...",
                        submit: "Envoyer"
                    },
                    trust: {
                        response: "Réponse sous 24h",
                        quote: "Devis gratuit"
                    }
                },

                // Footer Section
                footer: {
                    tagline: "Data Analytics Expert",
                    badge1: "Zscore IA",
                    badge2: "DashBoard Power BI - E-commerce",
                    badge3: "DashBoard Power BI - Finance",
                    copyright: "© 2025 ZineInsight. Data Analyst diplômé Le Wagon."
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
                    contact: "Contact",
                    dashboards: "Power BI Dashboards",
                    quote: "Free Quote",
                    zscore: "ZScore AI"
                },

                // Hero Section
                hero: {
                    badge: "🚀 Power BI & Data Analytics Expert",
                    title: "From raw data to strategic decision",
                    subtitle: "10 years Corporate Finance + Le Wagon Data Science Training =\nPower BI dashboards that transform your data into profitable decisions.",
                    cta: "Free data audit",
                    cta_secondary: "See my work",
                    stats: {
                        delivery: "Guaranteed delivery",
                        price: "Starting from",
                        specialty: "Specialist"
                    }
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
                    delivery: "2-3 days delivery",
                    cta: "Free quote"
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
                },

                // Portfolio Section
                portfolio: {
                    badge: "🚀 Portfolio",
                    title: "Power BI Dashboards & Data Analytics",
                    subtitle: "Concrete applications developed with focus on business ROI",
                    project1: {
                        title: "E-commerce Power BI Dashboard",
                        description: "Complete e-commerce dashboard: Revenue, ROI, product performance.",
                        tech1: "Power BI",
                        tech2: "BigQuery",
                        tech3: "E-commerce KPIs",
                        tech4: "ROI Tracking",
                        cta1: "View dashboard",
                        cta2: "View code"
                    },
                    project2: {
                        title: "ZScore Analytics AI / Le Wagon Signature Project",
                        description: "Algorithm-based simulation to find your ideal city.",
                        tech1: "Power BI",
                        tech2: "AI Scoring",
                        badge1: "Free Simulation",
                        badge2: "12 markets",
                        cta1: "Try Simulation",
                        cta2: "View code"
                    },
                    project3: {
                        title: "Enterprise Finance Dashboard",
                        description: "Finance Dashboard. Systemic risk analysis. Regulatory compliance.",
                        tech1: "Power BI",
                        tech2: "BigQuery",
                        badge1: "Financial Results",
                        badge2: "Risk Analysis",
                        cta1: "View dashboard",
                        cta2: "View code"
                    }
                },

                // Testimonials Section
                testimonials: {
                    badge: "💬 Testimonials",
                    title: "What SME leaders say",
                    subtitle: "Concrete results and measurable time savings with Power BI dashboards",
                    testimonial1: {
                        text: "Our real-time sales tracking saved us 2 days a month on reports. We can see everything at a glance now.",
                        name: "Patrick D.",
                        role: "SARL Manager - Construction",
                        impact: "Sales tracking"
                    },
                    testimonial2: {
                        text: "No more endless Excel spreadsheets. Our sales team can see their objectives and results with a simple click. 2-hour training was perfect.",
                        name: "Marie L.",
                        role: "Director - B2B Services",
                        impact: "Team tracking"
                    },
                    testimonial3: {
                        text: "The dashboard allows us to better track our sales and anticipate our needs. We have reduced stockouts and gained peace of mind in inventory management.",
                        name: "Jean R.",
                        role: "SME CEO - Distribution",
                        impact: "inventory management"
                    }
                },

                // Technology Section
                technology: {
                    badge: "💡 Technology",
                    title: "Why choose Power BI for your business dashboards?",
                    subtitle: "The reference solution to transform your data into competitive advantage",
                    advantage1: {
                        title: "Microsoft Ecosystem",
                        description: "Native integration with Office 365, Teams, SharePoint, Azure. Your teams already use these tools daily.",
                        feature1: "Enterprise security (SSO, AD)",
                        feature2: "Native Teams collaboration",
                        feature3: "Centralized governance"
                    },
                    advantage2: {
                        title: "Performance & Speed",
                        description: "Ultra-fast calculation engine, automatic refresh, handling millions of rows without problem.",
                        feature1: "Scheduled automatic refresh",
                        feature2: "Smart cache",
                        feature3: "Optimized compression"
                    },
                    advantage3: {
                        title: "Universal Connectivity",
                        description: "200+ native connectors: SQL, Excel, REST APIs, Google Analytics, Salesforce, BigQuery...",
                        feature1: "BigQuery, PostgreSQL, MySQL",
                        feature2: "REST APIs and Web scraping",
                        feature3: "Excel, CSV, JSON"
                    },
                    advantage4: {
                        title: "Mobile & Cloud",
                        description: "Responsive dashboards, native mobile apps, cloud publishing with secure sharing.",
                        feature1: "Native iOS/Android apps",
                        feature2: "Secure link sharing",
                        feature3: "Mobile push alerts"
                    }
                },

                // Contact Section
                contact: {
                    badge: "📧 Contact",
                    title: "Let's work together",
                    subtitle: "Do you have a data project? An analysis to perform? Let's discuss your Data Analytics needs",
                    card: {
                        title: "Data Analytics Projects",
                        description: "Data pipelines, APIs, dashboards, analysis algorithms"
                    },
                    email: {
                        label: "Professional email"
                    },
                    form: {
                        project_placeholder: "Select your need",
                        option1: "Analytics & Dashboards",
                        option2: "Data Pipeline & APIs",
                        option3: "Data Strategy Consulting",
                        option4: "Other data project",
                        message_label: "Describe your project",
                        message_placeholder: "Describe your data analysis needs, or any other data project...",
                        submit: "Send"
                    },
                    trust: {
                        response: "Response within 24h",
                        quote: "Free quote"
                    }
                },

                // Footer Section
                footer: {
                    tagline: "Data Analytics Expert",
                    badge1: "Zscore AI",
                    badge2: "Power BI Dashboard - E-commerce",
                    badge3: "Power BI Dashboard - Finance",
                    copyright: "© 2025 ZineInsight. Data Analyst Le Wagon graduate."
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
            frBtn.addEventListener('click', () => this.switchLanguage('fr'));
            enBtn.addEventListener('click', () => this.switchLanguage('en'));
        }
    }

    switchLanguage(language) {
        console.log(`🔄 Switching language to: ${language}`);
        
        if (this.translations[language]) {
            this.currentLanguage = language;
            localStorage.setItem('portfolio-language', language);
            
            console.log(`✅ Language switched to: ${language}`);
            
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
                console.log('🔘 Button states updated');
            }

            // Apply new translations
            this.applyTranslations();
        } else {
            console.error(`❌ No translations found for language: ${language}`);
        }
    }

    applyTranslations() {
        const elements = document.querySelectorAll('[data-i18n]');
        const placeholderElements = document.querySelectorAll('[data-i18n-placeholder]');
        const currentTranslations = this.translations[this.currentLanguage];

        console.log(`Applying ${this.currentLanguage} translations to ${elements.length} elements`);

        // Translate text content
        elements.forEach(element => {
            const key = element.getAttribute('data-i18n');
            const translation = this.getNestedTranslation(currentTranslations, key);
            
            if (translation) {
                element.textContent = translation;
                console.log(`✅ ${key}: ${translation}`);
            } else {
                console.warn(`❌ Missing translation for: ${key}`);
            }
        });

        // Translate placeholders
        placeholderElements.forEach(element => {
            const key = element.getAttribute('data-i18n-placeholder');
            const translation = this.getNestedTranslation(currentTranslations, key);
            
            if (translation) {
                element.placeholder = translation;
                console.log(`✅ Placeholder ${key}: ${translation}`);
            } else {
                console.warn(`❌ Missing placeholder translation for: ${key}`);
            }
        });
        
        console.log('Translation application completed!');
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
    window.portfolioI18n = new PortfolioI18n();
});
