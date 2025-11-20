#Esempi polimorfismo
#Overloading
class Stampa:
 def mostra(self, a=None, b=None):
   if a is not None and b is not None:
     print(a + b)
   elif a is not None:
     print(a)
   else:
     print("Niente da mostrare")
     
s = Stampa()
s.mostra()
s.mostra(10)
s.mostra(5, 7)

#Polimorfismo passivo: duck typing
class Cane:
 def parla(self):
   return "Bau!"

class Gatto:
 def parla(self):
   return "Miao!"

def fai_parlare(animale):
 # Non importa di che tipo sia l'animale,
 print(animale.parla())

cane = Cane()
gatto = Gatto()

fai_parlare(cane) # Output: Bau!
fai_parlare(gatto) # Output: Miao!

class Cerchio:
 def disegna(self):
   print("Disegno un cerchio")

class Rettangolo:
 def disegna(self):
   print("Disegno un rettangolo")

def disegna_figura(figura):
 # Anche qui, basta che 'figura' abbia il metodo 'disegna'
 figura.disegna()

figure = [Cerchio(), Rettangolo()] # figure[0]=Cerchio() / figure[1]=Rettagolo()

# Iteriamo e disegniamo ogni figura
for figura in figure:
 disegna_figura(figura)
 
#len()
# Lista
print(len([1, 2, 3])) # Output: 3

# Stringa
print(len("Ciao")) # Output: 4

# Dizionario
print(len({"a": 1, "b": 2})) # Output: 2
