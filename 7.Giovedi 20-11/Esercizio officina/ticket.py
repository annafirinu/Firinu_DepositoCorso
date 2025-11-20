from elettrodomestici import Elettrodomestico

# Classe TicketRiparazione
class TicketRiparazione:
    def __init__(self, id_ticket: int, elettrodomestico: Elettrodomestico):
        # ID univoco del ticket
        self.__id_ticket: int = id_ticket
        
        # Oggetto elettrodomestico associato al ticket
        # Può essere qualsiasi sottoclasse di Elettrodomestico
        self.__elettrodomestico: Elettrodomestico = elettrodomestico
        
        # Stato iniziale del ticket ("aperto", "in lavorazione", "chiuso")
        self.__stato: str = "aperto"
        
        # Lista di note aggiuntive sul ticket
        self.__note: list[str] = []

   
    # Getter per ID ticket
    def get_id_ticket(self) -> int:
        return self.__id_ticket

    
    # Getter per elettrodomestico
    def get_elettrodomestico(self) -> Elettrodomestico:
        return self.__elettrodomestico

    
    # Getter e setter per lo stato
    def get_stato(self) -> str:
        return self.__stato

    def set_stato(self, stato: str):
        # Controllo valori validi
        if stato not in ["aperto", "in lavorazione", "chiuso"]:
            raise ValueError("Stato non valido")
        self.__stato = stato

    
    # Gestione note
    def aggiungi_nota(self, testo: str):
        # Aggiunge una nota alla lista
        self.__note.append(testo)

    def get_note(self) -> list[str]:
        # Restituisce la lista completa di note
        return self.__note

    
    # Calcolo preventivo (metodo variadico)
    def calcola_preventivo(self, *voci_extra: float) -> float:
        """
        Calcola il preventivo totale per il ticket.

        Parametri:
        *voci_extra: valori opzionali aggiuntivi (riparazioni extra, pezzi di ricambio, ecc.)

        Funzionamento:
        1. Prende il costo base dall'elettrodomestico associato
           (polimorfismo: ogni sottoclasse può avere un costo base diverso)
        2. Somma tutte le voci extra passate
        3. Restituisce il totale finale
        """
        totale = self.__elettrodomestico.stima_costo_base()  # costo base polimorfico
        totale += sum(voci_extra)                             # somma voci extra
        return totale
