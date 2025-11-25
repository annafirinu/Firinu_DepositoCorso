from operazioni import (
    crea_matrice,
    sotto_matrice_centrale,
    trasposta,
    somma_elementi,
    moltiplicazione_elementwise,
    media_matrice,
    determinante
)

def main():
    matrice = None  # Inizialmente non c'è nessuna matrice creata

    while True:
        print("\nMENU")
        print("1. Creare nuova matrice ")
        print("2. Estrarre sotto-matrice centrale")
        print("3. Trasporre matrice")
        print("4. Somma degli elementi")
        print("5. Moltiplicazione element-wise con un'altra matrice")
        print("6. Media degli elementi")
        print("7. Determinante")
        print("8. Leggi risultati da file")
        print("9. Uscire")

        scelta = input("Scegli un'opzione: ")

        if scelta == "1":
            matrice = crea_matrice()

        elif scelta == "2":
            if matrice is None:
                print("Crea una matrice")
            else:
                sotto_matrice_centrale(matrice)

        elif scelta == "3":
            if matrice is None:
                print("Crea una matrice")
            else:
                trasposta(matrice)

        elif scelta == "4":
            if matrice is None:
                print("Crea una matrice")
            else:
                somma_elementi(matrice)

        elif scelta == "5":
            if matrice is None:
                print("Crea una matrice")
            else:
                moltiplicazione_elementwise(matrice)

        elif scelta == "6":
            if matrice is None:
                print("Crea una matrice")
            else:
                media_matrice(matrice)

        elif scelta == "7":
            if matrice is None:
                print("Crea una matrice")
            else:
                determinante(matrice)
                
        elif scelta == "8":
            with open("risultati.txt", "r") as f:
                contenuto = f.read()
                if contenuto.strip() == "":
                    print("\nIl file è vuoto")
                else:
                    print("\nContenuto di risultati.txt")
                    print(contenuto)
                    print("-------------------------\n")

        elif scelta == "9":
            print("Arrivederci")
            break

        else:
            print("Scelta non valida")

if __name__ == "__main__":
    main()
