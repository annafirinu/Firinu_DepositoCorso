def inserisci_dati():
    while True:#Chiedo i dati all'utente finchè non inserisce i dati correttamente
        dati = input("Inserisci gli importi delle vendite separati da spazi: ").split()#Con split vado a isolare ciascun numero(creo delle sottostringhe)
        vendite = []#Lista in cui andranno inseriti i numeri inseriti dall'utente
        errore = False

        for valore in dati:
            if valore.isdigit():  #Verifico che si tratti di un numero
                vendite.append(int(valore))
            else:
                print(f"'{valore}' non è un numero valido")
                errore = True
                break

        if not errore:
            return vendite
        else:
            print("Reinserisci tutti i dati correttamente\n")

def calcola_totale_media(vendite):
    if len(vendite) == 0:#Controllo se la lista è vuota
        return 0, 0#Se è vuota ritorno 0
    totale = sum(vendite)#Totale delle vendite
    media = totale / len(vendite)#Media
    return totale, media

def vendite_sopra_media(vendite, media):
    sopra_media = [(i+1, v) for i, v in enumerate(vendite) if v > media]#Vado a filtrare solo le vendite sopra la media
    return sopra_media
