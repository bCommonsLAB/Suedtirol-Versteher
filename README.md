# Südtirol-Versteher README





## Einführung

Willkommen zu deinem Südtirol-Versteher-Projekt! Diese Anwendung ist ein German/Italian Speech-to-Text Bot mit Übersetzungs- und Zusammenfassungsfunktion. Diese Anleitung erklärt dir Schritt für Schritt, wie du deinen Python-Server startest und sicherstellst, dass alle Dateien im selben Verzeichnis liegen.

## Voraussetzungen

- Python muss auf deinem System installiert sein. Du kannst Python von der [offiziellen Website](https://www.python.org/) herunterladen und installieren.
- Der Paketmanager `pip` sollte ebenfalls installiert sein, um die notwendigen Pakete zu installieren.

## Installation

Bevor du den Server startest, müssen einige Python-Pakete installiert werden. Öffne ein Terminal oder eine Eingabeaufforderung und führe die folgenden Befehle aus:

```bash
pip install Flask Flask-CORS openai
```

Diese Befehle installieren die folgenden Pakete:
- `Flask`: Ein leichtes WSGI Web Application Framework.
- `Flask-CORS`: Eine Erweiterung für Flask, die Cross-Origin Resource Sharing (CORS) unterstützt.
- `openai`: Eine Python-Bibliothek für die OpenAI-API.

## Projektstruktur

Stelle sicher, dass alle Dateien im selben Verzeichnis liegen. Deine Projektstruktur sollte folgendermaßen aussehen:

```
/dein-projekt-verzeichnis
    ├── .gitignore
    ├── README.md
    ├── app.py
    ├── background.js
    ├── config.py
    ├── index.html
    ├── loader.css
    ├── recorder.js
    └── styles.css
    
```

## Konfigurationsdatei `config.py`

Öffne die Konfigurationsdatei namens `config.py` und füge ihren OpenAI API-Schlüssel dort hinzu. So müsste es am anfang ausehen:

```python
myopenkey = 'put your api key here'
```

## Starten des Servers

Um den Server zu starten, öffne ein Terminal oder eine Eingabeaufforderung im Verzeichnis, in dem sich deine `app.py` befindet, und führe folgenden Befehl aus:

```bash
python app.py
```

Dein Server sollte nun laufen und unter `http://localhost:5000` erreichbar sein.

## Verwendung der Anwendung

Öffne die `index.html` Datei in deinem Browser, um die Sprach-zu-Text-Funktionalität sowie die Übersetzungs- und Zusammenfassungsfunktionen zu nutzen. Weitere Funktionen und Anweisungen findest du in den entsprechenden JavaScript-Dateien (`background.js` und `recorder.js`) sowie in der `styles.css` Datei für das Styling.

## Kontakt und Support

Wenn du Fragen oder Probleme hast, zögere nicht, uns zu kontaktieren.Für weitere Informationen zu diesem und anderen Projekten schaue hier nach: https://www.bcommonslab.org/

Wenn du die Anwendung ausprobieren möchtest, mache das gerne hier: 
[Suedtirol Verteher](https://app.bcommonslab.org/suedtirolversteher/)

Viel Erfolg und Spaß mit deinem Südtirol-Versteher-Projekt!
