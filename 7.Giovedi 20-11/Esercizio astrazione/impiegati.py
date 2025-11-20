from abc import ABC, abstractmethod

#Classe astratta Impiegato
class Impiegato(ABC):
    def __init__(self, nome, cognome, stipendio_base):
        self.nome = nome
        self.cognome = cognome
        self.stipendio_base = stipendio_base

    @abstractmethod
    def calcola_stipendio(self):
        pass

#Classe derivata ImpiegatoFisso
class ImpiegatoFisso(Impiegato):
    def calcola_stipendio(self):
        return self.stipendio_base

#Classe derivata ImpiegatoAProvvigione
class ImpiegatoAProvvigione(Impiegato):
    def __init__(self, nome, cognome, stipendio_base, vendite, percentuale_bonus):
        super().__init__(nome, cognome, stipendio_base)
        self.vendite = vendite
        self.percentuale_bonus = percentuale_bonus 

    def calcola_stipendio(self):
        bonus = self.vendite * self.percentuale_bonus
        return self.stipendio_base + bonus


def stampa_info_impiegato(impiegato):
    print(f"Nome: {impiegato.nome}")
    print(f"Cognome: {impiegato.cognome}")
    print(f"Stipendio calcolato: {impiegato.calcola_stipendio():.2f}")
    print("-" * 30)
