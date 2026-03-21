from excel_reader import ExcelReader

df = ExcelReader("../data/raw/vente-appartement-2010-2024.xlsx")

df.extract_and_transform()

df.send_to_sql()