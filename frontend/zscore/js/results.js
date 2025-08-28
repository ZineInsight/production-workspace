/* ====================================
   🏆 RESULTS PAGE - REVOLUTIONARY JAVASCRIPT
   Ultra-functional results dashboard with premium UX
   Everything responds like a symphony! 🎼
==================================== */

// ===== SMART CITY IMAGES SYSTEM ===== //
// Convention: nom-ville.extension dans /images/cities/
// Exemple: ouarzazate.jpg, casablanca.webp, etc.
const SUPPORTED_IMAGE_FORMATS = ['.jpg', '.jpeg', '.png', '.webp', '.gif'];

// ===== REVOLUTIONARY RESULTS MANAGER ===== //
class RevolutionaryResultsManager {
    constructor() {
        this.apiBaseUrl = 'http://localhost:8000';
        this.resultsData = null;
        this.isLoaded = false;
        this.animations = new Map();

        // Initialize when DOM is ready
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => this.initialize());
        } else {
            this.initialize();
        }
    }

    // 🖼️ GET CITY IMAGE URL - SMART AUTO-DETECTION
    getCityImage(cityName) {
        // Normaliser le nom de ville (minuscules, sans accents, sans espaces)
        const normalizedName = cityName
            .toLowerCase()
            .normalize("NFD")
            .replace(/[\u0300-\u036f]/g, "") // Supprimer les accents
            .replace(/[^a-z0-9]/g, ""); // Garder que lettres/chiffres

        // Retourner le premier format trouvé
        for (const format of SUPPORTED_IMAGE_FORMATS) {
            const imageUrl = `images/cities/${normalizedName}${format}`;
            // On retourne l'URL, la vérification se fait dans updateCityImage
            return imageUrl;
        }

        return null;
    }

    // 🎨 UPDATE CITY IMAGE
    updateCityImage(cityName) {
        const placeholder = document.getElementById('cityImagePlaceholder');
        if (!placeholder) return;

        // Normaliser le nom de ville
        const normalizedName = cityName
            .toLowerCase()
            .normalize("NFD")
            .replace(/[\u0300-\u036f]/g, "")
            .replace(/[^a-z0-9]/g, "");

        // Essayer tous les formats dans l'ordre de préférence
        let imageFound = false;
        let formatIndex = 0;

        const tryNextFormat = () => {
            if (formatIndex >= SUPPORTED_IMAGE_FORMATS.length) {
                // Aucune image trouvée
                placeholder.innerHTML = `
                    <i data-lucide="image"></i>
                    <span>Photo de ${cityName}</span>
                    <small>Image à venir...</small>
                `;
                placeholder.classList.remove('has-image');
                if (typeof lucide !== 'undefined') lucide.createIcons();
                return;
            }

            const format = SUPPORTED_IMAGE_FORMATS[formatIndex];
            const imageUrl = `images/cities/${normalizedName}${format}`;

            const img = new Image();
            img.onload = () => {
                // Image trouvée !
                placeholder.innerHTML = `<img src="${imageUrl}" alt="Vue panoramique de ${cityName}" class="city-photo" />`;
                placeholder.classList.add('has-image');
                imageFound = true;
            };
            img.onerror = () => {
                // Essayer le format suivant
                formatIndex++;
                tryNextFormat();
            };
            img.src = imageUrl;
        };

        tryNextFormat();
    }

    // 🚀 INITIALIZE REVOLUTIONARY EXPERIENCE
    async initialize() {
        console.log('🚀 Initializing Revolutionary Results Dashboard...');

        try {
            // Initialize Lucide icons first
            if (typeof lucide !== 'undefined') {
                lucide.createIcons();
            }

            // Show loading overlay
            this.showLoadingOverlay();

            // Load results data
            await this.loadResultsData();

            // Setup all interactions
            this.setupEventListeners();

            // Initialize UI elements
            this.initializeUI();

            // Hide loading overlay
            this.hideLoadingOverlay();

            console.log('✅ Revolutionary Results Dashboard Ready!');

        } catch (error) {
            console.error('❌ Failed to initialize results:', error);
            this.handleInitializationError(error);
        }
    }

    // 📊 LOAD RESULTS DATA
    async loadResultsData() {
        console.log('📊 DEBUG Loading results data...');

        try {
            // FORCE CLEAR OLD CACHE - AUDIT MODE
            const storedResults = localStorage.getItem('zineinsight_results');
            if (storedResults) {
                const parsed = JSON.parse(storedResults);
                if (parsed.timestamp < Date.now() - 300000) { // Plus de 5 minutes
                    console.log('🗑️ AUDIT: Clearing old cache data');
                    localStorage.removeItem('zineinsight_results');
                    localStorage.removeItem('questionnaire_answers');
                    window.location.href = '/questionnaire.html';
                    return;
                }
            }

            const storedAnswers = localStorage.getItem('questionnaire_answers');

            console.log('📊 DEBUG storedResults exists:', !!storedResults);
            console.log('📊 DEBUG storedAnswers exists:', !!storedAnswers);

            if (storedResults) {
                console.log('✅ DEBUG Found stored results');
                this.resultsData = JSON.parse(storedResults);
                console.log('📊 DEBUG Parsed resultsData:', this.resultsData);
                console.log('📊 DEBUG First recommendation:', this.resultsData.recommendations?.[0]);
                this.isLoaded = true;
                return;
            }

            // If no stored results, try to get from questionnaire answers
            if (storedAnswers) {
                console.log('🔄 DEBUG No stored results, generating from answers...');
                const answers = JSON.parse(storedAnswers);
                console.log('📊 DEBUG Parsed answers:', answers);
                await this.generateResultsFromAnswers(answers);
                return;
            }

            // If nothing, show demo data
            console.log('🎯 DEBUG No data found, using demo results');
            this.generateDemoResults();

        } catch (error) {
            console.error('❌ Error loading results:', error);
            this.generateDemoResults();
        }
    }

    // 🎯 GENERATE RESULTS FROM ANSWERS
    async generateResultsFromAnswers(answers) {
        try {
            const response = await fetch(`${this.apiBaseUrl}/api/calculate`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    questionnaire: answers.responses || answers,
                    country: answers.selectedCountry || 'france'
                })
            });

            if (!response.ok) {
                throw new Error(`API Error: ${response.status}`);
            }

            const data = await response.json();
            console.log('🔍 DEBUG API Response:', data);

            // 🔧 ADAPTIVE DATA STRUCTURE DETECTION
            let recommendations = [];
            let isSuccessful = false;
            let countryIdSystemEnabled = false;

            // Detection de la structure de données
            if (data.success) {
                // Format simple avec data.recommendations direct (notre endpoint /api/calculate)
                recommendations = data.recommendations || [];
                isSuccessful = true;
                countryIdSystemEnabled = data.country_id_system || false;
                console.log('✅ Using simple format (local /api/calculate)');
            } else if (data.status === 'success' && data.recommendations) {
                // Format complexe avec data.recommendations.recommendations (API production)
                if (Array.isArray(data.recommendations)) {
                    // data.recommendations est déjà un tableau
                    recommendations = data.recommendations;
                } else if (data.recommendations.recommendations && Array.isArray(data.recommendations.recommendations)) {
                    // data.recommendations.recommendations est le tableau
                    recommendations = data.recommendations.recommendations;
                }
                isSuccessful = true;
                countryIdSystemEnabled = true; // Supposer que le système country_id est disponible
                console.log('✅ Using complex format (production API)');
                console.log('📊 Recommendations found:', recommendations.length);
            }

            if (isSuccessful && recommendations.length > 0) {
                // Adapter la structure des données de l'API au format attendu par le frontend
                const adaptedRecommendations = recommendations.map(city => {
                    // Format adaptatif selon la structure de la ville
                    const cityName = city.city || city.name || city.nom || 'Ville inconnue';
                    const cityCountry = city.country || city.pays || 'Pays inconnu';
                    const cityScore = city.compatibility || city.score_final || city.score || 0;
                    const cityCountryId = city.country_id || null;

                    return {
                        nom: cityName,
                        pays: cityCountry,
                        score_final: Math.round(cityScore * 100) || Math.round(cityScore),
                        points_forts: this.generateCityStrengths(cityName, cityCountry),
                        population: city.population || 'Non disponible',
                        temperature_moyenne: this.generateCityTemperature(cityName, cityCountry),
                        compatibilites: this.generateCityCompatibilities(cityName, cityCountry),
                        cout_vie: Math.round((city.cost_of_living || city.cout_vie || cityScore * 0.7) * 100) || 75,
                        emploi: Math.round((city.job_market || city.emploi || cityScore * 0.8) * 100) || 80,
                        culture: Math.round((city.culture || cityScore * 0.9) * 100) || 85,
                        qualite_vie: Math.round((city.quality_of_life || city.qualite_vie || cityScore) * 100) || Math.round(cityScore),
                        country_id: cityCountryId  // 🆔 NOUVEAU: Support du country_id system
                    };
                });

                this.resultsData = {
                    success: true,
                    recommendations: adaptedRecommendations,
                    selectedCountry: answers.selectedCountry || 'world',
                    questionsAnswered: Object.keys(answers.responses || answers).length,
                    analysisDate: new Date().toISOString(),
                    matchPercentage: Math.round(adaptedRecommendations[0]?.score_final || 85),
                    keyCriteria: this.extractKeyCriteria(answers.responses || answers),
                    country_id_system: countryIdSystemEnabled  // 🆔 Flag du nouveau système
                };

                // Store results for future use
                localStorage.setItem('zineinsight_results', JSON.stringify(this.resultsData));

                this.isLoaded = true;
                console.log('✅ Results generated from answers with', adaptedRecommendations.length, 'cities');
            } else {
                throw new Error('No valid recommendations found in API response');
            }

        } catch (error) {
            console.error('❌ Error generating results from answers:', error);
            this.generateDemoResults();
        }
    }

    // 🎪 GENERATE DEMO RESULTS
    generateDemoResults() {
        console.log('🎪 Generating demo results...');

        this.resultsData = {
            success: true,
            recommendations: [
                {
                    nom: "Bordeaux",
                    pays: "France",
                    score_final: 85,
                    points_forts: ["Culture riche", "Qualité de vie", "Gastronomie"],
                    population: "254,436 hab.",
                    temperature_moyenne: "16°C",
                    compatibilites: ["🍷 Climat viticole parfait", "🏛️ Patrimoine UNESCO", "🍽️ Gastronomie d'excellence"],
                    cout_vie: 72,
                    emploi: 78,
                    culture: 92,
                    qualite_vie: 88
                },
                {
                    nom: "Lyon",
                    pays: "France",
                    score_final: 82,
                    points_forts: ["Économie dynamique", "Transport", "Innovation"],
                    population: "515,695 hab.",
                    temperature_moyenne: "14°C",
                    compatibilites: ["🏢 Hub économique majeur", "🚇 Transport excellent", "💡 Écosystème startup"],
                    cout_vie: 68,
                    emploi: 85,
                    culture: 87,
                    qualite_vie: 83
                },
                {
                    nom: "Nantes",
                    pays: "France",
                    score_final: 79,
                    points_forts: ["Écologie", "Jeunesse", "Créativité"],
                    population: "314,138 hab.",
                    temperature_moyenne: "13°C",
                    compatibilites: ["🌱 Ville verte leader", "🎨 Créativité urbaine", "⚡ Innovation durable"],
                    cout_vie: 75,
                    emploi: 76,
                    culture: 84,
                    qualite_vie: 81
                }
            ],
            selectedCountry: 'france',
            questionsAnswered: 42,
            analysisDate: new Date().toISOString(),
            matchPercentage: 87,
            keyCriteria: ['Culture importante', 'Budget modéré', 'Vie urbaine', 'Opportunités professionnelles']
        };

        // Store demo results in localStorage
        localStorage.setItem('zineinsight_results', JSON.stringify(this.resultsData));
        localStorage.setItem('questionnaire_answers', JSON.stringify({
            responses: {
                budget: 'low',
                family: 'yes',
                job: 'tech',
                culture: 'important'
            },
            selectedCountry: 'france'
        }));

        this.isLoaded = true;
        console.log('✅ Demo results generated and stored');
    }

    // 🎨 INITIALIZE UI ELEMENTS
    initializeUI() {
        console.log('🎨 Initializing UI elements...');

        // Update page intro
        this.updatePageIntro();

        // Update podium
        this.updatePodium();

        // Update profile section
        this.updateProfileSection();

        // Update focus section
        this.updateFocusSection();

        // Update timestamp
        this.updateTimestamps();

        console.log('✅ UI elements initialized');
    }

    // 📝 UPDATE PAGE INTRO
    updatePageIntro() {
        const badge = document.getElementById('analysisTimestamp');
        if (badge && this.resultsData) {
            const date = new Date(this.resultsData.analysisDate);
            const timeAgo = this.getTimeAgo(date);
            badge.textContent = timeAgo;
        }
    }

    // 🏆 UPDATE PODIUM
    updatePodium() {
        console.log('🏆 DEBUG updatePodium - resultsData:', this.resultsData);

        if (!this.resultsData || !this.resultsData.recommendations) {
            console.error('❌ DEBUG: Pas de resultsData ou recommendations');
            return;
        }

        const recommendations = this.resultsData.recommendations.slice(0, 3);
        console.log('🏆 DEBUG recommendations:', recommendations);

        recommendations.forEach((city, index) => {
            const cityNum = index + 1;
            console.log(`🏆 DEBUG ville ${cityNum}:`, city);

            // Update city name
            const nameEl = document.getElementById(`city${cityNum}Name`);
            if (nameEl) {
                console.log(`🏆 DEBUG city${cityNum}Name element trouvé, valeur:`, city.nom);
                nameEl.textContent = city.nom || 'N/A';
                this.animateElementAppearance(nameEl, 300 + (index * 100));

                // 🖼️ UPDATE CITY IMAGE (si c'est la ville #1)
                if (cityNum === 1) {
                    this.updateCityImage(city.nom);
                    // Mettre à jour le titre de la section détail
                    const focusCityName = document.getElementById('focusCityName');
                    if (focusCityName) {
                        focusCityName.textContent = city.nom;
                    }
                }
            } else {
                console.error(`❌ DEBUG: Element city${cityNum}Name non trouvé`);
            }

            // Update country
            const countryEl = document.getElementById(`city${cityNum}Country`);
            if (countryEl) {
                console.log(`🏆 DEBUG city${cityNum}Country element trouvé, valeur:`, city.pays);
                countryEl.textContent = city.pays || 'N/A';
            } else {
                console.error(`❌ DEBUG: Element city${cityNum}Country non trouvé`);
            }

            // Update score
            const scoreEl = document.getElementById(`city${cityNum}Score`);
            if (scoreEl) {
                this.animateScore(scoreEl, city.score_final || 0, 500 + (index * 100));
            }

            // Update strengths
            const strengthsEl = document.getElementById(`city${cityNum}Strengths`);
            if (strengthsEl) {
                // Convert points_forts to array if it's a string
                let strengths = city.points_forts || [];
                if (typeof strengths === 'string') {
                    strengths = strengths.split(',').map(s => s.trim()).filter(s => s);
                }
                this.updateCityStrengths(strengthsEl, strengths);
            }
        });
    }

    // 💪 UPDATE CITY STRENGTHS
    updateCityStrengths(container, strengths) {
        const tagsContainer = container.querySelector('.strength-tags');
        if (!tagsContainer) return;

        tagsContainer.innerHTML = '';

        // Ensure strengths is an array
        if (typeof strengths === 'string') {
            strengths = strengths.split(',').map(s => s.trim()).filter(s => s);
        }

        if (!Array.isArray(strengths)) {
            console.warn('⚠️ strengths is not an array:', strengths);
            return;
        }

        strengths.slice(0, 3).forEach((strength, index) => {
            setTimeout(() => {
                const tag = document.createElement('span');
                tag.className = 'tag';
                tag.textContent = strength;
                tag.style.opacity = '0';
                tag.style.transform = 'translateY(10px)';

                tagsContainer.appendChild(tag);

                // Animate appearance
                setTimeout(() => {
                    tag.style.transition = 'all 0.3s ease-out';
                    tag.style.opacity = '1';
                    tag.style.transform = 'translateY(0)';
                }, 50);

            }, index * 100);
        });
    }

    // 👤 UPDATE PROFILE SECTION
    updateProfileSection() {
        if (!this.resultsData) return;

        // Questions answered
        const questionsEl = document.getElementById('questionsAnswered');
        if (questionsEl) {
            this.animateCounterNumber(questionsEl, this.resultsData.questionsAnswered || 0, 800);
        }

        // Match percentage
        const matchEl = document.getElementById('matchPercentage');
        if (matchEl) {
            this.animateCounterNumber(matchEl, this.resultsData.matchPercentage || 0, 1000, '%');
        }

        // Key criteria
        const criteriaList = document.getElementById('keyCriteria');
        if (criteriaList && this.resultsData.keyCriteria) {
            this.updateKeyCriteria(criteriaList, this.resultsData.keyCriteria);
        }

        // Selected country
        const countryEl = document.getElementById('selectedCountry');
        if (countryEl) {
            const countryNames = {
                'france': '🇫🇷 France',
                'usa': '🇺🇸 États-Unis',
                'canada': '🇨🇦 Canada',
                'uk': '🇬🇧 Royaume-Uni',
                'spain': '🇪🇸 Espagne',
                'germany': '🇩🇪 Allemagne'
            };
            countryEl.textContent = countryNames[this.resultsData.selectedCountry] || this.resultsData.selectedCountry;
        }
    }

    // 🎯 UPDATE KEY CRITERIA
    updateKeyCriteria(container, criteria) {
        container.innerHTML = '';

        criteria.forEach((criterion, index) => {
            setTimeout(() => {
                const li = document.createElement('li');
                li.className = 'criteria-item';
                li.style.opacity = '0';
                li.style.transform = 'translateX(-20px)';

                li.innerHTML = `
                    <i data-lucide="check-circle"></i>
                    <span>${criterion}</span>
                `;

                container.appendChild(li);

                // Re-create Lucide icons
                if (typeof lucide !== 'undefined') {
                    lucide.createIcons();
                }

                // Animate appearance
                setTimeout(() => {
                    li.style.transition = 'all 0.3s ease-out';
                    li.style.opacity = '1';
                    li.style.transform = 'translateX(0)';
                }, 50);

            }, index * 150);
        });
    }

    // 📍 UPDATE FOCUS SECTION
    updateFocusSection() {
        if (!this.resultsData || !this.resultsData.recommendations || this.resultsData.recommendations.length === 0) return;

        const topCity = this.resultsData.recommendations[0];

        // 🔥 FORCE: Générer les données dynamiques si manquantes
        if (!topCity.temperature_moyenne || topCity.temperature_moyenne === '--- °C') {
            topCity.temperature_moyenne = this.generateCityTemperature(topCity.nom, topCity.pays);
        }
        if (!topCity.compatibilites || topCity.compatibilites.length === 0) {
            topCity.compatibilites = this.generateCityCompatibilities(topCity.nom, topCity.pays);
        }

        // Update focus city name in title
        const focusTitle = document.getElementById('focusCityName');
        if (focusTitle) {
            focusTitle.textContent = topCity.nom || 'Ville #1';
        }

        // Update city details
        const populationEl = document.getElementById('cityPopulation');
        if (populationEl) {
            populationEl.textContent = topCity.population || 'Non disponible';
        }

        // ✨ NEW: Update city stats in the right container
        const populationStatEl = document.getElementById('cityPopulationStat');
        if (populationStatEl) {
            populationStatEl.textContent = topCity.population || '---';
        }

        const weatherStatEl = document.getElementById('cityWeatherStat');
        if (weatherStatEl) {
            weatherStatEl.textContent = topCity.temperature_moyenne || '--- °C';
        }

        // ✨ NEW: Update compatibilities
        this.updateCompatibilities(topCity);

        // Update score bars with animations
        this.updateScoreBar('costOfLivingBar', 'costOfLivingScore', topCity.cout_vie || 0, 1200);
        this.updateScoreBar('employmentBar', 'employmentScore', topCity.emploi || 0, 1400);
        this.updateScoreBar('cultureBar', 'cultureScore', topCity.culture || 0, 1600);
        this.updateScoreBar('qualityBar', 'qualityScore', topCity.qualite_vie || 0, 1800);
    }

    // ✨ NEW: UPDATE COMPATIBILITIES
    updateCompatibilities(city) {
        const compatibilities = city.compatibilites || [];

        // Update each compatibility item with animation
        for (let i = 1; i <= 3; i++) {
            const compatEl = document.getElementById(`compatibility${i}`);
            if (compatEl) {
                const compatibility = compatibilities[i - 1] || `${i}. Critère non défini`;

                // Add loading animation effect
                setTimeout(() => {
                    compatEl.style.opacity = '0';
                    setTimeout(() => {
                        compatEl.textContent = `${i}. ${compatibility}`;
                        compatEl.style.opacity = '1';
                        compatEl.style.transition = 'opacity 0.5s ease-in-out';
                    }, 200);
                }, i * 300); // Staggered animation
            }
        }
    }

    // 📊 UPDATE SCORE BAR
    updateScoreBar(barId, scoreId, value, delay) {
        setTimeout(() => {
            const bar = document.getElementById(barId);
            const scoreText = document.getElementById(scoreId);

            if (bar) {
                bar.style.width = `${value}%`;
                bar.style.transition = 'width 1s ease-out';
            }

            if (scoreText) {
                this.animateCounterNumber(scoreText, value, 1000, '/100');
            }
        }, delay);
    }

    // ⏰ UPDATE TIMESTAMPS
    updateTimestamps() {
        const dateEl = document.getElementById('analysisDate');
        if (dateEl && this.resultsData) {
            const date = new Date(this.resultsData.analysisDate);
            dateEl.textContent = date.toLocaleDateString('fr-FR');
        }
    }

    // 🎭 SETUP EVENT LISTENERS
    setupEventListeners() {
        console.log('🎭 Setting up event listeners...');

        // Header actions
        this.setupHeaderActions();

        // Hover effects
        this.setupHoverEffects();

        // Keyboard navigation
        this.setupKeyboardNavigation();

        console.log('✅ Event listeners ready');
    }

    // 🌟 SETUP HEADER ACTIONS
    setupHeaderActions() {
        // Help button
        const helpBtn = document.querySelector('[data-action="help"]');
        if (helpBtn) {
            helpBtn.addEventListener('click', () => {
                this.showHelpModal();
            });
        }

        // Restart button
        const restartBtn = document.querySelector('[data-action="restart"]');
        if (restartBtn) {
            restartBtn.addEventListener('click', () => {
                this.handleRestart();
            });
        }
    }

    // ✨ SETUP HOVER EFFECTS
    setupHoverEffects() {
        // Podium places hover
        const podiumPlaces = document.querySelectorAll('.podium-place');
        podiumPlaces.forEach(place => {
            place.addEventListener('mouseenter', () => {
                this.enhancePodiumHover(place);
            });
        });

        // Grid sections hover
        const gridSections = document.querySelectorAll('.grid-section');
        gridSections.forEach(section => {
            section.addEventListener('mouseenter', () => {
                this.addSectionGlow(section);
            });
        });
    }

    // ⌨️ SETUP KEYBOARD NAVIGATION
    setupKeyboardNavigation() {
        document.addEventListener('keydown', (e) => {
            switch (e.key) {
                case 'Escape':
                    this.hidePaymentModal();
                    break;
                case 'r':
                    if (e.ctrlKey || e.metaKey) {
                        e.preventDefault();
                        this.handleRestart();
                    }
                    break;
                case 'h':
                    if (e.ctrlKey || e.metaKey) {
                        e.preventDefault();
                        this.showHelpModal();
                    }
                    break;
            }
        });
    }

    // 🚀 ANIMATION METHODS

    // ✨ ANIMATE ELEMENT APPEARANCE
    animateElementAppearance(element, delay = 0) {
        element.style.opacity = '0';
        element.style.transform = 'translateY(20px)';

        setTimeout(() => {
            element.style.transition = 'all 0.5s ease-out';
            element.style.opacity = '1';
            element.style.transform = 'translateY(0)';
        }, delay);
    }

    // 📊 ANIMATE SCORE
    animateScore(element, targetScore, delay = 0) {
        setTimeout(() => {
            let currentScore = 0;
            const increment = targetScore / 50;
            const interval = setInterval(() => {
                currentScore += increment;
                if (currentScore >= targetScore) {
                    currentScore = targetScore;
                    clearInterval(interval);
                }
                element.textContent = Math.round(currentScore);
            }, 20);
        }, delay);
    }

    // 🔢 ANIMATE COUNTER NUMBER
    animateCounterNumber(element, target, delay = 0, suffix = '') {
        setTimeout(() => {
            let current = 0;
            const increment = target / 40;
            const interval = setInterval(() => {
                current += increment;
                if (current >= target) {
                    current = target;
                    clearInterval(interval);
                }
                element.textContent = Math.round(current) + suffix;
            }, 25);
        }, delay);
    }

    // ✨ ENHANCE PODIUM HOVER
    enhancePodiumHover(place) {
        const medal = place.querySelector('.medal-emoji');
        if (medal) {
            medal.style.transform = 'scale(1.2) rotate(10deg)';
            medal.style.transition = 'transform 0.3s ease-out';

            setTimeout(() => {
                medal.style.transform = 'scale(1) rotate(0deg)';
            }, 300);
        }
    }

    // 🌈 ADD SECTION GLOW
    addSectionGlow(section) {
        const originalBoxShadow = section.style.boxShadow;
        section.style.boxShadow = '0 25px 50px -12px rgba(102, 126, 234, 0.4)';

        setTimeout(() => {
            section.style.boxShadow = originalBoxShadow;
        }, 300);
    }

    // ⏳ SHOW LOADING OVERLAY
    showLoadingOverlay() {
        const overlay = document.getElementById('loadingOverlay');
        if (overlay) {
            overlay.classList.add('active');
        }
    }

    // ✅ HIDE LOADING OVERLAY
    hideLoadingOverlay() {
        const overlay = document.getElementById('loadingOverlay');
        if (overlay) {
            setTimeout(() => {
                overlay.classList.remove('active');
            }, 800); // Give time for animations to complete
        }
    }

    //  HANDLE RESTART
    handleRestart() {
        if (confirm('Êtes-vous sûr de vouloir recommencer le questionnaire ?')) {
            // Clear stored data
            localStorage.removeItem('zineinsight_results');
            localStorage.removeItem('questionnaire_answers');

            // Redirect to questionnaire
            window.location.href = '/questionnaire.html';
        }
    }

    // ❓ SHOW HELP MODAL
    showHelpModal() {
        alert('Aide ZineInsight:\n\n🏆 Vos 3 villes parfaites selon votre profil\n📊 Basé sur vos réponses au questionnaire\n📍 Détails de votre ville #1\n🚀 Options pour aller plus loin\n\nRaccourcis:\n• Ctrl+R : Recommencer\n• Ctrl+H : Aide\n• Échap : Fermer modal');
    }

    // ⏰ GET TIME AGO
    getTimeAgo(date) {
        const now = new Date();
        const diffMs = now - date;
        const diffMins = Math.floor(diffMs / 60000);
        const diffHours = Math.floor(diffMs / 3600000);
        const diffDays = Math.floor(diffMs / 86400000);

        if (diffMins < 1) return 'À l\'instant';
        if (diffMins < 60) return `Il y a ${diffMins} minute${diffMins > 1 ? 's' : ''}`;
        if (diffHours < 24) return `Il y a ${diffHours} heure${diffHours > 1 ? 's' : ''}`;
        if (diffDays < 7) return `Il y a ${diffDays} jour${diffDays > 1 ? 's' : ''}`;

        return date.toLocaleDateString('fr-FR');
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
            'Krakow': ['Histoire', 'Architecture', 'Jeunesse'],
            'Budapest': ['Thermes', 'Architecture', 'Coût accessible'],
            'Dublin': ['Tech hub', 'Culture pub', 'Anglophones'],
            'Edinburgh': ['Histoire', 'Festivals', 'Éducation'],
            'Copenhagen': ['Design scandinave', 'Vélo culture', 'Innovation'],
            'Stockholm': ['Innovation tech', 'Nature urbaine', 'Qualité de vie'],
            'Helsinki': ['Design', 'Innovation', 'Nature proche'],
            'Zurich': ['Finance', 'Montagnes', 'Qualité suisse'],
            'Milan': ['Mode', 'Business', 'Gastronomie'],
            'Rome': ['Histoire antique', 'Art', 'Dolce vita'],
            'Florence': ['Art Renaissance', 'Culture', 'Gastronomie'],
            'Madrid': ['Vie culturelle', 'Gastronomie', 'Énergie'],
            'Mexico City': ['Culture riche', 'Coût bas', 'Gastronomie'],
            'Buenos Aires': ['Tango', 'Architecture', 'Steakhouses'],
            'Medellín': ['Printemps éternel', 'Innovation', 'Coût accessible'],
            'Tokyo': ['Tech avancée', 'Culture unique', 'Sécurité'],
            'Seoul': ['K-culture', 'Tech', 'Dynamisme'],
            'Singapore': ['Business hub', 'Multiculturalité', 'Efficacité'],
            'Kuala Lumpur': ['Diversité', 'Coût accessible', 'Modernité'],
            'Dubai': ['Luxe', 'Business', 'Innovation'],
            'Cape Town': ['Nature', 'Vin', 'Diversité'],
            'Tel Aviv': ['Startup nation', 'Plages', 'Innovation'],
            'Sydney': ['Plages', 'Qualité de vie', 'Opportunités'],
            'Melbourne': ['Culture coffee', 'Art', 'Multiculturalité'],
            'Toronto': ['Diversité', 'Tech', 'Qualité canadienne'],
            'Vancouver': ['Nature urbaine', 'Multiculturalité', 'Qualité de vie'],
            'Montreal': ['Culture française', 'Festivals', 'Coût accessible'],
            'New York': ['Opportunités', 'Culture', 'Énergie'],
            'San Francisco': ['Tech capitale', 'Innovation', 'Liberté'],
            'Los Angeles': ['Industrie créative', 'Climat', 'Diversité'],
            'Chicago': ['Architecture', 'Culture', 'Coût raisonnable'],
            'Miami': ['Climat tropical', 'Business latino', 'Plages'],
            'Austin': ['Tech scene', 'Musique live', 'Créativité'],
            'Boston': ['Éducation', 'Tech', 'Histoire'],
            'Seattle': ['Tech giants', 'Nature', 'Culture coffee'],
            'Portland': ['Créativité', 'Durabilité', 'Bière artisanale'],
            'Denver': ['Montagnes', 'Cannabis légal', 'Outdoor lifestyle'],
            'Nashville': ['Musique country', 'Culture sud', 'Croissance'],
            'Atlanta': ['Business hub sud', 'Culture afro', 'Coût accessible'],
            'Phoenix': ['Climat sec', 'Coût accessible', 'Croissance'],
            'San Diego': ['Climat parfait', 'Plages', 'Biotech'],
            'Las Vegas': ['Divertissement', 'Pas d\'impôt état', 'Opportunités']
        };

        return cityStrengths[cityName] || ['Qualité de vie', 'Opportunités', 'Culture locale'];
    }

    // 🌡️ GENERATE CITY TEMPERATURE
    generateCityTemperature(cityName, countryName) {
        const cityTemperatures = {
            // Europe
            'Barcelona': '18°C', 'Madrid': '16°C', 'Valencia': '20°C', 'Seville': '22°C',
            'Lisboa': '19°C', 'Porto': '16°C', 'Berlin': '10°C', 'Munich': '9°C', 'Hamburg': '9°C',
            'Amsterdam': '11°C', 'Rome': '17°C', 'Milan': '14°C', 'Florence': '16°C', 'Naples': '18°C',
            'Vienna': '12°C', 'Prague': '10°C', 'Budapest': '12°C', 'Warsaw': '9°C',
            'Stockholm': '7°C', 'Copenhagen': '9°C', 'Helsinki': '6°C', 'Dublin': '10°C',
            'London': '11°C', 'Edinburgh': '9°C', 'Manchester': '10°C',
            'Zurich': '9°C', 'Geneva': '11°C', 'Brussels': '11°C', 'Luxembourg': '10°C',

            // Asia
            'Bangkok': '29°C', 'Tokyo': '16°C', 'Seoul': '13°C', 'Singapore': '28°C',
            'Hong Kong': '24°C', 'Kuala Lumpur': '28°C', 'Dubai': '28°C', 'Tel Aviv': '21°C',

            // Americas
            'New York': '13°C', 'San Francisco': '15°C', 'Los Angeles': '18°C', 'Chicago': '10°C',
            'Miami': '25°C', 'Austin': '20°C', 'Boston': '11°C', 'Seattle': '12°C',
            'Portland': '12°C', 'Denver': '10°C', 'Toronto': '9°C', 'Vancouver': '11°C', 'Montreal': '7°C',

            // Oceania & Africa
            'Sydney': '18°C', 'Melbourne': '15°C', 'Cape Town': '17°C',

            // France default
            'Paris': '12°C', 'Lyon': '14°C', 'Marseille': '17°C', 'Toulouse': '15°C',
            'Nice': '18°C', 'Nantes': '13°C', 'Strasbourg': '11°C', 'Montpellier': '16°C',
            'Bordeaux': '16°C', 'Lille': '11°C', 'Rennes': '12°C', 'Reims': '11°C'
        };

        return cityTemperatures[cityName] || '15°C';
    }

    // 🎯 GENERATE CITY COMPATIBILITIES
    generateCityCompatibilities(cityName, countryName) {
        const cityCompatibilities = {
            // Europe Tech & Culture
            'Barcelona': ['🎨 Scène créative vibrante', '🏖️ Lifestyle méditerranéen', '💼 Hub startup européen'],
            'Madrid': ['🏛️ Culture espagnole authentique', '🍷 Gastronomie d\'excellence', '💼 Centre économique majeur'],
            'Lisboa': ['🌊 Qualité de vie océanique', '💰 Coût abordable Europe', '🎵 Culture portugaise riche'],
            'Berlin': ['🎭 Scène alternative unique', '💡 Écosystème startup', '💰 Coût accessible Europe'],
            'Amsterdam': ['🚲 Mobilité verte parfaite', '🌍 Ouverture internationale', '💼 Hub financier européen'],
            'Rome': ['🏛️ Patrimoine millénaire', '🍝 Gastronomie authentique', '🎨 Art à chaque coin'],
            'Vienna': ['🎼 Capitale musicale mondiale', '☕ Culture café viennoise', '🏛️ Architecture impériale'],
            'Prague': ['🏰 Beauté architecturale', '🍺 Culture bière authentique', '💰 Coût de vie attractif'],
            'London': ['💼 Hub financier mondial', '🎭 Scène culturelle riche', '🌍 Diversité cosmopolite'],
            'Zurich': ['💰 Stabilité financière', '🏔️ Nature alpine proche', '🔬 Innovation technologique'],

            // Asia Modern
            'Bangkok': ['🍜 Street food légendaire', '💰 Coût de vie ultra-bas', '🏛️ Culture thaï authentique'],
            'Tokyo': ['🗾 Innovation technologique', '🍱 Gastronomie raffinée', '🚄 Infrastructure parfaite'],
            'Seoul': ['📱 Tech avant-gardiste', '🎵 K-culture dynamique', '🍲 Cuisine coréenne'],
            'Singapore': ['🏙️ Efficacité urbaine parfaite', '🍜 Melting-pot culinaire', '💼 Hub business Asie'],
            'Hong Kong': ['🏢 Dynamisme économique', '🍜 Fusion culinaire', '🌆 Skyline légendaire'],
            'Dubai': ['💎 Luxe architectural', '💼 Hub business Moyen-Orient', '🌴 Lifestyle premium'],

            // Americas Dynamic
            'New York': ['💼 Opportunités infinies', '🎭 Capitale culturelle', '🌍 Melting-pot mondial'],
            'San Francisco': ['💻 Silicon Valley énergie', '🌁 Beauté naturelle', '💡 Innovation constante'],
            'Los Angeles': ['🎬 Industrie créative', '☀️ Climat californien', '🌮 Diversité culinaire'],
            'Toronto': ['🍁 Qualité canadienne', '🌍 Diversité multiculturelle', '💼 Économie dynamique'],
            'Vancouver': ['🏔️ Nature spectaculaire', '🌧️ Climat tempéré', '🎬 Industrie du film'],
            'Montreal': ['🇫🇷 Culture française Amérique', '🎪 Festivals toute l\'année', '💰 Coût abordable'],

            // Oceania & Unique
            'Sydney': ['🏖️ Plages urbaines parfaites', '☀️ Lifestyle décontracté', '💼 Opportunités Pacifique'],
            'Melbourne': ['☕ Culture café mondiale', '🎨 Scène artistique', '🏏 Sport passion'],
            'Cape Town': ['🍷 Vignobles mondiaux', '🏔️ Beauté naturelle unique', '🌍 Diversité culturelle'],

            // France default
            'Paris': ['🥐 Art de vivre parisien', '🎭 Culture mondiale', '💼 Hub européen'],
            'Lyon': ['🍽️ Capital gastronomique', '💡 Innovation technologique', '🏛️ Patrimoine UNESCO'],
            'Bordeaux': ['🍷 Capital mondial du vin', '🏛️ Architecture classique', '🚄 Accessibilité TGV'],
            'Marseille': ['🌊 Lifestyle méditerranéen', '🌍 Diversité culturelle', '☀️ Soleil toute l\'année'],
            'Toulouse': ['✈️ Capitale aérospatiale', '🎓 Ville étudiante', '🌸 Douceur de vivre'],
            'Nice': ['🏖️ Riviera française', '☀️ 300 jours de soleil', '🎨 Inspiration artistique'],
            'Nantes': ['🌱 Innovation verte', '🎨 Créativité urbaine', '🚊 Transport écologique'],
            'Montpellier': ['🎓 Jeunesse dynamique', '🌊 Proximité mer', '☀️ Climat ensoleillé']
        };

        return cityCompatibilities[cityName] || [
            '🏙️ Opportunités urbaines',
            '🌍 Ouverture internationale',
            '💡 Potentiel de développement'
        ];
    }

    // 🧮 CALCULATE MATCH PERCENTAGE
    calculateMatchPercentage(recommendations) {
        if (!recommendations || recommendations.length === 0) return 0;

        const avgScore = recommendations.reduce((sum, city) => sum + (city.score_final || 0), 0) / recommendations.length;
        return Math.round(avgScore);
    }

    // 🎯 EXTRACT KEY CRITERIA
    extractKeyCriteria(answers) {
        const criteria = [];

        // Analyze answers to extract key criteria
        if (answers.budget === 'low') criteria.push('Budget modéré');
        if (answers.budget === 'high') criteria.push('Budget élevé');
        if (answers.family === 'yes' || answers.family === 'famille') criteria.push('Adapté à la famille');
        if (answers.job === 'tech') criteria.push('Opportunités tech');
        if (answers.job === 'creative') criteria.push('Secteur créatif');
        if (answers.culture === 'important') criteria.push('Culture importante');
        if (answers.securite === 'importante') criteria.push('Sécurité prioritaire');

        // Add default criteria if none found
        if (criteria.length === 0) {
            criteria.push('Qualité de vie', 'Opportunités professionnelles', 'Coût de la vie', 'Environnement urbain');
        }

        return criteria.slice(0, 6); // Limit to 6 criteria
    }

    // ❌ HANDLE INITIALIZATION ERROR
    handleInitializationError(error) {
        console.error('❌ Initialization error:', error);

        const loadingOverlay = document.getElementById('loadingOverlay');
        if (loadingOverlay) {
            loadingOverlay.innerHTML = `
                <div class="loading-content error-content">
                    <div class="error-icon">
                        <i data-lucide="alert-circle"></i>
                    </div>
                    <h3 class="error-title">Oops ! Une erreur est survenue</h3>
                    <p class="error-subtitle">Impossible de charger vos résultats</p>
                    <div class="error-actions">
                        <button class="btn primary" onclick="location.reload()">
                            <i data-lucide="refresh-cw"></i>
                            Réessayer
                        </button>
                        <button class="btn secondary" onclick="location.href='/questionnaire.html'">
                            <i data-lucide="arrow-left"></i>
                            Retour au questionnaire
                        </button>
                    </div>
                </div>
            `;

            // Re-create Lucide icons
            if (typeof lucide !== 'undefined') {
                lucide.createIcons();
            }
        }
    }
}

// 🚀 INITIALIZE REVOLUTIONARY RESULTS MANAGER
const resultsManager = new RevolutionaryResultsManager();

// 🌟 GLOBAL ACCESS FOR DEBUGGING
window.resultsManager = resultsManager;

// 🎯 DEBUG FUNCTIONS FOR TESTING
window.testResults = () => {
    console.log('🎯 Generating test results...');
    resultsManager.generateDemoResults();
    setTimeout(() => {
        location.reload();
    }, 500);
};

window.clearResults = () => {
    console.log('🗑️ Clearing all results...');
    localStorage.removeItem('zineinsight_results');
    localStorage.removeItem('questionnaire_answers');
    location.reload();
};

console.log('🚀 Revolutionary Results JavaScript Loaded!')
console.log('💡 Debug commands: testResults(), clearResults(), debugCityMapping()');

// 🐛 DEBUG FUNCTION pour tester le mapping des villes - VERSION SIMPLIFIÉE
window.debugCityMapping = () => {
    console.log('🔍 Testing simplified city mapping system...');

    // Test villes de différents pays
    const testCities = [
        // 🇺🇸 USA
        'Austin', 'Memphis', 'Pittsburgh', 'Louisville', 'New York', 'Los Angeles',
        // 🇫🇷 France
        'Paris', 'Lyon', 'Bordeaux', 'Marseille', 'Avignon', 'Dijon', 'Montpellier',
        // 🇬🇧 UK
        'London', 'Manchester', 'Edinburgh',
        // 🇯🇵 Japan
        'Tokyo', 'Osaka', 'Kyoto',
        // 🇹🇭 Thailand
        'Bangkok', 'Chiang Mai', 'Phuket',
        // 🇩🇪 Germany
        'Berlin', 'Munich', 'Hamburg',
        // 🇪🇸 Spain
        'Madrid', 'Barcelona', 'Valencia',
        // 🇲🇦 Morocco
        'Casablanca', 'Rabat', 'Marrakech',
        // 🇨🇦 Canada
        'Toronto', 'Vancouver', 'Montreal',
        // Villes sans guide
        'Sydney', 'Rome', 'Amsterdam'
    ];

    console.log('\n🧪 TESTING SIMPLIFIED CITY → GUIDE MAPPING:');
    console.log('==========================================');

    // Test le pays sélectionné actuel
    const currentCountry = window.resultsManager?.resultsData?.selectedCountry;
    console.log(`🌍 Current selected country: ${currentCountry || 'Not found'}`);
    if (currentCountry) {
        const countryGuide = getCountryGuide(currentCountry);
        console.log(`🎯 Country guide: ${countryGuide || 'No guide'}`);
    }

    console.log('\n📊 CITY MAPPING RESULTS:');
    testCities.forEach(city => {
        const guide = getCityCountryGuideV2(city);
        const status = guide ? '✅' : '❌';
        console.log(`${status} ${city.padEnd(15)} → ${guide || 'NO GUIDE FOUND'}`);
    });

    console.log('\n📊 SUMMARY:');
    const successful = testCities.filter(city => getCityCountryGuideV2(city)).length;
    const failed = testCities.length - successful;
    console.log(`✅ Successful mappings: ${successful}/${testCities.length}`);
    console.log(`❌ Failed mappings: ${failed}/${testCities.length}`);
    console.log(`📈 Success rate: ${Math.round(successful / testCities.length * 100)}%`);

    // Test du mapping par pays direct
    console.log('\n🌍 COUNTRY DIRECT MAPPING TEST:');
    const countries = ['france', 'usa', 'uk', 'germany', 'spain', 'japan', 'thailand', 'morocco', 'canada', 'brazil', 'australia'];
    countries.forEach(country => {
        const guide = getGuideFromCountryName(country);
        const status = guide ? '✅' : '❌';
        console.log(`${status} ${country.padEnd(12)} → ${guide || 'NO GUIDE'}`);
    });
};

// ====================================
//    📱 SOCIAL SHARING FUNCTIONALITY
// ====================================

// Initialize social buttons when DOM is ready
document.addEventListener('DOMContentLoaded', function () {
    initializeSocialButtons();
});

function initializeSocialButtons() {
    const socialButtons = document.querySelectorAll('.social-mini');

    socialButtons.forEach(button => {
        button.addEventListener('click', function () {
            const platform = this.dataset.platform;
            const cityName = document.getElementById('focusCityName')?.textContent || 'Ma ville parfaite';

            // Generate sharing content
            const shareText = `🏆 J'ai découvert ma ville parfaite : ${cityName} ! Découvre la tienne avec ZineInsight ✨`;
            const shareUrl = window.location.origin;

            // Platform-specific sharing
            switch (platform) {
                case 'whatsapp':
                    shareToWhatsApp(shareText, shareUrl);
                    break;
                case 'instagram':
                    shareToInstagram(shareText);
                    break;
                case 'facebook':
                    shareToFacebook(shareText, shareUrl);
                    break;
                case 'x':
                case 'twitter':
                    shareToX(shareText, shareUrl);
                    break;
            }
        });
    });
}

// Platform-specific sharing functions
function shareToWhatsApp(text, url) {
    const message = `${text}\n\n${url}`;
    const whatsappUrl = `https://wa.me/?text=${encodeURIComponent(message)}`;
    window.open(whatsappUrl, '_blank', 'noopener,noreferrer');
}

function shareToInstagram(text) {
    // Instagram doesn't support direct URL sharing, copy to clipboard
    if (navigator.clipboard) {
        navigator.clipboard.writeText(text).then(() => {
            showShareNotification('📋 Texte copié ! Ouvre Instagram et colle-le dans une story');
        });
    } else {
        showShareNotification('📱 Ouvre Instagram et partage ton résultat !');
    }
}

function shareToFacebook(text, url) {
    const facebookUrl = `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(url)}&quote=${encodeURIComponent(text)}`;
    window.open(facebookUrl, '_blank', 'width=600,height=400,noopener,noreferrer');
}

function shareToX(text, url) {
    const xUrl = `https://x.com/intent/tweet?text=${encodeURIComponent(text)}&url=${encodeURIComponent(url)}`;
    window.open(xUrl, '_blank', 'width=600,height=400,noopener,noreferrer');
}

// Show notification after sharing
function showShareNotification(message) {
    // Create notification element
    const notification = document.createElement('div');
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: #10B981;
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 12px;
        font-weight: 600;
        z-index: 9999;
        transform: translateX(100%);
        transition: transform 0.3s ease;
        max-width: 300px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
    `;
    notification.textContent = message;
    document.body.appendChild(notification);

    // Animate in
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 10);

    // Animate out and remove
    setTimeout(() => {
        notification.style.transform = 'translateX(100%)';
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 3000);
}

// ====================================
//    🗺️ CITY TO COUNTRY GUIDE MAPPING - AUTO-GENERATED FROM JSON DATA
// ====================================

// 🎯 AUTO-GENERATE CITY MAPPING FROM JSON DATA
async function loadCityMappingFromJSON() {
    const cityToGuideMap = {};

    // Mapping des fichiers JSON vers les guides HTML
    const jsonToGuideMapping = {
        'villes_usa_residents.json': 'usa.html',
        'villes_france_residents.json': 'france.html',
        'villes_uk_residents.json': 'uk.html',
        'villes_germany_residents.json': 'allemagne.html',
        'villes_spain_residents.json': 'espagne.html',
        'villes_japan_residents.json': 'japon.html',
        'villes_thailand_residents.json': 'thailande.html',
        'villes_morocco_residents.json': 'maroc.html',
        'villes_canada_residents.json': 'canada.html',
        // Pays sans guides HTML pour l'instant - fallback vers pages génériques
        'villes_brazil_residents.json': null, // Pas de guide brésil pour l'instant
        'villes_australia_residents.json': null, // Pas de guide australie pour l'instant
        'villes_mexico_residents.json': null // Pas de guide mexique pour l'instant
    };

    try {
        for (const [jsonFile, guideFile] of Object.entries(jsonToGuideMapping)) {
            try {
                // Try multiple paths for JSON files - FIXED PATHS
                const possiblePaths = [
                    `/platform/backend/data_v2/${jsonFile}`,
                    `../../backend/data_v2/${jsonFile}`,
                    `../backend/data_v2/${jsonFile}`,
                    `/backend/data_v2/${jsonFile}`,
                    `http://localhost:8000/platform/backend/data_v2/${jsonFile}`
                ];

                let data = null;
                for (const path of possiblePaths) {
                    try {
                        const response = await fetch(path);
                        if (response.ok) {
                            data = await response.json();
                            console.log(`✅ Successfully loaded ${jsonFile} from ${path}`);
                            break;
                        }
                    } catch (pathError) {
                        // Continue to next path
                        continue;
                    }
                }

                if (data && data.cities && Array.isArray(data.cities)) {
                    data.cities.forEach(city => {
                        if (city.name && guideFile) { // Only map if guide exists
                            cityToGuideMap[city.name] = guideFile;
                            console.log(`🗺️ Mapped ${city.name} → ${guideFile}`);
                        }
                    });
                } else if (!data) {
                    console.warn(`⚠️ Could not load ${jsonFile} from any path`);
                }
            } catch (error) {
                console.warn(`⚠️ Could not load ${jsonFile}:`, error);
            }
        }

        console.log(`✅ Generated city mapping with ${Object.keys(cityToGuideMap).length} cities`);
        return cityToGuideMap;

    } catch (error) {
        console.error('❌ Error loading city mappings:', error);
        return {};
    }
}

// Global city mapping cache
let CITY_TO_GUIDE_CACHE = null;

// 🗺️ SMART INTERNATIONAL COUNTRY DETECTION FROM CITY NAME
function detectCountryFromCity(cityName) {
    // Mapping intelligent ville → pays pour le système international 201 villes
    const cityToCountryMap = {
        // 🇺🇸 USA - Major cities
        'New York': 'usa', 'Los Angeles': 'usa', 'Chicago': 'usa', 'Houston': 'usa', 'Phoenix': 'usa',
        'Philadelphia': 'usa', 'San Antonio': 'usa', 'San Diego': 'usa', 'Dallas': 'usa', 'San Jose': 'usa',
        'Austin': 'usa', 'Jacksonville': 'usa', 'Fort Worth': 'usa', 'Columbus': 'usa', 'Charlotte': 'usa',
        'San Francisco': 'usa', 'Indianapolis': 'usa', 'Seattle': 'usa', 'Denver': 'usa', 'Boston': 'usa',
        'Memphis': 'usa', 'Pittsburgh': 'usa', 'Louisville': 'usa', 'Miami': 'usa', 'Las Vegas': 'usa',
        'Portland': 'usa', 'Nashville': 'usa', 'Atlanta': 'usa',

        // 🇫🇷 France - Villes principales
        'Paris': 'france', 'Marseille': 'france', 'Lyon': 'france', 'Toulouse': 'france', 'Nice': 'france',
        'Nantes': 'france', 'Strasbourg': 'france', 'Montpellier': 'france', 'Bordeaux': 'france', 'Lille': 'france',
        'Rennes': 'france', 'Reims': 'france', 'Le Havre': 'france', 'Saint-Étienne': 'france', 'Toulon': 'france',
        'Angers': 'france', 'Grenoble': 'france', 'Dijon': 'france', 'Nîmes': 'france', 'Aix-en-Provence': 'france',
        'Avignon': 'france', 'Clermont-Ferrand': 'france', 'Tours': 'france', 'Limoges': 'france', 'Villeurbanne': 'france',

        // 🇬🇧 UK - Major cities
        'London': 'uk', 'Birmingham': 'uk', 'Liverpool': 'uk', 'Leeds': 'uk', 'Glasgow': 'uk',
        'Sheffield': 'uk', 'Bradford': 'uk', 'Edinburgh': 'uk', 'Manchester': 'uk', 'Bristol': 'uk',

        // 🇩🇪 Germany - Major cities
        'Berlin': 'germany', 'Hamburg': 'germany', 'Munich': 'germany', 'Cologne': 'germany', 'Frankfurt': 'germany',
        'Stuttgart': 'germany', 'Düsseldorf': 'germany', 'Dortmund': 'germany', 'Essen': 'germany', 'Leipzig': 'germany',

        // 🇪🇸 Spain - Major cities
        'Madrid': 'spain', 'Barcelona': 'spain', 'Valencia': 'spain', 'Seville': 'spain', 'Zaragoza': 'spain',
        'Málaga': 'spain', 'Murcia': 'spain', 'Palma': 'spain', 'Las Palmas': 'spain', 'Bilbao': 'spain',

        // 🇯🇵 Japan - Major cities
        'Tokyo': 'japan', 'Yokohama': 'japan', 'Osaka': 'japan', 'Nagoya': 'japan', 'Sapporo': 'japan',
        'Fukuoka': 'japan', 'Kobe': 'japan', 'Kawasaki': 'japan', 'Kyoto': 'japan', 'Saitama': 'japan',

        // 🇹🇭 Thailand - Major cities
        'Bangkok': 'thailand', 'Chiang Mai': 'thailand', 'Pattaya': 'thailand', 'Phuket': 'thailand', 'Hat Yai': 'thailand',

        // 🇲🇦 Morocco - Major cities
        'Casablanca': 'morocco', 'Rabat': 'morocco', 'Fès': 'morocco', 'Marrakech': 'morocco', 'Agadir': 'morocco',
        'Tangier': 'morocco', 'Meknès': 'morocco', 'Salé': 'morocco', 'Tétouan': 'morocco', 'Oujda': 'morocco',

        // 🇨🇦 Canada - Major cities
        'Toronto': 'canada', 'Montreal': 'canada', 'Calgary': 'canada', 'Ottawa': 'canada', 'Edmonton': 'canada',
        'Mississauga': 'canada', 'Winnipeg': 'canada', 'Vancouver': 'canada', 'Quebec City': 'canada', 'Hamilton': 'canada'
    };

    return cityToCountryMap[cityName] || null;
}

// 🌍 SMART COUNTRY ID TO GUIDE MAPPING - PERFECT FOR 201 CITIES
function getGuideFromCountryID(countryId) {
    console.log('🔍 Getting guide for country ID:', countryId);

    // Direct mapping country ID → guide HTML
    const countryIdToGuideMap = {
        'fr': 'france.html',
        'us': 'usa.html',
        'ca': 'canada.html',
        'uk': 'uk.html',
        'de': 'allemagne.html',
        'es': 'espagne.html',
        'jp': 'japon.html',
        'th': 'thailande.html',
        'ma': 'maroc.html',

        // Pays sans guides → null (message "à venir")
        'br': null, // Brazil
        'au': null, // Australia
        'mx': null, // Mexico
        'it': null, // Italy
        'pt': null, // Portugal
        'nl': null, // Netherlands
        'se': null, // Sweden
        'no': null, // Norway
        'dk': null, // Denmark
        'fi': null, // Finland
        'ie': null, // Ireland
        'be': null, // Belgium
        'ch': null, // Switzerland
        'at': null, // Austria
        'pl': null, // Poland
        'cz': null, // Czech Republic
        'hu': null, // Hungary
        'ro': null, // Romania
        'bg': null, // Bulgaria
        'hr': null, // Croatia
        'rs': null, // Serbia
        'gr': null, // Greece
        'tr': null, // Turkey
        'il': null, // Israel
        'ae': null, // UAE
        'sg': null, // Singapore
        'my': null, // Malaysia
        'id': null, // Indonesia
        'ph': null, // Philippines
        'vn': null, // Vietnam
        'kr': null, // South Korea
        'cn': null, // China
        'in': null, // India
        'ru': null, // Russia
        'ua': null, // Ukraine
        'za': null, // South Africa
        'eg': null, // Egypt
        'ng': null, // Nigeria
        'ke': null, // Kenya
        'cl': null, // Chile
        'ar': null, // Argentina
        'co': null, // Colombia
        'pe': null, // Peru
        'ec': null, // Ecuador
        'uy': null, // Uruguay
        'py': null, // Paraguay
        'bo': null, // Bolivia
        've': null  // Venezuela
    };

    const guide = countryIdToGuideMap[countryId?.toLowerCase()] || null;
    console.log('📖 Guide for country ID:', guide || 'No guide available');
    return guide;
}

function getCityCountryGuide(cityName) {
    console.log('🔍 Getting guide for city:', cityName);

    // � PRIORITÉ 1: Utiliser le pays sélectionné dans le questionnaire
    if (window.resultsManager && window.resultsManager.resultsData) {
        const selectedCountry = window.resultsManager.resultsData.selectedCountry;
        if (selectedCountry) {
            console.log('🌍 Using selected country from questionnaire:', selectedCountry);
            const guide = getCountryGuide(selectedCountry);
            if (guide) {
                console.log('✅ Guide found via selected country:', guide);
                return guide;
            }
        }
    }

    // 🎯 PRIORITÉ 2: Fallback pour villes spécifiques non couvertes
    const cityFallbacks = {
        // Villes US populaires
        'New York': 'usa.html',
        'Los Angeles': 'usa.html',
        'San Francisco': 'usa.html',
        'Chicago': 'usa.html',
        'Miami': 'usa.html',
        'Seattle': 'usa.html',
        'Boston': 'usa.html',
        'Las Vegas': 'usa.html',

        // Villes EU populaires
        'London': 'uk.html',
        'Londres': 'uk.html',
        'Manchester': 'uk.html',
        'Edinburgh': 'uk.html',

        'Paris': 'france.html',
        'Lyon': 'france.html',
        'Marseille': 'france.html',
        'Bordeaux': 'france.html',
        'Toulouse': 'france.html',

        'Berlin': 'allemagne.html',
        'Munich': 'allemagne.html',
        'Hamburg': 'allemagne.html',

        'Madrid': 'espagne.html',
        'Barcelona': 'espagne.html',
        'Valencia': 'espagne.html',

        'Tokyo': 'japon.html',
        'Osaka': 'japon.html',
        'Kyoto': 'japon.html',

        'Bangkok': 'thailande.html',
        'Chiang Mai': 'thailande.html',
        'Phuket': 'thailande.html',

        'Casablanca': 'maroc.html',
        'Rabat': 'maroc.html',
        'Marrakech': 'maroc.html',

        'Toronto': 'canada.html',
        'Vancouver': 'canada.html',
        'Montreal': 'canada.html'
    };

    if (cityFallbacks[cityName]) {
        console.log('🎯 Guide found via city fallback:', cityFallbacks[cityName]);
        return cityFallbacks[cityName];
    }

    console.log('❌ No guide found for city:', cityName);
    return null; // Will show "Guide à venir" message
}

// 🎯 NEW ENHANCED CITY GUIDE FUNCTION WITH COUNTRY ID SUPPORT
function getCityCountryGuideV2(cityName, cityData = null) {
    console.log('🔍 Getting guide for city:', cityName, 'with data:', cityData);

    // 🎯 PRIORITÉ 1: Utiliser le country_id de la ville si disponible (NOUVEAU SYSTÈME 201 VILLES)
    if (cityData && cityData.country_id) {
        console.log('🆔 Using country_id from city data:', cityData.country_id);
        const guide = getGuideFromCountryID(cityData.country_id);
        if (guide) {
            console.log('✅ Guide found via country_id:', guide);
            return guide;
        }
    }

    // 🌍 PRIORITÉ 2: Utiliser le pays sélectionné dans le questionnaire
    if (window.resultsManager && window.resultsManager.resultsData) {
        const selectedCountry = window.resultsManager.resultsData.selectedCountry;
        if (selectedCountry) {
            console.log('🌍 Using selected country from questionnaire:', selectedCountry);
            const guide = getGuideFromCountryName(selectedCountry);
            if (guide) {
                console.log('✅ Guide found via selected country:', guide);
                return guide;
            }
        }
    }

    // 🔍 PRIORITÉ 3: Détecter le pays depuis le nom de ville
    const detectedCountryId = detectCountryFromCity(cityName);
    if (detectedCountryId) {
        console.log('🔍 Country detected from city name:', detectedCountryId);
        const guide = getGuideFromCountryID(detectedCountryId);
        if (guide) {
            console.log('✅ Guide found via city detection:', guide);
            return guide;
        }
    }

    // 🎯 PRIORITÉ 4: Fallback pour villes spécifiques non couvertes
    const cityFallbacks = {
        // Villes US populaires
        'New York': 'usa.html', 'Los Angeles': 'usa.html', 'San Francisco': 'usa.html',
        'Chicago': 'usa.html', 'Miami': 'usa.html', 'Seattle': 'usa.html', 'Boston': 'usa.html',
        'Las Vegas': 'usa.html', 'Austin': 'usa.html', 'Memphis': 'usa.html', 'Pittsburgh': 'usa.html',

        // Villes EU populaires
        'London': 'uk.html', 'Londres': 'uk.html', 'Manchester': 'uk.html', 'Edinburgh': 'uk.html',
        'Paris': 'france.html', 'Lyon': 'france.html', 'Marseille': 'france.html', 'Bordeaux': 'france.html',
        'Toulouse': 'france.html', 'Montpellier': 'france.html', 'Avignon': 'france.html', 'Dijon': 'france.html',
        'Berlin': 'allemagne.html', 'Munich': 'allemagne.html', 'Hamburg': 'allemagne.html',
        'Madrid': 'espagne.html', 'Barcelona': 'espagne.html', 'Valencia': 'espagne.html',
        'Tokyo': 'japon.html', 'Osaka': 'japon.html', 'Kyoto': 'japon.html',
        'Bangkok': 'thailande.html', 'Chiang Mai': 'thailande.html', 'Phuket': 'thailande.html',
        'Casablanca': 'maroc.html', 'Rabat': 'maroc.html', 'Marrakech': 'maroc.html',
        'Toronto': 'canada.html', 'Vancouver': 'canada.html', 'Montreal': 'canada.html'
    };

    if (cityFallbacks[cityName]) {
        console.log('🎯 Guide found via city fallback:', cityFallbacks[cityName]);
        return cityFallbacks[cityName];
    }

    console.log('❌ No guide found for city:', cityName);
    return null; // Will show "Guide à venir" message
}

// 🌍 HELPER: Country name to guide mapping (pour compatibilité questionnaire)
function getGuideFromCountryName(countryName) {
    const countryNameToGuideMap = {
        'france': 'france.html',
        'usa': 'usa.html',
        'united-states': 'usa.html',
        'canada': 'canada.html',
        'uk': 'uk.html',
        'united-kingdom': 'uk.html',
        'germany': 'allemagne.html',
        'allemagne': 'allemagne.html',
        'spain': 'espagne.html',
        'espagne': 'espagne.html',
        'japan': 'japon.html',
        'japon': 'japon.html',
        'thailand': 'thailande.html',
        'thailande': 'thailande.html',
        'morocco': 'maroc.html',
        'maroc': 'maroc.html'
    };

    return countryNameToGuideMap[countryName?.toLowerCase()] || null;
}

// Initialize guide button functionality
document.addEventListener('DOMContentLoaded', function () {
    // 🎯 Load city mapping from JSON data
    loadCityMappingFromJSON().then(cityMapping => {
        CITY_TO_GUIDE_CACHE = cityMapping;
        console.log('✅ City to guide mapping loaded:', Object.keys(cityMapping).length, 'cities');
    }).catch(error => {
        console.warn('⚠️ Could not load city mappings, using fallback:', error);
        CITY_TO_GUIDE_CACHE = {};
    });

    const guideBtn = document.querySelector('.guide-btn-main');
    if (guideBtn) {
        guideBtn.addEventListener('click', function () {
            const cityName = document.getElementById('focusCityName')?.textContent || 'Paris';
            console.log('🗺️ Opening guide for city:', cityName);

            // Obtenir le guide pays correspondant avec le nouveau système country ID
            const topCity = window.resultsManager?.resultsData?.recommendations?.[0];
            const guideFile = getCityCountryGuideV2(cityName, topCity);
            console.log('📖 Guide file:', guideFile);

            if (guideFile) {
                // Ouvrir le guide pays
                window.open(guideFile, '_blank', 'noopener,noreferrer');
            } else {
                // Afficher message d'attente
                showShareNotification('📖 Guide à venir pour cette destination ! Nous travaillons dessus...');
            }
        });
    }
});

// ===== ZINE COACH IA POUR RESULTS =====
class ResultsAICoach {
    constructor() {
        this.avatar = document.getElementById('zine-avatar');
        this.bubble = document.getElementById('zine-bubble');
        this.message = document.getElementById('zine-message');
        this.isMessageVisible = false;
        this.messageTimeout = null;
        this.lastComment = '';
        this.resultsData = null;

        this.init();
    }

    init() {
        if (!this.avatar || !this.bubble || !this.message) {
            console.log('Éléments de l\'assistant Zine non trouvés');
            return;
        }

        // Event listeners
        this.avatar.addEventListener('click', () => this.showContextualTip());

        // Message de bienvenue après chargement des résultats
        setTimeout(() => {
            this.showResultsWelcomeMessage();
        }, 3000);

        // Écouter les données de résultats
        this.setupResultsListener();
    }

    setupResultsListener() {
        // Observer quand les résultats sont chargés
        const observer = new MutationObserver(() => {
            const city1Name = document.getElementById('city1Name')?.textContent;
            if (city1Name && city1Name !== 'Chargement...' && !this.resultsData) {
                this.onResultsLoaded();
            }
        });

        observer.observe(document.body, { childList: true, subtree: true });
    }

    onResultsLoaded() {
        // Récupérer les données des résultats
        this.resultsData = {
            city1: document.getElementById('city1Name')?.textContent || 'Ville 1',
            city2: document.getElementById('city2Name')?.textContent || 'Ville 2',
            city3: document.getElementById('city3Name')?.textContent || 'Ville 3',
            score1: document.getElementById('city1Score')?.textContent || '90',
            score2: document.getElementById('city2Score')?.textContent || '85',
            score3: document.getElementById('city3Score')?.textContent || '80'
        };

        // Générer un commentaire personnalisé après un délai
        setTimeout(() => {
            this.generateResultsComment();
        }, 5000);
    }

    generateResultsComment() {
        if (!this.resultsData) return;

        const { city1, score1 } = this.resultsData;

        // Commentaires dynamiques basés sur les résultats avec i18n AMÉLIORÉ
        const resultComments = [
            window.revolutionaryI18n ?
                window.revolutionaryI18n.translate('zine.results.comment_excellent', null, { city: city1, score: score1 }) :
                `🎯 ${city1} avec ${score1}/100 ! Un excellent match pour ton profil !`,
            window.revolutionaryI18n ?
                window.revolutionaryI18n.translate('zine.results.comment_analysis', null, { city: city1, score: score1 }) :
                `✨ Analyse terminée ! ${city1} sort du lot avec ${score1}% de compatibilité !`,
            window.revolutionaryI18n ?
                window.revolutionaryI18n.translate('zine.results.comment_top', null, { city: city1 }) :
                `🏆 Top résultat : ${city1} ! L'IA a détecté une synergie parfaite !`,
            window.revolutionaryI18n ?
                window.revolutionaryI18n.translate('zine.results.comment_first', null, { city: city1 }) :
                `🚀 ${city1} en première position ! Cette ville correspond à tes critères !`,
            window.revolutionaryI18n ?
                window.revolutionaryI18n.translate('zine.results.comment_impressive', null, { city: city1, score: score1 }) :
                `💡 Résultat impressionnant : ${city1} score ${score1}/100 selon ton profil !`
        ];

        const randomComment = resultComments[Math.floor(Math.random() * resultComments.length)];
        this.showMessage(randomComment, 8000);
    } showResultsWelcomeMessage() {
        const welcomeMessages = [
            window.revolutionaryI18n ?
                window.revolutionaryI18n.translate('zine.results.congratulations') :
                "Félicitations ! Tes résultats sont prêts ! 🎉",
            window.revolutionaryI18n ?
                window.revolutionaryI18n.translate('zine.results.analysis_done') :
                "Analyse terminée ! Découvre tes villes parfaites ! ✨",
            window.revolutionaryI18n ?
                window.revolutionaryI18n.translate('zine.results.mission_accomplished') :
                "Mission accomplie ! Voici ton top 3 personnalisé ! 🏆",
            window.revolutionaryI18n ?
                window.revolutionaryI18n.translate('zine.results.ai_has_spoken') :
                "L'IA a parlé ! Tes destinations idéales t'attendent ! 🌍"
        ];

        const randomWelcome = welcomeMessages[Math.floor(Math.random() * welcomeMessages.length)];
        this.showMessage(randomWelcome, 6000);
    } showContextualTip() {
        const tips = [
            window.revolutionaryI18n ?
                window.revolutionaryI18n.translate('zine.results.tip_click_city') :
                "💡 Clique sur chaque ville pour plus de détails !",
            window.revolutionaryI18n ?
                window.revolutionaryI18n.translate('zine.results.tip_guide') :
                "🗺️ Le bouton 'Guide' te donne des infos pratiques !",
            window.revolutionaryI18n ?
                window.revolutionaryI18n.translate('zine.results.tip_score') :
                "📊 Ton score reflète la compatibilité avec tes critères !",
            window.revolutionaryI18n ?
                window.revolutionaryI18n.translate('zine.results.tip_retry') :
                "🔄 Tu peux refaire le questionnaire pour comparer !",
            window.revolutionaryI18n ?
                window.revolutionaryI18n.translate('zine.results.tip_share') :
                "⭐ Partage tes résultats sur les réseaux sociaux !"
        ];

        const randomTip = tips[Math.floor(Math.random() * tips.length)];
        this.showMessage(randomTip, 5000);
    }

    showMessage(text, duration = 4000) {
        if (this.lastComment === text) return; // Éviter les répétitions

        clearTimeout(this.messageTimeout);

        this.message.textContent = text;
        this.lastComment = text;

        this.bubble.style.opacity = '1';
        this.bubble.style.transform = 'translateY(0) scale(1)';
        this.isMessageVisible = true;

        this.messageTimeout = setTimeout(() => {
            this.hideMessage();
        }, duration);
    }

    hideMessage() {
        if (this.bubble) {
            this.bubble.style.opacity = '0';
            this.bubble.style.transform = 'translateY(10px) scale(0.95)';
            this.isMessageVisible = false;
        }
    }
}

// Initialiser l'IA Coach quand la page est prête
document.addEventListener('DOMContentLoaded', function () {
    if (typeof ResultsAICoach !== 'undefined') {
        window.resultsAI = new ResultsAICoach();
        console.log('🤖 Results AI Coach initialized');
    }
});
