"""
💰 WEALTH SERVICE - INTELLIGENCE PATRIMONIALE RÉVOLUTIONNAIRE
=============================================================
Service de liberté financière et optimisation patrimoniale
Roadmap personnalisée vers indépendance financière complète

Features:
- Analyse gap patrimoine actuel vs objectifs liberté
- Stratégies investissement personnalisées par profil
- Timeline réaliste vers indépendance financière
- Optimisation fiscale multi-pays intelligente
"""

__version__ = "0.9.0"
__service_name__ = "wealth"
__endpoints__ = ["/api/wealth", "/api/wealth/markets", "/api/wealth/strategies"]

# Imports du service Wealth
from .algorithm import WealthAlgorithm
from .routes import wealth_bp

__all__ = ['WealthAlgorithm', 'wealth_bp']