from unitamilitare import UnitaMilitare

class Fanteria(UnitaMilitare): #Definisco la classe Fanteria
    def __init__(self, nome, numero_soldati, numero_fanteria, numero_difesetemporanee):
        super().__init__(nome, numero_soldati)
        self.numero_fanteria = numero_fanteria
        self.numero_difesetemporanee = numero_difesetemporanee
        
    def costruisci_trincea(self):
        super().muovi()
        print(f"La fanteria numero {self.numero_fanteria} sta costruendo {self.numero_difesetemporanee} difese temporanee")
        
class Artiglieria(UnitaMilitare): #Definisco la classe Artiglieria
    def __init__(self, nome, numero_soldati, pezzi_artiglieria):
        super().__init__(nome, numero_soldati)
        self.pezzi_artiglieria = pezzi_artiglieria
             
    def calibra_artiglieria(self):
        super().muovi()
        print(f"La fanteria {self.nome} ha calibrato {self.pezzi_artiglieria} pezzi d'artiglieria")
        
class Cavalleria(UnitaMilitare): #Definisco la classe Cavalleria
    def __init__(self, nome, numero_soldati, area):
        super().__init__(nome, numero_soldati)
        self.area = area
             
    def esplora_terreno(self):
        super().muovi()
        print(f"La fanteria {self.nome} ha esplorato l'area '{self.area}' per avere informazioni sul nemico")
        
class Supportologistico(UnitaMilitare): #Definisco la classe Supportologistico
    def __init__(self, nome, numero_soldati, numero_unita):
        super().__init__(nome, numero_soldati)
        self.numero_unita = numero_unita
             
    def rifornisci_unita(self):
        super().muovi()
        print(f"La fanteria {self.nome} ha rifornito l'unita numero {self.numero_unita}")
        
class Ricognizione(UnitaMilitare): #Definisco la classe Ricognizione
    def __init__(self, nome, numero_soldati, soldato):
        super().__init__(nome, numero_soldati)
        self.soldato = soldato
             
    def conduci_ricognizione(self):
        super().muovi()
        print(f"Il soldato {self.soldato} ha eseguito la ricognizione")
        

class ControlloMilitare(Fanteria, Artiglieria, Cavalleria, Supportologistico, Ricognizione): #Creo la classe ControlloMilitare
    
    def __init__(self):
        self.unita_registrate = {} #Dizionario: {nome_unità: istanza_unità}

    def registra_unita(self, unita: UnitaMilitare):
        if isinstance(unita, UnitaMilitare):
            self.unita_registrate[unita.nome] = unita
            print(f"Unità '{unita.nome}' ({unita.tipo_unita}) registrata")
        else:
            print("Errore: L'oggetto non è valido")

    def mostra_unita(self):
        print("\nUnità Militari Registrate")
        if not self.unita_registrate:
            print("Nessuna unità registrata")
            return

        for nome, unita in self.unita_registrate.items():
            print(f"{unita}")
        print("__________")

    def dettagli_unita(self, nome: str):
        print(f"\nDettagli Unità: {nome}")
        unita = self.unita_registrate.get(nome)
        
        if unita:
            print(str(unita))
            print("\nAzioni base:")
            unita.muovi()
            unita.attacca()
            unita.ritira()
            
        else:
            print(f"Unità '{nome}' non trovata nel registro")
        print("________________________")