import pandas as pd
import numpy as np

from sql_connector import SqlConnector

class ExcelReader:

    def __init__(self, file, skipfooter = 6):

        self.file = file
        self.skipfooter = skipfooter
        self.df = None

    def get_all_sheet_names(self):

        df = pd.ExcelFile(self.file)

        all_years = df.sheet_names

        all_years = list(map(int, all_years))

        return all_years


    def extract_and_transform(self):

        all_sheet_names = self.get_all_sheet_names()

        list_df = []

        for sheet_name in all_sheet_names:

            if sheet_name < 2021:

                df_temp = pd.read_excel(self.file, sheet_name=str(sheet_name),
                                   skiprows= 10, skipfooter=self.skipfooter)

            else:

                df_temp = pd.read_excel(self.file, sheet_name=str(sheet_name),
                                   skiprows=7, skipfooter=self.skipfooter)

            df_temp = df_temp.replace(to_replace="*", value=np.nan)

            df_temp = df_temp.dropna(how="all")
            df_temp = df_temp.dropna(axis=1, how="all")

            df_temp = df_temp.iloc[1:].reset_index(drop=True)

            df_temp.columns = ["commune", "nombre_offres", "prix_moyen", "prix_m2"]

            df_temp["annee"] = sheet_name

            list_df.append(df_temp)

            print(sheet_name)

        self.df = pd.concat(list_df, ignore_index=True)
        print(f"{len(self.df)}")

    def send_to_sql(self):

        connect = SqlConnector()
        connect.insert_data(self.df)