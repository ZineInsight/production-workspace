"""
🔐 REVOLUTIONARY AUTH MODULE
===========================
Module d'authentification complet pour ZineInsight Revolutionary

Components:
- AuthManager: Gestion JWT + Redis sessions
- PaywallManager: Restrictions par tier
- Routes: Endpoints Flask authentification
- Decorators: @require_auth, @require_premium
"""

from .auth_manager import AuthManager, init_auth_manager, get_auth_manager
from .paywall_manager import PaywallManager
from .routes import auth_bp, require_auth, require_premium, init_paywall_manager

__all__ = [
    'AuthManager',
    'PaywallManager',
    'auth_bp',
    'require_auth',
    'require_premium',
    'init_auth_manager',
    'get_auth_manager',
    'init_paywall_manager'
]
