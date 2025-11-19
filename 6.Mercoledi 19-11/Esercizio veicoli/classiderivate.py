from veicolo import Veicolo

class Auto(Veicolo):#Creo la classe auto
    def __init__(self, marca: str, modello: str, anno: int, numero_porte: int, accensione: bool = False):
        super().__init__(marca, modello, anno, accensione)#Chiamo il costruttore della classe base
        self.__numero_porte: int = numero_porte #Definisco l'attributo specifico di Auto

    def suona_clacson(self):
        print("Ho suonato il clacson!")
        
class Furgone(Veicolo):#Creo la classe furgone
    def __init__(self, marca: str, modello: str, anno: int, capacita_carico: int, accensione: bool = False):
        super().__init__(marca, modello, anno, accensione)#Chiamo il costruttore della classe base
        self.__capacita_carico: int = capacita_carico  #Definisco l'attributo specifico di Furgone
        self.__carico_attuale: int = 0  #carico iniziale uguale a 0
        
    # Metodo per caricare il furgone
    def carica(self, peso: int):
        self.__carico_attuale += peso
        print(f"Caricato {peso} kg. Carico attuale: {self.__carico_attuale} kg")

    # Metodo per scaricare il furgone
    def scarica(self, peso: int):
        if peso > self.__carico_attuale:  # Controllo per non scaricare troppo
            print("Non puoi scaricare più di quanto caricato!")
        else:
            self.__carico_attuale -= peso
            print(f"Scaricato {peso} kg. Carico attuale: {self.__carico_attuale} kg")
            
class Motocicletta(Veicolo):#Creo la classe motocicletta
    def __init__(self, marca: str, modello: str, anno: int, tipo: str, accensione: bool = False):
        super().__init__(marca, modello, anno, accensione)#Chiamo il costruttore della classe base
        self.__tipo: str = tipo  #Definisco l'attributo specifico di motocicletta

    def esegui_wheelie(self):
        if self.__tipo.lower() == "sportiva":  # Solo le moto sportive possono fare wheelie
            print(f"{self._Veicolo__marca} {self._Veicolo__modello} fa un wheelie")
        else:
            print(f"{self._Veicolo__marca} {self._Veicolo__modello} non può fare wheelie")
