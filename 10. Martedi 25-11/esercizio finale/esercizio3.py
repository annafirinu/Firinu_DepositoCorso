import numpy as np

#1. Creare un array NumPy di forma (4, 4) contenente numeri casuali interi tra 10 e 50.
array = np.random.randint(10, 51, size=(4, 4))
print("Array:\n", array)

#2. Utilizzare fancy indexing per selezionare e stampare gli elementi agli indici (0,1), (1, 3), (2, 2) e (3, 0).
elementi_selezionati = array[[0, 1, 2, 3], [1, 3, 2, 0]]
print("Elementi selezionati:", elementi_selezionati)

#3. Utilizzare fancy indexing per selezionare e stampare tutte le righe disparidell'array (considerando la numerazione delle righe che parte da 0).
righe_dispari = array[1::2, :]
print("Righe dispari:\n", righe_dispari)

#4. Modificare gli elementi selezionati nel primo punto dell'esercizio aggiungendo 10 al loro valore.
array[[0, 1, 2, 3], [1, 3, 2, 0]] += 10
print("Array modificato:\n", array)

