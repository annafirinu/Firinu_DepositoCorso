from eserciziodue import *

def chiedi_si_no(testo): #Creo una funzione che posso riutilizzare nel menu tutte le volte che l'utente deve scegliere se svolgere o meno l'operazione
    while True:
        risposta = input(testo + " (si/no): ").lower()
        if risposta in ["si", "no"]:
            return risposta
        print("Risposta non valida. Scrivi 'si' o 'no'")

def main():
    print("PROGRAMMA DI GENERAZIONE E ANALISI DATI")

    while True:
        
        # 1) Vuoi generare dati?
        genera = chiedi_si_no("Vuoi generare dati?")
        if genera == "no":
            print("Uscita dal programma")
            break

        # 2) Scelta del tipo di dati
        print("\nChe tipo di dati vuoi generare?")
        print("1. Linspace")
        print("2. Numeri casuali")
        print("3. Entrambi")

        scelta = input("Seleziona 1, 2 o 3: ")

        a = b = None

        if scelta == "1":
            a = genera_linspace()
            b = genera_linspace()

        elif scelta == "2":
            a = genera_random()
            b = genera_random()

        elif scelta == "3":
            a = genera_linspace()
            b = genera_random()

        else:
            print("Scelta non valida, riprova")
            continue

        # 3) Operazioni richieste dall'esercizio
        nuovo = somma_array(a, b)
        totale = somma_totale(nuovo)
        somma_5 = somma_maggiori_di_5(nuovo)

        # 4) Stampa
        output = prepara_output(a, b, nuovo, totale, somma_5)
        print(output)

        
        # 5) Salvataggio su file esercizio.txt
        sovrascrivi = chiedi_si_no("Vuoi sovrascrivere il file esercizio.txt?")
        salva_su_file(output, sovrascrivi == "si")
        
        # 6) Vuoi leggere il contenuto del file?
        leggi = chiedi_si_no("Vuoi leggere il contenuto del file esercizio.txt?")
        if leggi == "si":
          leggi_file()

        # 7) Ripetere il processo?
        ripeti = chiedi_si_no("Vuoi ripetere il processo?")
        if ripeti == "no":
            print("Programma terminato")
            break


if __name__ == "__main__":
    main()
