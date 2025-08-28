"""
🎯 REVOLUTIONARY TEST SERVER - Quick Test
=======================================
"""

from flask import Flask, jsonify
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def homepage():
    """Test simple"""
    return jsonify({
        "message": "🎯 Revolutionary Backend TEST - ZineInsight Intelligence Platform",
        "version": "1.0.0-test",
        "services": {
            "zscore": {"name": "Geographic Intelligence", "endpoint": "/api/calculate"},
            "skillgraph": {"name": "Career Intelligence", "endpoint": "/api/career"},
            "wealth": {"name": "Wealth Intelligence", "endpoint": "/api/wealth"}
        },
        "status": "operational",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/health')
def health():
    return jsonify({"status": "healthy", "timestamp": datetime.now().isoformat()})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8001))
    print(f"🚀 Revolutionary TEST Server on port {port}")
    app.run(host='0.0.0.0', port=port, debug=False)
