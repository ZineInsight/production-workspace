#!/usr/bin/env python3
"""
📊 ANALYSE PROFESSIONNELLE DATASET COURSE_GREEN
==============================================
Exploration approfondie et analyse métier du dataset e-commerce
"""

import os
import pandas as pd
import numpy as np
from google.cloud import bigquery
from dotenv import load_dotenv
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Charger les variables d'environnement
load_dotenv()

class CourseGreenBusinessAnalyst:
    def __init__(self):
        self.project_id = "versatile-vine-462408-g0"
        self.dataset_id = "Course_green"
        self.client = bigquery.Client(project=self.project_id)

    def get_data_overview(self):
        """Vue d'ensemble complète des données"""
        print("📊 ANALYSE DATASET COURSE_GREEN - VUE D'ENSEMBLE")
        print("=" * 60)

        # Informations sur toutes les tables
        dataset_ref = self.client.dataset(self.dataset_id)
        tables = list(self.client.list_tables(dataset_ref))

        overview = {}
        for table in tables:
            table_ref = dataset_ref.table(table.table_id)
            table_obj = self.client.get_table(table_ref)

            overview[table.table_id] = {
                'rows': table_obj.num_rows,
                'columns': len(table_obj.schema),
                'size_mb': round(table_obj.num_bytes / (1024*1024), 3),
                'created': table_obj.created.strftime('%Y-%m-%d'),
                'schema': [(field.name, field.field_type) for field in table_obj.schema]
            }

        # Affichage structuré
        for table_name, info in overview.items():
            print(f"\n🗂️ TABLE: {table_name}")
            print(f"   📊 Lignes: {info['rows']:,}")
            print(f"   📋 Colonnes: {info['columns']}")
            print(f"   💾 Taille: {info['size_mb']} MB")
            print(f"   📅 Créée: {info['created']}")
            print(f"   🏗️ Schéma: {', '.join([f'{name}({type})' for name, type in info['schema']])}")

        return overview

    def analyze_data_quality(self):
        """Analyse de la qualité des données"""
        print(f"\n📈 ANALYSE QUALITÉ DONNÉES")
        print("=" * 40)

        # Analyse des catégories
        categories_query = f"""
        SELECT
            COUNT(*) as total_categories,
            COUNT(DISTINCT category_1) as unique_cat1,
            COUNT(DISTINCT category_2) as unique_cat2,
            COUNT(DISTINCT category_3) as unique_cat3,
            COUNT(CASE WHEN category_1 IS NULL OR category_1 = '' THEN 1 END) as null_cat1,
            COUNT(CASE WHEN category_2 IS NULL OR category_2 = '' THEN 1 END) as null_cat2,
            COUNT(CASE WHEN category_3 IS NULL OR category_3 = '' THEN 1 END) as null_cat3
        FROM `{self.project_id}.{self.dataset_id}.green_categories`
        """

        cat_quality = self.client.query(categories_query).to_dataframe()

        print("🏷️ QUALITÉ CATÉGORIES:")
        for col, val in cat_quality.iloc[0].items():
            print(f"   • {col}: {val}")

        # Analyse des produits
        products_query = f"""
        SELECT
            COUNT(*) as total_products,
            COUNT(CASE WHEN pdt_name IS NULL OR pdt_name = '' THEN 1 END) as null_names,
            COUNT(DISTINCT products_status) as status_types,
            COUNT(CASE WHEN categories_id IS NULL THEN 1 END) as null_categories,
            COUNT(CASE WHEN promo_id IS NULL THEN 1 END) as null_promos
        FROM `{self.project_id}.{self.dataset_id}.green_product`
        """

        prod_quality = self.client.query(products_query).to_dataframe()

        print("\n📦 QUALITÉ PRODUITS:")
        for col, val in prod_quality.iloc[0].items():
            print(f"   • {col}: {val}")

        # Analyse des ventes
        sales_query = f"""
        SELECT
            COUNT(*) as total_sales,
            SUM(qty) as total_quantity,
            AVG(qty) as avg_quantity,
            MIN(qty) as min_quantity,
            MAX(qty) as max_quantity,
            COUNT(DISTINCT pdt_id) as unique_products_sold
        FROM `{self.project_id}.{self.dataset_id}.green_sales`
        """

        sales_quality = self.client.query(sales_query).to_dataframe()

        print("\n💰 QUALITÉ VENTES:")
        for col, val in sales_quality.iloc[0].items():
            if isinstance(val, float):
                print(f"   • {col}: {val:.2f}")
            else:
                print(f"   • {col}: {val}")

    def analyze_business_segments(self):
        """Analyse des segments métier"""
        print(f"\n🎯 ANALYSE SEGMENTS MÉTIER")
        print("=" * 40)

        # Top catégories niveau 1
        cat1_query = f"""
        SELECT
            category_1,
            COUNT(*) as nb_products,
            ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) as percentage
        FROM `{self.project_id}.{self.dataset_id}.green_categories`
        WHERE category_1 IS NOT NULL AND category_1 != ''
        GROUP BY category_1
        ORDER BY nb_products DESC
        """

        cat1_data = self.client.query(cat1_query).to_dataframe()

        print("🏷️ TOP CATÉGORIES NIVEAU 1:")
        for idx, row in cat1_data.head(10).iterrows():
            print(f"   {idx+1}. {row['category_1']}: {row['nb_products']} produits ({row['percentage']}%)")

        # Analyse des segments produits
        segments_query = f"""
        SELECT
            pdt_segment,
            COUNT(*) as nb_products,
            ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) as percentage
        FROM `{self.project_id}.{self.dataset_id}.green_pdt_segment`
        WHERE pdt_segment IS NOT NULL
        GROUP BY pdt_segment
        ORDER BY nb_products DESC
        """

        segments_data = self.client.query(segments_query).to_dataframe()

        print(f"\n📊 SEGMENTS PRODUITS:")
        for idx, row in segments_data.iterrows():
            print(f"   • Segment {row['pdt_segment']}: {row['nb_products']} produits ({row['percentage']}%)")

    def analyze_pricing_strategy(self):
        """Analyse de la stratégie pricing"""
        print(f"\n💰 ANALYSE STRATÉGIE PRICING")
        print("=" * 40)

        # Analyse des prix
        pricing_query = f"""
        SELECT
            COUNT(*) as total_prices,
            AVG(ps_cat) as avg_standard_price,
            AVG(pd_cat) as avg_discount_price,
            MIN(ps_cat) as min_price,
            MAX(ps_cat) as max_price,
            STDDEV(ps_cat) as std_price,
            COUNT(CASE WHEN ps_cat != pd_cat THEN 1 END) as products_with_discount
        FROM `{self.project_id}.{self.dataset_id}.green_price`
        WHERE ps_cat IS NOT NULL AND pd_cat IS NOT NULL
        """

        pricing_data = self.client.query(pricing_query).to_dataframe().iloc[0]

        print("💵 STATISTIQUES PRICING:")
        print(f"   • Prix moyen standard: {pricing_data['avg_standard_price']:.2f}€")
        print(f"   • Prix moyen remisé: {pricing_data['avg_discount_price']:.2f}€")
        print(f"   • Fourchette prix: {pricing_data['min_price']:.2f}€ - {pricing_data['max_price']:.2f}€")
        print(f"   • Écart-type: {pricing_data['std_price']:.2f}€")
        print(f"   • Produits avec remise: {pricing_data['products_with_discount']}")

        # Analyse par segment
        segment_pricing_query = f"""
        SELECT
            s.pdt_segment,
            COUNT(*) as nb_products,
            AVG(p.ps_cat) as avg_price,
            MIN(p.ps_cat) as min_price,
            MAX(p.ps_cat) as max_price
        FROM `{self.project_id}.{self.dataset_id}.green_price` p
        JOIN `{self.project_id}.{self.dataset_id}.green_pdt_segment` s ON p.products_id = s.products_id
        WHERE p.ps_cat IS NOT NULL
        GROUP BY s.pdt_segment
        ORDER BY avg_price DESC
        """

        segment_pricing = self.client.query(segment_pricing_query).to_dataframe()

        print(f"\n📊 PRICING PAR SEGMENT:")
        for idx, row in segment_pricing.iterrows():
            print(f"   • Segment {row['pdt_segment']}: {row['avg_price']:.2f}€ moyen ({row['nb_products']} produits)")

    def analyze_sales_performance(self):
        """Analyse de la performance des ventes"""
        print(f"\n📈 ANALYSE PERFORMANCE VENTES")
        print("=" * 40)

        # Top produits vendus
        top_sales_query = f"""
        SELECT
            p.pdt_name,
            s.qty,
            c.category_1,
            seg.pdt_segment,
            pr.ps_cat as price,
            (s.qty * pr.ps_cat) as revenue_estimate
        FROM `{self.project_id}.{self.dataset_id}.green_sales` s
        JOIN `{self.project_id}.{self.dataset_id}.green_product` p ON s.pdt_id = p.products_id
        LEFT JOIN `{self.project_id}.{self.dataset_id}.green_categories` c ON p.categories_id = c.categories_id
        LEFT JOIN `{self.project_id}.{self.dataset_id}.green_pdt_segment` seg ON p.products_id = seg.products_id
        LEFT JOIN `{self.project_id}.{self.dataset_id}.green_price` pr ON p.products_id = pr.products_id
        WHERE s.qty IS NOT NULL
        ORDER BY s.qty DESC
        LIMIT 10
        """

        top_sales = self.client.query(top_sales_query).to_dataframe()

        print("🏆 TOP 10 VENTES:")
        for idx, row in top_sales.iterrows():
            revenue = row['revenue_estimate'] if pd.notna(row['revenue_estimate']) else 0
            print(f"   {idx+1}. {row['pdt_name'][:50]}...")
            print(f"      Qty: {row['qty']}, Prix: {row['price']:.2f}€, CA estimé: {revenue:.2f}€")

        # Performance par catégorie
        category_sales_query = f"""
        SELECT
            c.category_1,
            COUNT(DISTINCT s.pdt_id) as nb_products_sold,
            SUM(s.qty) as total_quantity,
            AVG(s.qty) as avg_quantity_per_product
        FROM `{self.project_id}.{self.dataset_id}.green_sales` s
        JOIN `{self.project_id}.{self.dataset_id}.green_product` p ON s.pdt_id = p.products_id
        JOIN `{self.project_id}.{self.dataset_id}.green_categories` c ON p.categories_id = c.categories_id
        WHERE c.category_1 IS NOT NULL
        GROUP BY c.category_1
        ORDER BY total_quantity DESC
        LIMIT 10
        """

        cat_sales = self.client.query(category_sales_query).to_dataframe()

        print(f"\n📊 PERFORMANCE PAR CATÉGORIE:")
        for idx, row in cat_sales.iterrows():
            print(f"   {idx+1}. {row['category_1']}: {row['total_quantity']} unités vendues")
            print(f"      ({row['nb_products_sold']} produits, {row['avg_quantity_per_product']:.1f} moy/produit)")

    def analyze_promotions_impact(self):
        """Analyse de l'impact des promotions"""
        print(f"\n🎯 ANALYSE IMPACT PROMOTIONS")
        print("=" * 40)

        # Statut des promotions
        promo_status_query = f"""
        SELECT
            CASE
                WHEN promo_pourcent = 0 THEN 'Inactive'
                WHEN promo_pourcent <= 0.10 THEN 'Faible (≤10%)'
                WHEN promo_pourcent <= 0.25 THEN 'Modérée (11-25%)'
                ELSE 'Forte (>25%)'
            END as promo_type,
            COUNT(*) as nb_promos,
            AVG(promo_pourcent) as avg_discount,
            MIN(promo_pourcent) as min_discount,
            MAX(promo_pourcent) as max_discount
        FROM `{self.project_id}.{self.dataset_id}.green_promo`
        GROUP BY 1
        ORDER BY avg_discount DESC
        """

        promo_analysis = self.client.query(promo_status_query).to_dataframe()

        print("🎁 RÉPARTITION PROMOTIONS:")
        for idx, row in promo_analysis.iterrows():
            print(f"   • {row['promo_type']}: {row['nb_promos']} promos")
            print(f"     Remise moyenne: {row['avg_discount']*100:.1f}%")

    def generate_business_recommendations(self):
        """Génération de recommandations business"""
        print(f"\n💡 RECOMMANDATIONS BUSINESS")
        print("=" * 40)

        print("🎯 AXES D'AMÉLIORATION IDENTIFIÉS:")
        print("   1. Harmoniser la classification des catégories")
        print("   2. Optimiser la stratégie pricing par segment")
        print("   3. Améliorer le tracking des promotions")
        print("   4. Développer l'analyse de cohorts clients")
        print("   5. Créer des KPIs de performance produits")

        print(f"\n📊 MÉTRIQUES CLÉS À SUIVRE:")
        print("   • Taux de conversion par catégorie")
        print("   • Panier moyen par segment")
        print("   • ROI des promotions")
        print("   • Rotation des stocks")
        print("   • Marge par produit")

    def run_complete_analysis(self):
        """Lance l'analyse complète"""
        print("🚀 DÉMARRAGE ANALYSE PROFESSIONNELLE")
        print("=" * 60)

        # Vue d'ensemble
        self.get_data_overview()

        # Qualité des données
        self.analyze_data_quality()

        # Segments métier
        self.analyze_business_segments()

        # Stratégie pricing
        self.analyze_pricing_strategy()

        # Performance ventes
        self.analyze_sales_performance()

        # Impact promotions
        self.analyze_promotions_impact()

        # Recommandations
        self.generate_business_recommendations()

        print(f"\n✅ ANALYSE TERMINÉE - {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print("=" * 60)

def main():
    """Fonction principale"""
    analyst = CourseGreenBusinessAnalyst()
    analyst.run_complete_analysis()

if __name__ == "__main__":
    main()
