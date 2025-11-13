for i in range(5):
    print(i) #stop
    
for i in range(2, 8):
    print(i) #start e stop
    
for i in range(1, 10, 2):
    print(i) #step
    
#Esercizio1
while True:
    numero = int(input("Inserisci un numero per il conto alla rovescia: "))

    for i in range(numero, -1, -1):  #conto alla rovescia che parte da 'numero'e arriva a 0
        print(i)

    scelta = input("Vuoi ripetere? (si/no): ").lower()
    if scelta != "si":
        print("Fine del programma.")
        break

#Esercizio2
numeri_primi = []

while len(numeri_primi) < 5:
    numero = int(input("Inserisci un numero: "))

    # Controllo se il numero inserito dall'utente è primo
    if numero > 1:
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                print("Il numero non è primo.")
                break
        else:
            print("Il numero è primo!")
            numeri_primi.append(numero)
    else:
        print("Il numero non è primo.")

print("Hai inserito 5 numeri primi: ", numeri_primi)


#Esercizio completo

#Punto 1: Utilizzo di if
numero = int(input("Inserisci un numero: "))#Chiedo all'utente di inserire un numero

if numero % 2 == 0:
    print("Pari")
else:
    print("Dispari")
    
#Punto 2: Utilizzo di while e range

ripeti = "si"

while ripeti == "si":
    numero = int(input("Inserisci un numero intero positivo: "))

    if numero >= 0:
        i = numero
        while i >= 0:
            print(i)
            i = i - 1   # decrementa di 1 a ogni ciclo
    else:
        print("Devi inserire un numero positivo!")

    ripeti = input("Vuoi ripetere l'operazione con un altro numero? (si/no): ")

print("Fine programma.")

#Punto 3: Utilizzo di for
numeri = []

while True:
    n = int(input("Inserisci un numero intero (0 per terminare): "))
    if n == 0:
        break  # con break esco dal ciclo quando l'utente decide che non vuole più inserire numeri
    numeri.append(n)

# Stampo il quadrato di ciascun numero
for numero in numeri:
    print("Il quadrato d: ", numero," é " , numero**2)
    
#Punto 4: Utilizzo di if, while e for insieme

numeri = []

while True: #Chiedo i numeri all'utente
    n = int(input("Inserisci un numero intero (0 per terminare): "))
    if n == 0:
        break#esco dal ciclo se l'utente non vuole inserire più numeri
    numeri.append(n)


if len(numeri) == 0:#Controllo se la lista è vuota, se non lo è con il for trovo il valore massimo
    print("Lista Vuota")
else:

    massimo = numeri[0]  # parto dal primo elemento e li confronto uno a uno
    for numero in numeri:
        if numero > massimo:
            massimo = numero

    #COnto quanti elementi ci sono nella lista
    count = 0
    i = 0
    while i < len(numeri):
        count += 1
        i += 1

    #Stampo i risultati
    print("Numero massimo: ", massimo)
    print("Numero di elementi nella lista: " , count)