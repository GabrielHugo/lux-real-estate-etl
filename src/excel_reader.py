import pandas as pd
import numpy as np

class ExcelReader:

    def __init__(self, file, sheet_name = 2020, skiprows = 7, skipfooter = 6):

        self.file = file
        self.sheet_name = sheet_name
        self.skiprows = skiprows
        self.skipfooter = skipfooter

    def get_all_sheet_names(self):

        df = pd.ExcelFile(self.file)

        all_years = df.sheet_names

        all_years = list(map(int, all_years))

        return all_years


    def extract_and_transform(self):

        all_sheet_names = ExcelReader(self.file)

        years = all_sheet_names.get_all_sheet_names()

        for year in years:

            if year < 2021:

                df = pd.read_excel(self.file, sheet_name=str(year),
                                   skiprows= 10, skipfooter=self.skipfooter)

                df = df.replace(to_replace="*", value=np.nan)

                df = df.dropna(how="all")
                df = df.dropna(axis=1, how="all")

                df = df.iloc[1:].reset_index(drop=True)

                df.columns = ["commune", "nombre_offres", "prix_moyen", "prix_m2"]

            else:

                df = pd.read_excel(self.file, sheet_name=str(year),
                                   skiprows=7, skipfooter=self.skipfooter)

                df = df.replace(to_replace="*", value=np.nan)

                df = df.dropna(how="all")
                df = df.dropna(axis=1, how="all")

                df = df.iloc[1:].reset_index(drop=True)

                df.columns = ["commune", "nombre_offres", "prix_moyen", "prix_m2"]



            print(df, year)