import numpy as np

#1. Crea un array di 50 numeri equidistanti tra 0 e 10
def genera_linspace():
    return np.linspace(0, 10, 50)

#2. Crea un array di 50 numeri casuali compresi tra 0 e 1
def genera_random():
    return np.random.random(50)

#3. Somma i 2 array elemento per elemento per ottenere un nuovo array
def somma_array(a, b):
    return a + b

#4. Calcola la somma totale degli elementi del nuovo array
def somma_totale(arr):
    return np.sum(arr)

#5. Calcola la somma totale degli elementi del nuovo array che sono maggiori di 5
def somma_maggiori_di_5(arr):
    return np.sum(arr[arr > 5])

#6. Stampa i risultati di tutte le operazioni precedenti
def prepara_output(a, b, nuovo, totale, somma_5):
    return (
        "\nRISULTATI\n"
        f"Array numeri equidistanti:\n{a}\n\n"
        f"Array numeri casuali:\n{b}\n\n"
        f"Somma dei due array:\n{nuovo}\n\n"
        f"Somma totale: {totale}\n"
        f"Somma valori maggiori di 5: {somma_5}\n"
        "\n"
    )
    
#7.Salva i dati su un file txt a ogni giro
def salva_su_file(contenuto, sovrascrivi=False):
    percorso_file = "esercizio.txt"
    mode = "w" if sovrascrivi else "a"  # w=sovrascrive, a=append

    separatore = "="*50

    blocco = (
        f"\n{separatore}\n"
        f"{contenuto}"
        f"{separatore}\n"
    )

    with open(percorso_file, mode, encoding="utf-8") as f:
        f.write(blocco)

#Aggiungo una funzione per leggere il file così posso verificare che tutto venga scritto o sovrascritto correttamente       
def leggi_file(percorso="esercizio.txt"):
    with open(percorso, "r", encoding="utf-8") as f:
        contenuto = f.read()
        print("\nCONTENUTO DEL FILE:\n")
        print(contenuto)

