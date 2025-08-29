#!/bin/bash
# 🔐 Setup authentification Google Cloud
echo "🔐 Configuration authentification BigQuery..."

# Option 1: Authentification utilisateur (plus simple)
echo "Exécutez cette commande pour vous authentifier:"
echo "gcloud auth application-default login"

# Option 2: Service Account (plus pro)
echo ""
echo "Ou placez votre fichier de service account dans:"
echo "data/config/bigquery-credentials.json"
