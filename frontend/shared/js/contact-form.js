/**
 * 📧 FORMULAIRE DE CONTACT - GESTIONNAIRE JAVASCRIPT
 */

class ContactFormManager {
    constructor() {
        this.form = document.getElementById('contactForm');
        this.submitButton = document.querySelector('.btn-contact');
        this.originalButtonText = 'Envoyer';
        this.init();
    }

    init() {
        if (this.form) {
            this.form.addEventListener('submit', (e) => this.handleSubmit(e));
            console.log('📧 Contact form manager initialized');
        }
    }

    async handleSubmit(event) {
        event.preventDefault();
        this.setLoadingState(true);

        try {
            const formData = new FormData(this.form);
            const data = {
                name: formData.get('name').trim(),
                email: formData.get('email').trim(),
                project: formData.get('project'),
                message: formData.get('message').trim()
            };

            const response = await fetch('/contact.php', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });

            const result = await response.json();

            if (result.success) {
                this.showMessage('Message envoyé avec succès ! Nous vous répondrons rapidement.', 'success');
                this.form.reset();
            } else {
                this.showMessage(result.error || 'Erreur lors de l\'envoi', 'error');
            }

        } catch (error) {
            this.showMessage('Erreur de connexion. Veuillez réessayer.', 'error');
        } finally {
            this.setLoadingState(false);
        }
    }

    setLoadingState(loading) {
        if (this.submitButton) {
            this.submitButton.disabled = loading;
            this.submitButton.textContent = loading ? 'Envoi en cours...' : this.originalButtonText;
        }
    }

    showMessage(message, type) {
        const existing = document.querySelector('.contact-message');
        if (existing) existing.remove();

        const messageEl = document.createElement('div');
        messageEl.className = 'contact-message';
        messageEl.textContent = message;
        messageEl.style.cssText = `
            padding: 12px 16px; margin-top: 16px; border-radius: 8px;
            background: ${type === 'success' ? '#d4edda' : '#f8d7da'};
            color: ${type === 'success' ? '#155724' : '#721c24'};
            border: 1px solid ${type === 'success' ? '#c3e6cb' : '#f5c6cb'};
        `;

        this.form.insertAdjacentElement('afterend', messageEl);
        setTimeout(() => messageEl.remove(), 5000);
    }
}

// Auto-initialisation
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => new ContactFormManager());
} else {
    new ContactFormManager();
}
