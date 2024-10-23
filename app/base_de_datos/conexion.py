import traceback
import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv
load_dotenv()

class Conexion:
    def __init__(self):
        self.conexion = None
        self.transaccion_activa = False
        self.establecer_conexion()#agrego

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.cerrar_conexion()

    def establecer_conexion(self):
        """Establece la conexión con la base de datos."""
        try:
            # self.conexion = mysql.connector.connect(
            #     host="bxhg7av36sf1uym9jely-mysql.services.clever-cloud.com",
            #     user="uhxhjceoahgp4u98",
            #     password="OinmQHRskRHND1iJAJVH",
            #     database="bxhg7av36sf1uym9jely"
            # )
            self.conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="admin",
                database="arg_broker",
                port=3307  # Especifica el puerto aquí
            )
        except Error as e:
            print(f"Error al conectar con la base de datos: {e}")
            self.conexion = None

    def iniciar_transaccion(self):
        """Inicia una transacción manualmente."""
        if self.conexion and self.conexion.is_connected():
            try:
                self.conexion.start_transaction()
                self.transaccion_activa = True
                print("Transacción iniciada.")
            except Error as e:
                print(f"Error al iniciar la transacción: {e}")

    def ejecutar_query(self, query, valores=None, mantener_transaccion=False):
        """Ejecuta una consulta en la base de datos, manejando transacciones."""
        if self.conexion is None:
            print("La conexión a la base de datos no está establecida.")
            return False

        cursor = self.conexion.cursor()
        try:
            if valores:
                cursor.execute(query, valores)
            else:
                cursor.execute(query)
            
            # Si es un SELECT, devuelve los resultados
            if query.strip().lower().startswith("select"):
                return cursor.fetchall()

            # Devuelve el ID de la última fila insertada para INSERT, UPDATE, DELETE
            return cursor.lastrowid

        except Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            traceback.print_exc()
            self.revertir()  # Hace rollback si ocurre un error
            return False

        finally:
            cursor.close()
            # Si no se debe mantener la transacción, confirma o revierte según corresponda
            if not mantener_transaccion:
                if self.transaccion_activa:
                    try:
                        self.confirmar()
                    except Exception as e:
                        self.revertir()


    def verificar_existencia(self, tabla, campo, valor):
        """Verifica si existe un registro en la tabla según el campo y valor proporcionados."""
        query = f"SELECT COUNT(*) FROM {tabla} WHERE {campo} = %s"

        resultado = self.ejecutar_query(query, (valor,))
        return resultado[0][0] > 0 if resultado else False

    def confirmar(self):
        """Confirma los cambios en la base de datos."""
        if self.conexion and self.conexion.is_connected():
            try:
                self.conexion.commit()
                self.transaccion_activa = False
                print("Transacción confirmada.")
            except Error as e:
                print(f"Error al confirmar la transacción: {e}")
                self.revertir()

    def revertir(self):
        """Revierte los cambios en la base de datos."""
        if self.conexion and self.conexion.is_connected():
            try:
                self.conexion.rollback()
                self.transaccion_activa = False
                print("Transacción revertida.")
            except Error as e:
                print(f"Error al revertir la transacción: {e}")


    def cerrar_conexion(self):
        """Cierra la conexión solo si no hay una transacción en curso."""
        if not self.transaccion_activa and self.conexion and self.conexion.is_connected():
            self.conexion.close()
            print("Conexión cerrada porque no hay transacción activa.")
        elif self.transaccion_activa:
            print("No se cerró la conexión porque hay una transacción en curso.")

    def obtener_cursor(self):
        """Devuelve un cursor para realizar operaciones en la base de datos."""
        if self.conexion and self.conexion.is_connected():
            return self.conexion.cursor(buffered=True)
        else:
            print("No se pudo obtener el cursor. No hay conexión activa.")
            return None
