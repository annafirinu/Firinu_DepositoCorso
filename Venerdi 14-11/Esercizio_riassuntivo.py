'''Voglio creare un programma che chieda all'utente il suo livello in 4 sport comuni. Per ogni sport verrà comunicato
se si tratta di uno sport olimpico o meno. Il sistema comunicherà all'utente il suo livello in ciascuno degli sport 
(esperto, principiante) e alla fine farà un riassunto dei punteggi dell'utente in ciascuno sport'''

def gestione_sport():
    # Tupla con i punteggi minimi per vedere il limite tra principiante e avanzato
    punteggi_minimi = (2, 3, 5, 2)  # calcio, pallavolo, basket, tennis
    #Lista degli sport
    sport_base = ["calcio", "pallavolo", "basket", "tennis"]
    #Insieme degli sport olimpici
    sport_olimpici = {"pallavolo", "basket", "nuoto", "atletica"}

    continua = True
    while continua:
        # Copia della lista per permettere di rimuovere sport già scelti
        sport_disponibili = sport_base.copy()
        punteggi_utente = {}

    
        print("\nValuta il tuo livello in tutti gli sport")

        # Ciclo finché ci sono sport disponibili
        while sport_disponibili:
            print("\nSport disponibili:")
            for s in sport_disponibili:
                print("-", s)

            # L'utente sceglie uno sport
            scelta = input("\nScegli uno sport dalla lista: ").lower()

            # Controllo scelta valida
            if scelta not in sport_disponibili:
                print("Scelta non valida, riprova.")
                continue

            # Trovo l'indice per la tupla dei punteggi minimi
            indice = sport_base.index(scelta)
            punteggio_min = punteggi_minimi[indice]

            # Segnala se lo sport è olimpico
            if scelta in sport_olimpici:
                print("Questo è uno sport olimpico!")
            else:
                print("Questo sport non è olimpico.")

            # Chiedi punteggio in base allo sport
            if scelta == "calcio":
                punteggio = input("Quanti gol hai fatto? ")
                while not punteggio.isdigit():
                    punteggio = input("Valore non valido! Inserisci un numero intero: ")
                punteggio = int(punteggio)

            elif scelta == "pallavolo":
                punteggio = input("Quanti km hai corso? ")
                while not punteggio.replace(".", "", 1).isdigit():
                    punteggio = input("Valore non valido! Inserisci un numero: ")
                punteggio = float(punteggio)

            elif scelta == "basket":
                punteggio = input("Quanti canestri su 10 hai fatto? ")
                while not punteggio.replace(".", "", 1).isdigit():
                    punteggio = input("Valore non valido! Inserisci un numero: ")
                punteggio = float(punteggio)

            elif scelta == "tennis":
                punteggio = input("Quanti ace hai servito? ")
                while not punteggio.isdigit():
                    punteggio = input("Valore non valido! Inserisci un numero intero: ")
                punteggio = int(punteggio)

            # Salva punteggio
            punteggi_utente[scelta] = punteggio

            # esperto/principiante
            if punteggio >= punteggio_min:
                print("Sei esperto in questo sport!")
            else:
                print("Sei principiante in questo sport!")

            # Rimuovi sport già scelto
            sport_disponibili.remove(scelta)

        #Riassunto finale 
        print("\nRIASSUNTO PUNTEGGI")
        for s in sport_base:
            print( s, ":", punteggi_utente[s])

        # Chiedi se ripetere
        risposta = input("\nVuoi inserire nuovamente i punteggi? (si o no): ").lower()
        continua = risposta == "si"

    print("\nFine.")
    


if __name__ == "__main__":
    gestione_sport()           #Se il file viene importato, non verrà eseguito qui
   