import pandas as pd

# 1. Caricare i dati in un DataFrame
df = pd.read_csv(r"C:\Users\annaf\OneDrive\Desktop\Firinu_DepositoCorso\12. Giovedi 27-11\esercizio2\vendite.csv")

# 2. Aggiungere una colonna "Totale Vendite"
df["Totale Vendite"] = df["Quantità"] * df["Prezzo Unitario"]

# 3. Raggruppare i dati per Prodotto e calcolare il totale delle vendite per ciascun prodotto
totale_vendite_per_prodotto = df.groupby("Prodotto")["Totale Vendite"].sum().reset_index()  #sommo il totale delle vendite per ciascun prodotto che raggruppo
totale_vendite_per_prodotto = totale_vendite_per_prodotto.sort_values(by="Totale Vendite", ascending=False) #Metto le vendite in ordine decrescente
print("Totale vendite per prodotto:")
print(totale_vendite_per_prodotto)

# 4. Trovare il prodotto più venduto in termini di Quantità
prodotto_piu_venduto = df.groupby("Prodotto")["Quantità"].sum().idxmax()
quantita_massima = df.groupby("Prodotto")["Quantità"].sum().max()
print(f"\nProdotto più venduto in termini di quantità: {prodotto_piu_venduto}, pezzi {quantita_massima}")

# 5. Identificare la città con il maggior volume di vendite totali
citta_maggior_volume = df.groupby("Città")["Totale Vendite"].sum().idxmax()
volume_maggiore = df.groupby("Città")["Totale Vendite"].sum().max()
print(f"\nCittà con il maggior volume di vendite totali: {citta_maggior_volume}. volume ({volume_maggiore:.2f} €)")


