import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv
load_dotenv()

class Conexion:
    def __init__(self):
        self.conexion = None

    def conectar(self):
        """Establece una conexión con la base de datos."""
        try:
            self.conexion = mysql.connector.connect(
                host=os.getenv("http://bxhg7av36sf1uym9jely-mysql.services.clever-cloud.com"),
                user=os.getenv("uhxhjceoahgp4u98"),
                password=os.getenv("OinmQHRskRHND1iJAJVH"),
                database=os.getenv("bxhg7av36sf1uym9jely")
            )
            if self.conexion.is_connected():
                print("Conexión establecida con éxito")
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return False
        return True

    def confirmar(self):
        """Confirma la transacción actual."""
        if self.conexion:
            self.conexion.commit()
            print("Transacción confirmada (commit)")

    def revertir(self):
        """Revierte la transacción actual."""
        if self.conexion:
            self.conexion.rollback()
            print("Transacción revertida (rollback)")

    def cerrar(self):
        """Cierra la conexión a la base de datos."""
        if self.conexion.is_connected():
            self.conexion.close()
            print("Conexión cerrada")
