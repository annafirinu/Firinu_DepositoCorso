import numpy as np

# 1. Creare un array di numeri interi da 10 a 49
arr = np.arange(10, 50)  #(inizio, fine) -> include inizio, esclude fine arrivando quindi a 49
print("Array:", arr)

# 2. Verificare il tipo di dato iniziale
print("Tipo di dato:", arr.dtype)

# 3. Cambiare il tipo di dato in float64
arr = arr.astype(np.float64) 
print("Tipo di dato modificato:", arr.dtype)

# 4. Stampare la forma dell'array
print("Forma dell'array:", arr.shape)
