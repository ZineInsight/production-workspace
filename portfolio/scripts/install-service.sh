#!/bin/bash

# Script d'installation du service systemd pour ZineInsight Portfolio
# Ce script configure le portfolio pour qu'il reste toujours allumé

echo "🔧 Installation du service ZineInsight Portfolio..."

# Vérifier les permissions
if [ "$EUID" -ne 0 ]; then
    echo "❌ Ce script doit être exécuté en tant que root (avec sudo)"
    echo "Usage: sudo ./install-service.sh"
    exit 1
fi

# Vérifier qu'on est dans le bon dossier
if [ ! -f "backend/main.py" ]; then
    echo "❌ Erreur: Veuillez exécuter ce script depuis le dossier portfolio"
    exit 1
fi

# Arrêter l'ancien serveur s'il tourne
echo "🛑 Arrêt des anciens processus..."
pkill -f "python.*main.py" 2>/dev/null || true
pkill -f "gunicorn.*backend.main" 2>/dev/null || true

# Créer le dossier logs s'il n'existe pas
mkdir -p logs

# Installer les dépendances nécessaires
echo "📦 Installation de gunicorn si nécessaire..."
/var/www/production-workspace/.venv/bin/pip install gunicorn

# Copier le fichier de service
echo "📋 Installation du service systemd..."
cp zineinsight-portfolio.service /etc/systemd/system/

# Recharger systemd
echo "🔄 Rechargement de systemd..."
systemctl daemon-reload

# Activer le service (démarrage automatique au boot)
echo "✅ Activation du service au démarrage..."
systemctl enable zineinsight-portfolio

# Démarrer le service
echo "🚀 Démarrage du service..."
systemctl start zineinsight-portfolio

# Attendre un peu que le service démarre
sleep 3

# Vérifier le statut
echo "📊 Vérification du statut..."
if systemctl is-active --quiet zineinsight-portfolio; then
    echo "✅ Service démarré avec succès !"
    echo ""
    echo "📱 Votre portfolio est maintenant accessible sur :"
    echo "   🌐 Portfolio: http://$(hostname -I | awk '{print $1}'):5000/"
    echo "   📊 Dashboard: http://$(hostname -I | awk '{print $1}'):5000/dashboard"
    echo ""
    echo "🔧 Commandes utiles :"
    echo "   • Statut     : sudo systemctl status zineinsight-portfolio"
    echo "   • Arrêter    : sudo systemctl stop zineinsight-portfolio"
    echo "   • Redémarrer : sudo systemctl restart zineinsight-portfolio"
    echo "   • Logs       : sudo journalctl -u zineinsight-portfolio -f"
    echo "   • Logs app   : tail -f logs/access.log"
    echo ""
    echo "💡 Le service redémarrera automatiquement :"
    echo "   • En cas de crash"
    echo "   • Au redémarrage du serveur"
    echo "   • Plus besoin de terminal ouvert !"
else
    echo "❌ Erreur lors du démarrage du service"
    echo "📝 Vérifiez les logs avec : sudo journalctl -u zineinsight-portfolio"
    exit 1
fi
