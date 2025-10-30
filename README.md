# STADS Data Boot Camp

Wir haben am Advanced-Track des „Halloween Challenge“ im Rahmen des STADS Data Boot Camps 2025 teilgenommen. In diesem Projekt haben wir praktische Erfahrungen im Bereich Machine Learning gesammelt.

## Kernaktivitäten & Lernergebnisse
- Datenaufbereitung (Data Cleaning): Umgang mit fehlenden Werten, Formatierung und Vorbereitung von Datensätzen für die Analyse.
- Datenvisualisierung (Data Visualization): Erkundung von Mustern und Erkenntnissen mittels grafischer Darstellungen.
- Einführung in Machine Learning: Anwendung einfacher ML-Techniken auf den Challenge-Datensatz und erste Modelle entwickelt.

## Unsere Modelle

Wir haben zwei Modelle trainiert und ihre Ergebnisse miteinander verglichen:
- Random Forest Classifier
- Gradient Boosting Classifier

## Random Forest

Der Random Forest gehört zur Familie der Bagging-Methoden („Bootstrap Aggregating“). Dabei werden viele Entscheidungsbäume auf zufällig gezogenen Teilmengen der Daten trainiert. Die Ergebnisse dieser Bäume werden anschließend kombiniert (z. B. durch Mehrheitsentscheidung), um eine robustere und stabilere Vorhersage zu erhalten. Ziel ist es, Varianz zu reduzieren und Overfitting zu vermeiden.

### Vorteile
- Robust gegenüber Overfitting
- Funktioniert gut bei verrauschten oder unausgeglichenen Daten
- Liefert Feature Importance
- Relativ einfach zu trainieren und zu verstehen

### Nachteile
- Kann bei großen Datensätzen langsam sein
- Etwas weniger präzise als Boosting-Modelle
- Schwerer zu interpretieren als ein einzelner Entscheidungsbaum


## Gradient Boosting

Der Gradient Boosting Classifier ist eine Boosting-Methode. Im Gegensatz zum Bagging werden hier die Bäume nacheinander trainiert. Jeder neue Baum versucht, die Fehler der vorherigen Bäume zu korrigieren. Das Modell wird schrittweise verbessert, wodurch eine Reduktion des Bias erreicht wird und die Genauigkeit steigt.

### Vorteile
- hohe Genauigkeit
- Gute Leistung bei komplexen, nichtlinearen Zusammenhängen
- Fein abstimmbar durch viele Hyperparameter

### Nachteile
- Empfindlich gegenüber Overfitting, wenn nicht reguliert
- Langsameres Training, da Bäume sequentiell gebaut werden
- Erfordert oft mehr Parameter-Tuning

## Ergebnis

Beide Modelle lieferten ähnliche Resultate – der Leistungsunterschied war statistisch insignifikant.