from mysql.connector import Error
# from app.clases.cuenta import Cuenta


class CuentaDao:
    def __init__(self, acceso_bd):
        self.acceso_bd = acceso_bd

    def obtener_datos_cuenta(self, id_cuenta):

        cursor = self.acceso_bd.obtener_cursor()

        if cursor is None:
            return None #no se puede obtener cursos, termina aqui

        try:
            query = "SELECT numero_cuenta, saldo, fecha_creacion FROM cuentas WHERE id_cuenta = %s"
            cursor.execute(query, (id_cuenta,))#usar tupla con una coma
            datos = cursor.fetchone()
            return datos
        except Error as e:
            print(f"Error al acceder a la base de datos: {e}")
            return None
        finally:
            cursor.close()
            self.acceso_bd.cerrar_conexion()










