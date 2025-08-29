"""
🧹 NETTOYAGE ET DIVERSIFICATION DES DONNÉES
Créer une distribution temporelle réaliste pour le dashboard
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
from pathlib import Path

def diversify_temporal_data():
    """Créer une distribution temporelle réaliste"""
    print("🔄 Chargement des données originales...")

    # Charger les données
    sales_df = pd.read_csv('raw_datasets/raw_gz_sales.csv')
    products_df = pd.read_csv('raw_datasets/raw_gz_product.csv')
    facebook_df = pd.read_csv('raw_datasets/raw_gz_facebook.csv')

    print(f"📊 Données chargées: {len(sales_df)} ventes")

    # Créer une gamme de dates réaliste (6 mois)
    start_date = datetime(2021, 1, 1)
    end_date = datetime(2021, 6, 30)
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')

    print(f"📅 Distribution sur {len(date_range)} jours")

    # Créer une distribution réaliste
    # Plus d'activité en semaine, pics en fin de mois
    weights = []
    for date in date_range:
        weight = 1.0

        # Moins d'activité le weekend
        if date.weekday() >= 5:  # Weekend
            weight *= 0.6

        # Pics en fin de mois (effet salaire)
        if date.day >= 25:
            weight *= 1.5

        # Croissance progressive (business qui grandit)
        month_factor = 1 + (date.month - 1) * 0.1
        weight *= month_factor

        weights.append(weight)

    # Normaliser les poids
    weights = np.array(weights)
    weights = weights / weights.sum()

    # Assigner des dates aléatoires selon la distribution
    new_dates = np.random.choice(date_range, size=len(sales_df), p=weights)
    sales_df['date_date'] = [pd.to_datetime(date).strftime('%Y-%m-%d') for date in new_dates]

    # Trier par date pour plus de réalisme
    sales_df = sales_df.sort_values('date_date').reset_index(drop=True)

    # Ajuster les order_id pour qu'ils soient cohérents chronologiquement
    sales_df = sales_df.sort_values('date_date')
    unique_dates = sorted(sales_df['date_date'].unique())

    new_order_id = 800000
    for date in unique_dates:
        date_mask = sales_df['date_date'] == date
        date_orders = sales_df[date_mask]['orders_id'].unique()

        for old_id in date_orders:
            sales_df.loc[sales_df['orders_id'] == old_id, 'orders_id'] = new_order_id
            new_order_id += 1

    print("✅ Diversification temporelle terminée")

    # Sauvegarder les données nettoyées
    Path('cleaned_datasets').mkdir(exist_ok=True)

    sales_df.to_csv('cleaned_datasets/sales_cleaned.csv', index=False)
    products_df.to_csv('cleaned_datasets/products_cleaned.csv', index=False)
    facebook_df.to_csv('cleaned_datasets/facebook_cleaned.csv', index=False)

    # Statistiques
    print("\n📈 NOUVELLE DISTRIBUTION:")
    print(f"Date min: {sales_df['date_date'].min()}")
    print(f"Date max: {sales_df['date_date'].max()}")
    print(f"Dates uniques: {sales_df['date_date'].nunique()}")
    print(f"Période: {(pd.to_datetime(sales_df['date_date'].max()) - pd.to_datetime(sales_df['date_date'].min())).days} jours")

    # Distribution par mois
    sales_df['month'] = pd.to_datetime(sales_df['date_date']).dt.month
    monthly_dist = sales_df.groupby('month').agg({
        'revenue': 'sum',
        'orders_id': 'nunique'
    }).round(2)
    print("\n📊 DISTRIBUTION MENSUELLE:")
    print(monthly_dist)

    # Distribution par jour de semaine
    sales_df['weekday'] = pd.to_datetime(sales_df['date_date']).dt.day_name()
    weekday_dist = sales_df.groupby('weekday').agg({
        'revenue': 'sum',
        'orders_id': 'nunique'
    }).round(2)
    print("\n📊 DISTRIBUTION HEBDOMADAIRE:")
    print(weekday_dist)

if __name__ == "__main__":
    diversify_temporal_data()
