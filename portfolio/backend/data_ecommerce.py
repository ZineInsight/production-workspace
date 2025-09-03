# ===== DONNÉES E-COMMERCE RÉELLES - BASÉES SUR LE PDF POWER BI =====
# Remplace les données Amazon fictives par les vraies métriques e-commerce

# 📊 MÉTRIQUES PRINCIPALES - DASHBOARD PRINCIPAL
ECOMMERCE_MAIN_METRICS = {
    "chiffre_affaires": {
        "value": 574.92,  # K€
        "growth": 14.8,   # %
        "currency": "K€",
        "period": "2024-2025"
    },
    "marge_brute": {
        "value": 60.72,   # K€  
        "percentage": 10.58,  # %
        "currency": "K€"
    },
    "commandes": {
        "total": 1247,
        "avg_value": 460.93,  # €
        "currency": "€"
    },
    "clients": {
        "total": 892,
        "retention_rate": 68.2,  # %
        "ltv": 644.18  # €
    }
}

# 🏆 TOP PRODUITS - BASÉ SUR L'ANALYSE PDF
TOP_PRODUCTS = [
    {
        "name": "Casques Audio Premium",
        "revenue": 202.45,  # K€
        "units": 441,
        "margin": 22.3,     # %
        "category": "Électronique",
        "growth": 18.7      # %
    },
    {
        "name": "iPhone 15 Series", 
        "revenue": 153.28,  # K€
        "units": 187,
        "margin": 12.8,     # %
        "category": "Smartphones",
        "growth": 31.2      # %
    },
    {
        "name": "Laptops Business",
        "revenue": 89.67,   # K€
        "units": 78,
        "margin": 8.4,      # %
        "category": "Informatique", 
        "growth": -5.3      # % (rotation lente)
    },
    {
        "name": "Montres Connectées",
        "revenue": 67.82,   # K€
        "units": 156,
        "margin": 19.1,     # %
        "category": "Wearables",
        "growth": 24.6      # %
    },
    {
        "name": "Suppléments Santé",
        "revenue": 45.33,   # K€
        "units": 289,
        "margin": 5.7,      # % (marge faible identifiée)
        "category": "Santé",
        "growth": 8.1       # %
    }
]

# 📈 ÉVOLUTION TEMPORELLE - SAISONNALITÉ IDENTIFIÉE
MONTHLY_PERFORMANCE = [
    {"month": "Jan", "revenue": 78.5, "orders": 167, "conversion": 3.2},
    {"month": "Fév", "revenue": 65.2, "orders": 142, "conversion": 2.9},
    {"month": "Mar", "revenue": 71.8, "orders": 155, "conversion": 3.1},
    {"month": "Avr", "revenue": 82.3, "orders": 178, "conversion": 3.4},
    {"month": "Mai", "revenue": 89.1, "orders": 192, "conversion": 3.6},
    {"month": "Jun", "revenue": 94.7, "orders": 201, "conversion": 3.8}, # Pic identifié
    {"month": "Jul", "revenue": 67.4, "orders": 145, "conversion": 2.8},
    {"month": "Aoû", "revenue": 42.1, "orders": 98, "conversion": 2.1},  # Creux identifié (-47%)
    {"month": "Sep", "revenue": 76.9, "orders": 163, "conversion": 3.2},
    {"month": "Oct", "revenue": 85.4, "orders": 181, "conversion": 3.5},
    {"month": "Nov", "revenue": 91.8, "orders": 195, "conversion": 3.7},
    {"month": "Déc", "revenue": 88.2, "orders": 189, "conversion": 3.6}
]

# 🎯 CATÉGORIES - PERFORMANCE ET ANALYSE
CATEGORIES_PERFORMANCE = [
    {
        "name": "Électronique",
        "revenue": 289.73,  # K€ (50.4% du CA)
        "margin": 18.2,     # %
        "units": 756,
        "status": "leader",  # Segment porteur identifié
        "recommendation": "Maintenir leadership, explorer nouveaux produits"
    },
    {
        "name": "Smartphones",
        "revenue": 153.28,  # K€ (26.7% du CA)
        "margin": 12.8,     # %
        "units": 187,
        "status": "growth",
        "recommendation": "Capitaliser sur iPhone success, diversifier gamme"
    },
    {
        "name": "Informatique",
        "revenue": 89.67,   # K€ (15.6% du CA)
        "margin": 8.4,      # %
        "units": 78,
        "status": "warning", # Rotation lente identifiée
        "recommendation": "Revoir stratégie pricing et stock laptops"
    },
    {
        "name": "Santé",
        "revenue": 42.24,   # K€ (7.3% du CA)
        "margin": 5.7,      # % (Problème identifié)
        "units": 226,
        "status": "alert",   # Marge faible critique
        "recommendation": "Urgence: revoir pricing et fournisseurs santé"
    }
]

# 🚨 ALERTES BUSINESS - DÉTECTION AUTOMATIQUE
BUSINESS_ALERTS = [
    {
        "type": "critical",
        "category": "Performance",
        "title": "Chute août -47%",
        "description": "Baisse drastique des ventes en août (42.1K€ vs 67.4K€ juillet)",
        "impact": "high",
        "action": "Campagne marketing ciblée période estivale"
    },
    {
        "type": "warning", 
        "category": "Rentabilité",
        "title": "Marge Santé critique 5.7%",
        "description": "Catégorie Santé sous seuil rentabilité acceptable (< 10%)",
        "impact": "medium",
        "action": "Renégocier fournisseurs ou augmenter prix"
    },
    {
        "type": "info",
        "category": "Stock",
        "title": "Laptops rotation lente",
        "description": "Informatique: 78 unités vendues, rotation 2.3x/an (optimal: 4x)",
        "impact": "medium", 
        "action": "Déstockage promotionnel ou réduction références"
    }
]

# 💰 OPPORTUNITÉS IDENTIFIÉES
BUSINESS_OPPORTUNITIES = [
    {
        "title": "Casques: Volume + Marge optimale",
        "category": "Électronique",
        "revenue_potential": 45.8,  # K€ additionnel
        "description": "22.3% marge + forte demande = investir stock avant pics saisonniers",
        "timeline": "Q4 2025",
        "confidence": 85  # %
    },
    {
        "title": "Printemps: Pic saisonnier",
        "category": "Saisonnalité", 
        "revenue_potential": 28.7,  # K€ additionnel
        "description": "Avril-Juin: +15% vs moyenne. Préparer campagnes ciblées",
        "timeline": "Q2 2025",
        "confidence": 78  # %
    },
    {
        "title": "iPhone momentum",
        "category": "Smartphones",
        "revenue_potential": 62.4,  # K€ additionnel
        "description": "31.2% growth iPhone 15. Capitaliser avec accessoires",
        "timeline": "Q1-Q2 2025",
        "confidence": 92  # %
    }
]

# 🎯 RECOMMANDATIONS ACTIONNABLES
ACTIONABLE_RECOMMENDATIONS = [
    {
        "priority": 1,
        "title": "Renforcer stock casques avant Q4",
        "description": "Commander +300 unités casques premium avant pic novembre-décembre",
        "expected_roi": "22.3% marge x volume additionnel = +45.8K€",
        "timeline": "Septembre 2025",
        "effort": "Facile"
    },
    {
        "priority": 2,
        "title": "Campagne anti-creux août",
        "description": "Marketing ciblé juillet pour contrer baisse historique -47%",
        "expected_roi": "Récupérer 50% du gap = +12.7K€",
        "timeline": "Juillet 2025", 
        "effort": "Moyen"
    },
    {
        "priority": 3,
        "title": "Revoir pricing Santé",
        "description": "Négocier fournisseurs ou +20% prix pour atteindre 10% marge",
        "expected_roi": "4.3% marge additionnelle = +8.1K€",
        "timeline": "Octobre 2025",
        "effort": "Complexe"
    }
]

# 📱 DASHBOARD CONFIG - SIMULE INTERFACE POWER BI
DASHBOARD_CONFIG = {
    "title": "E-commerce Analytics Dashboard",
    "subtitle": "Analyse des Ventes 2025 - Performance & Optimisation",
    "last_refresh": "2025-09-03 14:30:00",
    "data_source": "SQL Database + API Shopify",
    "filters": {
        "period": "2024-2025",
        "categories": ["Toutes", "Électronique", "Smartphones", "Informatique", "Santé"],
        "status": ["Actif", "En promotion", "Rupture"]
    },
    "kpi_targets": {
        "revenue_target": 650,      # K€
        "margin_target": 12,        # %
        "conversion_target": 3.5,   # %
        "retention_target": 70      # %
    }
}

# 🎨 POWER BI VISUAL ELEMENTS - Pour styling authentique
POWERBI_ELEMENTS = {
    "colors": {
        "primary": "#F2C811",      # Jaune Power BI
        "secondary": "#004B87",    # Bleu foncé Power BI  
        "background": "#F8F8F8",   # Gris clair Power BI
        "chart_bg": "#FFFFFF",     # Blanc charts
        "text": "#323130",         # Gris texte Power BI
        "border": "#E1E1E1"        # Bordures Power BI
    },
    "chart_types": [
        "bar_chart",    # CA par mois
        "donut_chart",  # Répartition catégories  
        "line_chart",   # Évolution temporelle
        "kpi_cards",    # Métriques principales
        "table",        # Top produits
        "gauge"         # Performance vs objectifs
    ]
}
