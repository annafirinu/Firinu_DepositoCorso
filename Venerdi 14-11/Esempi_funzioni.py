#definizione del comportamento di una funzione
def saluta(nome): #def definisce la funzione, saluta è il nome della funzione, nelle parentesi c'è il parametro
    print("Ciao, ", nome) #righe che deve eseguire
    print("Benvenuto nel nostro programma!")
    
def somma (a,b):
    risultato = a+b
    print("La somma è: ", risultato)
  
    
#Richiamo della funzione
saluta("Alice")
somma(5,3)

#Esempio
def quadrato(numero):
    return numero*numero

risultato=quadrato(4)
print(risultato)



