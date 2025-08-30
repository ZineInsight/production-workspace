from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <html>
        <head><title>Test Flask</title></head>
        <body>
            <h1>🎯 Test Flask Serveur</h1>
            <p>Si vous voyez cette page, le serveur web fonctionne parfaitement !</p>
            <p>Le problème vient donc spécifiquement de <strong>Streamlit</strong>.</p>
            <hr>
            <h2>Diagnostic :</h2>
            <ul>
                <li>✅ Serveur web : OK</li>
                <li>✅ Réseau : OK</li>
                <li>❌ Streamlit : Problème</li>
            </ul>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8504, debug=True)
