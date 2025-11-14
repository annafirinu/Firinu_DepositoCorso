input_lista = []  # Creo una lista per salvare tutti gli input dell'utente

while True:  # Ripete tutto finché l'utente non scrive "stop"
    
    # Chiedo all'utente di inserire un numero oppure stop se vuole terminare il programma
    scelta = input("Inserisci un numero intero positivo, oppure scrivi stop per terminare: ")

    if scelta.lower() == "stop":
        print("Programma terminato.")
        break

    # Controllo che l'utente inserisca effettivamente un numero
    if not scelta.isdigit():
        print("Inserisci un numero valido!")
        continue  # Torno all'inizio del ciclo per chiedere un numero valido

    # Converto in intero
    n = int(scelta)

    # Controllo che l'utente inserisca effettivamente un numero positivo
    if n <= 0:
        print("Il numero inserito non è positivo!!!")  # Se il numero non è positivo genero un messaggio che lo comunichi all'utente
        continue  # Torno all'inizio del ciclo per chiedere un numero valido

    # Salvo l'input nella lista
    input_lista.append(n)

    # Utilizzo un ciclo for con range per calcolare e stampare la somma dei numeri pari da 1 a n
    somma_numeri_pari = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            somma_numeri_pari += i

    print("La somma dei numeri pari da 1 a", n, "è", somma_numeri_pari)

    # Stampo attraverso un ciclo for tutti i numeri dispari da 1 a n 
    print("Numeri dispari da 1 a", n, ":")
    for i in range(1, n + 1, 2):  # Parto da uno a step di 2 così vado a prendere direttamente solo i dispari
        print(i, end=" ")  # Uso end per non andare a capo dopo ogni stampa
    print()  # Vado a capo dopo aver stampato tutti i dispari

    # Utilizzo if per determinare se n è un numero primo
    if n == 1:
        primo = False  # se n è uguale a 1 non è sicuramente un numero primo
    else:
        primo = True
        for i in range(2, int(n ** 0.5) + 1):  # Controllo tutti i divisori sino alla sua radice quadrata
            if n % i == 0:
                primo = False  # Se n è divisibile per i non è primo
                break  # interrompo il ciclo perché basta un divisore a dire che non è primo

    if primo:
        print(n, "è un numero primo")
    else:
        print(n, "non è un numero primo")

#stampo la lista completa di tutti i numeri inseriti dall'utente
print("Lista completa degli input inseriti:", input_lista)
