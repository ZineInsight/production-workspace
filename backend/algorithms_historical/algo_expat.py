"""
🎯 ALGORITHME EXPAT SIMPLE - LIEU DE VIE IDÉAL
==============================================
Algorithme direct basé sur les 9 questions expat avec LOGIQUE DE BON SENS
Version: 1.0 - Simple & Efficace
Author: Revolutionary Team

PRINCIPE : Matching intelligent questionnaire → critères villes (0=médiocre, 1=excellent)
OBJECTIF : TOP 3 villes parfaitement adaptées au profil utilisateur
"""

import json
import os

class AlgorithmeExpat:

    def __init__(self):
        """Initialisation avec mapping intelligent questionnaire → critères"""

        # 🎯 MAPPING RÉPONSES → FONCTIONS DE COMPATIBILITÉ
        self.compatibility_functions = {
            'expat_passport': self.eval_passport_compatibility,
            'expat_budget_realistic': self.eval_budget_compatibility,
            'expat_climate_tolerance': self.eval_climate_compatibility,
            'expat_security_needs': self.eval_security_compatibility,
            'expat_lifestyle_pace': self.eval_lifestyle_compatibility,
            'expat_language_comfort': self.eval_language_compatibility,
            'expat_family_status': self.eval_family_compatibility,
            'expat_professional_status': self.eval_professional_compatibility,
            'expat_mobility_preference': self.eval_mobility_compatibility
        }

        # 🏆 POIDS DES QUESTIONS (importance relative)
        self.question_weights = {
            'expat_passport': 10,        # Contrainte légale absolue
            'expat_budget_realistic': 9,  # Quasi-contrainte absolue
            'expat_climate_tolerance': 8, # Impact santé/humeur
            'expat_security_needs': 8,    # Tranquillité d'esprit
            'expat_family_status': 8,     # Impact majeur logement/écoles
            'expat_lifestyle_pace': 7,    # Rythme urbain
            'expat_language_comfort': 7,  # Barrière communication
            'expat_professional_status': 7, # Opportunités/visa/revenus
            'expat_mobility_preference': 6  # Mobilité quotidienne
        }

    def calculer_recommandations(self, reponses_user, country='world'):
        """
        🎯 FONCTION PRINCIPALE - Calcule les 3 meilleures villes

        Args:
            reponses_user (dict): Réponses du questionnaire
            country (str): Pays/région ('world' pour international)

        Returns:
            list: Top 3 villes avec scores de compatibilité
        """

        # Charger les données des villes
        villes = self.charger_donnees_villes(country)
        if not villes:
            return []

        # Calculer compatibilité pour chaque ville
        scores_villes = []

        for ville in villes:
            score_total = self.calculer_score_ville(reponses_user, ville)

            # 🚫 LOGIQUE DE BON SENS - Filtrage intelligent
            if self.appliquer_logique_bon_sens(reponses_user, ville, score_total):
                scores_villes.append({
                    'city': ville['city'],
                    'country': ville['country'],
                    'score': round(score_total, 1),
                    'compatibility': min(100, round(score_total * 100, 1))
                })

        # Trier par score et retourner TOP 3
        scores_villes.sort(key=lambda x: x['score'], reverse=True)
        return scores_villes[:3]

    def calculer_score_ville(self, reponses_user, ville):
        """Calcule le score de compatibilité total d'une ville"""

        score_total = 0
        poids_total = 0

        for question_id, reponse_valeur in reponses_user.items():
            if question_id in self.compatibility_functions:
                # Fonction de compatibilité spécifique
                compatibility_func = self.compatibility_functions[question_id]
                score_compatibilite = compatibility_func(reponse_valeur, ville)

                # Pondération par importance de la question
                poids = self.question_weights.get(question_id, 5)
                score_total += score_compatibilite * poids
                poids_total += poids

        # Score final normalisé (0.0 à 1.0)
        return score_total / poids_total if poids_total > 0 else 0.0

    # ===============================================
    # 🎯 FONCTIONS DE COMPATIBILITÉ PAR QUESTION
    # ===============================================

    def eval_budget_compatibility(self, budget_choice, ville):
        """Évaluation compatibilité budget - LOGIQUE STRICTE"""

        # Récupération des critères coût (0=cher, 1=pas cher)
        ratio_salaire_loyer = ville['scores'].get('ratio_salaire_loyer', 0.5)
        cout_installation = ville['scores'].get('cout_installation', 0.5)

        cout_global = (ratio_salaire_loyer + cout_installation) / 2

        if budget_choice == 'budget_maximizer':      # 500-1200€
            return cout_global  # Plus c'est pas cher, mieux c'est
        elif budget_choice == 'budget_balanced':     # 1200-2500€
            return 1.0 - abs(cout_global - 0.6)  # Optimal autour de 0.6
        elif budget_choice == 'budget_comfort':      # 2500-4000€
            return 1.0 - abs(cout_global - 0.4)  # Optimal autour de 0.4
        elif budget_choice == 'budget_premium':      # 4000€+
            return 1.0 - cout_global  # Plus c'est cher, plus c'est premium

        return 0.5

    def eval_climate_compatibility(self, climate_choice, ville):
        """Évaluation compatibilité climat"""

        climat_agreable = ville['scores'].get('climat_agreable', 0.5)
        ville_nom = ville['city'].lower()

        if climate_choice == 'tropical_lover':
            # Bonus pour villes tropicales
            tropicales = ['bangkok', 'manila', 'jakarta', 'mumbai', 'ho chi minh city',
                         'kuala lumpur', 'miami', 'rio de janeiro', 'bogotá', 'medellín',
                         'quito', 'nairobi', 'lagos', 'casablanca', 'cape town']
            bonus = 0.3 if any(t in ville_nom for t in tropicales) else 0
            return min(1.0, climat_agreable + bonus)

        elif climate_choice == 'mediterranean_fan':
            # Bonus pour climat méditerranéen
            med_cities = ['barcelona', 'lisbon', 'tel aviv', 'cape town', 'casablanca']
            bonus = 0.3 if any(m in ville_nom for m in med_cities) else 0
            return min(1.0, climat_agreable + bonus)

        elif climate_choice == 'cool_weather_lover':
            # Malus pour les trop chauds
            if any(t in ville_nom for t in ['bangkok', 'mumbai', 'dubai', 'miami']):
                return climat_agreable * 0.5
            return climat_agreable

        return climat_agreable

    def eval_security_compatibility(self, security_choice, ville):
        """Évaluation compatibilité sécurité"""

        securite = ville['scores'].get('securite_publique', 0.5)
        stabilite = ville['scores'].get('stabilite_juridique', 0.5)

        securite_globale = (securite + stabilite) / 2

        if security_choice == 'maximum_security':
            return securite_globale if securite_globale >= 0.8 else 0.2
        elif security_choice == 'high_security':
            return securite_globale if securite_globale >= 0.7 else 0.4
        elif security_choice == 'reasonable_security':
            return securite_globale if securite_globale >= 0.5 else 0.6
        elif security_choice == 'adventure_tolerance':
            return min(1.0, securite_globale + 0.3)  # Plus tolérant

        return securite_globale

    def eval_lifestyle_compatibility(self, lifestyle_choice, ville):
        """Évaluation compatibilité style de vie"""

        culture_loisirs = ville['scores'].get('culture_loisirs', 0.5)
        scene_culturelle = ville['scores'].get('scene_culturelle', 0.5)

        dynamisme = (culture_loisirs + scene_culturelle) / 2

        if lifestyle_choice == 'hyperactive_urban':
            megacities = ['new york city', 'tokyo', 'hong kong', 'singapore', 'london']
            ville_nom = ville['city'].lower()
            bonus = 0.3 if any(m in ville_nom for m in megacities) else 0
            return min(1.0, dynamisme + bonus)
        elif lifestyle_choice == 'quiet_peaceful':
            # Malus pour mégapoles
            megacities = ['new york city', 'mumbai', 'são paulo', 'lagos']
            ville_nom = ville['city'].lower()
            malus = -0.3 if any(m in ville_nom for m in megacities) else 0
            return max(0.0, dynamisme + malus)

        return dynamisme

    def eval_language_compatibility(self, language_choice, ville):
        """Évaluation compatibilité langue"""

        tolerance_diversite = ville['scores'].get('tolerance_diversite', 0.5)

        if language_choice == 'english_only':
            anglophones = ['toronto', 'new york city', 'san francisco', 'vancouver',
                          'seattle', 'austin', 'montreal', 'miami', 'denver', 'sydney', 'auckland']
            ville_nom = ville['city'].lower()
            if any(a in ville_nom for a in anglophones):
                return 1.0
            elif ville_nom in ['singapore', 'hong kong', 'dublin', 'amsterdam']:
                return 0.9  # Anglais très répandu
            else:
                return 0.3  # Difficile sans anglais

        return tolerance_diversite

    def eval_family_compatibility(self, family_choice, ville):
        """Évaluation compatibilité situation familiale"""

        if family_choice == 'single_flexible':
            scene_culturelle = ville['scores'].get('scene_culturelle', 0.5)
            tolerance_diversite = ville['scores'].get('tolerance_diversite', 0.5)
            return (scene_culturelle + tolerance_diversite) / 2

        elif family_choice == 'family_young_kids':
            ecoles_int = ville['scores'].get('ecoles_internationales', 0.5)
            activites_enfants = ville['scores'].get('activites_enfants', 0.5)
            securite = ville['scores'].get('securite_publique', 0.5)
            return (ecoles_int + activites_enfants + securite) / 3

        return 0.5

    def eval_professional_compatibility(self, pro_choice, ville):
        """Évaluation compatibilité situation professionnelle"""

        if pro_choice == 'entrepreneur_startup':
            startup = ville['scores'].get('scene_startup', 0.5)
            innovation = ville['scores'].get('ecosysteme_innovation', 0.5)
            coworking = ville['scores'].get('espaces_coworking', 0.5)
            return (startup + innovation + coworking) / 3

        elif pro_choice == 'digital_nomad':
            coworking = ville['scores'].get('espaces_coworking', 0.5)
            infrastructure = ville['scores'].get('infrastructure_premium', 0.5)
            return (coworking + infrastructure) / 2

        return ville['scores'].get('emploi_accessible', 0.5)

    def eval_mobility_compatibility(self, mobility_choice, ville):
        """Évaluation compatibilité transport"""

        transport_eco = ville['scores'].get('transport_economique', 0.5)
        infrastructure = ville['scores'].get('infrastructure_premium', 0.5)

        if mobility_choice == 'public_transport_only':
            return (transport_eco + infrastructure) / 2
        elif mobility_choice == 'car_essential':
            return infrastructure  # Infrastructure routière

        return (transport_eco + infrastructure) / 2

    def eval_passport_compatibility(self, passport_choice, ville):
        """Évaluation compatibilité passeport/visa"""

        facilite_visa = ville['scores'].get('facilite_visa', 0.5)

        if passport_choice == 'eu_passport':
            # Bonus pour l'Europe
            eu_cities = ['lisbon', 'berlin', 'amsterdam', 'prague', 'barcelona',
                        'vienna', 'warsaw', 'dublin', 'stockholm', 'zurich']
            ville_nom = ville['city'].lower()
            bonus = 0.4 if any(eu in ville_nom for eu in eu_cities) else 0
            return min(1.0, facilite_visa + bonus)

        return facilite_visa

    # ===============================================
    # 🚫 LOGIQUE DE BON SENS - FILTRAGE INTELLIGENT
    # ===============================================

    def appliquer_logique_bon_sens(self, reponses_user, ville, score):
        """Applique la logique de bon sens pour éviter les incohérences"""

        ville_nom = ville['city'].lower()
        budget = reponses_user.get('expat_budget_realistic', '')
        lifestyle = reponses_user.get('expat_lifestyle_pace', '')
        security = reponses_user.get('expat_security_needs', '')

        # 🚫 RÈGLE 1: Pas de Dubai/Singapore pour les budgets serrés
        if budget == 'budget_maximizer':
            villes_cheres = ['dubai', 'singapore', 'zurich', 'hong kong', 'new york city', 'san francisco']
            if any(cher in ville_nom for cher in villes_cheres):
                return False

        # 🚫 RÈGLE 2: Pas de NYC pour quelqu'un qui veut du calme
        if lifestyle == 'quiet_peaceful':
            megacities_stressantes = ['new york city', 'mumbai', 'tokyo', 'hong kong']
            if any(stress in ville_nom for stress in megacities_stressantes):
                return False

        # 🚫 RÈGLE 3: Sécurité maximale incompatible avec villes dangereuses
        if security == 'maximum_security':
            villes_risquees = ['caracas', 'lagos', 'manila', 'bogotá']
            if any(risque in ville_nom for risque in villes_risquees):
                return False

        # 🚫 RÈGLE 4: Score minimum pour être recommandé
        return score >= 0.4

    # ===============================================
    # 🗄️ CHARGEMENT DES DONNÉES
    # ===============================================

    def charger_donnees_villes(self, country):
        """Charge les données des villes depuis le JSON"""

        try:
            # Chemin vers le fichier des villes
            data_path = os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                'data_v2',
                'villes_world.json'
            )

            with open(data_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get('cities', [])

        except Exception as e:
            print(f"❌ Erreur chargement données: {e}")
            return []

    def get_available_countries(self):
        """Retourne la liste des pays disponibles (compatibilité API)"""
        try:
            villes = self.charger_donnees_villes('world')
            countries = list(set(ville['country'] for ville in villes))
            return countries
        except Exception as e:
            print(f"❌ Erreur récupération pays: {e}")
            return ['World']

# ===============================================
# 🎯 FONCTION PRINCIPALE POUR L'API
# ===============================================

def calculer_recommandations_expat(reponses_user, country='world'):
    """
    🎯 Fonction principale appelée par l'API

    Args:
        reponses_user (dict): Réponses du questionnaire frontend
        country (str): Pays/région

    Returns:
        list: Top 3 villes recommandées avec scores
    """

    algorithme = AlgorithmeExpat()
    return algorithme.calculer_recommandations(reponses_user, country)

# Test de l'algorithme si exécuté directement
if __name__ == "__main__":
    # Test avec profil utilisateur exemple
    test_reponses = {
        'expat_passport': 'eu_passport',
        'expat_budget_realistic': 'budget_maximizer',
        'expat_climate_tolerance': 'tropical_lover',
        'expat_security_needs': 'maximum_security',
        'expat_lifestyle_pace': 'hyperactive_urban',
        'expat_language_comfort': 'english_only',
        'expat_family_status': 'single_flexible',
        'expat_professional_status': 'entrepreneur_startup',
        'expat_mobility_preference': 'public_transport_only'
    }

    resultats = calculer_recommandations_expat(test_reponses)

    print("🎯 RÉSULTATS TEST:")
    for i, ville in enumerate(resultats, 1):
        print(f"{i}. {ville['city']}, {ville['country']} - {ville['compatibility']}%")
