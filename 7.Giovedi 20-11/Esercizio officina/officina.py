from ticket import TicketRiparazione
from elettrodomestici import Lavatrice, Frigorifero, Forno

# Classe Officina
# Gestisce i ticket di riparazione e gli elettrodomestici
class Officina:
    def __init__(self, nome: str):
        # Nome dell'officina
        self.nome: str = nome
        
        # Lista dei ticket presenti nell'officina
        self.tickets: list[TicketRiparazione] = []

   
    # Aggiunge un ticket alla lista
    def aggiungi_ticket(self, ticket: TicketRiparazione):
        self.tickets.append(ticket)

    
    # Chiude un ticket tramite ID
    def chiudi_ticket(self, id_ticket: int):
        for ticket in self.tickets:
            if ticket.get_id_ticket() == id_ticket:
                ticket.set_stato("chiuso")
                return
        print("Ticket non trovato.")

   
    # Stampa tutti i ticket aperti
    def stampa_ticket_aperti(self):
        print(f"Ticket aperti in {self.nome}:")
        for ticket in self.tickets:
            if ticket.get_stato() != "chiuso":
                elettro = ticket.get_elettrodomestico()
                
                # Recupera il tipo reale dell'elettrodomestico usando type()
                tipo = type(elettro).__name__  
                
                print(f"ID: {ticket.get_id_ticket()}, Tipo: {tipo}, Stato: {ticket.get_stato()}")

   
    # Calcola il totale dei preventivi di tutti i ticket
    def totale_preventivi(self) -> float:
        # Usa polimorfismo: calcola il preventivo per ogni ticket
        return sum(ticket.calcola_preventivo() for ticket in self.tickets)

    
    # Statistiche per tipo di elettrodomestico
    def statistiche_per_tipo(self):
        # Inizializza il contatore per ciascun tipo
        count = {"Lavatrice": 0, "Frigorifero": 0, "Forno": 0}
        
        for ticket in self.tickets:
            elettro = ticket.get_elettrodomestico()
            
            # Usa isinstance per capire di quale sottoclasse si tratta
            if isinstance(elettro, Lavatrice):
                count["Lavatrice"] += 1
            elif isinstance(elettro, Frigorifero):
                count["Frigorifero"] += 1
            elif isinstance(elettro, Forno):
                count["Forno"] += 1

        # Stampa il report
        print("Statistiche per tipo di elettrodomestico:")
        for k, v in count.items():
            print(f"Numero di {k} in riparazione: {v}")
