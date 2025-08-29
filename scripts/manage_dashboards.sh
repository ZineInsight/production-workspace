#!/bin/bash

# 🚀 GESTIONNAIRE MULTI-DASHBOARDS STREAMLIT
# Otmane Boulahia - Data Engineering Por        echo "  start   - Démarre les 2 dashboards sélectionnés"
        echo "  stop    - Arrête tous les dashboards"
        echo "  status  - Affiche l'état des dashboards"
        echo "  restart - Redémarre les dashboards"io
# Gestion intelligente de tous les dashboards

echo "📊 GESTIONNAIRE DASHBOARDS STREAMLIT"
echo "====================================="
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

# Fonction pour démarrer tous les dashboards
start_all_dashboards() {
    echo "🚀 Démarrage des dashboards sélectionnés..."
    echo ""

    cd /var/www/production-workspace

    # Arrêter tous les processus Streamlit existants
    pkill -f streamlit 2>/dev/null
    sleep 2

    # Démarrer les 2 dashboards sélectionnés
    echo "📑 Dashboard Compact (port 8503)..."
    /var/www/production-workspace/.venv/bin/python -m streamlit run streamlit_dev/compact_dashboard.py --server.headless true --server.address 0.0.0.0 --server.port 8503 > compact.log 2>&1 &

    echo "🌱 Dashboard Greenweez (port 8504)..."
    /var/www/production-workspace/.venv/bin/python -m streamlit run streamlit_dev/greenweez_dashboard.py --server.headless true --server.address 0.0.0.0 --server.port 8504 > greenweez.log 2>&1 &

    # Attendre que tous démarrent
    echo "⏳ Démarrage en cours..."
    sleep 8

    echo ""
    echo "✅ Les 2 dashboards sont lancés !"
    show_status
}

# Fonction pour afficher le statut
show_status() {
    echo ""
    echo "📋 ÉTAT DES DASHBOARDS:"
    echo "======================="

    declare -A dashboards
    dashboards[8503]="📑 Dashboard Compact"
    dashboards[8504]="🌱 Dashboard Greenweez"

    for port in 8503 8504; do
        if check_port $port; then
            echo "✅ ${dashboards[$port]} : http://localhost:$port"
        else
            echo "❌ ${dashboards[$port]} : Arrêté"
        fi
    done

    echo ""
    echo "🔄 Processus Streamlit actifs:"
    ps aux | grep streamlit | grep -v grep | wc -l | xargs echo "   Nombre de processus:"
}

# Fonction pour arrêter tous les dashboards
stop_all_dashboards() {
    echo "🛑 Arrêt de tous les dashboards..."
    pkill -f streamlit 2>/dev/null
    sleep 2
    echo "✅ Tous les dashboards ont été arrêtés"
}

# Menu principal
case "$1" in
    "start")
        start_all_dashboards
        ;;
    "stop")
        stop_all_dashboards
        ;;
    "status")
        show_status
        ;;
    "restart")
        stop_all_dashboards
        echo ""
        start_all_dashboards
        ;;
    *)
        echo "Usage: $0 {start|stop|status|restart}"
        echo ""
        echo "Commandes disponibles:"
        echo "  start   - Démarre tous les 4 dashboards"
        echo "  stop    - Arrête tous les dashboards"
        echo "  status  - Affiche l'état de tous les dashboards"
        echo "  restart - Redémarre tous les dashboards"
        echo ""
        show_status
        ;;
esac
