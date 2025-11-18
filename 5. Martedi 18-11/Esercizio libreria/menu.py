from libro import Libro #Importo la classe libro
from libreria import Libreria #Importo la classe libreria

def menu(): #Creo il menu con le varie opzioni possibili
    print("\nLIBRERIA")
    print("1. Aggiungi libro")
    print("2. Rimuovi libro tramite ISBN")
    print("3. Cerca libro per titolo")
    print("4. Mostra catalogo")
    print("5. Esci")

libreria = Libreria()

#Oltre quelli che sceglierà l'utente inserisco qualche libro nel catalogo
libri_iniziali = [
    Libro("Il Signore degli Anelli", "J.R.R. Tolkien", "111"),
    Libro("Harry Potter e la Pietra Filosofale", "J.K. Rowling", "222"),
    Libro("1984", "George Orwell", "333"),
    Libro("Il Piccolo Principe", "Antoine de Saint-Exupéry", "444"),
    Libro("I Promessi Sposi", "Alessandro Manzoni", "555")
]

for libro in libri_iniziali:#Aggiungo i libri al catalogo
    libreria.aggiungi_libro(libro)

#Chiedo all'utente di scegliere l'operazione che desidera
while True:
    menu()
    scelta = input("Scelta: ")

    if scelta == "1":
        print("\nAggiungi libro")
        titolo = input("Titolo: ")
        autore = input("Autore: ")
        isbn = input("ISBN: ")

        libro = Libro(titolo, autore, isbn)
        libreria.aggiungi_libro(libro) #Aggiungo il libro al catalogo 

        print("Libro aggiunto\n")

    elif scelta == "2":
        print("\nRimuovi libro")
        isbn = input("ISBN del libro da rimuovere: ")
        libreria.rimuovi_libro(isbn) #Rimuovo il libro dal catalogo
        print("Libro rimosso")

    elif scelta == "3":
        print("\nCerca per titolo")
        titolo = input("Titolo da cercare: ")

        risultati = libreria.cerca_per_titolo(titolo)#Cerco il libro per titolo

        if not risultati:
            print("Nessun libro trovato")
        else:
            print("\nRisultati:")
            matrice_ricerca = [[l.titolo, l.autore, l.isbn] for l in risultati]
            for riga in matrice_ricerca:
                print(riga)

    elif scelta == "4":
        print("\nCatalogo Attuale")
        libreria.mostra_matrice() #Stampo il catalogo della libreria in formato matrice

    elif scelta == "5":
        print("\nArrivederci")
        break

    else:
        print("Scelta non valida!")
