#!/bin/bash

# Script de déploiement en production pour le portfolio ZineInsight

echo "🚀 Déploiement en production du portfolio ZineInsight..."

# Vérifier si on est dans le bon dossier
if [ ! -f "backend/main.py" ]; then
    echo "❌ Erreur: Veuillez exécuter ce script depuis le dossier portfolio"
    exit 1
fi

# Activer l'environnement virtuel
if [ -d "../.venv" ]; then
    echo "🐍 Activation de l'environnement virtuel..."
    source ../.venv/bin/activate
fi

# Installer les dépendances
echo "📦 Installation des dépendances de production..."
pip install -r requirements.txt

# Configuration pour la production
export FLASK_ENV=production
export FLASK_DEBUG=False

# Vérifier que gunicorn est installé
if ! command -v gunicorn &> /dev/null; then
    echo "⚠️ Gunicorn non trouvé, installation..."
    pip install gunicorn
fi

# Créer le fichier PID si nécessaire
mkdir -p logs

# Arrêter le serveur s'il existe déjà
if [ -f "logs/portfolio.pid" ]; then
    echo "🛑 Arrêt du serveur existant..."
    kill $(cat logs/portfolio.pid) 2>/dev/null || true
    rm -f logs/portfolio.pid
fi

# Démarrer le serveur Gunicorn
echo "🌐 Démarrage du serveur de production avec Gunicorn..."
echo "📊 Portfolio disponible sur http://91.99.237.55:5000"
echo "📊 Dashboard disponible sur http://91.99.237.55:5000/dashboard"

# Lancer en arrière-plan avec Gunicorn
gunicorn \
    --bind 0.0.0.0:5000 \
    --workers 4 \
    --worker-class sync \
    --timeout 120 \
    --keepalive 5 \
    --max-requests 1000 \
    --max-requests-jitter 100 \
    --preload \
    --pid logs/portfolio.pid \
    --access-logfile logs/access.log \
    --error-logfile logs/error.log \
    --log-level info \
    --daemon \
    backend.main:app

echo "✅ Serveur démarré en mode production !"
echo "📝 Logs disponibles dans le dossier logs/"
echo "🔧 Pour arrêter : kill \$(cat logs/portfolio.pid)"
