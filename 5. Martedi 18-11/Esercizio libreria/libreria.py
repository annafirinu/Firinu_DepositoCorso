class Libreria:#Creo la classe libreria
    def __init__(self):
        self.catalogo = []   #Creo la lista che conterrà gli oggetti della classe Libro
        self.matrice = []    # matrice: ogni riga = [titolo, autore, isbn]

    def aggiungi_libro(self, libro):
        self.catalogo.append(libro)#Aggiungo il libro alla lista
        self.matrice.append([libro.titolo, libro.autore, libro.isbn])#Aggiungo il libro alla matrice

    def rimuovi_libro(self, isbn):
        self.catalogo = [l for l in self.catalogo if l.isbn != isbn]#Rimuovo elemento con quel determinato isbn dalla lista
        self.matrice = [r for r in self.matrice if r[2] != isbn]#Rimuovo elemento con quel determinato isbn dalla matrice

    def cerca_per_titolo(self, titolo):
        return [l for l in self.catalogo if l.titolo.lower() == titolo.lower()]#Cerco l'elemento con quel determinato titolo

    def mostra_catalogo(self): #Stampo il catalogo tramite le liste
        if not self.catalogo:
            print("Il catalogo è vuoto")
        else:
            for libro in self.catalogo:
                print(libro.descrizione())

    def mostra_matrice(self): #Stampo la matrice che contiene tutti i libri
        print("Matrice dei dati:")
        for riga in self.matrice:
            print(riga)

