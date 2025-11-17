#Esercizio for

stringa = input("Inserisci una stringa: ")
intero = int(input("Inserisci un numero intero: "))
booleano = input("Inserisci True o False: ")

if booleano.lower() == "true": #Converto la stringa in booleano
    booleano = True
else:
    booleano = False

lista_valori = [stringa, intero, booleano] #Creo la lista

dizionario = { #Creo il dizionario
    "tipididato": lista_valori
}

# Stampo il dizionario
for chiave, valore in dizionario.items():
    print("Chiave:", chiave)
    print("Valore:", valore)