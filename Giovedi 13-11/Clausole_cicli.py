#break e continue

numeri=[1,2,3,4,5]

for numero in numeri:
    if numero == 2:
        continue
    print(numero) #Col continue bloccherà solo il giro del 2 e continuerà
    
for numero in numeri:
    if numero == 4:
        break
    print(numero) #Col break arrivato al 4 si ferma(gia il 4 non verrà stampato)

#Il pass è un place holder che serve a non avere gli errori. Non fa nulla, passa oltre
for i in range(5):
    if i == 3:
        pass
    print(i) #serve per non bloccare il codice se non si è ancora pronti a definire quel pezzo
    
#operatore splat *
numeri=[*range(1,11)]
print(numeri)#stamperà i numeri da 1 compreso a 11 non compreso
 
#Esercizio 1
ripeti = "si"

while ripeti == "si":
    scelta = input("Vuoi inserire un numero o una stringa?: ")

    if scelta == "numero":
        numero = int(input("Inserisci un numero: "))
        if numero % 2 == 0:
            print("Il numero è pari.")
        else:
            print("Il numero è dispari.")

    elif scelta == "stringa":
        stringa = input("Inserisci una stringa: ")
        if len(stringa) % 2 == 0:
            print("La stringa è pari.")
        else:
            print("La stringa è dispari.")
    else:
        print("Scelta non valida.")

    ripeti = input("Vuoi ripetere?: ")

print("Programma terminato.") 

#Esercizio 2
ripeti = "si"

while ripeti == "si":

    n1 = int(input("Inserisci il primo numero: "))
    n2 = int(input("Inserisci il secondo numero: "))

    #Faccio in modo che vengano presi in ordine crescente
    if n1 < n2:
        inizio = n1
        fine = n2
    else:
        inizio = n2
        fine = n1

    primi = []
    non_primi = []

    # Ciclo su tutti i numeri dell'intervallo
    for numero in range(inizio, fine + 1):
        if numero < 2:
            non_primi.append(numero)
        else:
            # Controllo se il numero è primo
            for divisore in range(2, numero):#Provo tutti i divisori possibili partendo da 2
                if numero % divisore == 0:
                    non_primi.append(numero)#Se non c'è resto non è un numero primo
                    break
            else:
                primi.append(numero)

    # Stampo i risultati
    print("Numeri primi:", primi)
    print("Numeri non primi:", non_primi)

    ripeti = input("Vuoi ripetere?: ")

print("Programma terminato.")
  