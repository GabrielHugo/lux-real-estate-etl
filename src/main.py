from excel_reader import ExcelReader

# ExcelReader

df = ExcelReader("../data/raw/vente-appartement-2010-2024.xlsx")

df.extract_and_transform()