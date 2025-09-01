#!/usr/bin/env python3
"""
🚀 EXPORT OPTIMISÉ POUR POWER BI
================================
Génère des fichiers CSV parfaits pour Power BI depuis BigQuery
"""

import os
import pandas as pd
from google.cloud import bigquery
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

class PowerBIExporter:
    def __init__(self):
        self.project_id = "versatile-vine-462408-g0"
        self.dataset_id = "Course_green"
        self.client = bigquery.Client(project=self.project_id)
        self.export_dir = "/var/www/production-workspace/bigquery-analysis/data/powerbi_exports"

        # Créer le dossier d'export
        os.makedirs(self.export_dir, exist_ok=True)

    def export_category_revenue_analysis(self):
        """Export CA par catégorie - Perfect pour Power BI"""
        print("📊 Export analyse CA par catégorie...")

        query = f"""
        SELECT
            c.category_1 as Categorie,
            c.category_2 as SousCategorie,
            COUNT(DISTINCT p.products_id) as NombreProduits,
            SUM(COALESCE(s.qty, 0)) as QuantiteVendue,
            SUM(CASE
                WHEN pr.ps_cat > 0 THEN COALESCE(s.qty, 0) * pr.ps_cat
                ELSE 0
            END) as ChiffreAffaires,
            AVG(pr.ps_cat) as PrixMoyen,
            COUNT(CASE WHEN COALESCE(s.qty, 0) > 0 THEN 1 END) as ProduitsActifs,
            SUM(COALESCE(st.stock, 0)) as StockTotal
        FROM `{self.project_id}.{self.dataset_id}.green_product` p
        LEFT JOIN `{self.project_id}.{self.dataset_id}.green_categories` c
            ON p.categories_id = c.categories_id
        LEFT JOIN `{self.project_id}.{self.dataset_id}.green_price` pr
            ON p.products_id = pr.products_id
        LEFT JOIN `{self.project_id}.{self.dataset_id}.green_sales` s
            ON p.products_id = s.pdt_id
        LEFT JOIN `{self.project_id}.{self.dataset_id}.green_stock` st
            ON p.products_id = st.pdt_id
        WHERE c.category_1 IS NOT NULL
        GROUP BY c.category_1, c.category_2
        ORDER BY ChiffreAffaires DESC
        """

        df = self.client.query(query).to_dataframe()

        # Formatage pour Power BI
        df['PourcentageCA'] = (df['ChiffreAffaires'] / df['ChiffreAffaires'].sum() * 100).round(2)
        df['TauxActivation'] = (df['ProduitsActifs'] / df['NombreProduits'] * 100).round(2)

        filepath = f"{self.export_dir}/category_revenue_analysis.csv"
        df.to_csv(filepath, index=False, encoding='utf-8')
        print(f"✅ Exporté : {filepath}")
        return filepath

    def export_product_performance(self):
        """Export détail produits - Perfect pour Power BI"""
        print("📦 Export performance produits...")

        query = f"""
        SELECT
            p.products_id as ProductID,
            p.pdt_name as NomProduit,
            c.category_1 as Categorie,
            c.category_2 as SousCategorie,
            pr.ps_cat as PrixStandard,
            pr.pd_cat as PrixDiscount,
            COALESCE(s.qty, 0) as QuantiteVendue,
            CASE
                WHEN pr.ps_cat > 0 THEN COALESCE(s.qty, 0) * pr.ps_cat
                ELSE 0
            END as ChiffreAffaires,
            COALESCE(st.stock, 0) as Stock,
            CASE
                WHEN pr.ps_cat != pr.pd_cat THEN
                    ROUND((pr.ps_cat - pr.pd_cat) / pr.ps_cat * 100, 2)
                ELSE 0
            END as PourcentageRemise,
            CASE
                WHEN COALESCE(s.qty, 0) > 0 THEN 'Vendeur'
                WHEN COALESCE(st.stock, 0) > 0 THEN 'En Stock'
                ELSE 'Dormant'
            END as Statut,
            CASE
                WHEN pr.ps_cat >= 50 THEN 'Premium'
                WHEN pr.ps_cat >= 10 THEN 'Standard'
                ELSE 'Accessible'
            END as GammePrix
        FROM `{self.project_id}.{self.dataset_id}.green_product` p
        LEFT JOIN `{self.project_id}.{self.dataset_id}.green_categories` c
            ON p.categories_id = c.categories_id
        LEFT JOIN `{self.project_id}.{self.dataset_id}.green_price` pr
            ON p.products_id = pr.products_id
        LEFT JOIN `{self.project_id}.{self.dataset_id}.green_sales` s
            ON p.products_id = s.pdt_id
        LEFT JOIN `{self.project_id}.{self.dataset_id}.green_stock` st
            ON p.products_id = st.pdt_id
        WHERE c.category_1 IS NOT NULL
        ORDER BY ChiffreAffaires DESC
        """

        df = self.client.query(query).to_dataframe()

        filepath = f"{self.export_dir}/product_performance.csv"
        df.to_csv(filepath, index=False, encoding='utf-8')
        print(f"✅ Exporté : {filepath}")
        return filepath

    def export_kpis_summary(self):
        """Export KPIs globaux - Perfect pour Power BI"""
        print("📈 Export KPIs globaux...")

        query = f"""
        SELECT
            'Course Green' as Dataset,
            COUNT(DISTINCT p.products_id) as TotalProduits,
            COUNT(DISTINCT CASE WHEN COALESCE(s.qty, 0) > 0 THEN p.products_id END) as ProduitsActifs,
            COUNT(DISTINCT c.category_1) as NombreCategories,
            SUM(CASE
                WHEN pr.ps_cat > 0 THEN COALESCE(s.qty, 0) * pr.ps_cat
                ELSE 0
            END) as ChiffreAffairesTotal,
            SUM(COALESCE(s.qty, 0)) as QuantiteTotaleVendue,
            AVG(pr.ps_cat) as PrixMoyenCatalogue,
            SUM(COALESCE(st.stock, 0)) as StockTotalValue,
            CURRENT_DATE() as DateMiseAJour
        FROM `{self.project_id}.{self.dataset_id}.green_product` p
        LEFT JOIN `{self.project_id}.{self.dataset_id}.green_categories` c
            ON p.categories_id = c.categories_id
        LEFT JOIN `{self.project_id}.{self.dataset_id}.green_price` pr
            ON p.products_id = pr.products_id
        LEFT JOIN `{self.project_id}.{self.dataset_id}.green_sales` s
            ON p.products_id = s.pdt_id
        LEFT JOIN `{self.project_id}.{self.dataset_id}.green_stock` st
            ON p.products_id = st.pdt_id
        """

        df = self.client.query(query).to_dataframe()

        # Calculs additionnels
        df['TauxActivationGlobal'] = (df['ProduitsActifs'] / df['TotalProduits'] * 100).round(2)
        df['CAMoyenParProduitActif'] = (df['ChiffreAffairesTotal'] / df['ProduitsActifs']).round(2)

        filepath = f"{self.export_dir}/kpis_summary.csv"
        df.to_csv(filepath, index=False, encoding='utf-8')
        print(f"✅ Exporté : {filepath}")
        return filepath

    def export_all(self):
        """Export complet pour Power BI"""
        print("🚀 EXPORT COMPLET POUR POWER BI")
        print("=" * 50)

        exports = []
        exports.append(self.export_category_revenue_analysis())
        exports.append(self.export_product_performance())
        exports.append(self.export_kpis_summary())

        print(f"\n🎉 Export terminé ! {len(exports)} fichiers générés :")
        for filepath in exports:
            print(f"📂 {filepath}")

        print(f"\n💡 Pour Power BI :")
        print(f"1. Téléchargez ces CSV sur votre Mac")
        print(f"2. Importez-les dans Power BI Service")
        print(f"3. Créez vos graphiques en drag & drop !")

        return exports

def main():
    """Fonction principale"""
    exporter = PowerBIExporter()
    exporter.export_all()

if __name__ == "__main__":
    main()
