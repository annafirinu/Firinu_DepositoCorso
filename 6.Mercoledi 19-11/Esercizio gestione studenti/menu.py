from classi import Studente, Professore

def menu():
    studenti = []
    professori = []

    while True:
        print("\nMENU")
        print("1. Aggiungi Studente")
        print("2. Aggiungi Professore")
        print("3. Mostra Studenti")
        print("4. Mostra Professori")
        print("5. Calcola media di uno studente")
        print("6. Esci")

        scelta = input("Seleziona un'opzione: ")

        if scelta == "1":
            nome = ""
            while nome == "":
                nome = input("Nome dello studente: ")
                if nome == "":
                    print("Inserire un testo valido")

            
            eta = None
            while eta is None:
                s = input("Età dello studente: ")
                if s.isdigit():
                    eta = int(s)
                else:
                    print("Inserire un numero intero maggiore o uguale a 0")

            
            voti = None
            while voti is None:
                s = input("Voti dello studente (separati da spazio): ")
                parti = s.split()
                if all(p.isdigit() for p in parti):
                    voti = [int(p) for p in parti]
                else:
                    print("Inserire solo numeri interi separati da spazio")

            studenti.append(Studente(nome, eta, voti))
            print("Studente aggiunto con successo!")

        elif scelta == "2":
            
            nome = ""
            while nome == "":
                nome = input("Nome del professore: ")
                if nome == "":
                    print("Inserire un testo valido")

            
            eta = None
            while eta is None:
                s = input("Età del professore: ")
                if s.isdigit():
                    eta = int(s)
                else:
                    print("Inserire un numero intero maggiore o uguale a 0")

            
            materia = ""
            while materia == "":
                materia = input("Materia insegnata: ")
                if materia == "":
                    print("Inserire un testo valido")

            professori.append(Professore(nome, eta, materia))
            print("Professore aggiunto con successo!")

        elif scelta == "3":
            if not studenti:
                print("Nessuno studente registrato")
            else:
                print("\nElenco Studenti")
                for s in studenti:
                    s.presentazione()

        elif scelta == "4":
            if not professori:
                print("Nessun professore registrato")
            else:
                print("\nElenco Professori")
                for p in professori:
                    p.presentazione()

        elif scelta == "5":
            if not studenti:
                print("Nessuno studente registrato")
            else:
                print("\nSeleziona lo studente per calcolare la media:")
                for i, s in enumerate(studenti):
                    print(f"{i}. {s.get_nome()}")
                idx = None
                while idx is None:
                    s = input("Inserisci il numero dello studente: ")
                    if s.isdigit() and 0 <= int(s) < len(studenti):
                        idx = int(s)
                    else:
                        print("Indice non valido")
                print(f"Media di {studenti[idx].get_nome()}: {studenti[idx].calcola_media():.2f}")

        elif scelta == "6":
            print("Arrivederci")
            break

        else:
            print("Opzione non valida, riprova")

if __name__ == "__main__":
    menu()
