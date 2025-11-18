class UnitaMilitare: #Creo la classe base UnitaMilitare
    def __init__(self, nome: str, numero_soldati: int): #Definisco gli attribuiti impostando anche il tipo di dato richiesto
        self.nome: str = nome
        self.numero_soldati: int = numero_soldati

    def muovi(self):
        print(f"L'unita è in movimento")
        
    def attacca(self):
        print(f"Stiamo attaccando")
        
    def ritira(self):
        print(f"L'unita è in movimento")