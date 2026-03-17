import pandas as pd
import numpy as np

from sql_connector import SqlConnector

class ExcelReader:

    def __init__(self, file, skipfooter = 6):

        self.file = file
        self.skipfooter = skipfooter
        self.df = file

    def get_all_sheet_names(self):

        df = pd.ExcelFile(self.file)

        all_years = df.sheet_names

        all_years = list(map(int, all_years))

        return all_years


    def extract_and_transform(self):

        all_sheet_names = self.get_all_sheet_names()

        for sheet_name in all_sheet_names:

            if sheet_name < 2021:

                self.df = pd.read_excel(self.file, sheet_name=str(sheet_name),
                                   skiprows= 10, skipfooter=self.skipfooter)

            else:

                self.df = pd.read_excel(self.file, sheet_name=str(sheet_name),
                                   skiprows=7, skipfooter=self.skipfooter)

            self.df = self.df.replace(to_replace="*", value=np.nan)

            self.df = self.df.dropna(how="all")
            self.df = self.df.dropna(axis=1, how="all")

            self.df = self.df.iloc[1:].reset_index(drop=True)

            self.df.columns = ["commune", "nombre_offres", "prix_moyen", "prix_m2"]

            print(self.df, sheet_name)

    def send_to_sql(self):

        extract_and_transform = self.extract_and_transform()

        for index, row in self.df.iterrows():
            print(row)

        connector = SqlConnector().__enter__("test", 50, 5656.5, 646.5)


        print(connector)