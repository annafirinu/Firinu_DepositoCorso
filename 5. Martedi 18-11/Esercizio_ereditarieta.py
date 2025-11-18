class Animale: #Creo la classe base Animale
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def fai_suono(self):
        print(f"{self.nome} fa un suono generico")

class Leone(Animale): #Creo la classe derivata leone
    def __init__(self, nome, eta, caccia):
        super().__init__(nome, eta)
        self.caccia = caccia #Attributo specifico del leone

    def fai_suono(self):
        print(f"{self.nome} ruggisce")

    def caccia(self):
        print(f"{self.nome} sta cacciando in un raggio di {self.caccia} metri.")

class Giraffa(Animale):#Creo la classe Giraffa
    def __init__(self, nome, eta, altezza_collo):
        super().__init__(nome, eta)
        self.altezza_collo = altezza_collo  #Attributo specifico della giraffa

    def fai_suono(self):
        print(f"{self.nome} saluta")

    def mangia_foglie(self):
        print(f"{self.nome} ha un collo di {self.altezza_collo} metri.")

class Pinguino(Animale): #Creo la classe Pinguino
    def __init__(self, nome, eta, nuota_velocita):
        super().__init__(nome, eta)
        self.nuota_velocita = nuota_velocita  #Attributo specifico del pinguino

    def fai_suono(self):
        print(f"{self.nome} gracchia")

    def nuota(self):
        print(f"{self.nome} nuota a {self.nuota_velocita} km/h")

#Provo a utilizzare le classi
leone = Leone("Simba", 5, 50)
giraffa = Giraffa("Melman", 7, 5)
pinguino = Pinguino("Pingu", 3, 10)


leone.fai_suono()
leone.caccia()
giraffa.fai_suono()
giraffa.mangia_foglie()
pinguino.fai_suono()
pinguino.nuota()
