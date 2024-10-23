from mysql.connector import Error
from app.base_de_datos.conexion import Conexion
# from app.clases.cuenta import Cuenta


class CuentaDao:
    def __init__(self):
        pass

    def obtener_datos_cuenta(self, id_cuenta):
        with Conexion() as conexion:
            try:
                query = """
                    SELECT numero_cuenta, saldo, fecha_creacion 
                    FROM cuentas 
                    WHERE id_inversor = %s
                """
                resultado = conexion.ejecutar_query(query, (id_cuenta,))
                return resultado[0] if resultado else None
                
            except Error as e:
                print(f"Error al acceder a la base de datos: {e}")
                return None










