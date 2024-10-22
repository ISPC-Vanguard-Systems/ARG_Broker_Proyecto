from app.base_de_datos.conexion import Conexion

class AccionesDAO:
    def __init__(self):
        self.conexion = Conexion()

    def __del__(self):
        self.conexion.cerrar_conexion()

    def listar_acciones_disponibles(self):
        query = "SELECT id_accion, simbolo, nombre_empresa, precio_compra, precio_venta FROM acciones"
        acciones = self.conexion.ejecutar_query(query)
        
        if acciones:
            print("\n--- Acciones Disponibles ---")
            for accion in acciones:
                print(f"ID: {accion[0]} - Símbolo: {accion[1]} - Empresa: {accion[2]} - Precio Compra: {accion[3]} - Precio Venta: {accion[4]}")
        else:
            print("No hay acciones disponibles.")

    def comprobar_accion(self, id_accion):
        """Comprueba si la acción existe en la base de datos."""
        query = "SELECT * FROM acciones WHERE id_accion = %s"
        resultado = self.conexion.ejecutar_query(query, (id_accion,))
        
        # Retorna True si existe al menos una acción con ese id, False en caso contrario
        return resultado if resultado else False

    def obtener_saldo_inversor(self, id_inversor):
        query = "SELECT saldo FROM cuentas WHERE id_inversor = %s"
        resultado = self.conexion.ejecutar_query(query, (id_inversor,))
        return resultado[0][0] if resultado else 0.0
    
    def registrar_transaccion(self, id_inversor, id_accion, cantidad, monto_total, comision, tipo_transaccion):
        query = """
            INSERT INTO transacciones (cantidad_acciones, monto_total, comision, fecha_hora, numero_cuenta, 
                                    id_tipo_transaccion, id_accion)
            VALUES (%s, %s, %s, NOW(), 
                (SELECT numero_cuenta FROM cuentas WHERE id_inversor = %s), 
                %s, %s)
        """
        self.conexion.ejecutar_query(query, (cantidad, monto_total, comision, id_inversor, tipo_transaccion, id_accion))
        self.conexion.confirmar()

    def actualizar_saldo(self, id_inversor, nuevo_saldo):
        query = "UPDATE cuentas SET saldo = %s WHERE id_inversor = %s"
        self.conexion.ejecutar_query(query, (nuevo_saldo, id_inversor))
        self.conexion.confirmar()

    def asignar_acciones(self, id_inversor, id_accion, cantidad, precio_compra, precio_venta):
        query = """
            INSERT INTO acciones_por_inversores (id_inversor, id_accion, cantidad_acciones, 
                                                precio_compra, precio_venta)
            VALUES (%s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE cantidad_acciones = cantidad_acciones + %s
        """
        self.conexion.ejecutar_query(
            query, (id_inversor, id_accion, cantidad, precio_compra, precio_venta, cantidad)
        )
        self.conexion.confirmar()





