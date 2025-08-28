/**
 * 🎯 ANALYSIS.JS - Système de questionnaire intelligent unifié
 * ===========================================================
 * Container dynamique ultra-fluide avec gestion des états
 * Author: Revolutionary Team | Version: 3.0.0 - Smart Container
 */

class ZineInsightAnalysis {
    constructor() {
        // 🎯 État global du questionnaire
        this.state = {
            currentStep: 'parcours',           // parcours | country-selector | questions | analysis
            selectedParcours: null,            // 'international' | 'national'
            selectedCountry: null,             // code du pays (france, usa, etc.)
            currentQuestionIndex: 0,           // index question actuelle
            answers: {},                       // réponses collectées
            questions: [],                     // questions du parcours actuel
            totalQuestions: 0,                 // nombre total de questions
            startTime: null,                   // timestamp début
            navigationHistory: []              // historique pour bouton retour
        };

        // 🎨 Éléments DOM cachés
        this.elements = {};

        this.init();
    }

    // 🚀 INITIALISATION SYSTÈME
    async init() {
        console.log('🎯 Initialisation ZineInsight Analysis v3.0...');

        // Attendre que le DOM soit prêt
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => this.setupSystem());
        } else {
            this.setupSystem();
        }
    }

    // 🔧 CONFIGURATION SYSTÈME
    setupSystem() {
        this.cacheElements();
        this.generateCountryGrid();
        this.setupEventListeners();
        this.initializeFirstStep();

        console.log('✨ ZineInsight Analysis prêt ! État:', this.state);
    }

    // 🗺️ GÉNÉRATION DYNAMIQUE DES PAYS
    generateCountryGrid() {
        const countryGrid = document.querySelector('.country-grid');
        if (!countryGrid || !window.QUESTIONS_DATA) return;

        // Configuration des pays avec drapeaux
        const countries = {
            france: { flag: '🇫🇷', name: 'France' },
            usa: { flag: '🇺🇸', name: 'États-Unis' },
            canada: { flag: '🇨🇦', name: 'Canada' },
            germany: { flag: '🇩🇪', name: 'Allemagne' },
            brazil: { flag: '🇧🇷', name: 'Brésil' },
            italy: { flag: '🇮🇹', name: 'Italie' },
            japan: { flag: '🇯🇵', name: 'Japon' },
            mexico: { flag: '🇲🇽', name: 'Mexique' },
            uk: { flag: '🇬🇧', name: 'Royaume-Uni' },
            australia: { flag: '🇦🇺', name: 'Australie' },
            thailand: { flag: '🇹🇭', name: 'Thaïlande' },
            southafrica: { flag: '🇿🇦', name: 'Afrique du Sud' },
            spain: { flag: '🇪🇸', name: 'Espagne' },
            morocco: { flag: '🇲🇦', name: 'Maroc' },
            argentina: { flag: '🇦🇷', name: 'Argentine' }
        };

        // Générer le HTML pour tous les pays disponibles
        const countryCards = Object.keys(countries)
            .filter(countryCode => window.QUESTIONS_DATA[countryCode]) // Vérifier que les données existent
            .map(countryCode => {
                const country = countries[countryCode];
                return `
                    <div class="country-card" data-country="${countryCode}">
                        <div class="country-flag">${country.flag}</div>
                        <h3 class="country-name" data-i18n="questionnaire.country.${countryCode}">${country.name}</h3>
                    </div>
                `;
            }).join('');

        countryGrid.innerHTML = countryCards;
        console.log(`🗺️ ${Object.keys(countries).length} pays générés dynamiquement`);
    }

    // 📦 CACHE DES ÉLÉMENTS DOM
    cacheElements() {
        this.elements = {
            // Container principal
            dynamicContainer: document.getElementById('dynamicQuestionContainer'),

            // Steps
            stepParcours: document.getElementById('parcoursSection'),
            stepCountrySelector: document.getElementById('countrySection'),
            stepQuestions: document.getElementById('questionsSection'),
            stepAnalysis: document.getElementById('step-analysis'),

            // Progress bar - Complete version
            progressBar: document.getElementById('progressBar'),
            progressPercent: document.getElementById('progressPercent'),
            currentStep: document.getElementById('currentStep'),
            currentQuestion: document.getElementById('currentQuestion'),
            totalQuestions: document.getElementById('totalQuestions'),

            // Questions zone
            questionsTitle: document.getElementById('questionsTitle'),
            questionsSubtitle: document.getElementById('questionsSubtitle'),
            questionText: document.getElementById('questionTitle'),
            questionOptions: document.getElementById('questionOptions'),
            nextQuestionBtn: document.getElementById('nextQuestionBtn'),
            backBtn: document.getElementById('backToCountryOrParcours'),

            // Time
            timeRemaining: document.querySelectorAll('#timeRemaining')
        };

        console.log('📦 Éléments DOM cachés:', Object.keys(this.elements).length);
    }

    // 🎮 ÉVÉNEMENTS GLOBAUX
    setupEventListeners() {
        // Délégation d'événements sur le container principal
        document.addEventListener('click', (e) => {
            const optionCard = e.target.closest('.option-card');
            const parcoursCard = e.target.closest('.parcours-card');
            const countryCard = e.target.closest('.country-card');
            const backButton = e.target.closest('.back-button');
            const nextButton = e.target.closest('#nextQuestionBtn');

            if (parcoursCard) {
                this.handleParcoursClick(parcoursCard, e);
            } else if (countryCard) {
                this.handleCountryClick(countryCard, e);
            } else if (optionCard) {
                this.handleOptionClick(optionCard, e);
            } else if (backButton) {
                this.handleBackClick(backButton, e);
            } else if (nextButton && !nextButton.disabled) {
                this.handleNextQuestion();
            }
        });

        // Keyboard navigation
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') this.handleBackClick();
            if (e.key === 'Enter' && this.state.currentStep === 'questions') this.handleNextQuestion();
        });

        // 🌍 Language change listener for question translation
        window.addEventListener('languageChanged', (e) => {
            console.log('🌍 Language changed, refreshing current question...');
            // Add a small delay to ensure language change is fully processed
            setTimeout(() => {
                // Refresh current question display if we're in questions step
                if (this.state.currentStep === 'questions' && this.state.questions && this.state.currentQuestionIndex < this.state.questions.length) {
                    this.displayCurrentQuestion();
                }
            }, 100); // 100ms delay to ensure language is fully updated
        });
    }

    // 🎬 INITIALISATION PREMIÈRE ÉTAPE
    initializeFirstStep() {
        // Masquer l'écran de bienvenue
        const welcomeScreen = document.getElementById('welcomeScreen');
        if (welcomeScreen) {
            welcomeScreen.style.display = 'none';
        }

        this.state.startTime = Date.now();
        this.showStep('parcours');
        this.updateProgress();
    }

    // 📍 NAVIGATION ENTRE ÉTAPES
    showStep(stepName) {
        console.log(`🎬 Transition vers: ${stepName}`);

        // Masquer toutes les étapes
        ['parcours', 'country-selector', 'questions', 'analysis'].forEach(step => {
            let element;
            if (step === 'parcours') element = this.elements.stepParcours;
            else if (step === 'country-selector') element = this.elements.stepCountrySelector;
            else if (step === 'questions') element = this.elements.stepQuestions;
            else if (step === 'analysis') element = this.elements.stepAnalysis;

            if (element) {
                element.style.display = 'none';
                element.classList.remove('active');
            }
        });

        // Afficher l'étape courante avec animation
        let currentElement;
        if (stepName === 'parcours') currentElement = this.elements.stepParcours;
        else if (stepName === 'country-selector') currentElement = this.elements.stepCountrySelector;
        else if (stepName === 'questions') currentElement = this.elements.stepQuestions;
        else if (stepName === 'analysis') currentElement = this.elements.stepAnalysis;

        if (currentElement) {
            currentElement.style.display = 'block';
            setTimeout(() => currentElement.classList.add('active'), 50);
        }

        this.state.currentStep = stepName;
        this.updateProgress();
    }

    // 📊 MISE À JOUR BARRE DE PROGRESSION
    updateProgress() {
        const progressSteps = {
            'parcours': {
                percent: 0,
                text: '1 sur 4',
                label: 'Choix du parcours',
                questionText: 'Sélection en cours...'
            },
            'country-selector': {
                percent: 0,
                text: '2 sur 4',
                label: 'Sélection du pays',
                questionText: 'Sélection en cours...'
            },
            'questions': {
                percent: (this.state.currentQuestionIndex / Math.max(this.state.totalQuestions, 1)) * 100,
                text: '3 sur 4',
                label: 'Questionnaire',
                questionText: `Question ${this.state.currentQuestionIndex + 1} sur ${this.state.totalQuestions}`
            },
            'analysis': {
                percent: 100,
                text: '4 sur 4',
                label: 'Analyse terminée',
                questionText: 'Analyse complète !'
            }
        };

        const progress = progressSteps[this.state.currentStep];

        if (progress) {
            // Barre de progression
            if (this.elements.progressBar) {
                this.elements.progressBar.style.width = `${progress.percent}%`;
            }

            // Pourcentage
            if (this.elements.progressPercent) {
                this.elements.progressPercent.textContent = `${Math.round(progress.percent)}%`;
            }

            // Questions spécifiques (uniquement pour l'étape questions)
            if (this.state.currentStep === 'questions') {
                if (this.elements.currentQuestion) {
                    this.elements.currentQuestion.textContent = this.state.currentQuestionIndex + 1;
                }
                if (this.elements.totalQuestions) {
                    this.elements.totalQuestions.textContent = this.state.totalQuestions;
                }
            }
        }

        // Mise à jour temps estimé
        this.updateTimeRemaining();
    }

    // ⏱️ TEMPS RESTANT ESTIMÉ
    updateTimeRemaining() {
        const timeEstimates = {
            'parcours': '~3 min',
            'country-selector': '~2 min',
            'questions': `~${Math.ceil((this.state.totalQuestions - this.state.currentQuestionIndex) * 0.2)} min`,
            'analysis': '~30 sec'
        };

        const timeText = timeEstimates[this.state.currentStep] || '~2 min';
        this.elements.timeRemaining.forEach(el => el.textContent = timeText);
    }

    // 🛤️ GESTION CLIC SUR PARCOURS
    handleParcoursClick(parcoursCard, event) {
        event.preventDefault();

        const parcours = parcoursCard.dataset.parcours;
        console.log(`🎯 Parcours sélectionné: ${parcours}`);

        if (parcours) {
            this.handleParcoursChoice(parcours);
        }
    }

    // 🗺️ GESTION CLIC SUR PAYS
    handleCountryClick(countryCard, event) {
        event.preventDefault();

        const countryCode = countryCard.dataset.country;
        console.log(`🌍 Pays sélectionné: ${countryCode}`);

        if (countryCode) {
            this.handleCountryChoice(countryCode);
        }
    }

    // 🎯 GESTION CLIC SUR OPTION
    handleOptionClick(optionCard, event) {
        event.preventDefault();

        const choice = optionCard.dataset.choice;
        const nextStep = optionCard.dataset.nextStep;
        const answer = optionCard.dataset.answer;

        console.log('🎯 Option cliquée:', { choice, nextStep, answer, step: this.state.currentStep });

        // Feedback visuel immédiat
        this.selectOptionCard(optionCard);

        if (this.state.currentStep === 'parcours') {
            this.handleParcoursChoice(choice, nextStep);
        } else if (this.state.currentStep === 'country-selector') {
            this.handleCountryChoice(choice);
        } else if (this.state.currentStep === 'questions') {
            this.handleQuestionAnswer(optionCard, answer);
        }
    }

    // ✨ SÉLECTION VISUELLE OPTION
    selectOptionCard(selectedCard) {
        // Désélectionner toutes les autres
        selectedCard.parentNode.querySelectorAll('.option-card').forEach(card => {
            card.classList.remove('selected');
        });

        // Sélectionner la carte cliquée
        selectedCard.classList.add('selected');

        // Animation de feedback
        selectedCard.style.transform = 'scale(1.02)';
        setTimeout(() => {
            selectedCard.style.transform = '';
        }, 200);
    }

    // 🛤️ CHOIX DU PARCOURS
    handleParcoursChoice(parcours, nextStep) {
        this.state.selectedParcours = parcours;
        this.addToHistory('parcours');

        if (parcours === 'international') {
            // 🌍 PARCOURS INTERNATIONAL = MONDE ENTIER
            this.state.selectedCountry = 'world';
            this.loadQuestions('international');
            this.showStep('questions');
        } else if (parcours === 'national') {
            // Aller au choix du pays
            this.showStep('country-selector');
        }
    }

    // 🏳️ CHOIX DU PAYS
    handleCountryChoice(countryCode) {
        this.state.selectedCountry = countryCode;
        this.addToHistory('country-selector');

        this.loadQuestions(countryCode);
        this.showStep('questions');
    }

    // 📚 CHARGEMENT DES QUESTIONS
    loadQuestions(type) {
        if (!window.QUESTIONS_DATA || !window.QUESTIONS_DATA[type]) {
            console.error('❌ Questions non trouvées pour:', type);
            return;
        }

        this.state.questions = window.QUESTIONS_DATA[type];
        this.state.totalQuestions = this.state.questions.length;
        this.state.currentQuestionIndex = 0;
        this.state.answers = {};

        console.log(`📚 Questions chargées pour ${type}:`, this.state.questions.length);

        // Mise à jour de l'interface
        this.updateQuestionsHeader(type);
        this.displayCurrentQuestion();
        this.updateProgress(); // Force update après reset de currentQuestionIndex
    }

    // 🏷️ MISE À JOUR EN-TÊTE QUESTIONNAIRE
    updateQuestionsHeader(type) {
        const headers = {
            international: {
                title: '🌍 Questions Expatriation Internationale',
                subtitle: 'Questions universelles pour optimiser votre expatriation'
            },
            france: {
                title: '🇫🇷 Questions France - Optimisation Locale',
                subtitle: 'Questions spécifiques pour optimiser votre vie en France'
            },
            usa: {
                title: '🇺🇸 Questions USA - American Dream',
                subtitle: 'Questions spécialisées pour votre aventure américaine'
            },
            canada: {
                title: '🇨🇦 Questions Canada - Great North',
                subtitle: 'Questions spécialisées pour votre aventure canadienne'
            },
            uk: {
                title: '�🇧 Questions UK - British Life',
                subtitle: 'Questions spécialisées pour votre vie au Royaume-Uni'
            },
            germany: {
                title: '🇩🇪 Questions Germany - Deutsche Leben',
                subtitle: 'Questions spécialisées pour votre vie en Allemagne'
            },
            australia: {
                title: '🇦🇺 Questions Australia - Aussie Life',
                subtitle: 'Questions spécialisées pour votre vie en Australie'
            },
            spain: {
                title: '🇪🇸 Questions Spain - Vida Española',
                subtitle: 'Questions spécialisées pour votre vie en Espagne'
            },
            mexico: {
                title: '🇲🇽 Questions Mexico - Vida Mexicana',
                subtitle: 'Questions spécialisées pour votre aventure mexicaine'
            }
            // ... autres pays
        };

        const header = headers[type] || { title: '📋 Questionnaire personnalisé', subtitle: 'Questions adaptées à votre profil' };

        if (this.elements.questionsTitle) {
            this.elements.questionsTitle.textContent = header.title;
        }
        if (this.elements.questionsSubtitle) {
            this.elements.questionsSubtitle.textContent = header.subtitle;
        }
    }

    // ❓ AFFICHAGE QUESTION COURANTE
    displayCurrentQuestion() {
        const question = this.state.questions[this.state.currentQuestionIndex];

        if (!question) {
            console.error('❌ Question introuvable à l\'index:', this.state.currentQuestionIndex);
            return;
        }

        // Store current question data globally for i18n
        window.currentQuestionData = question;

        // 🌍 Check current language and use appropriate translation
        const currentLang = window.revolutionaryI18n ? window.revolutionaryI18n.currentLanguage : 'fr';

        console.log('🔍 DEBUG Translation System:', {
            revolutionaryI18n: !!window.revolutionaryI18n,
            currentLanguage: currentLang,
            metaTranslationSystem: !!window.metaTranslationSystem,
            questionTitle: question.title,
            hasEnglishTitle: !!question.title_en,
            englishTitle: question.title_en
        });

        // Mise à jour texte de la question avec traduction
        if (this.elements.questionText) {
            let questionTitle = question.title;

            // Use English translation if available and language is English
            if (currentLang === 'en' && question.title_en) {
                questionTitle = question.title_en;
                console.log('🌍 Translation applied:', question.title, '→', questionTitle);
            } else if (currentLang === 'fr') {
                console.log('🇫🇷 Using French (original):', questionTitle);
            } else {
                console.log('⚠️ No translation found for language:', currentLang);
            }

            console.log('📝 Final question text set to:', questionTitle);
            this.elements.questionText.textContent = questionTitle;
        }

        // Génération des options
        this.generateQuestionOptions(question.options);

        // Désactiver le bouton suivant
        if (this.elements.nextQuestionBtn) {
            this.elements.nextQuestionBtn.disabled = true;
            this.elements.nextQuestionBtn.classList.add('disabled');
        }

        this.updateProgress();

        // 🌍 Trigger event for i18n system
        window.dispatchEvent(new CustomEvent('questionChanged', {
            detail: {
                question: question,
                index: this.state.currentQuestionIndex
            }
        }));
    }

    // 🎨 GÉNÉRATION OPTIONS QUESTION
    generateQuestionOptions(options) {
        if (!this.elements.questionOptions || !options) return;

        // 🌍 Check current language for translations
        const currentLang = window.revolutionaryI18n ? window.revolutionaryI18n.currentLanguage : 'fr';

        console.log('🔍 DEBUG Options Translation:', {
            revolutionaryI18n: !!window.revolutionaryI18n,
            currentLanguage: currentLang,
            metaTranslationSystem: !!window.metaTranslationSystem,
            optionsCount: options.length
        });

        console.log('🌍 Translating options...');

        const html = options.map(option => {
            let optionTitle = option.title;
            let optionDescription = option.description;

            // Use English translations if available and language is English
            if (currentLang === 'en') {
                if (option.title_en) {
                    optionTitle = option.title_en;
                    console.log('🔄 Option:', option.title, '→', optionTitle);
                }
                if (option.description_en) {
                    optionDescription = option.description_en;
                }
            }

            return `
                <div class="option-card" data-answer="${option.value}">
                    <div class="option-icon">${option.icon}</div>
                    <h4 class="option-title">${optionTitle}</h4>
                    <p class="option-description">${optionDescription}</p>
                </div>
            `;
        }).join('');

        this.elements.questionOptions.innerHTML = html;

        // Add class to options for easier i18n targeting
        this.elements.questionOptions.querySelectorAll('.option-card').forEach(optionEl => {
            optionEl.classList.add('option-item');
        });
    }

    // ✅ GESTION RÉPONSE QUESTION
    handleQuestionAnswer(optionCard, answer) {
        const question = this.state.questions[this.state.currentQuestionIndex];

        // Enregistrer la réponse
        this.state.answers[question.id] = answer;

        // Activer le bouton suivant
        if (this.elements.nextQuestionBtn) {
            this.elements.nextQuestionBtn.disabled = false;
            this.elements.nextQuestionBtn.classList.remove('disabled');
        }

        console.log('✅ Réponse enregistrée:', question.id, answer);

        // Auto-advance après un délai
        setTimeout(() => {
            this.handleNextQuestion();
        }, 800); // Délai de 800ms pour voir la sélection
    }

    // ➡️ QUESTION SUIVANTE
    handleNextQuestion() {
        this.state.currentQuestionIndex++;

        if (this.state.currentQuestionIndex >= this.state.totalQuestions) {
            // Questionnaire terminé
            this.finishQuestionnaire();
        } else {
            // Question suivante
            this.displayCurrentQuestion();
        }
    }

    // 🏁 FIN DU QUESTIONNAIRE
    finishQuestionnaire() {
        console.log('🏁 Questionnaire terminé ! Réponses:', this.state.answers);

        this.showStep('analysis');

        // Simuler l'analyse IA
        setTimeout(() => {
            this.processAnalysis();
        }, 3000);
    }

    // 🧠 TRAITEMENT ANALYSE IA - CONNEXION API RÉELLE
    async processAnalysis() {
        try {
            console.log('🧠 🔥 DEBUG MAX: Connexion API backend en cours...');

            // 📊 Collecter toutes les réponses du questionnaire
            const answers = this.collectAllAnswers();
            const country = this.state.selectedCountry || 'france';
            const parcours = this.state.selectedParcours;

            console.log('📤 🔥 DEBUG MAX: Envoi vers API:', { answers, country, parcours });
            console.log('📤 🔥 DEBUG MAX: Nombre de réponses:', Object.keys(answers).length);
            console.log('📤 🔥 DEBUG MAX: Détail réponses:', JSON.stringify(answers, null, 2));

            // 🇺🇸🇫🇷 ADAPTER LES DONNÉES POUR LES APIS SPÉCIALISÉES
            let requestPayload;
            if (this.state.selectedCountry === 'usa') {
                console.log('🇺🇸 🔥 DEBUG MAX: Adaptation des réponses pour API USA...');
                requestPayload = this.adaptAnswersForUSA(answers);
                console.log('🇺🇸 🔥 DEBUG MAX: Payload adapté pour USA:', requestPayload);
            } else if (this.state.selectedCountry === 'france') {
                console.log('🇫🇷 🔥 DEBUG MAX: Adaptation des réponses pour API France...');
                requestPayload = this.adaptAnswersForFrance(answers);
                console.log('🇫🇷 🔥 DEBUG MAX: Payload adapté pour France:', requestPayload);
            } else if (this.state.selectedCountry === 'canada') {
                console.log('🇨🇦 🔥 DEBUG MAX: Adaptation des réponses pour API Canada...');
                requestPayload = this.adaptAnswersForCanada(answers);
                console.log('🇨🇦 🔥 DEBUG MAX: Payload adapté pour Canada:', requestPayload);
            } else if (this.state.selectedCountry === 'australia') {
                console.log('🇦🇺 🔥 DEBUG MAX: Adaptation des réponses pour API Australia...');
                requestPayload = this.adaptAnswersForAustralia(answers);
                console.log('🇦🇺 🔥 DEBUG MAX: Payload adapté pour Australia:', requestPayload);
            } else if (this.state.selectedCountry === 'spain') {
                console.log('🇪🇸 🔥 DEBUG MAX: Adaptation des réponses pour API Spain...');
                requestPayload = this.adaptAnswersForSpain(answers);
                console.log('🇪🇸 🔥 DEBUG MAX: Payload adapté pour Spain:', requestPayload);
            } else if (this.state.selectedCountry === 'mexico') {
                console.log('🇲🇽 🔥 DEBUG MAX: Adaptation des réponses pour API Mexico...');
                requestPayload = this.adaptAnswersForMexico(answers);
                console.log('🇲🇽 🔥 DEBUG MAX: Payload adapté pour Mexico:', requestPayload);
            } else if (this.state.selectedCountry === 'brazil') {
                console.log('🇧🇷 🔥 DEBUG MAX: Adaptation des réponses pour API Brazil...');
                requestPayload = this.adaptAnswersForBrazil(answers);
                console.log('🇧🇷 🔥 DEBUG MAX: Payload adapté pour Brazil:', requestPayload);
            } else if (this.state.selectedCountry === 'japan') {
                console.log('🇯🇵 🔥 DEBUG MAX: Adaptation des réponses pour API Japan...');
                requestPayload = this.adaptAnswersForJapan(answers);
                console.log('🇯🇵 🔥 DEBUG MAX: Payload adapté pour Japan:', requestPayload);
            } else if (this.state.selectedCountry === 'morocco') {
                console.log('🇲🇦 🔥 DEBUG MAX: Adaptation des réponses pour API Morocco...');
                requestPayload = this.adaptAnswersForMorocco(answers);
                console.log('🇲🇦 🔥 DEBUG MAX: Payload adapté pour Morocco:', requestPayload);
            } else if (this.state.selectedCountry === 'thailand') {
                console.log('🇹🇭 🔥 DEBUG MAX: Adaptation des réponses pour API Thailand...');
                requestPayload = this.adaptAnswersForThailand(answers);
                console.log('🇹🇭 🔥 DEBUG MAX: Payload adapté pour Thailand:', requestPayload);
            } else {
                requestPayload = { answers, country };
            }

            // 🚀 APPEL API BACKEND - AVEC CONFIGURATION ENVIRONNEMENT
            console.log('🚀 🔥 DEBUG MAX: Détection environnement...');

            // Utiliser la configuration d'environnement
            const envConfig = new EnvironmentConfig();
            const apiBaseUrl = envConfig.config.apiBaseUrl;

            // Choisir l'endpoint selon le parcours
            let apiUrl;
            if (this.state.selectedCountry === 'usa') {
                apiUrl = `${apiBaseUrl}/usa-residents/recommendations`;
                console.log('🇺🇸 🔥 DEBUG MAX: Utilisation endpoint USA Residents');
            } else if (this.state.selectedCountry === 'france') {
                apiUrl = `${apiBaseUrl}/france-residents/recommendations`;
                console.log('🇫🇷 🔥 DEBUG MAX: Utilisation endpoint France Residents');
            } else if (this.state.selectedCountry === 'canada') {
                apiUrl = `${apiBaseUrl}/canada-residents/recommendations`;
                console.log('🇨🇦 🔥 DEBUG MAX: Utilisation endpoint Canada Residents');
            } else if (this.state.selectedCountry === 'uk') {
                apiUrl = `${apiBaseUrl}/uk-residents/recommendations`;
                console.log('🇬🇧 🔥 DEBUG MAX: Utilisation endpoint UK Residents');
            } else if (this.state.selectedCountry === 'japan') {
                apiUrl = `${apiBaseUrl}/japan-residents/recommendations`;
                console.log('🇯🇵 🔥 DEBUG MAX: Utilisation endpoint Japan Residents');
            } else if (this.state.selectedCountry === 'morocco') {
                apiUrl = `${apiBaseUrl}/morocco-residents/recommendations`;
                console.log('🇲🇦 🔥 DEBUG MAX: Utilisation endpoint Morocco Residents');
            } else if (this.state.selectedCountry === 'thailand') {
                apiUrl = `${apiBaseUrl}/thailand-residents/recommendations`;
                console.log('🇹🇭 🔥 DEBUG MAX: Utilisation endpoint Thailand Residents');
            } else if (this.state.selectedCountry === 'germany') {
                apiUrl = `${apiBaseUrl}/germany-residents/recommendations`;
                console.log('🇩🇪 🔥 DEBUG MAX: Utilisation endpoint Germany Residents');
            } else if (this.state.selectedCountry === 'australia') {
                apiUrl = `${apiBaseUrl}/australia-residents/recommendations`;
                console.log('🇦🇺 🔥 DEBUG MAX: Utilisation endpoint Australia Residents');
            } else if (this.state.selectedCountry === 'spain') {
                apiUrl = `${apiBaseUrl}/spain-residents/recommendations`;
                console.log('🇪🇸 🔥 DEBUG MAX: Utilisation endpoint Spain Residents');
                console.log('🔍 🇪🇸 DEBUG: Payload complet à envoyer:', JSON.stringify(requestPayload, null, 2));
                console.log('🔍 🇪🇸 DEBUG: Nombre de clés dans le payload:', Object.keys(requestPayload).length);
                Object.entries(requestPayload).forEach(([key, value]) => {
                    console.log(`🔍 🇪🇸 DEBUG: ${key} = ${value}`);
                });
            } else if (this.state.selectedCountry === 'brazil') {
                apiUrl = `${apiBaseUrl}/brazil-residents/recommendations`;
                console.log('🇧🇷 🔥 DEBUG MAX: Utilisation endpoint Brazil Residents');
                console.log('🔍 🇧🇷 DEBUG: Payload complet à envoyer:', JSON.stringify(requestPayload, null, 2));
                console.log('🔍 🇧🇷 DEBUG: Nombre de clés dans le payload:', Object.keys(requestPayload).length);
                Object.entries(requestPayload).forEach(([key, value]) => {
                    console.log(`🔍 🇧🇷 DEBUG: ${key} = ${value}`);
                });
            } else if (this.state.selectedCountry === 'mexico') {
                apiUrl = `${apiBaseUrl}/mexico-residents/recommendations`;
                console.log('🇲🇽 🔥 DEBUG MAX: Utilisation endpoint Mexico Residents');
                console.log('🔍 🇲🇽 DEBUG: Payload complet à envoyer:', JSON.stringify(requestPayload, null, 2));
                console.log('🔍 🇲🇽 DEBUG: Nombre de clés dans le payload:', Object.keys(requestPayload).length);
                Object.entries(requestPayload).forEach(([key, value]) => {
                    console.log(`🔍 🇲🇽 DEBUG: ${key} = ${value}`);
                });
            } else {
                apiUrl = `${apiBaseUrl}/calculate`;
                console.log('🌍 🔥 DEBUG MAX: Utilisation endpoint standard');
            }

            console.log('🚀 🔥 DEBUG MAX: Environment:', envConfig.environment);
            console.log('🚀 🔥 DEBUG MAX: API Base URL:', apiBaseUrl);
            console.log('🚀 🔥 DEBUG MAX: Full API URL:', apiUrl);

            const response = await fetch(apiUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(requestPayload)
            });

            console.log('📡 🔥 DEBUG MAX: Response status:', response.status);
            console.log('📡 🔥 DEBUG MAX: Response ok:', response.ok);

            if (!response.ok) {
                console.error('❌ 🔥 DEBUG MAX: Erreur HTTP:', response.status, response.statusText);
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            console.log('📥 🔥 DEBUG MAX: Parsing JSON...');
            const results = await response.json();
            console.log('✅ 🔥 DEBUG MAX: Résultats API reçus:', results);

            // DEBUG SPÉCIFIQUE SPAIN
            if (this.state.selectedCountry === 'spain') {
                console.log('🔍 🇪🇸 DEBUG: === ANALYSE RÉPONSE API SPAIN ===');
                console.log('🔍 🇪🇸 DEBUG: results.status =', results.status);
                console.log('🔍 🇪🇸 DEBUG: results.recommendations =', results.recommendations);
                console.log('🔍 🇪🇸 DEBUG: Longueur recommendations =', results.recommendations?.length);
                console.log('🔍 🇪🇸 DEBUG: Type recommendations =', typeof results.recommendations);
                console.log('🔍 🇪🇸 DEBUG: recommendations est un Array =', Array.isArray(results.recommendations));
                if (results.recommendations && Array.isArray(results.recommendations)) {
                    console.log('🔍 🇪🇸 DEBUG: DÉTAIL de chaque recommandation:');
                    results.recommendations.forEach((rec, i) => {
                        console.log(`🔍 🇪🇸 DEBUG: Recommandation ${i + 1}:`, rec);
                        console.log(`🔍 🇪🇸 DEBUG:   - city: ${rec.city}`);
                        console.log(`🔍 🇪🇸 DEBUG:   - region: ${rec.region}`);
                        console.log(`🔍 🇪🇸 DEBUG:   - score_percentage: ${rec.score_percentage}`);
                        console.log(`🔍 🇪🇸 DEBUG:   - score: ${rec.score}`);
                    });
                }
                console.log('🔍 🇪🇸 DEBUG: === FIN ANALYSE SPAIN ===');
            }
            console.log('✅ � DEBUG MAX: Type de results:', typeof results);
            console.log('✅ 🔥 DEBUG MAX: Clés de results:', Object.keys(results));
            console.log('�🔍 🔥 DEBUG MAX: recommendations brutes:', results.recommendations);
            console.log('🔍 🔥 DEBUG MAX: Type de recommendations:', typeof results.recommendations);
            console.log('🔍 🔥 DEBUG MAX: results.success:', results.success);
            console.log('🔍 🔥 DEBUG MAX: Boolean results.success:', !!results.success);
            console.log('🔍 🔥 DEBUG MAX: results.status:', results.status);

            // Support des deux formats d'API : success (USA/International) et status:'success' (France)
            const isSuccessful = results.success || results.status === 'success';
            console.log('🔍 🔥 DEBUG MAX: isSuccessful final:', isSuccessful);

            if (isSuccessful && results.recommendations) {
                console.log('🎯 🔥 DEBUG MAX: Condition success ET recommendations = TRUE');

                // 🔧 HELPER FUNCTION: Extract recommendations array from API response
                const extractRecommendations = (results) => {
                    let recommendations = [];
                    
                    if (results.recommendations && Array.isArray(results.recommendations)) {
                        // Format direct : results.recommendations est déjà un tableau
                        recommendations = results.recommendations;
                        console.log('✅ Using direct recommendations array');
                    } else if (results.recommendations && results.recommendations.recommendations && Array.isArray(results.recommendations.recommendations)) {
                        // Format imbriqué : results.recommendations.recommendations est le tableau
                        recommendations = results.recommendations.recommendations;
                        console.log('✅ Using nested recommendations.recommendations array');
                    } else if (results.recommendations && typeof results.recommendations === 'object') {
                        // Tentative de trouver un tableau quelque part dans l'objet
                        const keys = Object.keys(results.recommendations);
                        for (const key of keys) {
                            if (Array.isArray(results.recommendations[key])) {
                                recommendations = results.recommendations[key];
                                console.log(`✅ Using recommendations.${key} array`);
                                break;
                            }
                        }
                    }
                    
                    console.log('📊 Extracted recommendations count:', recommendations.length);
                    return recommendations;
                };

                // Adapter la structure selon le type d'API (USA vs International)
                console.log('🔄 🔥 DEBUG MAX: Début adaptation des données...');
                let adaptedRecommendations;

                if (this.state.selectedCountry === 'usa') {
                    // Format USA Residents API
                    console.log('🇺🇸 🔥 DEBUG MAX: Adaptation format USA Residents');
                    
                    const usaRecommendations = extractRecommendations(results);
                    if (usaRecommendations.length > 0) {
                        console.log('🎯 🔥 DEBUG MAX: AVANT tri - ordre API USA:', usaRecommendations.map(c => `${c.city}, ${c.state}: ${c.score_percentage}%`));
                    }

                    adaptedRecommendations = usaRecommendations.map(city => ({
                        nom: city.city,
                        pays: city.state,
                        score_final: Math.round(city.score_percentage),
                        points_forts: city.top_strengths || ['Excellente qualité de vie', 'Bonnes opportunités', 'Environnement agréable'],
                        population: city.population ? city.population.toLocaleString() : 'Non disponible',
                        cout_vie: Math.round(city.score_percentage * 0.85),
                        emploi: Math.round(city.score_percentage * 0.90),
                        culture: Math.round(city.score_percentage * 0.88),
                        qualite_vie: Math.round(city.score_percentage),
                        why_recommended: city.why_recommended || `${city.city}, ${city.state} est parfaite pour votre profil.`,
                        country_id: city.country_id || 'us'  // 🆔 Ajouter le country_id
                    }))
                        .sort((a, b) => b.score_final - a.score_final);
                } else if (this.state.selectedCountry === 'france') {
                    // Format France Residents API
                    console.log('🇫🇷 🔥 DEBUG MAX: Adaptation format France Residents');
                    
                    const franceRecommendations = extractRecommendations(results);
                    if (franceRecommendations.length > 0) {
                        console.log('🎯 🔥 DEBUG MAX: AVANT tri - ordre API France:', franceRecommendations.map(c => `${c.city}, ${c.region}: ${c.score_percentage}%`));
                    }

                    adaptedRecommendations = franceRecommendations.map(city => ({
                        nom: city.city,
                        pays: city.region,
                        score_final: Math.round(city.score_percentage),
                        points_forts: city.top_strengths || ['Excellent cadre de vie', 'Bonnes opportunités', 'Richesse culturelle'],
                        population: city.population ? city.population.toLocaleString() : 'Non disponible',
                        cout_vie: Math.round(city.score_percentage * 0.85),
                        emploi: Math.round(city.score_percentage * 0.90),
                        culture: Math.round(city.score_percentage * 0.92),
                        qualite_vie: Math.round(city.score_percentage),
                        why_recommended: city.why_recommended || `${city.city} (${city.region}) est parfaite pour votre profil français.`,
                        country_id: city.country_id || 'fr'  // 🆔 Ajouter le country_id
                    }))
                        .sort((a, b) => b.score_final - a.score_final);
                } else if (this.state.selectedCountry === 'canada') {
                    // Format Canada Residents API
                    console.log('🇨🇦 🔥 DEBUG MAX: Adaptation format Canada Residents');
                    
                    const canadaRecommendations = extractRecommendations(results);
                    if (canadaRecommendations.length > 0) {
                        console.log('🎯 🔥 DEBUG MAX: AVANT tri - ordre API Canada:', canadaRecommendations.map(c => `${c.city}, ${c.province}: ${c.score_percentage}%`));
                    }

                    adaptedRecommendations = canadaRecommendations.map(city => ({
                        nom: city.city,
                        pays: city.province,
                        score_final: Math.round(city.score_percentage),
                        points_forts: city.top_strengths || ['Excellent système de santé', 'Bonnes opportunités', 'Qualité de vie remarquable'],
                        population: city.population ? city.population.toLocaleString() : 'Non disponible',
                        cout_vie: Math.round(city.score_percentage * 0.88),
                        emploi: Math.round(city.score_percentage * 0.87),
                        culture: Math.round(city.score_percentage * 0.85),
                        qualite_vie: Math.round(city.score_percentage),
                        why_recommended: city.why_recommended || `${city.city} (${city.province}) est parfaite pour votre profil canadien.`,
                        country_id: city.country_id || 'ca'  // 🆔 Ajouter le country_id
                    }))
                        .sort((a, b) => b.score_final - a.score_final);
                } else if (this.state.selectedCountry === 'uk') {
                    // Format UK Residents API
                    console.log('🇬🇧 🔥 DEBUG MAX: Adaptation format UK Residents');
                    
                    const ukRecommendations = extractRecommendations(results);
                    if (ukRecommendations.length > 0) {
                        console.log('🎯 🔥 DEBUG MAX: AVANT tri - ordre API UK:', ukRecommendations.map(c => `${c.city}, ${c.region}: ${c.score_percentage}%`));
                    }

                    adaptedRecommendations = ukRecommendations.map(city => ({
                        nom: city.city,
                        pays: city.region,
                        score_final: Math.round(city.score_percentage),
                        points_forts: city.top_strengths || ['Excellent NHS', 'Rich cultural heritage', 'Great opportunities'],
                        population: city.population ? city.population.toLocaleString() : 'Non disponible',
                        cout_vie: Math.round(city.score_percentage * 0.83),
                        emploi: Math.round(city.score_percentage * 0.89),
                        culture: Math.round(city.score_percentage * 0.93),
                        qualite_vie: Math.round(city.score_percentage),
                        why_recommended: city.why_recommended || `${city.city} (${city.region}) is perfect for your UK profile.`,
                        country_id: city.country_id || 'uk'  // 🆔 Ajouter le country_id
                    }))
                        .sort((a, b) => b.score_final - a.score_final);
                } else if (this.state.selectedCountry === 'japan') {
                    // Format Japan Residents API
                    console.log('🇯🇵 🔥 DEBUG MAX: Adaptation format Japan Residents');
                    console.log('🔍 🇯🇵 DEBUG: Réponse API complète Japan:', results);
                    console.log('🔍 🇯🇵 DEBUG: Nb de recommandations reçues:', results.recommendations?.length);
                    console.log('🔍 🇯🇵 DEBUG: Status de la réponse:', results.status);
                    console.log('🔍 🇯🇵 DEBUG: Détail des recommandations:');
                    results.recommendations?.forEach((city, index) => {
                        console.log(`   ${index + 1}. ${city.city} (${city.region}) - Score: ${city.score_percentage}% - Raw score: ${city.score}`);
                        console.log(`      Population: ${city.population}, Top strengths:`, city.top_strengths);
                    });
                    const japanRecommendations = extractRecommendations(results);
                    if (japanRecommendations.length > 0) {
                        console.log('🎯 🔥 DEBUG MAX: AVANT tri - ordre API Japan:', japanRecommendations.map(c => `${c.city}, ${c.region}: ${c.score_percentage}%`));
                    }

                    adaptedRecommendations = results.recommendations.map(city => ({
                        nom: city.city,
                        pays: city.region,
                        score_final: Math.round(city.score_percentage),
                        points_forts: city.top_strengths || ['Excellent infrastructure', 'Rich cultural heritage', 'Great work opportunities'],
                        population: city.population ? city.population.toLocaleString() : 'Non disponible',
                        cout_vie: Math.round(city.score_percentage * 0.81),
                        emploi: Math.round(city.score_percentage * 0.87),
                        culture: Math.round(city.score_percentage * 0.95),
                        qualite_vie: Math.round(city.score_percentage),
                        why_recommended: city.why_recommended || `${city.city} (${city.region}) est parfait pour votre profil japonais.`
                    }))
                        .sort((a, b) => b.score_final - a.score_final);
                } else if (this.state.selectedCountry === 'morocco') {
                    // Format Morocco Residents API - Les données arrivent déjà formatées !
                    console.log('🇲🇦 🔥 DEBUG MAX: Morocco API - données déjà formatées');
                    console.log('🔍 🇲🇦 DEBUG: Réponse API complète Morocco:', results);
                    console.log('🔍 🇲🇦 DEBUG: Nb de recommandations reçues:', results.recommendations?.length);
                    console.log('🔍 🇲🇦 DEBUG: Status de la réponse:', results.status);
                    console.log('🔍 🇲🇦 DEBUG: Détail première recommandation:', results.recommendations?.[0]);

                    // L'API Morocco retourne déjà le format final avec nom, pays, score_final
                    // Pas besoin de re-mapping, juste prendre les données telles quelles
                    adaptedRecommendations = results.recommendations || [];

                    console.log('🎯 🔥 DEBUG MAX: Recommendations Morocco directes:', adaptedRecommendations);
                    console.log('🎯 🔥 DEBUG MAX: Premier élément:', adaptedRecommendations[0]);
                } else if (this.state.selectedCountry === 'germany') {
                    // Format Germany Residents API - STRUCTURE IMBRIQUÉE
                    console.log('🇩🇪 🔥 DEBUG MAX: Adaptation format Germany Residents');
                    
                    // 🔧 FIX: Les recommandations sont dans results.recommendations.recommendations
                    let germanyRecommendations = [];
                    if (results.recommendations && Array.isArray(results.recommendations)) {
                        // Format direct : results.recommendations est déjà un tableau
                        germanyRecommendations = results.recommendations;
                        console.log('✅ Using direct recommendations array');
                    } else if (results.recommendations && results.recommendations.recommendations && Array.isArray(results.recommendations.recommendations)) {
                        // Format imbriqué : results.recommendations.recommendations est le tableau
                        germanyRecommendations = results.recommendations.recommendations;
                        console.log('✅ Using nested recommendations.recommendations array');
                    } else {
                        console.error('❌ No valid recommendations array found in results.recommendations');
                        germanyRecommendations = [];
                    }
                    
                    console.log('🎯 🔥 DEBUG MAX: Germany recommendations found:', germanyRecommendations.length);
                    if (germanyRecommendations.length > 0) {
                        console.log('🎯 🔥 DEBUG MAX: AVANT tri - ordre API Germany:', germanyRecommendations.map(c => `${c.city}, ${c.region}: ${c.score_percentage}%`));
                    }

                    adaptedRecommendations = germanyRecommendations.map(city => ({
                        nom: city.city,
                        pays: city.region,
                        score_final: Math.round(city.score_percentage),
                        points_forts: city.top_strengths || ['Excellent infrastructure', 'Strong economy', 'High quality of life'],
                        population: city.population ? city.population.toLocaleString() : 'Non disponible',
                        cout_vie: Math.round(city.score_percentage * 0.78),
                        emploi: Math.round(city.score_percentage * 0.92),
                        culture: Math.round(city.score_percentage * 0.88),
                        qualite_vie: Math.round(city.score_percentage),
                        why_recommended: city.why_recommended || `${city.city} (${city.region}) ist perfekt für Ihr deutsches Profil.`,
                        country_id: city.country_id || 'de'  // 🆔 Ajouter le country_id
                    }))
                        .sort((a, b) => b.score_final - a.score_final);
                } else if (this.state.selectedCountry === 'australia') {
                    // Format Australia Residents API (hybrid approach)
                    console.log('🇦🇺 🔥 DEBUG MAX: Adaptation format Australia Residents');
                    const australiaRecommendations = extractRecommendations(results);
                    if (australiaRecommendations.length > 0) {
                        console.log('🎯 🔥 DEBUG MAX: AVANT tri - ordre API Australia:', australiaRecommendations.map(c => `${c.city}, ${c.state}: ${c.score_percentage}%`));
                    }

                    adaptedRecommendations = results.recommendations.map(city => ({
                        nom: city.city,
                        pays: city.state,
                        score_final: Math.round(city.score_percentage),
                        points_forts: city.top_criteria?.map(c => c.criteria).join(', ') || 'Perfect Australian lifestyle match',
                        population: city.population ? city.population.toLocaleString() : 'Non disponible',
                        cout_vie: Math.round(city.score_percentage * 0.75), // Cost of living generally higher in Australia
                        emploi: Math.round(city.score_percentage * 0.90),   // Strong job markets
                        culture: Math.round(city.score_percentage * 0.85),  // Multicultural diversity
                        qualite_vie: Math.round(city.score_percentage),
                        why_recommended: city.why_recommended || `${city.city} offers the perfect blend of Australian lifestyle and opportunities.`
                    }))
                        .sort((a, b) => b.score_final - a.score_final);
                } else if (this.state.selectedCountry === 'spain') {
                    // Format Spain Residents API (hybrid residents/expats approach)
                    console.log('🇪🇸 🔥 DEBUG MAX: Adaptation format Spain Residents');
                    console.log('🔍 🇪🇸 DEBUG: Réponse API complète Spain:', results);
                    console.log('🔍 🇪🇸 DEBUG: Nb de recommandations reçues:', results.recommendations?.length);
                    console.log('🔍 🇪🇸 DEBUG: Status de la réponse:', results.status);
                    console.log('🔍 🇪🇸 DEBUG: Détail des recommandations:');
                    results.recommendations?.forEach((city, index) => {
                        console.log(`   ${index + 1}. ${city.city} (${city.region}) - Score: ${city.score_percentage}% - Raw score: ${city.score}`);
                        console.log(`      Population: ${city.population}, Insights:`, city.insights);
                    });
                    const spainRecommendations = extractRecommendations(results);
                    if (spainRecommendations.length > 0) {
                        console.log('🎯 🔥 DEBUG MAX: AVANT tri - ordre API Spain:', spainRecommendations.map(c => `${c.city}, ${c.region}: ${c.score_percentage}%`));
                    }

                    adaptedRecommendations = results.recommendations.map(city => ({
                        nom: city.city,
                        pays: city.region,
                        score_final: Math.round(city.score_percentage),
                        points_forts: city.insights?.lifestyle || 'Excellent qualité de vie espagnole',
                        population: city.population ? city.population.toLocaleString() : 'Non disponible',
                        cout_vie: Math.round(city.score_percentage * 0.80), // Reasonable cost of living in Spain
                        emploi: Math.round(city.score_percentage * 0.75),   // Job market varies by region
                        culture: Math.round(city.score_percentage * 0.95),  // Rich Spanish culture
                        qualite_vie: Math.round(city.score_percentage),
                        why_recommended: city.insights?.culture || `${city.city} offre un parfait équilibre entre culture espagnole et opportunités modernes.`
                    }))
                        .sort((a, b) => b.score_final - a.score_final);
                } else if (this.state.selectedCountry === 'mexico') {
                    // Format Mexico Residents API (hybrid residents/expats approach)
                    console.log('🇲🇽 🔥 DEBUG MAX: Adaptation format Mexico Residents');
                    console.log('🔍 🇲🇽 DEBUG: Réponse API complète Mexico:', results);
                    console.log('🔍 🇲🇽 DEBUG: Nb de recommandations reçues:', results.recommendations?.length);
                    console.log('🔍 🇲🇽 DEBUG: Status de la réponse:', results.status);
                    console.log('🔍 🇲🇽 DEBUG: Détail des recommandations:');
                    results.recommendations?.forEach((city, index) => {
                        console.log(`   ${index + 1}. ${city.nom} (${city.region}) - Score: ${city.score_final} - Zone: ${city.zone}`);
                        console.log(`      Population: ${city.population}, Points forts:`, city.points_forts);
                    });
                    const mexicoRecommendations = extractRecommendations(results);
                    if (mexicoRecommendations.length > 0) {
                        console.log('🎯 🔥 DEBUG MAX: AVANT tri - ordre API Mexico:', mexicoRecommendations.map(c => `${c.nom}: ${c.score_final}`));
                    }

                    adaptedRecommendations = results.recommendations.map(city => ({
                        nom: city.nom,
                        pays: city.region || 'México',
                        score_final: Math.round(city.score_final),
                        points_forts: city.points_forts || city.highlights || ['Charme mexicain authentique'],
                        population: city.population || 'Non disponible',
                        cout_vie: Math.round(city.cout_vie || city.score_final * 50), // Coût vie en pesos convertis
                        emploi: Math.round(city.score_final * 0.80),   // Job market varies by region
                        culture: Math.round(city.score_final * 0.95),  // Rich Mexican culture
                        qualite_vie: Math.round(city.score_final),
                        why_recommended: city.why_recommended || `${city.nom} offre un parfait équilibre entre culture mexicaine et opportunités modernes.`
                    }))
                        .sort((a, b) => b.score_final - a.score_final);
                } else if (this.state.selectedCountry === 'brazil') {
                    // Format Brazil Residents API (residents/expats inclusive approach)
                    console.log('🇧🇷 🔥 DEBUG MAX: Adaptation format Brazil Residents');
                    console.log('🔍 🇧🇷 DEBUG: Réponse API complète Brazil:', results);
                    console.log('🔍 🇧🇷 DEBUG: Nb de recommandations reçues:', results.recommendations?.length);
                    console.log('🔍 🇧🇷 DEBUG: Status de la réponse:', results.status);
                    console.log('🔍 🇧🇷 DEBUG: User profile summary:', results.metadata?.user_profile_summary);
                    console.log('🔍 🇧🇷 DEBUG: Détail des recommandations:');
                    results.recommendations?.forEach((city, index) => {
                        console.log(`   ${index + 1}. ${city.city} (${city.region}) - Score: ${city.score_percentage}% - Population: ${city.population}`);
                        console.log(`      Coordonnées: [${city.coordinates}]`);
                    });
                    const brazilRecommendations = extractRecommendations(results);
                    if (brazilRecommendations.length > 0) {
                        console.log('🎯 🔥 DEBUG MAX: AVANT tri - ordre API Brazil:', brazilRecommendations.map(c => `${c.city}: ${c.score_percentage}%`));
                    }

                    adaptedRecommendations = results.recommendations.map(city => ({
                        nom: city.city,
                        pays: city.region,
                        score_final: Math.round(city.score_percentage),
                        points_forts: this.generateBrazilCityStrengths(city.city, city.region, city.detailed_scores),
                        population: city.population ? city.population.toLocaleString() : 'Non disponible',
                        cout_vie: Math.round((city.detailed_scores?.cost_of_living || 0.7) * 100), // Brazilian cost of living
                        emploi: Math.round((city.detailed_scores?.job_opportunities || 0.7) * 100),   // Job market varies by region
                        culture: Math.round((city.detailed_scores?.cultural_scene || 0.8) * 100),  // Rich Brazilian culture
                        qualite_vie: Math.round(city.score_percentage),
                        coordinates: city.coordinates,
                        why_recommended: this.generateBrazilRecommendationReason(city.city, city.region, city.detailed_scores, results.metadata?.user_profile_summary)
                    }))
                        .sort((a, b) => b.score_final - a.score_final);
                } else if (this.state.selectedCountry === 'thailand') {
                    // Format Thailand Residents API - Les données arrivent déjà formatées !
                    console.log('🇹🇭 🔥 DEBUG MAX: Thailand API - données déjà formatées');
                    console.log('🔍 🇹🇭 DEBUG: Réponse API complète Thailand:', results);
                    console.log('🔍 🇹🇭 DEBUG: Nb de recommandations reçues:', results.recommendations?.length);
                    console.log('🔍 🇹🇭 DEBUG: Status de la réponse:', results.status);
                    console.log('🔍 🇹🇭 DEBUG: Détail première recommandation:', results.recommendations?.[0]);

                    // L'API Thailand retourne déjà le format final avec nom, pays, score_final
                    // Pas besoin de re-mapping, juste prendre les données telles quelles
                    adaptedRecommendations = results.recommendations || [];

                    console.log('🎯 🔥 DEBUG MAX: Recommendations Thailand directes:', adaptedRecommendations);
                    console.log('🎯 🔥 DEBUG MAX: Premier élément:', adaptedRecommendations[0]);
                } else {
                    // Format International API
                    console.log('🌍 🔥 DEBUG MAX: Adaptation format International');
                    console.log('🎯 🔥 DEBUG MAX: AVANT tri - ordre API International:', results.recommendations.map(c => `${c.city}: ${Math.round(c.compatibility)}%`));

                    adaptedRecommendations = results.recommendations.map(city => ({
                        nom: city.city,
                        pays: city.country,
                        score_final: Math.round(city.compatibility),
                        points_forts: this.generateCityStrengths(city.city, city.country),
                        population: 'Non disponible',
                        cout_vie: Math.round(city.score * 100),
                        emploi: Math.round(city.compatibility * 0.8),
                        culture: Math.round(city.compatibility * 0.9),
                        qualite_vie: Math.round(city.compatibility)
                    }))
                        .sort((a, b) => b.score_final - a.score_final);
                }

                console.log('🔄 🔥 DEBUG MAX: Données adaptées:', adaptedRecommendations);
                console.log('🏆 🔥 DEBUG MAX: APRÈS tri - ordre final:', adaptedRecommendations.slice(0, 5).map(c => `${c.nom}: ${c.score_final}%`));

                // Stocker les résultats pour la page suivante
                console.log('💾 🔥 DEBUG MAX: Stockage dans localStorage...');
                localStorage.setItem('zineinsight_results', JSON.stringify({
                    recommendations: adaptedRecommendations,
                    country: country,
                    questionnaire: answers,
                    timestamp: Date.now(),
                    success: true,
                    selectedCountry: country,
                    questionsAnswered: Object.keys(answers).length,
                    analysisDate: new Date().toISOString(),
                    matchPercentage: Math.round(results.recommendations[0]?.compatibility || 85),
                    keyCriteria: this.extractKeyCriteria(answers)
                }));

                // Store questionnaire answers separately
                console.log('💾 🔥 DEBUG MAX: Stockage questionnaire answers...');
                localStorage.setItem('questionnaire_answers', JSON.stringify({
                    responses: answers,
                    selectedCountry: country
                }));

                console.log('🎉 🔥 DEBUG MAX: Redirection vers results.html...');
                // Redirection vers les vrais résultats
                window.location.href = '/results.html?completed=true';
            } else {
                console.error('❌ 🔥 DEBUG MAX: Condition success ET recommendations = FALSE');
                console.error('❌ 🔥 DEBUG MAX: results.success:', results.success);
                console.error('❌ 🔥 DEBUG MAX: results.status:', results.status);
                console.error('❌ 🔥 DEBUG MAX: isSuccessful calculé:', isSuccessful);
                console.error('❌ 🔥 DEBUG MAX: results.recommendations existe:', !!results.recommendations);
                console.error('❌ 🔥 DEBUG MAX: Type recommendations:', typeof results.recommendations);
                console.error('❌ 🔥 DEBUG MAX: Length recommendations:', results.recommendations?.length);
                console.error('❌ 🔥 DEBUG MAX: Erreur API complète:', results);
                console.error('❌ 🔥 DEBUG MAX: results.error:', results.error);
                this.showErrorMessage('Erreur d\'analyse. Veuillez réessayer.');
            }

        } catch (error) {
            console.error('❌ 🔥 DEBUG MAX: CATCH ERROR - Type:', typeof error);
            console.error('❌ 🔥 DEBUG MAX: CATCH ERROR - Message:', error.message);
            console.error('❌ 🔥 DEBUG MAX: CATCH ERROR - Stack:', error.stack);
            console.error('❌ 🔥 DEBUG MAX: CATCH ERROR - Objet complet:', error);
            this.showErrorMessage('Connexion impossible. Vérifiez votre connexion.');
        }
    }

    // 📊 COLLECTE COMPLÈTE DES RÉPONSES
    collectAllAnswers() {
        console.log('📋 🔥 DEBUG MAX: Début collectAllAnswers()');
        console.log('📋 🔥 DEBUG MAX: this.state:', this.state);

        const answers = {};

        // Parcours sélectionné
        if (this.state.selectedParcours) {
            answers.parcours = this.state.selectedParcours;
            console.log('📋 🔥 DEBUG MAX: Parcours ajouté:', this.state.selectedParcours);
        }

        // Pays sélectionné
        if (this.state.selectedCountry) {
            answers.country = this.state.selectedCountry;
            console.log('📋 🔥 DEBUG MAX: Pays ajouté:', this.state.selectedCountry);
        }

        // Toutes les réponses aux questions
        console.log('📋 🔥 DEBUG MAX: this.state.answers:', this.state.answers);
        console.log('📋 🔥 DEBUG MAX: Nombre de questions répondues:', Object.keys(this.state.answers).length);

        Object.keys(this.state.answers).forEach(questionId => {
            const answer = this.state.answers[questionId];
            answers[questionId] = answer;
            console.log(`📋 🔥 DEBUG MAX: ${questionId} = ${answer}`);
        });

        console.log('📋 🔥 DEBUG MAX: Réponses finales collectées:', answers);
        console.log('📋 🔥 DEBUG MAX: Fin collectAllAnswers()');
        return answers;
    }

    // ⚠️ AFFICHAGE MESSAGE D'ERREUR
    showErrorMessage(message) {
        const aiComment = document.querySelector('.ai-comment');
        if (aiComment) {
            aiComment.innerHTML = `
                <div style="color: #ff6b6b; text-align: center;">
                    <i class="lucide-alert-circle" style="margin-right: 8px;"></i>
                    ${message}
                    <button onclick="location.reload()" style="
                        margin-top: 10px;
                        background: var(--accent-primary);
                        color: white;
                        border: none;
                        padding: 8px 16px;
                        border-radius: 6px;
                        cursor: pointer;
                    ">
                        Réessayer
                    </button>
                </div>
            `;
        }
    }

    // 🔙 GESTION BOUTON RETOUR
    handleBackClick() {
        const history = this.state.navigationHistory;

        if (history.length > 0) {
            const previousStep = history.pop();
            this.showStep(previousStep);

            // Réinitialiser selon l'étape
            if (previousStep === 'parcours') {
                this.state.selectedParcours = null;
                this.state.selectedCountry = null;
            } else if (previousStep === 'country-selector') {
                this.state.selectedCountry = null;
            }
        }
    }

    // 📝 HISTORIQUE NAVIGATION
    addToHistory(step) {
        this.state.navigationHistory.push(step);
    }

    // 🎯 MÉTHODES UTILITAIRES
    getElapsedTime() {
        return this.state.startTime ? Date.now() - this.state.startTime : 0;
    }

    getCompletionRate() {
        if (this.state.currentStep === 'questions') {
            return (this.state.currentQuestionIndex / this.state.totalQuestions) * 100;
        }
        return { 'parcours': 25, 'country-selector': 50, 'analysis': 100 }[this.state.currentStep] || 0;
    }

    // 🏙️ GENERATE CITY STRENGTHS
    generateCityStrengths(cityName, countryName) {
        const cityStrengths = {
            'Barcelona': ['Vie nocturne', 'Architecture', 'Plages urbaines'],
            'Lisbon': ['Coût de la vie', 'Climat doux', 'Startup scene'],
            'Bangkok': ['Cuisine locale', 'Coût très bas', 'Vie tropicale'],
            'Amsterdam': ['Vélo-friendly', 'Culture tolérante', 'Business hub'],
            'Berlin': ['Créativité', 'Histoire riche', 'Vie alternative'],
            'Prague': ['Architecture médiévale', 'Bière locale', 'Coût accessible'],
            'Porto': ['Gastronomie', 'Océan proche', 'Patrimoine'],
            'Valencia': ['Qualité de vie', 'Plages', 'Innovation'],
            'Vienna': ['Culture classique', 'Qualité de vie', 'Sécurité'],
            'Dublin': ['Tech hub', 'Culture pub', 'Anglophones'],
            'Singapore': ['Business hub', 'Multiculturalité', 'Efficacité'],
            'Tokyo': ['Tech avancée', 'Culture unique', 'Sécurité'],
            'New York': ['Opportunités', 'Culture', 'Énergie'],
            'Sydney': ['Plages', 'Qualité de vie', 'Opportunités']
        };

        return cityStrengths[cityName] || ['Qualité de vie', 'Opportunités', 'Culture locale'];
    }

    // 🎯 EXTRACT KEY CRITERIA
    extractKeyCriteria(answers) {
        const criteria = [];

        if (answers.expat_budget_realistic === 'budget_maximizer') criteria.push('Budget optimisé');
        if (answers.expat_passport === 'eu_passport') criteria.push('Liberté européenne');
        if (answers.expat_climate_tolerance === 'tropical_lover') criteria.push('Climat tropical');
        if (answers.expat_security_needs === 'adventure_tolerance') criteria.push('Tolérance aventure');
        if (answers.expat_lifestyle_pace === 'hyperactive_urban') criteria.push('Rythme urbain');
        if (answers.expat_professional_status === 'digital_nomad') criteria.push('Nomadisme digital');

        // Add default criteria if none found
        if (criteria.length === 0) {
            criteria.push('Adapté à votre profil', 'Recommandations IA');
        }

        return criteria.slice(0, 6);
    }

    // 🇺🇸 ADAPTER LES RÉPONSES POUR L'API USA
    adaptAnswersForUSA(answers) {
        console.log('🇺🇸 🔥 DEBUG USA: Réponses brutes reçues:', answers);

        // L'API USA s'attend à TOUTES ces 10 clés
        const requiredKeys = [
            'usa_main_priority',
            'usa_monthly_budget',
            'usa_work_situation',
            'usa_climate_preference',
            'usa_lifestyle_density',
            'usa_tax_philosophy',
            'usa_disaster_tolerance',
            'usa_transport_preference',
            'usa_education_priority',
            'usa_social_scene'
        ];

        const adaptedPayload = {};

        // Copier les réponses qui correspondent aux clés attendues
        for (const key of requiredKeys) {
            if (answers[key]) {
                adaptedPayload[key] = answers[key];
                console.log(`🇺🇸 ✅ DEBUG USA: ${key} = ${answers[key]}`);
            } else {
                console.log(`🇺🇸 ⚠️ DEBUG USA: Question manquante: ${key}`);
            }
        }

        // Valeurs par défaut intelligentes si des réponses manquent
        const defaults = {
            'usa_main_priority': 'career_growth',
            'usa_monthly_budget': 'budget_moderate',
            'usa_work_situation': 'hybrid',
            'usa_climate_preference': 'temperate',
            'usa_lifestyle_density': 'mixed_preference',
            'usa_tax_philosophy': 'moderate_taxes',
            'usa_disaster_tolerance': 'risk_averse',
            'usa_transport_preference': 'car_friendly',
            'usa_education_priority': 'good_schools',
            'usa_social_scene': 'balanced_social'
        };

        // Appliquer les défauts pour les réponses manquantes
        for (const [key, defaultValue] of Object.entries(defaults)) {
            if (!adaptedPayload[key]) {
                adaptedPayload[key] = defaultValue;
                console.log(`🇺🇸 🔥 DEBUG USA: Valeur par défaut ${key} = ${defaultValue}`);
            }
        }

        console.log('🇺🇸 ✅ DEBUG USA: Payload final adapté avec', Object.keys(adaptedPayload).length, 'clés:', adaptedPayload);
        return adaptedPayload;
    }

    adaptAnswersForFrance(answers) {
        console.log('🇫🇷 🔥 DEBUG FRANCE: Réponses brutes reçues:', answers);

        // L'API France s'attend à TOUTES ces 10 clés
        const requiredKeys = [
            'france_main_priority',
            'france_age_profile',
            'france_monthly_budget',
            'france_work_situation',
            'france_housing_preference',
            'france_transport_preference',
            'france_climate_preference',
            'france_social_scene',
            'france_family_situation',
            'france_deal_breaker'
        ];

        const adaptedPayload = {};

        // Copier les réponses qui correspondent aux clés attendues
        for (const key of requiredKeys) {
            if (answers[key]) {
                adaptedPayload[key] = answers[key];
                console.log(`🇫🇷 ✅ DEBUG FRANCE: ${key} = ${answers[key]}`);
            } else {
                console.log(`🇫🇷 ⚠️ DEBUG FRANCE: Question manquante: ${key}`);
            }
        }

        // Valeurs par défaut intelligentes si des réponses manquent
        const defaults = {
            'france_main_priority': 'lifestyle_upgrade',
            'france_age_profile': 'young_active',
            'france_monthly_budget': 'budget_balanced',
            'france_work_situation': 'stable_cdi',
            'france_housing_preference': 'transport_connected',
            'france_transport_preference': 'multimodal_flexible',
            'france_climate_preference': 'climate_adaptable',
            'france_social_scene': 'gastronomy_culture',
            'france_family_situation': 'single_no_children',
            'france_deal_breaker': 'cost_too_high'
        };

        // Appliquer les défauts pour les réponses manquantes
        for (const [key, defaultValue] of Object.entries(defaults)) {
            if (!adaptedPayload[key]) {
                adaptedPayload[key] = defaultValue;
                console.log(`🇫🇷 🔥 DEBUG FRANCE: Valeur par défaut ${key} = ${defaultValue}`);
            }
        }

        console.log('🇫🇷 ✅ DEBUG FRANCE: Payload final adapté avec', Object.keys(adaptedPayload).length, 'clés:', adaptedPayload);
        return adaptedPayload;
    }

    adaptAnswersForCanada(answers) {
        console.log('🇨🇦 🔥 DEBUG CANADA: Réponses brutes reçues:', answers);

        // L'API Canada s'attend à TOUTES ces 10 clés
        const requiredKeys = [
            'canada_main_priority',
            'canada_age_profile',
            'canada_monthly_budget',
            'canada_work_situation',
            'canada_housing_preference',
            'canada_transport_preference',
            'canada_climate_preference',
            'canada_social_scene',
            'canada_family_situation',
            'canada_deal_breaker'
        ];

        const adaptedPayload = {};

        // Copier les réponses qui correspondent aux clés attendues
        for (const key of requiredKeys) {
            if (answers[key]) {
                adaptedPayload[key] = answers[key];
                console.log(`🇨🇦 ✅ DEBUG CANADA: ${key} = ${answers[key]}`);
            } else {
                console.log(`🇨🇦 ⚠️ DEBUG CANADA: Question manquante: ${key}`);
            }
        }

        // Valeurs par défaut intelligentes si des réponses manquent
        const defaults = {
            'canada_main_priority': 'lifestyle_upgrade',
            'canada_age_profile': 'young_professional',
            'canada_monthly_budget': 'budget_balanced',
            'canada_work_situation': 'stable_employment',
            'canada_housing_preference': 'transport_connected',
            'canada_transport_preference': 'multimodal_flexible',
            'canada_climate_preference': 'climate_adaptable',
            'canada_social_scene': 'outdoor_sports',
            'canada_family_situation': 'single_no_children',
            'canada_deal_breaker': 'cost_too_high'
        };

        // Appliquer les défauts pour les réponses manquantes
        for (const [key, defaultValue] of Object.entries(defaults)) {
            if (!adaptedPayload[key]) {
                adaptedPayload[key] = defaultValue;
                console.log(`🇨🇦 🔥 DEBUG CANADA: Valeur par défaut ${key} = ${defaultValue}`);
            }
        }

        console.log('🇨🇦 ✅ DEBUG CANADA: Payload final adapté avec', Object.keys(adaptedPayload).length, 'clés:', adaptedPayload);
        return adaptedPayload;
    }

    adaptAnswersForAustralia(answers) {
        console.log('🇦🇺 🔥 DEBUG AUSTRALIA: Réponses brutes reçues:', answers);

        // L'API Australia s'attend à TOUTES ces 12 clés (approche hybride)
        const requiredKeys = [
            'australia_lifestyle_priority',
            'australia_climate_preference',
            'australia_work_environment',
            'australia_budget_range',
            'australia_housing_preference',
            'australia_transport_priority',
            'australia_social_scene',
            'australia_nature_access',
            'australia_family_situation',
            'australia_education_priority',
            'australia_connectivity_need',
            'australia_career_stage'
        ];

        const adaptedPayload = {};

        // Copier les réponses qui correspondent aux clés attendues
        for (const key of requiredKeys) {
            if (answers[key]) {
                adaptedPayload[key] = answers[key];
                console.log(`🇦🇺 ✅ DEBUG AUSTRALIA: ${key} = ${answers[key]}`);
            } else {
                console.log(`🇦🇺 ⚠️ DEBUG AUSTRALIA: Question manquante: ${key}`);
            }
        }

        // Valeurs par défaut intelligentes pour approche hybride
        const defaults = {
            'australia_lifestyle_priority': 'city_business',
            'australia_climate_preference': 'temperate_mild',
            'australia_work_environment': 'corporate_cbd',
            'australia_budget_range': 'budget_comfortable',
            'australia_housing_preference': 'apartment_city',
            'australia_transport_priority': 'transport_helpful',
            'australia_social_scene': 'multicultural_diverse',
            'australia_nature_access': 'city_parks_enough',
            'australia_family_situation': 'single_independent',
            'australia_education_priority': 'education_moderate',
            'australia_connectivity_need': 'domestic_travel',
            'australia_career_stage': 'career_building'
        };

        // Appliquer les défauts pour les réponses manquantes
        for (const [key, defaultValue] of Object.entries(defaults)) {
            if (!adaptedPayload[key]) {
                adaptedPayload[key] = defaultValue;
                console.log(`🇦🇺 🔥 DEBUG AUSTRALIA: Valeur par défaut ${key} = ${defaultValue}`);
            }
        }

        console.log('🇦🇺 ✅ DEBUG AUSTRALIA: Payload final adapté avec', Object.keys(adaptedPayload).length, 'clés:', adaptedPayload);
        return adaptedPayload;
    }

    adaptAnswersForSpain(answers) {
        console.log('🇪🇸 🔧 DEBUG SPAIN: Adaptation des réponses pour l\'Espagne');
        console.log('🇪🇸 📥 DEBUG SPAIN: Réponses reçues:', answers);

        const requiredKeys = [
            'spain_lifestyle_priority',
            'spain_climate_preference',
            'spain_work_environment',
            'spain_budget_comfort',
            'spain_social_life',
            'spain_transport_priority',
            'spain_housing_type',
            'spain_food_culture',
            'spain_pace_of_life',
            'spain_seasonal_preference'
        ];

        const adaptedPayload = {};

        // Copier les réponses qui correspondent aux clés attendues
        for (const key of requiredKeys) {
            if (answers[key]) {
                adaptedPayload[key] = answers[key];
                console.log(`🇪🇸 ✅ DEBUG SPAIN: ${key} = ${answers[key]}`);
            } else {
                console.log(`🇪🇸 ⚠️ DEBUG SPAIN: Question manquante: ${key}`);
            }
        }

        // Valeurs par défaut intelligentes pour approche hybride
        const defaults = {
            'spain_lifestyle_priority': 'city_culture',
            'spain_climate_preference': 'mediterranean_warm',
            'spain_work_environment': 'flexible_bilingual',
            'spain_budget_comfort': 'middle_class',
            'spain_social_life': 'social_active',
            'spain_transport_priority': 'public_transport',
            'spain_housing_type': 'apartment_central',
            'spain_food_culture': 'local_traditional',
            'spain_pace_of_life': 'relaxed_balanced',
            'spain_seasonal_preference': 'warm_seasons'
        };

        // Appliquer les valeurs par défaut si manquantes
        for (const [key, defaultValue] of Object.entries(defaults)) {
            if (!adaptedPayload[key]) {
                adaptedPayload[key] = defaultValue;
                console.log(`🇪🇸 🔧 DEBUG SPAIN: Valeur par défaut appliquée: ${key} = ${defaultValue}`);
            }
        }

        console.log('🇪🇸 ✅ DEBUG SPAIN: Payload final adapté avec', Object.keys(adaptedPayload).length, 'clés:', adaptedPayload);
        return adaptedPayload;
    }

    adaptAnswersForMexico(answers) {
        console.log('🇲🇽 🔧 DEBUG MEXICO: Adaptation des réponses pour le Mexique');
        console.log('🇲🇽 📥 DEBUG MEXICO: Réponses reçues:', answers);

        const requiredKeys = [
            'mexico_lifestyle_priority',
            'mexico_climate_preference',
            'mexico_work_environment',
            'mexico_budget_comfort',
            'mexico_social_life',
            'mexico_transport_priority',
            'mexico_housing_type',
            'mexico_food_culture',
            'mexico_pace_of_life',
            'mexico_safety_priority'
        ];

        const adaptedPayload = {};

        // Copier les réponses qui correspondent aux clés attendues
        for (const key of requiredKeys) {
            if (answers[key]) {
                adaptedPayload[key] = answers[key];
                console.log(`🇲🇽 ✅ DEBUG MEXICO: ${key} = ${answers[key]}`);
            } else {
                console.log(`🇲🇽 ⚠️ DEBUG MEXICO: Question manquante: ${key}`);
            }
        }

        // Valeurs par défaut intelligentes pour approche hybride
        const defaults = {
            'mexico_lifestyle_priority': 'expat_friendly',
            'mexico_climate_preference': 'climate_flexible',
            'mexico_work_environment': 'flexible_opportunity',
            'mexico_budget_comfort': 'budget_flexible',
            'mexico_social_life': 'mixed_social',
            'mexico_transport_priority': 'mixed_transport',
            'mexico_housing_type': 'flexible_housing',
            'mexico_food_culture': 'food_flexible',
            'mexico_pace_of_life': 'flexible_pace',
            'mexico_safety_priority': 'reasonable_caution'
        };

        // Appliquer les valeurs par défaut si manquantes
        for (const [key, defaultValue] of Object.entries(defaults)) {
            if (!adaptedPayload[key]) {
                adaptedPayload[key] = defaultValue;
                console.log(`🇲🇽 🔧 DEBUG MEXICO: Valeur par défaut appliquée: ${key} = ${defaultValue}`);
            }
        }

        console.log('🇲🇽 ✅ DEBUG MEXICO: Payload final adapté avec', Object.keys(adaptedPayload).length, 'clés:', adaptedPayload);
        return { preferences: adaptedPayload };
    }

    adaptAnswersForBrazil(answers) {
        console.log('🇧🇷 🔧 DEBUG BRAZIL: Adaptation des réponses pour le Brésil');
        console.log('🇧🇷 📥 DEBUG BRAZIL: Réponses reçues:', answers);

        // Mapping des nouveaux noms de questions vers les anciens noms attendus par l'algorithme
        const fieldMapping = {
            'brazil_regional_preference': 'brazil_region_preference',
            'brazil_lifestyle_priority': 'brazil_main_priority',
            'brazil_work_environment': 'brazil_work_situation',
            'brazil_budget_range': 'brazil_monthly_budget',
            'brazil_climate_preference': 'brazil_climate_preference', // même nom
            'brazil_housing_preference': 'brazil_housing_preference', // même nom
            'brazil_transport_style': 'brazil_transport_preference',
            'brazil_social_scene': 'brazil_lifestyle_scene',
            'brazil_culture_priorities': 'brazil_safety_vs_culture',
            'brazil_language_comfort': 'brazil_age_profile',
            'brazil_safety_priorities': 'brazil_family_situation',
            'brazil_food_culture': 'brazil_deal_breaker'
        };

        const adaptedPayload = {};

        // Convertir les réponses selon le mapping
        for (const [newKey, oldKey] of Object.entries(fieldMapping)) {
            if (answers[newKey]) {
                adaptedPayload[oldKey] = answers[newKey];
                console.log(`🇧🇷 ✅ DEBUG BRAZIL: ${newKey} → ${oldKey} = ${answers[newKey]}`);
            }
        }

        // Valeurs par défaut pour les champs obligatoires
        if (!adaptedPayload['brazil_main_priority']) {
            adaptedPayload['brazil_main_priority'] = 'lifestyle_upgrade';
        }
        if (!adaptedPayload['brazil_monthly_budget']) {
            adaptedPayload['brazil_monthly_budget'] = 'budget_balanced';
        }

        console.log('🇧🇷 ✅ DEBUG BRAZIL: Payload final adapté avec', Object.keys(adaptedPayload).length, 'clés:', adaptedPayload);
        return adaptedPayload;
    }

    generateBrazilCityStrengths(cityName, region, detailedScores) {
        const strengths = [];

        // Points forts basés sur les scores détaillés
        if (detailedScores?.cultural_scene > 0.8) strengths.push('Scène culturelle dynamique');
        if (detailedScores?.nightlife > 0.7) strengths.push('Vie nocturne vibrante');
        if (detailedScores?.food_scene > 0.8) strengths.push('Gastronomie brésilienne authentique');
        if (detailedScores?.safety > 0.6) strengths.push('Sécurité raisonnable');
        if (detailedScores?.cost_of_living > 0.7) strengths.push('Coût de vie abordable');
        if (detailedScores?.job_opportunities > 0.6) strengths.push('Opportunités professionnelles');
        if (detailedScores?.climate > 0.8) strengths.push('Climat tropical agréable');
        if (detailedScores?.beach_access > 0.7) strengths.push('Accès aux plages');

        // Points forts spécifiques par ville
        const citySpecific = {
            'São Paulo': ['Centre économique du Brésil', 'Diversité culturelle', 'Opportunités business'],
            'Rio de Janeiro': ['Plages mythiques', 'Carnaval et festivités', 'Paysages iconiques'],
            'Brasília': ['Architecture unique', 'Centre politique', 'Urbanisme moderne'],
            'Belo Horizonte': ['Culture mineira authentique', 'Gastronomie réputée', 'Proximité nature'],
            'Curitiba': ['Ville modèle écologique', 'Transports urbains', 'Qualité de vie'],
            'Salvador': ['Patrimoine afro-brésilien', 'Musique et danse', 'Architecture coloniale'],
            'Fortaleza': ['Plages paradisiaques', 'Culture nordestine', 'Hospitalité locale'],
            'Recife': ['Centre technologique', 'Histoire coloniale', 'Frevo et culture'],
            'Porto Alegre': ['Influence européenne', 'Éducation de qualité', 'Proximité Uruguay'],
            'Florianópolis': ['Île magique', 'Plages et nature', 'Innovation technologique']
        };

        if (citySpecific[cityName]) {
            strengths.push(...citySpecific[cityName]);
        }

        // Points forts régionaux
        const regionalStrengths = {
            'Sudeste': ['Développement économique', 'Infrastructure moderne'],
            'Sul': ['Influence européenne', 'Éducation de qualité'],
            'Nordeste': ['Culture authentique', 'Plages magnifiques'],
            'Norte': ['Amazonie unique', 'Écosystème préservé'],
            'Centro-Oeste': ['Agronégoce dynamique', 'Espaces naturels']
        };

        if (regionalStrengths[region]) {
            strengths.push(...regionalStrengths[region]);
        }

        return strengths.slice(0, 4); // Limiter à 4 points forts
    }

    generateBrazilRecommendationReason(cityName, region, detailedScores, userProfile) {
        const reasons = [];

        // Raisons basées sur le profil utilisateur (objet)
        if (userProfile) {
            if (userProfile.region === 'sudeste') {
                reasons.push('correspondance parfaite avec votre préférence pour le Sudeste');
            }
            if (userProfile.priority === 'career_growth') {
                reasons.push('excellentes opportunités de croissance professionnelle');
            }
            if (userProfile.lifestyle === 'active_social') {
                reasons.push('scène sociale dynamique adaptée à votre profil');
            }
            if (userProfile.budget === 'budget_comfortable') {
                reasons.push('coût de vie équilibré pour votre budget');
            }
        }

        // Raisons basées sur les scores
        if (detailedScores?.cultural_scene > 0.8) {
            reasons.push('scène culturelle exceptionnelle');
        }
        if (detailedScores?.cost_of_living > 0.7) {
            reasons.push('excellent rapport qualité-prix');
        }
        if (detailedScores?.climate > 0.8) {
            reasons.push('climat tropical idéal');
        }

        // Raisons par défaut par ville
        const defaultReasons = {
            'São Paulo': 'métropole économique et culturelle du Brésil',
            'Rio de Janeiro': 'ville merveilleuse entre mer et montagne',
            'Brasília': 'capitale moderne et architecturale unique',
            'Belo Horizonte': 'charme mineiro et qualité de vie',
            'Curitiba': 'modèle écologique et innovation urbaine',
            'Salvador': 'berceau de la culture afro-brésilienne',
            'Fortaleza': 'porte d\'entrée du Nordeste authentique',
            'Recife': 'Venise brésilienne et hub technologique',
            'Porto Alegre': 'influences européennes et gaúcha',
            'Florianópolis': 'île magique de l\'innovation'
        };

        const mainReason = defaultReasons[cityName] || 'destination brésilienne de choix';

        if (reasons.length > 0) {
            return `${cityName} combine ${mainReason} avec ${reasons.slice(0, 2).join(' et ')}.`;
        } else {
            return `${cityName} représente ${mainReason} parfaitement adaptée à vos attentes.`;
        }
    }

    // 🇯🇵 ADAPTATION RÉPONSES POUR API JAPAN
    adaptAnswersForJapan(answers) {
        console.log('🇯🇵 🔧 DEBUG JAPAN: Adaptation des réponses pour le Japon');
        console.log('🇯🇵 📥 DEBUG JAPAN: Réponses reçues:', answers);

        // Pour le Japon, les réponses ont déjà les bons noms (japan_region_preference, etc.)
        // Donc on retourne directement les réponses sans mapping
        const adaptedPayload = { ...answers };

        console.log('🇯🇵 📤 DEBUG JAPAN: Payload adapté:', adaptedPayload);
        console.log('🇯🇵 ✅ DEBUG JAPAN: Nombre de paramètres adaptés:', Object.keys(adaptedPayload).length);

        return adaptedPayload;
    }

    // 🇲🇦 ADAPTATION RÉPONSES POUR API MOROCCO
    adaptAnswersForMorocco(answers) {
        console.log('🇲🇦 🔧 DEBUG MOROCCO: Adaptation des réponses pour le Maroc');
        console.log('🇲🇦 📥 DEBUG MOROCCO: Réponses reçues:', answers);

        // L'API Morocco attend un format {"preferences": {...}}
        // Extraire seulement les préférences Morocco (sans parcours/country)
        const moroccoPreferences = {};

        // Copier toutes les réponses qui commencent par "morocco_"
        Object.keys(answers).forEach(key => {
            if (key.startsWith('morocco_')) {
                moroccoPreferences[key] = answers[key];
            }
        });

        const adaptedPayload = {
            preferences: moroccoPreferences
        };

        console.log('🇲🇦 📤 DEBUG MOROCCO: Payload adapté:', adaptedPayload);
        console.log('🇲🇦 ✅ DEBUG MOROCCO: Nombre de préférences Morocco:', Object.keys(moroccoPreferences).length);

        return adaptedPayload;
    }

    // 🇹🇭 ADAPTATION RÉPONSES POUR API THAILAND
    adaptAnswersForThailand(answers) {
        console.log('🇹🇭 🔧 DEBUG THAILAND: Adaptation des réponses pour la Thaïlande');
        console.log('🇹🇭 📥 DEBUG THAILAND: Réponses reçues:', answers);

        // L'API Thailand attend un format {"responses": {...}}
        // Extraire seulement les réponses Thailand (sans parcours/country)
        const thailandResponses = {};

        // Copier toutes les réponses qui commencent par "thailand_"
        Object.keys(answers).forEach(key => {
            if (key.startsWith('thailand_')) {
                thailandResponses[key] = answers[key];
            }
        });

        const adaptedPayload = {
            responses: thailandResponses
        };

        console.log('🇹🇭 📤 DEBUG THAILAND: Payload adapté:', adaptedPayload);
        console.log('🇹🇭 ✅ DEBUG THAILAND: Nombre de réponses Thailand:', Object.keys(thailandResponses).length);

        return adaptedPayload;
    }
}

// 🚀 INITIALISATION GLOBALE
document.addEventListener('DOMContentLoaded', () => {
    window.zineAnalysis = new ZineInsightAnalysis();
    console.log('🎯 ZineInsight Analysis initialisé !');
});

// Export pour debug
window.ZineInsightAnalysis = ZineInsightAnalysis;
