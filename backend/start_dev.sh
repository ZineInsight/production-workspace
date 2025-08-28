#!/bin/bash
# 🎯 REVOLUTIONARY BACKEND - SCRIPT DE DÉMARRAGE POUR TESTS
# ======================================================
# Script pour lancer le backend révolutionnaire sur port 9000
# Usage: ./start_dev.sh

echo "🚀 REVOLUTIONARY BACKEND - Starting Development Server"
echo "=============================================="
echo "📊 Services: ZScore + SkillGraph + Wealth"
echo "🌍 Port: 9000 (pour éviter conflit avec production 8000)"
echo "📁 Data: $(find /var/www/Revolutionnary/platform/backend/data -name '*.json' | wc -l) fichiers JSON"
echo ""

cd /var/www/Revolutionnary/platform/backend

# Vérifier les dépendances
if ! python3 -c "import flask" 2>/dev/null; then
    echo "❌ Flask manquant, installation..."
    pip3 install flask flask-cors stripe
fi

# Variables d'environnement de développement
export PORT=9000
export FLASK_ENV=development
export SECRET_KEY=dev-key-revolutionary-backend

# Lancer le serveur
echo "🎯 Lancement sur http://localhost:9000"
echo "📱 Endpoints disponibles:"
echo "  GET  /                     → Homepage avec tous les services"
echo "  POST /api/calculate        → ZScore Intelligence (🏙️)"
echo "  POST /api/career          → SkillGraph Intelligence (💼)"
echo "  POST /api/wealth          → Wealth Intelligence (💰)"
echo "  GET  /api/health          → Health check global"
echo ""
echo "🛑 Pour arrêter: Ctrl+C"
echo ""

python3 main.py
