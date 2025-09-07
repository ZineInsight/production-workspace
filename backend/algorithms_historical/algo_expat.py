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
            'expat_mobility_preference': self.eval_mobility_compatibility,
            'expat_health_wellbeing': self.eval_health_compatibility,
            'expat_environmental_values': self.eval_environmental_compatibility,
            'expat_tax_finance_optimization': self.eval_tax_finance_compatibility
        }

        # 🏆 POIDS DES QUESTIONS (importance relative)
        self.question_weights = {
            'expat_passport': 10,        # Contrainte légale absolue
            'expat_budget_realistic': 9,  # Quasi-contrainte absolue
            'expat_climate_tolerance': 8, # Impact santé/humeur
            'expat_security_needs': 8,    # Tranquillité d'esprit
            'expat_family_status': 8,     # Impact majeur logement/écoles
            'expat_health_wellbeing': 8,  # Santé & bien-être
            'expat_lifestyle_pace': 7,    # Rythme urbain
            'expat_language_comfort': 7,  # Barrière communication
            'expat_professional_status': 7, # Opportunités/visa/revenus
            'expat_tax_finance_optimization': 7, # Optimisation fiscale
            'expat_mobility_preference': 6,  # Mobilité quotidienne
            'expat_environmental_values': 6  # Conscience écologique
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
                    'compatibility': min(100, round(score_total * 100, 1)),
                    'continent': self.get_continent(ville['country']),
                    'original_score': score_total  # Score original avant ajustements
                })

        # 🌍 ANTI-MONOPOLE GÉOGRAPHIQUE - Diversité forcée
        scores_villes = self.apply_geographic_diversity(scores_villes, reponses_user)

        # Trier par score ajusté et retourner TOP 3
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
            # Bonus pour villes vraiment froides
            cold_cities = ['stockholm', 'helsinki', 'copenhagen', 'oslo', 'reykjavik', 
                          'moscow', 'st petersburg', 'tallinn', 'riga', 'vilnius',
                          'montreal', 'toronto', 'vancouver', 'berlin', 'prague', 'warsaw']
            bonus = 0.4 if any(c in ville_nom for c in cold_cities) else 0
            
            # Malus FORT pour les trop chauds (méditerranéen inclus)
            hot_cities = ['bangkok', 'mumbai', 'dubai', 'miami', 'lisbon', 'barcelona', 
                         'tel aviv', 'casablanca', 'rio de janeiro']
            if any(h in ville_nom for h in hot_cities):
                return climat_agreable * 0.3  # Malus renforcé
            
            return min(1.0, climat_agreable + bonus)

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

    def eval_health_compatibility(self, health_choice, ville):
        """Évaluation compatibilité santé & bien-être"""

        soins_accessibles = ville['scores'].get('soins_accessibles', 0.5)
        qualite_air = ville['scores'].get('qualite_air', 0.5)
        pollution_niveau = ville['scores'].get('pollution_niveau', 0.5)

        if health_choice == 'health_premium':
            # Exigence maximale : soins + air excellent
            score_sante = (soins_accessibles * 0.4 + qualite_air * 0.4 + (1 - pollution_niveau) * 0.2)
            return min(1.0, score_sante * 1.2)  # Boost pour les excellents

        elif health_choice == 'health_preventive':
            # Focus prévention : air + style de vie sain
            score_preventif = (qualite_air * 0.5 + (1 - pollution_niveau) * 0.3 + soins_accessibles * 0.2)
            return score_preventif

        elif health_choice == 'health_standard':
            # Soins corrects suffisent
            return soins_accessibles

        elif health_choice == 'health_adaptive':
            # S'adapte, même à la pollution
            return min(1.0, soins_accessibles * 0.7 + 0.3)  # Bonus adaptabilité

        return soins_accessibles

    def eval_environmental_compatibility(self, env_choice, ville):
        """Évaluation compatibilité conscience écologique"""

        energie_verte = ville['scores'].get('energie_verte', 0.5)
        agriculture_locale = ville['scores'].get('agriculture_locale', 0.5)
        mobilite_verte = ville['scores'].get('mobilite_verte', 0.5)

        if env_choice == 'eco_militant':
            # Écologie priorité absolue
            score_eco = (energie_verte * 0.4 + agriculture_locale * 0.3 + mobilite_verte * 0.3)
            return min(1.0, score_eco * 1.3)  # Boost pour les leaders verts

        elif env_choice == 'eco_conscious':
            # Conscient et engagé
            score_conscient = (energie_verte * 0.35 + mobilite_verte * 0.35 + agriculture_locale * 0.3)
            return score_conscient

        elif env_choice == 'eco_interested':
            # Intéressé si pratique
            score_pratique = (mobilite_verte * 0.5 + energie_verte * 0.3 + agriculture_locale * 0.2)
            return score_pratique

        elif env_choice == 'eco_neutral':
            # Neutre - pas de pénalité/bonus
            return 0.6  # Score neutre

        return (energie_verte + agriculture_locale + mobilite_verte) / 3

    def eval_tax_finance_compatibility(self, tax_choice, ville):
        """Évaluation compatibilité optimisation fiscale & finance"""

        optimisation_fiscale = ville['scores'].get('optimisation_fiscale', 0.5)
        services_bancaires = ville['scores'].get('services_bancaires', 0.5)
        services_luxe = ville['scores'].get('services_luxe', 0.5)

        if tax_choice == 'tax_optimizer':
            # Optimisation fiscale maximale
            score_optim = (optimisation_fiscale * 0.6 + services_bancaires * 0.25 + services_luxe * 0.15)
            return min(1.0, score_optim * 1.2)  # Boost paradis fiscaux

        elif tax_choice == 'tax_efficient':
            # Fiscalité avantageuse recherchée
            score_efficace = (optimisation_fiscale * 0.5 + services_bancaires * 0.5)
            return score_efficace

        elif tax_choice == 'tax_standard':
            # Fiscalité normale acceptable
            return services_bancaires  # Focus sur services bancaires

        elif tax_choice == 'tax_contribution':
            # Accepte impôts élevés si services publics excellents
            infrastructure = ville['scores'].get('infrastructure_premium', 0.5)
            soins = ville['scores'].get('soins_accessibles', 0.5)
            score_social = (infrastructure * 0.4 + soins * 0.4 + services_bancaires * 0.2)
            return score_social

        return optimisation_fiscale

    # ===============================================
    # 🌍 SYSTÈME ANTI-MONOPOLE GÉOGRAPHIQUE
    # ===============================================

    def get_continent(self, country):
        """Mapping pays → continent pour diversité géographique"""
        
        continent_mapping = {
            # Europe
            'Germany': 'Europe', 'Netherlands': 'Europe', 'Switzerland': 'Europe',
            'Sweden': 'Europe', 'Austria': 'Europe', 'Poland': 'Europe',
            'Czech Republic': 'Europe', 'Portugal': 'Europe', 'Spain': 'Europe',
            'Ireland': 'Europe',
            
            # Amérique du Nord
            'United States': 'North_America', 'Canada': 'North_America',
            
            # Amérique du Sud
            'Brazil': 'South_America', 'Colombia': 'South_America', 
            'Argentina': 'South_America', 'Chile': 'South_America',
            'Peru': 'South_America', 'Ecuador': 'South_America', 
            'Uruguay': 'South_America', 'Venezuela': 'South_America',
            
            # Asie
            'Singapore': 'Asia', 'Japan': 'Asia', 'South Korea': 'Asia',
            'Thailand': 'Asia', 'Malaysia': 'Asia', 'Indonesia': 'Asia',
            'Philippines': 'Asia', 'Vietnam': 'Asia', 'India': 'Asia',
            'Hong Kong': 'Asia',
            
            # Moyen-Orient
            'United Arab Emirates': 'Middle_East', 'Israel': 'Middle_East',
            
            # Afrique
            'South Africa': 'Africa', 'Morocco': 'Africa', 'Tunisia': 'Africa',
            'Nigeria': 'Africa', 'Kenya': 'Africa',
            
            # Océanie
            'Australia': 'Oceania', 'New Zealand': 'Oceania',
            
            # Amérique Centrale
            'Mexico': 'Central_America'
        }
        
        return continent_mapping.get(country, 'Other')

    def apply_geographic_diversity(self, scores_villes, reponses_user):
        """Applique la diversité géographique pour éviter le monopole"""
        
        if len(scores_villes) < 6:  # Pas assez de villes pour diversifier
            return scores_villes
        
        # 1. Identifier les continents représentés dans le TOP 10
        top_candidates = sorted(scores_villes, key=lambda x: x['original_score'], reverse=True)[:15]
        
        continent_counts = {}
        for ville in top_candidates:
            continent = ville['continent']
            continent_counts[continent] = continent_counts.get(continent, 0) + 1
        
        # 2. Appliquer malus aux continents sur-représentés
        for ville in scores_villes:
            continent = ville['continent']
            continent_count = continent_counts.get(continent, 0)
            
            # Malus progressif selon sur-représentation
            if continent_count >= 4:  # 4+ villes même continent
                malus = 0.15  # -15% du score
            elif continent_count >= 3:  # 3 villes même continent  
                malus = 0.10  # -10% du score
            elif continent_count >= 2:  # 2 villes même continent
                malus = 0.05  # -5% du score
            else:
                malus = 0.0   # Pas de malus
            
            # Appliquer le malus
            ville['score'] = ville['original_score'] * (1 - malus)
        
        # 3. Bonus diversité pour profils aventuriers
        adventure_profiles = ['adventure_tolerance', 'emerging_passport', 'immersion_ready']
        is_adventurous = any(
            reponses_user.get(key, '') in adventure_profiles 
            for key in ['expat_security_needs', 'expat_passport', 'expat_language_comfort']
        )
        
        if is_adventurous:
            # Bonus pour continents exotiques
            exotic_continents = ['Africa', 'South_America', 'Central_America']
            for ville in scores_villes:
                if ville['continent'] in exotic_continents:
                    ville['score'] = ville['original_score'] * 1.08  # +8% bonus aventure
        
        # 4. Forcer diversité dans le TOP 3 final
        return self.force_top3_diversity(scores_villes)

    def force_top3_diversity(self, scores_villes):
        """Force la diversité dans le TOP 3 final"""
        
        # Trier par score ajusté
        candidates = sorted(scores_villes, key=lambda x: x['score'], reverse=True)
        
        final_top3 = []
        used_continents = set()
        used_countries = set()
        
        # Sélection intelligente du TOP 3
        for ville in candidates:
            continent = ville['continent']
            country = ville['country']
            
            # Critères d'acceptation
            accept = True
            
            # RÈGLE 1: Maximum 2 villes du même continent
            if len(final_top3) >= 2 and continent in used_continents:
                if len([v for v in final_top3 if v['continent'] == continent]) >= 2:
                    accept = False
            
            # RÈGLE 2: Maximum 1 ville du même pays
            if country in used_countries:
                accept = False
            
            # RÈGLE 3: Si on a déjà 2 villes et pas assez de diversité, forcer
            if len(final_top3) == 2 and len(used_continents) == 1:
                # Forcer une ville d'un autre continent
                if continent in used_continents:
                    accept = False
            
            if accept:
                final_top3.append(ville)
                used_continents.add(continent)
                used_countries.add(country)
                
                if len(final_top3) >= 3:
                    break
        
        # Si on n'a pas assez de villes, prendre les meilleures restantes
        while len(final_top3) < 3 and len(final_top3) < len(candidates):
            for ville in candidates:
                if ville not in final_top3:
                    final_top3.append(ville)
                    break
        
        # Retourner tous les scores ajustés (pour tri final)
        return scores_villes

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
        """Applique la logique de bon sens avancée pour éviter les incohérences"""

        ville_nom = ville['city'].lower()
        
        # Extraction des réponses utilisateur
        budget = reponses_user.get('expat_budget_realistic', '')
        lifestyle = reponses_user.get('expat_lifestyle_pace', '')
        security = reponses_user.get('expat_security_needs', '')
        climate = reponses_user.get('expat_climate_tolerance', '')
        family = reponses_user.get('expat_family_status', '')
        health = reponses_user.get('expat_health_wellbeing', '')
        environmental = reponses_user.get('expat_environmental_values', '')
        tax_finance = reponses_user.get('expat_tax_finance_optimization', '')

        # 🚫 RÈGLE 1: BUDGET vs COÛT DE VIE
        if budget == 'budget_maximizer':
            villes_tres_cheres = ['zurich', 'geneva', 'singapore', 'hong kong', 'new york city', 
                                 'san francisco', 'sydney', 'oslo', 'copenhagen']
            if any(cher in ville_nom for cher in villes_tres_cheres):
                return False
                
        elif budget == 'budget_balanced':
            # Budget équilibré incompatible avec les plus chères
            villes_ultra_cheres = ['zurich', 'geneva', 'hong kong']
            if any(ultra in ville_nom for ultra in villes_ultra_cheres):
                return False

        # 🚫 RÈGLE 2: LIFESTYLE vs RYTHME URBAIN
        if lifestyle == 'quiet_peaceful':
            megacities_stressantes = ['new york city', 'mumbai', 'tokyo', 'hong kong', 
                                    'manila', 'jakarta', 'buenos aires']
            if any(stress in ville_nom for stress in megacities_stressantes):
                return False
                
        elif lifestyle == 'hyperactive_urban':
            # Hyperactif incompatible avec villes très calmes
            villes_trop_calmes = ['reykjavik', 'wellington', 'dublin', 'porto']
            if any(calme in ville_nom for calme in villes_trop_calmes):
                return False

        # 🚫 RÈGLE 3: SÉCURITÉ vs STABILITÉ
        if security == 'maximum_security':
            villes_instables = ['caracas', 'lagos', 'manila', 'bogotá', 'lima', 'nairobi']
            if any(instable in ville_nom for instable in villes_instables):
                return False
                
        elif security == 'adventure_tolerance':
            # Si on accepte l'aventure, boost pour villes émergentes
            villes_emergentes = ['nairobi', 'lima', 'bogotá', 'manila', 'mumbai']
            if any(emergent in ville_nom for emergent in villes_emergentes):
                return True  # Force l'acceptation

        # 🚫 RÈGLE 4: CLIMAT vs PRÉFÉRENCES
        if climate == 'cool_weather_lover':
            villes_tropicales = ['bangkok', 'ho chi minh city', 'jakarta', 'mumbai', 
                               'manila', 'kuala lumpur', 'singapore']
            if any(tropical in ville_nom for tropical in villes_tropicales):
                return False
                
        elif climate == 'tropical_lover':
            villes_froides = ['stockholm', 'helsinki', 'oslo', 'reykjavik', 'montreal', 'toronto']
            if any(froid in ville_nom for froid in villes_froides):
                return False

        # 🚫 RÈGLE 5: FAMILLE vs INFRASTRUCTURE
        if family in ['family_young_kids', 'family_teenagers']:
            # Familles évitent villes peu sûres ou infrastructure faible
            villes_peu_familiales = ['caracas', 'lagos', 'manila', 'nairobi']
            if any(peu_fam in ville_nom for peu_fam in villes_peu_familiales):
                return False

        # 🚫 RÈGLE 6: SANTÉ vs QUALITÉ AIR/SOINS
        if health == 'health_premium':
            # Santé premium incompatible avec pollution élevée
            villes_polluees = ['mumbai', 'delhi', 'jakarta', 'manila', 'ho chi minh city']
            if any(pollue in ville_nom for pollue in villes_polluees):
                return False

        # 🚫 RÈGLE 7: ÉCOLOGIE vs POLITIQUE VERTE
        if environmental == 'eco_militant':
            # Écolo militant évite les pays peu verts
            villes_peu_vertes = ['dubai', 'kuwait city', 'abu dhabi', 'caracas']
            if any(peu_vert in ville_nom for peu_vert in villes_peu_vertes):
                return False

        # 🚫 RÈGLE 8: FISCALITÉ vs SYSTÈME FISCAL
        if tax_finance == 'tax_optimizer':
            # Optimiseur fiscal évite les pays à fiscalité lourde
            villes_fiscalite_lourde = ['stockholm', 'copenhagen', 'oslo', 'helsinki']
            if any(lourd in ville_nom for lourd in villes_fiscalite_lourde):
                return False
                
        elif tax_finance == 'tax_contribution':
            # Contributeur évite les paradis fiscaux
            paradis_fiscaux = ['dubai', 'singapore', 'zurich', 'monaco']
            if any(paradis in ville_nom for paradis in paradis_fiscaux):
                return False

        # 🚫 RÈGLE 9: SCORE MINIMUM GÉNÉRAL
        if score < 0.35:  # Score trop faible
            return False
            
        # 🚫 RÈGLE 10: COHÉRENCE PROFIL GLOBAL
        # Budget serré + Sécurité max + Climat tropical = quasi impossible
        impossible_combinations = [
            (budget == 'budget_maximizer' and security == 'maximum_security' and score < 0.6),
            (health == 'health_premium' and environmental == 'eco_militant' and score < 0.5)
        ]
        
        if any(impossible_combinations):
            return False

        return True

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
        'expat_mobility_preference': 'public_transport_only',
        'expat_health_wellbeing': 'health_premium',
        'expat_environmental_values': 'eco_conscious',
        'expat_tax_finance_optimization': 'tax_optimizer'
    }

    resultats = calculer_recommandations_expat(test_reponses)

    print("🎯 RÉSULTATS TEST:")
    for i, ville in enumerate(resultats, 1):
        print(f"{i}. {ville['city']}, {ville['country']} - {ville['compatibility']}%")
