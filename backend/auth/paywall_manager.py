"""
💰 REVOLUTIONARY PAYWALL MANAGER
===============================
Gestion des restrictions et limites d'usage par tier d'abonnement

Tiers d'abonnement:
- FREE: 1 analyse/mois par service, pas de dashboard
- PREMIUM (29€/mois): Illimité + dashboard + historique
- PRO (79€/mois): Premium + API + white-label

Features:
- Vérification limites d'usage en temps réel
- Reset automatique mensuel
- Tracking précis par service
- Upgrade seamless
"""

import json
import redis
import logging
from datetime import datetime, timedelta
from typing import Dict, Any, Tuple, Optional

logger = logging.getLogger(__name__)

class PaywallManager:
    """Gestionnaire principal du paywall et des restrictions"""

    def __init__(self, redis_client=None):
        self.redis_client = redis_client or redis.Redis(host='localhost', port=6379, decode_responses=True)

        # Configuration des tiers d'abonnement
        self.tiers_config = {
            'free': {
                'zscore_analyses': 1,      # 1 par mois
                'skillgraph_scans': 1,     # 1 par mois
                'wealth_portfolios': 0,    # 0 en free
                'dashboard_access': False, # Pas d'accès dashboard
                'api_access': False,       # Pas d'API
                'export_pdf': False,       # Pas d'export
                'historical_data': False,  # Pas d'historique
                'support_priority': False  # Support standard
            },
            'premium': {
                'zscore_analyses': -1,     # Illimité (-1)
                'skillgraph_scans': -1,    # Illimité
                'wealth_portfolios': -1,   # Illimité
                'dashboard_access': True,  # Accès complet dashboard
                'api_access': False,       # Pas d'API (réservé PRO)
                'export_pdf': True,        # Export PDF
                'historical_data': True,   # Historique 12 mois
                'support_priority': True   # Support prioritaire
            },
            'pro': {
                'zscore_analyses': -1,     # Illimité
                'skillgraph_scans': -1,    # Illimité
                'wealth_portfolios': -1,   # Illimité
                'dashboard_access': True,  # Accès complet dashboard
                'api_access': True,        # API access complet
                'export_pdf': True,        # Export PDF + CSV + JSON
                'historical_data': True,   # Historique illimité
                'support_priority': True,  # Support VIP
                'white_label': True        # White-label
            }
        }

        logger.info("💰 PaywallManager initialized with 3 tiers")

    def check_usage_limit(self, user_email: str, service: str) -> Tuple[bool, int, int]:
        """
        Vérifier si l'utilisateur peut utiliser un service

        Returns:
            (can_use: bool, remaining: int, limit: int)
        """
        try:
            # Récupérer l'utilisateur
            user_data = self._get_user_data(user_email)
            if not user_data:
                return False, 0, 0

            tier = user_data.get('subscription_tier', 'free')
            limits = user_data.get('usage_limits', {})
            current_usage = user_data.get('usage_current', {})

            # Vérifier si le reset mensuel est nécessaire
            self._check_monthly_reset(user_email, user_data)

            # Récupérer la limite pour ce service
            service_limit = limits.get(f'{service}_analyses') or limits.get(f'{service}_scans') or limits.get(f'{service}_portfolios', 0)

            # Si limite = -1, c'est illimité (premium/pro)
            if service_limit == -1:
                return True, -1, -1

            # Vérifier l'usage actuel
            current_count = current_usage.get(f'{service}_analyses') or current_usage.get(f'{service}_scans') or current_usage.get(f'{service}_portfolios', 0)

            can_use = current_count < service_limit
            remaining = max(0, service_limit - current_count)

            logger.info(f"💰 Usage check for {user_email} - {service}: {current_count}/{service_limit} (can_use: {can_use})")

            return can_use, remaining, service_limit

        except Exception as e:
            logger.error(f"Usage limit check error: {e}")
            return False, 0, 0

    def increment_usage(self, user_email: str, service: str) -> bool:
        """
        Incrémenter l'usage d'un service

        Returns:
            success: bool
        """
        try:
            # Vérifier d'abord si l'usage est autorisé
            can_use, remaining, limit = self.check_usage_limit(user_email, service)

            if not can_use and limit != -1:  # -1 = illimité
                logger.warning(f"💰 Usage limit reached for {user_email} - {service}")
                return False

            # Récupérer et mettre à jour les données utilisateur
            user_data = self._get_user_data(user_email)
            if not user_data:
                return False

            current_usage = user_data.get('usage_current', {})

            # Déterminer la clé d'usage selon le service
            usage_key = f'{service}_analyses'
            if service == 'skillgraph':
                usage_key = f'{service}_scans'
            elif service == 'wealth':
                usage_key = f'{service}_portfolios'

            # Incrémenter
            current_usage[usage_key] = current_usage.get(usage_key, 0) + 1
            user_data['usage_current'] = current_usage

            # Sauvegarder dans Redis
            self.redis_client.setex(
                f"user:{user_email}",
                3600 * 24 * 7,  # 7 jours
                json.dumps(user_data)
            )

            logger.info(f"💰 Usage incremented for {user_email} - {service}: {current_usage[usage_key]}")
            return True

        except Exception as e:
            logger.error(f"Usage increment error: {e}")
            return False

    def check_feature_access(self, user_email: str, feature: str) -> bool:
        """
        Vérifier l'accès à une fonctionnalité

        Features: dashboard_access, api_access, export_pdf, historical_data, etc.
        """
        try:
            user_data = self._get_user_data(user_email)
            if not user_data:
                return False

            tier = user_data.get('subscription_tier', 'free')
            tier_config = self.tiers_config.get(tier, self.tiers_config['free'])

            has_access = tier_config.get(feature, False)

            logger.info(f"💰 Feature access check for {user_email} - {feature}: {has_access} (tier: {tier})")
            return has_access

        except Exception as e:
            logger.error(f"Feature access check error: {e}")
            return False

    def upgrade_user_tier(self, user_email: str, new_tier: str) -> bool:
        """
        Upgrader le tier d'un utilisateur
        """
        try:
            if new_tier not in self.tiers_config:
                logger.error(f"Invalid tier: {new_tier}")
                return False

            user_data = self._get_user_data(user_email)
            if not user_data:
                return False

            old_tier = user_data.get('subscription_tier', 'free')

            # Mettre à jour le tier et les limites
            user_data['subscription_tier'] = new_tier
            user_data['usage_limits'] = self.tiers_config[new_tier].copy()
            user_data['upgraded_at'] = datetime.utcnow().isoformat()
            user_data['previous_tier'] = old_tier

            # Sauvegarder
            self.redis_client.setex(
                f"user:{user_email}",
                3600 * 24 * 7,
                json.dumps(user_data)
            )

            logger.info(f"💰 User tier upgraded: {user_email} from {old_tier} to {new_tier}")
            return True

        except Exception as e:
            logger.error(f"User tier upgrade error: {e}")
            return False

    def get_upgrade_recommendations(self, user_email: str) -> Dict[str, Any]:
        """
        Obtenir des recommandations d'upgrade basées sur l'usage
        """
        try:
            user_data = self._get_user_data(user_email)
            if not user_data:
                return {}

            tier = user_data.get('subscription_tier', 'free')
            current_usage = user_data.get('usage_current', {})
            limits = user_data.get('usage_limits', {})

            recommendations = {
                'current_tier': tier,
                'should_upgrade': False,
                'blocked_features': [],
                'usage_pressure': {},
                'recommended_tier': None,
                'savings_potential': 0
            }

            # Calculer la pression d'usage
            for service in ['zscore', 'skillgraph', 'wealth']:
                for action in ['analyses', 'scans', 'portfolios']:
                    key = f'{service}_{action}'
                    if key in current_usage and key in limits:
                        limit = limits[key]
                        usage = current_usage[key]

                        if limit > 0:  # Pas illimité
                            pressure = usage / limit
                            recommendations['usage_pressure'][key] = {
                                'usage': usage,
                                'limit': limit,
                                'pressure': pressure,
                                'blocked': pressure >= 1.0
                            }

                            if pressure >= 0.8:  # 80% de la limite
                                recommendations['should_upgrade'] = True

            # Recommandations de tier
            if tier == 'free' and recommendations['should_upgrade']:
                recommendations['recommended_tier'] = 'premium'
                recommendations['savings_potential'] = 29  # €/mois
            elif tier == 'premium' and any(p.get('blocked', False) for p in recommendations['usage_pressure'].values()):
                recommendations['recommended_tier'] = 'pro'
                recommendations['savings_potential'] = 50  # €/mois de différence

            return recommendations

        except Exception as e:
            logger.error(f"Upgrade recommendations error: {e}")
            return {}

    def get_pricing_info(self) -> Dict[str, Any]:
        """Récupérer les informations de tarification"""
        return {
            'tiers': {
                'free': {
                    'name': 'Gratuit',
                    'price': 0,
                    'period': 'mois',
                    'features': [
                        '1 analyse ZScore/mois',
                        '1 scan SkillGraph/mois',
                        'Support communauté',
                        'Données de base'
                    ],
                    'limitations': [
                        'Pas d\'accès dashboard',
                        'Pas de Wealth analysis',
                        'Pas d\'historique',
                        'Pas d\'export'
                    ]
                },
                'premium': {
                    'name': 'Premium',
                    'price': 29,
                    'period': 'mois',
                    'features': [
                        'Analyses illimitées',
                        'Dashboard complet',
                        'Historique 12 mois',
                        'Export PDF/CSV',
                        'Support prioritaire',
                        'Wealth analysis'
                    ],
                    'popular': True
                },
                'pro': {
                    'name': 'Professionnel',
                    'price': 79,
                    'period': 'mois',
                    'features': [
                        'Tout Premium +',
                        'Accès API complet',
                        'White-label',
                        'Historique illimité',
                        'Support VIP',
                        'Intégrations custom'
                    ]
                }
            },
            'contact_sales': {
                'enterprise': 'Pour les besoins enterprise, contactez-nous',
                'email': 'sales@zineinsight.com'
            }
        }

    def _get_user_data(self, user_email: str) -> Optional[Dict[str, Any]]:
        """Récupérer les données utilisateur depuis Redis"""
        try:
            user_json = self.redis_client.get(f"user:{user_email}")
            return json.loads(user_json) if user_json else None
        except Exception as e:
            logger.error(f"Failed to get user data: {e}")
            return None

    def _check_monthly_reset(self, user_email: str, user_data: Dict[str, Any]) -> bool:
        """Vérifier et effectuer le reset mensuel si nécessaire"""
        try:
            current_usage = user_data.get('usage_current', {})
            last_reset = current_usage.get('last_reset')

            if not last_reset:
                # Premier reset
                current_usage['last_reset'] = datetime.utcnow().replace(day=1).isoformat()
                return False

            last_reset_date = datetime.fromisoformat(last_reset)
            current_month_start = datetime.utcnow().replace(day=1, hour=0, minute=0, second=0, microsecond=0)

            if last_reset_date < current_month_start:
                # Reset nécessaire
                logger.info(f"💰 Monthly usage reset for {user_email}")

                # Reset des compteurs
                for key in list(current_usage.keys()):
                    if key.endswith(('_analyses', '_scans', '_portfolios')):
                        current_usage[key] = 0

                current_usage['last_reset'] = current_month_start.isoformat()
                user_data['usage_current'] = current_usage

                # Sauvegarder
                self.redis_client.setex(
                    f"user:{user_email}",
                    3600 * 24 * 7,
                    json.dumps(user_data)
                )

                return True

            return False

        except Exception as e:
            logger.error(f"Monthly reset check error: {e}")
            return False

    def get_usage_analytics(self, user_email: str) -> Dict[str, Any]:
        """Obtenir les analytics d'usage pour un utilisateur"""
        try:
            user_data = self._get_user_data(user_email)
            if not user_data:
                return {}

            tier = user_data.get('subscription_tier', 'free')
            current_usage = user_data.get('usage_current', {})
            limits = user_data.get('usage_limits', {})

            analytics = {
                'tier': tier,
                'services': {},
                'monthly_summary': {
                    'total_requests': 0,
                    'remaining_requests': 0,
                    'utilization_rate': 0.0
                },
                'recommendations': self.get_upgrade_recommendations(user_email)
            }

            # Analytics par service
            services = ['zscore', 'skillgraph', 'wealth']
            for service in services:
                service_data = {
                    'usage': 0,
                    'limit': 0,
                    'remaining': 0,
                    'utilization_rate': 0.0,
                    'status': 'available'
                }

                # Trouver la bonne clé d'usage
                for suffix in ['analyses', 'scans', 'portfolios']:
                    key = f'{service}_{suffix}'
                    if key in current_usage or key in limits:
                        service_data['usage'] = current_usage.get(key, 0)
                        service_data['limit'] = limits.get(key, 0)

                        if service_data['limit'] == -1:  # Illimité
                            service_data['remaining'] = -1
                            service_data['utilization_rate'] = 0.0
                            service_data['status'] = 'unlimited'
                        else:
                            service_data['remaining'] = max(0, service_data['limit'] - service_data['usage'])
                            if service_data['limit'] > 0:
                                service_data['utilization_rate'] = service_data['usage'] / service_data['limit']

                            if service_data['remaining'] == 0:
                                service_data['status'] = 'exhausted'
                            elif service_data['utilization_rate'] >= 0.8:
                                service_data['status'] = 'warning'

                        break

                analytics['services'][service] = service_data

                # Ajouter au résumé mensuel
                if service_data['limit'] != -1:
                    analytics['monthly_summary']['total_requests'] += service_data['usage']
                    analytics['monthly_summary']['remaining_requests'] += service_data['remaining']

            # Calculer le taux d'utilisation global
            total_possible = sum(s['limit'] for s in analytics['services'].values() if s['limit'] > 0)
            if total_possible > 0:
                analytics['monthly_summary']['utilization_rate'] = analytics['monthly_summary']['total_requests'] / total_possible

            return analytics

        except Exception as e:
            logger.error(f"Usage analytics error: {e}")
            return {}
