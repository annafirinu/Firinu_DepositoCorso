class Veicolo:#Creo la classe base Veicolo
    def __init__(self, marca: str, modello: str, anno: int, accensione: bool = False):#Costruttore con parametri e relativo tipo
        self.__marca: str = marca#Creo gli attributi
        self.__modello: str = modello
        self.__anno: int = anno
        self.__accensione: bool = accensione

    def accendi(self):#Creo il metodo accendi
        self.__accensione = True
        print(f"{self.__marca} {self.__modello} è accesa")

    def spegni(self):#Creo il metodo spegni
        self.__accensione = False
        print(f"{self.__marca} {self.__modello} è spenta")

    
