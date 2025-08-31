#!/bin/bash

# Script de vérification de santé du portfolio

echo "🔍 Vérification de santé du Portfolio ZineInsight..."
echo ""

# Vérifier si le service est actif
if systemctl is-active --quiet zineinsight-portfolio 2>/dev/null; then
    echo "✅ Service systemd : ACTIF"
    SERVICE_STATUS="✅"
else
    echo "❌ Service systemd : INACTIF"
    SERVICE_STATUS="❌"
fi

# Vérifier si l'application répond
HTTP_STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:5000/health 2>/dev/null)
if [ "$HTTP_STATUS" = "200" ]; then
    echo "✅ Application web : RÉPOND (HTTP $HTTP_STATUS)"
    WEB_STATUS="✅"
else
    echo "❌ Application web : NE RÉPOND PAS (HTTP $HTTP_STATUS)"
    WEB_STATUS="❌"
fi

# Vérifier les fichiers essentiels
ESSENTIAL_FILES=("backend/main.py" "static/css/portfolio.css" "templates/index.html" ".env")
FILES_OK=true

for file in "${ESSENTIAL_FILES[@]}"; do
    if [ -f "$file" ]; then
        echo "✅ Fichier $file : PRÉSENT"
    else
        echo "❌ Fichier $file : MANQUANT"
        FILES_OK=false
    fi
done

# Vérifier les logs
if [ -d "logs" ]; then
    echo "✅ Dossier logs : PRÉSENT"
    LOG_COUNT=$(ls -1 logs/*.log 2>/dev/null | wc -l)
    echo "📊 Nombre de fichiers de logs : $LOG_COUNT"
else
    echo "❌ Dossier logs : MANQUANT"
    mkdir -p logs
    echo "📁 Dossier logs créé"
fi

# Résumé
echo ""
echo "📊 RÉSUMÉ DE SANTÉ :"
echo "  Service systemd : $SERVICE_STATUS"
echo "  Application web : $WEB_STATUS"
echo "  Fichiers essentiels : $([ "$FILES_OK" = true ] && echo "✅" || echo "❌")"

# URLs de test
if [ "$WEB_STATUS" = "✅" ]; then
    IP=$(hostname -I | awk '{print $1}')
    echo ""
    echo "🌐 URLs de test :"
    echo "  Portfolio : http://$IP:5000/"
    echo "  Dashboard : http://$IP:5000/dashboard"
    echo "  API Health: http://$IP:5000/health"
fi

# Suggestions
echo ""
echo "🔧 ACTIONS SUGGÉRÉES :"
if [ "$SERVICE_STATUS" = "❌" ]; then
    echo "  - Installer/démarrer le service : ./portfolio.sh install"
fi
if [ "$WEB_STATUS" = "❌" ]; then
    echo "  - Vérifier les logs : ./portfolio.sh logs"
    echo "  - Redémarrer le service : ./portfolio.sh restart"
fi
if [ "$FILES_OK" = false ]; then
    echo "  - Vérifier l'intégrité des fichiers du projet"
fi

echo ""
echo "✅ Vérification terminée !"
