from mysql.connector import Error
from app.base_de_datos.conexion import Conexion
from app.clases.cuenta import Cuenta


def obtener_datos_cuenta(id_cuenta):
    try:
        conexion = Conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT numero_cuenta, saldo FROM cuentas WHERE id = %s",
                       (id_cuenta))
        datos = cursor.fetchone()

        return datos
    except Error as e:
        print(f"Error al acceder a la base de datos: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()


def obtener_cuenta(id_cuenta):
    datos = obtener_datos_cuenta(id_cuenta)
    if datos:
        return Cuenta(id_cuenta, *datos)
    return None









