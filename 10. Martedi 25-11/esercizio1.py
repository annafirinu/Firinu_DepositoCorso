import numpy as np

# 1. Crea un array di 12 numeri equidistanti tra 0 e 1 usando linsapce
array = np.linspace(0, 1, 12)
print("Array:\n", array)

# 2. Cambia la forma dell'array a una matrice 3x4
matrice = array.reshape(3, 4)
print("Matrice:\n", matrice)

# 3. Genera una matrice 3x4 di numeri casuali tra 0 e 1
matrice_casuale = np.random.rand(3, 4)
print("Matrice casuale:\n", matrice_casuale)

# 4. Calcola la somma degli elementi di entrambe le matrici
somma_matrice = np.sum(matrice)
somma_matrice_casuale = np.sum(matrice_casuale)

print("Somma elementi matrice:", somma_matrice)
print("Somma elementi matrice casuale:", somma_matrice_casuale)
