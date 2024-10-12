from mysql.connector import Error
from app.base_de_datos.conexion import Conexion
from app.clases.usuario import Usuario

def obtener_datos():
    conexion_obj = Conexion()
    if conexion_obj.conectar():
        try:
            cursor = conexion_obj.conexion.cursor(dictionary=True)
            cursor.execute("SELECT id, nombre, edad FROM usuarios")
            resultados = cursor.fetchall()
            usuarios = [Usuario(**dato) for dato in resultados]  # Creamos instancias de Usuario
            return usuarios
        except Error as e:
            print(f"Error al obtener los datos: {e}")
            return []
        finally:
            conexion_obj.cerrar()

def insertar_dato(nombre, edad):
    conexion_obj = Conexion()
    if conexion_obj.conectar():
        try:
            cursor = conexion_obj.conexion.cursor()
            query = "INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)"
            cursor.execute(query, (nombre, edad))
            conexion_obj.confirmar()
            return True
        except Error as e:
            print(f"Error al insertar los datos: {e}")
            conexion_obj.revertir()
            return False
        finally:
            conexion_obj.cerrar()

def actualizar_dato(id, nuevo_nombre, nueva_edad):
    conexion_obj = Conexion()
    if conexion_obj.conectar():
        try:
            cursor = conexion_obj.conexion.cursor()
            query = "UPDATE usuarios SET nombre = %s, edad = %s WHERE id = %s"
            cursor.execute(query, (nuevo_nombre, nueva_edad, id))
            conexion_obj.confirmar()
            return True
        except Error as e:
            print(f"Error al actualizar los datos: {e}")
            conexion_obj.revertir()
            return False
        finally:
            conexion_obj.cerrar()

def eliminar_dato(id):
    conexion_obj = Conexion()
    if conexion_obj.conectar():
        try:
            cursor = conexion_obj.conexion.cursor()
            query = "DELETE FROM usuarios WHERE id = %s"
            cursor.execute(query, (id,))
            conexion_obj.confirmar()
            return True
        except Error as e:
            print(f"Error al eliminar los datos: {e}")
            conexion_obj.revertir()
            return False
        finally:
            conexion_obj.cerrar()