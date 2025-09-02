#!/usr/bin/env python3
"""
🚀 GÉNÉRATEUR DE FICHIERS TEMPORELS POUR POWER BI
================================================
Génère des tables temporelles optimisées pour l'analyse Power BI
"""

import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from pathlib import Path

class TemporalFilesGenerator:
    def __init__(self):
        self.base_dir = Path("/var/www/production-workspace/bigquery-powerbi-prep")
        self.data_dir = self.base_dir / "data" / "powerbi_exports"
        self.output_dir = self.data_dir / "temporal_analysis"
        
        # Créer le dossier de sortie
        self.output_dir.mkdir(exist_ok=True)
        
        # Charger les données existantes
        self.overview = pd.read_csv(self.data_dir / "course_green_overview.csv")
        self.sales = pd.read_csv(self.data_dir / "greenweez_geographic_sales_v2_no_ca.csv")
        self.sales['date_vente'] = pd.to_datetime(self.sales['date_vente'])

    def generate_calendar_dimension(self):
        """📅 Génère table calendrier complète pour Power BI"""
        print("📅 Génération calendar_dimension.csv...")
        
        # Période étendue : Sept 2024 → Déc 2025
        start_date = pd.Timestamp('2024-09-01')
        end_date = pd.Timestamp('2025-12-31')
        
        # Génération de toutes les dates
        dates = pd.date_range(start=start_date, end=end_date, freq='D')
        
        calendar_data = []
        
        for date in dates:
            calendar_data.append({
                'Date': date.strftime('%Y-%m-%d'),
                'DateKey': date.strftime('%Y%m%d'),
                'Annee': date.year,
                'Mois': date.month,
                'MoisNom': date.strftime('%B'),
                'MoisNomCourt': date.strftime('%b'),
                'Trimestre': f"T{date.quarter}",
                'TrimestreAnnee': f"{date.year}-T{date.quarter}",
                'Semaine': date.isocalendar()[1],
                'SemaineAnnee': f"{date.year}-S{date.isocalendar()[1]:02d}",
                'JourSemaine': date.weekday() + 1,
                'JourSemaineNom': date.strftime('%A'),
                'JourSemaineNomCourt': date.strftime('%a'),
                'JourMois': date.day,
                'JourAnnee': date.timetuple().tm_yday,
                'EstWeekend': 1 if date.weekday() >= 5 else 0,
                'EstDebutMois': 1 if date.day == 1 else 0,
                'EstFinMois': 1 if date.day == pd.Timestamp(date.year, date.month, 1).days_in_month else 0,
                'Saison': self._get_season(date.month),
                'PeriodeFiscale': f"FY{date.year if date.month <= 6 else date.year + 1}",
                'MoisFrancais': self._get_french_month(date.month),
                'EstJourOuvrable': 1 if date.weekday() < 5 else 0
            })
        
        calendar_df = pd.DataFrame(calendar_data)
        
        # Export
        filepath = self.output_dir / "calendar_dimension.csv"
        calendar_df.to_csv(filepath, index=False, encoding='utf-8')
        
        print(f"✅ Calendar généré : {filepath}")
        print(f"   📊 {len(calendar_df)} jours de {start_date.strftime('%d/%m/%Y')} à {end_date.strftime('%d/%m/%Y')}")
        return filepath

    def generate_sales_monthly_summary(self):
        """📊 Génère résumé mensuel des ventes"""
        print("📊 Génération sales_monthly_summary.csv...")
        
        # Jointure sales + overview pour avoir les prix
        sales_enriched = self.sales.merge(
            self.overview[['products_id', 'category_1', 'category_2', 'ps_cat', 'pd_cat']], 
            on='products_id', 
            how='left'
        )
        
        # Calcul du CA
        sales_enriched['ca_standard'] = sales_enriched['quantity'] * sales_enriched['ps_cat']
        sales_enriched['ca_discount'] = sales_enriched['quantity'] * sales_enriched['pd_cat']
        sales_enriched['year_month'] = sales_enriched['date_vente'].dt.to_period('M')
        
        # Agrégation mensuelle
        monthly_summary = sales_enriched.groupby('year_month').agg({
            'sale_id': 'count',
            'quantity': 'sum',
            'ca_standard': 'sum',
            'ca_discount': 'sum',
            'products_id': 'nunique',
            'category_1': 'nunique'
        }).reset_index()
        
        # Renommage et calculs
        monthly_summary.columns = [
            'PeriodeMois', 'NombreVentes', 'QuantiteTotale', 
            'CAStandard', 'CADiscount', 'NombreProduitsVendus', 'NombreCategoriesActives'
        ]
        
        monthly_summary['Date'] = monthly_summary['PeriodeMois'].dt.start_time.dt.date
        monthly_summary['Annee'] = monthly_summary['PeriodeMois'].dt.year
        monthly_summary['Mois'] = monthly_summary['PeriodeMois'].dt.month
        monthly_summary['MoisNom'] = monthly_summary['PeriodeMois'].dt.strftime('%B')
        monthly_summary['PanierMoyen'] = (monthly_summary['CAStandard'] / monthly_summary['NombreVentes']).round(2)
        monthly_summary['QuantiteMoyenneParVente'] = (monthly_summary['QuantiteTotale'] / monthly_summary['NombreVentes']).round(2)
        monthly_summary['RemiseTotale'] = (monthly_summary['CAStandard'] - monthly_summary['CADiscount']).round(2)
        monthly_summary['TauxRemise'] = ((monthly_summary['RemiseTotale'] / monthly_summary['CAStandard']) * 100).round(2)
        
        # Réorganisation des colonnes
        cols_order = [
            'Date', 'Annee', 'Mois', 'MoisNom', 'NombreVentes', 'QuantiteTotale',
            'CAStandard', 'CADiscount', 'RemiseTotale', 'TauxRemise', 'PanierMoyen',
            'QuantiteMoyenneParVente', 'NombreProduitsVendus', 'NombreCategoriesActives'
        ]
        monthly_summary = monthly_summary[cols_order]
        
        # Export
        filepath = self.output_dir / "sales_monthly_summary.csv"
        monthly_summary.to_csv(filepath, index=False, encoding='utf-8')
        
        print(f"✅ Résumé mensuel généré : {filepath}")
        print(f"   📊 {len(monthly_summary)} mois d'analyse")
        return filepath

    def generate_seasonal_analysis(self):
        """🌱 Génère analyse saisonnière par catégorie"""
        print("🌱 Génération seasonal_analysis.csv...")
        
        # Jointure sales + overview
        sales_enriched = self.sales.merge(
            self.overview[['products_id', 'category_1', 'category_2', 'ps_cat']], 
            on='products_id', 
            how='left'
        )
        
        # Ajout des dimensions temporelles
        sales_enriched['mois'] = sales_enriched['date_vente'].dt.month
        sales_enriched['saison'] = sales_enriched['mois'].apply(self._get_season)
        sales_enriched['ca'] = sales_enriched['quantity'] * sales_enriched['ps_cat']
        
        # Agrégation par saison et catégorie
        seasonal_data = sales_enriched.groupby(['saison', 'category_1']).agg({
            'quantity': 'sum',
            'ca': 'sum',
            'sale_id': 'count',
            'products_id': 'nunique'
        }).reset_index()
        
        seasonal_data.columns = ['Saison', 'Categorie', 'QuantiteTotale', 'CATotal', 'NombreVentes', 'NombreProduitsVendus']
        
        # Calculs additionnels
        seasonal_data['PanierMoyen'] = (seasonal_data['CATotal'] / seasonal_data['NombreVentes']).round(2)
        seasonal_data['QuantiteMoyenneParVente'] = (seasonal_data['QuantiteTotale'] / seasonal_data['NombreVentes']).round(2)
        
        # Calcul des pourcentages par saison
        total_by_season = seasonal_data.groupby('Saison')['CATotal'].sum().reset_index()
        total_by_season.columns = ['Saison', 'CATotalSaison']
        seasonal_data = seasonal_data.merge(total_by_season, on='Saison')
        seasonal_data['PourcentageCAParSaison'] = ((seasonal_data['CATotal'] / seasonal_data['CATotalSaison']) * 100).round(2)
        
        # Tri par saison et CA
        seasonal_order = ['Automne', 'Hiver', 'Printemps', 'Été']
        seasonal_data['SaisonOrdre'] = seasonal_data['Saison'].map({s: i for i, s in enumerate(seasonal_order)})
        seasonal_data = seasonal_data.sort_values(['SaisonOrdre', 'CATotal'], ascending=[True, False])
        seasonal_data = seasonal_data.drop('SaisonOrdre', axis=1)
        
        # Export
        filepath = self.output_dir / "seasonal_analysis.csv"
        seasonal_data.to_csv(filepath, index=False, encoding='utf-8')
        
        print(f"✅ Analyse saisonnière générée : {filepath}")
        print(f"   📊 {len(seasonal_data)} combinaisons saison/catégorie")
        return filepath

    def generate_product_temporal_performance(self):
        """📦 Génère performance temporelle des produits"""
        print("📦 Génération product_temporal_performance.csv...")
        
        # Jointure sales + overview pour récupérer les infos produit
        sales_with_overview = self.sales.merge(
            self.overview[['products_id', 'category_1', 'ps_cat', 'stock']], 
            on='products_id', 
            how='left'
        )
        
        # Ajout dimensions temporelles
        sales_with_overview['year_month'] = sales_with_overview['date_vente'].dt.to_period('M')
        sales_with_overview['ca'] = sales_with_overview['quantity'] * sales_with_overview['ps_cat']
        
        # Agrégation par produit et mois (utilisation du pdt_name depuis sales)
        product_monthly = sales_with_overview.groupby(['products_id', 'pdt_name', 'category_1', 'year_month']).agg({
            'quantity': 'sum',
            'ca': 'sum',
            'sale_id': 'count',
            'ps_cat': 'first',
            'stock': 'first'
        }).reset_index()
        
        product_monthly.columns = [
            'ProductID', 'NomProduit', 'Categorie', 'PeriodeMois', 
            'QuantiteVendue', 'CAGenere', 'NombreVentes', 'PrixStandard', 'Stock'
        ]
        
        # Conversion de la période en date
        product_monthly['Date'] = product_monthly['PeriodeMois'].dt.start_time.dt.date
        product_monthly['Annee'] = product_monthly['PeriodeMois'].dt.year
        product_monthly['Mois'] = product_monthly['PeriodeMois'].dt.month
        
        # Calculs de performance
        product_monthly['VelociteRotation'] = (product_monthly['QuantiteVendue'] / product_monthly['Stock'] * 100).round(2)
        product_monthly['PanierMoyenProduit'] = (product_monthly['CAGenere'] / product_monthly['NombreVentes']).round(2)
        
        # Classement mensuel par catégorie
        product_monthly['RangCACategorie'] = product_monthly.groupby(['Categorie', 'PeriodeMois'])['CAGenere'].rank(ascending=False, method='dense')
        
        # Tendance (évolution vs mois précédent)
        product_monthly = product_monthly.sort_values(['ProductID', 'Date'])
        product_monthly['CAMoisPrecedent'] = product_monthly.groupby('ProductID')['CAGenere'].shift(1)
        product_monthly['TendanceCA'] = (((product_monthly['CAGenere'] - product_monthly['CAMoisPrecedent']) / product_monthly['CAMoisPrecedent']) * 100).round(2)
        
        # Statut de performance
        def get_performance_status(row):
            if pd.isna(row['VelociteRotation']):
                return 'Nouveau'
            elif row['VelociteRotation'] >= 20:
                return 'Excellent'
            elif row['VelociteRotation'] >= 10:
                return 'Bon'
            elif row['VelociteRotation'] >= 5:
                return 'Moyen'
            else:
                return 'Lent'
        
        product_monthly['StatutPerformance'] = product_monthly.apply(get_performance_status, axis=1)
        
        # Réorganisation des colonnes
        cols_order = [
            'Date', 'Annee', 'Mois', 'ProductID', 'NomProduit', 'Categorie',
            'QuantiteVendue', 'CAGenere', 'NombreVentes', 'PrixStandard',
            'PanierMoyenProduit', 'VelociteRotation', 'RangCACategorie',
            'TendanceCA', 'StatutPerformance', 'Stock'
        ]
        product_monthly = product_monthly[cols_order]
        
        # Export
        filepath = self.output_dir / "product_temporal_performance.csv"
        product_monthly.to_csv(filepath, index=False, encoding='utf-8')
        
        print(f"✅ Performance temporelle produits générée : {filepath}")
        print(f"   📊 {len(product_monthly)} enregistrements produit/mois")
        return filepath

    def generate_weekly_trends(self):
        """📅 Génère tendances hebdomadaires"""
        print("📅 Génération weekly_trends.csv...")
        
        # Jointure sales + overview
        sales_enriched = self.sales.merge(
            self.overview[['products_id', 'category_1', 'ps_cat']], 
            on='products_id', 
            how='left'
        )
        
        # Ajout dimensions temporelles
        sales_enriched['year_week'] = sales_enriched['date_vente'].dt.isocalendar().week
        sales_enriched['year'] = sales_enriched['date_vente'].dt.year
        sales_enriched['week_year'] = sales_enriched['year'].astype(str) + '-S' + sales_enriched['year_week'].astype(str).str.zfill(2)
        sales_enriched['day_of_week'] = sales_enriched['date_vente'].dt.weekday + 1
        sales_enriched['day_name'] = sales_enriched['date_vente'].dt.strftime('%A')
        sales_enriched['ca'] = sales_enriched['quantity'] * sales_enriched['ps_cat']
        
        # Agrégation hebdomadaire globale
        weekly_summary = sales_enriched.groupby(['year', 'year_week', 'week_year']).agg({
            'quantity': 'sum',
            'ca': 'sum',
            'sale_id': 'count',
            'products_id': 'nunique',
            'category_1': 'nunique'
        }).reset_index()
        
        weekly_summary.columns = [
            'Annee', 'NumeroSemaine', 'SemaineAnnee', 'QuantiteTotale', 
            'CATotal', 'NombreVentes', 'NombreProduitsVendus', 'NombreCategoriesActives'
        ]
        
        # Calculs additionnels
        weekly_summary['PanierMoyenHebdo'] = (weekly_summary['CATotal'] / weekly_summary['NombreVentes']).round(2)
        weekly_summary['QuantiteMoyenneParVente'] = (weekly_summary['QuantiteTotale'] / weekly_summary['NombreVentes']).round(2)
        
        # Date de début de semaine pour jointure
        def get_week_start_date(year, week):
            from datetime import datetime, timedelta
            jan4 = datetime(year, 1, 4)
            week_start = jan4 + timedelta(days=(week - 1) * 7 - jan4.weekday())
            return week_start.date()
        
        weekly_summary['DateDebutSemaine'] = weekly_summary.apply(
            lambda row: get_week_start_date(row['Annee'], row['NumeroSemaine']), axis=1
        )
        
        # Tendance hebdomadaire
        weekly_summary = weekly_summary.sort_values(['Annee', 'NumeroSemaine'])
        weekly_summary['CASemainePrecedente'] = weekly_summary['CATotal'].shift(1)
        weekly_summary['TendanceHebdo'] = (((weekly_summary['CATotal'] - weekly_summary['CASemainePrecedente']) / weekly_summary['CASemainePrecedente']) * 100).round(2)
        
        # Réorganisation
        cols_order = [
            'DateDebutSemaine', 'Annee', 'NumeroSemaine', 'SemaineAnnee',
            'NombreVentes', 'QuantiteTotale', 'CATotal', 'PanierMoyenHebdo',
            'QuantiteMoyenneParVente', 'NombreProduitsVendus', 'NombreCategoriesActives',
            'TendanceHebdo'
        ]
        weekly_summary = weekly_summary[cols_order]
        
        # Export
        filepath = self.output_dir / "weekly_trends.csv"
        weekly_summary.to_csv(filepath, index=False, encoding='utf-8')
        
        print(f"✅ Tendances hebdomadaires générées : {filepath}")
        print(f"   📊 {len(weekly_summary)} semaines d'analyse")
        return filepath

    def _get_season(self, month):
        """Retourne la saison selon le mois"""
        if month in [12, 1, 2]:
            return 'Hiver'
        elif month in [3, 4, 5]:
            return 'Printemps'
        elif month in [6, 7, 8]:
            return 'Été'
        else:
            return 'Automne'
    
    def _get_french_month(self, month):
        """Retourne le nom du mois en français"""
        months = {
            1: 'Janvier', 2: 'Février', 3: 'Mars', 4: 'Avril',
            5: 'Mai', 6: 'Juin', 7: 'Juillet', 8: 'Août',
            9: 'Septembre', 10: 'Octobre', 11: 'Novembre', 12: 'Décembre'
        }
        return months[month]

    def generate_all_temporal_files(self):
        """🚀 Génère tous les fichiers temporels"""
        print("🚀 GÉNÉRATION COMPLÈTE DES FICHIERS TEMPORELS")
        print("=" * 50)
        
        files_generated = []
        
        # 1. Calendar dimension (BASE - Priorité 1)
        files_generated.append(self.generate_calendar_dimension())
        
        # 2. Monthly summary (AGRÉGATION MENSUELLE)
        files_generated.append(self.generate_sales_monthly_summary())
        
        # 3. Seasonal analysis (PATTERNS SAISONNIERS)
        files_generated.append(self.generate_seasonal_analysis())
        
        # 4. Weekly trends (TENDANCES HEBDOMADAIRES)
        files_generated.append(self.generate_weekly_trends())
        
        # 5. Product temporal performance (ÉVOLUTION PRODUITS)
        files_generated.append(self.generate_product_temporal_performance())
        
        print(f"\n🎉 GÉNÉRATION TERMINÉE !")
        print(f"📂 {len(files_generated)} fichiers créés dans : {self.output_dir}")
        for file in files_generated:
            print(f"   📄 {file.name}")
        
        # Résumé des relations Power BI recommandées
        print(f"\n🔗 RELATIONS POWER BI RECOMMANDÉES :")
        print(f"   📅 calendar_dimension[Date] ← → greenweez_geographic_sales[date_vente] (Many-to-One)")
        print(f"   📊 sales_monthly_summary[Date] ← → calendar_dimension[Date] (One-to-One)")
        print(f"   🌱 seasonal_analysis[Saison] ← → calendar_dimension[Saison] (Many-to-One)")
        print(f"   📅 weekly_trends[DateDebutSemaine] ← → calendar_dimension[Date] (One-to-Many)")
        print(f"   📦 product_temporal_performance[ProductID] ← → course_green_overview[products_id] (Many-to-One)")
        print(f"   📦 product_temporal_performance[Date] ← → calendar_dimension[Date] (Many-to-One)")
        
        return files_generated

def main():
    """Fonction principale"""
    generator = TemporalFilesGenerator()
    generator.generate_all_temporal_files()

if __name__ == "__main__":
    main()
