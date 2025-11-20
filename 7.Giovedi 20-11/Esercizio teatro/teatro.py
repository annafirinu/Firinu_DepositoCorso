class Posto:#Creo la classe base Posto
    def __init__(self, numero: int, fila: str):#Creo il costruttore e inserisco i parametri
        self._numero: int = numero#Creo gli attributi
        self._fila: str = fila
        self._occupato: bool = False

    def prenota(self): #Metodo prenota: Permetterà di prenotare un posto se non è già occupato
        if not self._occupato:
            self._occupato = True
            print(f"Posto fila {self._fila}, numero {self._numero} prenotato con successo")
        else:
            print(f"Il posto fila {self._fila}, numero {self._numero} è già occupato")

    def libera(self): #Metodo libera: Permetterà di liberare un posto se è gia occupato
        if self._occupato:
            self._occupato = False
            print(f"Posto fila {self._fila}, numero {self._numero} liberato")
        else:
            print(f"Il posto fila {self._fila}, numero {self._numero} non era prenotato")

    def get_numero(self) -> int:   #Metodi get che permettono di leggere i dati dall'esterno
        return self._numero

    def get_fila(self) -> str:
        return self._fila

    def get_occupato(self) -> bool:
        return self._occupato

    def get_tipo(self) -> str:
        return "Standard" 

class PostoVIP(Posto):#Creo la classe derivata PostoVIP
    def __init__(self, numero: int, fila: str, servizi_extra: list[str] = None):#Aggiungo l'attributo servizi extra
        super().__init__(numero, fila)#Chiamo il costruttore della classe base
        if servizi_extra is None:#Creo il nuovo attributo
            servizi_extra = []
        self.servizi_extra: list[str] = servizi_extra

    def prenota(self): #Metodo prenota: Mi permetterà di prenottare un posto se non è occupato, andando a elencare quali sono i servizi extra dei posti VIP
        if not self._occupato:
            super().prenota()
            if self.servizi_extra:
                print(f"Servizi extra attivati: {', '.join(self.servizi_extra)}")
        else:
            print(f"Il posto VIPfila {self._fila}, numero {self._numero} è già occupato")

    def get_tipo(self) -> str:
        return "VIP"

class PostoStandard(Posto):#Creo la classe derivata PostoStandard
    def __init__(self, numero: int, fila: str, costo: float):#Aggiungo l'attributo costo
        super().__init__(numero, fila)#Chiamo il costruttore della classe base
        self.costo: float = costo#Creo il nuovo attributo

    def prenota(self):#Metodo prenota: Mi permetterà di prenottare un posto se non è occupato, e mi comunicherà il costo del posto
        if not self._occupato:
            super().prenota()
            print(f"Il costo della prenotazione è: €{self.costo}")
        else:
            print(f"Il posto standard fila {self._fila}, numero {self._numero} è già occupato")

    def get_tipo(self) -> str:
        return "Standard"


class Teatro:#Creo la classe Teatro
    def __init__(self):
        self._posti: list[Posto] = []

    def aggiungi_posto(self, posto: Posto):
        self._posti.append(posto)
        print(f"Posto fila {posto.get_fila()}, numero {posto.get_numero()} aggiunto al teatro")

    def prenota_posto(self, numero: int, fila: str):
        for posto in self._posti:
            if posto.get_numero() == numero and posto.get_fila() == fila:
                posto.prenota() 
                return
        print(f"Nessun posto trovato con numero {numero} e fila {fila}")

    def libera_posto(self, numero: int, fila: str):
        for posto in self._posti:
            if posto.get_numero() == numero and posto.get_fila() == fila:
                posto.libera()
                return
        print(f"Nessun posto trovato con numero {numero} e fila {fila}")

    def stampa_posti_occupati(self):
        print("Posti occupati:")
        for posto in self._posti:
            if posto.get_occupato():
                tipo = posto.get_tipo()
                servizi = ""
                if isinstance(posto, PostoVIP):
                    servizi = f" - Servizi: {', '.join(posto.servizi_extra)}"
                print(f"FILA {posto.get_fila()}, POSTO {posto.get_numero()} ({tipo}){servizi}")
