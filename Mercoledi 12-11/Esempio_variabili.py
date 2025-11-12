# tipo int
# sono i numeri interi positivi o negativi
x=10
y=-10
print(x,y)

#tipo float

x=1
y="Mirko"


#Esempio 1
s="Python"
print(s[0])#va a stampare la lettera della stringa in posizione 0 (Output:'P')
print(s[2])#va a stampare la lettera della stringa in posizione 2 (Output:'t')

#Esempio 2
saluto= "Ciao"
nome="Alice"
messaggio=saluto + " " + nome
print(messaggio) #Output: 'Ciao Alice'

#Stringhe: Metodi che si utilizzano con le stringhe
s= "Ciao, mondo"
print(len(s))#Ottengo la lunghezza della stringa
print(s.upper())#Converto tutta la stringa in maiuscolo
print(s.split(','))#Divido la stringa in una lista di sottostringhe
print(s.replace('mondo','universo'))#Sostituisco parti della stringa con un altra

#Carattere
carattere= 'A'

#Booleani
t=True
f=False
print(t,f) #Stampo i valori booleani

#Utilizzo degli operatori logici 
x=5
y=10
z=7
print(x<y and y>z) #True
print(x<y or z>y) #True
print(not x<y) #False

#Utilizzo degli operatori di confronto
print(x==y) #uguale a (False)
print(x != y) #diverso da (True)
print (x < y) #minore di (True)
print(x>y) #maggiore di (False)
print (x <= y) #minore o uguale a (True)
print(x>=y) #maggiore o uguale a (False)

