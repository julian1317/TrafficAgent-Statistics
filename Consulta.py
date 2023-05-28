import os
from dotenv import load_dotenv
import psycopg2

# Cargar las variables de entorno desde el archivo .env
load_dotenv("secrets.env")

class Consulta:
    def __init__(self):
        self.hostname = os.getenv("DB_HOSTNAME")
        self.port = int(os.getenv("DB_PORT"))
        self.database = os.getenv("DB_DATABASE")
        self.username = os.getenv("DB_USERNAME")
        self.password = os.getenv("DB_PASSWORD")
        
    def ejecutar_consulta(self):
        conn_string = f"host='{self.hostname}' port={self.port} dbname='{self.database}' user='{self.username}' password='{self.password}'"

        conn = psycopg2.connect(conn_string)

        cursor = conn.cursor()

        cursor.execute("SELECT latitud, longitud FROM report_users")

        results = cursor.fetchall()

        cursor.close()
        conn.close()      
        return results

consulta = Consulta()

consulta.ejecutar_consulta()


