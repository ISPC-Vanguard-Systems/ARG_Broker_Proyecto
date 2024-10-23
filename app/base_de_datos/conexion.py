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
<<<<<<< Updated upstream
                host=os.getenv("HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME")
=======
                host="localhost",
                user="root",
                password="",
                database="arg_broker",
                port=3306  # Especifica el puerto aquí
>>>>>>> Stashed changes
            )
            if self.conexion.is_connected():
                print("Conexión establecida con éxito")
        except Error as e:
<<<<<<< Updated upstream
            print(f"Error al conectar a la base de datos: {e}")
=======
            print(f"Error al conectar con la base de datos: {e}")
            self.conexion = None

    def iniciar_transaccion(self):
        """Inicia una transacción manualmente."""
        if self.conexion and self.conexion.is_connected():
            try:
                self.conexion.start_transaction()
                self.transaccion_activa = True
            except Error as e:
                print(f"Error al iniciar la transacción: {e}")

    def ejecutar_query(self, query, valores=None, mantener_transaccion=False):
        """Ejecuta una consulta en la base de datos, manejando transacciones."""
        if self.conexion is None:
            print("La conexión a la base de datos no está establecida.")
>>>>>>> Stashed changes
            return False
        return True

    def confirmar(self):
<<<<<<< Updated upstream
        """Confirma la transacción actual."""
        if self.conexion:
            self.conexion.commit()
            print("Transacción confirmada (commit)")

    def revertir(self):
        """Revierte la transacción actual."""
        if self.conexion:
            self.conexion.rollback()
            print("Transacción revertida (rollback)")
=======
        """Confirma los cambios en la base de datos."""
        if self.conexion and self.conexion.is_connected():
            try:
                self.conexion.commit()
                self.transaccion_activa = False
            except Error as e:
                print(f"Error al confirmar la transacción: {e}")
                self.revertir()

    def revertir(self):
        """Revierte los cambios en la base de datos."""
        if self.conexion and self.conexion.is_connected():
            try:
                self.conexion.rollback()
                self.transaccion_activa = False
            except Error as e:
                print(f"Error al revertir la transacción: {e}")
>>>>>>> Stashed changes

    def cerrar(self):
        """Cierra la conexión a la base de datos."""
        if self.conexion.is_connected():
            self.conexion.close()
<<<<<<< Updated upstream
            print("Conexión cerrada")
=======
        elif self.transaccion_activa:
            print("No se cerró la conexión porque hay una transacción en curso.")

    def obtener_cursor(self):
        """Devuelve un cursor para realizar operaciones en la base de datos."""
        if self.conexion and self.conexion.is_connected():
            return self.conexion.cursor(buffered=True)
        else:
            return None
>>>>>>> Stashed changes
