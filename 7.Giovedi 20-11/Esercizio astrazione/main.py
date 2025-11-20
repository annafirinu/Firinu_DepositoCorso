from impiegati import ImpiegatoFisso, ImpiegatoAProvvigione, stampa_info_impiegato

def main():
    impiegati = []

    # Funzione per cercare un impiegato per nome e cognome
    def trova_impiegato(nome, cognome):
        for imp in impiegati:
            if imp.nome == nome and imp.cognome == cognome:
                return imp
        return None

    while True:
        print("\nGestione Impiegati")
        print("1. Aggiungi Impiegato Fisso")
        print("2. Aggiungi Impiegato a Provvigione")
        print("3. Mostra stipendio di un impiegato")
        print("4. Mostra tutti gli impiegati")
        print("5. Esci")
        
        scelta = input("Seleziona un'opzione (1-5): ")

        if scelta == '1':
            nome = input("Nome: ")
            cognome = input("Cognome: ")
            stipendio_base = float(input("Stipendio base: "))
            imp = ImpiegatoFisso(nome, cognome, stipendio_base)
            impiegati.append(imp)
            print("Impiegato fisso aggiunto!")

        elif scelta == '2':
            nome = input("Nome: ")
            cognome = input("Cognome: ")
            stipendio_base = float(input("Stipendio base: "))
            vendite = float(input("Totale vendite: "))
            percentuale_bonus = float(input("Percentuale bonus: "))
            imp = ImpiegatoAProvvigione(nome, cognome, stipendio_base, vendite, percentuale_bonus)
            impiegati.append(imp)
            print("Impiegato a provvigione aggiunto!")

        elif scelta == '3':
            nome = input("Nome impiegato: ")
            cognome = input("Cognome impiegato: ")
            imp = trova_impiegato(nome, cognome)
            if imp:
                print(f"Stipendio calcolato: {imp.calcola_stipendio():.2f}")
            else:
                print("Impiegato non trovato")

        elif scelta == '4':
            if not impiegati:
                print("Nessun impiegato inserito")
            else:
                print("\nLista Impiegati e Stipendi")
                for imp in impiegati:
                    stampa_info_impiegato(imp)

        elif scelta == '5':
            print("Arrivederci!")
            break

        else:
            print("Opzione non valida, riprova")

if __name__ == "__main__":
    main()
