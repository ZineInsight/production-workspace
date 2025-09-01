#!/usr/bin/env python3
"""
🔧 Test de connexion BigQuery
============================
Script simple pour vérifier que vos credentials fonctionnent
"""

import os
import sys
from dotenv import load_dotenv

def test_bigquery_connection():
    """Test simple de la connexion BigQuery"""

    # Charger les variables d'environnement
    load_dotenv()

    print("🔍 Test de connexion BigQuery")
    print("=" * 40)

    # Vérifier les variables d'environnement
    project_id = os.getenv('PROJECT_ID')
    dataset_id = os.getenv('DATASET_ID')

    print(f"📋 PROJECT_ID: {project_id}")
    print(f"📋 DATASET_ID: {dataset_id}")

    if not project_id:
        print("❌ PROJECT_ID manquant dans le fichier .env")
        return False

    try:
        from google.cloud import bigquery

        # Initialiser le client BigQuery
        print("\n🔌 Initialisation du client BigQuery...")
        client = bigquery.Client(project=project_id)

        # Test simple : lister les datasets
        print("📊 Test : Liste des datasets disponibles...")
        datasets = list(client.list_datasets())

        if datasets:
            print(f"✅ Connexion réussie ! Datasets trouvés : {len(datasets)}")
            for dataset in datasets[:5]:  # Afficher les 5 premiers
                print(f"   📁 {dataset.dataset_id}")
        else:
            print("⚠️ Connexion OK mais aucun dataset trouvé")

        # Test spécifique sur votre dataset si spécifié
        if dataset_id:
            print(f"\n🔍 Test spécifique sur le dataset : {dataset_id}")
            try:
                dataset_ref = client.dataset(dataset_id)
                tables = list(client.list_tables(dataset_ref))
                print(f"✅ Dataset '{dataset_id}' accessible avec {len(tables)} tables")

                for table in tables[:3]:  # Afficher les 3 premières tables
                    print(f"   📋 {table.table_id}")

            except Exception as e:
                print(f"⚠️ Dataset '{dataset_id}' non accessible : {e}")

        return True

    except Exception as e:
        print(f"❌ Erreur de connexion BigQuery : {e}")
        print("\n💡 Vérifiez :")
        print("  - Vos credentials dans .env")
        print("  - Que l'API BigQuery est activée")
        print("  - Les permissions de votre service account")
        return False

if __name__ == "__main__":
    success = test_bigquery_connection()
    sys.exit(0 if success else 1)
