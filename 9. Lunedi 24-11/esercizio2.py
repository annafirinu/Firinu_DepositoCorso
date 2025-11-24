import numpy as np

# 1. Creare un array 1D di 20 numeri interi casuali tra 10 e 50
array = np.random.randint(10, 51, size=20)
print("Array di partenza:", array)

# 2. Estrarre i primi 10 elementi
primi_10_elementi = array[:10]
print("Primi 10 elementi:", primi_10_elementi)

# 3. Estrarre gli ultimi 5 elementi
ultimi_5_elementi = array[-5:]
print("Ultimi 5 elementi:", ultimi_5_elementi)

# 4. Estrarre gli elementi dall'indice 5 all'indice 15 (escluso)
elementi_dal_5_al_15 = array[5:15]
print("Elementi dall'indice 5 all'indice 15:", elementi_dal_5_al_15)

# 5. Estrarre ogni terzo elemento
ogni_terzo_elemento = array[::3] #Dall'inizio alla fine a passi di 3 
print("Ogni terzo elemento:", ogni_terzo_elemento)

# 6. Modificare gli elementi dall'indice 5 all'indice 10 (escluso) assegnando 99
array[5:10] = 99
print("Array modificato:", array)



