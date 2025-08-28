"""
🧠 BASE ALGORITHM - CLASSE MÈRE UNIVERSELLE
===========================================
Classe de base pour tous les algorithmes Revolutionary Platform
Patterns communs: scoring, validation, logging, caching

Utilisée par:
- ZScoreAlgorithm (villes/pays)
- SkillGraphAlgorithm (carrières)
- WealthAlgorithm (patrimoine)
"""

import json
import logging
from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional, Union

# Setup logging
logger = logging.getLogger(__name__)


class BaseAlgorithm(ABC):
    """Classe mère pour tous les algorithmes Revolutionary"""

    def __init__(self, service_name: str, version: str = "1.0.0"):
        self.service_name = service_name
        self.version = version
        self.criteria_count = 0
        self.last_calculation = None
        self.cache = {}

        # Critères de scoring communs à tous les algorithmes
        self.base_criteria = [
            'user_priority_1', 'user_priority_2', 'user_priority_3',
            'budget_constraints', 'timeline_flexibility', 'risk_tolerance'
        ]

        logger.info(f"✅ {service_name} Algorithm v{version} initialized")

    @abstractmethod
    def get_specific_criteria(self) -> List[str]:
        """Retourne les critères spécifiques à chaque algorithme"""
        pass

    @abstractmethod
    def calculate_score(self, data: Dict, questionnaire: Dict) -> float:
        """Calcule le score pour un élément donné"""
        pass

    @abstractmethod
    def analyze(self, questionnaire: Dict, country: str = None) -> Dict:
        """Analyse principale - Point d'entrée pour chaque service"""
        pass

    def get_all_criteria(self) -> List[str]:
        """Retourne tous les critères (base + spécifiques)"""
        return self.base_criteria + self.get_specific_criteria()

    def validate_questionnaire(self, questionnaire: Dict) -> bool:
        """Valide la structure du questionnaire"""
        if not isinstance(questionnaire, dict):
            logger.error("❌ Questionnaire must be a dictionary")
            return False

        if len(questionnaire) == 0:
            logger.error("❌ Questionnaire cannot be empty")
            return False

        logger.info(f"✅ Questionnaire validated: {len(questionnaire)} responses")
        return True

    def normalize_score(self, score: float, min_val: float = 0, max_val: float = 1) -> float:
        """Normalise un score entre min_val et max_val"""
        if score < min_val:
            return min_val
        elif score > max_val:
            return max_val
        return round(score, 3)

    def calculate_weighted_average(self, scores: List[float], weights: List[float] = None) -> float:
        """Calcule une moyenne pondérée des scores"""
        if not scores:
            return 0.0

        if weights is None:
            weights = [1.0] * len(scores)

        if len(scores) != len(weights):
            logger.warning("⚠️ Scores and weights length mismatch, using equal weights")
            weights = [1.0] * len(scores)

        total_weight = sum(weights)
        if total_weight == 0:
            return 0.0

        weighted_sum = sum(score * weight for score, weight in zip(scores, weights))
        return round(weighted_sum / total_weight, 3)

    def cache_result(self, key: str, result: Any, ttl_minutes: int = 30):
        """Cache un résultat avec TTL"""
        self.cache[key] = {
            'data': result,
            'timestamp': datetime.now(),
            'ttl_minutes': ttl_minutes
        }
        logger.debug(f"📦 Result cached for key: {key}")

    def get_cached_result(self, key: str) -> Optional[Any]:
        """Récupère un résultat du cache si valide"""
        if key not in self.cache:
            return None

        cached_item = self.cache[key]
        age_minutes = (datetime.now() - cached_item['timestamp']).total_seconds() / 60

        if age_minutes > cached_item['ttl_minutes']:
            del self.cache[key]
            logger.debug(f"🗑️ Expired cache removed for key: {key}")
            return None

        logger.debug(f"📦 Cache hit for key: {key}")
        return cached_item['data']

    def log_calculation(self, questionnaire_size: int, results_count: int, country: str = None):
        """Log les détails d'un calcul"""
        self.last_calculation = {
            'timestamp': datetime.now().isoformat(),
            'questionnaire_size': questionnaire_size,
            'results_count': results_count,
            'country': country,
            'service': self.service_name,
            'version': self.version
        }

        logger.info(f"📊 {self.service_name} calculation completed: "
                   f"{questionnaire_size} responses → {results_count} results "
                   f"({country or 'global'})")

    def get_algorithm_stats(self) -> Dict:
        """Retourne les statistiques de l'algorithme"""
        return {
            'service': self.service_name,
            'version': self.version,
            'criteria_count': len(self.get_all_criteria()),
            'cache_size': len(self.cache),
            'last_calculation': self.last_calculation,
            'base_criteria': len(self.base_criteria),
            'specific_criteria': len(self.get_specific_criteria())
        }

    def clear_cache(self):
        """Vide le cache de l'algorithme"""
        cache_size = len(self.cache)
        self.cache.clear()
        logger.info(f"🗑️ Cache cleared: {cache_size} items removed")

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(service='{self.service_name}', version='{self.version}')>"
