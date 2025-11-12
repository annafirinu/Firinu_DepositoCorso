#Liste

numeri = [1, 2, 3, 4, 5]
nomi = ["Alice","Bob","Charlie"]
misto = [1, "due", True, 4.5]

print(numeri[0])#Stampa il numero 1 che si trova in posizione 0
print(numeri[2])#Stampa il numero 3 che si trova in posizione 2

#modifica funzionale
numeri = [1, 2, 3, 4, 5]
numeri[2]=10
print(numeri)#stamperà 10 al posto di 3

#matodi applicabili alle liste
numeri=[3,1,4,2,5]
print(len(numeri))#output 5, stamperà la lunghezza della lista
numeri.append(6)#aggiungo il numero 6 alla fine della lista
print(numeri)
numeri.insert(2,10)#aggiungo l'elemento 10 in posizione 2
print(numeri)
numeri.remove(4)#rimuove l'elemento 4
print(numeri)
numeri.sort()#ordina gli elementi della lista 
print(numeri)

#Esercizio
nome_utente="admin"
password="ciao"
login=[nome_utente, password]

nome_utente2=input("Inserisci nome utente: ")
password2=input("Inserisci password: ")

if nome_utente2==nome_utente and password2==password:
    print("Benvenuto all'interno del portale!")
    print("Ora puoi modificare nome Utente e Password")
    login.remove("admin")
    login.remove("ciao")
    login.insert(0,input("Inserisci nuovo nome utente: "))
    login.insert(1,input("Inserisci nuova password: "))
    print("I tuoi nome utente e la password sono stati modificati: ", login)
    print("Scegli la domanda segreta:")
    print("1. Qual'è il tuo colore preferito?")
    print("2. Qual'è il tuo animale preferito?")

    scelta = input("Scegli un'opzione (1-2): ")

    if scelta == "1":
       colore=input("Qual'è il tuo colore preferito?")
       print("Il tuo colore preferito è il: ", colore)

    elif scelta == "2":
        animale=input("Qual'è il tuo animale preferito?")
        print("Il tuo animale preferito è il: ", animale)

    else:
        print("Scelta non valida.")
        
else:
    print("Nome utente e password errati!")