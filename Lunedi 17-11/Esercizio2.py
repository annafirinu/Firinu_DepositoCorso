class Libro: #Creo una classe chiamata Libro
    def __init__(self, titolo, autore, pagine):#Attributi titolo, autore, pagine
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
    #Metodo descrizione che mi restituisce una stampa
    def descrizione(self):
        return f"Il libro '{self.titolo}' è stato scritto da '{self.autore}' e ha '{self.pagine}' pagine."


# Utilizzo la classe
libro1 = Libro("Il Signore degli Anelli", "J.R.R. Tolkien", 1200)
print(libro1.descrizione())
