from teatro import Teatro, PostoVIP, PostoStandard

def crea_teatro():#Prima di far utilizzare il programma creo un teatro con 40 file da 20 posti ciascuna
    teatro = Teatro()
    numero_posti_per_fila = 20
    numero_file = 40

    for f in range(1, numero_file + 1):
        fila_id = str(f)
        for n in range(1, numero_posti_per_fila + 1):
            if n == 1:
                #Il primo posto di ogni fila sarà VIP e avrà i servizi specifici
                teatro.aggiungi_posto(PostoVIP(n, fila_id, ["Accesso al lounge", "Servizio in posto"]))
            else:
                teatro.aggiungi_posto(PostoStandard(n, fila_id, 50.0))

    return teatro


def menu():
    teatro = crea_teatro()

    while True:
        print("\nMENU TEATRO")
        print("1. Prenota un posto")
        print("2. Libera un posto")
        print("3. Mostra posti occupati")
        print("4. Aggiungi un nuovo posto")
        print("5. Esci")

        scelta = input("Seleziona un'opzione (1-5): ")

        if scelta == '1':
            fila = str(input("Inserisci la fila del posto (1-40): "))
            numero = int(input("Inserisci il numero del posto (1-20): "))
            teatro.prenota_posto(numero, fila)

        elif scelta == '2':
            fila = str(input("Inserisci la fila del posto (1-40): "))
            numero = int(input("Inserisci il numero del posto (1-20): "))
            teatro.libera_posto(numero, fila)

        elif scelta == '3':
            teatro.stampa_posti_occupati()

        elif scelta == '4':
            tipo = input("Tipo di posto (VIP/Standard): ").lower()
            fila = str(input("Inserisci la fila del posto: "))
            numero = int(input("Inserisci il numero del posto: "))
            if tipo == 'vip':
                servizi = input("Inserisci i servizi extra separati da virgola: ").split(',')
                servizi = [s for s in servizi if s]
                teatro.aggiungi_posto(PostoVIP(numero, fila, servizi))
            elif tipo == 'standard':
                costo = float(input("Inserisci il costo del posto: "))
                teatro.aggiungi_posto(PostoStandard(numero, fila, costo))
            else:
                print("Tipo di posto non valido")

        elif scelta == '5':
            print("Arrivederci")
            break

        else:
            print("Opzione non valida")


if __name__ == "__main__":
    menu()
