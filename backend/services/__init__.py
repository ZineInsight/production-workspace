"""
💼 SERVICES MÉTIER - REVOLUTIONARY BACKEND
==========================================
Modules de services spécialisés:
- ZScore: Intelligence géographique et lifestyle
- SkillGraph: Intelligence carrière et compétences
- Wealth: Intelligence financière et patrimoniale
"""

# Services disponibles
__services__ = {
    "zscore": {
        "name": "ZScore Intelligence",
        "description": "Analyse villes/pays optimaux selon profil utilisateur",
        "version": "2.0.0",
        "endpoints": ["/api/calculate", "/api/cities", "/api/countries"]
    },
    "skillgraph": {
        "name": "SkillGraph Intelligence",
        "description": "Optimisation carrière et développement compétences",
        "version": "1.0.0",
        "endpoints": ["/api/career", "/api/skills", "/api/jobs"]
    },
    "wealth": {
        "name": "Wealth Monitor Intelligence",
        "description": "Gestion patrimoine et optimisation financière",
        "version": "0.9.0",
        "endpoints": ["/api/wealth", "/api/portfolio", "/api/tax"]
    }
}

def get_service_info(service_name: str) -> dict:
    """Retourne les informations d'un service"""
    return __services__.get(service_name, {})
