from elettrodomestici import Lavatrice, Frigorifero, Forno
from ticket import TicketRiparazione
from officina import Officina

def main():
    print("Gestionale Officina Elettrodomestici")
    nome_officina = input("Inserisci il nome dell'officina: ")
    officina = Officina(nome_officina)

    while True:
        print("\n--- Menu ---")
        print("1. Aggiungi ticket")
        print("2. Chiudi ticket")
        print("3. Stampa ticket aperti")
        print("4. Totale preventivi")
        print("5. Statistiche per tipo")
        print("0. Esci")
        scelta = input("Scegli un'opzione: ")

        if scelta == "1":
            # Creazione di un nuovo ticket
            tipo = input("Tipo elettrodomestico (Lavatrice/Frigorifero/Forno): ").lower()
            marca = input("Marca: ")
            modello = input("Modello: ")
            anno = int(input("Anno di acquisto: "))
            guasto = input("Descrizione guasto: ")
            id_ticket = input("ID Ticket: ")

            if tipo == "lavatrice":
                capacita = int(input("Capacità kg: "))
                giri = int(input("Giri centrifuga: "))
                elettro = Lavatrice(marca, modello, anno, guasto, capacita, giri)
            elif tipo == "frigorifero":
                litri = int(input("Litri: "))
                freezer_input = input("Ha freezer? (si/no): ").lower()
                freezer = freezer_input == "si"
                elettro = Frigorifero(marca, modello, anno, guasto, litri, freezer)
            elif tipo == "forno":
                tipo_alim = input("Tipo alimentazione (elettrico/gas): ").lower()
                ventilato_input = input("Ha ventilato? (si/no): ").lower()
                ventilato = ventilato_input == "si"
                elettro = Forno(marca, modello, anno, guasto, tipo_alim, ventilato)
            else:
                print("Tipo non valido!")
                continue

            ticket = TicketRiparazione(id_ticket, elettro)
            officina.aggiungi_ticket(ticket)
            print("Ticket aggiunto correttamente!")

        elif scelta == "2":
            id_ticket = input("Inserisci ID ticket da chiudere: ")
            officina.chiudi_ticket(id_ticket)

        elif scelta == "3":
            officina.stampa_ticket_aperti()

        elif scelta == "4":
            totale = officina.totale_preventivi()
            print(f"Totale preventivi di tutti i ticket: {totale:.2f} €")

        elif scelta == "5":
            officina.statistiche_per_tipo()

        elif scelta == "0":
            print("Arrivederci!")
            break
        else:
            print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    main()
