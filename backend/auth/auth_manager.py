"""
🔐 REVOLUTIONARY AUTH - JWT & Redis Sessions
============================================
Système d'authentification complet pour ZineInsight Revolutionary

Features:
- JWT tokens sécurisés avec expiration
- Redis sessions pour performance
- Email verification avec SendGrid
- Password hashing bcrypt
- Rate limiting par IP
- Audit trail complet

Architecture:
- AuthManager: Gestion principale
- JWTHandler: Tokens JWT
- RedisSessionStore: Cache sessions
- EmailVerification: Envoi emails
- PaywallManager: Restrictions premium
"""

import jwt
import bcrypt
import redis
import json
import uuid
import logging
from datetime import datetime, timedelta
from typing import Dict, Optional, Tuple, Any
from flask import current_app, request
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import secrets
import re

logger = logging.getLogger(__name__)

class AuthManager:
    """Gestionnaire principal d'authentification"""

    def __init__(self, secret_key: str, redis_client=None, sendgrid_key: str = None):
        self.secret_key = secret_key
        self.redis_client = redis_client or redis.Redis(host='localhost', port=6379, decode_responses=True)
        self.sendgrid_key = sendgrid_key
        self.jwt_handler = JWTHandler(secret_key)
        self.session_store = RedisSessionStore(self.redis_client)
        self.email_verifier = EmailVerification(sendgrid_key) if sendgrid_key else None

        # Configuration
        self.token_expiry = timedelta(days=7)  # JWT expire après 7 jours
        self.session_expiry = 3600 * 24 * 7    # Session Redis 7 jours
        self.max_login_attempts = 5            # Max tentatives avant blocage
        self.lockout_duration = 1800           # 30 minutes de blocage

        logger.info("🔐 AuthManager initialized")

    def register_user(self, email: str, password: str, name: str = None) -> Dict[str, Any]:
        """Inscription utilisateur avec validation"""
        try:
            # Validation email
            if not self._is_valid_email(email):
                return {"success": False, "error": "Email invalide"}

            # Validation password
            if not self._is_strong_password(password):
                return {"success": False, "error": "Mot de passe trop faible (min 8 caractères, 1 majuscule, 1 chiffre)"}

            # Vérifier si l'utilisateur existe déjà
            if self._user_exists(email):
                return {"success": False, "error": "Utilisateur déjà existant"}

            # Hash du password
            password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            # Créer l'utilisateur
            user_id = str(uuid.uuid4())
            verification_token = secrets.token_urlsafe(32)

            user_data = {
                "id": user_id,
                "email": email,
                "name": name or email.split('@')[0],
                "password_hash": password_hash,
                "created_at": datetime.utcnow().isoformat(),
                "is_verified": False,
                "verification_token": verification_token,
                "subscription_tier": "free",  # free, premium, pro
                "usage_limits": {
                    "zscore_analyses": 1,      # 1 par mois en free
                    "skillgraph_scans": 1,     # 1 par mois en free
                    "wealth_portfolios": 0,    # 0 en free
                    "dashboard_access": False   # Pas d'accès dashboard en free
                },
                "usage_current": {
                    "zscore_analyses": 0,
                    "skillgraph_scans": 0,
                    "wealth_portfolios": 0,
                    "last_reset": datetime.utcnow().replace(day=1).isoformat()  # Reset mensuel
                }
            }

            # Sauvegarder dans Redis
            self.redis_client.setex(
                f"user:{email}",
                self.session_expiry,
                json.dumps(user_data)
            )

            # Envoyer email de vérification
            if self.email_verifier:
                verification_sent = self.email_verifier.send_verification_email(
                    email,
                    user_data["name"],
                    verification_token
                )
                if not verification_sent:
                    logger.warning(f"Failed to send verification email to {email}")

            logger.info(f"🎯 User registered: {email} (ID: {user_id})")

            return {
                "success": True,
                "user_id": user_id,
                "email": email,
                "name": user_data["name"],
                "verification_required": True
            }

        except Exception as e:
            logger.error(f"Registration error: {e}")
            return {"success": False, "error": "Erreur lors de l'inscription"}

    def login_user(self, email: str, password: str, ip_address: str = None) -> Dict[str, Any]:
        """Connexion utilisateur avec rate limiting"""
        try:
            # Vérifier rate limiting
            if not self._check_rate_limit(email, ip_address):
                return {"success": False, "error": "Trop de tentatives. Réessayez plus tard"}

            # Récupérer l'utilisateur
            user_data = self._get_user(email)
            if not user_data:
                self._increment_failed_attempts(email, ip_address)
                return {"success": False, "error": "Email ou mot de passe incorrect"}

            # Vérifier le password
            if not bcrypt.checkpw(password.encode('utf-8'), user_data["password_hash"].encode('utf-8')):
                self._increment_failed_attempts(email, ip_address)
                return {"success": False, "error": "Email ou mot de passe incorrect"}

            # Vérifier si le compte est vérifié
            if not user_data.get("is_verified", False):
                return {"success": False, "error": "Compte non vérifié. Vérifiez votre email"}

            # Générer JWT token
            token_payload = {
                "user_id": user_data["id"],
                "email": user_data["email"],
                "tier": user_data.get("subscription_tier", "free"),
                "iat": datetime.utcnow(),
                "exp": datetime.utcnow() + self.token_expiry
            }

            jwt_token = self.jwt_handler.encode_token(token_payload)

            # Créer session Redis
            session_id = str(uuid.uuid4())
            session_data = {
                "user_id": user_data["id"],
                "email": user_data["email"],
                "name": user_data["name"],
                "tier": user_data.get("subscription_tier", "free"),
                "login_time": datetime.utcnow().isoformat(),
                "ip_address": ip_address,
                "jwt_token": jwt_token
            }

            self.session_store.create_session(session_id, session_data)

            # Reset failed attempts
            self._reset_failed_attempts(email, ip_address)

            logger.info(f"✅ User logged in: {email} (Session: {session_id})")

            return {
                "success": True,
                "jwt_token": jwt_token,
                "session_id": session_id,
                "user": {
                    "id": user_data["id"],
                    "email": user_data["email"],
                    "name": user_data["name"],
                    "tier": user_data.get("subscription_tier", "free"),
                    "usage_limits": user_data.get("usage_limits", {}),
                    "usage_current": user_data.get("usage_current", {})
                }
            }

        except Exception as e:
            logger.error(f"Login error: {e}")
            return {"success": False, "error": "Erreur lors de la connexion"}

    def verify_email(self, token: str) -> Dict[str, Any]:
        """Vérification email avec token"""
        try:
            # Chercher l'utilisateur avec ce token
            for key in self.redis_client.scan_iter(match="user:*"):
                user_json = self.redis_client.get(key)
                if user_json:
                    user_data = json.loads(user_json)
                    if user_data.get("verification_token") == token:
                        # Marquer comme vérifié
                        user_data["is_verified"] = True
                        user_data["verified_at"] = datetime.utcnow().isoformat()
                        del user_data["verification_token"]

                        # Sauvegarder
                        self.redis_client.setex(
                            key,
                            self.session_expiry,
                            json.dumps(user_data)
                        )

                        logger.info(f"✅ Email verified: {user_data['email']}")
                        return {"success": True, "message": "Email vérifié avec succès"}

            return {"success": False, "error": "Token de vérification invalide"}

        except Exception as e:
            logger.error(f"Email verification error: {e}")
            return {"success": False, "error": "Erreur lors de la vérification"}

    def logout_user(self, session_id: str) -> Dict[str, Any]:
        """Déconnexion utilisateur"""
        try:
            self.session_store.delete_session(session_id)
            logger.info(f"🚪 User logged out (Session: {session_id})")
            return {"success": True, "message": "Déconnexion réussie"}
        except Exception as e:
            logger.error(f"Logout error: {e}")
            return {"success": False, "error": "Erreur lors de la déconnexion"}

    def get_user_from_token(self, jwt_token: str) -> Optional[Dict[str, Any]]:
        """Récupérer utilisateur depuis JWT token"""
        try:
            payload = self.jwt_handler.decode_token(jwt_token)
            if payload:
                user_data = self._get_user(payload["email"])
                if user_data:
                    return {
                        "id": user_data["id"],
                        "email": user_data["email"],
                        "name": user_data["name"],
                        "tier": user_data.get("subscription_tier", "free"),
                        "usage_limits": user_data.get("usage_limits", {}),
                        "usage_current": user_data.get("usage_current", {})
                    }
            return None
        except Exception as e:
            logger.error(f"Token validation error: {e}")
            return None

    # Méthodes privées
    def _is_valid_email(self, email: str) -> bool:
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def _is_strong_password(self, password: str) -> bool:
        if len(password) < 8:
            return False
        if not re.search(r'[A-Z]', password):
            return False
        if not re.search(r'[0-9]', password):
            return False
        return True

    def _user_exists(self, email: str) -> bool:
        return self.redis_client.exists(f"user:{email}")

    def _get_user(self, email: str) -> Optional[Dict[str, Any]]:
        user_json = self.redis_client.get(f"user:{email}")
        return json.loads(user_json) if user_json else None

    def _check_rate_limit(self, email: str, ip_address: str) -> bool:
        # Vérifier tentatives par email
        email_attempts = self.redis_client.get(f"failed_attempts:email:{email}")
        if email_attempts and int(email_attempts) >= self.max_login_attempts:
            return False

        # Vérifier tentatives par IP
        if ip_address:
            ip_attempts = self.redis_client.get(f"failed_attempts:ip:{ip_address}")
            if ip_attempts and int(ip_attempts) >= self.max_login_attempts * 3:  # Plus strict par IP
                return False

        return True

    def _increment_failed_attempts(self, email: str, ip_address: str):
        # Incrémenter tentatives email
        key_email = f"failed_attempts:email:{email}"
        self.redis_client.incr(key_email)
        self.redis_client.expire(key_email, self.lockout_duration)

        # Incrémenter tentatives IP
        if ip_address:
            key_ip = f"failed_attempts:ip:{ip_address}"
            self.redis_client.incr(key_ip)
            self.redis_client.expire(key_ip, self.lockout_duration)

    def _reset_failed_attempts(self, email: str, ip_address: str):
        self.redis_client.delete(f"failed_attempts:email:{email}")
        if ip_address:
            self.redis_client.delete(f"failed_attempts:ip:{ip_address}")


class JWTHandler:
    """Gestionnaire des tokens JWT"""

    def __init__(self, secret_key: str):
        self.secret_key = secret_key
        self.algorithm = 'HS256'

    def encode_token(self, payload: Dict[str, Any]) -> str:
        """Encoder un token JWT"""
        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)

    def decode_token(self, token: str) -> Optional[Dict[str, Any]]:
        """Décoder un token JWT"""
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload
        except jwt.ExpiredSignatureError:
            logger.warning("JWT token expired")
            return None
        except jwt.InvalidTokenError:
            logger.warning("Invalid JWT token")
            return None


class RedisSessionStore:
    """Gestionnaire des sessions Redis"""

    def __init__(self, redis_client):
        self.redis_client = redis_client
        self.session_expiry = 3600 * 24 * 7  # 7 jours

    def create_session(self, session_id: str, session_data: Dict[str, Any]):
        """Créer une session"""
        self.redis_client.setex(
            f"session:{session_id}",
            self.session_expiry,
            json.dumps(session_data)
        )

    def get_session(self, session_id: str) -> Optional[Dict[str, Any]]:
        """Récupérer une session"""
        session_json = self.redis_client.get(f"session:{session_id}")
        return json.loads(session_json) if session_json else None

    def delete_session(self, session_id: str):
        """Supprimer une session"""
        self.redis_client.delete(f"session:{session_id}")

    def refresh_session(self, session_id: str):
        """Rafraîchir l'expiration d'une session"""
        self.redis_client.expire(f"session:{session_id}", self.session_expiry)


class EmailVerification:
    """Gestionnaire d'envoi d'emails de vérification"""

    def __init__(self, sendgrid_api_key: str):
        self.sendgrid_api_key = sendgrid_api_key
        self.client = SendGridAPIClient(api_key=sendgrid_api_key) if sendgrid_api_key else None

    def send_verification_email(self, email: str, name: str, verification_token: str) -> bool:
        """Envoyer email de vérification"""
        if not self.client:
            logger.warning("SendGrid not configured, skipping email")
            return True  # Ne pas bloquer en dev

        try:
            verification_url = f"https://zineinsight.com/verify-email?token={verification_token}"

            html_content = f"""
            <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; background: #1a1a1a; color: #fff; border-radius: 16px; overflow: hidden;">
                <div style="background: linear-gradient(135deg, #FD1056, #FA709A); padding: 30px; text-align: center;">
                    <h1 style="margin: 0; font-size: 28px;">🚀 Bienvenue sur ZineInsight</h1>
                    <p style="margin: 10px 0 0 0; opacity: 0.9;">Votre révolution personnelle commence maintenant</p>
                </div>

                <div style="padding: 30px;">
                    <p style="font-size: 18px; margin-bottom: 20px;">Salut {name} ! 👋</p>

                    <p>Félicitations ! Vous avez rejoint la révolution de l'intelligence personnalisée avec nos 148 critères d'analyse :</p>

                    <div style="background: #2a2a2a; border-radius: 12px; padding: 20px; margin: 20px 0;">
                        <p style="margin: 0;">🏙️ <strong>ZScore</strong> - 49 critères géographiques</p>
                        <p style="margin: 5px 0;">💼 <strong>SkillGraph</strong> - 53 critères carrière</p>
                        <p style="margin: 5px 0 0 0;">💰 <strong>Wealth</strong> - 46 critères patrimoniaux</p>
                    </div>

                    <p>Pour activer votre compte et accéder à votre première analyse gratuite :</p>

                    <div style="text-align: center; margin: 30px 0;">
                        <a href="{verification_url}" style="background: linear-gradient(135deg, #FD1056, #FA709A); color: white; padding: 15px 30px; text-decoration: none; border-radius: 30px; font-weight: bold; display: inline-block; font-size: 16px;">
                            ✅ Vérifier mon email
                        </a>
                    </div>

                    <p style="font-size: 14px; opacity: 0.8; margin-top: 30px;">Si le bouton ne fonctionne pas, copiez ce lien dans votre navigateur :</p>
                    <p style="font-size: 12px; word-break: break-all; background: #2a2a2a; padding: 10px; border-radius: 6px;">{verification_url}</p>
                </div>

                <div style="background: #2a2a2a; padding: 20px; text-align: center; font-size: 14px; opacity: 0.8;">
                    <p>🚀 ZineInsight Revolutionary - Intelligence artificielle personnalisée</p>
                    <p>Si vous n'avez pas créé ce compte, ignorez cet email.</p>
                </div>
            </div>
            """

            message = Mail(
                from_email='noreply@zineinsight.com',
                to_emails=email,
                subject='🚀 Vérifiez votre compte ZineInsight Revolutionary',
                html_content=html_content
            )

            response = self.client.send(message)
            logger.info(f"📧 Verification email sent to {email} (Status: {response.status_code})")
            return True

        except Exception as e:
            logger.error(f"Failed to send verification email: {e}")
            return False

# Singleton global pour l'application
auth_manager = None

def init_auth_manager(app):
    """Initialiser l'AuthManager avec la config Flask"""
    global auth_manager

    secret_key = app.config.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    sendgrid_key = app.config.get('SENDGRID_API_KEY')

    # Redis client
    redis_client = redis.Redis(
        host=app.config.get('REDIS_HOST', 'localhost'),
        port=app.config.get('REDIS_PORT', 6379),
        decode_responses=True
    )

    auth_manager = AuthManager(secret_key, redis_client, sendgrid_key)
    logger.info("🔐 Auth system initialized")
    return auth_manager

def get_auth_manager():
    """Récupérer l'instance AuthManager"""
    return auth_manager
