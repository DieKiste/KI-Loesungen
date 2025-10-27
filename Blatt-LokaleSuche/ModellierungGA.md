## 8-Queens-Problem


### Individuum

[(0,0), (1,2), (6,7), (-1,-1), (-1,-1), (5,5), (-1,-1), (1,7)]

- Positionen der Damen

### Crossover

 Für jeden Index des Kindes wird die Koordinate aus eienm Zufälligen Elternteil am selben Index übernommen

### Mutation

Bei einer zufälligen Koordinate wird entweder der x oder der y Wert um entweder -1 oder 1 geändert falls das nicht die Grenzen überschreitet

### Fitnessfunktion

Die Damen werden nacheinander auf dem Brett platziert, für jede die auf ein inkorrektes Feld platziert wird 1 punkt abgezogen.

n: Summe der menge an Damen jeder Dame die diese Dame blockieren.

Fitness = 56 - n

Jede der 8 Damen kann von maximal 7 anderen Damen blockiert werden, somit kann n maximal einen Wert von 56 erreichen

### Simulated Annealing

Um das Problem mit Simulated Annealing lösen zu können bräuchten wir eine Anzahl an Aktionen die der Algorithmus ausführen kann und eine Ergebisfunktion.

Als Aktionen kann man für jedes Feld eine Dame Platzieren oder Wegnehmen.

Als Ergebnisfunktion:

Dc: Anzahl korrekt platzierter Damen
Di: Anzahl inkorrekt platzierter Damen
B: Blockierte Felder


E = 25 * Dc - 20 * Di - B

Damen sind höher gewichtet damit der Algorithmus lieber Damen platziert als das ganze Feld freizulassen
Inkorrekt platzierte Damen sind nicht ganz so hoch gewichtet damit der Algorithmus wahrscheinlicher eine Dame hinstellt und eine andere wieder wegnimmt.

## Färbeproblem

[0,1,2,1,3,2,1]

Jeder Index beschreibt ein anderes Feld auf der Karte. Gleiche Zahlen stehen für jeweils gleiche Farbe

### Crossover

Für jeden Index wird eine Farbe von einem Elternteil aus dem jeweiligen Index übernommen

### Mutation

Ein Zufälliger Farbwert bekommt einen neuen zufälligen Wert (limits dürfen nicht überschritten werden)

### Fitnessfunktion

a: Anzahl angrenzender Felder mit der selben Farbe

Fitness = -a

### Simulated Annealing

Um das Problem mit Simulated Annealing lösen zu können bräuchten wir eine Anzahl an Aktionen die der Algorithmus ausführen kann und eine Ergebisfunktion.

Als Aktion kann ein Feld in eine andere Farbe gefärbt werden. d.h: für jedes Feld x jede Farbe gibt es eine Aktion

Als Ergebnisfunktion kann die Anzahl an überschneidungen genommen werden, welche minimiert werden muss