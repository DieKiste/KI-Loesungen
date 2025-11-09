## 1


### Zoo
=== Summary ===

Correctly Classified Instances         100               99.0099 %
Incorrectly Classified Instances         1                0.9901 %
Kappa statistic                          0.987 
Mean absolute error                      0.0047
Root mean squared error                  0.0486
Relative absolute error                  2.1552 %
Root relative squared error             14.7377 %
Total Number of Instances              101


Confusion Matrix
Fehler im detail
ein fehler ist bei den anmphibien aufgeteten

### Restaurant
=== Summary ===

Correctly Classified Instances           9               75      %
Incorrectly Classified Instances         3               25      %
Kappa statistic                          0.6842
Mean absolute error                      0.0833
Root mean squared error                  0.2041
Relative absolute error                 35.3723 %
Root relative squared error             59.9123 %
Total Number of Instances               12

Confusion Matrix

Ich verstehe die Confusion Matrix nicht
Wieso werden Klassifikationen doppelt aufgeführt?

=== Confusion Matrix ===

 a b c d e f g   <-- classified as
 4 0 0 0 0 0 0 | a =    Yes
 0 0 1 0 0 0 0 | b =   No
 0 0 2 0 0 0 0 | c =   Yes
 0 0 0 2 0 0 0 | d =     No 
 0 0 0 0 1 0 0 | e =    No
 0 0 1 0 0 0 0 | f =   No 
 0 0 0 0 1 0 0 | g =    No 

 ## 2
 NUMERIC - reelle oder ganze Zahl
 NOMINAL - ein Element aus einer Liste an elementen (bisschen wie enum)
 STRING - text

 ## 3

Das erneute Trainieren in J48 hat keinen unterschied gemacht.

### Restaurant mit ID3
=== Summary ===

Correctly Classified Instances          12              100      %
Incorrectly Classified Instances         0                0      %
Kappa statistic                          1     
Mean absolute error                      0     
Root mean squared error                  0     
Relative absolute error                  0      %
Root relative squared error              0      %
Total Number of Instances               12     

ID3 hat alles richtig klassifiziert