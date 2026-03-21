import pandas as pd
import pyodbc
from dotenv import load_dotenv
from os import getenv
load_dotenv()

from sqlalchemy import create_engine

class SqlConnector:

    def __init__(self):

        serveur = getenv("DB_SERVER")
        bdd = getenv("DB_NAME")

        connection = (f"mssql+pyodbc://@{serveur}/{bdd}"
                      f"?driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes")

        self.engine = create_engine(connection)

    def insert_data(self, df, table_name="Excel"):
        df.to_sql(name=table_name, con=self.engine, if_exists="append", index=False)
        print("Success")

