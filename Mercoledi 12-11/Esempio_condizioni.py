#Controllo del flusso

#if viene utilizzata per eseguire un blocco di codice se una determinata condizione è vera
numero=10
if numero > 0:
    print("Il numero è positivo")
    
#else viene usata per definire un blocco di codice da eseguire se le condizioni precedenti risultano false    
#va inserito allo stesso livello di profondità del suo if
numero= -10 
if numero > 0:
    print("Il numero è positivo")
else:
    print("Blocco Else")
   
#con elif si specificano ulteriori condizioni da verificare 
numero=100
if numero > 0:
    print("Il numero è positivo")
    if numero ==100:
        print("wow")
elif numero < 0:
    print("Il numero è negativo")
    
else:
    print("Il numero è 0") #numero =100 output wow
    

#Esercizio 1
nome_corso=input("Inserisci il nome del corso: ")

if nome_corso == "Python":
    print("Nome corso corretto! Procedi con l'inserimento del nome utente.")
    
    nome_utente=input("Inserisci il nome utente: ")
    
    if nome_utente == "annafirinu":
        print("Nome utente corretto! Ora inserisci la password.")
        
        password =input("Inserisci la password: ")
        
        if password == "ciao":
            print("Accesso consentito!")
        else:
            print("Password errata!")
    else:
        print("Nome utente errato")
else:
    print("Nome corso errato")
    
#Esercizio 2
print("Menu:")
print("1. Aggiungi elemento")
print("2. Rimuovi elemento")
print("3. Elimina elemento")

scelta = input("Scegli un'opzione (1-3): ")

if scelta == "1":
    print("Hai aggiunto un elemento")

elif scelta == "2":
        print("Hai rimosso un elemento")

elif scelta == "3":
        print("Hai eliminato un elemento")

else:
    print("Scelta non valida.")
    
#match 
comando= input("Inserisci un comando: " )

match comando:
    case "start":
        print("Avvio del programma.")
    case "stop":
        print("Chiusura del programma")
    case "pausa":
        print("Programma in pausa")
    case _:
        print("Comando non riconusciuto")
    

    


    
