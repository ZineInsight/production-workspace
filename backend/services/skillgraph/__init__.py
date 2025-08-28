"""
💼 SKILLGRAPH SERVICE - INTELLIGENCE CARRIÈRE
=============================================
Service d'optimisation carrière et développement compétences
Recommandations emplois/formations basées sur profil et objectifs

Features:
- Matching intelligent emplois/compétences
- Analyse gaps compétences et formations
- Recommandations salaires et évolution
- Intégration bases emplois internationales
"""

__version__ = "1.0.0"
__service_name__ = "skillgraph"
__endpoints__ = ["/api/career", "/api/sectors", "/api/markets"]

# Imports du service SkillGraph
from .algorithm import SkillGraphAlgorithm
from .routes import skillgraph_bp

__all__ = ['SkillGraphAlgorithm', 'skillgraph_bp']