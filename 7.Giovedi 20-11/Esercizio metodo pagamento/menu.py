from pagamenti import MetodoPagamento, CartaDiCredito, PayPal, BonificoBancario, gestisci_pagamento

def menu():
    while True:
        print("\n--- MENU PAGAMENTI ---")
        print("1. Metodo Generico")
        print("2. Carta di Credito")
        print("3. PayPal")
        print("4. Bonifico Bancario")
        print("5. Esci")

        scelta = input("Scegli un'opzione: ")

        if scelta == "1":
            importo = float(input("Inserisci importo: "))
            metodo = MetodoPagamento()

        elif scelta == "2":
            numero = input("Inserisci numero carta: ")
            importo = float(input("Inserisci importo: "))
            metodo = CartaDiCredito(numero)

        elif scelta == "3":
            email = input("Inserisci email PayPal: ")
            importo = float(input("Inserisci importo: "))
            metodo = PayPal(email)

        elif scelta == "4":
            iban = input("Inserisci IBAN: ")
            importo = float(input("Inserisci importo: "))
            metodo = BonificoBancario(iban)

        elif scelta == "5":
            print("Uscita...")
            break

        else:
            print("Scelta non valida!")
            continue

        gestisci_pagamento(metodo, importo)


if __name__ == "__main__":
    menu()

