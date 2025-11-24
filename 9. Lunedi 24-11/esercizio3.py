import numpy as np

# 1. Crea una matrice dimensione 6x6 contenente numeri interi casuali tra 1 e 100
matrice = np.random.randint(1, 101, (6, 6)) #Valore minimo incluso, valore massimo escluso, dimensione della matrice(righe x colonne)
print("Mateice di partenza:", matrice)

# 2. Estrai la sotto-matrice centrale 4x4
sottomatrice = matrice[1:5, 1:5]   # elimino riga e colonna 0e5
print("Sottomatrice:", sottomatrice)

# 3. Inverti le righe della sotto-matrice
invertita = sottomatrice[::-1, :] #(righe,colonne) per le colonne le prenderà dall'inizio alla fine, per le righe essendo lo step -1 la fine sarà l'inizio e l'inizio la fine
print("Matrice invertita:", invertita)

# 4. Estrai la diagonale principale della matrice invertita
diagonale = np.diag(invertita) #Lo fa in automatico la funzione np.diag
print("Diagonale della matrice invertita:", diagonale)

# 5. Sostituisci gli elementi multipli di 3 con -1
invertita_modificata = invertita.copy() #Creo una copia della matrice invertita
invertita_modificata[invertita_modificata % 3 == 0] = -1 #Trasformo in -1 tutti gli elementi che non danno resto quqndo vengono divisi per 3
print("Matrice invertita modificata:", invertita_modificata)
