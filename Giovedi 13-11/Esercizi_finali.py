#Esercizio 1
somma = 0 #Dichiaro la variabile somma uguale a zero 

while True:
    numero = int(input("Inserisci un numero intero oppure 0 per terminare): "))
    if numero == 0:
        break  #Se l'utente inserisce 0 il ciclo si interrompe
    somma += numero #Aggiungo a ogni ciclo il numero inserito dall'utente alla variabile somma

print("La somma dei numeri inseriti è:", somma)

#Esercizio 2
parola = input("Inserisci una parola: ")

risultato= ""

for lettera in parola:
    risultato += lettera + " " #Il ciclo for legge ogni singolo carattere della stringa in automatico
print(risultato)
  
# Esercizio 3
nmax = int(input("Inserisci il numero massimo: "))
step = int(input("Inserisci lo step: "))

risultato = []  #Creo la lista vuota

for i in range(0, nmax + 1, step):
    risultato.append(i)  #Aggiungo il numero intero come elemento della lista

print(risultato)  #Stampo la lista finale
