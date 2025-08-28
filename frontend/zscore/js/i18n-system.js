/**
 * 🌍 REVOLUTIONARY I18N SYSTEM - CENTRALIZED
 * =============================================
 * Système de traduction unifié pour toute la plateforme
 */

class RevolutionaryI18n {
    constructor() {
        this.currentLanguage = 'fr';
        this.translations = {};
        this.questionTranslations = {};
        this.init();
    }

    init() {
        // Load saved language
        const savedLang = localStorage.getItem('preferred-language') || 'fr';
        this.loadTranslations();
        this.setLanguage(savedLang, false); // Don't translate questions on init
        this.setupEventListeners();
    }

    loadTranslations() {
        // 📝 INTERFACE TRANSLATIONS
        this.translations = {
            fr: {
                // Navigation
                'nav.home': 'Accueil',
                'nav.services': 'Services',
                'nav.about': 'À propos',
                'nav.contact': 'Contact',
                'nav.login': 'Connexion',
                'nav.register': 'S\'inscrire',
                'nav.logout': 'Déconnexion',
                'nav.products': 'Produits',
                'nav.features': 'IA Premium',
                'nav.pricing': 'Tarifs',
                'nav.testimonials': 'Success Stories',

                // User Menu
                'user.dashboard': 'Dashboard',
                'user.profile': 'Profil',
                'user.billing': 'Facturation',
                'user.settings': 'Paramètres',

                // Auth
                'auth.title': 'Authentification | Revolutionary Platform',
                'auth.home': 'Accueil',
                'auth.brand': 'Revolutionary',
                'auth.login.subtitle': 'Connectez-vous à votre compte',
                'auth.register.subtitle': 'Créez votre compte gratuitement',
                'auth.forgot.title': 'Récupération',
                'auth.forgot.subtitle': 'Entrez votre adresse e-mail',
                'auth.email.label': 'Adresse e-mail',
                'auth.email.placeholder': 'votre@email.com',
                'auth.password.label': 'Mot de passe',
                'auth.password.placeholder': '••••••••',
                'auth.login.button': 'Se connecter',
                'auth.register.button': 'Créer mon compte',
                'auth.forgot.button': 'Envoyer le lien',
                'auth.divider': 'ou',
                'auth.forgot.link': 'Mot de passe oublié ?',
                'auth.register.link': 'Pas encore de compte ? ',
                'auth.register.cta': 'Créer un compte',
                'auth.login.link': 'Déjà un compte ? ',
                'auth.login.cta': 'Se connecter',
                'auth.back.link': '← Retour à la connexion',

                // Hero
                'hero.title': 'Révolutionnez Votre Vie avec l\'Intelligence Artificielle',
                'hero.subtitle': 'Notre outil ZScore analyse 30+ critères avec l\'IA pour vous guider vers votre ville idéale. Rejoignez la révolution de l\'expatriation intelligente.',
                // TEMP DÉSACTIVÉ - Stats utilisateurs : 'hero.badge': 'utilisateurs révolutionnent déjà leur vie',
                'hero.badge': 'Nouvelle plateforme IA révolutionnaire',
                'hero.cta.primary': 'Révolutionner ma vie maintenant',
                'hero.cta.secondary': 'Dashboard Premium',
                'hero.trust.text': 'Utilisé par des professionnels de',

                // Stats
                'stats.users': 'Utilisateurs Actifs',
                // TEMP DÉSACTIVÉ - Stats utilisateurs : 'stats.users': 'Utilisateurs',
                'stats.criteria': 'Critères IA',
                'stats.satisfaction': 'Satisfaction',
                'stats.countries': 'Pays Analysés',

                // Products
                'product.zscore.title': 'ZScore Intelligence',
                'product.zscore.subtitle': 'Votre ville parfaite',
                'product.zscore.description': 'Algorithme IA qui analyse 49 critères géographiques pour identifier votre destination idéale.',
                'product.zscore.btn': 'Découvrir ZScore',

                'product.skillgraph.title': 'SkillGraph Intelligence',
                'product.skillgraph.subtitle': 'Votre carrière optimisée',
                'product.skillgraph.description': 'Intelligence qui cartographie vos compétences sur 53 critères pour accélérer votre réussite.',
                'product.skillgraph.btn': 'Découvrir SkillGraph',

                'product.wealth.title': 'Wealth Intelligence',
                'product.wealth.subtitle': 'Votre patrimoine optimisé',
                'product.wealth.description': 'Stratégies d\'investissement premium analysant 46 critères pour maximiser votre richesse.',
                'product.wealth.btn': 'Découvrir Wealth',

                // Product details
                'product.badge.popular': 'Le plus populaire',
                'product.zscore.feature1': '50+ critères d\'analyse IA',
                'product.zscore.feature2': '156 pays & 2000+ villes',
                'product.zscore.feature3': 'Prédiction de bonheur 94% précise',
                'product.zscore.feature4': 'Comparateur coût de vie temps réel',

                // Questionnaire
                'questionnaire.welcome.subtitle': 'Découvrez votre potentiel unique avec notre analyse IA révolutionnaire.<br>Répondez à quelques questions pour révéler les opportunités qui vous attendent.',
                'questionnaire.welcome.start': 'Commencer l\'analyse',
                'questionnaire.parcours.title': '🌍 Choisissez votre parcours',
                'questionnaire.parcours.subtitle': 'Sélectionnez le type d\'analyse qui correspond à vos objectifs',
                'questionnaire.parcours.international.title': 'International',
                'questionnaire.parcours.international.description': 'Analyse générale pour l\'expatriation mondiale',
                'questionnaire.parcours.national.title': 'National',
                'questionnaire.parcours.national.description': 'Analyse spécifique à un pays',
                'questionnaire.country.title': '🗺️ Sélectionnez votre destination',
                'questionnaire.country.subtitle': 'Choisissez le pays pour une analyse personnalisée',
                'questionnaire.country.france': 'France',
                'questionnaire.country.usa': 'États-Unis',
                'questionnaire.country.canada': 'Canada',
                'questionnaire.country.germany': 'Allemagne',
                'questionnaire.country.brazil': 'Brésil',
                'questionnaire.country.italy': 'Italie',
                'questionnaire.country.japan': 'Japon',
                'questionnaire.country.mexico': 'Mexique',
                'questionnaire.country.uk': 'Royaume-Uni',
                'questionnaire.country.australia': 'Australie',
                'questionnaire.country.thailand': 'Thaïlande',
                'questionnaire.country.southafrica': 'Afrique du Sud',
                'questionnaire.country.spain': 'Espagne',
                'questionnaire.country.morocco': 'Maroc',
                'questionnaire.country.argentina': 'Argentine',
                'questionnaire.question.question': 'Question',
                'questionnaire.question.of': 'sur',
                'questionnaire.navigation.previous': 'Précédent',
                'questionnaire.navigation.next': 'Suivant',

                // Results
                'results.meta.title': '🏆 Vos Villes Parfaites - ZineInsight Revolutionary',
                'results.meta.description': 'Découvrez vos 3 villes recommandées selon votre profil personnalisé par l\'intelligence artificielle ZineInsight.',
                'results.header.tagline': 'Intelligence Géographique',
                'results.nav.questionnaire': 'Questionnaire',
                'results.nav.results': 'Résultats',
                'results.nav.about': 'À Propos',
                'results.header.help': 'Aide',
                'results.header.restart': 'Recommencer',
                'results.main.title.prefix': 'Vos',
                'results.main.title.highlight': '3 Villes Parfaites',
                'results.main.subtitle': 'Recommandations basées sur l\'IA propriétaire ZineInsight • Précision 94%',
                'results.main.badge': 'Analyse IA Avancée Complétée',
                'results.main.timestamp': 'Il y a quelques instants',
                'results.podium.title': 'Podium de Vos Villes',
                'results.podium.subtitle': 'Top 3 selon votre profil',
                'results.ai.title': 'Analyse IA de Vos Résultats',
                'results.ai.subtitle': 'Commentaire personnalisé',
                'results.focus.title.suffix': 'en Détail',
                'results.focus.subtitle': 'Votre meilleure recommandation',
                'results.focus.image.placeholder': 'Photo de la ville',
                'results.focus.info.population': 'Population',
                'results.focus.info.cost': 'Coût de vie',
                'results.focus.info.employment': 'Emploi',
                'results.focus.info.culture': 'Culture',
                'results.focus.info.quality': 'Qualité de vie',
                'results.footer.tagline': 'L\'intelligence artificielle au service de vos décisions géographiques',
                'results.footer.stats.cities': 'villes analysées',
                'results.footer.stats.criteria': 'critères par ville',
                'results.footer.stats.countries': 'pays couverts',
                'results.footer.platform.title': 'Plateforme',
                'results.footer.platform.home': 'Accueil',
                'results.footer.platform.questionnaire': 'Questionnaire',
                'results.footer.platform.about': 'À Propos',
                'results.footer.platform.contact': 'Contact',
                'results.footer.legal.title': 'Legal',
                'results.footer.legal.privacy': 'Confidentialité',
                'results.footer.legal.terms': 'Conditions',
                'results.footer.legal.cookies': 'Cookies',
                'results.footer.help.title': 'Aide',
                'results.footer.help.faq': 'FAQ',
                'results.footer.help.support': 'Support',
                'results.footer.help.guides': 'Guides',
                'results.footer.copyright': '© 2025 ZineInsight Revolutionary. Tous droits réservés.',
                'results.footer.made.text': 'Fait avec',
                'results.footer.made.ai': 'et IA révolutionnaire',
                'results.loading.title': 'Chargement de vos résultats...',
                'results.loading.subtitle': 'Analyse de vos données personnalisées',
                'results.payment.title': 'Confirmation d\'Achat',
                'results.payment.cancel': 'Annuler',
                'results.payment.proceed': 'Procéder au Paiement',

                // Modals
                'modal.zscore.title': 'ZScore Intelligence',
                'modal.zscore.h1': 'Intelligence Artificielle Avancée',
                'modal.zscore.p1': 'Notre IA révolutionnaire analyse 49 critères uniques pour chaque ville du monde',
                'modal.zscore.h2': '20+ Pays Analysés',
                'modal.zscore.p2': 'De Paris à Tokyo, de New York à Sydney - découvrez votre ville parfaite',
                'modal.zscore.h3': 'Scoring Personnalisé',
                'modal.zscore.p3': 'Chaque analyse est 100% personnalisée selon votre profil et vos préférences',
                'modal.zscore.h4': 'Révolutionnez Votre Vie',
                'modal.zscore.p4': 'Ne laissez plus le hasard décider - prenez les meilleures décisions avec ZScore',
                'modal.zscore.cta': 'Commencer mon analyse ZScore',

                // Cookies
                'cookies.title': 'Nous respectons votre vie privée',
                'cookies.description': 'Nous utilisons des cookies essentiels pour sauvegarder vos préférences (langue, thème) et améliorer votre expérience. Aucun tracking publicitaire.',
                'cookies.reject': 'Refuser',
                'cookies.customize': 'Personnaliser',
                'cookies.accept': 'Accepter tout',
                'cookies.settings.title': 'Paramètres des cookies',
                'cookies.essential.title': 'Cookies essentiels',
                'cookies.essential.description': 'Nécessaires au fonctionnement du site (langue, sécurité)',
                'cookies.preferences.title': 'Cookies de préférences',
                'cookies.preferences.description': 'Sauvegarde vos choix (langue, thème, paramètres)',
                'cookies.analytics.title': 'Cookies analytiques',
                'cookies.analytics.description': 'Nous aident à améliorer le site (anonymisés)',
                'cookies.cancel': 'Annuler',
                'cookies.save': 'Sauvegarder',

                // Zine AI Coach
                'zine.welcome.index': 'Salut ! Moi c\'est Zine ! 🤖',
                'zine.welcome.questionnaire': 'Hey ! Moi c\'est Zine ! Je vais t\'accompagner 😊',
                'zine.welcome.results': 'Félicitations ! Tes résultats sont prêts ! 🎉',
                'zine.tooltip': 'Zine Assistant',

                // Index page enhanced dynamic messages
                'zine.index.welcome_variants.1': 'Hello ! 🤖 Prêt·e à révolutionner ta vie ? Je suis Zine !',
                'zine.index.welcome_variants.2': 'Salut l\'aventurier·ère ! ✨ Zine ici, ton guide IA personnel !',
                'zine.index.welcome_variants.3': 'Hey ! 🚀 Moi c\'est Zine ! On va trouver ta ville parfaite ?',
                'zine.index.welcome_variants.4': 'Yo ! 🌍 Zine présent ! Prêt pour une aventure internationale ?',

                'zine.index.tips.1': '💡 Le questionnaire ne prend que 3 minutes ! Quick & efficient !',
                'zine.index.tips.2': '🎯 L\'IA analyse 30+ critères pour ton profil parfait !',
                'zine.index.tips.3': '⚡ Déjà 10,000+ personnes ont trouvé leur ville idéale !',
                'zine.index.tips.4': '🌟 100% gratuit, 0% bullshit ! Pure performance IA !',
                'zine.index.tips.5': '🚀 Algorithm révolutionnaire = résultats précis garantis !',
                'zine.index.tips.6': '🏆 Top 3 villes personnalisées selon TON profil unique !',

                'zine.index.scroll_tips.1': '👇 Scroll pour découvrir comment ça marche !',
                'zine.index.scroll_tips.2': '📖 Plus bas : témoignages et stats impressionnantes !',
                'zine.index.scroll_tips.3': '⬇️ Descends voir pourquoi tout le monde adore ZineInsight !',

                'zine.index.cta_motivation.1': '🎯 Ton futur t\'attend ! Clique sur "Commencer" !',
                'zine.index.cta_motivation.2': '⚡ 3 minutes pour changer ta vie ! Let\'s go !',
                'zine.index.cta_motivation.3': '🚀 Ta prochaine aventure commence ici ! Ready ?',

                // Questionnaire dynamic messages
                'zine.questionnaire.ready': 'Prêt(e) pour ton analyse IA ? 🤖 C\'est parti !',
                'zine.questionnaire.comment': 'Salut ! Je vais commenter tes réponses ! 🎯',
                'zine.questionnaire.profile': 'Hey ! Ton profil parfait se construit ici ! ✨',
                'zine.questionnaire.tip_authentic': '💡 Sois authentique, l\'IA détecte tout !',
                'zine.questionnaire.tip_refine': '🎯 Chaque réponse affine ton profil !',
                'zine.questionnaire.tip_precise': '🚀 Plus tu es précis, meilleurs sont les résultats !',
                'zine.questionnaire.tip_analyze': '🔍 L\'IA analyse 30+ critères par réponse !',
                'zine.questionnaire.tip_future': '⚡ Ton futur se dessine question par question !',

                // Results dynamic messages
                'zine.results.congratulations': 'Félicitations ! Tes résultats sont prêts ! 🎉',
                'zine.results.analysis_done': 'Analyse terminée ! Découvre tes villes parfaites ! ✨',
                'zine.results.mission_accomplished': 'Mission accomplie ! Voici ton top 3 personnalisé ! 🏆',
                'zine.results.ai_has_spoken': 'L\'IA a parlé ! Tes destinations idéales t\'attendent ! 🌍',
                'zine.results.tip_click_city': '💡 Clique sur chaque ville pour plus de détails !',
                'zine.results.tip_guide': '🗺️ Le bouton \'Guide\' te donne des infos pratiques !',
                'zine.results.tip_score': '📊 Ton score reflète la compatibilité avec tes critères !',
                'zine.results.tip_retry': '🔄 Tu peux refaire le questionnaire pour comparer !',
                'zine.results.tip_share': '⭐ Partage tes résultats sur les réseaux sociaux !',

                // Results dynamic comments with city/score placeholders
                'zine.results.comment_excellent': '🎯 {city} avec {score}/100 ! Un excellent match pour ton profil !',
                'zine.results.comment_analysis': '✨ Analyse terminée ! {city} sort du lot avec {score}% de compatibilité !',
                'zine.results.comment_top': '🏆 Top résultat : {city} ! L\'IA a détecté une synergie parfaite !',
                'zine.results.comment_first': '🚀 {city} en première position ! Cette ville correspond à tes critères !',
                'zine.results.comment_impressive': '💡 Résultat impressionnant : {city} score {score}/100 selon ton profil !',

                // Commentaires dynamiques questionnaire - parcours_type
                'zine.dynamic.parcours_type.international.1': 'Mindset international ! 🌍 Le monde t\'appartient !',
                'zine.dynamic.parcours_type.international.2': 'Vision globale activée ! 🚀 Excellent choix !',
                'zine.dynamic.parcours_type.international.3': 'Aventurier mondial détecté ! ✈️ C\'est parti !',
                'zine.dynamic.parcours_type.national.1': 'Focus pays spécifique ! 🎯 Stratégie précise !',
                'zine.dynamic.parcours_type.national.2': 'Approche ciblée ! 💡 Smart move !',
                'zine.dynamic.parcours_type.national.3': 'Localisation focused ! 📍 J\'adore !',

                // Commentaires dynamiques questionnaire - age_situation
                'zine.dynamic.age_situation.young_single.1': 'Libre comme l\'air ! 🦅 Tu peux tout oser ! Le monde t\'attend !',
                'zine.dynamic.age_situation.young_single.2': 'Le monde t\'appartient ! 🌍 Fonce ! Zéro limite, maximum liberté !',
                'zine.dynamic.age_situation.young_single.3': 'Aucune limite à tes rêves ! ✨ Prime time pour l\'aventure absolue !',
                'zine.dynamic.age_situation.young_couple.1': 'En duo, vous êtes imbattables ! 💑 Power couple activated !',
                'zine.dynamic.age_situation.young_couple.2': 'Deux cerveaux valent mieux qu\'un ! 🧠 Double énergie, double fun !',
                'zine.dynamic.age_situation.young_couple.3': 'L\'union fait la force ! 💪 Teamwork makes the dream work !',
                'zine.dynamic.age_situation.family_building.1': 'Famille = motivation x1000 ! 👨‍👩‍👧‍👦 Éducation globale pour tous !',
                'zine.dynamic.age_situation.family_building.2': 'Construire pour les siens, noble mission ! 🏗️ Legacy mode: ON !',
                'zine.dynamic.age_situation.family_building.3': 'Vos enfants seront fiers de vous ! 🏆 Citoyens du monde en préparation !',
                'zine.dynamic.age_situation.established.1': 'L\'expérience, ton super-pouvoir ! 💎 Sagesse + nouveaux horizons !',
                'zine.dynamic.age_situation.established.2': 'Sagesse + ambition = combo gagnant ! 🎯 Prime time 2.0 !',
                'zine.dynamic.age_situation.established.3': 'Tu connais tes forces, use-s\'en ! ⚡ Mature mindset, fresh adventure !',

                // Commentaires dynamiques questionnaire - income_level
                'zine.dynamic.income_level.starter.1': 'Tout génie a commencé quelque part ! 🚀 Startup mindset activated !',
                'zine.dynamic.income_level.starter.2': 'L\'important c\'est la progression ! 📈 Growth trajectory engaged !',
                'zine.dynamic.income_level.starter.3': 'Petit budget, grandes ambitions ! 💫 Big dreams, smart strategy !',
                'zine.dynamic.income_level.growing.1': 'Sur la bonne trajectoire ! 🎯 Momentum building, respect !',
                'zine.dynamic.income_level.growing.2': 'Momentum positif détecté ! ⚡ Scaling mode activated !',
                'zine.dynamic.income_level.growing.3': 'Continue, ça paye ! 💰 Investment in yourself pays off !',
                'zine.dynamic.income_level.comfortable.1': 'Bel équilibre financier ! ⚖️ Sweet spot achieved !',
                'zine.dynamic.income_level.comfortable.2': 'Stabilité = liberté de choix ! 🗽 Options unlocked !',
                'zine.dynamic.income_level.comfortable.3': 'Tu géres comme un chef ! 👑 Master of your financial destiny !',
                'zine.dynamic.income_level.high_earner.1': 'Niveau expert débloqué ! 🏆 Elite league member !',
                'zine.dynamic.income_level.high_earner.2': 'Performance financière top ! 💎 Premium lifestyle enabled !',
                'zine.dynamic.income_level.high_earner.3': 'Tu joues dans la cour des grands ! 🎩 Big league player detected !',

                // Commentaires dynamiques questionnaire - priority
                'zine.dynamic.priority.location.1': 'Géolocalisation stratégique ! 🗺️ Location first, everything follows !',
                'zine.dynamic.priority.location.2': 'Le lieu façonne la vie ! 🏙️ Smart choice, bright future !',
                'zine.dynamic.priority.location.3': 'Smart move, l\'emplacement c\'est tout ! 📍 Geographic genius activated !',
                'zine.dynamic.priority.career.1': 'Ambition professionnelle au max ! 💼 Career rocket mode: ON !',
                'zine.dynamic.priority.career.2': 'Carrière first, respect ! 🚀 Professional domination incoming !',
                'zine.dynamic.priority.career.3': 'Le travail, ton terrain de jeu ! ⚡ Success mindset detected !',
                'zine.dynamic.priority.wealth.1': 'Vision patrimoniale claire ! 💰 Money talks, you listen !',
                'zine.dynamic.priority.wealth.2': 'L\'argent travaille pour toi ! 📊 Financial freedom pathway !',
                'zine.dynamic.priority.wealth.3': 'Richesse = liberté ! 🦅 Wealth building champion !',

                // 🎯 ZINE DYNAMIC COMMENTS - LIFESTYLE DETAILED (16 messages - ENHANCED)
                'zine.dynamic.lifestyle_detailed.urban.1': 'Urbain dans l\'âme ! 🏙️ L\'énergie de la ville coule dans tes veines !',
                'zine.dynamic.lifestyle_detailed.urban.2': 'City life = opportunités infinies ! 🌃 Tu vas surfer sur l\'énergie urbaine !',
                'zine.dynamic.lifestyle_detailed.urban.3': 'Le béton, ton habitat naturel ! 🏢 Metropolitan mindset activated !',
                'zine.dynamic.lifestyle_detailed.urban.4': 'Skyline addict detected ! 🏗️ Ton terrain de jeu : la métropole !',

                'zine.dynamic.lifestyle_detailed.suburban.1': 'Équilibre parfait trouvé ! 🏡 Best of both worlds master !',
                'zine.dynamic.lifestyle_detailed.suburban.2': 'Tranquillité + accessibilité ! ✨ Tu as craqué le code du bonheur !',
                'zine.dynamic.lifestyle_detailed.suburban.3': 'Banlieue intelligente ! 🚂 Calme ET connecté, génial !',
                'zine.dynamic.lifestyle_detailed.suburban.4': 'Sweet spot lifestyle ! 🌸 Ni trop, ni trop peu, parfait !',

                'zine.dynamic.lifestyle_detailed.rural.1': 'Nature = ressourcement absolu ! 🌿 Tes poumons vont te remercier !',
                'zine.dynamic.lifestyle_detailed.rural.2': 'Loin de la foule, près de l\'essentiel ! 🍃 Back to basics champion !',
                'zine.dynamic.lifestyle_detailed.rural.3': 'Campagne = qualité de vie premium ! 🌾 Slow life expert !',
                'zine.dynamic.lifestyle_detailed.rural.4': 'Green therapy activated ! 🌳 La nature, ton antistress naturel !',

                'zine.dynamic.lifestyle_detailed.digital_nomad.1': 'Freedom lifestyle unlocked ! 🌍 Le monde comme bureau, respect !',
                'zine.dynamic.lifestyle_detailed.digital_nomad.2': 'Location independence master ! 💻 Tu redéfinis les règles du jeu !',
                'zine.dynamic.lifestyle_detailed.digital_nomad.3': 'Nomade = liberté totale ! ⚡ Ton passeport, ton meilleur ami !',
                'zine.dynamic.lifestyle_detailed.digital_nomad.4': 'Wanderlust + WiFi = combo gagnant ! 🗺️ Adventure meets productivity !',

                // 🌍 ZINE DYNAMIC COMMENTS - DESTINATION COUNTRY (NEW SECTION)
                'zine.dynamic.destination_country.france.1': 'La France ! 🇫🇷 Art de vivre légendaire ! Savoir-vivre premium !',
                'zine.dynamic.destination_country.france.2': 'Baguettes et châteaux ! 🥖 Romantique ! Culture at its finest !',
                'zine.dynamic.destination_country.france.3': 'Hexagone power ! ⚡ Culture et gastronomie ! Excellence française !',
                'zine.dynamic.destination_country.usa.1': 'USA ! 🇺🇸 Land of opportunities ! Dream big, achieve bigger !',
                'zine.dynamic.destination_country.usa.2': 'American Dream activated ! 🦅 Let\'s go ! Freedom + innovation !',
                'zine.dynamic.destination_country.usa.3': 'États-Unis ! 🗽 Innovation et ambition ! The world\'s stage !',
                'zine.dynamic.destination_country.canada.1': 'Canada ! 🇨🇦 Politesse et paysages ! Nature meets civilisation !',
                'zine.dynamic.destination_country.canada.2': 'Eh ! Maple syrup country ! 🍁 Quality of life champion !',
                'zine.dynamic.destination_country.canada.3': 'Great White North ! ❄️ Friendly vibes + stunning landscapes !',
                'zine.dynamic.destination_country.australia.1': 'Australia ! 🇦🇺 Laid-back lifestyle ! G\'day mate, good life !',
                'zine.dynamic.destination_country.australia.2': 'Down Under adventure ! 🦘 Sun, surf, and success !',
                'zine.dynamic.destination_country.australia.3': 'Aussie spirit ! 🌅 Work-life balance perfected !',

                // 🤖 RESULTS PAGE AI COACH MESSAGES - FRENCH
                'zine.results.congratulations': 'Félicitations ! Tes résultats sont prêts ! 🎉',
                'zine.results.analysis_done': 'Analyse terminée ! Découvre tes villes parfaites ! ✨',
                'zine.results.mission_accomplished': 'Mission accomplie ! Voici ton top 3 personnalisé ! 🏆',
                'zine.results.ai_has_spoken': 'L\'IA a parlé ! Tes destinations idéales t\'attendent ! 🌍',
                'zine.results.comment_excellent': '🎯 {city} avec {score}/100 ! Un excellent match pour ton profil !',
                'zine.results.comment_analysis': '✨ Analyse terminée ! {city} sort du lot avec {score}% de compatibilité !',
                'zine.results.comment_top': '🏆 Top résultat : {city} ! L\'IA a détecté une synergie parfaite !',
                'zine.results.comment_first': '🚀 {city} en première position ! Cette ville correspond à tes critères !',
                'zine.results.comment_impressive': '💡 Résultat impressionnant : {city} score {score}/100 selon ton profil !',
                'zine.results.tip_click_city': '💡 Clique sur chaque ville pour plus de détails !',
                'zine.results.tip_guide': '🗺️ Le bouton \'Guide\' te donne des infos pratiques !',
                'zine.results.tip_score': '📊 Ton score reflète la compatibilité avec tes critères !',
                'zine.results.tip_retry': '🔄 Tu peux refaire le questionnaire pour comparer !',
                'zine.results.tip_share': '⭐ Partage tes résultats sur les réseaux sociaux !',

                // 🤖 INDEX PAGE AI COACH MESSAGES - FRENCH
                'zine.welcome.message1': 'Salut ! Je suis Zine, ton coach IA ! 👋',
                'zine.welcome.message2': 'Prêt à découvrir ta ville parfaite ? ✨',
                'zine.welcome.message3': 'Je vais t\'accompagner dans cette aventure ! 🚀',
                'zine.tip.questionnaire': '🎯 Lance le questionnaire pour une analyse personnalisée !',
                'zine.tip.ai_power': '🧠 Mon IA analyse +50 critères pour toi !',
                'zine.tip.worldwide': '🌍 +200 destinations analysées en temps réel !',
                'zine.tip.personalized': '✨ Chaque recommandation est unique à ton profil !',
                'zine.tip.free': '🎁 Analyse gratuite, résultats premium !',
                'zine.tip.speed': '⚡ Questionnaire : 3 minutes, résultats : instantanés !',

                // Footer
                'footer.description': 'Découvrez votre ville idéale grâce à l\'IA.<br>Questionnaire rapide → Top 3 personnalisé → Guide gratuit.<br>Révolutionnez votre expatriation maintenant.',
                'footer.copyright': '© 2025 ZineInsight Revolutionary Platform. Tous droits réservés.'
            },
            en: {
                // Navigation
                'nav.home': 'Home',
                'nav.services': 'Services',
                'nav.about': 'About',
                'nav.contact': 'Contact',
                'nav.login': 'Login',
                'nav.register': 'Register',
                'nav.logout': 'Logout',
                'nav.products': 'Products',
                'nav.features': 'Premium AI',
                'nav.pricing': 'Pricing',
                'nav.testimonials': 'Success Stories',

                // User Menu
                'user.dashboard': 'Dashboard',
                'user.profile': 'Profile',
                'user.billing': 'Billing',
                'user.settings': 'Settings',

                // Auth
                'auth.title': 'Authentication | Revolutionary Platform',
                'auth.home': 'Home',
                'auth.brand': 'Revolutionary',
                'auth.login.subtitle': 'Sign in to your account',
                'auth.register.subtitle': 'Create your free account',
                'auth.forgot.title': 'Recovery',
                'auth.forgot.subtitle': 'Enter your email address',
                'auth.email.label': 'Email address',
                'auth.email.placeholder': 'your@email.com',
                'auth.password.label': 'Password',
                'auth.password.placeholder': '••••••••',
                'auth.login.button': 'Sign in',
                'auth.register.button': 'Create my account',
                'auth.forgot.button': 'Send link',
                'auth.divider': 'or',
                'auth.forgot.link': 'Forgot password?',
                'auth.register.link': 'Don\'t have an account yet? ',
                'auth.register.cta': 'Create an account',
                'auth.login.link': 'Already have an account? ',
                'auth.login.cta': 'Sign in',
                'auth.back.link': '← Back to login',

                // Hero
                'hero.title': 'Revolutionize Your Life with Artificial Intelligence',
                'hero.subtitle': 'Our ZScore tool analyzes 30+ criteria with AI to guide you to your ideal city. Join the smart expatriation revolution.',
                // TEMP DÉSACTIVÉ - Stats utilisateurs : 'hero.badge': 'users are already revolutionizing their lives',
                'hero.badge': 'New revolutionary AI platform',
                'hero.cta.primary': 'Revolutionize my life now',
                'hero.cta.secondary': 'Premium Dashboard',
                'hero.trust.text': 'Used by professionals from',

                // Stats
                'stats.users': 'Active Users',
                // TEMP DÉSACTIVÉ - Stats utilisateurs : 'stats.users': 'Users',
                'stats.criteria': 'AI Criteria',
                'stats.satisfaction': 'Satisfaction',
                'stats.countries': 'Countries Analyzed',

                // Products
                'product.zscore.title': 'ZScore Intelligence',
                'product.zscore.subtitle': 'Your perfect city',
                'product.zscore.description': 'AI algorithm that analyzes 49 geographic criteria to identify your ideal destination.',
                'product.zscore.btn': 'Discover ZScore',

                'product.skillgraph.title': 'SkillGraph Intelligence',
                'product.skillgraph.subtitle': 'Your optimized career',
                'product.skillgraph.description': 'Intelligence that maps your skills across 53 criteria to accelerate your success.',
                'product.skillgraph.btn': 'Discover SkillGraph',

                'product.wealth.title': 'Wealth Intelligence',
                'product.wealth.subtitle': 'Your optimized wealth',
                'product.wealth.description': 'Premium investment strategies analyzing 46 criteria to maximize your wealth.',
                'product.wealth.btn': 'Discover Wealth',

                // Product details
                'product.badge.popular': 'Most Popular',
                'product.zscore.feature1': '50+ AI analysis criteria',
                'product.zscore.feature2': '156 countries & 2000+ cities',
                'product.zscore.feature3': '94% accurate happiness prediction',
                'product.zscore.feature4': 'Real-time cost of living comparator',

                // Questionnaire
                'questionnaire.welcome.subtitle': 'Discover your unique potential with our revolutionary AI analysis.<br>Answer a few questions to reveal the opportunities waiting for you.',
                'questionnaire.welcome.start': 'Start Analysis',
                'questionnaire.parcours.title': '🌍 Choose your path',
                'questionnaire.parcours.subtitle': 'Select the type of analysis that matches your goals',
                'questionnaire.parcours.international.title': 'International',
                'questionnaire.parcours.international.description': 'General analysis for worldwide expatriation',
                'questionnaire.parcours.national.title': 'National',
                'questionnaire.parcours.national.description': 'Country-specific analysis',
                'questionnaire.country.title': '🗺️ Select your destination',
                'questionnaire.country.subtitle': 'Choose the country for a personalized analysis',
                'questionnaire.country.france': 'France',
                'questionnaire.country.usa': 'USA',
                'questionnaire.country.canada': 'Canada',
                'questionnaire.country.germany': 'Germany',
                'questionnaire.country.brazil': 'Brazil',
                'questionnaire.country.italy': 'Italy',
                'questionnaire.country.japan': 'Japan',
                'questionnaire.country.mexico': 'Mexico',
                'questionnaire.country.uk': 'United Kingdom',
                'questionnaire.country.australia': 'Australia',
                'questionnaire.country.thailand': 'Thailand',
                'questionnaire.country.southafrica': 'South Africa',
                'questionnaire.country.spain': 'Spain',
                'questionnaire.country.morocco': 'Morocco',
                'questionnaire.country.argentina': 'Argentina',
                'questionnaire.question.question': 'Question',
                'questionnaire.question.of': 'of',
                'questionnaire.navigation.previous': 'Previous',
                'questionnaire.navigation.next': 'Next',

                // Results
                'results.meta.title': '🏆 Your Perfect Cities - ZineInsight Revolutionary',
                'results.meta.description': 'Discover your 3 recommended cities based on your profile personalized by ZineInsight artificial intelligence.',
                'results.header.tagline': 'Geographic Intelligence',
                'results.nav.questionnaire': 'Questionnaire',
                'results.nav.results': 'Results',
                'results.nav.about': 'About',
                'results.header.help': 'Help',
                'results.header.restart': 'Start Over',
                'results.main.title.prefix': 'Your',
                'results.main.title.highlight': '3 Perfect Cities',
                'results.main.subtitle': 'Recommendations based on proprietary ZineInsight AI • 94% Precision',
                'results.main.badge': 'Advanced AI Analysis Completed',
                'results.main.timestamp': 'A few moments ago',
                'results.podium.title': 'Your Cities Podium',
                'results.podium.subtitle': 'Top 3 according to your profile',
                'results.ai.title': 'AI Analysis of Your Results',
                'results.ai.subtitle': 'Personalized commentary',
                'results.focus.title.suffix': 'in Detail',
                'results.focus.subtitle': 'Your best recommendation',
                'results.focus.image.placeholder': 'City photo',
                'results.focus.info.population': 'Population',
                'results.focus.info.cost': 'Cost of living',
                'results.focus.info.employment': 'Employment',
                'results.focus.info.culture': 'Culture',
                'results.focus.info.quality': 'Quality of life',
                'results.footer.tagline': 'Artificial intelligence serving your geographic decisions',
                'results.footer.stats.cities': 'cities analyzed',
                'results.footer.stats.criteria': 'criteria per city',
                'results.footer.stats.countries': 'countries covered',
                'results.footer.platform.title': 'Platform',
                'results.footer.platform.home': 'Home',
                'results.footer.platform.questionnaire': 'Questionnaire',
                'results.footer.platform.about': 'About',
                'results.footer.platform.contact': 'Contact',
                'results.footer.legal.title': 'Legal',
                'results.footer.legal.privacy': 'Privacy',
                'results.footer.legal.terms': 'Terms',
                'results.footer.legal.cookies': 'Cookies',
                'results.footer.help.title': 'Help',
                'results.footer.help.faq': 'FAQ',
                'results.footer.help.support': 'Support',
                'results.footer.help.guides': 'Guides',
                'results.footer.copyright': '© 2025 ZineInsight Revolutionary. All rights reserved.',
                'results.footer.made.text': 'Made with',
                'results.footer.made.ai': 'and revolutionary AI',
                'results.loading.title': 'Loading your results...',
                'results.loading.subtitle': 'Analyzing your personalized data',
                'results.payment.title': 'Purchase Confirmation',
                'results.payment.cancel': 'Cancel',
                'results.payment.proceed': 'Proceed to Payment',

                // Modals
                'modal.zscore.title': 'ZScore Intelligence',
                'modal.zscore.h1': 'Advanced Artificial Intelligence',
                'modal.zscore.p1': 'Our revolutionary AI analyzes 49 unique criteria for each city worldwide',
                'modal.zscore.h2': '20+ Countries Analyzed',
                'modal.zscore.p2': 'From Paris to Tokyo, from New York to Sydney - discover your perfect city',
                'modal.zscore.h3': 'Personalized Scoring',
                'modal.zscore.p3': 'Each analysis is 100% personalized according to your profile and preferences',
                'modal.zscore.h4': 'Revolutionize Your Life',
                'modal.zscore.p4': 'Don\'t let chance decide - make the best decisions with ZScore',
                'modal.zscore.cta': 'Start my ZScore analysis',

                // Cookies
                'cookies.title': 'We respect your privacy',
                'cookies.description': 'We use essential cookies to save your preferences (language, theme) and improve your experience. No advertising tracking.',
                'cookies.reject': 'Reject',
                'cookies.customize': 'Customize',
                'cookies.accept': 'Accept all',
                'cookies.settings.title': 'Cookie settings',
                'cookies.essential.title': 'Essential cookies',
                'cookies.essential.description': 'Necessary for site functionality (language, security)',
                'cookies.preferences.title': 'Preference cookies',
                'cookies.preferences.description': 'Save your choices (language, theme, settings)',
                'cookies.analytics.title': 'Analytics cookies',
                'cookies.analytics.description': 'Help us improve the site (anonymized)',
                'cookies.cancel': 'Cancel',
                'cookies.save': 'Save',

                // Zine AI Coach
                'zine.welcome.index': 'Hi! I\'m Zine! 🤖',
                'zine.welcome.questionnaire': 'Hey! I\'m Zine! I\'ll guide you 😊',
                'zine.welcome.results': 'Congratulations! Your results are ready! 🎉',
                'zine.tooltip': 'Zine Assistant',

                // Questionnaire dynamic messages
                'zine.questionnaire.ready': 'Ready for your AI analysis? 🤖 Let\'s go!',
                'zine.questionnaire.comment': 'Hi! I\'ll comment on your answers! 🎯',
                'zine.questionnaire.profile': 'Hey! Your perfect profile is being built here! ✨',
                'zine.questionnaire.tip_authentic': '💡 Be authentic, the AI detects everything!',
                'zine.questionnaire.tip_refine': '🎯 Each answer refines your profile!',
                'zine.questionnaire.tip_precise': '🚀 The more precise you are, the better the results!',
                'zine.questionnaire.tip_analyze': '🔍 The AI analyzes 30+ criteria per answer!',
                'zine.questionnaire.tip_future': '⚡ Your future is shaped question by question!',

                // Results dynamic messages
                'zine.results.congratulations': 'Congratulations! Your results are ready! 🎉',
                'zine.results.analysis_done': 'Analysis complete! Discover your perfect cities! ✨',
                'zine.results.mission_accomplished': 'Mission accomplished! Here\'s your personalized top 3! 🏆',
                'zine.results.ai_has_spoken': 'The AI has spoken! Your ideal destinations await! 🌍',
                'zine.results.tip_click_city': '💡 Click on each city for more details!',
                'zine.results.tip_guide': '🗺️ The \'Guide\' button gives you practical info!',
                'zine.results.tip_score': '📊 Your score reflects compatibility with your criteria!',
                'zine.results.tip_retry': '🔄 You can retake the questionnaire to compare!',
                'zine.results.tip_share': '⭐ Share your results on social media!',

                // Results dynamic comments with city/score placeholders
                'zine.results.comment_excellent': '🎯 {city} with {score}/100! An excellent match for your profile!',
                'zine.results.comment_analysis': '✨ Analysis complete! {city} stands out with {score}% compatibility!',
                'zine.results.comment_top': '🏆 Top result: {city}! The AI detected perfect synergy!',
                'zine.results.comment_first': '🚀 {city} in first position! This city matches your criteria!',
                'zine.results.comment_impressive': '💡 Impressive result: {city} scores {score}/100 according to your profile!',

                // Questionnaire dynamic comments - parcours_type
                'zine.dynamic.parcours_type.international.1': 'International mindset! 🌍 The world belongs to you!',
                'zine.dynamic.parcours_type.international.2': 'Global vision activated! 🚀 Excellent choice!',
                'zine.dynamic.parcours_type.international.3': 'World adventurer detected! ✈️ Let\'s go!',
                'zine.dynamic.parcours_type.national.1': 'Specific country focus! 🎯 Precise strategy!',
                'zine.dynamic.parcours_type.national.2': 'Targeted approach! 💡 Smart move!',
                'zine.dynamic.parcours_type.national.3': 'Location focused! 📍 I love it!',

                // Questionnaire dynamic comments - age_situation
                'zine.dynamic.age_situation.young_single.1': 'Free as a bird! 🦅 You can dare anything!',
                'zine.dynamic.age_situation.young_single.2': 'The world belongs to you! 🌍 Go for it!',
                'zine.dynamic.age_situation.young_single.3': 'No limits to your dreams! ✨',
                'zine.dynamic.age_situation.young_couple.1': 'As a duo, you\'re unbeatable! 💑',
                'zine.dynamic.age_situation.young_couple.2': 'Two brains are better than one! 🧠',
                'zine.dynamic.age_situation.young_couple.3': 'Unity makes strength! 💪',
                'zine.dynamic.age_situation.family_building.1': 'Family = motivation x1000! 👨‍👩‍👧‍👦',
                'zine.dynamic.age_situation.family_building.2': 'Building for your loved ones, noble mission! 🏗️',
                'zine.dynamic.age_situation.family_building.3': 'Your children will be proud of you! 🏆',
                'zine.dynamic.age_situation.established.1': 'Experience, your superpower! 💎',
                'zine.dynamic.age_situation.established.2': 'Wisdom + ambition = winning combo! 🎯',
                'zine.dynamic.age_situation.established.3': 'You know your strengths, use them! ⚡',

                // Questionnaire dynamic comments - income_level
                'zine.dynamic.income_level.starter.1': 'Every genius started somewhere! 🚀',
                'zine.dynamic.income_level.starter.2': 'Progress is what matters! 📈',
                'zine.dynamic.income_level.starter.3': 'Small budget, big ambitions! 💫',
                'zine.dynamic.income_level.growing.1': 'On the right trajectory! 🎯',
                'zine.dynamic.income_level.growing.2': 'Positive momentum detected! ⚡',
                'zine.dynamic.income_level.growing.3': 'Keep going, it pays off! 💰',
                'zine.dynamic.income_level.comfortable.1': 'Beautiful financial balance! ⚖️',
                'zine.dynamic.income_level.comfortable.2': 'Stability = freedom of choice! 🗽',
                'zine.dynamic.income_level.comfortable.3': 'You manage like a boss! 👑',
                'zine.dynamic.income_level.high_earner.1': 'Expert level unlocked! 🏆',
                'zine.dynamic.income_level.high_earner.2': 'Top financial performance! 💎',
                'zine.dynamic.income_level.high_earner.3': 'You play in the big leagues! 🎩',

                // Questionnaire dynamic comments - priority
                'zine.dynamic.priority.location.1': 'Strategic geolocation! 🗺️',
                'zine.dynamic.priority.location.2': 'Location shapes life! 🏙️',
                'zine.dynamic.priority.location.3': 'Smart move, location is everything! 📍',
                'zine.dynamic.priority.career.1': 'Professional ambition to the max! 💼',
                'zine.dynamic.priority.career.2': 'Career first, respect! 🚀',
                'zine.dynamic.priority.career.3': 'Work is your playground! ⚡',
                'zine.dynamic.priority.wealth.1': 'Clear wealth vision! 💰',
                'zine.dynamic.priority.wealth.2': 'Money works for you! 📊',
                'zine.dynamic.priority.wealth.3': 'Wealth = freedom! 🦅',

                // Questionnaire dynamic comments - lifestyle_detailed
                'zine.dynamic.lifestyle_detailed.urban.1': 'Urban at heart! 🏙️ Energy +',
                'zine.dynamic.lifestyle_detailed.urban.2': 'City life = opportunities! 🌃',
                'zine.dynamic.lifestyle_detailed.urban.3': 'Concrete is your natural habitat! 🏢',
                'zine.dynamic.lifestyle_detailed.suburban.1': 'Perfect balance found! 🏡',
                'zine.dynamic.lifestyle_detailed.suburban.2': 'Tranquility + accessibility! ✨',
                'zine.dynamic.lifestyle_detailed.suburban.3': 'Smart suburbs! 🚂',
                'zine.dynamic.lifestyle_detailed.rural.1': 'Nature = renewal! 🌿',
                'zine.dynamic.lifestyle_detailed.rural.2': 'Far from crowds, close to essentials! 🍃',
                'zine.dynamic.lifestyle_detailed.rural.3': 'Countryside = quality of life! 🌾',
                'zine.dynamic.lifestyle_detailed.digital_nomad.1': 'Freedom lifestyle! 🌍',
                'zine.dynamic.lifestyle_detailed.digital_nomad.2': 'The world as your office! 💻',
                'zine.dynamic.lifestyle_detailed.digital_nomad.3': 'Nomad = total freedom! ⚡',

                // 🤖 RESULTS PAGE AI COACH MESSAGES
                'zine.results.congratulations': 'Congratulations! Your results are ready! 🎉',
                'zine.results.analysis_done': 'Analysis complete! Discover your perfect cities! ✨',
                'zine.results.mission_accomplished': 'Mission accomplished! Here\'s your personalized top 3! 🏆',
                'zine.results.ai_has_spoken': 'AI has spoken! Your ideal destinations await! 🌍',
                'zine.results.comment_excellent': '🎯 {city} with {score}/100! An excellent match for your profile!',
                'zine.results.comment_analysis': '✨ Analysis complete! {city} stands out with {score}% compatibility!',
                'zine.results.comment_top': '🏆 Top result: {city}! AI detected perfect synergy!',
                'zine.results.comment_first': '🚀 {city} in first position! This city matches your criteria!',
                'zine.results.comment_impressive': '💡 Impressive result: {city} scores {score}/100 for your profile!',
                'zine.results.tip_click_city': '💡 Click on each city for more details!',
                'zine.results.tip_guide': '🗺️ The \'Guide\' button gives you practical info!',
                'zine.results.tip_score': '📊 Your score reflects compatibility with your criteria!',
                'zine.results.tip_retry': '🔄 You can retake the questionnaire to compare!',
                'zine.results.tip_share': '⭐ Share your results on social media!',

                // 🤖 INDEX PAGE AI COACH MESSAGES - ENGLISH
                'zine.welcome.message1': 'Hi! I\'m Zine, your AI coach! 👋',
                'zine.welcome.message2': 'Ready to discover your perfect city? ✨',
                'zine.welcome.message3': 'I\'ll guide you through this adventure! 🚀',
                'zine.tip.questionnaire': '🎯 Launch the questionnaire for personalized analysis!',
                'zine.tip.ai_power': '🧠 My AI analyzes +50 criteria for you!',
                'zine.tip.worldwide': '🌍 +200 destinations analyzed in real-time!',
                'zine.tip.personalized': '✨ Each recommendation is unique to your profile!',
                'zine.tip.free': '🎁 Free analysis, premium results!',
                'zine.tip.speed': '⚡ Questionnaire: 3 minutes, results: instant!',

                // Footer
                // TEMP DÉSACTIVÉ - Stats utilisateurs : 'footer.description': 'Revolutionize your life with the most advanced AI for expatriation and career. Join +2,847 users who have already transformed their future.',
                'footer.description': 'Find your ideal city with AI assistance.<br>Quick questionnaire → Top 3 personalized → Free guide.<br>Revolutionize your expatriation now.',
                'footer.copyright': '© 2025 ZineInsight Revolutionary Platform. All rights reserved.'
            }
        };

        // 🎯 QUESTIONS TRANSLATIONS (Common patterns)
        this.questionTranslations = {
            fr: {
                // Lifestyle patterns
                'lifestyle_expatriation': 'Style de vie expatriation',
                'family_situation': 'Situation familiale',
                'work_preference': 'Préférence travail',
                'climate_preference': 'Préférence climatique',
                'cost_of_living': 'Coût de la vie',
                'career_level': 'Niveau de carrière',
                'wealth_goal': 'Objectif patrimonial',

                // Common options
                'single': 'Célibataire',
                'couple': 'En couple',
                'family': 'Famille',
                'remote': 'Télétravail',
                'office': 'Bureau',
                'hybrid': 'Hybride',
                'warm': 'Chaud',
                'cold': 'Froid',
                'temperate': 'Tempéré',
                'tropical': 'Tropical',
                'low': 'Bas',
                'medium': 'Moyen',
                'high': 'Élevé',
                'junior': 'Junior',
                'senior': 'Senior',
                'expert': 'Expert',
                'security': 'Sécurité',
                'growth': 'Croissance',
                'independence': 'Indépendance'
            },
            en: {
                // Lifestyle patterns
                'lifestyle_expatriation': 'Expatriation lifestyle',
                'family_situation': 'Family situation',
                'work_preference': 'Work preference',
                'climate_preference': 'Climate preference',
                'cost_of_living': 'Cost of living',
                'career_level': 'Career level',
                'wealth_goal': 'Wealth goal',

                // Common options
                'single': 'Single',
                'couple': 'Couple',
                'family': 'Family',
                'remote': 'Remote work',
                'office': 'Office',
                'hybrid': 'Hybrid',
                'warm': 'Warm',
                'cold': 'Cold',
                'temperate': 'Temperate',
                'tropical': 'Tropical',
                'low': 'Low',
                'medium': 'Medium',
                'high': 'High',
                'junior': 'Junior',
                'senior': 'Senior',
                'expert': 'Expert',
                'security': 'Security',
                'growth': 'Growth',
                'independence': 'Independence'
            }
        };
    }

    setLanguage(lang, updateQuestions = true) {
        this.currentLanguage = lang;
        document.documentElement.lang = lang;

        // Store preference
        localStorage.setItem('preferred-language', lang);

        // Update language buttons
        document.querySelectorAll('.lang-btn').forEach(btn => {
            btn.classList.toggle('active', btn.getAttribute('data-lang') === lang);
        });

        // Update interface elements
        this.updateInterface(lang);

        // ⚠️ DÉSACTIVÉ - Analysis.js gère maintenant les traductions des questions
        // Update questions if needed
        // if (updateQuestions) {
        //     this.updateQuestions(lang);
        // }

        // Trigger custom event
        window.dispatchEvent(new CustomEvent('languageChanged', {
            detail: { language: lang }
        }));

        console.log(`🌍 Revolutionary Platform language changed to: ${lang}`);
    }

    updateInterface(lang) {
        // Update meta tags
        const titleMeta = document.querySelector('title[data-i18n]');
        const descMeta = document.querySelector('meta[name="description"][data-i18n]');

        if (titleMeta) {
            const key = titleMeta.getAttribute('data-i18n');
            if (this.translations[lang] && this.translations[lang][key]) {
                titleMeta.textContent = this.translations[lang][key];
            }
        }

        if (descMeta) {
            const key = descMeta.getAttribute('data-i18n');
            if (this.translations[lang] && this.translations[lang][key]) {
                descMeta.setAttribute('content', this.translations[lang][key]);
            }
        }

        // Update all elements with data-i18n
        document.querySelectorAll('[data-i18n]').forEach(el => {
            const key = el.getAttribute('data-i18n');
            if (this.translations[lang] && this.translations[lang][key]) {
                if (this.translations[lang][key].includes('<') || this.translations[lang][key].includes('&')) {
                    el.innerHTML = this.translations[lang][key];
                } else {
                    el.textContent = this.translations[lang][key];
                }
            }
        });
    }

    updateQuestions(lang) {
        // ⚠️ DÉSACTIVÉ - Analysis.js gère maintenant les traductions des questions
        // avec accès direct aux title_en/description_en dans les fichiers de données
        console.log(`🚫 Revolutionary I18n updateQuestions() désactivé - Analysis.js prend le relais`);
        return;

        // Update dynamic question content
        const questionTitle = document.getElementById('questionTitle');
        if (questionTitle && window.currentQuestionData) {
            const translated = this.translateQuestionText(window.currentQuestionData.title, lang);
            questionTitle.textContent = translated;
        }

        // Update question options
        const questionOptions = document.getElementById('questionOptions');
        if (questionOptions && window.currentQuestionData && window.currentQuestionData.options) {
            const options = questionOptions.querySelectorAll('.option-item');
            options.forEach((option, index) => {
                if (window.currentQuestionData.options[index]) {
                    const titleElement = option.querySelector('.option-title');
                    const descElement = option.querySelector('.option-description');

                    if (titleElement) {
                        const translated = this.translateQuestionText(window.currentQuestionData.options[index].title, lang);
                        titleElement.textContent = translated;
                    }

                    if (descElement && window.currentQuestionData.options[index].description) {
                        const translated = this.translateQuestionText(window.currentQuestionData.options[index].description, lang);
                        descElement.textContent = translated;
                    }
                }
            });
        }
    }

    translateQuestionText(text, lang) {
        if (!text || lang === 'fr') return text;

        // Simple pattern-based translation for common terms
        let translated = text;

        // Replace common patterns
        Object.keys(this.questionTranslations.fr).forEach(frKey => {
            const frText = this.questionTranslations.fr[frKey];
            const enText = this.questionTranslations.en[frKey];

            if (translated.includes(frText)) {
                translated = translated.replace(new RegExp(frText, 'gi'), enText);
            }
        });

        return translated;
    }

    setupEventListeners() {
        // Language switcher buttons
        document.addEventListener('click', (e) => {
            if (e.target.classList.contains('lang-btn') || e.target.closest('.lang-btn')) {
                const btn = e.target.classList.contains('lang-btn') ? e.target : e.target.closest('.lang-btn');
                const lang = btn.getAttribute('data-lang');
                if (lang && lang !== this.currentLanguage) {
                    this.setLanguage(lang);
                }
            }
        });

        // ⚠️ DÉSACTIVÉ - Analysis.js gère maintenant les traductions des questions
        // Listen for question changes to update translations
        // window.addEventListener('questionChanged', () => {
        //     if (this.currentLanguage === 'en') {
        //         setTimeout(() => this.updateQuestions('en'), 100);
        //     }
        // });
        console.log(`🚫 Revolutionary I18n event listeners pour questions désactivés`);
    }

    // Utility methods
    t(key) {
        return this.translations[this.currentLanguage]?.[key] || key;
    }

    // 🌍 MAIN TRANSLATE METHOD - Used everywhere
    translate(key, fallback = null, replacements = {}) {
        let translation = this.translations[this.currentLanguage]?.[key];
        translation = translation || fallback || key;

        // Handle variable replacements like {city}, {score}, etc.
        if (replacements && typeof replacements === 'object') {
            Object.keys(replacements).forEach(replaceKey => {
                const placeholder = `{${replaceKey}}`;
                translation = translation.replace(new RegExp(placeholder, 'g'), replacements[replaceKey]);
            });
        }

        return translation;
    }

    getCurrentLanguage() {
        return this.currentLanguage;
    }
}

// 🚀 INITIALIZE GLOBAL I18N SYSTEM
window.revolutionaryI18n = new RevolutionaryI18n();

// Export for modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = RevolutionaryI18n;
}
