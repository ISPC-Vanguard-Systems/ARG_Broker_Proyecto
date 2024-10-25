from mysql.connector import Error
from app.base_de_datos.conexion import Conexion
from app.clases.transaccion import Transaccion


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
                SELECT a.simbolo,
                       SUM(t.cantidad_acciones) AS total_acciones,
                       SUM(t.monto_total) AS monto_total,
                       SUM(t.comision) AS total_comision 
                FROM transacciones t 
                INNER JOIN cuentas c ON t.numero_cuenta = c.numero_cuenta 
                INNER JOIN acciones a ON t.id_accion = a.id_accion
                WHERE c.id_cuenta = %s
                GROUP BY a.simbolo
            """
            resultado = conexion.ejecutar_query(query, (id_cuenta,))
            return [Transaccion(simbolo, total_acciones, monto_total, total_comision) for
                simbolo, total_acciones, monto_total, total_comision in resultado] if resultado else []










