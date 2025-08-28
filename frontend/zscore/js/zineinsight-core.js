/**
 * ====================================
 * 🚀 ZINEINSIGHT REVOLUTIONARY JAVASCRIPT
 * The most advanced JavaScript ever created
 * Prepare for interactive revolution!
 * ====================================
 */

class ZineInsightRevolutionary {
    constructor() {
        this.isInitialized = false;
        this.animations = new Map();
        this.observers = new Map();
        this.particles = [];
        this.mouse = { x: 0, y: 0 };
        this.theme = 'dark';
        this.isScrolling = false;
        this.lastScrollTop = 0;

        // Performance monitoring
        this.performance = {
            startTime: performance.now(),
            interactions: 0,
            animationFrames: 0
        };

        // Initialize everything
        this.init();
    }

    /**
     * 🚀 REVOLUTIONARY INITIALIZATION
     */
    async init() {
        try {
            console.log('🔥 Initializing ZineInsight Revolutionary Platform...');

            // Wait for DOM to be ready
            if (document.readyState === 'loading') {
                await this.waitForDOMReady();
            }

            // Initialize core systems
            this.setupEventListeners();
            this.initializeAnimations();
            this.setupIntersectionObservers();
            this.initializeParticleSystem();
            this.setupScrollEffects();
            this.initializeCounters();
            this.setupThemeSystem();
            this.initializeNavigation();
            this.setupButtonEffects();
            this.initializeProductCards();
            this.setupMobileMenu();
            this.initializePerformanceMonitor();

            // Mark as initialized
            this.isInitialized = true;

            console.log('✨ ZineInsight Revolutionary Platform - FULLY LOADED!');
            this.triggerRevolutionaryEntrance();

        } catch (error) {
            console.error('💥 Revolutionary initialization failed:', error);
        }
    }

    /**
     * 🎯 WAIT FOR DOM READY
     */
    waitForDOMReady() {
        return new Promise(resolve => {
            if (document.readyState === 'loading') {
                document.addEventListener('DOMContentLoaded', resolve);
            } else {
                resolve();
            }
        });
    }

    /**
     * ⚡ SETUP EVENT LISTENERS
     */
    setupEventListeners() {
        // Mouse tracking for interactive effects
        document.addEventListener('mousemove', this.handleMouseMove.bind(this));
        document.addEventListener('click', this.handleClick.bind(this));

        // Window events
        window.addEventListener('scroll', this.handleScroll.bind(this), { passive: true });
        window.addEventListener('resize', this.handleResize.bind(this));
        window.addEventListener('beforeunload', this.handleBeforeUnload.bind(this));

        // Performance events
        window.addEventListener('load', this.handleWindowLoad.bind(this));

        // Keyboard navigation
        document.addEventListener('keydown', this.handleKeydown.bind(this));
    }

    /**
     * 🎬 INITIALIZE ANIMATIONS
     */
    initializeAnimations() {
        console.log('🎬 Initializing revolutionary animations...');

        // Create animation timeline
        this.animationTimeline = {
            hero: this.createHeroAnimations(),
            products: this.createProductAnimations(),
            ui: this.createUIAnimations()
        };
    }

    /**
     * 🎨 CREATE PRODUCT ANIMATIONS
     */
    createProductAnimations() {
        return {
            cards: { delay: 0, duration: 800, easing: 'cubic-bezier(0.25, 0.46, 0.45, 0.94)' },
            features: { delay: 200, duration: 600, easing: 'ease-out' },
            stats: { delay: 400, duration: 500, easing: 'ease-out' }
        };
    }

    /**
     * 🎭 CREATE UI ANIMATIONS
     */
    createUIAnimations() {
        return {
            navigation: { delay: 0, duration: 300, easing: 'ease-out' },
            buttons: { delay: 0, duration: 200, easing: 'cubic-bezier(0.68, -0.55, 0.265, 1.55)' },
            modals: { delay: 0, duration: 400, easing: 'ease-out' }
        };
    }

    /**
     * 👁️ SETUP INTERSECTION OBSERVERS
     */
    setupIntersectionObservers() {
        console.log('👁️ Setting up intersection observers...');

        // Main content observer
        const mainObserver = new IntersectionObserver(
            this.handleIntersection.bind(this),
            {
                rootMargin: '-10% 0px -10% 0px',
                threshold: [0, 0.25, 0.5, 0.75, 1]
            }
        );

        // Observe all animated elements
        document.querySelectorAll('[data-animate]').forEach(el => {
            mainObserver.observe(el);
        });

        this.observers.set('main', mainObserver);

        // Header scroll observer
        const headerObserver = new IntersectionObserver(
            this.handleHeaderIntersection.bind(this),
            { threshold: [0.9] }
        );

        const heroSection = document.getElementById('hero');
        if (heroSection) {
            headerObserver.observe(heroSection);
        }

        this.observers.set('header', headerObserver);
    }

    /**
     * ✨ PARTICLE SYSTEM INITIALIZATION
     */
    initializeParticleSystem() {
        console.log('✨ Initializing revolutionary particle system...');

        try {
            this.particleCanvas = this.createParticleCanvas();
            this.particleContext = this.particleCanvas.getContext('2d');

            // Create initial particles
            this.createParticles(50);

            // Start particle animation loop
            this.animateParticles();
        } catch (error) {
            console.warn('⚠️ Particle system initialization failed:', error);
            // Continue without particles
            this.particleCanvas = null;
            this.particleContext = null;
        }
    }    /**
     * 🌊 CREATE PARTICLE CANVAS
     */
    createParticleCanvas() {
        const canvas = document.createElement('canvas');
        canvas.style.position = 'fixed';
        canvas.style.top = '0';
        canvas.style.left = '0';
        canvas.style.width = '100%';
        canvas.style.height = '100%';
        canvas.style.pointerEvents = 'none';
        canvas.style.zIndex = '1';
        canvas.style.opacity = '0.6';

        // Insert before main content
        document.body.insertBefore(canvas, document.body.firstChild);

        // Set canvas size
        this.resizeCanvas(canvas);

        return canvas;
    }

    /**
     * 📏 RESIZE CANVAS
     */
    resizeCanvas(canvas) {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }

    /**
     * ✨ CREATE PARTICLES
     */
    createParticles(count) {
        this.particles = [];

        for (let i = 0; i < count; i++) {
            this.particles.push({
                x: Math.random() * window.innerWidth,
                y: Math.random() * window.innerHeight,
                size: Math.random() * 3 + 1,
                speedX: (Math.random() - 0.5) * 0.5,
                speedY: (Math.random() - 0.5) * 0.5,
                opacity: Math.random() * 0.5 + 0.2,
                color: this.getRandomParticleColor()
            });
        }
    }

    /**
     * 🎨 GET RANDOM PARTICLE COLOR
     */
    getRandomParticleColor() {
        const colors = [
            'rgba(102, 126, 234, 0.8)',
            'rgba(0, 212, 170, 0.8)',
            'rgba(255, 107, 107, 0.8)',
            'rgba(255, 255, 255, 0.6)'
        ];
        return colors[Math.floor(Math.random() * colors.length)];
    }

    /**
     * 🎬 ANIMATE PARTICLES
     */
    animateParticles() {
        if (!this.particleContext || !this.particleCanvas) return;

        const animate = () => {
            try {
                this.performance.animationFrames++;

                // Clear canvas
                this.particleContext.clearRect(0, 0, this.particleCanvas.width, this.particleCanvas.height);

                // Update and draw particles
                this.particles.forEach(particle => {
                    // Update position
                    particle.x += particle.speedX;
                    particle.y += particle.speedY;

                    // Wrap around edges
                    if (particle.x > window.innerWidth) particle.x = 0;
                    if (particle.x < 0) particle.x = window.innerWidth;
                    if (particle.y > window.innerHeight) particle.y = 0;
                    if (particle.y < 0) particle.y = window.innerHeight;

                    // Mouse interaction (safe)
                    if (this.mouse && typeof this.mouse.x === 'number') {
                        const dx = this.mouse.x - particle.x;
                        const dy = this.mouse.y - particle.y;
                        const distance = Math.sqrt(dx * dx + dy * dy);

                        if (distance < 100) {
                            const force = (100 - distance) / 100;
                            particle.x -= (dx / distance) * force * 2;
                            particle.y -= (dy / distance) * force * 2;
                        }
                    }

                    // Draw particle
                    this.particleContext.beginPath();
                    this.particleContext.arc(particle.x, particle.y, particle.size, 0, Math.PI * 2);
                    this.particleContext.fillStyle = particle.color;
                    this.particleContext.globalAlpha = particle.opacity;
                    this.particleContext.fill();
                });

                requestAnimationFrame(animate);
            } catch (error) {
                console.warn('⚠️ Particle animation error:', error);
                // Stop animation on persistent errors
            }
        };

        animate();
    }

    /**
     * 🌊 SETUP SCROLL EFFECTS
     */
    setupScrollEffects() {
        console.log('🌊 Setting up revolutionary scroll effects...');

        // Scroll progress bar
        this.scrollProgress = document.getElementById('scroll-progress');

        // Parallax elements
        this.parallaxElements = document.querySelectorAll('[data-parallax]');

        // Setup smooth scroll for navigation links
        document.querySelectorAll('[data-scroll-to]').forEach(link => {
            link.addEventListener('click', this.handleSmoothScroll.bind(this));
        });
    }

    /**
     * 🔢 INITIALIZE COUNTERS
     */
    initializeCounters() {
        console.log('🔢 Initializing animated counters...');

        this.counters = document.querySelectorAll('[data-counter]');
        this.counterAnimations = new Map();

        this.counters.forEach(counter => {
            const finalValue = parseInt(counter.getAttribute('data-counter'));
            this.counterAnimations.set(counter, {
                current: 0,
                target: finalValue,
                increment: finalValue / 100,
                hasAnimated: false
            });
        });
    }

    /**
     * 🎨 SETUP THEME SYSTEM
     */
    setupThemeSystem() {
        console.log('🎨 Setting up revolutionary theme system...');

        // Detect user preference
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        const savedTheme = localStorage.getItem('zineinsight-theme');

        this.theme = savedTheme || (prefersDark ? 'dark' : 'light');
        this.applyTheme(this.theme);

        // Listen for system theme changes
        window.matchMedia('(prefers-color-scheme: dark)')
            .addEventListener('change', this.handleThemeChange.bind(this));
    }

    /**
     * 🧭 INITIALIZE NAVIGATION
     */
    initializeNavigation() {
        console.log('🧭 Initializing revolutionary navigation...');

        this.navigation = {
            links: document.querySelectorAll('.nav-link'),
            indicators: document.querySelectorAll('.nav-indicator'),
            currentSection: 'hero'
        };

        // Setup navigation hover effects
        this.navigation.links.forEach(link => {
            link.addEventListener('mouseenter', this.handleNavHover.bind(this));
            link.addEventListener('mouseleave', this.handleNavLeave.bind(this));
        });
    }

    /**
     * ⚡ SETUP BUTTON EFFECTS
     */
    setupButtonEffects() {
        console.log('⚡ Setting up revolutionary button effects...');

        // All buttons with effects
        document.querySelectorAll('.btn').forEach(button => {
            this.setupButtonRipple(button);
            this.setupButtonMagnetism(button);
        });

        // Special CTA buttons
        document.querySelectorAll('.btn-primary, .btn-gradient').forEach(button => {
            this.setupButtonGlow(button);
        });
    }

    /**
     * 📱 SETUP PRODUCT CARDS
     */
    initializeProductCards() {
        console.log('📱 Initializing revolutionary product cards...');

        document.querySelectorAll('.product-card').forEach(card => {
            this.setupCard3D(card);
            this.setupCardInteractions(card);
        });
    }

    /**
     * 🍔 SETUP MOBILE MENU
     */
    setupMobileMenu() {
        console.log('🍔 Setting up revolutionary mobile menu...');

        const mobileToggle = document.getElementById('mobile-toggle');
        const navMenu = document.getElementById('nav-menu');

        if (mobileToggle && navMenu) {
            mobileToggle.addEventListener('click', () => {
                this.toggleMobileMenu(navMenu);
            });
        }
    }

    /**
     * 📊 INITIALIZE PERFORMANCE MONITOR
     */
    initializePerformanceMonitor() {
        console.log('📊 Initializing performance monitor...');

        // Monitor FPS
        this.fpsCounter = 0;
        this.lastFPSCheck = performance.now();

        setInterval(() => {
            this.checkPerformance();
        }, 5000);
    }

    /**
     * 🎭 EVENT HANDLERS
     */

    /**
     * 🖱️ HANDLE MOUSE MOVE
     */
    handleMouseMove(e) {
        this.mouse.x = e.clientX;
        this.mouse.y = e.clientY;

        // Update cursor effects (safe call)
        try {
            this.updateCursorEffects && this.updateCursorEffects(e);
        } catch (err) {
            // Silently handle missing method
        }

        // Update magnetism effects (safe call)
        try {
            this.updateMagnetismEffects && this.updateMagnetismEffects(e);
        } catch (err) {
            // Silently handle missing method
        }
    }

    /**
     * ✨ UPDATE CURSOR EFFECTS
     */
    updateCursorEffects(e) {
        // Create cursor trail effect
        if (Math.random() > 0.9) {
            const trail = document.createElement('div');
            trail.style.cssText = `
                position: fixed;
                left: ${e.clientX}px;
                top: ${e.clientY}px;
                width: 4px;
                height: 4px;
                background: rgba(102, 126, 234, 0.6);
                border-radius: 50%;
                pointer-events: none;
                z-index: 9999;
                transform: translate(-50%, -50%);
                transition: opacity 1s ease-out;
            `;
            document.body.appendChild(trail);

            setTimeout(() => {
                trail.style.opacity = '0';
                setTimeout(() => {
                    document.body.removeChild(trail);
                }, 1000);
            }, 100);
        }
    }

    /**
     * 🧲 UPDATE MAGNETISM EFFECTS
     */
    updateMagnetismEffects(e) {
        // Update magnetic buttons
        document.querySelectorAll('.btn-primary, .btn-gradient').forEach(btn => {
            const rect = btn.getBoundingClientRect();
            const distance = Math.sqrt(
                Math.pow(e.clientX - (rect.left + rect.width / 2), 2) +
                Math.pow(e.clientY - (rect.top + rect.height / 2), 2)
            );

            if (distance < 100) {
                const strength = (100 - distance) / 100;
                const x = (e.clientX - (rect.left + rect.width / 2)) * strength * 0.1;
                const y = (e.clientY - (rect.top + rect.height / 2)) * strength * 0.1;
                btn.style.transform = `translate(${x}px, ${y}px)`;
            }
        });
    }

    /**
     * 👆 HANDLE CLICK
     */
    handleClick(e) {
        this.performance.interactions++;

        // Create click ripple effect
        this.createClickRipple(e.clientX, e.clientY);

        // Haptic feedback for mobile
        if ('vibrate' in navigator) {
            navigator.vibrate(10);
        }
    }

    /**
     * 📜 HANDLE SCROLL
     */
    handleScroll() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        const scrollHeight = document.documentElement.scrollHeight - window.innerHeight;
        const scrollProgress = scrollTop / scrollHeight;

        // Update scroll progress
        if (this.scrollProgress) {
            this.scrollProgress.style.transform = `scaleX(${scrollProgress})`;
        }

        // Update parallax effects
        this.updateParallaxEffects(scrollTop);

        // Update navigation active states
        this.updateNavigationActive(scrollTop);

        // Throttle scroll events
        if (!this.isScrolling) {
            this.isScrolling = true;
            setTimeout(() => {
                this.isScrolling = false;
            }, 100);
        }

        this.lastScrollTop = scrollTop;
    }

    /**
     * 📱 HANDLE RESIZE
     */
    handleResize() {
        // Resize particle canvas (safe call)
        if (this.particleCanvas) {
            this.resizeCanvas(this.particleCanvas);
            // Recreate particles for new dimensions
            this.createParticles(50);
        }

        // Update 3D card effects (safe call)
        try {
            this.update3DCards && this.update3DCards();
        } catch (err) {
            // Silently handle missing method
        }
    }

    /**
     * 🎴 UPDATE 3D CARDS
     */
    update3DCards() {
        // Refresh 3D card effects after resize
        document.querySelectorAll('.product-card').forEach(card => {
            card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translateZ(0px)';
        });
    }

    /**
     * 👁️ HANDLE INTERSECTION
     */
    handleIntersection(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                this.animateElement(entry.target);

                // Start counter animations
                if (entry.target.hasAttribute('data-counter')) {
                    this.animateCounter(entry.target);
                }
            }
        });
    }

    /**
     * 📍 HANDLE HEADER INTERSECTION
     */
    handleHeaderIntersection(entries) {
        const header = document.getElementById('header-main');
        if (!header) return;

        entries.forEach(entry => {
            if (entry.isIntersecting) {
                header.classList.remove('scrolled');
            } else {
                header.classList.add('scrolled');
            }
        });
    }

    /**
     * ⌨️ HANDLE KEYDOWN
     */
    handleKeydown(e) {
        // Escape key handling
        if (e.key === 'Escape') {
            this.closeMobileMenu();
            this.closeModals();
        }

        // Navigation shortcuts
        if (e.ctrlKey || e.metaKey) {
            switch (e.key) {
                case '1':
                    e.preventDefault();
                    this.scrollToSection('hero');
                    break;
                case '2':
                    e.preventDefault();
                    this.scrollToSection('products');
                    break;
                case '3':
                    e.preventDefault();
                    this.scrollToSection('pricing');
                    break;
            }
        }
    }

    /**
     * ❌ CLOSE MODALS
     */
    closeModals() {
        // Close any open modals
        document.querySelectorAll('.modal.open, .modal.active').forEach(modal => {
            modal.classList.remove('open', 'active');
        });

        // Close dropdowns
        document.querySelectorAll('.dropdown.open, .user-dropdown.open').forEach(dropdown => {
            dropdown.classList.remove('open');
        });

        // Restore body scroll
        document.body.style.overflow = '';
    }

    /**
     * 🎬 ANIMATION METHODS
     */

    /**
     * 🚀 TRIGGER REVOLUTIONARY ENTRANCE
     */
    triggerRevolutionaryEntrance() {
        console.log('🚀 Triggering revolutionary entrance...');

        // Animate hero section
        setTimeout(() => {
            this.animateHeroEntrance();
        }, 500);

        // Animate navigation
        setTimeout(() => {
            this.animateNavigationEntrance();
        }, 800);

        // Show welcome message
        this.showWelcomeMessage();
    }

    /**
     * 🌟 ANIMATE ELEMENT
     */
    animateElement(element) {
        const animationType = element.getAttribute('data-animate');
        const delay = parseInt(element.getAttribute('data-delay')) || 0;

        setTimeout(() => {
            element.classList.add('animate-in');

            // Special animations
            switch (animationType) {
                case 'fade-up':
                    this.animateFadeUp(element);
                    break;
                case 'fade-left':
                    this.animateFadeLeft(element);
                    break;
                case 'bounce':
                    this.animateBounce(element);
                    break;
            }
        }, delay);
    }

    /**
     * ⬆️ ANIMATE FADE UP
     */
    animateFadeUp(element) {
        element.style.transform = 'translateY(0)';
        element.style.opacity = '1';
    }

    /**
     * ⬅️ ANIMATE FADE LEFT
     */
    animateFadeLeft(element) {
        element.style.transform = 'translateX(0)';
        element.style.opacity = '1';
    }

    /**
     * 🎾 ANIMATE BOUNCE
     */
    animateBounce(element) {
        element.style.animation = 'bounce 2s infinite';
    }

    /**
     * 🔢 ANIMATE COUNTER
     */
    animateCounter(counterElement) {
        const animation = this.counterAnimations.get(counterElement);
        if (!animation || animation.hasAnimated) return;

        animation.hasAnimated = true;

        const animateCount = () => {
            if (animation.current < animation.target) {
                animation.current += animation.increment;
                counterElement.textContent = Math.floor(animation.current);
                requestAnimationFrame(animateCount);
            } else {
                counterElement.textContent = animation.target;
            }
        };

        animateCount();
    }

    /**
     * 🎨 VISUAL EFFECTS METHODS
     */

    /**
     * 💫 CREATE CLICK RIPPLE
     */
    createClickRipple(x, y) {
        const ripple = document.createElement('div');
        ripple.style.position = 'fixed';
        ripple.style.left = x + 'px';
        ripple.style.top = y + 'px';
        ripple.style.width = '20px';
        ripple.style.height = '20px';
        ripple.style.background = 'radial-gradient(circle, rgba(102, 126, 234, 0.6) 0%, transparent 70%)';
        ripple.style.borderRadius = '50%';
        ripple.style.transform = 'translate(-50%, -50%) scale(0)';
        ripple.style.pointerEvents = 'none';
        ripple.style.zIndex = '9999';
        ripple.style.transition = 'transform 0.6s ease-out, opacity 0.6s ease-out';

        document.body.appendChild(ripple);

        setTimeout(() => {
            ripple.style.transform = 'translate(-50%, -50%) scale(20)';
            ripple.style.opacity = '0';
        }, 10);

        setTimeout(() => {
            document.body.removeChild(ripple);
        }, 600);
    }

    /**
     * 🌊 SETUP BUTTON RIPPLE
     */
    setupButtonRipple(button) {
        button.addEventListener('click', (e) => {
            const rect = button.getBoundingClientRect();
            const x = e.clientX - rect.left + rect.left;
            const y = e.clientY - rect.top + rect.top;

            this.createClickRipple(x, y);
        });
    }

    /**
     * 🧲 SETUP BUTTON MAGNETISM
     */
    setupButtonMagnetism(button) {
        const magnetic = {
            element: button,
            strength: 0.3
        };

        button.addEventListener('mouseenter', () => {
            button.style.transition = 'transform 0.3s ease-out';
        });

        button.addEventListener('mouseleave', () => {
            button.style.transform = 'translate(0, 0)';
            button.style.transition = 'transform 0.5s ease-out';
        });

        button.addEventListener('mousemove', (e) => {
            const rect = button.getBoundingClientRect();
            const x = e.clientX - rect.left - rect.width / 2;
            const y = e.clientY - rect.top - rect.height / 2;

            button.style.transform = `translate(${x * magnetic.strength}px, ${y * magnetic.strength}px)`;
        });
    }

    /**
     * 🎴 SETUP CARD 3D
     */
    setupCard3D(card) {
        card.addEventListener('mouseenter', () => {
            card.style.transformStyle = 'preserve-3d';
            card.style.transition = 'transform 0.3s ease-out';
        });

        card.addEventListener('mouseleave', () => {
            card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translateZ(0px)';
            card.style.transition = 'transform 0.5s ease-out';
        });

        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = (e.clientX - rect.left) / rect.width;
            const y = (e.clientY - rect.top) / rect.height;

            const rotateX = (y - 0.5) * 20;
            const rotateY = (x - 0.5) * -20;
            const translateZ = 10;

            card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateZ(${translateZ}px)`;
        });
    }

    /**
     * 🎮 SETUP CARD INTERACTIONS
     */
    setupCardInteractions(card) {
        // Enhanced click effects
        card.addEventListener('click', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left + rect.left;
            const y = e.clientY - rect.top + rect.top;

            this.createClickRipple(x, y);

            // Scale animation
            card.style.transform = 'scale(0.98)';
            setTimeout(() => {
                card.style.transform = '';
            }, 150);
        });

        // Glow effect on hover
        card.addEventListener('mouseenter', () => {
            card.style.boxShadow = '0 10px 40px rgba(102, 126, 234, 0.3)';
            card.style.transition = 'box-shadow 0.3s ease, transform 0.3s ease';
        });

        card.addEventListener('mouseleave', () => {
            card.style.boxShadow = '';
        });

        // Button interactions within card
        const buttons = card.querySelectorAll('.btn');
        buttons.forEach(btn => {
            btn.addEventListener('mouseenter', (e) => {
                e.stopPropagation();
                btn.style.transform = 'translateY(-2px)';
            });

            btn.addEventListener('mouseleave', (e) => {
                e.stopPropagation();
                btn.style.transform = '';
            });
        });
    }

    /**
     * 🧭 NAVIGATION HOVER HANDLERS
     */
    handleNavHover(e) {
        const link = e.currentTarget;
        const indicator = link.querySelector('.nav-indicator');

        if (indicator) {
            indicator.style.transform = 'scaleX(1)';
            indicator.style.opacity = '1';
        }

        link.style.color = '#a855f7';
        link.style.transform = 'translateY(-2px)';
    }

    handleNavLeave(e) {
        const link = e.currentTarget;
        const indicator = link.querySelector('.nav-indicator');

        if (indicator && !link.classList.contains('active')) {
            indicator.style.transform = 'scaleX(0)';
            indicator.style.opacity = '0';
        }

        if (!link.classList.contains('active')) {
            link.style.color = '';
            link.style.transform = '';
        }
    }

    /**
     * 🌈 SETUP BUTTON GLOW
     */
    setupButtonGlow(button) {
        button.addEventListener('mouseenter', () => {
            button.style.boxShadow = '0 0 40px rgba(102, 126, 234, 0.6), 0 20px 40px -10px rgba(0, 0, 0, 0.3)';
        });

        button.addEventListener('mouseleave', () => {
            button.style.boxShadow = '';
        });
    }

    /**
     * 🎵 SMOOTH SCROLL
     */
    handleSmoothScroll(e) {
        e.preventDefault();
        const targetId = e.currentTarget.getAttribute('data-scroll-to');
        this.scrollToSection(targetId);
    }

    /**
     * 📍 SCROLL TO SECTION
     */
    scrollToSection(sectionId) {
        const target = document.getElementById(sectionId);
        if (!target) return;

        const offsetTop = target.offsetTop - 80; // Account for fixed header

        window.scrollTo({
            top: offsetTop,
            behavior: 'smooth'
        });
    }

    /**
     * 📱 MOBILE MENU METHODS
     */

    /**
     * 🍔 TOGGLE MOBILE MENU
     */
    toggleMobileMenu(navMenu) {
        const isOpen = navMenu.classList.contains('mobile-open');

        if (isOpen) {
            this.closeMobileMenu();
        } else {
            this.openMobileMenu(navMenu);
        }
    }

    /**
     * 📱 OPEN MOBILE MENU
     */
    openMobileMenu(navMenu) {
        navMenu.classList.add('mobile-open');
        document.body.style.overflow = 'hidden';
    }

    /**
     * ❌ CLOSE MOBILE MENU
     */
    closeMobileMenu() {
        const navMenu = document.getElementById('nav-menu');
        if (navMenu) {
            navMenu.classList.remove('mobile-open');
        }
        document.body.style.overflow = '';
    }

    /**
     * 🎨 THEME METHODS
     */

    /**
     * 🌙 APPLY THEME
     */
    applyTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem('zineinsight-theme', theme);
        this.theme = theme;
    }

    /**
     * 🔄 HANDLE THEME CHANGE
     */
    handleThemeChange(e) {
        if (!localStorage.getItem('zineinsight-theme')) {
            this.applyTheme(e.matches ? 'dark' : 'light');
        }
    }

    /**
     * 📊 PERFORMANCE METHODS
     */

    /**
     * 🎯 CHECK PERFORMANCE
     */
    checkPerformance() {
        const now = performance.now();
        const fps = Math.round(this.performance.animationFrames / ((now - this.lastFPSCheck) / 1000));

        console.log(`🚀 Performance Stats:
            FPS: ${fps}
            Interactions: ${this.performance.interactions}
            Uptime: ${Math.round((now - this.performance.startTime) / 1000)}s
        `);

        // Reset counters
        this.performance.animationFrames = 0;
        this.lastFPSCheck = now;

        // Optimize if performance is low
        if (fps < 30) {
            this.optimizePerformance();
        }
    }

    /**
     * ⚡ OPTIMIZE PERFORMANCE
     */
    optimizePerformance() {
        console.log('⚡ Optimizing performance...');

        // Reduce particle count
        if (this.particles.length > 25) {
            this.particles = this.particles.slice(0, 25);
        }

        // Reduce animation complexity
        document.documentElement.style.setProperty('--transition-duration', '150ms');
    }

    /**
     * 🎉 UTILITY METHODS
     */

    /**
     * 📝 SHOW WELCOME MESSAGE
     */
    showWelcomeMessage() {
        console.log(`
        🚀 ================================
           WELCOME TO ZINEINSIGHT!
        ================================
        🎯 Ready to revolutionize your life?
        ✨ Experience the future of expatriation
        🧠 Powered by revolutionary AI

        Made with ❤️ by ZineInsight Team
        ================================
        `);
    }

    /**
     * 💫 CREATE HERO ANIMATIONS
     */
    createHeroAnimations() {
        return {
            title: { delay: 0, duration: 1000, easing: 'cubic-bezier(0.25, 0.46, 0.45, 0.94)' },
            subtitle: { delay: 200, duration: 800, easing: 'ease-out' },
            stats: { delay: 400, duration: 600, easing: 'ease-out' },
            cta: { delay: 600, duration: 500, easing: 'cubic-bezier(0.68, -0.55, 0.265, 1.55)' }
        };
    }

    /**
     * 🎨 ANIMATE HERO ENTRANCE
     */
    animateHeroEntrance() {
        const heroElements = {
            badge: document.querySelector('.hero-badge'),
            title: document.querySelector('.hero-title'),
            subtitle: document.querySelector('.hero-subtitle'),
            stats: document.querySelector('.hero-stats'),
            actions: document.querySelector('.hero-actions'),
            visual: document.querySelector('.hero-visual')
        };

        // Animate each element with staggered timing
        Object.entries(heroElements).forEach(([key, element], index) => {
            if (element) {
                setTimeout(() => {
                    element.style.opacity = '1';
                    element.style.transform = 'translateY(0)';
                }, index * 150);
            }
        });
    }

    /**
     * 🧭 ANIMATE NAVIGATION ENTRANCE
     */
    animateNavigationEntrance() {
        const navLinks = document.querySelectorAll('.nav-link');
        navLinks.forEach((link, index) => {
            setTimeout(() => {
                link.style.opacity = '1';
                link.style.transform = 'translateY(0)';
            }, index * 100);
        });
    }

    /**
     * 🔄 UPDATE PARALLAX EFFECTS
     */
    updateParallaxEffects(scrollTop) {
        this.parallaxElements.forEach(element => {
            const speed = parseFloat(element.getAttribute('data-parallax')) || 0.5;
            const yPos = -(scrollTop * speed);
            element.style.transform = `translateY(${yPos}px)`;
        });
    }

    /**
     * 🧭 UPDATE NAVIGATION ACTIVE
     */
    updateNavigationActive(scrollTop) {
        const sections = ['hero', 'products', 'pricing', 'testimonials'];
        let currentSection = 'hero';

        sections.forEach(sectionId => {
            const section = document.getElementById(sectionId);
            if (section) {
                const sectionTop = section.offsetTop - 100;
                const sectionBottom = sectionTop + section.offsetHeight;

                if (scrollTop >= sectionTop && scrollTop < sectionBottom) {
                    currentSection = sectionId;
                }
            }
        });

        // Update active navigation
        document.querySelectorAll('.nav-link').forEach(link => {
            const target = link.getAttribute('data-scroll-to');
            if (target === currentSection) {
                link.classList.add('active');
            } else {
                link.classList.remove('active');
            }
        });
    }

    /**
     * 💫 CLEANUP ON UNLOAD
     */
    handleBeforeUnload() {
        // Cleanup observers
        this.observers.forEach(observer => observer.disconnect());

        // Stop particle animation
        if (this.particleCanvas && this.particleCanvas.parentNode) {
            this.particleCanvas.parentNode.removeChild(this.particleCanvas);
        }

        console.log('🔄 ZineInsight Revolutionary - Cleaned up successfully');
    }

    /**
     * 🏁 HANDLE WINDOW LOAD
     */
    handleWindowLoad() {
        const loadTime = performance.now() - this.performance.startTime;
        console.log(`⚡ Page loaded in ${Math.round(loadTime)}ms`);
    }
}

/**
 * 🚀 REVOLUTIONARY API EXTENSIONS
 */

// Extend the revolutionary experience
ZineInsightRevolutionary.prototype.createMagicCursor = function () {
    const cursor = document.createElement('div');
    cursor.className = 'magic-cursor';
    cursor.style.cssText = `
        position: fixed;
        width: 20px;
        height: 20px;
        background: radial-gradient(circle, rgba(102, 126, 234, 0.8) 0%, transparent 70%);
        border-radius: 50%;
        pointer-events: none;
        z-index: 9999;
        transition: transform 0.1s ease-out;
        opacity: 0;
    `;

    document.body.appendChild(cursor);

    document.addEventListener('mousemove', (e) => {
        cursor.style.left = e.clientX - 10 + 'px';
        cursor.style.top = e.clientY - 10 + 'px';
        cursor.style.opacity = '1';
    });

    document.addEventListener('mouseleave', () => {
        cursor.style.opacity = '0';
    });

    return cursor;
};

/**
 * 🎯 REVOLUTIONARY SHORTCUTS API
 */
window.ZineInsight = {
    // Quick access methods
    scrollTo: (section) => window.zineApp?.scrollToSection(section),
    toggleTheme: () => window.zineApp?.applyTheme(window.zineApp.theme === 'dark' ? 'light' : 'dark'),
    getStats: () => window.zineApp?.performance,

    // Easter eggs
    konami: () => {
        console.log('🎮 KONAMI CODE ACTIVATED! 🚀');
        document.body.style.animation = 'rainbow 2s infinite';
    },

    // Revolutionary mode
    revolutionaryMode: () => {
        document.documentElement.style.filter = 'hue-rotate(180deg) saturate(1.5)';
        setTimeout(() => {
            document.documentElement.style.filter = '';
        }, 3000);
    }
};

/**
 * 🚀 AUTO-INITIALIZE ON DOM READY - ROBUST VERSION
 */
if (typeof window !== 'undefined') {
    // Enhanced error handling
    let initAttempts = 0;
    const maxAttempts = 3;

    const safeInit = () => {
        try {
            if (initAttempts >= maxAttempts) {
                console.warn('🚨 Max initialization attempts reached');
                return;
            }

            initAttempts++;
            console.log(`🚀 Initialization attempt ${initAttempts}/${maxAttempts}`);

            // Create revolutionary instance
            window.zineApp = new ZineInsightRevolutionary();
            console.log('✅ ZineInsight Revolutionary successfully initialized!');

        } catch (error) {
            console.error(`💥 Initialization failed (attempt ${initAttempts}):`, error);

            if (initAttempts < maxAttempts) {
                console.log('🔄 Retrying initialization in 1 second...');
                setTimeout(safeInit, 1000);
            } else {
                console.error('🚨 All initialization attempts failed. Running in fallback mode.');
                // Fallback minimal initialization
                window.zineApp = {
                    scrollToSection: (id) => {
                        const element = document.getElementById(id);
                        if (element) {
                            element.scrollIntoView({ behavior: 'smooth' });
                        }
                    },
                    theme: 'dark',
                    performance: { interactions: 0, animationFrames: 0 }
                };
            }
        }
    };

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', safeInit);
    } else {
        safeInit();
    }

    // Enhanced global error handler
    window.addEventListener('error', (e) => {
        // Only log critical errors, suppress 404s for optional resources
        if (!e.filename?.includes('favicon') && !e.filename?.includes('manifest')) {
            console.error('🚨 Revolutionary Error:', e.error || e.message);
        }
    });

    // Unhandled promise rejection handler
    window.addEventListener('unhandledrejection', (e) => {
        console.error('🚨 Revolutionary Promise Rejection:', e.reason);
        e.preventDefault(); // Prevent uncaught promise rejection
    });
}/**
 * ====================================
 * 🎉 ZINEINSIGHT REVOLUTIONARY LOADED
 * The future of web experiences!
 * ====================================
 */

console.log(`
🔥 ========================================
   ZINEINSIGHT REVOLUTIONARY JAVASCRIPT
   The most advanced web experience!
========================================
🚀 Features loaded:
   ✨ Particle System
   🎬 Advanced Animations
   👁️ Intersection Observers
   🧲 Magnetic Interactions
   📱 Mobile Optimizations
   🌙 Theme System
   📊 Performance Monitor
   🎯 Smooth Scrolling
   💫 3D Effects
   🌊 Parallax Effects
========================================
`);

// Export for ES6 modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = ZineInsightRevolutionary;
}
