#!/bin/bash

# 🚀 DASHBOARD LAUNCHER SCRIPT
# Otmane Boulahia - Data Engineering Portfolio
# Script pour lancer facilement les différentes versions du dashboard

echo "📊 DASHBOARD LAUNCHER - Portfolio Analytics"
echo "=========================================="
echo "Otmane Boulahia - Data Engineer"
echo ""

# Navigation du répertoire
cd /var/www/production-workspace

# Arrêter tous les processus Streamlit existants
echo "🔄 Arrêt des processus Streamlit existants..."
pkill -f streamlit 2>/dev/null

echo ""
echo "Choisissez votre dashboard:"
echo "1.  Dashboard Compact (Navigation Onglets)"
echo "2. 🌱 Dashboard Greenweez Bio (Noms produits + CSS responsive)"
echo ""

read -p "Votre choix (1-2): " choice

case $choice in
    1)
        echo "🚀 Lancement Dashboard Compact (Onglets)..."
        /var/www/production-workspace/.venv/bin/python -m streamlit run streamlit_dev/compact_dashboard.py --server.headless true --server.address 0.0.0.0 --server.port 8503
        ;;
    2)
        echo "🌱 Lancement Dashboard Greenweez Bio (Responsive + Noms produits)..."
        /var/www/production-workspace/.venv/bin/python -m streamlit run streamlit_dev/greenweez_dashboard.py --server.headless true --server.address 0.0.0.0 --server.port 8504
        ;;
    *)
        echo "❌ Choix invalide. Utilisation: 1 ou 2"
        exit 1
        ;;
esac