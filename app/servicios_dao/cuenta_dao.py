from mysql.connector import Error
from app.base_de_datos.conexion import Conexion
from app.clases.cuenta import Cuenta


class CuentaDao:

    def obtener_datos_cuenta(self, id_cuenta):

        conexion = Conexion()
        cursor = conexion.obtener_cursor()

        if cursor is None:
            return None #no se puede obtener cursos, termina aqui

        try:
            query = "SELECT numero_cuenta, saldo FROM cuentas WHERE id_cuenta = %s"
            cursor.execute(query, (id_cuenta,))#usar tupla con una coma
            datos = cursor.fetchone()
            return datos
        except Error as e:
            print(f"Error al acceder a la base de datos: {e}")
            return None
        finally:
            cursor.close()
            conexion.cerrar_conexion()


    def obtener_cuenta(self, id_cuenta):
        datos = self.obtener_datos_cuenta(id_cuenta)
        if datos:
            return Cuenta(id_cuenta, *datos)
        return None








