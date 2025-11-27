import pandas as pd 
import numpy as np 

#Ho utilizzato il file train.csv da Titanic – Machine Learning from Disaster

# 1️. Caricare i dati da un file CSV
df = pd.read_csv('train.csv') 

#Seleziono solo le colonne Age, Cabin e Embarked
df = df[['Age', 'Cabin', 'Embarked']]

#2. Visualizzare le prime e le ultime 5 righe
print("Prime 5 righe:")
print(df.head())
print("\nUltime 5 righe:")
print(df.tail())

#3.Visualizzare i tipi di dati
print("\nTipi di dati delle colonne:")
print(df.dtypes)

#4. Statistiche descrittive della colonna numerica Age
print("\nStatistiche descrittive per Age:")
print(df['Age'].describe())
print("Mediana di Age:", df['Age'].median())#non uso soltanto describe perchè la mediana mi servirà successivamente e con describe non ottengo un oggetto assegnabile

#5. Rimuovere eventuali duplicati
print(f"\nNumero di duplicati prima della rimozione: {df.duplicated().sum()}")
df = df.drop_duplicates()
print(f"Numero di duplicati dopo la rimozione: {df.duplicated().sum()}")

#6. Sostituire i valori mancanti con la mediana della colonna
df['Age'].fillna(df['Age'].median(), inplace=True)

#7. Creazione della nuova colonna 'Categoria Età'
def categoria_eta(eta):
    if eta <= 18:
        return 'Giovane'
    elif eta <= 65:
        return 'Adulto'
    else:
        return 'Senior'

df['Categoria Età'] = df['Age'].apply(categoria_eta)

#8. Salvare il DataFrame pulito in un nuovo CSV
df.to_csv('train_nuovo.csv', index=False)
print("\nDataFrame nuovo salvato sul csv'")
