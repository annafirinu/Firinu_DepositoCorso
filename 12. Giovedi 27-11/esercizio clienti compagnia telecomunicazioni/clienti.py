import pandas as pd
import numpy as np

# 1. Caricamento e Esplorazione Iniziale
df = pd.read_csv(r"C:\Users\annaf\OneDrive\Desktop\Firinu_DepositoCorso\12. Giovedi 27-11\esercizio clienti compagnia telecomunicazioni\clienticompagnia.csv")

# Estraggo la distribuzione dei dati e identifico colonne con valori mancanti
print("Info:")
print(df.info())

print("\nDescribe:")
print(df.describe())

print("\nvalue_counts:")
print(df['Churn'].value_counts())

print("\nValori mancanti:")
print(df.isnull().sum())

# 2. Pulizia dei dati
# Sostituzione valori mancanti con mediana
df['Età'] = df['Età'].fillna(df['Età'].median())
df['Durata_Abbonamento'] = df['Durata_Abbonamento'].fillna(df['Durata_Abbonamento'].median())
df['Tariffa_Mensile'] = df['Tariffa_Mensile'].fillna(df['Tariffa_Mensile'].median())
df['Dati_Consumati'] = df['Dati_Consumati'].fillna(df['Dati_Consumati'].median())
df['Servizio_Clienti_Contatti'] = df['Servizio_Clienti_Contatti'].fillna(df['Servizio_Clienti_Contatti'].median())


# Correzione anomalie
df = df[df['Età'] > 0]                  # età negative rimosse
df = df[df['Tariffa_Mensile'] >= 0]    # tariffe negative rimosse

print("\nValori mancanti dopo correzione:")
print(df.isnull().sum())

# 3. Analisi Esplorativa dei Dati (EDA)
# Nuova colonna: Costo per GB
df['Costo_per_GB'] = df['Tariffa_Mensile'] / df['Dati_Consumati'].replace(0, np.nan)
df['Costo_per_GB'] = df['Costo_per_GB'].fillna(0)

# Groupby per esplorare relazioni
print("\nETA' MEDIA PER CHURN")
print(df.groupby('Churn')['Età'].mean())

print("\nTARIFFA MEDIA PER CHURN")
print(df.groupby('Churn')['Tariffa_Mensile'].mean())

print("\nDURATA MEDIA ABBONAMENTO PER CHURN")
print(df.groupby('Churn')['Durata_Abbonamento'].mean())

# Conversione Churn in numerico per includerla nelle correlazioni
df['Churn_numerico'] = df['Churn'].map({'No': 0, 'Sì': 1})

# Correlazioni tra colonne numeriche
numerical_cols = ['Età', 'Durata_Abbonamento', 'Tariffa_Mensile', 
                  'Dati_Consumati', 'Servizio_Clienti_Contatti', 'Costo_per_GB', 'Churn_numerico']

print("\nCorrelazioni (solo numeriche):")
print(df[numerical_cols].corr())

# 4. Preparazione dei Dati per la Modellazione
# Normalizzazione colonne numeriche
cols_to_normalize = ['Età', 'Durata_Abbonamento', 'Tariffa_Mensile', 
                     'Dati_Consumati', 'Servizio_Clienti_Contatti', 'Costo_per_GB']

df_normalized = df.copy()
df_normalized[cols_to_normalize] = (df[cols_to_normalize] - df[cols_to_normalize].mean()) / df[cols_to_normalize].std()

print("\nDati normalizzati:")
print(df_normalized.head(99))
