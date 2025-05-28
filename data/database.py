import mysql.connector
import logging
from mysql.connector import errorcode


# Función para crear y devolver la conexión
def crear_conexion():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            port=3307,
            user="root",
            password="1234",
            database="abp_programador",
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
