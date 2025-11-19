class ContoBancario: #Creo la classe conto bancario
    def __init__(self, titolare, saldo_iniziale=0.0):#Costruttore con parametri, se non passo nessun saldo sarà di default 0
        self.__titolare = None #Creo l'attributo privato titolare
        self.set_titolare(titolare)  #Chiamo il setter del titolare in modo tale da applicare la validazione prima di assegnarli un valore
        self.__saldo = saldo_iniziale  #Cro l'attributo privato saldo

    
    def get_titolare(self):#Metodo che permette di leggere il valore del titolare fuori dalla classe
        return self.__titolare

    def set_titolare(self, nome):#Metodo che permette di modificare il nome del titolare, ma a patto che sia una stringa e che il nome non sia vuoto
        if isinstance(nome, str) and nome:
            self.__titolare = nome
        else:
            raise ValueError("Il titolare deve essere una stringa non vuota")

    def deposita(self, importo):#Creo il metodo deposita
        if importo > 0:
            self.__saldo += importo
            return True
        return False

    def preleva(self, importo):#Creo il metodo preleva
        if importo > 0 and importo <= self.__saldo:
            self.__saldo -= importo
            return True
        return False

    def visualizza_saldo(self):#Creo il metodo visualizza saldo
        return self.__saldo
