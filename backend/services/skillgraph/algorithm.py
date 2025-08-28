"""
💼 SKILLGRAPH ALGORITHM - INTELLIGENCE CARRIÈRE MODERNE
======================================================
Algorithme de recommandation carrière et optimisation compétences
Hérite de BaseAlgorithm pour patterns communs et évolutivité

Features:
- 34+ critères carrière/compétences personnalisables
- Matching intelligent profil/opportunités
- Gap analysis et formations recommandées
- Support marché emploi international
- Salaires et évolution de carrière optimisés

Basé sur: L'esprit ZScore adapté au monde professionnel
Architecture: BaseAlgorithm + DataLoader pattern évolutif
"""

import json
import random
import logging
from typing import Dict, List, Optional, Any
from datetime import datetime

# Import depuis la racine backend
import sys
from pathlib import Path
backend_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(backend_root))

from core.base_algorithm import BaseAlgorithm
from core.data_loader import DataLoader

logger = logging.getLogger(__name__)


class SkillGraphAlgorithm(BaseAlgorithm):
    """Algorithme SkillGraph moderne - Intelligence carrière et compétences"""

    def __init__(self, data_loader: Optional[DataLoader] = None):
        # Initialiser la classe mère
        super().__init__(service_name="skillgraph", version="1.0.0")

        # DataLoader centralisé (prêt pour futures données emplois)
        self.data_loader = data_loader or DataLoader()

        # 🏢 Secteurs d'activité supportés
        self.supported_sectors = {
            'tech': {'name': 'Technologies', 'growth': 'high', 'remote_friendly': True},
            'finance': {'name': 'Finance & Banque', 'growth': 'medium', 'remote_friendly': False},
            'healthcare': {'name': 'Santé & Medical', 'growth': 'high', 'remote_friendly': False},
            'education': {'name': 'Éducation & Formation', 'growth': 'medium', 'remote_friendly': True},
            'consulting': {'name': 'Conseil & Stratégie', 'growth': 'medium', 'remote_friendly': True},
            'marketing': {'name': 'Marketing & Communication', 'growth': 'medium', 'remote_friendly': True},
            'engineering': {'name': 'Ingénierie & R&D', 'growth': 'high', 'remote_friendly': False},
            'sales': {'name': 'Ventes & Business Dev', 'growth': 'medium', 'remote_friendly': True},
            'design': {'name': 'Design & Créatif', 'growth': 'medium', 'remote_friendly': True},
            'operations': {'name': 'Opérations & Logistique', 'growth': 'low', 'remote_friendly': False}
        }

        # 🌍 Marchés emploi internationaux
        self.job_markets = {
            'france': {'currency': 'EUR', 'avg_salary_range': '35K-80K', 'visa_req': False},
            'usa': {'currency': 'USD', 'avg_salary_range': '60K-150K', 'visa_req': True},
            'canada': {'currency': 'CAD', 'avg_salary_range': '50K-120K', 'visa_req': True},
            'uk': {'currency': 'GBP', 'avg_salary_range': '40K-100K', 'visa_req': True},
            'germany': {'currency': 'EUR', 'avg_salary_range': '40K-90K', 'visa_req': True},
            'netherlands': {'currency': 'EUR', 'avg_salary_range': '45K-95K', 'visa_req': True},
            'australia': {'currency': 'AUD', 'avg_salary_range': '60K-130K', 'visa_req': True},
            'singapore': {'currency': 'SGD', 'avg_salary_range': '50K-120K', 'visa_req': True}
        }

        logger.info(f"✅ SkillGraph Algorithm v{self.version} initialized - {len(self.supported_sectors)} sectors")

    def get_specific_criteria(self) -> List[str]:
        """Critères spécifiques à SkillGraph (34+ critères carrière/compétences)"""
        return [
            # 💰 Rémunération et avantages
            'salary_expectations', 'bonus_structure', 'equity_options', 'benefits_package',
            'pension_plan', 'health_insurance', 'vacation_days', 'flexible_hours',

            # 🎯 Compétences et expertise
            'technical_skills', 'soft_skills', 'leadership_skills', 'language_skills',
            'certification_level', 'years_experience', 'domain_expertise', 'learning_agility',

            # 🏢 Environnement de travail
            'company_size', 'startup_vs_corporate', 'team_size', 'management_style',
            'company_culture', 'diversity_inclusion', 'innovation_level', 'work_life_balance',

            # 📍 Localisation et mobilité
            'remote_work', 'hybrid_work', 'travel_requirements', 'relocation_flexibility',
            'visa_sponsorship', 'cost_of_living_adjust', 'commute_time', 'city_preference',

            # 📈 Évolution et croissance
            'career_growth', 'promotion_speed', 'mentorship_available', 'training_budget',
            'conference_budget', 'internal_mobility', 'skill_development', 'network_building',

            # 🎪 Mission et impact
            'job_impact', 'social_mission', 'industry_prestige', 'job_security',
            'performance_pressure', 'creative_freedom', 'decision_autonomy'
        ]

    def analyze(self, questionnaire: Dict, country: str = "france") -> Dict:
        """
        Analyse principale SkillGraph - Recommandations carrière intelligentes
        Implémentation de la méthode abstraite BaseAlgorithm
        """
        try:
            # Validation questionnaire (héritée)
            if not self.validate_questionnaire(questionnaire):
                return {"error": "Invalid questionnaire", "recommendations": []}

            # Cache check
            cache_key = f"skillgraph_{country}_{len(questionnaire)}"
            cached_result = self.get_cached_result(cache_key)
            if cached_result:
                logger.info("📦 Returning cached SkillGraph result")
                return cached_result

            # 1. Analyser profil utilisateur
            user_profile = self._analyze_user_profile(questionnaire)

            # 2. Générer recommandations emplois (MVP avec données simulées)
            job_recommendations = self._generate_job_recommendations(user_profile, country)

            # 3. Analyser gaps compétences
            skill_gaps = self._analyze_skill_gaps(user_profile, job_recommendations)

            # 4. Recommandations formations
            training_recommendations = self._recommend_training(skill_gaps)

            # 5. Préparer résultat final
            result = {
                "success": True,
                "career_recommendations": job_recommendations[:3],  # TOP 3
                "skill_analysis": {
                    "current_level": user_profile.get('experience_level', 'intermediate'),
                    "strengths": user_profile.get('strengths', []),
                    "skill_gaps": skill_gaps[:3],
                    "recommended_training": training_recommendations[:3]
                },
                "market_insights": {
                    "country": country,
                    "market_info": self.job_markets.get(country, {}),
                    "trending_skills": self._get_trending_skills(country),
                    "salary_trends": self._get_salary_trends(country)
                },
                "algorithm_version": f"SkillGraph {self.version}",
                "total_analyzed": len(job_recommendations)
            }

            # Cache et logs
            self.cache_result(cache_key, result, ttl_minutes=45)
            self.log_calculation(len(questionnaire), len(job_recommendations), country)

            return result

        except Exception as e:
            logger.error(f"❌ SkillGraph analysis error: {e}")
            return {"error": str(e), "career_recommendations": []}

    def calculate_score(self, job_data: Dict, questionnaire: Dict) -> float:
        """
        Calcule le score de compatibilité profil/emploi
        Implémentation de la méthode abstraite BaseAlgorithm
        """
        # Calculer poids personnalisés
        weights = self._calculate_career_weights(questionnaire)

        # Score de compatibilité basé sur les critères
        compatibility_scores = []

        for criterion, weight in weights.items():
            if criterion in job_data:
                job_value = float(job_data[criterion])
                weighted_score = job_value * weight
                compatibility_scores.append(weighted_score)

        # Score de base
        if compatibility_scores:
            base_score = self.calculate_weighted_average(compatibility_scores)
        else:
            base_score = 0.6  # Score neutre pour nouvelles opportunités

        # Bonus secteur en croissance
        sector_bonus = 0.05 if job_data.get('sector_growth') == 'high' else 0

        # Score final normalisé (0-100)
        final_score = self.normalize_score((base_score + sector_bonus) * 100, 0, 100)

        return final_score

    def _analyze_user_profile(self, questionnaire: Dict) -> Dict:
        """Analyse le profil utilisateur selon les réponses"""
        profile = {
            'experience_level': 'intermediate',
            'preferred_sectors': [],
            'strengths': [],
            'priorities': [],
            'work_style': 'balanced'
        }

        # Analyse des réponses pour extraire profil
        for key, response in questionnaire.items():
            response_text = str(response).lower() if not isinstance(response, dict) else str(response.get('value', '')).lower()

            # Détection niveau d'expérience
            if any(word in response_text for word in ['junior', 'débutant', 'entry']):
                profile['experience_level'] = 'junior'
            elif any(word in response_text for word in ['senior', 'expert', 'lead', 'manager']):
                profile['experience_level'] = 'senior'

            # Détection secteurs préférés
            for sector, info in self.supported_sectors.items():
                if sector in response_text or any(word in response_text for word in info['name'].lower().split()):
                    if sector not in profile['preferred_sectors']:
                        profile['preferred_sectors'].append(sector)

            # Détection priorités
            if any(word in response_text for word in ['salary', 'money', 'salaire']):
                profile['priorities'].append('compensation')
            if any(word in response_text for word in ['remote', 'télétravail', 'home']):
                profile['priorities'].append('flexibility')
            if any(word in response_text for word in ['growth', 'career', 'évolution']):
                profile['priorities'].append('development')

        # Fallback secteurs si aucun détecté
        if not profile['preferred_sectors']:
            profile['preferred_sectors'] = ['tech', 'consulting']

        # Générer forces basées sur l'expérience
        if profile['experience_level'] == 'senior':
            profile['strengths'] = ['Leadership', 'Strategic Vision', 'Team Management']
        elif profile['experience_level'] == 'junior':
            profile['strengths'] = ['Learning Agility', 'Fresh Perspective', 'Adaptability']
        else:
            profile['strengths'] = ['Problem Solving', 'Collaboration', 'Technical Skills']

        return profile

    def _generate_job_recommendations(self, user_profile: Dict, country: str) -> List[Dict]:
        """Génère des recommandations d'emplois (MVP avec données simulées)"""
        # Base de données emplois simulée (en attendant vraies données)
        job_templates = [
            {
                'title': 'Senior Data Scientist',
                'company': 'TechCorp Paris',
                'sector': 'tech',
                'location': 'Paris, France',
                'remote_friendly': True,
                'salary_range': '65K-85K EUR',
                'experience_required': 'senior',
                'key_skills': ['Python', 'Machine Learning', 'Statistics'],
                'visa_support': True,
                'company_size': 'medium'
            },
            {
                'title': 'Product Manager',
                'company': 'Startup Innovante',
                'sector': 'tech',
                'location': 'Lyon, France',
                'remote_friendly': True,
                'salary_range': '55K-75K EUR',
                'experience_required': 'intermediate',
                'key_skills': ['Product Strategy', 'Agile', 'Analytics'],
                'visa_support': False,
                'company_size': 'small'
            },
            {
                'title': 'Consultant Strategy',
                'company': 'Big Consulting',
                'sector': 'consulting',
                'location': 'Paris, France',
                'remote_friendly': False,
                'salary_range': '60K-90K EUR',
                'experience_required': 'intermediate',
                'key_skills': ['Strategic Analysis', 'Presentation', 'Client Management'],
                'visa_support': True,
                'company_size': 'large'
            },
            {
                'title': 'UX Designer',
                'company': 'Creative Agency',
                'sector': 'design',
                'location': 'Bordeaux, France',
                'remote_friendly': True,
                'salary_range': '40K-60K EUR',
                'experience_required': 'intermediate',
                'key_skills': ['Figma', 'User Research', 'Prototyping'],
                'visa_support': False,
                'company_size': 'medium'
            },
            {
                'title': 'Marketing Manager',
                'company': 'Scale-up Marketing',
                'sector': 'marketing',
                'location': 'Nantes, France',
                'remote_friendly': True,
                'salary_range': '45K-65K EUR',
                'experience_required': 'intermediate',
                'key_skills': ['Digital Marketing', 'Analytics', 'Campaign Management'],
                'visa_support': False,
                'company_size': 'medium'
            }
        ]

        # Filtrer selon profil utilisateur
        filtered_jobs = []
        preferred_sectors = user_profile.get('preferred_sectors', ['tech'])

        for job in job_templates:
            # Compatibilité secteur
            if job['sector'] in preferred_sectors:
                # Calculer score de compatibilité
                job['compatibility_score'] = self.calculate_score(job, {'priorities': user_profile.get('priorities', [])})
                job['match_reasons'] = self._generate_match_reasons(job, user_profile)
                filtered_jobs.append(job)

        # Ajouter diversité si pas assez de résultats
        if len(filtered_jobs) < 3:
            for job in job_templates:
                if job not in filtered_jobs:
                    job['compatibility_score'] = random.randint(70, 85)
                    job['match_reasons'] = ['Nouvelle opportunité', 'Secteur en croissance']
                    filtered_jobs.append(job)
                    if len(filtered_jobs) >= 5:
                        break

        # Trier par score de compatibilité
        filtered_jobs.sort(key=lambda x: x['compatibility_score'], reverse=True)

        return filtered_jobs

    def _calculate_career_weights(self, questionnaire: Dict) -> Dict[str, float]:
        """Calcule les poids selon les priorités carrière utilisateur"""
        all_criteria = self.get_specific_criteria()
        weights = {criterion: 1.0 for criterion in all_criteria}

        # Amplification selon les réponses
        for key, response in questionnaire.items():
            response_text = str(response).lower() if not isinstance(response, dict) else str(response.get('value', '')).lower()

            # Patterns de détection
            if any(word in response_text for word in ['salary', 'money', 'rémunération']):
                weights['salary_expectations'] *= 2.5
                weights['bonus_structure'] *= 2.0

            if any(word in response_text for word in ['remote', 'télétravail', 'flexibility']):
                weights['remote_work'] *= 2.5
                weights['flexible_hours'] *= 2.0

            if any(word in response_text for word in ['growth', 'career', 'évolution']):
                weights['career_growth'] *= 2.0
                weights['promotion_speed'] *= 1.8

            if any(word in response_text for word in ['startup', 'innovation', 'entrepreneur']):
                weights['startup_vs_corporate'] *= 2.0
                weights['innovation_level'] *= 1.8

        # Normalisation
        max_weight = max(weights.values()) if weights.values() else 1.0
        if max_weight > 1.0:
            weights = {k: v / max_weight for k, v in weights.items()}

        return weights

    def _analyze_skill_gaps(self, user_profile: Dict, job_recommendations: List[Dict]) -> List[str]:
        """Analyse les gaps de compétences pour les emplois recommandés"""
        # Compétences courantes supposées selon niveau
        current_skills = {
            'junior': ['Communication', 'Basic Analytics', 'Learning'],
            'intermediate': ['Project Management', 'Analytics', 'Leadership', 'Technical Skills'],
            'senior': ['Strategic Planning', 'Team Management', 'Expert Technical', 'Mentoring']
        }

        user_level = user_profile.get('experience_level', 'intermediate')
        user_skills = current_skills.get(user_level, [])

        # Identifier compétences manquantes
        required_skills = set()
        for job in job_recommendations[:3]:  # TOP 3 emplois
            required_skills.update(job.get('key_skills', []))

        # Gap analysis
        skill_gaps = []
        for skill in required_skills:
            if not any(existing_skill.lower() in skill.lower() for existing_skill in user_skills):
                skill_gaps.append(skill)

        return skill_gaps[:5]  # TOP 5 gaps

    def _recommend_training(self, skill_gaps: List[str]) -> List[Dict]:
        """Recommande des formations pour combler les gaps"""
        training_database = {
            'Python': {'provider': 'Coursera', 'duration': '3 mois', 'level': 'intermediate'},
            'Machine Learning': {'provider': 'edX', 'duration': '4 mois', 'level': 'advanced'},
            'Product Strategy': {'provider': 'Product School', 'duration': '2 mois', 'level': 'intermediate'},
            'Figma': {'provider': 'YouTube/Udemy', 'duration': '1 mois', 'level': 'beginner'},
            'Digital Marketing': {'provider': 'Google Skillshop', 'duration': '2 mois', 'level': 'intermediate'}
        }

        recommendations = []
        for skill in skill_gaps[:3]:
            if skill in training_database:
                training = training_database[skill].copy()
                training['skill'] = skill
                training['priority'] = 'high' if skill in ['Python', 'Machine Learning'] else 'medium'
                recommendations.append(training)

        return recommendations

    def _generate_match_reasons(self, job: Dict, user_profile: Dict) -> List[str]:
        """Génère les raisons de compatibilité emploi/profil"""
        reasons = []

        if job.get('sector') in user_profile.get('preferred_sectors', []):
            reasons.append(f"Secteur {job['sector']} correspond à vos intérêts")

        if job.get('remote_friendly') and 'flexibility' in user_profile.get('priorities', []):
            reasons.append("Télétravail possible")

        if job.get('experience_required') == user_profile.get('experience_level'):
            reasons.append("Niveau d'expérience parfait")

        if not reasons:
            reasons = ['Opportunité intéressante', 'Secteur en croissance']

        return reasons[:2]

    def _get_trending_skills(self, country: str) -> List[str]:
        """Retourne les compétences tendance par pays"""
        trending_by_country = {
            'france': ['Python', 'React', 'Data Analysis', 'Product Management'],
            'usa': ['AI/ML', 'Cloud Architecture', 'DevOps', 'Product Strategy'],
            'canada': ['Full-Stack Dev', 'Data Science', 'UX Design', 'Project Management']
        }

        return trending_by_country.get(country, ['Tech Skills', 'Analytics', 'Leadership'])

    def _get_salary_trends(self, country: str) -> Dict:
        """Retourne les tendances salariales par pays"""
        trends = {
            'france': {'growth': '+3%', 'hot_sectors': ['Tech', 'Finance'], 'avg_increase': '3-5%'},
            'usa': {'growth': '+5%', 'hot_sectors': ['AI/ML', 'Crypto'], 'avg_increase': '5-7%'},
            'canada': {'growth': '+4%', 'hot_sectors': ['Tech', 'Healthcare'], 'avg_increase': '4-6%'}
        }

        return trends.get(country, {'growth': '+3%', 'hot_sectors': ['Tech'], 'avg_increase': '3-5%'})

    def get_supported_sectors(self) -> List[str]:
        """Retourne la liste des secteurs supportés"""
        return list(self.supported_sectors.keys())

    def get_job_markets(self) -> List[str]:
        """Retourne la liste des marchés emploi supportés"""
        return list(self.job_markets.keys())

    def get_algorithm_info(self) -> Dict:
        """Informations détaillées sur l'algorithme SkillGraph"""
        base_stats = self.get_algorithm_stats()

        skillgraph_stats = {
            'supported_sectors': len(self.supported_sectors),
            'job_markets': len(self.job_markets),
            'career_criteria': len([c for c in self.get_specific_criteria() if c in ['salary_expectations', 'career_growth']]),
            'specialization': 'Career Intelligence & Skills Optimization'
        }

        return {**base_stats, **skillgraph_stats}
