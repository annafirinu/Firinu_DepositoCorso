class Prodotto: #Creo una classe chiamata Prodotto
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita

    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione


class Elettronica: #Creo una classe parallela chiamata Elettronica
    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        self.garanzia = garanzia

    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione


class Abbigliamento: #Creo una classe parallela chiamata Abbigliamento
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        self.materiale = materiale

    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione


class Fabbrica: #Creo una classe chiamata Fabbrica
    def __init__(self):
        self.inventario = {} #Dizionario che tiene traccia del numero di ogni tipo di prodotto in magazzino

    def aggiungi_prodotto(self, prodotto):
      if prodotto.nome in self.inventario:
        self.inventario[prodotto.nome] += 1
      else:
        self.inventario[prodotto.nome] = 1

      print(f"Aggiunto 1 prodotto: {prodotto.nome}")

    def vendi_prodotto(self, prodotto):
      if prodotto.nome not in self.inventario or self.inventario[prodotto.nome] == 0: #Controllo che ci sia almeno un pezzo di quel prodotto
        print("Prodotto non disponibile")
        return
    
      self.inventario[prodotto.nome] -= 1 #Diminuisco la quantità

      profitto = prodotto.calcola_profitto() #Calcolo il profitto

      print(f"Venduto 1 {prodotto.nome}. Profitto: {profitto}€")


    def resi_prodotto(self, prodotto):
      if prodotto.nome in self.inventario:
        self.inventario[prodotto.nome] += 1 #Aumento la quantità se il prodotto esiste
      else:
        self.inventario[prodotto.nome] = 1 #Aggiungo un pezzo se non esiste

      print(f"Reso un pezzo di di {prodotto.nome}")

#Testo i metodi

#Creo alcuni prodotti
maglia = Abbigliamento("Maglia", 5, 20, "Cotone")
portatile = Elettronica("Portatile", 400, 700, "2 anni")
smartwatch = Elettronica("Smartwatch", 100, 180, "1 anno")

#Creo la fabbrica
fabbrica = Fabbrica()

#Aggiungo prodotti all'inventario
fabbrica.aggiungi_prodotto(maglia)
fabbrica.aggiungi_prodotto(portatile)
fabbrica.aggiungi_prodotto(smartwatch)

#Stampo l'inventario iniziale
print("\n Inventario iniziale")
print(fabbrica.inventario)

#Vendo uno smartwatch
fabbrica.vendi_prodotto(smartwatch)

#Stampo l'inventario 
print("\n Inventario:")
print(fabbrica.inventario)

#Reso di un portatile
fabbrica.resi_prodotto(portatile)

#Stampo l'inventario 
print("\n Inventario:")
print(fabbrica.inventario)
