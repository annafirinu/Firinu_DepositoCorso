from datetime import datetime

# Classe base Elettrodomestico
class Elettrodomestico:
    def __init__(self, marca: str, modello: str, anno_acquisto: int, guasto: str):
        # Attributi privati (incapsulamento)
        self.__marca: str = marca
        self.__modello: str = modello
        
        # Controllo semplice sull'anno di acquisto
        if anno_acquisto > datetime.now().year:
            print("L'anno non può essere nel futuro")
        self.__anno_acquisto: int = anno_acquisto
        self.__guasto: str = guasto

    # Getter e setter per gli attributi
    def get_marca(self) -> str:
        return self.__marca

    def set_marca(self, marca: str):
        self.__marca = marca

    def get_modello(self) -> str:
        return self.__modello

    def set_modello(self, modello: str):
        self.__modello = modello

    def get_anno_acquisto(self) -> int:
        return self.__anno_acquisto

    def set_anno_acquisto(self, anno: int):
        if anno > datetime.now().year:
            print("L'anno non può essere nel futuro")
        self.__anno_acquisto = anno

    def get_guasto(self) -> str:
        return self.__guasto

    def set_guasto(self, guasto: str):
        self.__guasto = guasto

    
    # Metodi principali
    def descrizione(self) -> str:
        # Restituisce una descrizione testuale dell'elettrodomestico
        return f"Marca: {self.__marca}, modello: {self.__modello}, acquistato nel: {self.__anno_acquisto}, guasto: {self.__guasto}"

    def stima_costo_base(self) -> float:
        # Costo base generico per la diagnosi/riparazione
        return 50.0



# Classe Lavatrice (sottoclasse di Elettrodomestico)
class Lavatrice(Elettrodomestico):
    def __init__(self, marca: str, modello: str, anno_acquisto: int, guasto: str, capacita_kg: int, giri_centrifuga: int):
        super().__init__(marca, modello, anno_acquisto, guasto)
        # Attributi specifici della lavatrice
        self.__capacita_kg: int = capacita_kg
        self.__giri_centrifuga: int = giri_centrifuga

    # Getter e setter
    def get_capacita_kg(self) -> int:
        return self.__capacita_kg

    def set_capacita_kg(self, kg: int):
        self.__capacita_kg = kg

    def get_giri_centrifuga(self):
        return self.__giri_centrifuga

    def set_giri_centrifuga(self, giri: int):
        self.__giri_centrifuga = giri

    # Metodo polimorfico: stima costo base specifico per lavatrice
    def stima_costo_base(self) -> float:
        base = super().stima_costo_base()
        if self.__capacita_kg > 7:  # maggior costo se capacità elevata
            base += 20
        return base



# Classe Frigorifero (sottoclasse di Elettrodomestico)
class Frigorifero(Elettrodomestico):
    def __init__(self, marca: str, modello: str, anno_acquisto: int, guasto: str, litri: int, ha_freezer: bool):
        super().__init__(marca, modello, anno_acquisto, guasto)
        # Attributi specifici del frigorifero
        self.__litri: int = litri
        self.__ha_freezer: bool = ha_freezer

    # Getter e setter
    def get_litri(self) -> int:
        return self.__litri

    def set_litri(self, litri: int):
        self.__litri = litri

    def get_ha_freezer(self) -> bool:
        return self.__ha_freezer

    def set_ha_freezer(self, ha_freezer: bool):
        self.__ha_freezer = ha_freezer

    # Metodo polimorfico: stima costo base specifico per frigorifero
    def stima_costo_base(self) -> float:
        base = super().stima_costo_base()
        if self.__litri > 300:  # maggior costo se capacità grande
            base += 25
        if self.__ha_freezer:    # costo aggiuntivo se ha freezer
            base += 15
        return base



# Classe Forno (sottoclasse di Elettrodomestico)
class Forno(Elettrodomestico):
    def __init__(self, marca: str, modello: str, anno_acquisto: int, guasto: str, tipo_alimentazione: str, ha_ventilato: bool):
        super().__init__(marca, modello, anno_acquisto, guasto)
        # Attributi specifici del forno
        self.__tipo_alimentazione: str = tipo_alimentazione
        self.__ha_ventilato: bool = ha_ventilato

    # Getter e setter
    def get_tipo_alimentazione(self) -> str:
        return self.__tipo_alimentazione

    def set_tipo_alimentazione(self, tipo: str):
        self.__tipo_alimentazione = tipo

    def get_ha_ventilato(self) -> bool:
        return self.__ha_ventilato

    def set_ha_ventilato(self, ventilato: bool):
        self.__ha_ventilato = ventilato

    # Metodo polimorfico: stima costo base specifico per forno
    def stima_costo_base(self) -> float:
        base = super().stima_costo_base()
        if self.__tipo_alimentazione == "gas":  # maggior costo se a gas
            base += 20
        if self.__ha_ventilato:  # costo aggiuntivo se ventilato
            base += 10
        return base
