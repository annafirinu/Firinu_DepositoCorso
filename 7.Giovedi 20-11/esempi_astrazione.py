#ESEMPI DI UTILIZZO ASTRAZIONE

from abc import ABC, abstractmethod

class Animale(ABC):
 @abstractmethod
 def muovi(self):
   pass

class Cane(Animale):
 def muovi(self):
   print("Corro")

class Pesce(Animale):
 def muovi(self):
   print("Nuoto")
   
# Creo un cane e un pesce
cane = Cane()
pesce = Pesce()

# Chiamo il metodo muovi()
cane.muovi()   # Output: Corro
pesce.muovi()  # Output: Nuoto


class Forma(ABC):
 @abstractmethod
 def area(self):
   pass
 @abstractmethod
 def perimetro(self):
   pass

class Rettangolo(Forma):
 def __init__(self, larghezza, altezza):
   self.larghezza = larghezza
   self.altezza = altezza
 def area(self):
   return self.larghezza * self.altezza
 def perimetro(self):
   return 2 * (self.larghezza + self.altezza)

# f = Forma() # TypeError: Can't instantiate abstract class Forma

r = Rettangolo(5, 10)
print(r.area()) # Output: 50
print(r.perimetro()) # Output: 30