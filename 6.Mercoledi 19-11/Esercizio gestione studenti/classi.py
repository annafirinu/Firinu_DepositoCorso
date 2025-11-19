class Persona:#Creo la classe base persona
    def __init__(self, nome: str, eta: int): #Tra i parametri del costruttore impongo che nome sia una stringa e eta un intero
        self.__nome = nome #Creo l'attributo privato nome
        self.__eta = eta #Creo l'attributo privato eta


    def get_nome(self) -> str: #Metodo get che permette di leggere il nome dall'esterno
        return self.__nome

    def set_nome(self, nome: str):#Metodo set che permette di modificare il nome dall'esterno
        self.__nome = nome

    def get_eta(self) -> int:#Metodo get che permette di leggere l'eta dall'esterno
        return self.__eta

    def set_eta(self, eta: int):#Metodo set che permette di modificare l'eta dall'esterno
        self.__eta = eta

    def presentazione(self):#Metodo presentazione
        print(f"La persona {self.__nome} ha {self.__eta} anni")


class Studente(Persona):#Creo la sotttoclasse Studente
    def __init__(self, nome: str, eta: int, voti: list[int]): #Aggiungo l'attributo voti che è una lista di interi
        super().__init__(nome, eta) #Chiamo il costruttore della classe base per nome e eta
        self.__voti = voti #Creo l'attributo voti

    def get_voti(self) -> list[int]:#Metodo get che permette di leggere i voti dall'esterno
        return self.__voti

    def set_voti(self, voti: list[int]):#Metodo set che permette di modificare i voti dall'esterno
        self.__voti = voti

    def calcola_media(self) -> float: #Metodo calcola media
        if not self.__voti:
            return 0
        return sum(self.__voti) / len(self.__voti)

    def presentazione(self):# Override del metodo presentazione
        super().presentazione()
        media = self.calcola_media()
        print(f", è uno studente e ha una media di {media:.2f}.")


class Professore(Persona): #Creo la classe professore
    def __init__(self, nome: str, eta: int, materia: str):#Aggiungo l'attributo materia che è una stringa
        super().__init__(nome, eta)#Chiamo il costruttore della classe base per nome e eta
        self.__materia = materia#Creo l'attributo materia

    def get_materia(self) -> str:#Metodo get che permette di leggere la materia dall'esterno
        return self.__materia

    def set_materia(self, materia: str):#Metodo set che permette di modificare la materia dall'esterno
        self.__materia = materia

    # Override del metodo presentazione
    def presentazione(self):
        super().presentazione()
        print(f", è un Professore e insegna {self.__materia}")
