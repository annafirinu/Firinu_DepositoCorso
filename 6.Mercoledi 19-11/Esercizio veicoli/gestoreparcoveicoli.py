from classiderivate import Auto, Furgone, Motocicletta
from veicolo import Veicolo

class GestoreParcoVeicoli:
    def __init__(self):
        self.__veicoli: list[Veicolo] = []#Lista privata che andrà a contenere tutti i veicoli

    def aggiungi_veicolo(self, veicolo: Veicolo):
        self.__veicoli.append(veicolo)
        print(f"{type(veicolo).__name__} aggiunto al parco: {veicolo._Veicolo__marca} {veicolo._Veicolo__modello}")

    def rimuovi_veicolo(self, marca: str, modello: str):
        for v in self.__veicoli:
            if v._Veicolo__marca == marca and v._Veicolo__modello == modello:
                self.__veicoli.remove(v)
                print(f"{marca} {modello} rimosso dal parco.")
                return
        print(f"{marca} {modello} non trovato nel parco.")

    def lista_veicoli(self):
        if not self.__veicoli:
            print("Parco veicoli vuoto.")
            return
        print("Lista dei veicoli nel parco:")
        for i, v in enumerate(self.__veicoli, start=1):
            print(f"{i}. {v}")

    def get_veicoli(self):
        return self.__veicoli
