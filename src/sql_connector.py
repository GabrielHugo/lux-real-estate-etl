import pyodbc
from dotenv import load_dotenv
from os import getenv
load_dotenv()

class SqlConnector:

    DRIVER = r"DRIVER={ODBC Driver 17 for SQL Server};"
    SERVER = f"SERVER={getenv('DB_SERVER')};"
    DATABASE = f"DATABASE={getenv('DB_NAME')};"
    TRUSTED_CONNECTION = r"Trusted_Connection=yes;"
    TRUST_SERVER_CERTIFICATE = r"TrustServerCertificate=yes;"

    def __init__(self):

        self.cnxn = pyodbc.connect(self.DRIVER+self.SERVER+self.DATABASE+
                                   self.TRUSTED_CONNECTION+self.TRUST_SERVER_CERTIFICATE)

        self.cursor = self.cnxn.cursor()

    def __enter__(self):
        requete = """
                  CREATE TABLE Excel
                  (
                  P_ID int,
                  Commune VARCHAR(50),
                  Nombre_offres INT,
                  Prix_moyen INT,
                  Prix_m2 INT)
                  """

        if not requete:
            self.cnxn.commit()
            self.cursor.execute(requete)
            print("Table created")
        else:
            print("Table existing")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__")
        self.cursor.close()
        self.cnxn.close()