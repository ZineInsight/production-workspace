"""
📊 DATA LOADER - CHARGEMENT INTELLIGENT DONNÉES
===============================================
Gestionnaire centralisé pour toutes les données Revolutionary Platform
Cache, validation, optimisation performances

Données supportées:
- Villes mondiales (JSON 7000+ entries)
- Configurations pays (20+ pays)
- Templates guides dynamiques
- Bases emplois et compétences
"""

import json
import logging
from pathlib import Path
from typing import Dict, List, Any, Optional, Union
from datetime import datetime
import hashlib

# Setup logging
logger = logging.getLogger(__name__)


class DataLoader:
    """Gestionnaire intelligent de données avec cache et validation"""

    def __init__(self, data_root: Optional[Path] = None):
        # Chemin racine des données
        if data_root is None:
            data_root = Path(__file__).parent.parent / "data_v2"

        self.data_root = Path(data_root)
        self.cache = {}
        self.file_hashes = {}

        # Chemins des dossiers de données
        self.cities_dir = self.data_root / "cities"
        self.countries_dir = self.data_root / "countries"
        self.templates_dir = self.data_root / "templates"

        logger.info(f"📊 DataLoader initialized with root: {self.data_root}")

    def _calculate_file_hash(self, file_path: Path) -> str:
        """Calcule le hash MD5 d'un fichier pour détecter les changements"""
        try:
            with open(file_path, 'rb') as f:
                file_hash = hashlib.md5(f.read()).hexdigest()
            return file_hash
        except Exception as e:
            logger.error(f"❌ Error calculating file hash: {e}")
            return ""

    def _is_cache_valid(self, file_path: Path, cache_key: str) -> bool:
        """Vérifie si le cache est encore valide pour un fichier"""
        if cache_key not in self.cache:
            return False

        if cache_key not in self.file_hashes:
            return False

        # Vérifier si le fichier a changé
        current_hash = self._calculate_file_hash(file_path)
        return current_hash == self.file_hashes[cache_key]

    def _is_file_changed(self, file_path: Path) -> bool:
        """Vérifie si un fichier a changé depuis le dernier chargement"""
        current_hash = self._calculate_file_hash(file_path)
        previous_hash = self.file_hashes.get(str(file_path), "")

        if current_hash != previous_hash:
            self.file_hashes[str(file_path)] = current_hash
            return True
        return False

    def _load_json_file(self, file_path: Path, force_reload: bool = False) -> Optional[Any]:
        """Charge un fichier JSON avec cache intelligent"""
        file_path_str = str(file_path)

        # Vérifier le cache si pas de rechargement forcé
        if not force_reload and file_path_str in self.cache:
            if not self._is_file_changed(file_path):
                logger.debug(f"📦 Cache hit for {file_path.name}")
                return self.cache[file_path_str]['data']

        # Charger le fichier
        try:
            if not file_path.exists():
                logger.error(f"❌ File not found: {file_path}")
                return None

            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Mettre en cache
            self.cache[file_path_str] = {
                'data': data,
                'loaded_at': datetime.now(),
                'file_size': file_path.stat().st_size
            }

            logger.info(f"✅ Loaded {file_path.name}: {len(data) if isinstance(data, (list, dict)) else 'N/A'} items")
            return data

        except json.JSONDecodeError as e:
            logger.error(f"❌ JSON decode error in {file_path}: {e}")
            return None
        except Exception as e:
            logger.error(f"❌ Error loading {file_path}: {e}")
            return None

    def load_world_cities(self, force_reload: bool = False) -> Optional[List[Dict]]:
        """Charge les données villes mondiales"""
        # Utiliser villes_world.json qui contient les vraies données
        world_file = self.data_root / "villes_world.json"

        # Fallback vers les données existantes si pas encore migrées
        if not world_file.exists():
            fallback_path = self.data_root.parent.parent / "UNUSED_BACKUP/services/zscore/data_backup_from_skillgraph/villes_world.json"
            if fallback_path.exists():
                logger.info(f"📂 Using fallback data: {fallback_path}")
                world_file = fallback_path

        data = self._load_json_file(world_file, force_reload)
        if data:
            logger.info(f"🌍 World cities loaded: {len(data)} cities")
        return data

    def load_country_cities(self, country: str, force_reload: bool = False) -> Optional[List[Dict]]:
        """Charge les données villes d'un pays spécifique"""
        country_file = self.cities_dir / f"villes_{country}.json"

        # Fallback vers les données existantes
        if not country_file.exists():
            fallback_path = self.data_root.parent.parent / f"UNUSED_BACKUP/services/zscore/data_backup_from_skillgraph/villes_{country}.json"
            if fallback_path.exists():
                logger.info(f"📂 Using fallback data for {country}: {fallback_path}")
                country_file = fallback_path

        data = self._load_json_file(country_file, force_reload)
        if data:
            logger.info(f"🇫🇷 {country.title()} cities loaded: {len(data)} cities")
        return data

    def load_countries_config(self, force_reload: bool = False) -> Optional[Dict]:
        """Charge la configuration des pays supportés"""
        config_file = self.countries_dir / "config.json"

        # Fallback vers les données existantes
        if not config_file.exists():
            fallback_path = self.data_root.parent.parent / "UNUSED_BACKUP/services/zscore/data_backup_from_skillgraph/countries_config.json"
            if fallback_path.exists():
                logger.info(f"📂 Using fallback config: {fallback_path}")
                config_file = fallback_path

        data = self._load_json_file(config_file, force_reload)
        if data and 'supported_countries' in data:
            countries_count = len(data['supported_countries'])
            logger.info(f"🌍 Countries config loaded: {countries_count} countries")
        return data

    def load_guides_templates(self, force_reload: bool = False) -> Optional[Dict]:
        """Charge les templates pour guides dynamiques"""
        templates_file = self.templates_dir / "guides.json"

        # Fallback vers les données existantes
        if not templates_file.exists():
            fallback_path = self.data_root.parent.parent / "UNUSED_BACKUP/services/zscore/data_backup_from_skillgraph/guides_templates.json"
            if fallback_path.exists():
                logger.info(f"📂 Using fallback templates: {fallback_path}")
                templates_file = fallback_path

        data = self._load_json_file(templates_file, force_reload)
        if data:
            logger.info(f"📋 Guide templates loaded")
        return data

    def get_supported_countries(self) -> List[str]:
        """Retourne la liste des pays supportés"""
        config = self.load_countries_config()
        if config and 'supported_countries' in config:
            return list(config['supported_countries'].keys())
        return []

    def is_country_supported(self, country: str) -> bool:
        """Vérifie si un pays est supporté"""
        return country.lower() in self.get_supported_countries()

    def get_cache_stats(self) -> Dict:
        """Retourne les statistiques du cache"""
        total_items = 0
        total_size = 0

        for file_path, cache_data in self.cache.items():
            data = cache_data['data']
            if isinstance(data, (list, dict)):
                total_items += len(data)
            total_size += cache_data.get('file_size', 0)

        return {
            'cached_files': len(self.cache),
            'total_data_items': total_items,
            'total_file_size_bytes': total_size,
            'cache_memory_usage': len(str(self.cache))
        }

    def clear_cache(self):
        """Vide le cache de données"""
        cache_size = len(self.cache)
        self.cache.clear()
        self.file_hashes.clear()
        logger.info(f"🗑️ Data cache cleared: {cache_size} files removed")

    def preload_essential_data(self):
        """Précharge les données essentielles au démarrage"""
        logger.info("🚀 Preloading essential data...")

        # Charger en parallèle les données principales
        world_cities = self.load_world_cities()
        countries_config = self.load_countries_config()

        essential_countries = ['france', 'canada', 'usa', 'uk']
        for country in essential_countries:
            self.load_country_cities(country)

        logger.info(f"✅ Essential data preloaded: {len(self.cache)} files cached")
        return {
            'world_cities': len(world_cities) if world_cities else 0,
            'countries_config': bool(countries_config),
            'cached_files': len(self.cache)
        }

    def load_cities_data(self, file_name: str) -> Optional[Dict]:
        """
        Charge les données de villes depuis un fichier JSON
        Méthode wrapper pour compatibilité avec les algorithmes

        Args:
            file_name: Nom du fichier (ex: "france.json")
        """
        try:
            file_path = self.cities_dir / file_name

            if not file_path.exists():
                logger.warning(f"❌ Cities data file not found: {file_path}")
                return None

            # Utiliser le cache intelligent
            cache_key = f"cities_{file_name}"

            # Check cache
            if self._is_cache_valid(file_path, cache_key):
                logger.debug(f"📦 Using cached cities data: {file_name}")
                return self.cache[cache_key]

            # Charger depuis le fichier
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Valider la structure
            if 'cities' not in data:
                logger.warning(f"⚠️ Invalid cities data structure in {file_name}")
                return None

            # Mettre en cache
            self.cache[cache_key] = data
            self.file_hashes[cache_key] = self._calculate_file_hash(file_path)

            logger.info(f"✅ Loaded cities data: {file_name} ({len(data['cities'])} cities)")
            return data

        except Exception as e:
            logger.error(f"❌ Error loading cities data {file_name}: {e}")
            return None
