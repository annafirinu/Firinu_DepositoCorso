class MembroSquadra: #Creo la classe base MembroSquadra
    def __init__(self, nome: str, eta: int): #Definisco gli attribuiti impostando anche il tipo di dato richiesto
        self.nome: str = nome
        self.eta: int = eta

    def descrivi(self):
        print(f"Nome: {self.nome}, Età: {self.eta}")