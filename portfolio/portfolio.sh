#!/bin/bash

# Script principal de gestion du portfolio ZineInsight
# Usage: ./portfolio.sh [commande]

SCRIPT_DIR="scripts"

show_help() {
    echo "🎯 Portfolio ZineInsight - Gestionnaire Principal"
    echo ""
    echo "Usage: ./portfolio.sh [commande]"
    echo ""
    echo "📋 Commandes disponibles :"
    echo "  dev        Démarrer en mode développement"
    echo "  install    Installer le service systemd"
    echo "  start      Démarrer le service"
    echo "  stop       Arrêter le service"
    echo "  restart    Redémarrer le service"
    echo "  status     Voir le statut du service"
    echo "  info       Informations complètes"
    echo "  logs       Voir les logs système"
    echo "  app-logs   Voir les logs de l'application"
    echo "  clean      Nettoyer les anciens logs"
    echo "  health     Vérifier la santé de l'application"
    echo "  deploy     Déployer en mode production"
    echo ""
    echo "📁 Structure :"
    echo "  backend/     Application Flask"
    echo "  static/      CSS, JS, assets"
    echo "  templates/   Templates HTML"
    echo "  scripts/     Scripts de gestion"
    echo "  docs/        Documentation"
    echo ""
    echo "🌐 URLs (une fois démarré) :"
    echo "  http://localhost:5000/           Portfolio"
    echo "  http://localhost:5000/dashboard  Dashboard"
    echo "  http://localhost:5000/api/...    API REST"
}

case "$1" in
    dev)
        echo "🚀 Démarrage en mode développement..."
        ./$SCRIPT_DIR/start.sh
        ;;
    install)
        echo "🔧 Installation du service systemd..."
        ./$SCRIPT_DIR/install-service.sh
        ;;
    start|stop|restart|status|info|logs|app-logs)
        ./$SCRIPT_DIR/manage-service.sh $1
        ;;
    clean)
        ./$SCRIPT_DIR/clean-logs.sh
        ;;
    health)
        ./$SCRIPT_DIR/health-check.sh
        ;;
    deploy)
        echo "🚀 Déploiement en production..."
        ./$SCRIPT_DIR/deploy.sh
        ;;
    help|--help|-h)
        show_help
        ;;
    "")
        show_help
        ;;
    *)
        echo "❌ Commande inconnue: $1"
        echo ""
        show_help
        exit 1
        ;;
esac
