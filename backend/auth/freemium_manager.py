"""
💰 FREEMIUM MANAGER - Dashboard Paywall System
==============================================
Système intelligent de paywall pour le dashboard freemium
Gère les accès, limitations et conversions premium
"""

import logging
import json
from typing import Dict, Any, List
from datetime import datetime, timedelta
from enum import Enum

logger = logging.getLogger(__name__)

class PaywallType(Enum):
    """Types de paywalls disponibles"""
    GUIDE_UNLOCK = "guide_unlock"          # 4.99€ - Débloquer un guide spécifique
    COUNTRY_ACCESS = "country_access"      # 14.99€ - Accès complet à un pays
    UNLIMITED_ANALYSES = "unlimited"       # 9.99€/mois - Analyses illimitées
    PREMIUM_INSIGHTS = "premium_insights"  # 29.99€ - Tous les insights IA
    EXPORT_PDF = "export_pdf"             # 2.99€ - Export PDF professionnel

class FreemiumManager:
    """Gestionnaire du système freemium dashboard"""

    def __init__(self, redis_client, auth_manager):
        self.redis_client = redis_client
        self.auth_manager = auth_manager

        # Configuration des paywalls
        self.paywall_config = {
            PaywallType.GUIDE_UNLOCK.value: {
                "price": 499,  # 4.99€ en centimes
                "currency": "eur",
                "title": "🎯 Débloquer ce Guide Premium",
                "description": "Guide complet avec insights IA personnalisés",
                "features": [
                    "Guide détaillé 15+ pages",
                    "Insights IA personnalisés",
                    "Checklists pratiques",
                    "Ressources exclusives"
                ]
            },
            PaywallType.COUNTRY_ACCESS.value: {
                "price": 1499,  # 14.99€
                "currency": "eur",
                "title": "🌍 Accès Complet Pays",
                "description": "Toutes les villes + analyses illimitées",
                "features": [
                    "Toutes les villes du pays",
                    "Analyses illimitées",
                    "Comparaisons détaillées",
                    "Guides premium inclus"
                ]
            },
            PaywallType.UNLIMITED_ANALYSES.value: {
                "price": 999,  # 9.99€/mois
                "currency": "eur",
                "title": "🚀 Analyses Illimitées",
                "description": "Abonnement mensuel - Annulable",
                "features": [
                    "Analyses ZScore illimitées",
                    "Tous les algorithmes",
                    "Historique complet",
                    "Support prioritaire"
                ]
            },
            PaywallType.PREMIUM_INSIGHTS.value: {
                "price": 2999,  # 29.99€
                "currency": "eur",
                "title": "🧠 Insights IA Révolutionnaires",
                "description": "Accès complet à toute la plateforme",
                "features": [
                    "Tous les algorithmes premium",
                    "Insights IA personnalisés",
                    "Analyses prédictives",
                    "Rapports PDF illimités",
                    "Support VIP"
                ]
            },
            PaywallType.EXPORT_PDF.value: {
                "price": 299,  # 2.99€
                "currency": "eur",
                "title": "📄 Export PDF Professionnel",
                "description": "Rapport complet avec branding premium",
                "features": [
                    "Design professionnel",
                    "Logo personnalisé",
                    "Graphiques haute qualité",
                    "Format A4 optimisé"
                ]
            }
        }

        logger.info("💰 FreemiumManager initialized")

    def check_user_access(self, user_email: str, paywall_type: str, resource_id: str = None) -> Dict[str, Any]:
        """Vérifier l'accès utilisateur à une ressource"""
        try:
            # Récupérer l'utilisateur
            user_data = self.auth_manager._get_user(user_email)
            if not user_data:
                return {"has_access": False, "error": "Utilisateur introuvable"}

            user_tier = user_data.get("subscription_tier", "free")
            user_purchases = user_data.get("purchases", [])

            # Logique d'accès selon le type
            if paywall_type == PaywallType.GUIDE_UNLOCK.value:
                # Vérifier si ce guide spécifique a été acheté
                guide_key = f"guide_{resource_id}"
                has_access = any(p.get("item_id") == guide_key for p in user_purchases)

            elif paywall_type == PaywallType.COUNTRY_ACCESS.value:
                # Vérifier accès pays complet
                country_key = f"country_{resource_id}"
                has_access = (user_tier in ["premium", "pro"] or
                            any(p.get("item_id") == country_key for p in user_purchases))

            elif paywall_type == PaywallType.UNLIMITED_ANALYSES.value:
                # Vérifier abonnement actif
                has_access = user_tier in ["premium", "pro"]

            elif paywall_type == PaywallType.PREMIUM_INSIGHTS.value:
                # Accès complet premium
                has_access = user_tier == "pro"

            elif paywall_type == PaywallType.EXPORT_PDF.value:
                # Export PDF - achat ou abonnement
                has_access = (user_tier in ["premium", "pro"] or
                            any(p.get("type") == "pdf_export" for p in user_purchases))
            else:
                has_access = False

            return {
                "has_access": has_access,
                "user_tier": user_tier,
                "paywall_config": self.paywall_config.get(paywall_type, {}),
                "upgrade_suggestion": self._get_upgrade_suggestion(user_tier, paywall_type)
            }

        except Exception as e:
            logger.error(f"Access check error: {e}")
            return {"has_access": False, "error": "Erreur vérification accès"}

    def _get_upgrade_suggestion(self, current_tier: str, requested_paywall: str) -> Dict[str, Any]:
        """Suggérer la meilleure option d'upgrade"""
        suggestions = {
            "free": {
                PaywallType.GUIDE_UNLOCK.value: "Achetez ce guide pour 4.99€",
                PaywallType.COUNTRY_ACCESS.value: "Passez Premium (14.99€) pour tout le pays",
                PaywallType.UNLIMITED_ANALYSES.value: "Abonnement Premium 9.99€/mois",
                PaywallType.PREMIUM_INSIGHTS.value: "Accès Pro 29.99€ - Tout inclus"
            },
            "premium": {
                PaywallType.PREMIUM_INSIGHTS.value: "Passez Pro (29.99€) pour les insights IA"
            }
        }

        tier_suggestions = suggestions.get(current_tier, {})
        return {
            "message": tier_suggestions.get(requested_paywall, "Upgrade recommandé"),
            "show_upgrade": True
        }

    def create_paywall_session(self, user_email: str, paywall_type: str, resource_id: str = None, metadata: Dict = None) -> Dict[str, Any]:
        """Créer une session paywall pour Stripe"""
        try:
            paywall_config = self.paywall_config.get(paywall_type)
            if not paywall_config:
                return {"success": False, "error": "Type paywall invalide"}

            # Générer session data
            session_data = {
                "user_email": user_email,
                "paywall_type": paywall_type,
                "resource_id": resource_id,
                "price": paywall_config["price"],
                "currency": paywall_config["currency"],
                "title": paywall_config["title"],
                "description": paywall_config["description"],
                "features": paywall_config["features"],
                "metadata": metadata or {},
                "created_at": datetime.utcnow().isoformat(),
                "expires_at": (datetime.utcnow() + timedelta(minutes=30)).isoformat()
            }

            # Sauvegarder la session temporaire
            session_id = f"paywall_session_{user_email}_{paywall_type}_{int(datetime.utcnow().timestamp())}"
            self.redis_client.setex(
                f"paywall_session:{session_id}",
                1800,  # 30 minutes
                json.dumps(session_data)
            )

            return {
                "success": True,
                "session_id": session_id,
                "paywall_data": session_data
            }

        except Exception as e:
            logger.error(f"Paywall session creation error: {e}")
            return {"success": False, "error": "Erreur création session"}

    def process_successful_payment(self, session_id: str, stripe_payment_data: Dict) -> Dict[str, Any]:
        """Traiter un paiement réussi et débloquer l'accès"""
        try:
            # Récupérer la session paywall
            session_data = self.redis_client.get(f"paywall_session:{session_id}")
            if not session_data:
                return {"success": False, "error": "Session expirée"}

            import json
            session_info = json.loads(session_data)
            user_email = session_info["user_email"]
            paywall_type = session_info["paywall_type"]
            resource_id = session_info.get("resource_id")

            # Récupérer l'utilisateur
            user_data = self.auth_manager._get_user(user_email)
            if not user_data:
                return {"success": False, "error": "Utilisateur introuvable"}

            # Ajouter l'achat aux données utilisateur
            if "purchases" not in user_data:
                user_data["purchases"] = []

            purchase_record = {
                "id": f"purchase_{int(datetime.utcnow().timestamp())}",
                "paywall_type": paywall_type,
                "item_id": f"{paywall_type}_{resource_id}" if resource_id else paywall_type,
                "price_paid": stripe_payment_data.get("amount_received", 0),
                "currency": stripe_payment_data.get("currency", "eur"),
                "stripe_payment_id": stripe_payment_data.get("payment_intent_id"),
                "purchased_at": datetime.utcnow().isoformat(),
                "expires_at": None  # Permanent sauf abonnements
            }

            user_data["purchases"].append(purchase_record)

            # Upgrade automatique si applicable
            if paywall_type == PaywallType.UNLIMITED_ANALYSES.value:
                user_data["subscription_tier"] = "premium"
                purchase_record["expires_at"] = (datetime.utcnow() + timedelta(days=30)).isoformat()
            elif paywall_type == PaywallType.PREMIUM_INSIGHTS.value:
                user_data["subscription_tier"] = "pro"

            # Sauvegarder les modifications
            self.auth_manager.redis_client.set(
                f"user:{user_email.lower()}",
                json.dumps(user_data)
            )

            # Nettoyer la session temporaire
            self.redis_client.delete(f"paywall_session:{session_id}")

            logger.info(f"✅ Payment processed: {user_email} bought {paywall_type}")

            return {
                "success": True,
                "purchase_id": purchase_record["id"],
                "new_tier": user_data.get("subscription_tier", "free"),
                "access_unlocked": True
            }

        except Exception as e:
            logger.error(f"Payment processing error: {e}")
            return {"success": False, "error": "Erreur traitement paiement"}

    def get_dashboard_limitations(self, user_email: str) -> Dict[str, Any]:
        """Récupérer les limitations dashboard pour un utilisateur"""
        try:
            user_data = self.auth_manager._get_user(user_email)
            if not user_data:
                return {"error": "Utilisateur introuvable"}

            user_tier = user_data.get("subscription_tier", "free")
            user_purchases = user_data.get("purchases", [])

            limitations = {
                "free": {
                    "analyses_remaining": 1,
                    "countries_accessible": ["france"],  # Exemple avec France gratuit
                    "guides_unlocked": [],
                    "pdf_exports": 0,
                    "insights_ai": False,
                    "show_upgrade_cta": True
                },
                "premium": {
                    "analyses_remaining": -1,  # Illimité
                    "countries_accessible": "all",
                    "guides_unlocked": "purchased_only",
                    "pdf_exports": 10,
                    "insights_ai": False,
                    "show_upgrade_cta": True  # Vers Pro
                },
                "pro": {
                    "analyses_remaining": -1,
                    "countries_accessible": "all",
                    "guides_unlocked": "all",
                    "pdf_exports": -1,
                    "insights_ai": True,
                    "show_upgrade_cta": False
                }
            }

            user_limits = limitations.get(user_tier, limitations["free"])

            # Ajouter les achats spécifiques
            purchased_guides = [p.get("item_id") for p in user_purchases if p.get("paywall_type") == PaywallType.GUIDE_UNLOCK.value]
            purchased_countries = [p.get("item_id") for p in user_purchases if p.get("paywall_type") == PaywallType.COUNTRY_ACCESS.value]

            user_limits["purchased_guides"] = purchased_guides
            user_limits["purchased_countries"] = purchased_countries

            return {
                "success": True,
                "user_tier": user_tier,
                "limitations": user_limits,
                "paywall_options": list(self.paywall_config.keys())
            }

        except Exception as e:
            logger.error(f"Dashboard limitations error: {e}")
            return {"error": "Erreur récupération limitations"}
