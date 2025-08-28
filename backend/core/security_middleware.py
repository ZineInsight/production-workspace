"""
🛡️ SECURITY MIDDLEWARE - SÉCURITÉ PRODUCTION CENTRALISÉE
=========================================================
Middleware de sécurité pour tous les services Revolutionary Platform
Basé sur main_revolutionary_secure.py avec améliorations

Features:
- Validation requêtes et sanitization
- Rate limiting intelligent
- Session management sécurisé
- API key management
- Audit logs et monitoring
"""

import os
import logging
import secrets
import hashlib
import json
from datetime import datetime, timedelta
from functools import wraps
from typing import Dict, Any, Optional, List
from flask import request, jsonify, session, g, current_app
import re

# Setup logging
logger = logging.getLogger(__name__)


class SecurityMiddleware:
    """Middleware sécurité centralisé pour tous les services"""

    def __init__(self, app=None, config: Optional[Dict] = None):
        self.app = app
        self.config = config or {}

        # Configuration par défaut
        self.default_config = {
            'session_lifetime_hours': 24,
            'max_requests_per_hour': 1000,
            'require_https': True,
            'audit_logs_enabled': True,
            'rate_limiting_enabled': True,
            'ip_whitelist': [],
            'blocked_ips': []
        }

        # Merge config
        self.config = {**self.default_config, **self.config}

        # Cache pour rate limiting
        self.request_counts = {}
        self.blocked_ips_cache = set(self.config.get('blocked_ips', []))

        if app:
            self.init_app(app)

        logger.info("🛡️ SecurityMiddleware initialized")

    def init_app(self, app):
        """Initialise le middleware avec l'app Flask"""
        self.app = app

        # Middleware pré-requête
        app.before_request(self.before_request)
        app.after_request(self.after_request)

        logger.info("🔒 Security middleware registered with Flask app")

    def validate_environment(self) -> bool:
        """Valide les variables d'environnement critiques"""
        required_vars = [
            'SECRET_KEY',
            'STRIPE_SECRET_KEY',
            'STRIPE_PUBLIC_KEY'
        ]

        missing_vars = []
        for var in required_vars:
            if not os.environ.get(var):
                missing_vars.append(var)

        if missing_vars:
            logger.error(f"❌ Missing environment variables: {missing_vars}")
            return False

        logger.info("✅ Environment variables validated")
        return True

    def generate_session_token(self) -> str:
        """Génère un token de session sécurisé"""
        return secrets.token_urlsafe(32)

    def hash_ip_address(self, ip: str) -> str:
        """Hash une adresse IP pour les logs anonymes"""
        return hashlib.sha256(ip.encode()).hexdigest()[:16]

    def get_client_ip(self) -> str:
        """Récupère l'IP client en tenant compte des proxies"""
        # Headers possibles pour IP réelle
        headers_to_check = [
            'X-Forwarded-For',
            'X-Real-IP',
            'X-Client-IP',
            'CF-Connecting-IP'  # Cloudflare
        ]

        for header in headers_to_check:
            ip = request.headers.get(header)
            if ip:
                # Prendre la première IP si plusieurs
                return ip.split(',')[0].strip()

        return request.environ.get('REMOTE_ADDR', 'unknown')

    def is_ip_blocked(self, ip: str) -> bool:
        """Vérifie si une IP est bloquée"""
        return ip in self.blocked_ips_cache

    def is_ip_whitelisted(self, ip: str) -> bool:
        """Vérifie si une IP est whitelistée"""
        whitelist = self.config.get('ip_whitelist', [])
        return ip in whitelist if whitelist else True

    def check_rate_limit(self, ip: str) -> bool:
        """Vérifie les limites de taux de requêtes"""
        if not self.config.get('rate_limiting_enabled', True):
            return True

        now = datetime.now()
        hour_key = now.strftime('%Y-%m-%d-%H')
        ip_key = f"{ip}:{hour_key}"

        # Nettoyer les anciennes entrées
        keys_to_remove = []
        for key in self.request_counts:
            if not key.endswith(hour_key):
                keys_to_remove.append(key)

        for key in keys_to_remove:
            del self.request_counts[key]

        # Vérifier limite actuelle
        current_count = self.request_counts.get(ip_key, 0)
        max_requests = self.config.get('max_requests_per_hour', 1000)

        if current_count >= max_requests:
            logger.warning(f"🚫 Rate limit exceeded for IP: {self.hash_ip_address(ip)}")
            return False

        # Incrémenter compteur
        self.request_counts[ip_key] = current_count + 1
        return True

    def sanitize_input(self, data: Any) -> Any:
        """Sanitise les données d'entrée"""
        if isinstance(data, dict):
            return {key: self.sanitize_input(value) for key, value in data.items()}
        elif isinstance(data, list):
            return [self.sanitize_input(item) for item in data]
        elif isinstance(data, str):
            # Nettoyer les caractères dangereux
            dangerous_patterns = [
                r'<script.*?</script>',
                r'javascript:',
                r'on\w+\s*=',
                r'<.*?>'
            ]

            cleaned = data
            for pattern in dangerous_patterns:
                cleaned = re.sub(pattern, '', cleaned, flags=re.IGNORECASE | re.DOTALL)

            return cleaned.strip()

        return data

    def audit_log(self, event: str, details: Dict = None):
        """Enregistre un événement d'audit"""
        if not self.config.get('audit_logs_enabled', True):
            return

        audit_entry = {
            'timestamp': datetime.now().isoformat(),
            'event': event,
            'ip_hash': self.hash_ip_address(self.get_client_ip()),
            'user_agent': request.headers.get('User-Agent', 'unknown'),
            'endpoint': request.endpoint,
            'method': request.method,
            'details': details or {}
        }

        logger.info(f"🔍 AUDIT: {json.dumps(audit_entry)}")

    def before_request(self):
        """Middleware exécuté avant chaque requête"""
        client_ip = self.get_client_ip()

        # Vérifier IP bloquée
        if self.is_ip_blocked(client_ip):
            self.audit_log('blocked_ip_access', {'ip_hash': self.hash_ip_address(client_ip)})
            return jsonify({'error': 'Access denied'}), 403

        # Vérifier whitelist si configurée
        if not self.is_ip_whitelisted(client_ip):
            self.audit_log('non_whitelisted_access', {'ip_hash': self.hash_ip_address(client_ip)})
            return jsonify({'error': 'Access denied'}), 403

        # Vérifier rate limiting
        if not self.check_rate_limit(client_ip):
            self.audit_log('rate_limit_exceeded', {'ip_hash': self.hash_ip_address(client_ip)})
            return jsonify({'error': 'Rate limit exceeded'}), 429

        # HTTPS required en production
        if self.config.get('require_https', True) and not request.is_secure and request.headers.get('X-Forwarded-Proto') != 'https':
            if not current_app.debug:  # Seulement en production
                return jsonify({'error': 'HTTPS required'}), 400

        # Stocker l'IP dans le contexte
        g.client_ip = client_ip
        g.request_start_time = datetime.now()

    def after_request(self, response):
        """Middleware exécuté après chaque requête"""
        # Headers de sécurité
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'DENY'
        response.headers['X-XSS-Protection'] = '1; mode=block'
        response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'

        # CSP basique
        response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self' 'unsafe-inline'"

        # Log de la requête si audit activé
        if hasattr(g, 'request_start_time'):
            duration = (datetime.now() - g.request_start_time).total_seconds()

            if duration > 5.0:  # Log requêtes lentes
                self.audit_log('slow_request', {
                    'duration_seconds': duration,
                    'endpoint': request.endpoint,
                    'status_code': response.status_code
                })

        return response

    def require_valid_session(self, f):
        """Décorateur pour requérir une session valide"""
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'session_token' not in session:
                self.audit_log('missing_session_token')
                return jsonify({'error': 'Valid session required'}), 401

            # Vérifier expiration session
            session_created = session.get('created_at')
            if session_created:
                session_age = datetime.now() - datetime.fromisoformat(session_created)
                max_age = timedelta(hours=self.config.get('session_lifetime_hours', 24))

                if session_age > max_age:
                    session.clear()
                    self.audit_log('session_expired')
                    return jsonify({'error': 'Session expired'}), 401

            return f(*args, **kwargs)
        return decorated_function

    def create_secure_session(self, user_data: Dict = None):
        """Crée une session sécurisée"""
        session.clear()
        session['session_token'] = self.generate_session_token()
        session['created_at'] = datetime.now().isoformat()
        session['ip_hash'] = self.hash_ip_address(self.get_client_ip())

        if user_data:
            session['user_data'] = user_data

        self.audit_log('session_created')
        logger.info(f"🔐 Secure session created")

    def get_security_stats(self) -> Dict:
        """Retourne les statistiques de sécurité"""
        return {
            'blocked_ips_count': len(self.blocked_ips_cache),
            'active_rate_limits': len(self.request_counts),
            'config': {
                'rate_limiting_enabled': self.config.get('rate_limiting_enabled'),
                'audit_logs_enabled': self.config.get('audit_logs_enabled'),
                'max_requests_per_hour': self.config.get('max_requests_per_hour'),
                'session_lifetime_hours': self.config.get('session_lifetime_hours')
            }
        }
