"""
🎯 REVOLUTIONARY BACKEND - MAIN PACKAGE
======================================
Backend unifié pour ZineInsight Revolutionary Platform
- ZScore: Analyse villes/pays optimales
- SkillGraph: Optimisation carrières/compétences
- WealthMonitor: Gestion patrimoine intelligent

Architecture modulaire et évolutive
"""

__version__ = "1.0.0"
__author__ = "Revolutionary Platform Team"

# Services disponibles
SERVICES = [
    "zscore",      # Analyse villes/pays
    "skillgraph",  # Carrières/compétences
    "wealth"       # Patrimoine/finance
]

# Configuration par défaut
DEFAULT_CONFIG = {
    "debug": False,
    "port": 8000,
    "cors_enabled": True,
    "stripe_enabled": True,
    "session_enabled": True
}
