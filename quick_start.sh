#!/bin/bash

# 🚀 LANCEMENT RAPIDE DES DASHBOARDS SÉLECTIONNÉS
# Otmane Boulahia - Data Engineering Portfolio
# Dashboards 8503 (Compact) et 8504 (Greenweez)

echo "🚀 Lancement rapide des dashboards..."
echo "====================================="

# Aller dans le bon répertoire
cd /var/www/production-workspace

# Utiliser le gestionnaire principal
./manage_dashboards.sh start

echo ""
echo "🌐 Vos dashboards sont prêts :"
echo "   📑 Dashboard Compact  : http://localhost:8503"
echo "   🌱 Dashboard Greenweez: http://localhost:8504"
echo ""
echo "💡 Commandes utiles :"
echo "   ./quick_start.sh              - Ce script (démarrage rapide)"
echo "   ./manage_dashboards.sh stop   - Arrêter les dashboards"
echo "   ./manage_dashboards.sh status - Voir l'état"
