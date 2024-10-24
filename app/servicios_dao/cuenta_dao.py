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
                SELECT c.numero_cuenta, c.saldo, c.fecha_creacion,
                COALESCE(SUM(t.monto_total), 0) AS total_monto,
                COALESCE(SUM(t.comision), 0) AS total_comision
                FROM cuentas c
                LEFT JOIN transacciones t ON c.numero_cuenta = t.numero_cuenta
                WHERE c.id_cuenta = %s
                GROUP BY c.numero_cuenta, c.saldo, c.fecha_creacion
                """
                resultado = conexion.ejecutar_query(query, (id_cuenta,))
                return resultado[0] if resultado else None

            except Error as e:
                print(f"Error al acceder a la base de datos: {e}")
                raise
                # return None










