#!/bin/bash

# Script d'automatisation pour l'analyse BigQuery
# Usage: ./setup.sh

echo "🚀 Configuration du projet BigQuery Analytics"

# Créer l'environnement virtuel Python si nécessaire
if [ ! -d "venv" ]; then
    echo "📦 Création de l'environnement virtuel..."
    python3 -m venv venv
fi

# Activer l'environnement virtuel
echo "🔧 Activation de l'environnement virtuel..."
source venv/bin/activate

# Installer les dépendances
echo "📚 Installation des dépendances..."
pip install --upgrade pip
pip install -r requirements.txt

# Vérifier la configuration
if [ ! -f ".env" ]; then
    echo "⚠️  Fichier .env manquant!"
    echo "📋 Copiez .env.example vers .env et configurez vos paramètres:"
    echo "   cp .env.example .env"
    echo "   nano .env  # Éditez avec vos paramètres"
else
    echo "✅ Fichier .env trouvé"
fi

# Créer les dossiers nécessaires
mkdir -p data visualizations logs

echo ""
echo "✅ Configuration terminée!"
echo ""
echo "Prochaines étapes:"
echo "1. Configurez votre fichier .env avec vos credentials BigQuery"
echo "2. Lancez l'analyse avec: python quick_start.py"
echo "3. Ou ouvrez directement Jupyter: jupyter notebook notebooks/bigquery_analysis.ipynb"
echo ""
echo "🎯 Votre projet est prêt à analyser vos données BigQuery!"
