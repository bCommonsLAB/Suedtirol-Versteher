# Südtirol-Versteher README
![image](https://github.com/bCommonsLAB/Suedtirol-Versteher/assets/174307404/92de5605-f0e4-4568-96c0-e5d47afed427)
Einführung
Willkommen zu deinem Südtirol-Versteher-Projekt! Diese Anwendung ist ein German/Italian Speech-to-Text Bot mit Übersetzungs- und Zusammenfassungsfunktion. Diese Anleitung erklärt dir Schritt für Schritt, wie du deinen Python-Server startest und sicherstellst, dass alle Dateien im selben Verzeichnis liegen.

Voraussetzungen
Python muss auf deinem System installiert sein. Du kannst Python von der offiziellen Website herunterladen und installieren.
Der Paketmanager pip sollte ebenfalls installiert sein, um die notwendigen Pakete zu installieren.
Installation
Bevor du den Server startest, müssen einige Python-Pakete installiert werden. Öffne ein Terminal oder eine Eingabeaufforderung und führe die folgenden Befehle aus:

bash
Code kopieren
pip install Flask Flask-CORS openai
Diese Befehle installieren die folgenden Pakete:

Flask: Ein leichtes WSGI Web Application Framework.
Flask-CORS: Eine Erweiterung für Flask, die Cross-Origin Resource Sharing (CORS) unterstützt.
openai: Eine Python-Bibliothek für die OpenAI-API.
Projektstruktur
Stelle sicher, dass alle Dateien im selben Verzeichnis liegen. Deine Projektstruktur sollte folgendermaßen aussehen:

arduino
Code kopieren
/dein-projekt-verzeichnis
    ├── .gitignore
    ├── README.md
    ├── app.py
    ├── background.js
    ├── config.py
    ├── index.html
    ├── recorder.js
    └── styles.css
Konfigurationsdatei config.py

Sie müssem in der Konfigurationsdatei namens config.py ihren OpenAI API-Schlüssel einfügen.
'''myopenkey = 'put your api key here''''

python
Code kopieren
from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import config

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Willkommen zum Südtirol-Versteher!"

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    openai.api_key = config.myopenkey

    response = openai.ChatCompletion.create(
        model=config.modelname,
        messages=[
            {"role": "system", "content": config.prompt}
        ]
    )

    return jsonify(response.choices[0].message['content'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
Starten des Servers
Um den Server zu starten, öffne ein Terminal oder eine Eingabeaufforderung im Verzeichnis, in dem sich deine app.py befindet, und führe folgenden Befehl aus:

bash
Code kopieren
python app.py
Dein Server sollte nun laufen und unter http://localhost:5000 erreichbar sein.

Verwendung der Anwendung
Öffne die index.html Datei in deinem Browser, um die Sprach-zu-Text-Funktionalität sowie die Übersetzungs- und Zusammenfassungsfunktionen zu nutzen. Weitere Funktionen und Anweisungen findest du in den entsprechenden JavaScript-Dateien (background.js und recorder.js) sowie in der styles.css Datei für das Styling.

Kontakt und Support
Wenn du Fragen oder Probleme hast, zögere nicht, uns zu kontaktieren.

Viel Erfolg und Spaß mit deinem Südtirol-Versteher-Projekt!
