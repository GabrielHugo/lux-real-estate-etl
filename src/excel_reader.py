import pandas as pd
import numpy as np

from sql_connector import SqlConnector

class ExcelReader:

    def __init__(self, file, skipfooter = 6):

        self.file = file
        self.skipfooter = skipfooter

    def get_all_sheet_names(self):

        df = pd.ExcelFile(self.file)

        all_years = df.sheet_names

        all_years = list(map(int, all_years))

        return all_years


    def extract_and_transform(self):

        all_sheet_names = self.get_all_sheet_names()

        for sheet_name in all_sheet_names:

            if sheet_name < 2021:

                df = pd.read_excel(self.file, sheet_name=str(sheet_name),
                                   skiprows= 10, skipfooter=self.skipfooter)

            else:

                df = pd.read_excel(self.file, sheet_name=str(sheet_name),
                                   skiprows=7, skipfooter=self.skipfooter)

            df = df.replace(to_replace="*", value=np.nan)

            df = df.dropna(how="all")
            df = df.dropna(axis=1, how="all")

            df = df.iloc[1:].reset_index(drop=True)

            df.columns = ["commune", "nombre_offres", "prix_moyen", "prix_m2"]

            return df, sheet_name

    def send_to_sql(self):

        connector = SqlConnector()

        with connector as d:
            print(d)