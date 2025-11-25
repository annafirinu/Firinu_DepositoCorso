import numpy as np

#1. Creare una matrice 5x5 contenente numeri interi sequenziali da 1 a 25.
matrice = np.arange(1, 26).reshape(5, 5)
print("Matrice 5x5:\n", matrice)

#2. Estrarre e stampare la seconda colonna della matrice.
seconda_colonna = matrice[:, 1]
print("Seconda colonna:", seconda_colonna)

#3. Estrarre e stampare la terza riga della matrice.
terza_riga = matrice[2, :]
print("Terza riga:", terza_riga)

#4. Calcolare e stampare la somma degli elementi della diagonale principale della matrice.
somma_diagonale = np.trace(matrice)
print("Somma della diagonale principale:", somma_diagonale)
