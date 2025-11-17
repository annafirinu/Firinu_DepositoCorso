class Automobile: # dichiaro la classe
  numero_di_ruote = 4 # attributo di classe
  def __init__(self, marca, modello): # metodo costruttore
     self.marca = marca # attributo di istanza
     self.modello = modello # attributo di istanza
  def stampa_info(self): # metodo di istanza
     print("L'automobile è una", self.marca, self.modello)
     
     
auto1 = Automobile("Fiat", "500") # crea un oggetto di Automobile
auto2 = Automobile("BMW", "X3") # crea un altro oggetto di Automobile
auto1.stampa_info() # stampa "L'automobile è una Fiat 500"
auto2.stampa_info() # stampa "L'automobile è una BMW X3"

class Persona:
  def __init__(self, nome, eta):
    self.nome = nome # Attributo per memorizzare il nome
    self.eta = eta # Attributo per memorizzare l'età
    
  def __str__(self):
    #Viene richiamato quando facciamo print (istanza_di_persona)
    return f"Persona(nome={self.nome}, eta={self.eta})"
    
# Creazione di un oggetto Persona
p = Persona("Pippo", 30)

print(p.nome) # Output: Pippo
print(p.eta) # Output: 30

class Persona:
  def __init__(self, nome, eta):
    self.nome = nome
  def saluta(self):
    print(f"Ciao, mi chiamo {self.nome}")
# Creazione di un oggetto Persona
p = Persona("Luca", 25)
p.saluta()
# Output: Ciao, mi chiamo Luca

#Esempio metodo statico
class Calcolatrice:
  @staticmethod
  def somma(a, b):
    return a + b
# Uso del metodo statico senza creare un'istanza
risultato = Calcolatrice.somma(5, 3)

print(risultato)
# Output: 8

#Esempio metodo decorato
class Contatore:
  numero_istanze = 0 # Attributo di classe
  
  def __init__(self):
    Contatore.numero_istanze += 1
  @classmethod
  def mostra_numero_istanze(cls):
    print(f"Sono state create {cls.numero_istanze} istanze.")
    
# Creazione di alcune istanze
c1 = Contatore()
c2 = Contatore()

Contatore.mostra_numero_istanze()
# Output: Sono state create 2 istanze.

#Esempio metodo d'istanza
class Automobile: # dichiaro la classe
  numero_di_ruote = 4. # attributo di classe
  def __init__(self, marca, modello): # metodo costruttore
      self.marca = marca # attributo di istanza
      self.modello = modello # attributo di istanza
  def stampa_info(self): # metodo di istanza
      print("L'automobile è una", self.marca, self.modello)

