#!/usr/bin/env python3
"""
Analyseur de données Amazon E-commerce
Extrait les insights clés pour le dashboard
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json

class AmazonAnalyzer:
    def __init__(self):
        self.products_df = pd.read_csv('data/amazon_products.csv')
        self.sales_df = pd.read_csv('data/amazon_sales_timeseries.csv')

        # Preprocessing
        self.products_df['date_added'] = pd.to_datetime(self.products_df['date_added'])
        self.sales_df['date'] = pd.to_datetime(self.sales_df['date'])

    def get_category_performance(self):
        """Analyse de performance par catégorie"""

        category_stats = self.products_df.groupby('category').agg({
            'monthly_sales': ['mean', 'sum', 'count'],
            'current_price': ['mean', 'median'],
            'rating': 'mean',
            'num_reviews': 'mean',
            'discount_percent': 'mean'
        }).round(2)

        category_stats.columns = [f'{col[1]}_{col[0]}' for col in category_stats.columns]
        category_stats = category_stats.reset_index()

        # Calculer le revenue total par catégorie
        category_stats['total_revenue'] = (
            category_stats['sum_monthly_sales'] * category_stats['mean_current_price']
        ).round(2)

        # Trier par revenus
        category_stats = category_stats.sort_values('total_revenue', ascending=False)

        return category_stats.to_dict('records')

    def get_pricing_insights(self):
        """Analyse des stratégies de prix"""

        # Prix vs Ventes correlation
        price_ranges = []
        ranges = [(0, 25), (25, 50), (50, 100), (100, 200), (200, 500), (500, float('inf'))]

        for min_price, max_price in ranges:
            if max_price == float('inf'):
                mask = self.products_df['current_price'] >= min_price
                label = f"${min_price}+"
            else:
                mask = (self.products_df['current_price'] >= min_price) & (self.products_df['current_price'] < max_price)
                label = f"${min_price}-${max_price}"

            subset = self.products_df[mask]
            if len(subset) > 0:
                price_ranges.append({
                    'range': label,
                    'products': len(subset),
                    'avg_sales': subset['monthly_sales'].mean(),
                    'avg_rating': subset['rating'].mean(),
                    'avg_reviews': subset['num_reviews'].mean()
                })

        # Discount impact
        discount_impact = {
            'no_discount': self.products_df[self.products_df['discount_percent'] == 0]['monthly_sales'].mean(),
            'small_discount': self.products_df[(self.products_df['discount_percent'] > 0) & (self.products_df['discount_percent'] <= 20)]['monthly_sales'].mean(),
            'large_discount': self.products_df[self.products_df['discount_percent'] > 20]['monthly_sales'].mean()
        }

        return {
            'price_ranges': price_ranges,
            'discount_impact': discount_impact
        }

    def get_seasonal_trends(self):
        """Analyse des tendances saisonnières"""

        # Ajouter colonnes temporelles
        self.sales_df['month'] = self.sales_df['date'].dt.month
        self.sales_df['day_of_week'] = self.sales_df['date'].dt.dayofweek
        self.sales_df['quarter'] = self.sales_df['date'].dt.quarter

        # Tendances mensuelles
        monthly_trends = self.sales_df.groupby('month').agg({
            'total_sales': 'mean',
            'revenue': 'mean',
            'orders': 'mean'
        }).round(2)

        monthly_trends['month_name'] = [
            'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
            'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
        ]

        # Tendances par jour de la semaine
        weekly_trends = self.sales_df.groupby('day_of_week').agg({
            'total_sales': 'mean',
            'revenue': 'mean'
        }).round(2)

        weekly_trends['day_name'] = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

        # Événements spéciaux (Black Friday, Prime Day, etc.)
        special_events = []

        # Black Friday (fin novembre)
        bf_data = self.sales_df[
            (self.sales_df['date'].dt.month == 11) &
            (self.sales_df['date'].dt.day.isin([24, 25, 26, 27]))
        ]
        if len(bf_data) > 0:
            special_events.append({
                'event': 'Black Friday Week',
                'avg_sales': bf_data['total_sales'].mean(),
                'vs_normal': (bf_data['total_sales'].mean() / self.sales_df['total_sales'].mean() - 1) * 100
            })

        # Prime Day (juillet)
        pd_data = self.sales_df[
            (self.sales_df['date'].dt.month == 7) &
            (self.sales_df['date'].dt.day.isin([15, 16]))
        ]
        if len(pd_data) > 0:
            special_events.append({
                'event': 'Prime Day',
                'avg_sales': pd_data['total_sales'].mean(),
                'vs_normal': (pd_data['total_sales'].mean() / self.sales_df['total_sales'].mean() - 1) * 100
            })

        return {
            'monthly': monthly_trends.to_dict('records'),
            'weekly': weekly_trends.to_dict('records'),
            'special_events': special_events
        }

    def get_top_performers(self):
        """Top produits et catégories"""

        # Top produits par ventes
        top_products = self.products_df.nlargest(20, 'monthly_sales')[
            ['product_name', 'category', 'brand', 'monthly_sales', 'rating', 'current_price']
        ].to_dict('records')

        # Top marques
        top_brands = self.products_df.groupby('brand').agg({
            'monthly_sales': 'sum',
            'product_id': 'count',
            'rating': 'mean'
        }).sort_values('monthly_sales', ascending=False).head(15).to_dict('records')

        # Produits les mieux notés avec beaucoup de reviews
        top_rated = self.products_df[
            self.products_df['num_reviews'] >= 100
        ].nlargest(15, 'rating')[
            ['product_name', 'category', 'rating', 'num_reviews', 'monthly_sales']
        ].to_dict('records')

        return {
            'top_products': top_products,
            'top_brands': top_brands,
            'top_rated': top_rated
        }

    def get_inventory_insights(self):
        """Insights sur l'inventaire et stock"""

        # Stock par catégorie
        stock_by_category = self.products_df.groupby('category').agg({
            'stock_quantity': ['mean', 'sum', 'std'],
            'monthly_sales': 'sum'
        }).round(2)

        stock_by_category.columns = [f'{col[1]}_{col[0]}' for col in stock_by_category.columns]
        stock_by_category = stock_by_category.reset_index()

        # Calcul du ratio stock/ventes (mois de stock)
        stock_by_category['months_of_stock'] = (
            stock_by_category['sum_stock_quantity'] / stock_by_category['sum_monthly_sales']
        ).round(1)

        # Produits en rupture ou stock faible
        low_stock = self.products_df[self.products_df['stock_quantity'] < 50].groupby('category').size()
        out_of_stock = self.products_df[self.products_df['availability'] == 'Out of Stock'].groupby('category').size()

        return {
            'stock_by_category': stock_by_category.to_dict('records'),
            'low_stock_alerts': low_stock.to_dict() if not low_stock.empty else {},
            'out_of_stock_alerts': out_of_stock.to_dict() if not out_of_stock.empty else {}
        }

    def get_customer_behavior(self):
        """Analyse du comportement client"""

        # Corrélation rating vs sales
        rating_bins = pd.cut(self.products_df['rating'], bins=[0, 3, 3.5, 4, 4.5, 5], labels=['<3', '3-3.5', '3.5-4', '4-4.5', '4.5-5'])
        rating_sales = self.products_df.groupby(rating_bins)['monthly_sales'].mean().to_dict()

        # Prime vs non-Prime
        prime_impact = {
            'prime_eligible': self.products_df[self.products_df['prime_eligible']]['monthly_sales'].mean(),
            'non_prime': self.products_df[~self.products_df['prime_eligible']]['monthly_sales'].mean()
        }

        # Reviews impact
        review_bins = pd.cut(self.products_df['num_reviews'], bins=[0, 10, 50, 100, 500, float('inf')], labels=['<10', '10-50', '50-100', '100-500', '500+'])
        review_sales = self.products_df.groupby(review_bins)['monthly_sales'].mean().to_dict()

        return {
            'rating_impact': rating_sales,
            'prime_impact': prime_impact,
            'reviews_impact': review_sales
        }

    def get_all_insights(self):
        """Compile tous les insights"""

        print("🔍 Analyse des catégories...")
        category_performance = self.get_category_performance()

        print("💰 Analyse des prix...")
        pricing_insights = self.get_pricing_insights()

        print("📅 Analyse saisonnière...")
        seasonal_trends = self.get_seasonal_trends()

        print("🏆 Top performers...")
        top_performers = self.get_top_performers()

        print("📦 Analyse inventaire...")
        inventory_insights = self.get_inventory_insights()

        print("👥 Comportement client...")
        customer_behavior = self.get_customer_behavior()

        # Métriques générales
        general_metrics = {
            'total_products': len(self.products_df),
            'total_categories': self.products_df['category'].nunique(),
            'total_brands': self.products_df['brand'].nunique(),
            'avg_price': self.products_df['current_price'].mean(),
            'avg_rating': self.products_df['rating'].mean(),
            'total_monthly_sales': self.products_df['monthly_sales'].sum(),
            'prime_eligible_percent': (self.products_df['prime_eligible'].sum() / len(self.products_df)) * 100
        }

        return {
            'general_metrics': general_metrics,
            'category_performance': category_performance,
            'pricing_insights': pricing_insights,
            'seasonal_trends': seasonal_trends,
            'top_performers': top_performers,
            'inventory_insights': inventory_insights,
            'customer_behavior': customer_behavior,
            'generated_at': datetime.now().isoformat()
        }

if __name__ == "__main__":
    print("📊 Analyse des données Amazon E-commerce...")

    analyzer = AmazonAnalyzer()
    insights = analyzer.get_all_insights()

    # Sauvegarder les insights
    with open('data/amazon_insights.json', 'w') as f:
        json.dump(insights, f, indent=2, default=str)

    print("✅ Analyse terminée !")
    print(f"📈 {insights['general_metrics']['total_products']:,} produits analysés")
    print(f"💰 Prix moyen: ${insights['general_metrics']['avg_price']:.2f}")
    print(f"⭐ Rating moyen: {insights['general_metrics']['avg_rating']:.1f}")
    print(f"🛒 Ventes mensuelles totales: {insights['general_metrics']['total_monthly_sales']:,}")

    print("\n🏆 Top 3 catégories par revenus:")
    for i, cat in enumerate(insights['category_performance'][:3]):
        print(f"{i+1}. {cat['category']}: ${cat['total_revenue']:,.2f}")
