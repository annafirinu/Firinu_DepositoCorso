import numpy as np
import pandas as pd

# Creo un intervallo di date di un mese
date_range = pd.date_range(start="2024-01-01", end="2024-01-31", freq="D")

# Imposto le città e i prodotti
citta = ["Roma", "Milano", "Cagliari"]
prodotti = ["PC", "Smartphone", "Tablet"]

# Numero di righe (una per ogni giorno)
numero_righe_d = len(date_range)

# Genero i dati casuali
data = {
    "Data": np.repeat(date_range, 1),
    "Città": np.random.choice(citta, size=numero_righe_d),
    "Prodotto": np.random.choice(prodotti, size=numero_righe_d),
    "Vendite": np.random.randint(100, 1000, size=numero_righe_d)
}

# Creo un DataFrame e lo salvo su CSV
df_csv = pd.DataFrame(data)

# Salvo il CSV
df_csv.to_csv("es_uno.csv", index=False)
print("CSV creato con successo")

#Prendo il dataframe dal csv e lo salvo
df = pd.read_csv("es_uno.csv")
print("\nDataframe caricato dal CSV:")
print(df.head(31))

#Creo la tabella pivot
pivot = df.pivot_table(
    values="Vendite",
    index="Città",
    columns="Prodotto",
    aggfunc="mean"
)

print("\nTabella Pivot:")
print(pivot)


#Calcolo le vendite totali
vendite_totali = df.groupby("Prodotto")["Vendite"].sum()

print("\nVendite totali per prodotto:")
print(vendite_totali)


print("\nFine, programma terminato")
