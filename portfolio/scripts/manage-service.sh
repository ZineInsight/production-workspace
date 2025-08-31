#!/bin/bash

# Script de gestion du service ZineInsight Portfolio
# Usage: ./manage-service.sh [start|stop|restart|status|logs]

SERVICE_NAME="zineinsight-portfolio"

case "$1" in
    start)
        echo "🚀 Démarrage du service..."
        sudo systemctl start $SERVICE_NAME
        ;;
    stop)
        echo "🛑 Arrêt du service..."
        sudo systemctl stop $SERVICE_NAME
        ;;
    restart)
        echo "🔄 Redémarrage du service..."
        sudo systemctl restart $SERVICE_NAME
        ;;
    status)
        echo "📊 Statut du service :"
        sudo systemctl status $SERVICE_NAME
        ;;
    logs)
        echo "📝 Logs du service (Ctrl+C pour quitter) :"
        sudo journalctl -u $SERVICE_NAME -f
        ;;
    app-logs)
        echo "📝 Logs de l'application (Ctrl+C pour quitter) :"
        tail -f logs/access.log logs/error.log
        ;;
    info)
        echo "ℹ️  Informations du service :"
        echo ""
        if systemctl is-active --quiet $SERVICE_NAME; then
            echo "✅ Statut : ACTIF"
            echo "🌐 Portfolio : http://$(hostname -I | awk '{print $1}'):5000/"
            echo "📊 Dashboard : http://$(hostname -I | awk '{print $1}'):5000/dashboard"
        else
            echo "❌ Statut : INACTIF"
        fi
        echo ""
        echo "🔧 Service activé au démarrage : $(systemctl is-enabled $SERVICE_NAME 2>/dev/null || echo 'non')"
        echo "📁 Dossier de travail : $(pwd)"
        echo "📝 Logs système : sudo journalctl -u $SERVICE_NAME"
        echo "📝 Logs app : tail -f logs/*.log"
        ;;
    *)
        echo "🔧 Gestionnaire de service ZineInsight Portfolio"
        echo ""
        echo "Usage: $0 {start|stop|restart|status|logs|app-logs|info}"
        echo ""
        echo "Commandes disponibles :"
        echo "  start     - Démarrer le service"
        echo "  stop      - Arrêter le service"
        echo "  restart   - Redémarrer le service"
        echo "  status    - Afficher le statut détaillé"
        echo "  logs      - Voir les logs système en temps réel"
        echo "  app-logs  - Voir les logs de l'application"
        echo "  info      - Afficher les informations générales"
        echo ""
        exit 1
        ;;
esac
