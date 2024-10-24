from mysql.connector import Error
from app.base_de_datos.conexion import Conexion
from app.clases.transaccion import Transaccion
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
                raise
                # return None


    def obtener_transacciones_por_cuenta(self, id_cuenta):
        with Conexion() as conexion:
            query = """
                SELECT t.id_transaccion, t.cantidad_acciones, t.monto_total, t.comision 
               FROM transacciones t 
               INNER JOIN cuentas c ON t.numero_cuenta = c.numero_cuenta 
               WHERE c.id_cuenta = %s
            """
            resultado = conexion.ejecutar_query(query, (id_cuenta,))
            return [Transaccion(id_transaccion, cantidad_acciones, monto_total, comision) for
                id_transaccion, cantidad_acciones, monto_total, comision in resultado] if resultado else []










