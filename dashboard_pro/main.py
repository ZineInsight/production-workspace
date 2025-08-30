"""
🏢 DASHBOARD PROFESSIONNEL - FastAPI
===================================
Ultra-stable pour démos client - Otmane Boulahia
"""

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objects as go
import json
from datetime import datetime

app = FastAPI(title="📊 Analytics Pro Dashboard", version="1.0.0")

# Configuration des templates et fichiers statiques
templates = Jinja2Templates(directory="dashboard_pro/templates")
app.mount("/static", StaticFiles(directory="dashboard_pro/static"), name="static")

def load_data():
    """Charge et prépare les données"""
    try:
        sales_df = pd.read_csv('data/cleaned_datasets/sales_cleaned.csv')
        products_df = pd.read_csv('data/cleaned_datasets/products_cleaned.csv')

        sales_df['date_date'] = pd.to_datetime(sales_df['date_date'])

        # Enrichissement des données
        enriched = sales_df.merge(products_df, left_on='pdt_id', right_on='products_id', how='left')
        enriched['margin'] = enriched['revenue'] - (enriched['purchSE_PRICE'] * enriched['quantity'])
        enriched['margin_rate'] = (enriched['margin'] / enriched['revenue'] * 100).fillna(0)

        return enriched
    except Exception as e:
        print(f"Erreur chargement données: {e}")
        return pd.DataFrame()

@app.get("/")
async def dashboard(request: Request):
    """Page principale du dashboard"""
    df = load_data()

    if df.empty:
        return templates.TemplateResponse("error.html", {"request": request})

    # Calcul des KPIs
    total_revenue = float(df['revenue'].sum())
    total_orders = int(df['orders_id'].nunique())
    avg_basket = float(total_revenue / total_orders if total_orders > 0 else 0)
    margin_total = float(df['margin'].sum())
    margin_rate = float(margin_total / total_revenue * 100 if total_revenue > 0 else 0)

    kpis = {
        "revenue": f"{total_revenue:,.0f}€",
        "orders": f"{total_orders:,}",
        "avg_basket": f"{avg_basket:.2f}€",
        "margin_rate": f"{margin_rate:.1f}%"
    }

    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "kpis": kpis,
        "timestamp": datetime.now().strftime("%d/%m/%Y %H:%M")
    })

@app.get("/api/revenue-chart")
async def revenue_chart():
    """API pour le graphique de revenus"""
    df = load_data()

    if df.empty:
        return {"error": "Pas de données"}

    # Revenus mensuels
    monthly = df.groupby(df['date_date'].dt.to_period('M')).agg({
        'revenue': 'sum',
        'margin': 'sum'
    }).reset_index()
    monthly['date'] = monthly['date_date'].astype(str)
    monthly['margin_rate'] = monthly['margin'] / monthly['revenue'] * 100

    fig = go.Figure()
    fig.add_bar(x=monthly['date'], y=monthly['revenue'], name='Revenue €', yaxis='y')
    fig.add_scatter(x=monthly['date'], y=monthly['margin_rate'],
                   name='Marge %', yaxis='y2', mode='lines+markers')

    fig.update_layout(
        title="Évolution Revenue & Marge",
        yaxis=dict(title="Revenue €", side='left'),
        yaxis2=dict(title="Marge %", side='right', overlaying='y'),
        height=400,
        template="plotly_white"
    )

    return json.loads(fig.to_json())

@app.get("/api/top-products")
async def top_products():
    """API pour les top produits"""
    df = load_data()

    if df.empty:
        return {"error": "Pas de données"}

    products_metrics = df.groupby('pdt_id').agg({
        'revenue': 'sum',
        'quantity': 'sum',
        'margin': 'sum',
        'orders_id': 'nunique'
    }).round(2)

    top_products = products_metrics.sort_values('revenue', ascending=False).head(10)

    fig = px.bar(
        x=top_products['revenue'],
        y=top_products.index.astype(str),
        orientation='h',
        title="Top 10 Produits par Revenue",
        labels={'x': 'Revenue €', 'y': 'Produit ID'},
        template="plotly_white",
        height=400
    )
    fig.update_layout(yaxis={'categoryorder': 'total ascending'})

    return json.loads(fig.to_json())

@app.get("/api/abc-analysis")
async def abc_analysis():
    """API pour l'analyse ABC"""
    df = load_data()

    if df.empty:
        return {"error": "Pas de données"}

    products_metrics = df.groupby('pdt_id').agg({
        'revenue': 'sum'
    }).round(2)

    abc_df = products_metrics.sort_values('revenue', ascending=False).reset_index()
    abc_df['revenue_pct'] = abc_df['revenue'] / abc_df['revenue'].sum() * 100
    abc_df['cumulative_pct'] = abc_df['revenue_pct'].cumsum()

    fig = go.Figure()
    fig.add_scatter(
        x=list(range(1, len(abc_df) + 1)),
        y=abc_df['cumulative_pct'],
        mode='lines',
        name='% Cumulé Revenue',
        line=dict(color='blue', width=3)
    )
    fig.add_hline(y=80, line_dash="dash", line_color="red", annotation_text="80% - Classe A")
    fig.add_hline(y=95, line_dash="dash", line_color="orange", annotation_text="95% - Classe B")

    fig.update_layout(
        title="Courbe ABC - Concentration des Ventes",
        xaxis_title="Rang Produits",
        yaxis_title="% Cumulé Revenue",
        height=400,
        template="plotly_white"
    )

    return json.loads(fig.to_json())

@app.get("/health")
async def health_check():
    """Endpoint de santé du service"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
