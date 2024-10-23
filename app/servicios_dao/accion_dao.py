from app.base_de_datos.conexion import Conexion

class AccionesDAO:
    def __init__(self):
        pass

    def listar_acciones_disponibles(self):
        with Conexion() as conexion: # Esto se llama context manager
            query = "SELECT id_accion, simbolo, nombre_empresa, precio_compra, precio_venta FROM acciones"
            acciones = conexion.ejecutar_query(query)
            
            if acciones:
                print("\n--- Acciones Disponibles ---")
                for accion in acciones:
                    print(f"ID: {accion[0]} - Símbolo: {accion[1]} - Empresa: {accion[2]} - Precio Compra: {accion[3]} - Precio Venta: {accion[4]}")
            else:
                print("No hay acciones disponibles.")

    def comprobar_accion(self, id_accion):
        with Conexion() as conexion:
            """Comprueba si la acción existe en la base de datos."""
            query = "SELECT * FROM acciones WHERE id_accion = %s"
            resultado = conexion.ejecutar_query(query, (id_accion,))
            
            # Retorna True si existe al menos una acción con ese id, False en caso contrario
            return resultado if resultado else False

    def obtener_saldo_inversor(self, id_inversor):
        with Conexion() as conexion:
            query = "SELECT saldo FROM cuentas WHERE id_inversor = %s"
            resultado = conexion.ejecutar_query(query, (id_inversor,))
            return resultado[0][0] if resultado else 0.0
    
    def registrar_transaccion(self, id_inversor, id_accion, cantidad, monto_total, comision, tipo_transaccion):
        with Conexion() as conexion:
            query = """
                INSERT INTO transacciones (cantidad_acciones, monto_total, comision, fecha_hora, numero_cuenta, 
                                        id_tipo_transaccion, id_accion)
                VALUES (%s, %s, %s, NOW(), 
                    (SELECT numero_cuenta FROM cuentas WHERE id_inversor = %s), 
                    %s, %s)
            """
            conexion.ejecutar_query(query, (cantidad, monto_total, comision, id_inversor, tipo_transaccion, id_accion))
            conexion.confirmar()

    def actualizar_saldo(self, id_inversor, nuevo_saldo):
        with Conexion() as conexion:
            query = "UPDATE cuentas SET saldo = %s WHERE id_inversor = %s"
            conexion.ejecutar_query(query, (nuevo_saldo, id_inversor))
            conexion.confirmar()

    def asignar_acciones(self, id_inversor, id_accion, cantidad, precio_compra, precio_venta):
        with Conexion() as conexion:
            query = """
                INSERT INTO acciones_por_inversores (id_inversor, id_accion, cantidad_acciones, 
                                                    precio_compra, precio_venta)
                VALUES (%s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE cantidad_acciones = cantidad_acciones + %s
            """
            conexion.ejecutar_query(
                query, (id_inversor, id_accion, cantidad, precio_compra, precio_venta, cantidad)
            )
            conexion.confirmar()

    def listar_acciones_por_inversor(self, id_inversor):
        with Conexion() as conexion:
            query = """
                SELECT a.id_accion, a.nombre_empresa, ap.cantidad_acciones, a.precio_venta
                FROM acciones_por_inversores ap
                JOIN acciones a ON ap.id_accion = a.id_accion
                WHERE ap.id_inversor = %s
            """
            return conexion.ejecutar_query(query, (id_inversor,))

    def comprobar_accion_por_inversor(self, id_inversor, id_accion):
        with Conexion() as conexion:
            query = """
                SELECT a.id_accion, a.nombre_empresa, ap.cantidad_acciones, a.precio_venta
                FROM acciones_por_inversores ap
                JOIN acciones a ON ap.id_accion = a.id_accion
                WHERE ap.id_inversor = %s AND ap.id_accion = %s
            """
            return conexion.ejecutar_query(query, (id_inversor, id_accion))

    def actualizar_cantidad_acciones(self, id_inversor, id_accion, cantidad):
        with Conexion() as conexion:
            query = """
                UPDATE acciones_por_inversores
                SET cantidad_acciones = cantidad_acciones + %s
                WHERE id_inversor = %s AND id_accion = %s
            """
            conexion.ejecutar_query(query, (cantidad, id_inversor, id_accion))
            conexion.confirmar()




