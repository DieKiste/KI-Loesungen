## Where is Waldo

Ziel war es den Kürzesten Pfad zu finden um alle 68 Punkte zu verbinden.

Ein individuum hatte eine Reihenfolge der 68 Punkte.
Die Fitnessfunktion war die Länge der Linie wenn man die Punkte in der Reihenfolge verbindet

## Evolution Simulator

Ziel ist es einen Simulierten Organismus zu finden der in einer Zeitspanne am weitesten laufen kann

Das Individuum ist der Aufbau der Organismen

Die Fitness ist die Distanz die der Organismus in der gegebenen Zeitspanne zurücklegt

## american fuzzy lop

Ziel: User Input generieren der funktion in einem Programm auslöst um bugs zu finden

Das Individuum ist der generierte Input.

Laut Docs funktioniert der Algorithmus so:
1) Load user-supplied initial test cases into the queue,

  2) Take next input file from the queue,

  3) Attempt to trim the test case to the smallest size that doesn't alter
     the measured behavior of the program,

  4) Repeatedly mutate the file using a balanced and well-researched variety
     of traditional fuzzing strategies,

  5) If any of the generated mutations resulted in a new state transition
     recorded by the instrumentation, add mutated output as a new entry in the
     queue.

  6) Go to 2.