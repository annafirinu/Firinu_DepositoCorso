class Ristorante: #Creo una classe chiamata Ristorante
    def __init__(self, nome, tipo_cucina): #Creo il costruttore contenente come parametri nome e tipo cucina
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.aperto = False  #Creo l'attributo aperto che di default è impostato su False
        self.menu = {} #Creo un dizionario vuoto dove successivamente verranno aggiunti i piatti del menù

    #Metodo descrivi ristorante
    def descrivi_ristorante(self):
        print(f"Nel ristorante '{self.nome}' troverai cucina {self.tipo_cucina}")

    #Metodo stato apertura
    def stato_apertura(self):
        if self.aperto:
            print("Il ristorante è aperto")
        else:
            print("Il ristorante è chiuso")

    #Metodo apri ristorante
    def apri_ristorante(self):
        self.aperto = True
        print("Il ristorante ora è aperto")

    #Metodo chiudi ristorante
    def chiudi_ristorante(self):
        self.aperto = False
        print("Il ristorante ora è chiuso")

    #Metodo aggiungi al menu
    def aggiungi_al_menu(self, piatto, prezzo):
        self.menu[piatto] = prezzo #Essendo menu un dizionario aggiungo la copia chiave valore
        print(f"Il piatto '{piatto}'è stato aggiunto al menu a {prezzo}€")

    #Metodo togli dal menu
    def togli_dal_menu(self, piatto):
        if piatto in self.menu:
            del self.menu[piatto]
            print(f"Il piatto '{piatto}' è stato rimosso dal menu")
        else:
            print(f"Il piatto '{piatto}' non è presente nel menu")

    #Metodo stampa menu
    def stampa_menu(self):
        if not self.menu:
            print("Menu vuoto")
        else:
            print("\n MENU ")
            for piatto, prezzo in self.menu.items():
                print(f"{piatto}: {prezzo}€")
            print("\n")
            
#Creo il ristorante
ristorante = Ristorante("Da Anna", "italiana")

# Testo i metodi
ristorante.descrivi_ristorante()
ristorante.stato_apertura()

ristorante.apri_ristorante()

ristorante.aggiungi_al_menu("Carbonara", 12)
ristorante.aggiungi_al_menu("Amatriciana",11)
ristorante.aggiungi_al_menu("Gricia", 10)

ristorante.stampa_menu()

ristorante.togli_dal_menu("Amatriciana")

ristorante.stampa_menu()

ristorante.chiudi_ristorante()


