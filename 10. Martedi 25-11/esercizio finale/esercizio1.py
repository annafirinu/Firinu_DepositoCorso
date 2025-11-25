import numpy as np

#1. Creare un array NumPy di 15 elementi contenente numeri casuali compresi tra 1 e100.
array = np.random.randint(1, 101, size=15)
print("Array:", array)

#2. Calcolare e stampare la somma di tutti gli elementi dell'array.
somma = np.sum(array)
print("Somma degli elementi:", somma)

#3. Calcolare e stampare la media di tutti gli elementi dell'array.
media = np.mean(array)
print("Media degli elementi:", media)