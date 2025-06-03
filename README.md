# Böser Fitness Instructor
> Das hier ist ein Repo für einen Text-to-Speach Python Fitness-Coach, der einen etwas ... speziellen Humor hat.
> Text-To-Speach / Text-zu-Sprache wird durch das `pyttsx3` module realisiert, ein Text zu Sprache Synthese-Tool.

## Idee
- Im Script werden die Übungen als Strings hinterlegt
- Diese Übungen werden auf Farben gemapped
- Zu Beginn des Trainings erfolgt eine Durchsage, die einem durchsagt, welche Farbe zu welcher Übung gehört
- Das Farbe-Übung Mapping ist nach dem Festlegen gesetzt, aber die Durchsage der Farbe ist zufällig generiert
- Dadurch muss man immer schnell im Kopf sein, um sich an eine Übung für einem bestimmte Farbe zu erinnern
- Das Randomisieren sorgt dafür, dass man nicht immer den gleichen Ablauf im Training UND nicht das gleiche Mapping ZWISCHEN verschiedenen Durchläufen hat
- Dadurch soll die situative Aufmerksamkeit gesteigert werden wie auch das gleichzeitige Bewegen und Denken
- Insgesamt soll es zu gesteigerter geistiger Flexibilität beitragen
- Der Bot ist sehr einfach und kann easy umgescripted werden für etwas "annehmbareren" Humor ;)
  
## Funktionen
- `main(...)`: Gesamtdurchlauf und übergeordnete Ansagen
- `trainierDuPudding(...)`: Führt das eigentlich Training aus und sagt die Farben durch
- `speak(...)`: Wrapper für die Engine-Durchsagen

## Ausführung
Entweder das Modul `pyttsx3` manuel installieren mit `pip install pyttsx3` und dann ausführen oder direkt ausführen mit `python3 fitness.py -r`


Viel Spaß, hehehe.
