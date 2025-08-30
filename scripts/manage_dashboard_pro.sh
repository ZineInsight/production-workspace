#!/bin/bash

# 🚀 GESTIONNAIRE DASHBOARD PROFESSIONNEL - FastAPI
# Otmane Boulahia - Data Engineering Portfolio
# Solution ULTRA-FIABLE pour démos client

echo "📊 GESTIONNAIRE DASHBOARD PRO - FastAPI"
echo "========================================"
echo ""

# Fonction pour vérifier si un port est utilisé
check_port() {
    local port=$1
    if netstat -tlnp 2>/dev/null | grep ":$port " > /dev/null; then
        return 0  # Port utilisé
    else
        return 1  # Port libre
    fi
}

# Fonction pour démarrer le dashboard
start_dashboard() {
    echo "🚀 Démarrage du Dashboard Professionnel..."
    echo ""

    cd /var/www/production-workspace

    # Arrêter les anciens processus
    pkill -f "uvicorn.*dashboard_pro" 2>/dev/null
    sleep 2

    # Démarrer le dashboard FastAPI
    echo "📊 Dashboard Pro (port 8001)..."
    /var/www/production-workspace/.venv/bin/uvicorn dashboard_pro.main:app --host 0.0.0.0 --port 8001 --reload > dashboard_pro.log 2>&1 &

    # Attendre le démarrage
    echo "⏳ Démarrage en cours..."
    sleep 5

    echo ""
    echo "✅ Dashboard Pro lancé avec succès !"
    show_status
}

# Fonction pour afficher le statut
show_status() {
    echo ""
    echo "📋 ÉTAT DU DASHBOARD :"
    echo "====================="

    if check_port 8001; then
        echo "✅ 📊 Dashboard Pro : http://localhost:8001"
        echo "🌐 URL Publique    : http://91.99.237.55:8001"
    else
        echo "❌ 📊 Dashboard Pro : Arrêté"
    fi

    echo ""
    echo "🔄 Processus FastAPI actifs:"
    ps aux | grep uvicorn | grep -v grep | wc -l | xargs echo "   Nombre de processus:"

    echo ""
    echo "🎯 POUR VOS DÉMOS CLIENT :"
    echo "   http://91.99.237.55:8001"
}

# Fonction pour arrêter le dashboard
stop_dashboard() {
    echo "🛑 Arrêt du dashboard..."
    pkill -f "uvicorn.*dashboard_pro" 2>/dev/null
    sleep 2
    echo "✅ Dashboard arrêté"
}

# Menu principal
case "$1" in
    "start")
        start_dashboard
        ;;
    "stop")
        stop_dashboard
        ;;
    "status")
        show_status
        ;;
    "restart")
        stop_dashboard
        echo ""
        start_dashboard
        ;;
    "logs")
        echo "📜 LOGS DU DASHBOARD :"
        echo "====================="
        tail -50 /var/www/production-workspace/dashboard_pro.log 2>/dev/null || echo "Pas de logs disponibles"
        ;;
    *)
        echo "Usage: $0 {start|stop|status|restart|logs}"
        echo ""
        echo "Commandes disponibles:"
        echo "  start   - Démarre le dashboard professionnel"
        echo "  stop    - Arrête le dashboard"
        echo "  status  - Affiche l'état du dashboard"
        echo "  restart - Redémarre le dashboard"
        echo "  logs    - Affiche les logs du dashboard"
        echo ""
        echo "🎯 Dashboard conçu pour démos client - ULTRA FIABLE"
        echo ""
        show_status
        ;;
esac
