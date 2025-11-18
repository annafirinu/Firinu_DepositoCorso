from membrosquadra import MembroSquadra

class Giocatore(MembroSquadra): #Definisco la classe giocatore
    def __init__(self, nome, eta, ruolo, numero_maglia):
        super().__init__(nome, eta)
        self.ruolo = ruolo
        self.numero_maglia = numero_maglia

    def descrivi(self):
        super().descrivi()
        print(f"Ruolo: {self.ruolo}, Numero maglia: {self.numero_maglia}")

    def gioca_partita(self):
        print(f"{self.nome} sta partecipando come {self.ruolo} con la maglia n {self.numero_maglia}")


class Allenatore(MembroSquadra): #Definisco la classe Allenatore
    def __init__(self, nome, eta, anni_di_esperienza):
        super().__init__(nome, eta)
        self.anni_di_esperienza = anni_di_esperienza

    def descrivi(self):
        super().descrivi()
        print(f"Anni di esperienza: {self.anni_di_esperienza}")

    def dirige_allenamento(self):
        print(f"{self.nome} sta dirigendo l'allenamento con {self.anni_di_esperienza} anni di esperienza")


class Assistente(MembroSquadra): #Definisco la classe Assistente
    def __init__(self, nome, eta, specializzazione):
        super().__init__(nome, eta)
        self.specializzazione = specializzazione

    def descrivi(self):
        super().descrivi()
        print(f"Specializzazione: {self.specializzazione}")

    def supporta_team(self):
        print(f"{self.nome} sta supportando il team come {self.specializzazione}")
