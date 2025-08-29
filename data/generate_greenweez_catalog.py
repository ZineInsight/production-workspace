"""
🌱 GÉNÉRATEUR DE CATALOGUE PRODUITS BIO GREENWEEZ
===============================================
Transforme les IDs en noms de produits bio réalistes
Pour un dashboard e-commerce crédible et professionnel
"""

import pandas as pd
import random
import numpy as np

def generate_greenweez_catalog():
    """Génère un catalogue de produits bio Greenweez réalistes"""

    print("🌱 Génération du catalogue Greenweez Bio...")

    # Catégories de produits bio Greenweez
    bio_categories = {
        'Fruits & Légumes': [
            'Pommes bio Gala', 'Bananes bio équitables', 'Carottes bio Provence',
            'Tomates cerises bio', 'Avocat bio Pérou', 'Citrons bio Sicile',
            'Épinards bio français', 'Courgettes bio locales', 'Brocolis bio',
            'Pommes de terre bio Normandie', 'Oignons bio France', 'Ail bio Drôme'
        ],
        'Épicerie Bio': [
            'Quinoa bio tricolore', 'Riz basmati bio Inde', 'Pâtes complètes bio',
            'Lentilles corail bio', 'Flocons avoine bio', 'Huile olive bio Provence',
            'Vinaigre balsamique bio', 'Miel acacia bio France', 'Sucre coco bio',
            'Farine épeautre bio', 'Graines de chia bio', 'Amandes bio Espagne'
        ],
        'Boissons Bio': [
            'Jus pomme bio 1L', 'Thé vert bio Sencha', 'Café arabica bio équitable',
            'Eau de coco bio', 'Tisane camomille bio', 'Kombucha gingembre bio',
            'Lait avoine bio Oatly', 'Smoothie açaï bio', 'Thé chai bio épices',
            'Jus orange bio pressé', 'Infusion détox bio', 'Matcha bio premium'
        ],
        'Cosmétiques Bio': [
            'Shampoing bio karité', 'Savon bio olive Marseille', 'Crème visage bio aloe',
            'Huile argan bio Maroc', 'Dentifrice bio menthe', 'Déodorant bio palmarosa',
            'Gel douche bio lavande', 'Masque argile bio', 'Sérum anti-âge bio',
            'Baume lèvres bio cire abeille', 'Lotion tonique bio rose', 'Crème mains bio'
        ],
        'Bébé & Enfant Bio': [
            'Compote pomme bio bébé', 'Couches écolo T3', 'Lingettes bio calendula',
            'Lait infantile bio', 'Petit pot légumes bio', 'Biscuits bébé bio',
            'Gel lavant bio enfant', 'Crème change bio', 'Céréales bébé bio',
            'Purée fruits bio pot', 'Huile massage bébé bio', 'Pommade bio calendula'
        ],
        'Compléments Bio': [
            'Spiruline bio comprimés', 'Vitamine D3 bio', 'Probiotiques bio gélules',
            'Magnésium marin bio', 'Gelée royale bio', 'Propolis bio spray',
            'Omega 3 bio algues', 'Curcuma bio pipérine', 'Ginseng bio tonus',
            'Chlorella bio détox', 'Acérola bio vitamine C', 'Rhodiola bio stress'
        ]
    }

    # Charger les données actuelles
    products_df = pd.read_csv('cleaned_datasets/products_cleaned.csv')
    sales_df = pd.read_csv('cleaned_datasets/sales_cleaned.csv')

    # Récupérer tous les IDs produits vendus
    sold_product_ids = sales_df['pdt_id'].unique()

    # Générer des noms pour chaque ID
    catalog_enriched = []

    for product_id in sold_product_ids:
        # Choisir une catégorie aléatoire
        category = random.choice(list(bio_categories.keys()))
        product_names = bio_categories[category]

        # Choisir un nom de produit
        base_name = random.choice(product_names)

        # Ajouter de la variété avec des variants
        variants = ['', ' 500g', ' 250g', ' 1kg', ' pack de 6', ' format familial', ' premium']
        variant = random.choice(variants)

        product_name = base_name + variant

        # Prix cohérent avec le type de produit et Greenweez
        if 'Fruits & Légumes' in category:
            price_base = random.uniform(2.5, 8.9)
        elif 'Cosmétiques Bio' in category:
            price_base = random.uniform(5.9, 24.9)
        elif 'Compléments Bio' in category:
            price_base = random.uniform(12.9, 39.9)
        elif 'Boissons Bio' in category:
            price_base = random.uniform(2.9, 15.9)
        else:
            price_base = random.uniform(3.9, 18.9)

        catalog_enriched.append({
            'product_id': product_id,
            'product_name': product_name,
            'category': category,
            'price_catalog': round(price_base, 2),
            'brand': 'Greenweez' if random.random() > 0.7 else random.choice([
                'Biocoop', 'Naturalia', 'La Vie Claire', 'Bjorg', 'Léa Nature', 'Weleda'
            ])
        })

    # Créer le DataFrame enrichi
    catalog_df = pd.DataFrame(catalog_enriched)

    # Fusionner avec les données produits existantes
    enriched_products = products_df.merge(
        catalog_df,
        left_on='products_id',
        right_on='product_id',
        how='left'
    )

    # Sauvegarder le catalogue enrichi
    enriched_products.to_csv('cleaned_datasets/products_greenweez.csv', index=False)
    catalog_df.to_csv('cleaned_datasets/catalog_greenweez.csv', index=False)

    print(f"✅ Catalogue créé: {len(catalog_df)} produits bio nommés")
    print(f"📊 Répartition par catégorie:")
    category_counts = catalog_df['category'].value_counts()
    for cat, count in category_counts.items():
        print(f"  • {cat}: {count} produits")

    print(f"📦 Marques présentes:")
    brand_counts = catalog_df['brand'].value_counts()
    for brand, count in brand_counts.head().items():
        print(f"  • {brand}: {count} produits")

    # Échantillon final
    print("\\n🌱 ÉCHANTILLON CATALOGUE:")
    sample = catalog_df.sample(10)
    for _, row in sample.iterrows():
        print(f"  • {row['product_name']} - {row['category']} - {row['price_catalog']}€ - {row['brand']}")

    return catalog_df, enriched_products

if __name__ == "__main__":
    generate_greenweez_catalog()
