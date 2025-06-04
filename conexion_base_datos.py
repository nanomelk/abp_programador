# conexion_base_datos.py
import mysql.connector
from mysql.connector import errorcode
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, PORT


# Función para crear y devolver la conexión
def crear_conexion():
    try:
        conexion = mysql.connector.connect(
            host=DB_HOST,
            port=PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
        )
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")
            return conexion
    except errorcode as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None


# Función para cerrar la conexión
def cerrar_conexion(conexion):
    if conexion and conexion.is_connected():
        conexion.close()
        print("Conexión cerrada")
