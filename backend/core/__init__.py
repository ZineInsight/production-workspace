"""
🧠 CORE SERVICES - REVOLUTIONARY BACKEND
========================================
Services partagés et classes de base pour tous les modules
- BaseAlgorithm: Classe mère pour tous les algorithmes
- DataLoader: Chargement intelligent des données
- SecurityMiddleware: Sécurité production centralisée
"""

from .base_algorithm import BaseAlgorithm
from .data_loader import DataLoader
from .security_middleware import SecurityMiddleware

__all__ = [
    'BaseAlgorithm',
    'DataLoader',
    'SecurityMiddleware'
]

# Version des composants core
__version__ = "1.0.0"

# Validation import
import logging
logger = logging.getLogger(__name__)
logger.info("✅ Core services imported successfully")
