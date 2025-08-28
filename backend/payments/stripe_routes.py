"""
💳 STRIPE INTEGRATION - Revolutionary Payment System
===================================================
Intégration Stripe complète pour les paywalls freemium
Endpoints sécurisés pour checkout, webhooks et vérifications
"""

import logging
import os
import sys
import subprocess
import tempfile
import json
from flask import Blueprint, request, jsonify
from datetime import datetime
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv('/var/www/Revolutionnary/.env')

# Import Stripe via subprocess pour éviter les conflits avec platform/
def import_stripe_safely():
    """Importer Stripe en évitant les conflits de module platform"""
    try:
        # Changer temporairement de répertoire pour éviter le conflit
        old_cwd = os.getcwd()
        os.chdir('/tmp')

        # Vérifier si stripe est installé
        result = subprocess.run([sys.executable, '-c', 'import stripe; print("OK")'],
                               capture_output=True, text=True, cwd='/tmp')

        os.chdir(old_cwd)
        return result.returncode == 0
    except Exception as e:
        print(f"Erreur lors de la vérification de Stripe: {e}")
        return False

STRIPE_AVAILABLE = import_stripe_safely()

logger = logging.getLogger(__name__)

# Blueprint payments
payments_bp = Blueprint('payments', __name__, url_prefix='/api/payments')

# Configuration Stripe
stripe.api_key = os.environ.get('STRIPE_SECRET_KEY', 'sk_test_...')  # À remplacer
STRIPE_PUBLIC_KEY = os.environ.get('STRIPE_PUBLIC_KEY', 'pk_test_...')  # À remplacer
STRIPE_WEBHOOK_SECRET = os.environ.get('STRIPE_WEBHOOK_SECRET', '')

# Configuration des prix Stripe (Price IDs à créer sur Stripe Dashboard)
STRIPE_PRICES = {
    'guide_unlock': 'price_guide_unlock_499',       # 4.99€
    'country_access': 'price_country_access_1499',  # 14.99€
    'unlimited': 'price_unlimited_999',              # 9.99€/mois
    'premium_insights': 'price_premium_2999',       # 29.99€
    'export_pdf': 'price_export_pdf_299'            # 2.99€
}

@payments_bp.route('/config', methods=['GET'])
def get_stripe_config():
    """Récupérer la configuration publique Stripe"""
    return jsonify({
        "public_key": STRIPE_PUBLIC_KEY,
        "success": True
    })

@payments_bp.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    """Créer une session Stripe Checkout pour un paywall"""
    try:
        data = request.get_json()

        paywall_type = data.get('paywall_type')
        resource_id = data.get('resource_id', '')
        user_email = data.get('user_email', '')
        session_id = data.get('session_id', '')

        if not paywall_type or paywall_type not in STRIPE_PRICES:
            return jsonify({"error": "Type paywall invalide"}), 400

        # Récupérer le Price ID Stripe
        price_id = STRIPE_PRICES[paywall_type]

        # Métadonnées pour traçabilité
        metadata = {
            'paywall_type': paywall_type,
            'resource_id': resource_id,
            'user_email': user_email,
            'session_id': session_id,
            'created_at': datetime.utcnow().isoformat()
        }

        # Créer la session Checkout
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': price_id,
                'quantity': 1,
            }],
            mode='payment' if paywall_type != 'unlimited' else 'subscription',
            success_url=f"{request.host_url}dashboard?payment=success&session_id={{CHECKOUT_SESSION_ID}}",
            cancel_url=f"{request.host_url}dashboard?payment=cancelled",
            customer_email=user_email if user_email else None,
            metadata=metadata,
            allow_promotion_codes=True,  # Codes promo
            billing_address_collection='required',
        )

        logger.info(f"✅ Stripe session created: {checkout_session.id} for {paywall_type}")

        return jsonify({
            "success": True,
            "checkout_url": checkout_session.url,
            "session_id": checkout_session.id
        })

    except stripe.error.StripeError as e:
        logger.error(f"❌ Stripe error: {e}")
        return jsonify({"error": "Erreur paiement Stripe"}), 500
    except Exception as e:
        logger.error(f"❌ Payment session error: {e}")
        return jsonify({"error": "Erreur serveur"}), 500

@payments_bp.route('/create-payment-intent', methods=['POST'])
def create_payment_intent():
    """Créer un Payment Intent pour paiement inline"""
    try:
        data = request.get_json()

        paywall_type = data.get('paywall_type')
        amount = data.get('amount')  # En centimes
        currency = data.get('currency', 'eur')
        user_email = data.get('user_email', '')

        if not amount or amount < 50:  # Minimum Stripe
            return jsonify({"error": "Montant invalide"}), 400

        # Métadonnées
        metadata = {
            'paywall_type': paywall_type,
            'user_email': user_email,
            'created_at': datetime.utcnow().isoformat()
        }

        # Créer le Payment Intent
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            metadata=metadata,
            receipt_email=user_email if user_email else None
        )

        logger.info(f"✅ Payment Intent created: {intent.id}")

        return jsonify({
            "success": True,
            "client_secret": intent.client_secret,
            "payment_intent_id": intent.id
        })

    except stripe.error.StripeError as e:
        logger.error(f"❌ Stripe error: {e}")
        return jsonify({"error": "Erreur création Payment Intent"}), 500
    except Exception as e:
        logger.error(f"❌ Payment Intent error: {e}")
        return jsonify({"error": "Erreur serveur"}), 500

@payments_bp.route('/verify-payment', methods=['POST'])
def verify_payment():
    """Vérifier le statut d'un paiement"""
    try:
        data = request.get_json()
        session_id = data.get('session_id')

        if not session_id:
            return jsonify({"error": "Session ID requis"}), 400

        # Récupérer la session Stripe
        session = stripe.checkout.Session.retrieve(session_id)

        return jsonify({
            "success": True,
            "payment_status": session.payment_status,
            "session_status": session.status,
            "metadata": session.metadata
        })

    except stripe.error.StripeError as e:
        logger.error(f"❌ Stripe verification error: {e}")
        return jsonify({"error": "Erreur vérification"}), 500
    except Exception as e:
        logger.error(f"❌ Verification error: {e}")
        return jsonify({"error": "Erreur serveur"}), 500

@payments_bp.route('/webhook', methods=['POST'])
def stripe_webhook():
    """Webhook Stripe pour traiter les événements de paiement"""
    try:
        payload = request.get_data(as_text=True)
        sig_header = request.headers.get('Stripe-Signature')

        # Vérifier la signature webhook
        event = stripe.Webhook.construct_event(
            payload, sig_header, STRIPE_WEBHOOK_SECRET
        )

        logger.info(f"📥 Stripe webhook event: {event['type']}")

        # Traiter l'événement
        if event['type'] == 'checkout.session.completed':
            session = event['data']['object']
            handle_successful_payment(session)

        elif event['type'] == 'payment_intent.succeeded':
            payment_intent = event['data']['object']
            handle_payment_intent_success(payment_intent)

        elif event['type'] == 'invoice.payment_succeeded':
            # Pour les abonnements
            invoice = event['data']['object']
            handle_subscription_payment(invoice)

        return jsonify({"success": True})

    except ValueError as e:
        logger.error(f"❌ Invalid payload: {e}")
        return jsonify({"error": "Invalid payload"}), 400
    except stripe.error.SignatureVerificationError as e:
        logger.error(f"❌ Invalid signature: {e}")
        return jsonify({"error": "Invalid signature"}), 400
    except Exception as e:
        logger.error(f"❌ Webhook error: {e}")
        return jsonify({"error": "Webhook error"}), 500

def handle_successful_payment(session):
    """Traiter un paiement réussi"""
    try:
        # Import local pour éviter les dépendances circulaires
        from platform.backend.auth.freemium_manager import FreemiumManager
        from platform.backend.auth.auth_manager import get_auth_manager

        # Initialiser freemium_manager
        auth_manager = get_auth_manager()
        freemium_manager = FreemiumManager(auth_manager.redis_client, auth_manager)

        metadata = session.get('metadata', {})
        user_email = metadata.get('user_email')
        paywall_session_id = metadata.get('session_id')

        if user_email and paywall_session_id:
            # Préparer les données de paiement
            stripe_data = {
                'payment_intent_id': session.get('payment_intent'),
                'amount_received': session.get('amount_total', 0),
                'currency': session.get('currency', 'eur'),
                'status': 'succeeded'
            }

            # Traiter via FreemiumManager
            result = freemium_manager.process_successful_payment(
                paywall_session_id,
                stripe_data
            )

            if result.get('success'):
                logger.info(f"✅ Payment processed successfully for {user_email}")
            else:
                logger.error(f"❌ Failed to process payment: {result.get('error')}")

    except Exception as e:
        logger.error(f"❌ Payment handling error: {e}")

def handle_payment_intent_success(payment_intent):
    """Traiter un Payment Intent réussi"""
    try:
        metadata = payment_intent.get('metadata', {})
        user_email = metadata.get('user_email')

        logger.info(f"✅ Payment Intent succeeded for {user_email}: {payment_intent.id}")
        # Logique similaire selon tes besoins

    except Exception as e:
        logger.error(f"❌ Payment Intent handling error: {e}")

def handle_subscription_payment(invoice):
    """Traiter un paiement d'abonnement"""
    try:
        customer_email = invoice.get('customer_email')
        subscription_id = invoice.get('subscription')

        logger.info(f"✅ Subscription payment for {customer_email}: {subscription_id}")
        # Logique de renouvellement d'abonnement

    except Exception as e:
        logger.error(f"❌ Subscription handling error: {e}")
