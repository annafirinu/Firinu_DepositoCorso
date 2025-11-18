from membrosquadra import MembroSquadra
from ruoli import Giocatore, Allenatore, Assistente

squadra = [] #Creo una lista vuota che andrà successivamente a contenere tutti i membri della squadra

while True:
    print("\nMENU SQUADRA") #Creo un menu che permette all'utente di creare giocatori, allenatori e assistenti e di utilizzare i metodi presenti nelle classi
    print("1. Aggiungi Giocatore")
    print("2. Aggiungi Allenatore")
    print("3. Aggiungi Assistente")
    print("4. Mostra squadra")
    print("5. Giocatore: gioca partita")
    print("6. Allenatore: dirige allenamento")
    print("7. Assistente: supporta team")
    print("8. Esci")
    
    scelta = input("Scegli un'opzione: ")
    
    if scelta == "1":
        nome = input("Nome: ")
        eta = int(input("Età: "))
        ruolo = input("Ruolo: ")
        numero = input("Numero maglia: ")
        squadra.append(Giocatore(nome, eta, ruolo, numero))#Riprende il costruttore di giocatore
        
    elif scelta == "2":
        nome = input("Nome: ")
        eta = int(input("Età: "))
        esperienza = int(input("Anni di esperienza: "))
        squadra.append(Allenatore(nome, eta, esperienza))#Riprende il costruttore di allenatore
        
    elif scelta == "3":
        nome = input("Nome: ")
        eta = int(input("Età: "))
        specializzazione = input("Specializzazione: ")
        squadra.append(Assistente(nome, eta, specializzazione))#Riprende il costruttore di assistente
        
    elif scelta == "4":
        if not squadra:
            print("La squadra è vuota.")
        else:
            for membro in squadra:
                membro.descrivi()
                
    elif scelta == "5":
        for membro in squadra:#Eseguo gioca_partita su tutti i giocatori
            if isinstance(membro, Giocatore):
                membro.gioca_partita()
                
    elif scelta == "6":
        for membro in squadra: # Eseguo dirige_allenamento su tutti gli allenatori
            if isinstance(membro, Allenatore):
                membro.dirige_allenamento()
                
    elif scelta == "7":
        for membro in squadra:# Eseguo supporta_team su tutti gli assistenti
            if isinstance(membro, Assistente):
                membro.supporta_team()
                
    elif scelta == "8":
        print("Arrivederci")
        break
        
    else:
        print("Opzione non valida")
