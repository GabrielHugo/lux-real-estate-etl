import pyodbc
from dotenv import load_dotenv
from os import getenv
load_dotenv()

class SqlConnector:

    def __init__(self):

        self.DRIVER = r"DRIVER={ODBC Driver 17 for SQL Server};"
        self.SERVER = f"SERVER={getenv('DB_SERVER')};"
        self.DATABASE = f"DATABASE={getenv('DB_NAME')};"
        self.TRUSTED_CONNECTION = r"Trusted_Connection=yes;"
        self.TRUST_SERVER_CERTIFICATE = r"TrustServerCertificate=yes;"

        self.cnxn = pyodbc.connect(self.DRIVER+self.SERVER+self.DATABASE+
                                   self.TRUSTED_CONNECTION+self.TRUST_SERVER_CERTIFICATE)

        self.cursor = self.cnxn.cursor()

    def __enter__(self):

        create_table = """
        IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Excel')
        BEGIN
            CREATE TABLE Excel (
                ID_column INT NOT NULL IDENTITY(1, 1) PRIMARY KEY,
                Commune VARCHAR(50),
                Nombre_offres INT,
                Prix_moyen FLOAT,
                Prix_m2 FLOAT
            )
            END
            """

        self.cursor.execute(create_table)
        self.cnxn.commit()

        insert_table = """"""

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.cnxn.close()

