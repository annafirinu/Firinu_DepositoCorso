import pandas as pd 
import numpy as np 

df = pd.read_csv(r'C:\Users\annaf\OneDrive\Desktop\Firinu_DepositoCorso\12. Giovedi 27-11\cartella pandas\vendite.csv') 

# Creazione della tabella pivot
pivot_df = df.pivot_table(values='Quantità', index='Prodotto', columns='Città', aggfunc='mean')

print(pivot_df)

# Utilizzo di groupby per aggregare i dati
grouped_df = df.groupby('Prodotto').sum()

print(grouped_df)


