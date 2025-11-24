import numpy as np

# 1. Crea array con i valori da 0 a 49 più 50 valori casuali tra 49 e 101
array = np.concatenate([ #concatenate unisce 2 array generandone uno solo
    np.arange(50), #arange genera i numeri sequenziali
    np.random.randint(49, 102, size=50) #random genera 50 numeri random compresi in questo caso tra 49 e 102
])

#Stampo array, dtype, shape
print("Array iniziale:", array)
print("dtype:", array.dtype)
print("shape:", array.shape)

# 2. Modifica il tipo di dato in float64
array = array.astype(np.float64) #astipe va a modificare il tipo

#Verifico e stampo di nuovo dtype e shape
print("dtype:", array.dtype)
print("shape:", array.shape)

# 3. Slicing
#Stampo i primi 10 elementi
stampo_primi_10 = array[:10]
print("Primi 10 elementi:", stampo_primi_10)
#Stampo gli ultimi 7 elementi
stampo_ultimi_7 = array[-7:]
print("Ultimi 7 elementi:", stampo_ultimi_7)
#Stampo gli elementi daal'indice 5 al 20 escluso
stampo_da_5_a_20 = array[5:20]
print("Elementi da 5 a 20:", stampo_da_5_a_20)
#Stampo ogni quarto elemento
stampo_ogni_quarto = array[::4]
print("Ogni 4° elemento:", stampo_ogni_quarto)

# 4. Modifica con slicing gli elementi da 10 a 15 con 999
array[10:15] = 999
print("Array con 999:", array)

# 5. Fancy indexing
#Seleziono elementi in posizioni specifiche
posizioni_specifiche = array[[0, 3, 7, 12, 25, 33, 48]]
print("\nPosizioni [0,3,7,12,25,33,48]:", posizioni_specifiche)
#Utilizzo una maschera booleana per andare a selezionare tutti gli elemeti pari
pari = array[array % 2 == 0]
print("Elementi pari:", pari)
#Seleziono tutti gli elementi maggiori della media
media = array.mean() #Calcolo la media
print("Media:", media)
maggiore_media = array[array > media]#Utilizzo una maschera booleana per selezionare gli elementi maggiori della media
print("Elementi maggiori della media:", maggiore_media)

