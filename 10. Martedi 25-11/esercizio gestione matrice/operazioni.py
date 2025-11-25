import numpy as np

def salva_su_file(test):
    # Questa funzione serve a salvare una stringa all'interno di un file di testo
    # chiamato "risultati.txt". Ogni volta che viene chiamata, aggiunge una nuova
    # riga senza cancellare il contenuto precedente

    # 'with open(..., "a") as f:' apre il file in modalità "append"
    # se il file non esiste, viene creato automaticamente
    with open("risultati.txt", "a") as f:
        f.write(test + "\n")

#1.Creare una nuova matrice 2D di dimensioni specificate con numeri casuali.
def crea_matrice():
    # Chiedo all'utente il numero di righe della matrice
    righe = int(input("Inserisci numero di righe: "))
    # Chiedo all'utente il numero di colonne della matrice
    colonne = int(input("Inserisci numero di colonne: "))
    matrice = np.random.randint(0, 50, (righe, colonne))

    # Stampo la matrice
    print("\nMatrice:\n", matrice)
    
    # Salvo la matrice nel file risultati.txt
    salva_su_file(f"Matrice:\n{matrice}")

    return matrice

#2.Estrarre e stampare la sotto-matrice centrale.
def sotto_matrice_centrale(m):
    # Estraggo il numero di righe (r) e colonne (c) dalla matrice
    r, c = m.shape
    # Calcolo gli indici centrali per riga e colonna
    r_mid = r // 2
    c_mid = c // 2

    # Se sia il numero di righe sia il numero di colonne è dispari,
    # allora posso estrarre una sotto-matrice 3x3 centrata
    if r % 2 == 1 and c % 2 == 1:
        # Estraggo le righe da r_mid-1 a r_mid+1 e lo stesso per le colonne
        sotto = m[r_mid-1:r_mid+2, c_mid-1:c_mid+2]
    else:
        # In caso di dimensioni pari (o miste), estraggo una sotto-matrice 2x2
        sotto = m[r_mid-1:r_mid+1, c_mid-1:c_mid+1]

    # Stampo la sotto-matrice trovata
    print("\nSotto-matrice centrale:")
    print(sotto)

    # La salvo nel file risultati
    salva_su_file(f"Sotto-matrice centrale:\n{sotto}")

#3.Trasporre la matrice e stamparla.
def trasposta(m):
    # m è la matrice che viene passata dal main.py.
    # Contiene i valori su cui dobbiamo calcolare la trasposta.

    # .T è una proprietà degli array NumPy:
    # restituisce la trasposta della matrice,
    # cioè una nuova matrice ottenuta scambiando righe e colonne.
    t = m.T

    # Stampo la matrice trasposta
    print("\nMatrice trasposta:\n", t)

    # Salvo la matrice trasposta dentro il file di testo risultati.txt
    salva_su_file(f"Trasposta:\n{t}")

#4.Calcolare e stampare la somma di tutti gli elementi della matrice.
def somma_elementi(m):
    # La funzione riceve 'm', che è la matrice generata nel main.py.

    # np.sum(m) è una funzione di NumPy che:
    # - scorre tutti gli elementi della matrice
    # - li somma uno per uno
    # - restituisce il totale finale
    s = np.sum(m)

    # Stampo il risultato 
    print("\nSomma degli elementi:", s)

    # Salvo la somma all'interno del file risultati.txt
    salva_su_file(f"Somma: {s}")

#5.Moltiplicazione Element-wise con un'altra Matrice: L'utente può scegliere di creare una seconda matrice delle stesse dimensioni 
# della prima e moltiplicarle elemento per elemento e stampare il risultato.
def moltiplicazione_elementwise(m):
    print("\nCreazione seconda matrice:")

    # Creo una seconda matrice 'm2' con gli stessi valori di righe e colonne di 'm'
    m2 = np.random.randint(0, 50, m.shape)

    # Stampo la seconda matrice
    print("Seconda matrice:\n", m2)

    # Moltiplicazione elemento per elemento
    # In NumPy, l'operatore '*' tra due array della stessa forma moltiplica
    # ogni elemento corrispondente
    prodotto = m * m2

    # Stampo il risultato della moltiplicazione
    print("\nRisultato moltiplicazione element-wise:\n", prodotto)

    # Salvo il risultato nel file risultati.txt
    salva_su_file(f"Moltiplicazione element-wise:\n{prodotto}")


#6.Calcolo della Media degli Elementi della Matrice: Calcolare e stampare la media di tutti gli elementi della matrice.
def media_matrice(m):
    # np.mean(m) calcola la media aritmetica di tutti gli elementi
    # della matrice. Restituisce un singolo valore numerico.
    media = np.mean(m)

    # Stampo il risultato
    print("\nMedia degli elementi:", media)

    # Salvo il risultato nel file risultati.txt
    salva_su_file(f"Media: {media}")

    
#7. Determinante della Matrice: Calcolare e stampare il determinante della matrice(solo se la matrice è quadrata).
def determinante(m):
    # Controllo se la matrice è quadrata
    if m.shape[0] != m.shape[1]:
        print("Impossibile calcolare il determinante: la matrice non è quadrata")
        return 

    # np.linalg.det(m) calcola il determinante della matrice quadrata
    det = np.linalg.det(m)

    # Stampo il risultato a video
    print("\nDeterminante:", det)

    # Salvo il determinante nel file risultati.txt
    salva_su_file(f"Determinante: {det}")
