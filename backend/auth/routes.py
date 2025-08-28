"""
🔐 REVOLUTIONARY AUTH ROUTES - Flask Blueprint
=============================================
Routes d'authentification pour l'API Revolutionary

Endpoints:
- POST /auth/register - Inscription
- POST /auth/login - Connexion
- POST /auth/logout - Déconnexion
- GET /auth/verify-email - Vérification email
- GET /auth/me - Profil utilisateur
- POST /auth/forgot-password - Mot de passe oublié
- POST /auth/reset-password - Reset mot de passe
"""

from flask import Blueprint, request, jsonify, current_app
from functools import wraps
import logging
import json
import uuid
from datetime import datetime, timedelta
from datetime import datetime

from .auth_manager import get_auth_manager
from .paywall_manager import PaywallManager
from .freemium_manager import FreemiumManager

logger = logging.getLogger(__name__)

# Blueprint auth
auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

# Paywall manager global
paywall_manager = None
freemium_manager = None

def init_paywall_manager():
    """Initialiser le PaywallManager"""
    global paywall_manager, freemium_manager
    paywall_manager = PaywallManager()
    auth_manager = get_auth_manager()
    freemium_manager = FreemiumManager(auth_manager.redis_client, auth_manager)
    return paywall_manager

def require_auth(f):
    """Décorateur pour exiger une authentification"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('Authorization')

        if not auth_header or not auth_header.startswith('Bearer '):
            return jsonify({"success": False, "error": "Token d'authentification requis"}), 401

        token = auth_header.split(' ')[1]
        auth_manager = get_auth_manager()
        user = auth_manager.get_user_from_token(token)

        if not user:
            return jsonify({"success": False, "error": "Token invalide ou expiré"}), 401

        # Ajouter l'utilisateur au contexte de la requête
        request.current_user = user
        return f(*args, **kwargs)

    return decorated_function

def require_premium(f):
    """Décorateur pour exiger un abonnement premium"""
    @wraps(f)
    @require_auth
    def decorated_function(*args, **kwargs):
        user = request.current_user

        if user.get('tier') == 'free':
            return jsonify({
                "success": False,
                "error": "Fonctionnalité premium requise",
                "upgrade_url": "https://zineinsight.com/pricing"
            }), 403

        return f(*args, **kwargs)

    return decorated_function

@auth_bp.route('/register', methods=['POST'])
def register():
    """Inscription utilisateur"""
    try:
        data = request.get_json()

        if not data:
            return jsonify({"success": False, "error": "Données JSON requises"}), 400

        email = data.get('email', '').strip().lower()
        password = data.get('password', '')
        name = data.get('name', '').strip()

        if not email or not password:
            return jsonify({"success": False, "error": "Email et mot de passe requis"}), 400

        auth_manager = get_auth_manager()
        result = auth_manager.register_user(email, password, name)

        if result['success']:
            logger.info(f"🎯 User registered successfully: {email}")
            return jsonify(result), 201
        else:
            return jsonify(result), 400

    except Exception as e:
        logger.error(f"Registration endpoint error: {e}")
        return jsonify({"success": False, "error": "Erreur serveur"}), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    """Connexion utilisateur"""
    try:
        data = request.get_json()

        if not data:
            return jsonify({"success": False, "error": "Données JSON requises"}), 400

        email = data.get('email', '').strip().lower()
        password = data.get('password', '')

        if not email or not password:
            return jsonify({"success": False, "error": "Email et mot de passe requis"}), 400

        # IP pour rate limiting
        ip_address = request.remote_addr or request.environ.get('HTTP_X_FORWARDED_FOR', 'unknown')

        auth_manager = get_auth_manager()
        result = auth_manager.login_user(email, password, ip_address)

        if result['success']:
            logger.info(f"✅ User logged in successfully: {email}")
            return jsonify(result), 200
        else:
            return jsonify(result), 401

    except Exception as e:
        logger.error(f"Login endpoint error: {e}")
        return jsonify({"success": False, "error": "Erreur serveur"}), 500

@auth_bp.route('/logout', methods=['POST'])
@require_auth
def logout():
    """Déconnexion utilisateur"""
    try:
        # Récupérer le session_id depuis le header ou body
        session_id = request.headers.get('X-Session-ID') or request.get_json().get('session_id')

        if session_id:
            auth_manager = get_auth_manager()
            result = auth_manager.logout_user(session_id)
            return jsonify(result), 200
        else:
            return jsonify({"success": True, "message": "Déconnexion côté client"}), 200

    except Exception as e:
        logger.error(f"Logout endpoint error: {e}")
        return jsonify({"success": False, "error": "Erreur serveur"}), 500

@auth_bp.route('/verify-email', methods=['GET'])
def verify_email():
    """Vérification email avec token"""
    try:
        token = request.args.get('token')

        if not token:
            return jsonify({"success": False, "error": "Token de vérification requis"}), 400

        auth_manager = get_auth_manager()
        result = auth_manager.verify_email(token)

        if result['success']:
            # Rediriger vers le frontend avec succès
            return f"""
            <html>
                <head>
                    <title>Email vérifié - ZineInsight</title>
                    <style>
                        body {{
                            font-family: Arial, sans-serif;
                            background: linear-gradient(135deg, #1a1a1a, #2a2a2a);
                            color: white;
                            text-align: center;
                            padding: 50px;
                        }}
                        .container {{
                            max-width: 500px;
                            margin: 0 auto;
                            background: rgba(255,255,255,0.05);
                            padding: 40px;
                            border-radius: 16px;
                            backdrop-filter: blur(10px);
                        }}
                        .success {{ color: #00D4AA; font-size: 48px; margin-bottom: 20px; }}
                        h1 {{ color: #FD1056; margin-bottom: 20px; }}
                        .btn {{
                            background: linear-gradient(135deg, #FD1056, #FA709A);
                            color: white;
                            padding: 15px 30px;
                            text-decoration: none;
                            border-radius: 30px;
                            display: inline-block;
                            margin-top: 20px;
                            font-weight: bold;
                        }}
                    </style>
                </head>
                <body>
                    <div class="container">
                        <div class="success">✅</div>
                        <h1>Email vérifié !</h1>
                        <p>Votre compte ZineInsight Revolutionary est maintenant activé.</p>
                        <p>Vous pouvez maintenant accéder à votre première analyse gratuite !</p>
                        <a href="https://zineinsight.com" class="btn">🚀 Accéder au dashboard</a>
                    </div>

                    <script>
                        // Auto-redirect après 5 secondes
                        setTimeout(() => {{
                            window.location.href = 'https://zineinsight.com?verified=true';
                        }}, 5000);
                    </script>
                </body>
            </html>
            """
        else:
            return f"""
            <html>
                <head>
                    <title>Erreur vérification - ZineInsight</title>
                    <style>
                        body {{
                            font-family: Arial, sans-serif;
                            background: linear-gradient(135deg, #1a1a1a, #2a2a2a);
                            color: white;
                            text-align: center;
                            padding: 50px;
                        }}
                        .container {{
                            max-width: 500px;
                            margin: 0 auto;
                            background: rgba(255,255,255,0.05);
                            padding: 40px;
                            border-radius: 16px;
                            backdrop-filter: blur(10px);
                        }}
                        .error {{ color: #FD1056; font-size: 48px; margin-bottom: 20px; }}
                    </style>
                </head>
                <body>
                    <div class="container">
                        <div class="error">❌</div>
                        <h1>Erreur de vérification</h1>
                        <p>{result['error']}</p>
                        <a href="https://zineinsight.com" class="btn">🏠 Retour à l'accueil</a>
                    </div>
                </body>
            </html>
            """

    except Exception as e:
        logger.error(f"Email verification endpoint error: {e}")
        return jsonify({"success": False, "error": "Erreur serveur"}), 500

@auth_bp.route('/me', methods=['GET'])
@require_auth
def get_profile():
    """Récupérer le profil utilisateur"""
    try:
        user = request.current_user

        # Récupérer les données complètes depuis Redis
        auth_manager = get_auth_manager()
        full_user_data = auth_manager._get_user(user['email'])

        if full_user_data:
            # Retourner les infos sécurisées (sans password_hash)
            safe_user_data = {
                "id": full_user_data["id"],
                "email": full_user_data["email"],
                "name": full_user_data["name"],
                "subscription_tier": full_user_data.get("subscription_tier", "free"),
                "is_verified": full_user_data.get("is_verified", False),
                "created_at": full_user_data.get("created_at"),
                "usage_limits": full_user_data.get("usage_limits", {}),
                "usage_current": full_user_data.get("usage_current", {}),
            }

            return jsonify({"success": True, "user": safe_user_data}), 200
        else:
            return jsonify({"success": False, "error": "Utilisateur introuvable"}), 404

    except Exception as e:
        logger.error(f"Profile endpoint error: {e}")
        return jsonify({"success": False, "error": "Erreur serveur"}), 500

@auth_bp.route('/check-usage', methods=['POST'])
@require_auth
def check_usage():
    """Vérifier les limites d'usage pour un service"""
    try:
        data = request.get_json()
        service = data.get('service')  # zscore, skillgraph, wealth

        if not service:
            return jsonify({"success": False, "error": "Service requis"}), 400

        global paywall_manager
        if not paywall_manager:
            paywall_manager = init_paywall_manager()

        user = request.current_user
        can_use, remaining, limit = paywall_manager.check_usage_limit(user['email'], service)

        return jsonify({
            "success": True,
            "can_use": can_use,
            "remaining": remaining,
            "limit": limit,
            "service": service,
            "user_tier": user.get('tier', 'free')
        }), 200

    except Exception as e:
        logger.error(f"Check usage endpoint error: {e}")
        return jsonify({"success": False, "error": "Erreur serveur"}), 500

@auth_bp.route('/increment-usage', methods=['POST'])
@require_auth
def increment_usage():
    """Incrémenter l'usage d'un service"""
    try:
        data = request.get_json()
        service = data.get('service')

        if not service:
            return jsonify({"success": False, "error": "Service requis"}), 400

        global paywall_manager
        if not paywall_manager:
            paywall_manager = init_paywall_manager()

        user = request.current_user
        success = paywall_manager.increment_usage(user['email'], service)

        if success:
            return jsonify({"success": True, "message": f"Usage {service} incrémenté"}), 200
        else:
            return jsonify({"success": False, "error": "Limite d'usage atteinte"}), 403

    except Exception as e:
        logger.error(f"Increment usage endpoint error: {e}")
        return jsonify({"success": False, "error": "Erreur serveur"}), 500

# Routes de développement (à supprimer en production)
@auth_bp.route('/dev/create-premium-user', methods=['POST'])
def dev_create_premium_user():
    """Créer un utilisateur premium pour les tests (DEV UNIQUEMENT)"""
    if current_app.config.get('ENV') == 'production':
        return jsonify({"error": "Route de développement non disponible en production"}), 404

    try:
        auth_manager = get_auth_manager()

        # Créer un utilisateur premium
        email = "premium@test.com"
        password = "Premium123!"
        name = "Premium User"

        # Supprimer s'il existe déjà
        auth_manager.redis_client.delete(f"user:{email}")

        # Créer avec tier premium
        result = auth_manager.register_user(email, password, name)

        if result['success']:
            # Upgrade vers premium et vérifier directement
            user_data = auth_manager._get_user(email)
            user_data['subscription_tier'] = 'premium'
            user_data['is_verified'] = True
            user_data['usage_limits'] = {
                "zscore_analyses": -1,      # Illimité
                "skillgraph_scans": -1,     # Illimité
                "wealth_portfolios": -1,    # Illimité
                "dashboard_access": True    # Accès complet
            }

            # Sauvegarder
            auth_manager.redis_client.setex(
                f"user:{email}",
                auth_manager.session_expiry,
                json.dumps(user_data)
            )

            # Login automatique
            login_result = auth_manager.login_user(email, password, request.remote_addr)

            return jsonify({
                "success": True,
                "message": "Utilisateur premium créé",
                "email": email,
                "password": password,
                "login_data": login_result
            }), 201
        else:
            return jsonify(result), 400

    except Exception as e:
        logger.error(f"Dev premium user creation error: {e}")
        return jsonify({"success": False, "error": "Erreur serveur"}), 500


# 📊 DASHBOARD ANALYTICS ENDPOINTS
@auth_bp.route('/user-analytics', methods=['GET'])
@require_auth
def get_user_analytics():
    """Récupérer les analytics utilisateur pour le dashboard"""
    try:
        user = request.current_user
        user_email = user['email']

        auth_manager = get_auth_manager()

        # Récupérer les données utilisateur complètes
        full_user_data = auth_manager._get_user(user_email)
        if not full_user_data:
            return jsonify({"success": False, "error": "Utilisateur introuvable"}), 404

        # Récupérer l'historique des analyses depuis Redis
        analysis_history = auth_manager.redis_client.lrange(f"user_analyses:{user_email}", 0, -1)

        # Parser l'historique
        parsed_analyses = []
        for analysis in analysis_history:
            try:
                parsed_analysis = json.loads(analysis)
                parsed_analyses.append(parsed_analysis)
            except:
                continue

        # Calculer les statistiques
        total_analyses = len(parsed_analyses)

        # Scores moyens par service
        zscore_scores = [a.get('score', 0) for a in parsed_analyses if a.get('service') == 'zscore']
        skillgraph_scores = [a.get('score', 0) for a in parsed_analyses if a.get('service') == 'skillgraph']
        wealth_scores = [a.get('score', 0) for a in parsed_analyses if a.get('service') == 'wealth']

        avg_zscore = sum(zscore_scores) / len(zscore_scores) if zscore_scores else 0
        avg_skillgraph = sum(skillgraph_scores) / len(skillgraph_scores) if skillgraph_scores else 0
        avg_wealth = sum(wealth_scores) / len(wealth_scores) if wealth_scores else 0

        # Top villes/secteurs mentionnés
        mentioned_cities = []
        mentioned_sectors = []
        for analysis in parsed_analyses:
            if analysis.get('service') == 'zscore' and analysis.get('results'):
                cities = [r.get('name') for r in analysis.get('results', [])[:3]]
                mentioned_cities.extend(cities)
            elif analysis.get('service') == 'skillgraph' and analysis.get('results'):
                sectors = [r.get('sector') for r in analysis.get('results', [])[:3]]
                mentioned_sectors.extend(sectors)

        # Compter les occurrences
        from collections import Counter
        top_cities = dict(Counter(mentioned_cities).most_common(5))
        top_sectors = dict(Counter(mentioned_sectors).most_common(5))

        # Progression mensuelle (simulée pour commencer)
        import datetime
        current_month = datetime.datetime.now().month
        monthly_progress = []
        for i in range(6):  # 6 derniers mois
            month_analyses = [a for a in parsed_analyses
                            if a.get('timestamp', '').startswith(f"2025-{current_month-i:02d}")]
            avg_score = sum([a.get('score', 0) for a in month_analyses]) / len(month_analyses) if month_analyses else 0
            monthly_progress.append(round(avg_score, 1))

        # Construire la réponse
        analytics_data = {
            "success": True,
            "user_stats": {
                "total_analyses": total_analyses,
                "avg_zscore": round(avg_zscore, 1),
                "avg_skillgraph": round(avg_skillgraph, 1),
                "avg_wealth": round(avg_wealth, 1),
                "subscription_tier": full_user_data.get("subscription_tier", "free"),
                "usage_current": full_user_data.get("usage_current", {}),
                "usage_limits": full_user_data.get("usage_limits", {})
            },
            "analytics": {
                "monthly_trend": monthly_progress[::-1],  # Plus récent en dernier
                "top_cities": top_cities,
                "top_sectors": top_sectors,
                "service_usage": {
                    "zscore": len(zscore_scores),
                    "skillgraph": len(skillgraph_scores),
                    "wealth": len(wealth_scores)
                }
            },
            "recent_analyses": parsed_analyses[-5:]  # 5 dernières analyses
        }

        return jsonify(analytics_data), 200

    except Exception as e:
        logger.error(f"User analytics endpoint error: {e}")
        return jsonify({"success": False, "error": "Erreur serveur"}), 500


@auth_bp.route('/user-results/<service>', methods=['GET'])
@require_auth
def get_user_results(service):
    """Récupérer les résultats d'analyses d'un service spécifique"""
    try:
        if service not in ['zscore', 'skillgraph', 'wealth']:
            return jsonify({"success": False, "error": "Service non supporté"}), 400

        user = request.current_user
        user_email = user['email']

        auth_manager = get_auth_manager()

        # Récupérer les résultats depuis Redis
        results_key = f"user_results:{user_email}:{service}"
        results_data = auth_manager.redis_client.get(results_key)

        if results_data:
            try:
                parsed_results = json.loads(results_data)
                return jsonify({
                    "success": True,
                    "service": service,
                    "results": parsed_results,
                    "cached": True
                }), 200
            except:
                pass

        # Si pas de résultats cachés, retourner structure vide
        return jsonify({
            "success": True,
            "service": service,
            "results": None,
            "message": f"Aucune analyse {service} trouvée. Lancez une analyse d'abord."
        }), 200

    except Exception as e:
        logger.error(f"User results endpoint error: {e}")
        return jsonify({"success": False, "error": "Erreur serveur"}), 500


@auth_bp.route('/save-analysis', methods=['POST'])
@require_auth
def save_analysis():
    """Sauvegarder une analyse dans l'historique utilisateur"""
    try:
        user = request.current_user
        user_email = user['email']
        data = request.get_json()

        if not data:
            return jsonify({"success": False, "error": "Données requises"}), 400

        service = data.get('service')  # zscore, skillgraph, wealth
        results = data.get('results')
        score = data.get('score')
        questionnaire = data.get('questionnaire', {})

        if not all([service, results]):
            return jsonify({"success": False, "error": "Service et résultats requis"}), 400

        auth_manager = get_auth_manager()

        # Préparer l'entrée d'historique
        import datetime, json
        analysis_entry = {
            "service": service,
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "score": score or 0,
            "results": results,
            "questionnaire_summary": {
                "budget": questionnaire.get('budget_monthly'),
                "age": questionnaire.get('age'),
                "status": questionnaire.get('status'),
                "preferences": questionnaire.get('preferences', {})
            }
        }

        # Ajouter à l'historique (LIFO - plus récent en premier)
        auth_manager.redis_client.lpush(
            f"user_analyses:{user_email}",
            json.dumps(analysis_entry)
        )

        # Garder seulement les 50 dernières analyses
        auth_manager.redis_client.ltrim(f"user_analyses:{user_email}", 0, 49)

        # Sauvegarder aussi les résultats détaillés
        auth_manager.redis_client.setex(
            f"user_results:{user_email}:{service}",
            86400 * 7,  # 7 jours
            json.dumps({
                "timestamp": analysis_entry["timestamp"],
                "results": results,
                "score": score,
                "questionnaire": questionnaire
            })
        )

        return jsonify({
            "success": True,
            "message": "Analyse sauvegardée",
            "analysis_id": analysis_entry["timestamp"]
        }), 200

    except Exception as e:
        logger.error(f"Save analysis endpoint error: {e}")
        return jsonify({"success": False, "error": "Erreur serveur"}), 500


@auth_bp.route('/social-login', methods=['POST'])
def social_login():
    """Authentification via providers sociaux (Google, Microsoft, Apple)"""
    try:
        data = request.get_json()
        logger.info(f"Social login request: {data}")

        if not data:
            return jsonify({"success": False, "error": "Données requises"}), 400

        provider = data.get('provider')  # google, microsoft, apple
        token = data.get('token')
        user_info = data.get('user_info', {})
        action = data.get('action', 'login')  # 'login' ou 'register'

        logger.info(f"Social login: {action} with {provider} for {user_info.get('email', 'no-email')}")

        if not all([provider, token]):
            return jsonify({"success": False, "error": "Provider et token requis"}), 400

        # Valider le provider
        if provider not in ['google', 'microsoft', 'apple']:
            return jsonify({"success": False, "error": "Provider non supporté"}), 400

        try:
            auth_manager = get_auth_manager()
            logger.info("Auth manager obtained successfully")
        except Exception as e:
            logger.error(f"Failed to get auth manager: {e}")
            return jsonify({"success": False, "error": "Erreur système auth"}), 500

        # Extraire les informations utilisateur selon le provider
        if provider == 'google':
            email = user_info.get('email')
            name = user_info.get('name') or f"{user_info.get('given_name', '')} {user_info.get('family_name', '')}".strip()
            provider_id = user_info.get('sub')
        elif provider == 'microsoft':
            email = user_info.get('mail') or user_info.get('userPrincipalName')
            name = user_info.get('displayName') or user_info.get('givenName', '') + ' ' + user_info.get('surname', '')
            provider_id = user_info.get('id')
        elif provider == 'apple':
            email = user_info.get('email')
            name = user_info.get('name', {}).get('firstName', '') + ' ' + user_info.get('name', {}).get('lastName', '')
            provider_id = user_info.get('sub')

        if not email:
            return jsonify({"success": False, "error": "Email requis pour l'authentification sociale"}), 400

        logger.info(f"Processed user info: email={email}, name={name}, provider_id={provider_id}")

        # Vérifier si l'utilisateur existe déjà
        try:
            existing_user = auth_manager._get_user(email.lower())
            logger.info(f"User lookup result: {'found' if existing_user else 'not found'}")
        except Exception as e:
            logger.error(f"Failed to lookup user: {e}")
            return jsonify({"success": False, "error": "Erreur lookup utilisateur"}), 500

        if existing_user:
            # Utilisateur existant
            if action == 'register':
                # Si l'utilisateur essaie de s'inscrire mais existe déjà
                return jsonify({
                    "success": False,
                    "error": "Un compte existe déjà avec cet email. Utilisez 'Se connecter' à la place."
                }), 409

            # Connexion - Mettre à jour les infos de provider social
            try:
                existing_user[f'{provider}_id'] = provider_id
                existing_user[f'{provider}_connected'] = True
                existing_user['last_social_login'] = datetime.utcnow().isoformat()

                # Sauvegarder les modifications
                auth_manager.redis_client.set(
                    f"user:{email.lower()}",
                    json.dumps(existing_user)
                )
                logger.info("User updated successfully")
            except Exception as e:
                logger.error(f"Failed to update user: {e}")
                return jsonify({"success": False, "error": "Erreur mise à jour utilisateur"}), 500

            # Générer JWT token avec la logique existante
            try:
                token_payload = {
                    "user_id": existing_user["id"],
                    "email": existing_user["email"],
                    "tier": existing_user.get("subscription_tier", "free"),
                    "iat": int(datetime.utcnow().timestamp()),  # Conversion en timestamp
                    "exp": int((datetime.utcnow() + timedelta(days=7)).timestamp())  # 7 jours
                }

                jwt_token = auth_manager.jwt_handler.encode_token(token_payload)
                logger.info("JWT token generated successfully")
            except Exception as e:
                logger.error(f"Failed to generate JWT: {e}")
                return jsonify({"success": False, "error": "Erreur génération token"}), 500

            return jsonify({
                "success": True,
                "token": jwt_token,
                "user": {
                    "id": existing_user['id'],
                    "email": existing_user['email'],
                    "name": existing_user['name'],
                    "tier": existing_user.get('subscription_tier', 'free'),
                    "social_provider": provider
                },
                "message": f"Connexion {provider} réussie"
            }), 200

        else:
            # Nouvel utilisateur
            if action == 'login':
                # Si l'utilisateur essaie de se connecter mais n'existe pas
                return jsonify({
                    "success": False,
                    "error": "Aucun compte trouvé avec cet email. Utilisez 'Créer un compte' à la place."
                }), 404

            # Création de compte via social login
            import secrets
            user_id = str(uuid.uuid4())

            user_data = {
                "id": user_id,
                "email": email.lower(),
                "name": name.strip() or "Utilisateur",
                "password_hash": None,  # Pas de mot de passe pour auth sociale
                "created_at": datetime.utcnow().isoformat(),
                "is_verified": True,  # Auto-vérifié via provider social
                "verified_at": datetime.utcnow().isoformat(),
                "subscription_tier": "free",
                "usage_limits": {
                    "zscore_analyses": 1,
                    "skillgraph_scans": 1,
                    "wealth_portfolios": 0,
                    "dashboard_access": False
                },
                "usage_current": {
                    "zscore_analyses": 0,
                    "skillgraph_scans": 0,
                    "wealth_portfolios": 0,
                    "last_reset": datetime.utcnow().replace(day=1).isoformat()  # 1er du mois
                },
                f'{provider}_id': provider_id,
                f'{provider}_connected': True,
                'social_provider': provider,
                'created_via': f'social_{provider}'
            }

            # Sauvegarder l'utilisateur
            auth_manager.redis_client.set(
                f"user:{email.lower()}",
                json.dumps(user_data)
            )

            # Générer JWT token avec la logique existante
            try:
                token_payload = {
                    "user_id": user_data["id"],
                    "email": user_data["email"],
                    "tier": user_data.get("subscription_tier", "free"),
                    "iat": int(datetime.utcnow().timestamp()),  # Conversion en timestamp
                    "exp": int((datetime.utcnow() + timedelta(days=7)).timestamp())  # 7 jours
                }

                jwt_token = auth_manager.jwt_handler.encode_token(token_payload)
            except Exception as e:
                logger.error(f"Failed to generate JWT for new user: {e}")
                return jsonify({"success": False, "error": "Erreur génération token"}), 500

            logger.info(f"✅ New social user created via {provider}: {email}")

            return jsonify({
                "success": True,
                "token": jwt_token,
                "user": {
                    "id": user_data['id'],
                    "email": user_data['email'],
                    "name": user_data['name'],
                    "tier": user_data['subscription_tier'],
                    "social_provider": provider
                },
                "message": f"Compte créé via {provider}",
                "is_new_user": True
            }), 201

    except Exception as e:
        logger.error(f"Social login endpoint error: {e}")
        return jsonify({"success": False, "error": "Erreur serveur"}), 500


# ===================================================================
# 💰 FREEMIUM DASHBOARD ENDPOINTS
# ===================================================================

@auth_bp.route('/dashboard/limitations', methods=['GET'])
@require_auth
def get_dashboard_limitations():
    """Récupérer les limitations dashboard pour l'utilisateur"""
    try:
        user = request.current_user
        user_email = user['email']

        init_paywall_manager()  # S'assurer que freemium_manager est initialisé

        result = freemium_manager.get_dashboard_limitations(user_email)

        if result.get("error"):
            return jsonify({"success": False, "error": result["error"]}), 400

        return jsonify(result), 200

    except Exception as e:
        logger.error(f"Dashboard limitations endpoint error: {e}")
        return jsonify({"success": False, "error": "Erreur serveur"}), 500


@auth_bp.route('/paywall/check-access', methods=['POST'])
@require_auth
def check_paywall_access():
    """Vérifier l'accès à une ressource spécifique"""
    try:
        data = request.get_json()
        user = request.current_user
        user_email = user['email']

        paywall_type = data.get('paywall_type')
        resource_id = data.get('resource_id')

        if not paywall_type:
            return jsonify({"success": False, "error": "Type paywall requis"}), 400

        init_paywall_manager()

        result = freemium_manager.check_user_access(user_email, paywall_type, resource_id)

        return jsonify({
            "success": True,
            "access_result": result
        }), 200

    except Exception as e:
        logger.error(f"Paywall access check error: {e}")
        return jsonify({"success": False, "error": "Erreur serveur"}), 500


@auth_bp.route('/paywall/create-session', methods=['POST'])
@require_auth
def create_paywall_session():
    """Créer une session paywall pour Stripe"""
    try:
        data = request.get_json()
        user = request.current_user
        user_email = user['email']

        paywall_type = data.get('paywall_type')
        resource_id = data.get('resource_id')
        metadata = data.get('metadata', {})

        if not paywall_type:
            return jsonify({"success": False, "error": "Type paywall requis"}), 400

        init_paywall_manager()

        result = freemium_manager.create_paywall_session(user_email, paywall_type, resource_id, metadata)

        if not result.get("success"):
            return jsonify(result), 400

        return jsonify(result), 200

    except Exception as e:
        logger.error(f"Paywall session creation error: {e}")
        return jsonify({"success": False, "error": "Erreur serveur"}), 500


@auth_bp.route('/paywall/process-payment', methods=['POST'])
@require_auth
def process_paywall_payment():
    """Traiter un paiement paywall réussi"""
    try:
        data = request.get_json()

        session_id = data.get('session_id')
        stripe_payment_data = data.get('stripe_data', {})

        if not session_id:
            return jsonify({"success": False, "error": "Session ID requis"}), 400

        init_paywall_manager()

        result = freemium_manager.process_successful_payment(session_id, stripe_payment_data)

        if not result.get("success"):
            return jsonify(result), 400

        return jsonify(result), 200

    except Exception as e:
        logger.error(f"Paywall payment processing error: {e}")
        return jsonify({"success": False, "error": "Erreur serveur"}), 500
