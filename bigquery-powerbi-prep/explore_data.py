#!/usr/bin/env python3
"""
📊 Explorateur de données Course_green
=====================================
Script d'exploration et d'analyse du dataset Course_green
"""

import os
import pandas as pd
from google.cloud import bigquery
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

def explore_course_green_dataset():
    """Exploration complète du dataset Course_green"""

    # Configuration BigQuery
    project_id = os.getenv('PROJECT_ID')
    dataset_id = os.getenv('DATASET_ID')

    print("🌱 EXPLORATION DATASET COURSE_GREEN")
    print("=" * 50)
    print(f"📊 Projet: {project_id}")
    print(f"📁 Dataset: {dataset_id}")

    # Initialiser le client BigQuery
    client = bigquery.Client(project=project_id)

    # 1. Lister toutes les tables
    print("\n📋 TABLES DISPONIBLES:")
    print("-" * 30)

    dataset_ref = client.dataset(dataset_id)
    tables = list(client.list_tables(dataset_ref))

    table_info = {}
    for table in tables:
        table_ref = dataset_ref.table(table.table_id)
        table_obj = client.get_table(table_ref)

        print(f"📊 {table.table_id}")
        print(f"   📈 Lignes: {table_obj.num_rows:,}")
        print(f"   📋 Colonnes: {len(table_obj.schema)}")
        print(f"   📅 Créée: {table_obj.created.strftime('%Y-%m-%d')}")
        print(f"   💾 Taille: {table_obj.num_bytes / (1024*1024):.2f} MB")
        print()

        table_info[table.table_id] = {
            'rows': table_obj.num_rows,
            'columns': len(table_obj.schema),
            'schema': table_obj.schema,
            'created': table_obj.created
        }

    # 2. Explorer chaque table avec des échantillons
    print("\n🔍 APERÇU DES DONNÉES:")
    print("=" * 50)

    for table_name, info in table_info.items():
        print(f"\n📊 TABLE: {table_name}")
        print("-" * 30)

        # Afficher le schéma
        print("🏗️ STRUCTURE:")
        for field in info['schema'][:5]:  # Première 5 colonnes
            print(f"   • {field.name} ({field.field_type})")
        if len(info['schema']) > 5:
            print(f"   ... et {len(info['schema']) - 5} autres colonnes")

        # Échantillon de données
        query = f"""
        SELECT *
        FROM `{project_id}.{dataset_id}.{table_name}`
        LIMIT 3
        """

        try:
            df_sample = client.query(query).to_dataframe()
            print(f"\n📝 ÉCHANTILLON (3 premières lignes):")
            print(df_sample.to_string(index=False, max_cols=6))

            # Statistiques de base pour colonnes numériques
            numeric_cols = df_sample.select_dtypes(include=['int64', 'float64']).columns
            if len(numeric_cols) > 0:
                print(f"\n📈 STATISTIQUES NUMÉRIQUES:")
                print(df_sample[numeric_cols].describe().round(2))

        except Exception as e:
            print(f"⚠️ Erreur lors de l'échantillonnage: {e}")

        print("\n" + "="*50)

    return table_info

def analyze_green_categories():
    """Analyse spécifique de la table green_categories"""

    project_id = os.getenv('PROJECT_ID')
    dataset_id = os.getenv('DATASET_ID')
    client = bigquery.Client(project=project_id)

    print("\n🌿 ANALYSE DÉTAILLÉE: green_categories")
    print("=" * 50)

    # Requête d'analyse
    query = f"""
    SELECT
        COUNT(*) as total_categories,
        COUNT(DISTINCT category) as unique_categories,
        COUNT(DISTINCT subcategory) as unique_subcategories
    FROM `{project_id}.{dataset_id}.green_categories`
    """

    try:
        df = client.query(query).to_dataframe()
        print("📊 RÉSUMÉ GÉNÉRAL:")
        print(f"   • Total des entrées: {df['total_categories'].iloc[0]:,}")
        print(f"   • Catégories uniques: {df['unique_categories'].iloc[0]:,}")
        print(f"   • Sous-catégories uniques: {df['unique_subcategories'].iloc[0]:,}")

        # Top catégories
        query_top = f"""
        SELECT
            category,
            COUNT(*) as count
        FROM `{project_id}.{dataset_id}.green_categories`
        GROUP BY category
        ORDER BY count DESC
        LIMIT 10
        """

        df_top = client.query(query_top).to_dataframe()
        print(f"\n🏆 TOP 10 CATÉGORIES:")
        for idx, row in df_top.iterrows():
            print(f"   {idx+1}. {row['category']}: {row['count']:,}")

    except Exception as e:
        print(f"⚠️ Erreur lors de l'analyse: {e}")

if __name__ == "__main__":
    # Exploration complète
    table_info = explore_course_green_dataset()

    # Analyse spécialisée
    if 'green_categories' in table_info.keys():
        analyze_green_categories()

    print("\n✅ Exploration terminée !")
    print("\n💡 Prochaines étapes suggérées:")
    print("   1. Ouvrir le notebook Jupyter pour analyse interactive")
    print("   2. Créer des visualisations avec les données")
    print("   3. Identifier les insights clés pour votre site")
