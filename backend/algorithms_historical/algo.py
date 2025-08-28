"""
🚀 ALGORITHME DE SCORING PURIFIÉ - DIVERSITÉ MAXIMALE
====================================================

PHILOSOPHIE: Chaque utilisateur obtient des recommandations VRAIMENT personnalisées
OBJECTIF: Même avec des critères similaires, les recommandations sont diversifiées

INNOVATION:
- Scoring basé uniquement sur les priorités utilisateur
- Aucun biais de "villes favorites" prédéfinies
- Amplification intelligente des priorités mentionnées
- Maximum de diversité dans les recommandations

Créé: Août 2025 - Approche pure sans profils
"""

import json
import math
from pathlib import Path
from typing import Dict, List, Tuple

class AlgorithmeRevolutionnaire:
    """Algorithme de recommandation ultra-personnalisé"""

    def __init__(self, workspace_root: str = "/var/www/zscore"):
        self.workspace_root = Path(workspace_root)
        self.data_dir = self.workspace_root / "essentiels" / "data"

        # 🌍 PAYS DISPONIBLES
        self.countries = {
            'france': 'france/villes_france_universal.json',
            'world': 'world/villes_world.json',
            'usa': 'usa/villes_usa.json',
            'canada': 'canada/villes_canada.json',
            'uk': 'uk/villes_uk.json',
            'australia': 'australia/villes_australia.json',
            'spain': 'spain/villes_spain.json',
            'italy': 'italy/villes_italy.json',
            'germany': 'germany/villes_germany.json',
            'mexico': 'mexico/villes_mexico.json',
            'brazil': 'brazil/villes_brazil.json',
            'argentina': 'argentina/villes_argentina.json',
            'japan': 'japan/villes_japan.json',
            'thailand': 'thailand/villes_thailand.json',
            'maroc': 'maroc/villes_maroc_universal.json',
            'south_africa': 'south_africa/villes_south_africa.json',
            'egypt': 'egypt/villes_egypt.json',
            'nigeria': 'nigeria/villes_nigeria.json',
            'kenya': 'kenya/villes_kenya.json'
        }

        # 🎯 MAPPING INTELLIGENT - Questionnaire vers données
        self.mapping = {
            'cost_of_living': ['ratio_salaire_loyer', 'cout_installation'],
            'safety': ['securite_publique', 'stabilite_juridique'],
            'job_market': ['emploi_accessible', 'reseau_business'],
            'infrastructure': ['infrastructure_premium', 'transport_economique'],
            'education': ['ecoles_internationales', 'ecoles_publiques_qualite'],
            'healthcare': ['soins_accessibles'],
            'culture': ['culture_loisirs', 'scene_culturelle'],
            'climate': ['climat_agreable'],
            'environment': ['qualite_air', 'energie_verte'],
            'housing': ['cout_installation', 'logement_familial'],
            'transport': ['transport_economique', 'mobilite_verte'],
            'business': ['reseau_business', 'services_bancaires'],
            'lifestyle': ['services_luxe', 'gastronomie_qualite'],
            'innovation': ['scene_startup', 'ecosysteme_innovation'],
            'diversity': ['tolerance_diversite']
        }

        print(f"🚀 Algorithme Révolutionnaire initialisé - {len(self.countries)} pays")

    def analyser(self, questionnaire: Dict, country: str = "world") -> Dict:
        """
        🎯 ANALYSE RÉVOLUTIONNAIRE - SCORING PUR

        Étapes:
        1. Charger données villes
        2. Calcul poids selon priorités utilisateur
        3. Scoring basé uniquement sur critères réels
        4. Anti-monopole (diversité des résultats)
        5. Amplification contrastes
        """
        # 1. Charger données
        cities_data = self._load_country_data(country)
        if not cities_data:
            return {"error": f"Pays '{country}' non trouvé", "recommendations": []}

        # 2. Calcul poids selon priorités utilisateur
        weights = self._calculer_poids_personnalises(questionnaire)

        # 3. Scoring pur basé sur critères
        scored_cities = []
        for city in cities_data:
            # Score de base uniquement
            score_base = self._calculer_score_base(city, weights)

            # Pénalité anti-monopole (pour diversité)
            penalite_monopole = self._penalite_monopole(city)

            # Score final = critères purs
            score_final = score_base - penalite_monopole

            scored_cities.append({
                **city,
                "score": round(max(0, min(100, score_final * 100)), 1),
                "score_base": round(score_base * 100, 1)
                # Garde le country original de chaque ville du dataset
            })

        # 4. Tri et amplification des contrastes
        scored_cities = self._amplifier_contrastes(scored_cities)
        scored_cities.sort(key=lambda x: x["score"], reverse=True)

        # 5. 🌟 NOUVELLE LOGIQUE : Génération du top 5 diversifié
        diversified_recommendations = self._generate_diversified_top5(scored_cities, questionnaire, country)

        # 6. Statistiques de diversité
        diversity_summary = {
            'big_cities': len([c for c in diversified_recommendations if c.get('size_category') == 'big_city']),
            'medium_cities': len([c for c in diversified_recommendations if c.get('size_category') == 'medium_city']),
            'small_cities': len([c for c in diversified_recommendations if c.get('size_category') == 'small_city']),
            'total_analyzed': len(scored_cities)
        }

        return {
            "country": country,
            "total_cities": len(scored_cities),
            "algorithme": "scoring_diversifie_v2",
            "recommendations": diversified_recommendations,
            "diversity_summary": diversity_summary,
            "all_cities": scored_cities  # Garde toutes les villes pour debug si besoin
        }

    def _load_country_data(self, country: str) -> List[Dict]:
        """Charge données pays"""
        print(f"🔍 _load_country_data appelé avec country='{country}'")
        print(f"🔍 Pays disponibles: {list(self.countries.keys())}")

        if country not in self.countries:
            print(f"❌ Pays '{country}' non trouvé dans self.countries")
            return []

        file_path = self.data_dir / self.countries[country]
        print(f"🔍 Chemin fichier: {file_path}")

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                cities = data.get('cities', [])
                print(f"✅ {len(cities)} villes chargées pour {country}")
                return cities
        except Exception as e:
            print(f"❌ Erreur chargement {file_path}: {e}")
            return []

    def get_available_countries(self) -> List[str]:
        """Retourne la liste des pays disponibles"""
        return list(self.countries.keys())

    def get_country_info(self, country: str) -> Dict:
        """Informations sur un pays"""
        cities = self._load_country_data(country)
        return {
            "country": country,
            "cities_count": len(cities),
            "available": country in self.countries
        }


    def _calculer_poids_personnalises(self, questionnaire: Dict) -> Dict:
        """🔥 POIDS BASÉS UNIQUEMENT SUR LES PRIORITÉS UTILISATEUR"""
        priorities = questionnaire.get('priorites', [])
        budget = questionnaire.get('budget', 3000)

        # Conversion du budget en int si c'est une string
        if isinstance(budget, str):
            try:
                budget = int(budget)
            except (ValueError, TypeError):
                budget = 3000  # Valeur par défaut si conversion échoue

        # Poids de base pour tous les critères
        weights = {}
        for criterion in self.mapping.keys():
            weights[criterion] = 1.0  # Poids neutre de base

        # Application priorités avec AMPLIFICATION selon importance
        priority_scores = {}
        for priority in priorities:
            # Trouver le critère correspondant
            for questionnaire_criterion, mapped_criteria in self.mapping.items():
                if priority in mapped_criteria:
                    priority_scores[questionnaire_criterion] = priority_scores.get(questionnaire_criterion, 0) + 1

        # Amplifier les priorités mentionnées
        if priority_scores:
            max_mentions = max(priority_scores.values())
            for criterion, mentions in priority_scores.items():
                if mentions == max_mentions:
                    weights[criterion] = 10.0  # Priorité MAXIMALE
                elif mentions > 0:
                    weights[criterion] = 5.0   # Priorité élevée

        # Ajustement selon le budget (influence indirecte)
        if budget <= 2000:
            weights['cost_of_living'] *= 3.0  # Budget serré = coût important
        elif budget >= 6000:
            weights['lifestyle'] *= 2.0       # Budget élevé = lifestyle important

        return weights

    def _calculer_score_base(self, city: Dict, weights: Dict) -> float:
        """📊 CALCUL SCORE DE BASE OPTIMISÉ"""
        total_score = 0.0
        total_weight = 0.0

        for questionnaire_criterion, weight in weights.items():
            # Récupérer valeurs pour ce critère
            mapped_criteria = self.mapping.get(questionnaire_criterion, [])
            criterion_values = []

            for data_criterion in mapped_criteria:
                if 'scores' in city and data_criterion in city['scores']:
                    value = city['scores'][data_criterion]
                    if isinstance(value, (int, float)) and 0 <= value <= 1:
                        criterion_values.append(value)

            # Prendre la MEILLEURE valeur pour ce critère (optimiste)
            if criterion_values:
                best_value = max(criterion_values)
                total_score += best_value * weight
                total_weight += weight

        return total_score / total_weight if total_weight > 0 else 0.0



    def _penalite_monopole(self, city: Dict) -> float:
        """⚖️ PÉNALITÉ ANTI-MONOPOLE"""
        # Pénaliser les villes "trop parfaites" pour favoriser la diversité
        city_name = city.get('city', '').lower()

        # Villes qui reviennent trop souvent = pénalité
        monopoly_cities = ['singapore', 'zurich', 'geneva', 'dubai']

        if any(monopoly in city_name for monopoly in monopoly_cities):
            return 0.05  # -5% pour éviter la monopolisation

        return 0.0

    def _amplifier_contrastes(self, cities: List[Dict]) -> List[Dict]:
        """🔥 AMPLIFICATION DES CONTRASTES"""
        if not cities:
            return cities

        scores = [city['score'] for city in cities]
        score_max = max(scores)
        score_min = min(scores)
        score_range = score_max - score_min

        # Amplifier les différences
        for city in cities:
            score_normalized = (city['score'] - score_min) / score_range if score_range > 0 else 0
            # Fonction d'amplification non-linéaire
            amplified = math.pow(score_normalized, 0.7)  # Courbe d'amplification
            city['score'] = round(score_min + (amplified * score_range), 1)

        return cities

    # 🌟 NOUVELLES MÉTHODES POUR DIVERSIFICATION INTELLIGENTE

    def _get_population_number(self, population_str: str) -> float:
        """Parser universel de population - gère tous les formats"""
        if not population_str:
            return 0.0

        # Nettoyer la chaîne
        pop_clean = population_str.strip().upper()

        try:
            if 'M' in pop_clean:
                return float(pop_clean.replace('M', ''))
            elif 'K' in pop_clean:
                return float(pop_clean.replace('K', '')) / 1000  # Convertir en millions
            else:
                # Format numérique pur
                num = float(pop_clean)
                if num > 1000:  # Probablement en milliers
                    return num / 1000000  # Convertir en millions
                else:
                    return num
        except:
            return 0.0

    def _categorize_city_size_universal(self, population: float, country: str) -> str:
        """Catégorisation adaptée par pays"""

        # Seuils par pays (en millions)
        country_thresholds = {
            'usa': {'big': 2.0, 'medium': 0.5},      # USA a des mégalopoles
            'france': {'big': 1.0, 'medium': 0.3},   # France plus petite échelle
            'maroc': {'big': 1.0, 'medium': 0.4},    # Maroc échelle similaire France
            'canada': {'big': 1.5, 'medium': 0.4},   # Canada entre USA et Europe
            'uk': {'big': 1.0, 'medium': 0.3},       # UK comme France
            'germany': {'big': 1.5, 'medium': 0.4},  # Allemagne
            'spain': {'big': 1.2, 'medium': 0.3},    # Espagne
            'italy': {'big': 1.0, 'medium': 0.3},    # Italie
            'australia': {'big': 1.5, 'medium': 0.4}, # Australie
            'brazil': {'big': 3.0, 'medium': 1.0},   # Brésil grandes mégalopoles
            'mexico': {'big': 2.0, 'medium': 0.5},   # Mexique
            'argentina': {'big': 2.0, 'medium': 0.5}, # Argentine
            'japan': {'big': 2.0, 'medium': 0.8},    # Japon dense
            'thailand': {'big': 1.5, 'medium': 0.4}, # Thaïlande
            # Défaut pour autres pays
            'default': {'big': 1.0, 'medium': 0.4}
        }

        thresholds = country_thresholds.get(country, country_thresholds['default'])

        if population >= thresholds['big']:
            return 'big_city'
        elif population >= thresholds['medium']:
            return 'medium_city'
        else:
            return 'small_city'

    def _generate_explanation_universal(self, city: Dict, size_type: str, country: str, questionnaire: Dict) -> Dict:
        """Génère une explication personnalisée pour chaque recommandation"""

        city_name = city['city']

        # Templates d'explications par type
        explanations_templates = {
            'top_performer': {
                'maroc': {
                    'rabat': "🏛️ **Choix optimal** - Rabat excelle en stabilité juridique et infrastructure premium",
                    'casablanca': "💼 **Hub économique** - Casablanca domine en opportunités business et réseau professionnel",
                    'default': f"⭐ **Score global élevé** - {city_name} performe excellemment sur vos critères prioritaires"
                },
                'france': {
                    'paris': "🎨 **Capitale culturelle** - Paris concentre opportunités et art de vivre français",
                    'lyon': "⚖️ **Équilibre parfait** - Lyon combine dynamisme économique et qualité de vie",
                    'default': f"⭐ **Excellence française** - {city_name} répond parfaitement à vos attentes"
                },
                'usa': {
                    'new york': "🌆 **Métropole mondiale** - New York offre le maximum d'opportunités professionnelles",
                    'san francisco': "🚀 **Hub innovation** - San Francisco, cœur de la tech mondiale",
                    'default': f"⭐ **Excellence américaine** - {city_name} score le mieux selon vos critères"
                },
                'default': f"⭐ **Choix optimal** - {city_name} excelle sur vos priorités principales"
            },
            'best_big_city': {
                'maroc': f"🏙️ **Grande métropole** - {city_name} offre le maximum d'opportunités et d'infrastructure",
                'france': f"🌆 **Grande ville française** - {city_name} combine rayonnement et services premium",
                'usa': f"🏢 **Métropole américaine** - {city_name} concentre emplois et dynamisme urbain",
                'default': f"🏙️ **Grande ville** - {city_name} offre le maximum d'opportunités"
            },
            'best_medium_city': {
                'maroc': f"⚖️ **Équilibre marocain** - {city_name} combine authenticité et modernité",
                'france': f"🏘️ **Ville à taille humaine** - {city_name} offre qualité de vie et praticité",
                'usa': f"🌳 **Ville moyenne** - {city_name} balance opportunités et tranquillité",
                'default': f"⚖️ **Équilibre idéal** - {city_name} combine qualité de vie et praticité"
            },
            'best_small_city': {
                'maroc': f"🏡 **Authenticité marocaine** - {city_name} offre le vrai art de vivre local",
                'france': f"🌸 **Charme français** - {city_name} préserve l'authenticité et la douceur de vivre",
                'usa': f"🏞️ **Small town charm** - {city_name} offre tranquillité et communauté soudée",
                'default': f"🏡 **Authenticité locale** - {city_name} offre calme et budget optimisé"
            }
        }

        # Sélectionner le template approprié
        templates = explanations_templates.get(size_type, {})
        country_templates = templates.get(country, templates.get('default', ''))

        if isinstance(country_templates, dict):
            explanation = country_templates.get(city_name.lower(), country_templates.get('default', ''))
        else:
            explanation = country_templates

        # Générer le badge selon le type
        badges = {
            'top_performer': '⭐ Optimal',
            'best_big_city': '🌆 Métropole',
            'best_medium_city': '⚖️ Équilibre',
            'best_small_city': '🏡 Authenticité'
        }

        return {
            'explanation': explanation,
            'badge': badges.get(size_type, '✨ Recommandé'),
            'recommendation_type': size_type
        }

    def _generate_diversified_top5(self, scored_cities: List, questionnaire: Dict, country: str) -> List:
        """Génère un Top 5 diversifié avec explications contextuelles"""

        # 1. Catégoriser les villes par taille
        categorized = {'big_city': [], 'medium_city': [], 'small_city': []}

        for city in scored_cities:
            population = self._get_population_number(city.get('population', '0'))
            size_category = self._categorize_city_size_universal(population, country)
            categorized[size_category].append(city)

        # 2. Générer recommandations diversifiées
        diversified_top5 = []
        used_cities = set()

        # Toujours les 2 meilleurs scores absolus
        top_performers = sorted(scored_cities, key=lambda x: x['score'], reverse=True)[:2]
        for city in top_performers:
            if city['city'] not in used_cities:
                explanation_data = self._generate_explanation_universal(city, 'top_performer', country, questionnaire)
                diversified_city = {
                    **city,
                    **explanation_data,
                    'population': city.get('population', ''),
                    'size_category': self._categorize_city_size_universal(
                        self._get_population_number(city.get('population', '0')), country
                    )
                }
                diversified_top5.append(diversified_city)
                used_cities.add(city['city'])

        # 3. Ajouter diversité si possible (1 de chaque taille)
        remaining_spots = 5 - len(diversified_top5)

        for size_type in ['big_city', 'medium_city', 'small_city']:
            if remaining_spots <= 0:
                break

            # Prendre le meilleur de cette catégorie qui n'est pas déjà utilisé
            candidates = [c for c in categorized[size_type] if c['city'] not in used_cities]
            if candidates:
                best_in_category = max(candidates, key=lambda x: x['score'])
                explanation_data = self._generate_explanation_universal(
                    best_in_category, f'best_{size_type}', country, questionnaire
                )
                diversified_city = {
                    **best_in_category,
                    **explanation_data,
                    'population': best_in_category.get('population', ''),
                    'size_category': size_type
                }
                diversified_top5.append(diversified_city)
                used_cities.add(best_in_category['city'])
                remaining_spots -= 1

        # 4. Compléter avec les meilleurs scores restants si besoin
        while len(diversified_top5) < 5 and len(diversified_top5) < len(scored_cities):
            remaining_candidates = [c for c in scored_cities if c['city'] not in used_cities]
            if not remaining_candidates:
                break

            next_best = max(remaining_candidates, key=lambda x: x['score'])
            explanation_data = self._generate_explanation_universal(
                next_best, 'top_performer', country, questionnaire
            )
            diversified_city = {
                **next_best,
                **explanation_data,
                'population': next_best.get('population', ''),
                'size_category': self._categorize_city_size_universal(
                    self._get_population_number(next_best.get('population', '0')), country
                )
            }
            diversified_top5.append(diversified_city)
            used_cities.add(next_best['city'])

        return diversified_top5

# 🧪 TESTS RÉVOLUTIONNAIRES
if __name__ == "__main__":
    print("🧪 Test Algorithme Révolutionnaire")

    algo = AlgorithmeRevolutionnaire()

    # Tests avec critères différents pour démontrer la diversité
    tests_utilisateurs = [
        {
            'name': '💸 Budget Serré - Éducation',
            'questionnaire': {
                'age': 22,
                'budget': 1500,
                'priorites': ['education', 'cost_of_living', 'culture_loisirs']
            }
        },
        {
            'name': '💼 Business & Infrastructure',
            'questionnaire': {
                'age': 35,
                'budget': 6000,
                'priorites': ['reseau_business', 'services_bancaires', 'infrastructure_numerique']
            }
        }
    ]

    for test in tests_utilisateurs:
        print(f"\\n{test['name']}:")
        results = algo.analyser(test['questionnaire'], 'world')
        print("   Top 3:")
        for i, city in enumerate(results['recommendations'][:3], 1):
            print(f"   {i}. {city['city']} - {city['score']}%")
