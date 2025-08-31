#!/bin/bash

# Script de démarrage pour le portfolio ZineInsight

echo "🚀 Démarrage du portfolio ZineInsight..."

# Vérifier si on est dans le bon dossier
if [ ! -f "backend/main.py" ]; then
    echo "❌ Erreur: Veuillez exécuter ce script depuis le dossier portfolio"
    exit 1
fi

# Activer l'environnement virtuel si disponible
if [ -d "../.venv" ]; then
    echo "🐍 Activation de l'environnement virtuel..."
    source ../.venv/bin/activate
fi

# Installer les dépendances si nécessaire
if [ ! -f ".dependencies_installed" ]; then
    echo "📦 Installation des dépendances..."
    pip install -r requirements.txt
    touch .dependencies_installed
fi

# Exporter les variables d'environnement
export FLASK_APP=backend/main.py
export FLASK_ENV=development
export FLASK_DEBUG=True

# Démarrer le serveur Flask
echo "🌐 Démarrage du serveur sur http://localhost:5000"
echo "📊 Dashboard disponible sur http://localhost:5000/dashboard"
echo ""
echo "Appuyez sur Ctrl+C pour arrêter le serveur"
echo ""

python backend/main.py
