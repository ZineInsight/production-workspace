#!/usr/bin/env python3
"""
🎯 VALIDATION RAPIDE DONNÉES COURSE_GREEN
=========================================
Génère des échantillons CSV pour validation Power BI
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

class MockDataGenerator:
    def __init__(self):
        self.export_dir = "/var/www/production-workspace/bigquery-powerbi-prep/data/powerbi_exports"
        # Créer le dossier s'il n'existe pas
        import os
        os.makedirs(self.export_dir, exist_ok=True)

    def generate_sample_ecommerce_data(self):
        """Génère des données d'exemple réalistes basées sur la structure Course_green"""
        print("🏭 GÉNÉRATION DONNÉES ÉCHANTILLON COURSE_GREEN")
        print("=" * 60)
        
        # 1. Catégories (hiérarchie réaliste e-commerce)
        categories_data = {
            'categories_id': range(1, 16),
            'category_1': [
                'Électronique', 'Électronique', 'Électronique', 'Électronique',
                'Mode', 'Mode', 'Mode', 'Mode',
                'Maison', 'Maison', 'Maison',
                'Sport', 'Sport', 'Sport',
                'Santé'
            ],
            'category_2': [
                'Smartphones', 'Ordinateurs', 'Audio', 'Accessoires',
                'Vêtements Homme', 'Vêtements Femme', 'Chaussures', 'Accessoires Mode',
                'Cuisine', 'Décoration', 'Électroménager',
                'Fitness', 'Outdoor', 'Sports Collectifs',
                'Bien-être'
            ],
            'category_3': [
                'iPhone', 'Laptops', 'Casques', 'Cables',
                'T-shirts', 'Robes', 'Sneakers', 'Sacs',
                'Ustensiles', 'Coussins', 'Micro-ondes',
                'Yoga', 'Randonnée', 'Football',
                'Compléments'
            ]
        }
        
        categories_df = pd.DataFrame(categories_data)
        
        # 2. Produits (50 produits réalistes)
        products_data = []
        for i in range(1, 51):
            cat_idx = random.randint(0, 14)
            products_data.append({
                'products_id': i,
                'pdt_name': f"Produit {categories_data['category_3'][cat_idx]} {i:03d}",
                'categories_id': cat_idx + 1,
                'products_status': random.choice(['active', 'active', 'active', 'inactive']),
                'promo_id': random.choice([None, 1, 2, 3, 4])
            })
        
        products_df = pd.DataFrame(products_data)
        
        # 3. Prix (réalistes par catégorie)
        price_ranges = {
            'Électronique': (50, 1200),
            'Mode': (15, 250), 
            'Maison': (10, 400),
            'Sport': (20, 300),
            'Santé': (8, 80)
        }
        
        prices_data = []
        for _, product in products_df.iterrows():
            cat_id = product['categories_id']
            category = categories_df[categories_df['categories_id'] == cat_id]['category_1'].iloc[0]
            min_price, max_price = price_ranges[category]
            
            standard_price = round(random.uniform(min_price, max_price), 2)
            discount_price = round(standard_price * random.uniform(0.8, 1.0), 2)
            
            prices_data.append({
                'products_id': product['products_id'],
                'ps_cat': standard_price,
                'pd_cat': discount_price
            })
        
        prices_df = pd.DataFrame(prices_data)
        
        # 4. Ventes (données réalistes)
        sales_data = []
        active_products = products_df[products_df['products_status'] == 'active']['products_id'].tolist()
        
        for product_id in random.sample(active_products, min(35, len(active_products))):
            qty = random.randint(1, 100)
            sales_data.append({
                'pdt_id': product_id,
                'qty': qty
            })
        
        sales_df = pd.DataFrame(sales_data)
        
        # 5. Stocks
        stocks_data = []
        for product_id in products_df['products_id']:
            stock = random.randint(0, 500)
            stocks_data.append({
                'pdt_id': product_id,
                'stock': stock
            })
        
        stocks_df = pd.DataFrame(stocks_data)
        
        # 6. Promotions
        promos_data = {
            'promo_id': [1, 2, 3, 4],
            'promo_pourcent': [0.1, 0.15, 0.25, 0.3]
        }
        promos_df = pd.DataFrame(promos_data)
        
        # 7. Segments produits
        segments_data = []
        for product_id in products_df['products_id']:
            segment = random.choice(['Premium', 'Standard', 'Économique'])
            segments_data.append({
                'products_id': product_id,
                'pdt_segment': segment
            })
        
        segments_df = pd.DataFrame(segments_data)
        
        return {
            'categories': categories_df,
            'products': products_df,
            'prices': prices_df,
            'sales': sales_df,
            'stocks': stocks_df,
            'promos': promos_df,
            'segments': segments_df
        }

    def create_powerbi_ready_datasets(self):
        """Crée des datasets prêts pour Power BI"""
        print("\n📊 CRÉATION DATASETS POWER BI")
        print("=" * 40)
        
        # Générer les données
        data = self.generate_sample_ecommerce_data()
        
        # Dataset 1: Vue d'ensemble produits enrichie
        overview_df = (data['products']
                      .merge(data['categories'], on='categories_id', how='left')
                      .merge(data['prices'], on='products_id', how='left')
                      .merge(data['sales'], left_on='products_id', right_on='pdt_id', how='left')
                      .merge(data['stocks'], left_on='products_id', right_on='pdt_id', how='left')
                      .merge(data['segments'], on='products_id', how='left'))
        
        # Nettoyage
        overview_df['qty'] = overview_df['qty'].fillna(0)
        overview_df['stock'] = overview_df['stock'].fillna(0)
        
        # Calculs business
        overview_df['chiffre_affaires'] = overview_df['qty'] * overview_df['ps_cat']
        overview_df['marge_brute'] = overview_df['qty'] * (overview_df['ps_cat'] - overview_df['pd_cat'])
        overview_df['taux_remise'] = ((overview_df['ps_cat'] - overview_df['pd_cat']) / overview_df['ps_cat'] * 100).round(2)
        overview_df['statut_stock'] = overview_df['stock'].apply(
            lambda x: 'Rupture' if x == 0 else 'Faible' if x < 10 else 'Normal' if x < 100 else 'Élevé'
        )
        overview_df['performance'] = overview_df['qty'].apply(
            lambda x: 'Top' if x >= 50 else 'Bon' if x >= 20 else 'Moyen' if x > 0 else 'Aucune'
        )
        
        # Dataset 2: Analyse par catégorie
        category_analysis = (overview_df.groupby(['category_1', 'category_2', 'category_3'])
                           .agg({
                               'products_id': 'count',
                               'chiffre_affaires': 'sum',
                               'qty': 'sum',
                               'stock': 'sum',
                               'ps_cat': 'mean'
                           })
                           .round(2)
                           .reset_index())
        
        category_analysis.columns = ['Categorie_1', 'Categorie_2', 'Categorie_3', 
                                   'Nb_Produits', 'CA_Total', 'Qty_Totale', 'Stock_Total', 'Prix_Moyen']
        
        # Dataset 3: KPIs globaux
        kpis_data = {
            'Métrique': ['Produits Total', 'Produits Actifs', 'CA Total', 'Qty Totale Vendue', 
                        'Prix Moyen', 'Stock Total', 'Taux Activité'],
            'Valeur': [
                len(overview_df),
                len(overview_df[overview_df['qty'] > 0]),
                overview_df['chiffre_affaires'].sum(),
                overview_df['qty'].sum(),
                overview_df['ps_cat'].mean(),
                overview_df['stock'].sum(),
                len(overview_df[overview_df['qty'] > 0]) / len(overview_df) * 100
            ]
        }
        kpis_df = pd.DataFrame(kpis_data)
        kpis_df['Valeur'] = kpis_df['Valeur'].round(2)
        
        return {
            'overview': overview_df,
            'category_analysis': category_analysis,
            'kpis': kpis_df,
            'raw_data': data
        }

    def export_to_csv(self):
        """Export tous les datasets en CSV pour Power BI"""
        print("\n💾 EXPORT CSV POUR POWER BI")
        print("=" * 40)
        
        datasets = self.create_powerbi_ready_datasets()
        exported_files = []
        
        # Export dataset principal
        main_file = f"{self.export_dir}/course_green_overview.csv"
        datasets['overview'].to_csv(main_file, index=False, encoding='utf-8')
        exported_files.append(main_file)
        print(f"✅ Exporté: course_green_overview.csv ({len(datasets['overview'])} lignes)")
        
        # Export analyse catégories
        cat_file = f"{self.export_dir}/category_analysis.csv"
        datasets['category_analysis'].to_csv(cat_file, index=False, encoding='utf-8')
        exported_files.append(cat_file)
        print(f"✅ Exporté: category_analysis.csv ({len(datasets['category_analysis'])} lignes)")
        
        # Export KPIs
        kpi_file = f"{self.export_dir}/kpis_globaux.csv"
        datasets['kpis'].to_csv(kpi_file, index=False, encoding='utf-8')
        exported_files.append(kpi_file)
        print(f"✅ Exporté: kpis_globaux.csv ({len(datasets['kpis'])} lignes)")
        
        # Export tables de référence
        for name, df in datasets['raw_data'].items():
            ref_file = f"{self.export_dir}/ref_{name}.csv"
            df.to_csv(ref_file, index=False, encoding='utf-8')
            exported_files.append(ref_file)
            print(f"✅ Exporté: ref_{name}.csv ({len(df)} lignes)")
        
        return exported_files

    def generate_powerbi_instructions(self):
        """Génère les instructions Power BI"""
        print(f"\n📋 INSTRUCTIONS POWER BI")
        print("=" * 40)
        
        instructions = """
🎯 IMPORT DANS POWER BI:

1. 📂 Ouvrir Power BI Desktop
2. 📊 Obtenir des données > Fichier texte/CSV
3. 📁 Sélectionner: course_green_overview.csv (fichier principal)
4. ✅ Transformer les données si nécessaire
5. 🔄 Répéter pour les autres fichiers CSV

🏗️ RELATIONS RECOMMANDÉES:
• course_green_overview (table principale)
• category_analysis (pour drill-down catégories)
• kpis_globaux (pour cartes KPI)

📊 VISUALISATIONS SUGGÉRÉES:
• Carte: CA Total, Nb Produits
• Graphique en barres: Top produits par CA
• TreeMap: Répartition par catégories
• Scatter Plot: Prix vs Quantité
• Tableau: Détail produits avec filtres

🎨 DESIGN TIPS:
• Utiliser un thème cohérent
• Grouper les visuels par logique métier
• Ajouter des filtres interactifs
• Optimiser pour mobile
        """
        
        print(instructions)
        
        return instructions

def main():
    generator = MockDataGenerator()
    print("🎯 GÉNÉRATION DONNÉES ÉCHANTILLON COURSE_GREEN POUR POWER BI")
    print("=" * 70)
    
    # Export des données
    exported_files = generator.export_to_csv()
    
    # Instructions
    generator.generate_powerbi_instructions()
    
    print(f"\n🎉 GÉNÉRATION TERMINÉE!")
    print(f"📁 {len(exported_files)} fichiers créés dans: /var/www/production-workspace/bigquery-powerbi-prep/data/powerbi_exports/")
    
    print(f"\n🚀 PROCHAINES ÉTAPES:")
    print(f"1. Télécharger les CSV sur votre machine")
    print(f"2. Ouvrir Power BI Desktop")
    print(f"3. Importer les fichiers CSV")
    print(f"4. Créer votre dashboard de démo!")

if __name__ == "__main__":
    main()
