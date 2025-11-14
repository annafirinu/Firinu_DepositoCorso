#Esercizio 1
import random

def indovina_numero(numero_segreto=None):#se non viene passato un numero la funzione lo genererà da sola
    if numero_segreto is None:
        numero_segreto = random.randint(1, 100)
        print("Benvenuto nel gioco")

    tentativo = input("Inserisci un numero tra 1 e 100, oppure scrivi esci per terminare: ")
    
    if tentativo.lower() == 'esci':
        print("Grazie. Il numero era: ", numero_segreto)
        if input("Vuoi rigiocare? (si o no) ").lower() == 'si':
            return indovina_numero()
        else:
            print("Grazie per aver giocato!")
        return  #se l'utente vuole uscire comunico il numero segreto

    if not tentativo.isdigit():#con isdigit verifico che sia stato inserito effettivamente un numero
        print("Inserisci un numero valido.")
        return indovina_numero(numero_segreto)

    tentativo = int(tentativo) #converto il numero in intero e se non è un numero compreso tra 1 e 100 lo comunico
    if not 1 <= tentativo <= 100:
        print("Il numero deve essere tra 1 e 100.")
        return indovina_numero(numero_segreto)

    if tentativo < numero_segreto:
        print("Troppo basso!")
        return indovina_numero(numero_segreto)
    elif tentativo > numero_segreto:
        print("Troppo alto!")
        return indovina_numero(numero_segreto)
    else:
        print("Complimenti! Hai indovinato il numero!")
        if input("Vuoi rigiocare (si o no)").lower() == 'si':
            return indovina_numero()
        else:
           print("Grazie per aver giocato!")
    return 



indovina_numero()