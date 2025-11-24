file = open(r"C:\Users\annaf\OneDrive\Desktop\Firinu_DepositoCorso\8. Venerdi 21-11\anna.txt", "r") # Apertura in modalità lettura
contenuto = file.read() # Legge l'intero contenuto del file
print("Contenuto completo del file:")
print(contenuto)

file.seek(0)  # Torna all'inizio del file
riga = file.readline() # Legge una singola riga del file
print("\nPrima riga del file:")
print(riga)

file.close()  # Chiudi il file dopo averlo usato

file = open(r"C:\Users\annaf\OneDrive\Desktop\Firinu_DepositoCorso\8. Venerdi 21-11\anna.txt", "r")
contenuto = file.read() # Legge l'intero contenuto del file
riga = file.readline() # Legge una singola riga del file
file.close()  # Chiudi anche questo file



