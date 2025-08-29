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
echo "1. 📊 Dashboard Original (Simple & Efficace)"
echo "2. 🚀 Dashboard Avancé (Multi-pages + Analytics)"
echo "3. 📑 Dashboard Compact (Navigation Onglets)"
echo "4. 🌱 Dashboard Greenweez Bio (Noms produits + CSS responsive)"
echo "5. 🔍 Comparaison des 4 versions"
echo ""

read -p "Votre choix (1-5): " choice

case $choice in
    1)
        echo "🚀 Lancement Dashboard Original..."
        /var/www/production-workspace/.venv/bin/python -m streamlit run streamlit_dev/portfolio_dashboard.py --server.headless true --server.address 0.0.0.0 --server.port 8501
        ;;
    2)
        echo "🚀 Lancement Dashboard Avancé (Multi-pages)..."
        /var/www/production-workspace/.venv/bin/python -m streamlit run streamlit_dev/advanced_dashboard.py --server.headless true --server.address 0.0.0.0 --server.port 8501
        ;;
    3)
        echo "🚀 Lancement Dashboard Compact (Onglets)..."
        /var/www/production-workspace/.venv/bin/python -m streamlit run streamlit_dev/compact_dashboard.py --server.headless true --server.address 0.0.0.0 --server.port 8501
        ;;
    4)
        echo "🌱 Lancement Dashboard Greenweez Bio (Responsive + Noms produits)..."
        /var/www/production-workspace/.venv/bin/python -m streamlit run streamlit_dev/greenweez_dashboard.py --server.headless true --server.address 0.0.0.0 --server.port 8501
        ;;
    5)
        echo "🚀 Lancement des 4 versions en parallèle..."
        echo "📊 Dashboard Original: http://localhost:8501"
        echo "🚀 Dashboard Avancé: http://localhost:8502"
        echo "📑 Dashboard Compact: http://localhost:8503"
        echo "🌱 Dashboard Greenweez: http://localhost:8504"
        echo ""

        /var/www/production-workspace/.venv/bin/python -m streamlit run streamlit_dev/portfolio_dashboard.py --server.headless true --server.address 0.0.0.0 --server.port 8501 &
        /var/www/production-workspace/.venv/bin/python -m streamlit run streamlit_dev/advanced_dashboard.py --server.headless true --server.address 0.0.0.0 --server.port 8502 &
        /var/www/production-workspace/.venv/bin/python -m streamlit run streamlit_dev/compact_dashboard.py --server.headless true --server.address 0.0.0.0 --server.port 8503 &
        /var/www/production-workspace/.venv/bin/python -m streamlit run streamlit_dev/greenweez_dashboard.py --server.headless true --server.address 0.0.0.0 --server.port 8504 &

        echo "✅ Les 4 dashboards sont maintenant accessibles!"
        wait
        ;;
    *)
        echo "❌ Choix invalide. Utilisation: 1, 2, 3, 4 ou 5"
        exit 1
        ;;
esac