import traceback
import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv
load_dotenv()

class Conexion:
    def __init__(self):
        self.conexion = None
        self.establecer_conexion()#agrego
    def establecer_conexion(self):
        """Establece la conexión con la base de datos."""
        try:
            self.conexion = mysql.connector.connect(
                host="bxhg7av36sf1uym9jely-mysql.services.clever-cloud.com",
                user="uhxhjceoahgp4u98",
                password="OinmQHRskRHND1iJAJVH",
                database="bxhg7av36sf1uym9jely"
            )
        except Error as e:
            print(f"Error al conectar con la base de datos: {e}")
            self.conexion = None

    def iniciar_transaccion(self):
        """Inicia una transacción manualmente."""
        if self.conexion and self.conexion.is_connected():
            try:
                self.conexion.start_transaction()
                print("Transacción iniciada.")
            except Error as e:
                print(f"Error al iniciar la transacción: {e}")

    def ejecutar_query(self, query, valores=None):
        """Ejecuta una consulta en la base de datos."""
        if self.conexion is None:
            print("La conexión a la base de datos no está establecida.")
            return False

        cursor = self.conexion.cursor(buffered=True)
        try:
            if valores:
                cursor.execute(query, valores)
            else:
                cursor.execute(query)
            
            # Consume los resultados si es una consulta SELECT
            if query.strip().lower().startswith("select"):
                return cursor.fetchall()

            # Para INSERT, UPDATE, DELETE, etc., devuelve el ID de la última fila insertada
            return cursor.lastrowid
        except Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            traceback.print_exc()
            self.revertir()
            return False
        finally:
            cursor.close()

    def verificar_existencia(self, campo, valor):
        """Verifica si el valor existe en la base de datos para el campo especificado."""
        query = f"SELECT 1 FROM inversores WHERE {campo} = %s"
        resultado = self.ejecutar_query(query, (valor,))
        return len(resultado) > 0  # Retorna True si el valor existe

    def confirmar(self):
        """Confirma los cambios en la base de datos."""
        if self.conexion and self.conexion.is_connected():
            try:
                self.conexion.commit()
                print("Transacción confirmada.")
            except Error as e:
                print(f"Error al confirmar la transacción: {e}")
                self.revertir()

    def revertir(self):
        """Revierte los cambios en la base de datos."""
        if self.conexion and self.conexion.is_connected():
            try:
                self.conexion.rollback()
                print("Transacción revertida.")
            except Error as e:
                print(f"Error al revertir la transacción: {e}")

    def cerrar_conexion(self):
        """Cierra la conexión con la base de datos."""
        if self.conexion and self.conexion.is_connected():
            self.conexion.close()
            print("Conexión cerrada.")
        else:
            print("No hay conexión activa para cerrar.")

    def obtener_cursor(self):
        """Devuelve un cursor para realizar operaciones en la base de datos."""
        if self.conexion and self.conexion.is_connected():
            return self.conexion.cursor(buffered=True)
        else:
            print("No se pudo obtener el cursor. No hay conexión activa.")
            return None
