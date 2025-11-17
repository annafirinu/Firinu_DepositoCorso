class Libro:  # Creo una classe chiamata Libro
    def __init__(self, titolo, autore, pagine):  # Attributi titolo, autore, pagine
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    # Metodo descrizione che mi restituisce una stampa
    def descrizione(self):
        return f"Il libro '{self.titolo}' è stato scritto da '{self.autore}' e ha '{self.pagine}' pagine."


class Biblioteca: #Creo una classe Biblioteca
    def __init__(self):
        self.libri = []  #Creo una lista che conterrà tutti i libri

    def aggiungi_libro(self, libro):
        self.libri.append(libro) #Aggiungo alla lista ogni libro inserito

    def stampa_libri(self):
        if not self.libri: #Stampo tutti i libri presenti nella biblioteca
            print("La biblioteca è vuota.")
        else:
            print("\n Lista dei libri nella biblioteca:")
            for libro in self.libri:
                print(libro.descrizione())


biblioteca = Biblioteca()

#Chiedo all'utente di inserire Titolo, Autore e numero pagine per ogni libro
while True:  
    print("\nAggiungi un libro alla biblioteca:")
    titolo = input("Titolo: ")
    autore = input("Autore: ")
    pagine = input("Numero di pagine: ")

    nuovo_libro = Libro(titolo, autore, pagine)#Creo un nuovo libro

    biblioteca.aggiungi_libro(nuovo_libro)#Aggiungo il libro alla biblioteca

    scelta = input("Vuoi aggiungere un altro libro? (si o no): ")#Chiedo all'utente se vuole aggiungere altri libri
    if scelta.lower() != 'si':
        break

# Stampo tutti i libri
biblioteca.stampa_libri()
