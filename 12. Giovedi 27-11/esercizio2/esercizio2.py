import pandas as pd

# 1. Caricare i dati in un DataFrame
df = pd.read_csv(r"C:\Users\annaf\OneDrive\Desktop\Firinu_DepositoCorso\12. Giovedi 27-11\esercizio2\vendite.csv")
print(df)

# 2. Aggiungere una colonna "Totale Vendite"
df["Totale Vendite"] = df["Quantità"] * df["Prezzo Unitario"]
print(df)

# 3. Raggruppare i dati per Prodotto e calcolare il totale delle vendite per ciascun prodotto
totale_vendite_per_prodotto = df.groupby("Prodotto")["Totale Vendite"].sum().reset_index()  #sommo il totale delle vendite per ciascun prodotto che raggruppo
totale_vendite_per_prodotto = totale_vendite_per_prodotto.sort_values(by="Totale Vendite", ascending=False) #Metto le vendite in ordine decrescente
print("Totale vendite per prodotto:")
print(totale_vendite_per_prodotto)

# 4. Trovare il prodotto più venduto in termini di Quantità
prodotto_piu_venduto = df.groupby("Prodotto")["Quantità"].sum()
quantita_massima = df.groupby("Prodotto")["Quantità"].sum().max()
print(f"\nProdotto più venduto in termini di quantità: {prodotto_piu_venduto}, pezzi {quantita_massima}")

# 5. Identificare la città con il maggior volume di vendite totali
citta_maggior_volume = df.groupby("Città")["Totale Vendite"].sum()
volume_maggiore = df.groupby("Città")["Totale Vendite"].sum().max()
print(f"\nCittà con il maggior volume di vendite totali: {citta_maggior_volume}, volume {volume_maggiore:.2f} €")

# 6. Creare un nuovo DataFrame con vendite superiori a 1000 euro
df_vendite_superiori = df[df["Totale Vendite"] > 1000]
print(f"\nVendite superiori a 1000 €:")
print(df_vendite_superiori)

# 7. Ordinare il DataFrame originale per "Totale Vendite" in ordine decrescente
df_ordinato = df.sort_values(by="Totale Vendite", ascending=False)
print(f"\nDataFrame ordinato per Totale Vendite:")
print(df_ordinato.head())

# 8. Visualizzare il numero di vendite per ogni città
vendite_per_citta = df["Città"].value_counts()
print(f"\nNumero di vendite per città:")
print(vendite_per_citta)
