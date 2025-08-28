#!/usr/bin/env python3
"""
🎯 SERVEUR SIMPLE POUR TEST API - AVEC LOGS DÉTAILLÉS
====================================================
Version allégée pour débugger la connexion API avec logs complets
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os
import logging
from datetime import datetime
import traceback

# Configuration des logs
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from algorithms_historical.algo_expat import AlgorithmeExpat

app = Flask(__name__)
CORS(app, origins=["https://zineinsight.com", "http://localhost:3000", "http://127.0.0.1", "http://localhost"])

# Initialisation de l'algorithme
print("🚀 Initialisation de l'algorithme...")
logger.info("🚀 Starting algorithm initialization...")
try:
    algo = AlgorithmeExpat()
    countries_count = len(algo.get_available_countries())
    print(f"✅ Algorithme expat prêt - {countries_count} pays")
    logger.info(f"✅ Expat algorithm ready - {countries_count} countries")
except Exception as e:
    print(f"❌ Erreur initialisation: {str(e)}")
    logger.error(f"❌ Algorithm initialization failed: {str(e)}")
    logger.error(traceback.format_exc())
    sys.exit(1)

@app.before_request
def log_request():
    logger.info(f"📥 {request.method} {request.url} - IP: {request.remote_addr}")
    logger.info(f"📋 Headers: {dict(request.headers)}")
    if request.is_json:
        logger.info(f"📦 Body: {request.get_json()}")

@app.after_request
def log_response(response):
    logger.info(f"📤 Response: {response.status_code} - {response.status}")
    return response

@app.route('/health', methods=['GET'])
def health():
    logger.info("🔍 Health check requested")
    return jsonify({
        "status": "ok",
        "algorithm": "ready",
        "countries": len(algo.get_supported_countries()),
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/health', methods=['GET'])
def api_health():
    logger.info("🔍 API Health check requested")
    return jsonify({
        "status": "ok",
        "algorithm": "ready",
        "countries": len(algo.get_supported_countries()),
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/calculate', methods=['POST', 'OPTIONS'])
def calculate():
    logger.info(f"🎯 Calculate endpoint called - Method: {request.method}")

    if request.method == 'OPTIONS':
        logger.info("🔄 Handling CORS preflight")
        response = jsonify({})
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return response

    try:
        logger.info("📝 Processing calculate request...")

        # Récupération des données
        data = request.get_json()
        if not data:
            logger.error("❌ No JSON data received")
            return jsonify({"success": False, "error": "No data provided"}), 400

        answers = data.get('answers', {})
        logger.info(f"🎯 Received answers: {answers}")

        # Extraction du pays
        country = 'france'  # Par défaut

        # Chercher le pays dans les réponses
        for key, value in answers.items():
            if 'country' in key.lower() or key == 'pays':
                country = value
                logger.info(f"🌍 Country extracted from key '{key}': {country}")
                break

        # Si pas trouvé, chercher dans les valeurs
        if country == 'france':
            for key, value in answers.items():
                if isinstance(value, str) and value.lower() in ['france', 'canada', 'usa', 'uk', 'spain', 'germany']:
                    country = value.lower()
                    logger.info(f"🌍 Country found in values: {country}")
                    break

        logger.info(f"🎯 Final country selected: {country}")

        # Analyse avec l'algorithme
        logger.info("🧠 Starting algorithm analysis...")
        result = algo.analyser(answers, country)

        logger.info(f"✅ Algorithm result: success={result.get('success', False)}")

        if result.get('success', False):
            recommendations = result.get('recommendations', [])[:3]  # Top 3
            logger.info(f"🏆 Found {len(recommendations)} recommendations")

            for i, city in enumerate(recommendations, 1):
                logger.info(f"   {i}. {city.get('nom', 'N/A')} - Score: {city.get('score_final', 0)}")

            response_data = {
                "success": True,
                "recommendations": recommendations,
                "country": country,
                "timestamp": datetime.now().isoformat()
            }
            logger.info("📤 Sending successful response")
            return jsonify(response_data)
        else:
            error_msg = result.get('error', 'Unknown error')
            logger.error(f"❌ Algorithm failed: {error_msg}")
            return jsonify({
                "success": False,
                "error": error_msg,
                "country": country,
                "timestamp": datetime.now().isoformat()
            }), 400

    except Exception as e:
        error_msg = str(e)
        logger.error(f"❌ Exception in calculate: {error_msg}")
        logger.error(f"🔍 Traceback: {traceback.format_exc()}")
        return jsonify({
            "success": False,
            "error": error_msg,
            "timestamp": datetime.now().isoformat()
        }), 500

@app.errorhandler(404)
def not_found(error):
    logger.warning(f"❌ 404 Not Found: {request.url}")
    return jsonify({"error": "Not Found", "url": request.url}), 404

@app.errorhandler(500)
def internal_error(error):
    logger.error(f"❌ 500 Internal Error: {str(error)}")
    return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    print("\n🎯 SERVEUR SIMPLE - ZINEINSIGHT AVEC LOGS")
    print("="*50)
    print(f"🌐 Port: 8000")
    print(f"📊 Algorithme: {len(algo.get_available_countries())} pays")
    print(f"📝 Logs: DEBUG level activated")
    print(f"🕒 Démarrage: {datetime.now().isoformat()}")
    print("="*50)

    logger.info("🚀 Starting Flask server...")

    try:
        app.run(host='0.0.0.0', port=8000, debug=True, threaded=True)
    except Exception as e:
        logger.error(f"❌ Failed to start server: {str(e)}")
        print(f"❌ Erreur serveur: {str(e)}")
        sys.exit(1)
