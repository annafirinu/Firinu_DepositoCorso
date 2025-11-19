# menu.py
from gestoreparcoveicoli import GestoreParcoVeicoli
from classiderivate import Auto, Furgone, Motocicletta

def menu():
    gestore = GestoreParcoVeicoli()

    while True:
        print("\n--- Menu Gestore Parco Veicoli ---")
        print("1. Aggiungi Auto")
        print("2. Aggiungi Furgone")
        print("3. Aggiungi Motocicletta")
        print("4. Rimuovi Veicolo")
        print("5. Lista Veicoli")
        print("6. Accendi Veicolo")
        print("7. Spegni Veicolo")
        print("8. Suona Clacson Auto")
        print("9. Carica Furgone")
        print("10. Scarica Furgone")
        print("11. Wheelie Motocicletta")
        print("0. Esci")

        scelta = input("Scegli un'opzione: ")

        if scelta == "1":
            marca = input("Marca: ")
            modello = input("Modello: ")
            anno = int(input("Anno: "))
            porte = int(input("Numero porte: "))
            gestore.aggiungi_veicolo(Auto(marca, modello, anno, porte))

        elif scelta == "2":
            marca = input("Marca: ")
            modello = input("Modello: ")
            anno = int(input("Anno: "))
            capacita = int(input("Capacità carico (kg): "))
            gestore.aggiungi_veicolo(Furgone(marca, modello, anno, capacita))

        elif scelta == "3":
            marca = input("Marca: ")
            modello = input("Modello: ")
            anno = int(input("Anno: "))
            tipo = input("Tipo (sportiva/touring): ")
            gestore.aggiungi_veicolo(Motocicletta(marca, modello, anno, tipo))

        elif scelta == "4":
            marca = input("Marca: ")
            modello = input("Modello: ")
            gestore.rimuovi_veicolo(marca, modello)

        elif scelta == "5":
            gestore.lista_veicoli()

        elif scelta == "6":
            marca = input("Marca: ")
            modello = input("Modello: ")
            for v in gestore.get_veicoli():
                if v._Veicolo__marca == marca and v._Veicolo__modello == modello:
                    v.accendi()
                    break

        elif scelta == "7":
            marca = input("Marca: ")
            modello = input("Modello: ")
            for v in gestore.get_veicoli():
                if v._Veicolo__marca == marca and v._Veicolo__modello == modello:
                    v.spegni()
                    break

        elif scelta == "8":
            marca = input("Marca Auto: ")
            modello = input("Modello Auto: ")
            for v in gestore.get_veicoli():
                if isinstance(v, Auto) and v._Veicolo__marca == marca and v._Veicolo__modello == modello:
                    v.suona_clacson()
                    break

        elif scelta == "9":
            marca = input("Marca Furgone: ")
            modello = input("Modello Furgone: ")
            peso = int(input("Peso da caricare: "))
            for v in gestore.get_veicoli():
                if isinstance(v, Furgone) and v._Veicolo__marca == marca and v._Veicolo__modello == modello:
                    v.carica(peso)
                    break

        elif scelta == "10":
            marca = input("Marca Furgone: ")
            modello = input("Modello Furgone: ")
            peso = int(input("Peso da scaricare: "))
            for v in gestore.get_veicoli():
                if isinstance(v, Furgone) and v._Veicolo__marca == marca and v._Veicolo__modello == modello:
                    v.scarica(peso)
                    break

        elif scelta == "11":
            marca = input("Marca Moto: ")
            modello = input("Modello Moto: ")
            for v in gestore.get_veicoli():
                if isinstance(v, Motocicletta) and v._Veicolo__marca == marca and v._Veicolo__modello == modello:
                    v.esegui_wheelie()
                    break

        elif scelta == "0":
            print("Uscita dal programma.")
            break

        else:
            print("Opzione non valida. Riprova.")

# Avvio del menu
if __name__ == "__main__":
    menu()
