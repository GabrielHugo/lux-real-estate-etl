import pyodbc
from dotenv import load_dotenv
from os import getenv
load_dotenv()

conn_str = (
    r"DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={getenv('DB_SERVER')};"
    f"DATABASE={getenv('DB_NAME')};"
    r"Trusted_Connection=yes;"
    r"TrustServerCertificate=yes;"
)

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")

for row in cursor:
    print(row)

cursor.close()