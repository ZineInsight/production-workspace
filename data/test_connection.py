"""
🧪 Test de connexion BigQuery
Vérifie que tout est bien configuré avant l'export complet
"""

from google.cloud import bigquery
import os
from dotenv import load_dotenv

load_dotenv()

def test_bigquery_connection():
    """Test rapide de connexion"""
    try:
        project_id = os.getenv('BIGQUERY_PROJECT_ID', 'versatile-vine-462408')
        client = bigquery.Client(project=project_id)

        # Test simple: lister les datasets
        datasets = list(client.list_datasets())

        print(f"✅ Connexion BigQuery réussie!")
        print(f"🏗️ Projet: {project_id}")
        print(f"📊 Datasets disponibles: {len(datasets)}")

        for dataset in datasets:
            print(f"  └── {dataset.dataset_id}")

        return True

    except Exception as e:
        print(f"❌ Erreur connexion: {e}")
        print("\n💡 Solutions possibles:")
        print("1. gcloud auth application-default login")
        print("2. Vérifier GOOGLE_APPLICATION_CREDENTIALS")
        print("3. Vérifier les permissions BigQuery")

        return False

if __name__ == "__main__":
    test_bigquery_connection()
