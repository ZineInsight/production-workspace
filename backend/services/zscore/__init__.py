"""
🏙️ ZSCORE SERVICE RÉVOLUTIONNAIRE - INTELLIGENCE GÉOGRAPHIQUE AVANCÉE
====================================================================
Service d'analyse sophistiqué avec TOP 3 villes personnalisées
Basé sur 50+ critères ultra-personnalisés selon profil utilisateur

Features Révolutionnaires:
- Algorithme scoring multi-critères avancé
- Support 19 pays et +300 villes avec données enrichies
- TOP 3 vraiment diversifié avec explications personnalisées
- Pénalités anti-monopole et amplification contrastes
- Intégration Stripe pour premium
"""

__version__ = "2.1.0-revolutionary"
__service_name__ = "zscore"
__endpoints__ = ["/api/calculate", "/api/countries", "/api/stats"]

# Imports du service ZScore Révolutionnaire
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from algorithms_historical.algo_expat import AlgorithmeExpat as ZScoreAlgorithm
from .routes import zscore_bp

__all__ = ['ZScoreAlgorithm', 'zscore_bp']
