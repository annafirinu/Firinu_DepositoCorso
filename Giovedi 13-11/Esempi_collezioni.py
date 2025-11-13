#Esempi di TUPLE
#Le Tuple sono l'unico modo in Python per avere delle costanti
#Le variabili possono essere lette ma non modificate

#Definisco 3 diverse Tuple
punto= (3,4)
colore_rgb=(255, 128, 0)
informazioni_persona=("Alice", 25, "Femmina")

print(punto[0]) #Stampo il numero 3 nella posizione 0 della tupla
print(punto[1]) #Stampo il numero 4 nella posizione 1 della tupla

#Si possono creare tuple senza utilizzare le parentesi
punto= 3, 4 #Tuple packing
x, y = punto #Tuple unpacking
print(x,y) #Stamperà 3 e 4

#INSIEMI
#Liste che non accettano duplicati

set1 = set([1,2,3,4,5])#Si può dichiarare in questo modo come metodo e dentro una lista
set2= {4,5,6,7,8}#O direttamente inserendo gli elementi tra parentesi graffe
set3= {1,2,3,3,4,4,5}
print(set3)#Mi mostrerà che non stampa duplicati

#Con gli insiemi si possono fare diverse operazioni che non si possono fare con le liste
set1={1,2,3,4,5}
set2={4,5,6,7,8}
print(set1.union(set2))#Operazione d'unione: Tutti gli elementi di entrambi
print(set1.intersection(set2))#Operazione d'intersezione:Solo gli elementi comuni a ntrambi
print(set1.difference(set2))#Operazione di Differenza: Solo elementi presenti nell'insieme di partenza
print(set1.symmetric_difference(set2))#Operazione di Differenza simmetrica: Solo elementi presenti in uno dei due insiemi ma non in entrambi

print(set1.add(100))
print(set1.remove(1))
print(set1.discard(3))
print(len(set1))
set2 = set1.copy()
print(set2)        


