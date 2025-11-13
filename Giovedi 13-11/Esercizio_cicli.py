#ciclo matematico

conteggio=0

while conteggio <5:
    print(conteggio)
    conteggio += 1   #Continuo ad eseguire finchè è true, stamperà 0,1,2,3,4
    
#ciclo booleano
controllor=True

while controllor:
    print(controllor)
    scelta=input("vuoi continuare?")
    if scelta.lower() == "no":
        controllor=False
    else:
        print("stai continuando")
        
#Esempio for
numeri=[1,2,3,4,5]

for numero in numeri:
    print(numero)