# TOPAD-Experiment

TOPAD-Experiment ist ein verhaltensökonomisches Experiment, entwickelt mit [oTree](https://www.otree.org/), einer Python-Plattform für Online-Experimente.

## Projektbeschreibung

Dieses Projekt implementiert ein "Take-or-Pass" (TOPAD) Entscheidungsspiel, bei dem Teilnehmer in mehreren Runden entscheiden müssen, ob sie einen Geldbetrag annehmen oder ablehnen. Die Positionen der Spieler und die Auszahlungsbeträge ändern sich in jeder Runde.

## Installation

1. Klonen Sie das Repository:
```
git clone https://github.com/YourUsername/TOPAD-Experiment.git
cd TOPAD-Experiment
```

2. Eine virtuelle Umgebung erstellen und aktivieren:
```
python -m venv venv
source venv/bin/activate  # Unter Windows: venv\Scripts\activate
```

3. Abhängigkeiten installieren:
```
pip install -r requirements.txt
```

## Konfiguration

Die Hauptkonfiguration befindet sich in der `settings.py`-Datei. Dort können Sie Folgendes anpassen:
- Anzahl der Teilnehmer
- Auszahlungsparameter
- Spielreihenfolge

## Ausführen des Experiments

Starten Sie den lokalen Server mit:
```
otree devserver
```

Das Experiment ist dann unter `http://localhost:8000` verfügbar.

## Projektstruktur

- `topad/`: Hauptmodul für das TOPAD-Spiel
- `stall_page/`, `control/`: Zusätzliche Module für das Experiment
- `_templates/`: HTML-Vorlagen
- `_static/`: Statische Dateien (CSS, JavaScript)
- Verschiedene Python-Skripte für Datenanalyse und Ergebnisvisualisierung

## Lizenz

Dieses Projekt steht unter der Lizenz, die in der [LICENSE](LICENSE)-Datei beschrieben ist.

## Hinweise zur Veröffentlichung

Vor der Veröffentlichung des Codes sollten folgende Schritte durchgeführt werden:

1. Entfernen oder ersetzen Sie sensible Daten:
   - Überprüfen Sie die `settings.py`-Datei auf hartcodierte Anmeldedaten
   - Stellen Sie sicher, dass keine persönlichen Pfade enthalten sind (z.B. in Analysis.py)
   - Erstellen Sie eine `.env.example`-Datei mit Platzhaltern für sensible Daten

2. Entfernen Sie experimentspezifische Daten:
   - Datenbank-Datei (`db.sqlite3`)
   - Teilnehmerinformationen

3. Stellen Sie sicher, dass die Dokumentation vollständig ist, um die Reproduzierbarkeit zu gewährleisten 