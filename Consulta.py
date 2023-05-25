import os
from dotenv import load_dotenv
import psycopg2

# Cargar las variables de entorno desde el archivo .env
load_dotenv("secrets.env")

class Consulta:
    def __init__(self):
        # Establecer los valores de las credenciales desde las variables de entorno
        self.hostname = os.getenv("DB_HOSTNAME")
        self.port = int(os.getenv("DB_PORT"))
        self.database = os.getenv("DB_DATABASE")
        self.username = os.getenv("DB_USERNAME")
        self.password = os.getenv("DB_PASSWORD")
        
    def ejecutar_consulta(self):
        # Establecer la cadena de conexión
        conn_string = f"host='{self.hostname}' port={self.port} dbname='{self.database}' user='{self.username}' password='{self.password}'"

        # Conectar a la base de datos
        conn = psycopg2.connect(conn_string)

        # Crear un cursor para ejecutar consultas
        cursor = conn.cursor()

        # Ejemplo: Ejecutar una consulta SQL
        cursor.execute("SELECT latitud, longitud FROM report_users")

        # Obtener los resultados
        results = cursor.fetchall()

        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()      
        return results

# Crear una instancia de la clase Consulta
consulta = Consulta()

# Ejecutar la consulta
consulta.ejecutar_consulta()


