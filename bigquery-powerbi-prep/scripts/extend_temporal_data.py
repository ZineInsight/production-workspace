#!/usr/bin/env python3
"""
🚀 EXTENSION DES DONNÉES TEMPORELLES
===================================
Génère des données simulées cohérentes pour compléter jusqu'en décembre 2025
"""

import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from pathlib import Path

class TemporalDataExtender:
    def __init__(self):
        self.base_dir = Path("/var/www/production-workspace/bigquery-powerbi-prep")
        self.data_dir = self.base_dir / "data" / "powerbi_exports"
        self.temporal_dir = self.data_dir / "temporal_analysis"
        
        # Charger les données existantes
        self.monthly_summary = pd.read_csv(self.temporal_dir / "sales_monthly_summary.csv")
        self.calendar = pd.read_csv(self.temporal_dir / "calendar_dimension.csv")

    def extend_monthly_summary(self):
        """📈 Étend les données mensuelles jusqu'en décembre 2025"""
        print("📈 Extension sales_monthly_summary jusqu'en décembre 2025...")
        
        # Analyser les tendances existantes
        existing_data = self.monthly_summary.copy()
        existing_data['Date'] = pd.to_datetime(existing_data['Date'])
        
        # Calculer moyennes pour simuler des données réalistes
        avg_ventes = existing_data['NombreVentes'].mean()
        avg_ca = existing_data['CAStandard'].mean()
        avg_panier = existing_data['PanierMoyen'].mean()
        std_ca = existing_data['CAStandard'].std()
        
        # Données manquantes : octobre, novembre, décembre 2025
        new_months = []
        
        # Octobre 2025 (reprise post-été)
        new_months.append({
            'Date': '2025-10-01',
            'Annee': 2025,
            'Mois': 10,
            'MoisNom': 'October',
            'NombreVentes': int(avg_ventes * 1.1),  # +10% reprise
            'QuantiteTotale': int(avg_ventes * 1.1 * 5.5),
            'CAStandard': avg_ca * 0.85,  # Légère baisse
            'CADiscount': avg_ca * 0.85 * 0.91,
            'RemiseTotale': avg_ca * 0.85 * 0.09,
            'TauxRemise': 9.0,
            'PanierMoyen': avg_panier * 0.9,
            'QuantiteMoyenneParVente': 5.5,
            'NombreProduitsVendus': 18,
            'NombreCategoriesActives': 5
        })
        
        # Novembre 2025 (Black Friday boost)
        new_months.append({
            'Date': '2025-11-01',
            'Annee': 2025,
            'Mois': 11,
            'MoisNom': 'November',
            'NombreVentes': int(avg_ventes * 1.3),  # Black Friday
            'QuantiteTotale': int(avg_ventes * 1.3 * 6.2),
            'CAStandard': avg_ca * 1.15,  # +15% Black Friday
            'CADiscount': avg_ca * 1.15 * 0.85,
            'RemiseTotale': avg_ca * 1.15 * 0.15,
            'TauxRemise': 15.0,
            'PanierMoyen': avg_panier * 1.1,
            'QuantiteMoyenneParVente': 6.2,
            'NombreProduitsVendus': 22,
            'NombreCategoriesActives': 5
        })
        
        # Décembre 2025 (Noël peak)
        new_months.append({
            'Date': '2025-12-01',
            'Annee': 2025,
            'Mois': 12,
            'MoisNom': 'December',
            'NombreVentes': int(avg_ventes * 1.5),  # Peak Noël
            'QuantiteTotale': int(avg_ventes * 1.5 * 7.0),
            'CAStandard': avg_ca * 1.4,  # +40% Noël
            'CADiscount': avg_ca * 1.4 * 0.88,
            'RemiseTotale': avg_ca * 1.4 * 0.12,
            'TauxRemise': 12.0,
            'PanierMoyen': avg_panier * 1.3,
            'QuantiteMoyenneParVente': 7.0,
            'NombreProduitsVendus': 25,
            'NombreCategoriesActives': 5
        })
        
        # Créer DataFrame des nouvelles données
        new_data = pd.DataFrame(new_months)
        new_data['Date'] = pd.to_datetime(new_data['Date'])
        
        # Combiner avec les données existantes
        extended_monthly = pd.concat([existing_data, new_data], ignore_index=True)
        extended_monthly = extended_monthly.sort_values('Date')
        
        # Arrondir les valeurs
        for col in ['CAStandard', 'CADiscount', 'RemiseTotale', 'PanierMoyen']:
            extended_monthly[col] = extended_monthly[col].round(2)
        
        # Export
        filepath = self.temporal_dir / "sales_monthly_summary_extended.csv"
        extended_monthly.to_csv(filepath, index=False, encoding='utf-8')
        
        print(f"✅ Données mensuelles étendues : {filepath}")
        print(f"   📊 {len(extended_monthly)} mois total (vs {len(existing_data)} avant)")
        
        # Aperçu des nouvelles données
        print(f"\n🆕 NOUVELLES DONNÉES AJOUTÉES :")
        for _, row in new_data.iterrows():
            print(f"   {row['MoisNom']} 2025: {row['CAStandard']:.0f}€ ({row['NombreVentes']} ventes)")
        
        return filepath

    def extend_seasonal_analysis(self):
        """🌱 Met à jour l'analyse saisonnière avec plus de données"""
        print("🌱 Extension seasonal_analysis avec données simulées...")
        
        # Charger l'analyse saisonnière existante
        seasonal = pd.read_csv(self.temporal_dir / "seasonal_analysis.csv")
        
        # Ajouter des données simulées pour l'automne (oct-nov-déc)
        # Basé sur les patterns existants mais avec boost fin d'année
        
        autumn_boost = [
            # Électronique forte en fin d'année
            {'Saison': 'Automne', 'Categorie': 'Électronique', 'QuantiteTotale': 85, 
             'CATotal': 45000, 'NombreVentes': 18, 'NombreProduitsVendus': 8, 
             'PanierMoyen': 2500, 'QuantiteMoyenneParVente': 4.7},
            
            # Mode pour les fêtes
            {'Saison': 'Automne', 'Categorie': 'Mode', 'QuantiteTotale': 75, 
             'CATotal': 15000, 'NombreVentes': 15, 'NombreProduitsVendus': 7, 
             'PanierMoyen': 1000, 'QuantiteMoyenneParVente': 5.0},
             
            # Maison pour décorations
            {'Saison': 'Automne', 'Categorie': 'Maison', 'QuantiteTotale': 65, 
             'CATotal': 12000, 'NombreVentes': 12, 'NombreProduitsVendus': 6, 
             'PanierMoyen': 1000, 'QuantiteMoyenneParVente': 5.4}
        ]
        
        # Mettre à jour les totaux automne existants
        seasonal_extended = seasonal.copy()
        
        for boost in autumn_boost:
            mask = (seasonal_extended['Saison'] == boost['Saison']) & (seasonal_extended['Categorie'] == boost['Categorie'])
            if mask.any():
                # Ajouter aux données existantes
                seasonal_extended.loc[mask, 'QuantiteTotale'] += boost['QuantiteTotale']
                seasonal_extended.loc[mask, 'CATotal'] += boost['CATotal']
                seasonal_extended.loc[mask, 'NombreVentes'] += boost['NombreVentes']
        
        # Recalculer les pourcentages
        seasonal_totals = seasonal_extended.groupby('Saison')['CATotal'].sum().reset_index()
        seasonal_totals.columns = ['Saison', 'CATotalSaison']
        
        seasonal_extended = seasonal_extended.merge(seasonal_totals, on='Saison', suffixes=('', '_new'))
        seasonal_extended['PourcentageCAParSaison'] = ((seasonal_extended['CATotal'] / seasonal_extended['CATotalSaison_new']) * 100).round(2)
        seasonal_extended = seasonal_extended.drop('CATotalSaison_new', axis=1)
        seasonal_extended['CATotalSaison'] = seasonal_extended.groupby('Saison')['CATotal'].transform('sum')
        
        # Export
        filepath = self.temporal_dir / "seasonal_analysis_extended.csv"
        seasonal_extended.to_csv(filepath, index=False, encoding='utf-8')
        
        print(f"✅ Analyse saisonnière étendue : {filepath}")
        return filepath

    def extend_all(self):
        """🚀 Extension complète des données temporelles"""
        print("🚀 EXTENSION COMPLÈTE DES DONNÉES TEMPORELLES")
        print("=" * 50)
        
        files_generated = []
        
        # 1. Extension mensuelle
        files_generated.append(self.extend_monthly_summary())
        
        # 2. Extension saisonnière
        files_generated.append(self.extend_seasonal_analysis())
        
        print(f"\n🎉 EXTENSION TERMINÉE !")
        print(f"📂 {len(files_generated)} fichiers étendus")
        
        print(f"\n💡 POUR POWER BI :")
        print(f"   1. Supprimez l'ancienne table sales_monthly_summary")
        print(f"   2. Importez sales_monthly_summary_extended.csv")
        print(f"   3. Recréez les relations")
        print(f"   4. Vos graphiques iront maintenant jusqu'en décembre 2025 !")
        
        return files_generated

def main():
    """Fonction principale"""
    extender = TemporalDataExtender()
    extender.extend_all()

if __name__ == "__main__":
    main()
