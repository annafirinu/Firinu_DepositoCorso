from Esercizio_riassuntivo import gestione_sport

# Decoratore per il messaggio di benvenuto
def banner_benvenuto(funzione):
    def wrapper():
        print("   BENVENUTO NEL PROGRAMMA SPORTIVO   ")
        funzione()
    return wrapper

# Decoratore per il messaggio di saluto finale
def saluto_fine(funzione):
    def wrapper():
        funzione()
        print("\nGrazie per aver utilizzato il programma!")
    return wrapper

# Applico i decoratori direttamente alla funzione importata
gestione_sport_decorata = banner_benvenuto(saluto_fine(gestione_sport))

gestione_sport_decorata() 





