#!/usr/bin/env python3
"""
Générateur de dataset Amazon E-commerce pour l'étude de cas
Dataset simulé mais basé sur de vraies tendances Amazon
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import json

# Configuration
np.random.seed(42)
random.seed(42)

def generate_amazon_dataset():
    """Génère un dataset Amazon réaliste"""

    # Catégories de produits Amazon populaires
    categories = [
        "Electronics", "Clothing", "Home & Kitchen", "Books", "Sports & Outdoors",
        "Beauty & Personal Care", "Toys & Games", "Automotive", "Health & Household",
        "Garden & Outdoor", "Pet Supplies", "Baby Products"
    ]

    # Marques populaires par catégorie
    brands_by_category = {
        "Electronics": ["Samsung", "Apple", "Sony", "LG", "HP", "Dell", "Canon", "Nikon"],
        "Clothing": ["Nike", "Adidas", "Levi's", "Calvin Klein", "Tommy Hilfiger", "Gap"],
        "Home & Kitchen": ["Instant Pot", "Ninja", "Cuisinart", "KitchenAid", "Pyrex"],
        "Books": ["Penguin", "HarperCollins", "Random House", "Simon & Schuster"],
        "Sports & Outdoors": ["Nike", "Adidas", "Under Armour", "Columbia", "North Face"],
        "Beauty & Personal Care": ["L'Oreal", "Maybelline", "Neutrogena", "Olay"],
        "Toys & Games": ["LEGO", "Mattel", "Hasbro", "Fisher-Price", "Playmobil"],
        "Automotive": ["Bosch", "Castrol", "Mobil", "STP", "Chemical Guys"],
        "Health & Household": ["Johnson & Johnson", "P&G", "Unilever", "Colgate"],
        "Garden & Outdoor": ["Black & Decker", "Miracle-Gro", "Scotts", "Worx"],
        "Pet Supplies": ["Purina", "Hill's", "Blue Buffalo", "KONG", "Pedigree"],
        "Baby Products": ["Pampers", "Huggies", "Gerber", "Fisher-Price", "Chicco"]
    }

    # Génération des données
    n_products = 50000
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2024, 12, 31)

    products = []

    for i in range(n_products):
        category = random.choice(categories)
        brand = random.choice(brands_by_category[category])

        # Prix réalistes par catégorie
        price_ranges = {
            "Electronics": (50, 2000),
            "Clothing": (15, 300),
            "Home & Kitchen": (20, 500),
            "Books": (8, 50),
            "Sports & Outdoors": (25, 800),
            "Beauty & Personal Care": (10, 150),
            "Toys & Games": (15, 200),
            "Automotive": (20, 1000),
            "Health & Household": (5, 100),
            "Garden & Outdoor": (30, 600),
            "Pet Supplies": (10, 200),
            "Baby Products": (15, 300)
        }

        min_price, max_price = price_ranges[category]
        original_price = round(np.random.uniform(min_price, max_price), 2)

        # Discount aléatoire
        discount_prob = 0.3  # 30% de chance d'avoir une réduction
        if random.random() < discount_prob:
            discount = np.random.uniform(0.05, 0.5)  # 5-50% de réduction
            current_price = round(original_price * (1 - discount), 2)
        else:
            current_price = original_price

        # Rating réaliste (biaisé vers les bonnes notes)
        rating = round(np.random.beta(7, 2) * 4 + 1, 1)  # Biaisé vers 4-5 étoiles
        rating = min(5.0, max(1.0, rating))

        # Nombre de reviews corrélé au rating et à la popularité
        base_reviews = int(np.random.exponential(50))
        if rating >= 4.0:
            num_reviews = int(base_reviews * np.random.uniform(1.5, 3))
        else:
            num_reviews = int(base_reviews * np.random.uniform(0.3, 1))

        # Stock basé sur la popularité
        if num_reviews > 500:  # Produit populaire
            stock = np.random.randint(100, 5000)
        elif num_reviews > 100:
            stock = np.random.randint(50, 500)
        else:
            stock = np.random.randint(10, 100)

        # Ventes mensuelles corrélées au rating et prix
        monthly_sales = int(np.random.poisson(max(1, num_reviews / 10)))
        if rating >= 4.5:
            monthly_sales = int(monthly_sales * np.random.uniform(1.5, 2.5))
        if current_price < original_price:  # En promo
            monthly_sales = int(monthly_sales * np.random.uniform(1.2, 1.8))

        # Saisonnalité pour certains produits
        seasonal_boost = 1.0
        if category in ["Toys & Games", "Electronics"] and datetime.now().month == 12:
            seasonal_boost = 2.0
        elif category == "Garden & Outdoor" and datetime.now().month in [4, 5, 6]:
            seasonal_boost = 1.5

        monthly_sales = int(monthly_sales * seasonal_boost)

        # Date d'ajout du produit
        days_since_start = np.random.randint(0, (end_date - start_date).days)
        date_added = start_date + timedelta(days=days_since_start)

        # Prime eligibility (70% de chance)
        prime_eligible = random.random() < 0.7

        product = {
            'product_id': f'ASIN_{i+1:06d}',
            'product_name': f'{brand} {category} Product {i+1}',
            'category': category,
            'brand': brand,
            'original_price': original_price,
            'current_price': current_price,
            'discount_percent': round((1 - current_price/original_price) * 100, 1) if current_price < original_price else 0,
            'rating': rating,
            'num_reviews': num_reviews,
            'monthly_sales': monthly_sales,
            'stock_quantity': stock,
            'prime_eligible': prime_eligible,
            'date_added': date_added.strftime('%Y-%m-%d'),
            'seller_type': random.choice(['Amazon', 'Third-party', 'Amazon Warehouse']),
            'shipping_weight': round(np.random.exponential(2) + 0.1, 2),
            'dimensions': f"{np.random.randint(5, 50)}x{np.random.randint(5, 50)}x{np.random.randint(3, 30)}",
            'availability': random.choice(['In Stock', 'Limited Stock', 'Pre-order']) if stock > 0 else 'Out of Stock'
        }

        products.append(product)

    return pd.DataFrame(products)

def generate_sales_timeseries():
    """Génère des données de ventes temporelles"""

    dates = pd.date_range(start='2023-01-01', end='2024-12-31', freq='D')

    sales_data = []

    for date in dates:
        # Tendance générale croissante
        base_sales = 1000 + (date - dates[0]).days * 0.5

        # Saisonnalité
        month = date.month
        seasonal_multiplier = 1.0

        # Black Friday / Cyber Monday
        if month == 11 and date.day in [24, 25, 26, 27]:
            seasonal_multiplier = 3.0
        # Noël
        elif month == 12 and date.day < 25:
            seasonal_multiplier = 2.0
        # Prime Day (juillet)
        elif month == 7 and date.day in [15, 16]:
            seasonal_multiplier = 2.5
        # Rentrée scolaire
        elif month == 8:
            seasonal_multiplier = 1.3
        # Été
        elif month in [6, 7, 8]:
            seasonal_multiplier = 1.1

        # Effet jour de la semaine
        if date.weekday() in [5, 6]:  # Weekend
            seasonal_multiplier *= 1.2

        # Bruit aléatoire
        noise = np.random.normal(0, 0.1)

        daily_sales = int(base_sales * seasonal_multiplier * (1 + noise))
        daily_sales = max(100, daily_sales)  # Minimum 100 ventes/jour

        sales_data.append({
            'date': date.strftime('%Y-%m-%d'),
            'total_sales': daily_sales,
            'revenue': daily_sales * np.random.uniform(25, 75),  # Prix moyen
            'orders': int(daily_sales * np.random.uniform(0.7, 0.9)),  # Commandes vs produits
            'unique_customers': int(daily_sales * np.random.uniform(0.6, 0.8))
        })

    return pd.DataFrame(sales_data)

if __name__ == "__main__":
    print("🏭 Génération du dataset Amazon E-commerce...")

    # Créer le dossier data
    import os
    os.makedirs('data', exist_ok=True)

    # Générer les datasets
    products_df = generate_amazon_dataset()
    sales_df = generate_sales_timeseries()

    # Sauvegarder
    products_df.to_csv('data/amazon_products.csv', index=False)
    sales_df.to_csv('data/amazon_sales_timeseries.csv', index=False)

    print(f"✅ Dataset produits généré: {len(products_df):,} produits")
    print(f"✅ Dataset ventes généré: {len(sales_df):,} jours de données")

    # Aperçu des données
    print("\n📊 Aperçu des produits:")
    print(products_df.head())
    print(f"\nCatégories: {products_df['category'].unique()}")
    print(f"Prix moyen: ${products_df['current_price'].mean():.2f}")
    print(f"Rating moyen: {products_df['rating'].mean():.1f}")

    print("\n📈 Aperçu des ventes:")
    print(sales_df.head())
    print(f"Ventes totales: {sales_df['total_sales'].sum():,}")
    print(f"Revenus totaux: ${sales_df['revenue'].sum():,.2f}")
