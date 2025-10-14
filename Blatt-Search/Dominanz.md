h1(n) dominiert h2(n) wenn für alle n: h1(n) >= h2(n)
h1 muss immernoch zulässig sein: h(n) <= h*(n)

somit ist h1 genauer als h2 und A* findet den Weg mit geringerer Laufzeit

Beispiel: h1(n) = 0 (A* arbeitet genau wie Branch and Bound)

          h2(n) = h*(n) (die optimale heuristik: A* findet den optimalen Pfad sofort)