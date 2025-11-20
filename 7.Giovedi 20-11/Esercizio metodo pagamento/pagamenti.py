# Classe padre
class MetodoPagamento:
    def effettua_pagamento(self, importo):
        print(f"Pagamento di {importo}€")


# Sottoclassi
class CartaDiCredito(MetodoPagamento):
    def __init__(self, numero_carta):
        self.numero_carta = numero_carta

    def effettua_pagamento(self, importo):
        print(f"Pagamento di {importo}€ con la carta {self.numero_carta}")


class PayPal(MetodoPagamento):
    def __init__(self, email):
        self.email = email

    def effettua_pagamento(self, importo):
        print(f"Pagamento di {importo}€ dall'account PayPal {self.email}")


class BonificoBancario(MetodoPagamento):
    def __init__(self, iban):
        self.iban = iban

    def effettua_pagamento(self, importo):
        print(f"Pagamento di {importo}€ tramite IBAN {self.iban}")


# Funzione generica per duck typing / polimorfismo
def gestisci_pagamento(metodo, importo):
    metodo.effettua_pagamento(importo)
