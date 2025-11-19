from conto_bancario import ContoBancario  #Importo la classe conto bancario

def menu(): #Prima di accedere al menu chiedo all'utente di creare il conto
    print("Creazione Conto Bancario:")
    nome = input("Inserisci il nome del titolare: ")
    saldo_iniziale = float(input("Inserisci saldo iniziale: "))

    conto = ContoBancario(nome, saldo_iniziale)

    while True: #Menu che permette di utilizzare tutti i metodi
        print("\nMENU OPERAZIONI")
        print("1. Deposita")
        print("2. Preleva")
        print("3. Visualizza saldo")
        print("4. Modifica titolare")
        print("5. Esci")

        scelta = input("Seleziona un'opzione: ")

        if scelta == "1":#Richiamo il metodo deposita
            importo = float(input("Importo da depositare: "))
            if conto.deposita(importo):
                print("Deposito effettuato")
            else:
                print("Importo non valido")

        elif scelta == "2":#Richiamo il metodo preleva
            importo = float(input("Importo da prelevare: "))
            if conto.preleva(importo):
                print("Prelievo effettuato")
            else:
                print("Importo non valido o saldo insufficiente")

        elif scelta == "3":#Richiamo il metodo visualizza_saldo
            print(f"Saldo attuale: {conto.visualizza_saldo()} €")

        elif scelta == "4":#Modifico il nome del titolare
            nuovo_nome = input("Nuovo titolare: ")
            conto.set_titolare(nuovo_nome)
            print("Titolare aggiornato")

        elif scelta == "5":#Esco
            print("Arrivederci")
            break

        else:
            print("Scelta non valida.")

if __name__ == "__main__":
    menu()
