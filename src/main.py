from excel_reader import ExcelReader

df = ExcelReader("../data/raw/vente-appartement-2010-2024.xlsx",
                 2020, 7, 6)

print(df.read().isna().sum())