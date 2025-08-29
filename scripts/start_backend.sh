#!/bin/bash

# Script pour démarrer le backend en mode production stable
echo "🚀 Starting ZineInsight Backend..."

cd /var/www/production-workspace/backend

# Tuer les processus existants
pkill -f "python.*main.py" 2>/dev/null

# Attendre un peu
sleep 2

# Démarrer le backend
echo "🌍 Starting on port 8000..."
python3 main.py > /tmp/backend.log 2>&1 &

# Attendre que le serveur démarre
sleep 5

# Vérifier que le serveur tourne
if netstat -tlnp | grep -q ":8000"; then
    echo "✅ Backend started successfully on port 8000"
    echo "📊 Processes:"
    ps aux | grep -E "(python.*main.py)" | grep -v grep
else
    echo "❌ Backend failed to start"
    echo "📋 Last logs:"
    tail -10 /tmp/backend.log
fi
