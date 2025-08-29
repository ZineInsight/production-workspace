"""
🚀 BIGQUERY DATA EXPORTER - VERSION PRO
=======================================
Script technique pour exporter données BigQuery vers analytics portfolio
Otmane - Data Engineer - zineinsight.com
"""

from google.cloud import bigquery
import pandas as pd
import os
import json
from pathlib import Path
from dotenv import load_dotenv
from datetime import datetime

# Charger variables d'environnement
load_dotenv()

class BigQueryExporter:
    """Classe professionnelle pour export BigQuery"""

    def __init__(self, project_id=None):
        self.project_id = project_id or os.getenv('BIGQUERY_PROJECT_ID')
        self.client = None
        self.setup_client()

    def setup_client(self):
        """Configure le client BigQuery avec authentification"""
        try:
            # Authentification via service account ou défaut
            self.client = bigquery.Client(project=self.project_id)
            print(f"✅ Connexion BigQuery réussie - Projet: {self.project_id}")
        except Exception as e:
            print(f"❌ Erreur connexion BigQuery: {e}")
            print("💡 Assurez-vous d'avoir configuré l'authentification Google Cloud")

    def explore_dataset(self, dataset_id):
        """Explore un dataset pour lister les tables disponibles"""
        try:
            dataset_ref = self.client.dataset(dataset_id)
            tables = list(self.client.list_tables(dataset_ref))

            print(f"\n📊 DATASET: {dataset_id}")
            print(f"📈 Tables disponibles: {len(tables)}")

            for table in tables:
                # Récupérer les infos détaillées de la table
                table_ref = self.client.get_table(table)
                print(f"  └── {table.table_id} ({table_ref.num_rows} lignes)")

            return [table.table_id for table in tables]
        except Exception as e:
            print(f"❌ Erreur exploration dataset: {e}")
            return []

    def export_table_to_csv(self, table_id, output_file, limit=10000, sample=False):
        """Exporte une table BigQuery vers CSV avec options avancées"""

        # Requête avec échantillonnage optionnel
        if sample:
            query = f"""
            SELECT *
            FROM `{self.project_id}.{table_id}`
            TABLESAMPLE SYSTEM (10 PERCENT)
            LIMIT {limit}
            """
        else:
            query = f"""
            SELECT *
            FROM `{self.project_id}.{table_id}`
            LIMIT {limit}
            """

        print(f"📊 Export de {table_id}...")
        print(f"🔍 Requête: {query[:100]}...")

        try:
            # Exécuter la requête et convertir en DataFrame
            df = self.client.query(query).to_dataframe()

            # Créer le répertoire si nécessaire
            Path(output_file).parent.mkdir(parents=True, exist_ok=True)

            # Sauvegarder en CSV
            df.to_csv(output_file, index=False)

            # Métadonnées
            metadata = {
                'table_id': table_id,
                'export_date': datetime.now().isoformat(),
                'rows': len(df),
                'columns': len(df.columns),
                'file_size_mb': round(os.path.getsize(output_file) / 1024 / 1024, 2)
            }

            # Sauvegarder métadonnées
            meta_file = output_file.replace('.csv', '_metadata.json')
            with open(meta_file, 'w') as f:
                json.dump(metadata, f, indent=2)

            print(f"✅ Export réussi: {output_file}")
            print(f"📈 {len(df)} lignes, {len(df.columns)} colonnes")
            print(f"💾 Taille: {metadata['file_size_mb']} MB")

            return df, metadata

        except Exception as e:
            print(f"❌ Erreur export {table_id}: {e}")
            return None, None

def main():
    """Script principal d'export"""
    print("🚀 BIGQUERY PORTFOLIO EXPORTER")
    print("=" * 50)

    # Initialiser l'exporteur
    exporter = BigQueryExporter()

    if not exporter.client:
        print("❌ Impossible de se connecter à BigQuery")
        return

    # Explorer le dataset
    dataset_id = os.getenv('BIGQUERY_DATASET_ID', 'gz_raw_data')
    tables = exporter.explore_dataset(dataset_id)

    if not tables:
        print("⚠️ Aucune table trouvée")
        return

    # Tables à exporter pour portfolio
    priority_tables = [
        'raw_gz_sales',      # E-commerce (1.3M lignes!)
        'raw_gz_product',    # Catalogue (16K)
        'raw_gz_facebook',   # Marketing (1K)
    ]

    print(f"\n🎯 EXPORT POUR PORTFOLIO ANALYTICS")
    print(f"📊 Tables prioritaires: {len(priority_tables)}")

    exported_data = {}

    for table_name in priority_tables:
        if table_name in tables:
            output_file = f"data/raw_datasets/{table_name}.csv"
            table_id = f"{dataset_id}.{table_name}"

            df, metadata = exporter.export_table_to_csv(
                table_id,
                output_file,
                limit=5000,  # Limite pour portfolio
                sample=True  # Échantillonnage pour performances
            )

            if df is not None:
                exported_data[table_name] = {
                    'dataframe': df,
                    'metadata': metadata,
                    'file': output_file
                }
        else:
            print(f"⚠️ Table {table_name} non trouvée")

    # Résumé export
    print(f"\n✅ EXPORT TERMINÉ")
    print(f"📊 {len(exported_data)} tables exportées")

    for table_name, info in exported_data.items():
        print(f"  └── {table_name}: {info['metadata']['rows']} lignes")

    return exported_data

if __name__ == "__main__":
    main()
