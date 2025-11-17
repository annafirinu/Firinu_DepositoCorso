from vendite import inserisci_dati, calcola_totale_media, vendite_sopra_media

def menu():
    vendite = [120, 250, 300, 180, 400] #Dati preinseriti
    while True:#L'utente può scegliere che cosa fare finchè non decide di uscire
        print("\nMenu")
        print("1. Inserisci dati di vendita")
        print("2. Mostra totale e media vendite")
        print("3. Mostra vendite sopra la media")
        print("4. Esci")
        scelta = input("Scegli un'opzione (1-4): ")
#Utilizzo le funzioni create precedentemente
        if scelta == "1":
            nuove_vendite = inserisci_dati() 
            vendite.extend(nuove_vendite)  
            print("Dati inseriti correttamente!")
        elif scelta == "2":
            if len(vendite) == 0:
                print("Non ci sono dati di vendita da analizzare")
            else:
                totale, media = calcola_totale_media(vendite)
                print(f"Totale vendite: {totale}")
                print(f"Media vendite: {media:.2f}")
        elif scelta == "3":
            if len(vendite) == 0:
                print("Non ci sono dati di vendita da analizzare")
            else:
                totale, media = calcola_totale_media(vendite)
                sopra = vendite_sopra_media(vendite, media)
                if sopra:
                    print(f"Vendite sopra la media ({media:.2f}):")
                    for giorno, valore in sopra:
                        print(f"Giorno {giorno}: {valore}")
                else:
                    print(f"Nessuna vendita supera la media ({media:.2f}).")
        elif scelta == "4":
            print("Arrivederci!")
            break
        else:
            print("Scelta non valida, riprova")


if __name__ == "__main__":
    menu()
