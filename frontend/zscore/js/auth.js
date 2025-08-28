/**
 * 🔐 REVOLUTIONARY AUTH MANAGER
 * ===============================
 * Frontend authentication system with JWT + Redis integration
 * Author: Revolutionary Team
 * Version: 1.0.0
 */

// ===== AUTH CONFIG =====
const AUTH_CONFIG = {
    API_BASE_URL: window.location.protocol + '//' + window.location.hostname,
    ENDPOINTS: {
        LOGIN: '/api/auth/login',
        REGISTER: '/api/auth/register',
        LOGOUT: '/api/auth/logout',
        VERIFY_EMAIL: '/api/auth/verify-email',
        RESEND_VERIFICATION: '/api/auth/resend-verification',
        FORGOT_PASSWORD: '/api/auth/forgot-password',
        RESET_PASSWORD: '/api/auth/reset-password',
        PROFILE: '/api/auth/profile'
    },
    STORAGE_KEYS: {
        TOKEN: 'revolutionary_token',
        USER: 'revolutionary_user',
        REMEMBER_ME: 'revolutionary_remember'
    },
    VALIDATION: {
        EMAIL_REGEX: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
        PASSWORD_MIN_LENGTH: 8,
        NAME_MIN_LENGTH: 2
    }
};

// ===== AUTH MANAGER CLASS =====
class RevolutionaryAuth {
    constructor() {
        this.currentForm = 'login';
        this.isLoading = false;
        this.notifications = new NotificationManager();
        this.init();
    }

    // 🚀 Initialize authentication system
    init() {
        this.setupEventListeners();
        this.checkAuthStatus();
        this.handleURLParams();
        console.log('🔐 Revolutionary Auth initialized');
    }

    // 📱 Setup event listeners
    setupEventListeners() {
        // Form switching
        document.getElementById('switchToRegister')?.addEventListener('click', () => this.switchForm('register'));
        document.getElementById('switchToLogin')?.addEventListener('click', () => this.switchForm('login'));
        document.getElementById('backToLogin')?.addEventListener('click', () => this.switchForm('login'));
        document.getElementById('backToLoginFromForgot')?.addEventListener('click', () => this.switchForm('login'));

        document.getElementById('forgotPasswordLink')?.addEventListener('click', (e) => {
            e.preventDefault();
            this.switchForm('forgot');
        });

        // Form submissions
        document.getElementById('loginForm')?.addEventListener('submit', (e) => this.handleLogin(e));
        document.getElementById('registerForm')?.addEventListener('submit', (e) => this.handleRegister(e));
        document.getElementById('forgotPasswordForm')?.addEventListener('submit', (e) => this.handleForgotPassword(e));

        // Password toggles
        document.getElementById('loginPasswordToggle')?.addEventListener('click', () => this.togglePassword('loginPassword'));
        document.getElementById('registerPasswordToggle')?.addEventListener('click', () => this.togglePassword('registerPassword'));

        // Password strength
        document.getElementById('registerPassword')?.addEventListener('input', (e) => this.checkPasswordStrength(e.target.value));

        // Real-time validation
        this.setupRealTimeValidation();

        // Resend verification
        document.getElementById('resendVerification')?.addEventListener('click', () => this.resendVerification());
    }

    // ⚡ Setup real-time validation
    setupRealTimeValidation() {
        // Email validation
        ['loginEmail', 'registerEmail', 'forgotEmail'].forEach(id => {
            const element = document.getElementById(id);
            if (element) {
                element.addEventListener('blur', (e) => this.validateEmail(e.target));
                element.addEventListener('input', (e) => this.clearError(e.target));
            }
        });

        // Password validation
        ['loginPassword', 'registerPassword'].forEach(id => {
            const element = document.getElementById(id);
            if (element) {
                element.addEventListener('blur', (e) => this.validatePassword(e.target));
                element.addEventListener('input', (e) => this.clearError(e.target));
            }
        });

        // Name validation
        ['firstName', 'lastName'].forEach(id => {
            const element = document.getElementById(id);
            if (element) {
                element.addEventListener('blur', (e) => this.validateName(e.target));
                element.addEventListener('input', (e) => this.clearError(e.target));
            }
        });

        // Confirm password validation
        const confirmPassword = document.getElementById('confirmPassword');
        if (confirmPassword) {
            confirmPassword.addEventListener('blur', () => this.validateConfirmPassword());
            confirmPassword.addEventListener('input', () => this.clearError(confirmPassword));
        }
    }

    // 🔄 Switch between forms
    switchForm(formName) {
        // Hide all forms
        document.querySelectorAll('.auth-form').forEach(form => {
            form.classList.remove('active');
        });

        // Show target form
        const targetForm = document.querySelector(`[data-form="${formName}"]`);
        if (targetForm) {
            targetForm.classList.add('active');
            this.currentForm = formName;

            // Focus first input
            const firstInput = targetForm.querySelector('.form-input');
            if (firstInput) {
                setTimeout(() => firstInput.focus(), 300);
            }
        }

        // Track form switch
        this.trackEvent('form_switch', { form: formName });
    }

    // 🔐 Handle login
    async handleLogin(event) {
        event.preventDefault();

        if (this.isLoading) return;

        const formData = new FormData(event.target);
        const email = formData.get('email')?.trim();
        const password = formData.get('password');
        const rememberMe = formData.get('remember') === 'on';

        // Validate inputs
        if (!this.validateLoginForm(email, password)) return;

        // Set loading state
        this.setLoadingState('loginButton', true);

        try {
            const response = await this.apiCall('POST', AUTH_CONFIG.ENDPOINTS.LOGIN, {
                email,
                password,
                remember_me: rememberMe
            });

            if (response.success) {
                // Store authentication data
                this.storeAuthData(response, rememberMe);

                // Show success notification
                this.notifications.show('success', 'Connexion réussie', 'Bienvenue dans Revolutionary !');

                // Track successful login
                this.trackEvent('login_success', { email, remember_me: rememberMe });

                // Redirect to dashboard
                setTimeout(() => {
                    window.location.href = '/dashboard.html';
                }, 1500);
            } else {
                this.handleAuthError(response);
            }
        } catch (error) {
            console.error('Login error:', error);
            this.notifications.show('error', 'Erreur de connexion', 'Une erreur inattendue s\'est produite');
            this.trackEvent('login_error', { error: error.message });
        } finally {
            this.setLoadingState('loginButton', false);
        }
    }

    // 📝 Handle registration
    async handleRegister(event) {
        event.preventDefault();

        if (this.isLoading) return;

        const formData = new FormData(event.target);
        const firstName = formData.get('firstName')?.trim();
        const lastName = formData.get('lastName')?.trim();
        const email = formData.get('email')?.trim();
        const password = formData.get('password');
        const confirmPassword = formData.get('confirmPassword');
        const acceptTerms = formData.get('acceptTerms') === 'on';
        const acceptMarketing = formData.get('acceptMarketing') === 'on';

        // Validate registration form
        if (!this.validateRegisterForm(firstName, lastName, email, password, confirmPassword, acceptTerms)) return;

        // Set loading state
        this.setLoadingState('registerButton', true);

        try {
            const response = await this.apiCall('POST', AUTH_CONFIG.ENDPOINTS.REGISTER, {
                first_name: firstName,
                last_name: lastName,
                email,
                password,
                accept_marketing: acceptMarketing
            });

            if (response.success) {
                // Show email verification screen
                document.getElementById('verificationEmail').textContent = email;
                this.switchForm('verification');

                // Show success notification
                this.notifications.show('success', 'Compte créé', 'Vérifiez votre e-mail pour activer votre compte');

                // Track successful registration
                this.trackEvent('register_success', { email, accept_marketing: acceptMarketing });
            } else {
                this.handleAuthError(response);
            }
        } catch (error) {
            console.error('Register error:', error);
            this.notifications.show('error', 'Erreur d\'inscription', 'Une erreur inattendue s\'est produite');
            this.trackEvent('register_error', { error: error.message });
        } finally {
            this.setLoadingState('registerButton', false);
        }
    }

    // 🔑 Handle forgot password
    async handleForgotPassword(event) {
        event.preventDefault();

        if (this.isLoading) return;

        const formData = new FormData(event.target);
        const email = formData.get('email')?.trim();

        // Validate email
        if (!this.validateEmailInput(document.getElementById('forgotEmail'))) return;

        // Set loading state
        this.setLoadingState('forgotPasswordButton', true);

        try {
            const response = await this.apiCall('POST', AUTH_CONFIG.ENDPOINTS.FORGOT_PASSWORD, {
                email
            });

            if (response.success) {
                // Show success notification
                this.notifications.show('success', 'E-mail envoyé', 'Vérifiez votre boîte e-mail pour réinitialiser votre mot de passe');

                // Switch back to login
                setTimeout(() => this.switchForm('login'), 2000);

                // Track forgot password request
                this.trackEvent('forgot_password_request', { email });
            } else {
                this.handleAuthError(response);
            }
        } catch (error) {
            console.error('Forgot password error:', error);
            this.notifications.show('error', 'Erreur', 'Une erreur inattendue s\'est produite');
            this.trackEvent('forgot_password_error', { error: error.message });
        } finally {
            this.setLoadingState('forgotPasswordButton', false);
        }
    }

    // 📧 Resend verification email
    async resendVerification() {
        const email = document.getElementById('verificationEmail')?.textContent;
        if (!email) return;

        try {
            const response = await this.apiCall('POST', AUTH_CONFIG.ENDPOINTS.RESEND_VERIFICATION, {
                email
            });

            if (response.success) {
                this.notifications.show('success', 'E-mail renvoyé', 'Un nouveau lien de vérification a été envoyé');
                this.trackEvent('verification_resend', { email });
            } else {
                this.handleAuthError(response);
            }
        } catch (error) {
            console.error('Resend verification error:', error);
            this.notifications.show('error', 'Erreur', 'Impossible de renvoyer l\'e-mail');
        }
    }

    // ✅ Validate login form
    validateLoginForm(email, password) {
        let isValid = true;

        // Email validation
        if (!email || !AUTH_CONFIG.VALIDATION.EMAIL_REGEX.test(email)) {
            this.showError('loginEmailError', 'Adresse e-mail invalide');
            isValid = false;
        }

        // Password validation
        if (!password || password.length < AUTH_CONFIG.VALIDATION.PASSWORD_MIN_LENGTH) {
            this.showError('loginPasswordError', `Le mot de passe doit contenir au moins ${AUTH_CONFIG.VALIDATION.PASSWORD_MIN_LENGTH} caractères`);
            isValid = false;
        }

        return isValid;
    }

    // ✅ Validate registration form
    validateRegisterForm(firstName, lastName, email, password, confirmPassword, acceptTerms) {
        let isValid = true;

        // Name validation
        if (!firstName || firstName.length < AUTH_CONFIG.VALIDATION.NAME_MIN_LENGTH) {
            this.showError('firstNameError', 'Le prénom est requis');
            isValid = false;
        }

        if (!lastName || lastName.length < AUTH_CONFIG.VALIDATION.NAME_MIN_LENGTH) {
            this.showError('lastNameError', 'Le nom est requis');
            isValid = false;
        }

        // Email validation
        if (!email || !AUTH_CONFIG.VALIDATION.EMAIL_REGEX.test(email)) {
            this.showError('registerEmailError', 'Adresse e-mail invalide');
            isValid = false;
        }

        // Password validation
        if (!password || password.length < AUTH_CONFIG.VALIDATION.PASSWORD_MIN_LENGTH) {
            this.showError('registerPasswordError', `Le mot de passe doit contenir au moins ${AUTH_CONFIG.VALIDATION.PASSWORD_MIN_LENGTH} caractères`);
            isValid = false;
        }

        // Confirm password validation
        if (password !== confirmPassword) {
            this.showError('confirmPasswordError', 'Les mots de passe ne correspondent pas');
            isValid = false;
        }

        // Terms acceptance validation
        if (!acceptTerms) {
            this.notifications.show('warning', 'Conditions requises', 'Vous devez accepter les conditions d\'utilisation');
            isValid = false;
        }

        return isValid;
    }

    // ✅ Validate individual fields
    validateEmail(input) {
        if (!input) return false;

        const email = input.value.trim();
        const errorElement = document.getElementById(input.id + 'Error');

        if (!email) {
            this.showError(errorElement.id, 'L\'adresse e-mail est requise');
            return false;
        }

        if (!AUTH_CONFIG.VALIDATION.EMAIL_REGEX.test(email)) {
            this.showError(errorElement.id, 'Adresse e-mail invalide');
            return false;
        }

        this.clearError(input);
        return true;
    }

    validateEmailInput(input) {
        return this.validateEmail(input);
    }

    validatePassword(input) {
        if (!input) return false;

        const password = input.value;
        const errorElement = document.getElementById(input.id + 'Error');

        if (!password) {
            this.showError(errorElement.id, 'Le mot de passe est requis');
            return false;
        }

        if (password.length < AUTH_CONFIG.VALIDATION.PASSWORD_MIN_LENGTH) {
            this.showError(errorElement.id, `Minimum ${AUTH_CONFIG.VALIDATION.PASSWORD_MIN_LENGTH} caractères`);
            return false;
        }

        this.clearError(input);
        return true;
    }

    validateName(input) {
        if (!input) return false;

        const name = input.value.trim();
        const errorElement = document.getElementById(input.id + 'Error');

        if (!name) {
            this.showError(errorElement.id, 'Ce champ est requis');
            return false;
        }

        if (name.length < AUTH_CONFIG.VALIDATION.NAME_MIN_LENGTH) {
            this.showError(errorElement.id, `Minimum ${AUTH_CONFIG.VALIDATION.NAME_MIN_LENGTH} caractères`);
            return false;
        }

        this.clearError(input);
        return true;
    }

    validateConfirmPassword() {
        const password = document.getElementById('registerPassword')?.value;
        const confirmPassword = document.getElementById('confirmPassword');

        if (!confirmPassword || !password) return false;

        if (confirmPassword.value !== password) {
            this.showError('confirmPasswordError', 'Les mots de passe ne correspondent pas');
            return false;
        }

        this.clearError(confirmPassword);
        return true;
    }

    // 🔐 Check password strength
    checkPasswordStrength(password) {
        const strengthElement = document.getElementById('passwordStrength');
        if (!strengthElement || !password) {
            if (strengthElement) strengthElement.classList.remove('visible');
            return;
        }

        strengthElement.classList.add('visible');

        let score = 0;
        let feedback = '';

        // Length check
        if (password.length >= 8) score += 1;
        if (password.length >= 12) score += 1;

        // Character variety checks
        if (/[a-z]/.test(password)) score += 1;
        if (/[A-Z]/.test(password)) score += 1;
        if (/[0-9]/.test(password)) score += 1;
        if (/[^a-zA-Z0-9]/.test(password)) score += 1;

        // Set strength level
        strengthElement.className = 'password-strength visible';

        if (score <= 2) {
            strengthElement.classList.add('weak');
            feedback = 'Mot de passe faible';
        } else if (score <= 4) {
            strengthElement.classList.add('fair');
            feedback = 'Mot de passe moyen';
        } else if (score <= 5) {
            strengthElement.classList.add('good');
            feedback = 'Bon mot de passe';
        } else {
            strengthElement.classList.add('strong');
            feedback = 'Mot de passe fort';
        }

        strengthElement.querySelector('.strength-text').textContent = feedback;
    }

    // 👁️ Toggle password visibility
    togglePassword(inputId) {
        const input = document.getElementById(inputId);
        const toggle = document.getElementById(inputId + 'Toggle');

        if (!input || !toggle) return;

        const eyeOpen = toggle.querySelector('.eye-open');
        const eyeClosed = toggle.querySelector('.eye-closed');

        if (input.type === 'password') {
            input.type = 'text';
            eyeOpen.style.display = 'none';
            eyeClosed.style.display = 'block';
        } else {
            input.type = 'password';
            eyeOpen.style.display = 'block';
            eyeClosed.style.display = 'none';
        }
    }

    // 🚨 Show error message
    showError(elementId, message) {
        const errorElement = document.getElementById(elementId);
        if (errorElement) {
            errorElement.textContent = message;
            errorElement.classList.add('visible');
        }
    }

    // ✨ Clear error message
    clearError(input) {
        const errorElement = document.getElementById(input.id + 'Error');
        if (errorElement) {
            errorElement.textContent = '';
            errorElement.classList.remove('visible');
        }
    }

    // ⏳ Set loading state
    setLoadingState(buttonId, isLoading) {
        const button = document.getElementById(buttonId);
        if (!button) return;

        this.isLoading = isLoading;

        if (isLoading) {
            button.classList.add('loading');
            button.disabled = true;
        } else {
            button.classList.remove('loading');
            button.disabled = false;
        }
    }

    // 🌐 API call wrapper
    async apiCall(method, endpoint, data = null) {
        const url = AUTH_CONFIG.API_BASE_URL + endpoint;

        const config = {
            method,
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        };

        if (data) {
            config.body = JSON.stringify(data);
        }

        // Add auth token if available
        const token = this.getStoredToken();
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }

        const response = await fetch(url, config);

        // Handle different response types
        const contentType = response.headers.get('content-type');
        if (contentType && contentType.includes('application/json')) {
            return await response.json();
        } else {
            const text = await response.text();
            return { success: response.ok, message: text };
        }
    }

    // 💾 Store authentication data
    storeAuthData(authData, rememberMe) {
        const storage = rememberMe ? localStorage : sessionStorage;

        if (authData.token) {
            storage.setItem(AUTH_CONFIG.STORAGE_KEYS.TOKEN, authData.token);
        }

        if (authData.user) {
            storage.setItem(AUTH_CONFIG.STORAGE_KEYS.USER, JSON.stringify(authData.user));
        }

        if (rememberMe) {
            localStorage.setItem(AUTH_CONFIG.STORAGE_KEYS.REMEMBER_ME, 'true');
        }
    }

    // 🔍 Get stored token
    getStoredToken() {
        return localStorage.getItem(AUTH_CONFIG.STORAGE_KEYS.TOKEN) ||
            sessionStorage.getItem(AUTH_CONFIG.STORAGE_KEYS.TOKEN);
    }

    // 🔍 Get stored user
    getStoredUser() {
        const userStr = localStorage.getItem(AUTH_CONFIG.STORAGE_KEYS.USER) ||
            sessionStorage.getItem(AUTH_CONFIG.STORAGE_KEYS.USER);
        return userStr ? JSON.parse(userStr) : null;
    }

    // ✅ Check authentication status
    checkAuthStatus() {
        const token = this.getStoredToken();
        const user = this.getStoredUser();

        if (token && user) {
            // User is authenticated, redirect if on auth page
            if (window.location.pathname.includes('auth.html') || window.location.pathname.includes('auth')) {
                window.location.href = '/dashboard.html';
            }
        }
    }

    // 🔗 Handle URL parameters (email verification, password reset)
    handleURLParams() {
        const urlParams = new URLSearchParams(window.location.search);

        // Handle email verification
        if (urlParams.get('verify') === 'email') {
            const token = urlParams.get('token');
            if (token) {
                this.verifyEmail(token);
            }
        }

        // Handle password reset
        if (urlParams.get('reset') === 'password') {
            const token = urlParams.get('token');
            if (token) {
                this.showPasswordResetForm(token);
            }
        }
    }

    // ✉️ Verify email with token
    async verifyEmail(token) {
        try {
            const response = await this.apiCall('POST', AUTH_CONFIG.ENDPOINTS.VERIFY_EMAIL, {
                token
            });

            if (response.success) {
                this.notifications.show('success', 'E-mail vérifié', 'Votre compte a été activé avec succès');
                this.switchForm('login');
                this.trackEvent('email_verified', { token });
            } else {
                this.notifications.show('error', 'Vérification échouée', response.message || 'Lien de vérification invalide');
            }
        } catch (error) {
            console.error('Email verification error:', error);
            this.notifications.show('error', 'Erreur de vérification', 'Une erreur inattendue s\'est produite');
        }
    }

    // 🚨 Handle authentication errors
    handleAuthError(response) {
        const message = response.message || 'Une erreur s\'est produite';

        // Handle specific error types
        if (response.error && response.error.includes('Email ou mot de passe incorrect')) {
            this.notifications.show('error', 'Identifiants incorrects', 'E-mail ou mot de passe invalide');
            return;
        }

        if (response.error && response.error.includes('Email déjà utilisé')) {
            this.notifications.show('error', 'E-mail déjà utilisé', 'Un compte existe déjà avec cette adresse e-mail');
            return;
        }

        // Generic error
        this.notifications.show('error', 'Erreur', response.error || message);
    }

    // 📊 Track events for analytics
    trackEvent(event, data = {}) {
        if (typeof window.revolutionaryAuth?.trackEvent === 'function') {
            window.revolutionaryAuth.trackEvent(event, data);
        }
        console.log(`[Auth Event] ${event}:`, data);
    }
}

// ===== NOTIFICATION MANAGER =====
class NotificationManager {
    constructor() {
        this.container = document.getElementById('notifications');
        this.notifications = [];

        // Create notifications container if it doesn't exist
        if (!this.container) {
            this.container = document.createElement('div');
            this.container.id = 'notifications';
            this.container.className = 'notifications-container';
            document.body.appendChild(this.container);
        }
    }

    show(type, title, message, duration = 5000) {
        const notification = this.createNotification(type, title, message);
        this.container.appendChild(notification);
        this.notifications.push(notification);

        // Animate in
        setTimeout(() => notification.classList.add('show'), 100);

        // Auto remove
        setTimeout(() => this.remove(notification), duration);
    }

    createNotification(type, title, message) {
        const notification = document.createElement('div');
        notification.className = `notification ${type}`;

        notification.innerHTML = `
            <div class="notification-content">
                <div class="notification-icon">
                    ${this.getIcon(type)}
                </div>
                <div class="notification-text">
                    <div class="notification-title">${title}</div>
                    <div class="notification-message">${message}</div>
                </div>
                <button class="notification-close" onclick="this.closest('.notification').remove()">
                    <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <line x1="18" y1="6" x2="6" y2="18" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        <line x1="6" y1="6" x2="18" y2="18" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                </button>
            </div>
        `;

        return notification;
    }

    getIcon(type) {
        const icons = {
            success: `<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M9 12L11 14L15 10M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>`,
            error: `<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2"/>
                <line x1="15" y1="9" x2="9" y2="15" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                <line x1="9" y1="9" x2="15" y2="15" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>`,
            warning: `<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                <line x1="12" y1="9" x2="12" y2="13" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                <line x1="12" y1="17" x2="12.01" y2="17" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>`,
            info: `<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2"/>
                <path d="M12 16V12" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M12 8H12.01" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>`
        };
        return icons[type] || icons.info;
    }

    remove(notification) {
        notification.classList.remove('show');
        setTimeout(() => {
            if (notification.parentNode) {
                notification.parentNode.removeChild(notification);
            }
            const index = this.notifications.indexOf(notification);
            if (index > -1) {
                this.notifications.splice(index, 1);
            }
        }, 300);
    }
}

// ===== 🌐 SOCIAL AUTH MANAGER =====
class SocialAuthManager {
    constructor(authManager) {
        this.authManager = authManager;
        this.initSocialAuth();
    }

    initSocialAuth() {
        // Google Sign-In only
        this.loadGoogleSDK().then(() => {
            this.setupGoogleAuth();
        }).catch(err => {
            console.warn('Google SDK load failed:', err);
        });

        // Bind click events
        this.bindSocialEvents();
    }

    async loadGoogleSDK() {
        if (window.google) return;

        return new Promise((resolve, reject) => {
            const script = document.createElement('script');
            script.src = 'https://accounts.google.com/gsi/client';
            script.onload = resolve;
            script.onerror = reject;
            document.head.appendChild(script);
        });
    }

    setupGoogleAuth() {
        try {
            // Detect environment and use appropriate client ID
            const isProduction = window.location.hostname === 'zineinsight.com';
            const clientId = isProduction
                ? '674861755298-21pne5th32e8mqr3rqj8ame0rbp5qbu4.apps.googleusercontent.com'
                : '1086132225392-example.apps.googleusercontent.com';

            console.log('Setting up Google Auth with client ID:', clientId);

            window.google.accounts.id.initialize({
                client_id: clientId,
                callback: this.handleGoogleResponse.bind(this),
                auto_select: false,
                cancel_on_tap_outside: true
            });

            // Replace custom buttons with native Google buttons after a short delay
            setTimeout(() => {
                this.replaceWithNativeGoogleButtons();
            }, 500);

            console.log('Google Auth initialized successfully');

        } catch (error) {
            console.warn('Google Auth setup failed:', error);
        }
    }

    replaceWithNativeGoogleButtons() {
        const googleButtons = document.querySelectorAll('.btn-google');
        console.log('Found', googleButtons.length, 'Google buttons to replace');

        googleButtons.forEach((button, index) => {
            // Create container for Google button
            const container = document.createElement('div');
            container.className = 'google-signin-container';
            container.id = `google-signin-${index}`;

            // Insert container before the original button
            button.parentNode.insertBefore(container, button);

            // Render native Google button
            window.google.accounts.id.renderButton(container, {
                theme: 'outline',
                size: 'large',
                text: 'continue_with',
                shape: 'rectangular',
                width: container.offsetWidth || 300,
                logo_alignment: 'left'
            });

            console.log(`Native Google button ${index} rendered in container:`, container);
        });
    }

    bindSocialEvents() {
        // Les boutons Google natifs gèrent leurs propres événements
        // Pas besoin d'écouter les clics manuellement
        console.log('Social events: Using native Google buttons');
    }

    async loginWithGoogle() {
        try {
            this.setButtonLoading('google', true);

            // Use Google Identity Services directly
            if (window.google?.accounts?.id) {
                // Trigger the Google One Tap or popup
                window.google.accounts.id.prompt((notification) => {
                    console.log('Google prompt result:', notification);
                    if (notification.isNotDisplayed() || notification.isSkippedMoment()) {
                        console.warn('Google One Tap not available, user needs to click manually');
                        this.setButtonLoading('google', false);
                    }
                });
            } else {
                console.error('Google Identity Services not loaded');
                this.authManager.notifications.show('Google Identity Services non disponible', 'error');
                this.setButtonLoading('google', false);
            }
        } catch (error) {
            console.error('Google login error:', error);
            this.authManager.notifications.show('Erreur de connexion Google', 'error');
            this.setButtonLoading('google', false);
        }
    }

    async handleGoogleResponse(response) {
        try {
            // Decode JWT token to get user info
            const payload = JSON.parse(atob(response.credential.split('.')[1]));
            await this.processSocialAuth('google', response.credential, payload);
        } catch (error) {
            console.error('Google response error:', error);
            this.authManager.notifications.show('Erreur de traitement Google', 'error');
        }
    }

    async processSocialAuth(provider, token, userInfo) {
        try {
            // Send social auth info to our backend
            const response = await fetch(`${AUTH_CONFIG.API_BASE_URL}/api/auth/social-login`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    provider,
                    token,
                    user_info: userInfo
                })
            });

            const result = await response.json();

            if (result.success) {
                // Store auth data
                localStorage.setItem(AUTH_CONFIG.STORAGE_KEYS.TOKEN, result.token);
                localStorage.setItem(AUTH_CONFIG.STORAGE_KEYS.USER, JSON.stringify(result.user));

                this.authManager.notifications.show(`Connexion ${provider} réussie !`, 'success');

                // Redirect to dashboard
                setTimeout(() => {
                    window.location.href = '/dashboard.html';
                }, 1500);
            } else {
                this.authManager.notifications.show(result.message || `Erreur de connexion ${provider}`, 'error');
            }
        } catch (error) {
            console.error('Social auth processing error:', error);
            this.authManager.notifications.show('Erreur de traitement de la connexion sociale', 'error');
        }
    }

    setButtonLoading(provider, loading) {
        const buttons = [
            document.getElementById(`${provider}Login`),
            document.getElementById(`${provider}Register`)
        ];

        buttons.forEach(button => {
            if (button) {
                if (loading) {
                    button.classList.add('loading');
                    button.disabled = true;
                } else {
                    button.classList.remove('loading');
                    button.disabled = false;
                }
            }
        });
    }
}

// ===== INITIALIZE ON DOM READY =====
document.addEventListener('DOMContentLoaded', () => {
    window.revolutionaryAuth = new RevolutionaryAuth();

    // Initialize social auth after main auth
    setTimeout(() => {
        window.socialAuth = new SocialAuthManager(window.revolutionaryAuth);
    }, 1000);
});

// ===== EXPORT FOR MODULE SYSTEMS =====
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { RevolutionaryAuth, NotificationManager, SocialAuthManager };
}
