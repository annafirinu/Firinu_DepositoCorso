#Esercizi finali

#Esercizio 1
eta = int(input("Quanti anni hai? ")) #Chiedo all'utente la sua età

#utilizzo if per verificare che l'utente sia maggiorenne
if eta < 18:
    print("Mi dispiace, non puoi vedere questo film.")
else:
    print("Puoi vedere questo film.")
    
#Esercizio 2
numeri = [] #Creo una lista per i numeri che verranno inseriti

#Chiedo all'utente di inserire i due numeri
numeri.append(int(input("Inserisci il primo numero: ")))
numeri.append(int(input("Inserisci il secondo numero: ")))

# Chiedo all'utrnte di scegliere l'operazione
operazione = input("Scegli l'operazione (+, -, *, /): ")

# Utilizzo un if else in modo che venga eseguito solo il caso specifico
if operazione == "+":
    risultato = numeri[0] + numeri[1]
    print("Risultato:", risultato)
elif operazione == "-":
    risultato = numeri[0] - numeri[1]
    print("Risultato:", risultato)
elif operazione == "*":
    risultato = numeri[0] * numeri[1]
    print("Risultato:", risultato)
elif operazione == "/":
    if numeri[1] == 0:
        print("Errore: Divisione per zero.")
    else:
        risultato = numeri[0] / numeri[1]
        print("Risultato:", risultato)
else:
    print("Operazione non valida.") #Verrà eseguito l'else se viene indicata un operazione non presente nelle precedenti condizioni
    
#Esercizio Extra
numeri = [] #Creo una lista per i numeri che verranno inseriti

# Chiedo all'utente di inserire quattro numeri
numeri.append(int(input("Inserisci il primo numero: ")))
numeri.append(int(input("Inserisci il secondo numero: ")))
numeri.append(int(input("Inserisci il terzo numero: ")))
numeri.append(int(input("Inserisci il quarto numero: ")))

# Chiedo all'utente di scegliere l'operazione
operazione = input("Scegli l'operazione (+, -, *): ")

# Utilizzo un if else in modo che venga eseguito solo il caso specifico
if operazione == "+":
    risultato = numeri[0] + numeri[1] + numeri[2] + numeri[3]
    print("Risultato:", risultato)
elif operazione == "-":
    risultato = numeri[0] - numeri[1] - numeri[2] - numeri[3]
    print("Risultato:", risultato)
elif operazione == "*":
    risultato = numeri[0] * numeri[1] * numeri[2] * numeri[3]
    print("Risultato:", risultato)
else:
    print("Operazione non valida.")