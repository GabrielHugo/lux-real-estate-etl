import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

file = "../data/raw/vente-appartement-2010-2024.xlsx"

df = pd.read_excel(file, skiprows=10, na_values=['*'])

df = df.dropna(axis=1, how='all')
df = df.dropna(axis=0, how='all')

df.columns = ['commune', 'nombre_offres', 'prix_moyen', 'prix_m2']

df = df.iloc[1:].reset_index(drop=True)

print(df.head(10))
