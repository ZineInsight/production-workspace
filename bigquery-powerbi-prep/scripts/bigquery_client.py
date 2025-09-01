import os
from google.cloud import bigquery
import pandas as pd
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

class BigQueryClient:
    """Client pour interagir avec Google BigQuery"""

    def __init__(self):
        self.project_id = os.getenv('PROJECT_ID')
        self.client = bigquery.Client(project=self.project_id)

    def query_to_dataframe(self, query):
        """
        Exécute une requête SQL et retourne un DataFrame pandas

        Args:
            query (str): Requête SQL à exécuter

        Returns:
            pd.DataFrame: Résultats de la requête
        """
        try:
            df = self.client.query(query).to_dataframe()
            return df
        except Exception as e:
            print(f"Erreur lors de l'exécution de la requête: {e}")
            return None

    def get_table_schema(self, dataset_id, table_id):
        """
        Récupère le schéma d'une table

        Args:
            dataset_id (str): ID du dataset
            table_id (str): ID de la table

        Returns:
            list: Liste des champs de la table
        """
        try:
            table_ref = self.client.dataset(dataset_id).table(table_id)
            table = self.client.get_table(table_ref)
            return [(field.name, field.field_type) for field in table.schema]
        except Exception as e:
            print(f"Erreur lors de la récupération du schéma: {e}")
            return None

    def list_datasets(self):
        """Liste tous les datasets du projet"""
        try:
            datasets = list(self.client.list_datasets())
            return [dataset.dataset_id for dataset in datasets]
        except Exception as e:
            print(f"Erreur lors de la récupération des datasets: {e}")
            return []

    def list_tables(self, dataset_id):
        """Liste toutes les tables d'un dataset"""
        try:
            dataset_ref = self.client.dataset(dataset_id)
            tables = list(self.client.list_tables(dataset_ref))
            return [table.table_id for table in tables]
        except Exception as e:
            print(f"Erreur lors de la récupération des tables: {e}")
            return []

    def export_to_csv(self, query, filename):
        """
        Exécute une requête et exporte le résultat en CSV

        Args:
            query (str): Requête SQL
            filename (str): Nom du fichier CSV de sortie
        """
        df = self.query_to_dataframe(query)
        if df is not None:
            filepath = f"../data/{filename}"
            df.to_csv(filepath, index=False)
            print(f"Données exportées vers {filepath}")
            return filepath
        return None
