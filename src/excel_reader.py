import pandas as pd


class ExcelReader:

    def __init__(self, file, sheet_name, skiprows = 7, skipfooter = 6):
        self.file = file
        self.sheet_name = sheet_name
        self.skiprows = skiprows
        self.skipfooter = skipfooter

    def read(self):
        df = pd.read_excel(self.file, sheet_name=str(self.sheet_name),
                           skiprows=self.skiprows, skipfooter=self.skipfooter)

        df = df.dropna(how="all")
        df = df.dropna(axis=1, how="all")

        df = df.iloc[1:].reset_index(drop=True)

        df.columns = ["commune", "nombre_offres", "prix_moyen", "prix_m2"]
        return df