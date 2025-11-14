#Esercizio2
def sequenza_fibonacci(N):
   
    a, b = 0, 1 #Primi due numeri della sequenza di Fibonacci
    sequenza = []
    while a <= N:#Continuo a generare numeri finchè non arrivo ad N
        sequenza.append(a)#Aggiungo il numero alla lista
        a, b = b, a + b
    return sequenza#Restituisce la lista completa

def fibonacci():
    while True:
        n_input = input("Inserisci un numero N: ")
        if n_input.isdigit(): #Verifico che la stringa sia composta da soli numeri
            N = int(n_input) #Converto in intero
            break
        else:
            print("Inserisci un numero valido")

   
    sequenza = sequenza_fibonacci(N) #Chiamo la funzione passando N come parametro

    #Stampo
    print("Sequenza di Fibonacci fino a: ", N)
    print(sequenza)
    
    if input("Vuoi provare con un altro numero? (si o no): ").lower() == 'si':
        return fibonacci()
    else:
        print("Grazie. Alla prossima")

#Lancio il programma
fibonacci()

