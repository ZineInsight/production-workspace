from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import uvicorn
from pathlib import Path
import json
from datetime import datetime, timedelta
import random
import os

app = FastAPI(title="ZineInsight Portfolio Analytics", version="1.0.0")

# Configuration des chemins
BASE_DIR = Path(__file__).parent.parent  # Remonter au niveau portfolio/
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# Monter les fichiers statiques
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

@app.get("/")
async def homepage(request: Request):
    """Page d'accueil du portfolio analytics"""
    case_studies = [
        {
            "id": "finpay",
            "title": "FinPay SaaS",
            "subtitle": "Startup FinTech B2B",
            "challenge": "Réduire churn de 12% à 6%",
            "result": "✅ Objectif atteint en 8 mois",
            "icon": "🚀",
            "color": "primary"
        },
        {
            "id": "fashion",
            "title": "Fashion Lab", 
            "subtitle": "E-commerce Premium",
            "challenge": "Optimiser conversion mobile",
            "result": "📱 +127% conversion mobile",
            "icon": "🛒",
            "color": "success"
        },
        {
            "id": "techmarket",
            "title": "TechMarket",
            "subtitle": "Marketplace B2B",
            "challenge": "Augmenter take rate à 11%",
            "result": "📈 Take rate: 8% → 11.5%",
            "icon": "🏢",
            "color": "warning"
        }
    ]
    
    return templates.TemplateResponse("index.html", {
        "request": request,
        "case_studies": case_studies,
        "title": "Portfolio Analytics - ZineInsight"
    })

@app.get("/case/{case_id}")
async def case_study(case_id: str, request: Request):
    """Dashboard d'une étude de cas spécifique"""
    
    # Charger les données de l'étude de cas
    case_data = get_case_data(case_id)
    
    if not case_data:
        return templates.TemplateResponse("404.html", {"request": request}, status_code=404)
    
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "case_data": case_data,
        "case_id": case_id
    })

@app.get("/api/case/{case_id}/data")
async def get_case_api_data(case_id: str):
    """API pour récupérer les données d'un cas d'étude"""
    case_data = get_case_data(case_id)
    
    if not case_data:
        return JSONResponse({"error": "Case study not found"}, status_code=404)
    
    return JSONResponse(case_data["charts_data"])

def get_case_data(case_id: str):
    """Génère les données d'un cas d'étude"""
    
    if case_id == "finpay":
        return generate_finpay_data()
    elif case_id == "fashion":
        return generate_fashion_data()
    elif case_id == "techmarket":
        return generate_techmarket_data()
    else:
        return None

def generate_finpay_data():
    """Génère les données réalistes pour FinPay SaaS"""
    
    # Données MRR sur 18 mois avec croissance réaliste
    months = []
    mrr_data = []
    churn_data = []
    
    base_date = datetime(2023, 1, 1)
    base_mrr = 15000
    
    for i in range(18):
        current_date = base_date + timedelta(days=30*i)
        months.append(current_date.strftime("%Y-%m"))
        
        # MRR growth avec ralentissement naturel
        if i < 6:
            growth_rate = 0.18  # Croissance forte initiale
        elif i < 12:
            growth_rate = 0.12  # Ralentissement
        else:
            growth_rate = 0.08  # Maturité
            
        base_mrr *= (1 + growth_rate + random.uniform(-0.03, 0.03))
        mrr_data.append(int(base_mrr))
        
        # Churn rate amélioration progressive
        if i < 3:
            churn = 12.0 + random.uniform(-0.5, 0.5)
        elif i < 8:
            churn = 12.0 - (i-3) * 1.2 + random.uniform(-0.3, 0.3)  # Amélioration
        else:
            churn = 6.0 + random.uniform(-0.4, 0.4)  # Stabilisé
            
        churn_data.append(round(churn, 1))
    
    # Customer segments data
    segments_data = {
        "labels": ["Startups", "PME", "Enterprise"],
        "revenue": [25000, 42000, 18000],
        "churn": [8.2, 4.1, 2.8],
        "ltv": [890, 2400, 8500]
    }
    
    return {
        "title": "FinPay - Analyse Churn SaaS B2B",
        "description": "Startup FinTech proposant des solutions de paiement B2B. Challenge : réduire le churn de 12% à 6% pour améliorer la rentabilité.",
        "metrics": {
            "mrr_current": f"€{mrr_data[-1]:,}",
            "mrr_growth": "+467%",
            "churn_current": f"{churn_data[-1]}%",
            "churn_improvement": "-48%",
            "ltv_average": "€2,400",
            "customers": "342"
        },
        "insights": [
            "67% des churns provenaient des clients Basic <90 jours",
            "Les entreprises >50 employés ont 3x moins de churn",
            "Pic de churn en janvier lié aux budgets IT",
            "Plan Enterprise: churn 2.8% vs 8.2% Basic"
        ],
        "recommendations": [
            "Programme onboarding renforcé pour clients Basic",
            "Segmentation pricing selon taille entreprise",
            "Support proactif mois 1-3 pour nouveaux clients",
            "Incentives renouvellement fin d'année"
        ],
        "charts_data": {
            "mrr_evolution": {
                "labels": months,
                "data": mrr_data,
                "title": "Évolution MRR (Monthly Recurring Revenue)"
            },
            "churn_evolution": {
                "labels": months,
                "data": churn_data,
                "title": "Évolution Taux de Churn Mensuel"
            },
            "segments": segments_data
        }
    }

def generate_fashion_data():
    """Génère les données pour Fashion Lab e-commerce"""
    
    # Données conversion par device sur 12 mois
    months = []
    desktop_conversion = []
    mobile_conversion = []
    
    base_date = datetime(2023, 6, 1)
    
    for i in range(12):
        current_date = base_date + timedelta(days=30*i)
        months.append(current_date.strftime("%Y-%m"))
        
        # Desktop conversion stable
        desktop_conv = 3.4 + random.uniform(-0.2, 0.2)
        desktop_conversion.append(round(desktop_conv, 1))
        
        # Mobile conversion amélioration progressive
        if i < 3:
            mobile_conv = 1.2 + random.uniform(-0.1, 0.1)
        elif i < 8:
            mobile_conv = 1.2 + (i-3) * 0.52 + random.uniform(-0.1, 0.1)
        else:
            mobile_conv = 3.8 + random.uniform(-0.2, 0.2)
            
        mobile_conversion.append(round(mobile_conv, 1))
    
    return {
        "title": "Fashion Lab - Optimisation Mobile E-commerce",
        "description": "Brand fashion premium avec forte croissance. Challenge : conversion mobile 3x inférieure au desktop.",
        "metrics": {
            "conversion_mobile": "3.8%",
            "conversion_improvement": "+217%",
            "revenue_mobile": "€127K/mois",
            "mobile_traffic": "68%"
        },
        "charts_data": {
            "conversion_evolution": {
                "labels": months,
                "desktop": desktop_conversion,
                "mobile": mobile_conversion,
                "title": "Évolution Conversion par Device"
            }
        }
    }

def generate_techmarket_data():
    """Génère les données pour TechMarket B2B"""
    return {
        "title": "TechMarket - Optimisation Take Rate Marketplace",
        "description": "Marketplace B2B services tech. Challenge : augmenter take rate de 8% à 11% sans perdre de sellers.",
        "metrics": {
            "gmv_monthly": "€2.1M",
            "take_rate": "11.5%",
            "sellers_active": "1,247"
        },
        "charts_data": {}
    }

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8001))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
