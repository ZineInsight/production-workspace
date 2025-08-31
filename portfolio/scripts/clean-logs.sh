#!/bin/bash

# Script de nettoyage des logs
echo "🧹 Nettoyage des logs anciens..."

# Créer le dossier logs s'il n'existe pas
mkdir -p logs

# Sauvegarder les logs actuels avec timestamp
if [ -f "logs/access.log" ] && [ -s "logs/access.log" ]; then
    mv logs/access.log "logs/access_$(date +%Y%m%d_%H%M%S).log"
    echo "📦 Logs d'accès sauvegardés"
fi

if [ -f "logs/error.log" ] && [ -s "logs/error.log" ]; then
    mv logs/error.log "logs/error_$(date +%Y%m%d_%H%M%S).log"
    echo "📦 Logs d'erreur sauvegardés"
fi

# Créer de nouveaux fichiers de logs vides
touch logs/access.log
touch logs/error.log

# Supprimer les logs plus anciens que 30 jours
find logs/ -name "*.log" -type f -mtime +30 -delete

echo "✅ Nettoyage terminé !"
echo "📊 Logs actuels :"
ls -la logs/
