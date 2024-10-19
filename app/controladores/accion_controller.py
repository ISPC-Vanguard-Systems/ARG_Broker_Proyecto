from app.base_de_datos.conexion import Conexion

class AccionesDAO:
    def __init__(self):
        self.conexion = Conexion()
        self.conexion.establecer_conexion()

    def listar_acciones_disponibles(self):
        """Lista las acciones disponibles en la base de datos."""
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

    def asignar_acciones(self, id_inversor, id_accion, cantidad, precio_compra, precio_venta):
        """Asigna o actualiza la cantidad de acciones para un inversor."""
        query = """
            SELECT cantidad_acciones FROM acciones_por_inversores 
            WHERE id_inversor = %s AND id_accion = %s
        """
        resultado = self.conexion.ejecutar_query(query, (id_inversor, id_accion))

        if resultado:
            # Actualiza la cantidad de acciones y los precios si ya existen
            query_update = """
                UPDATE acciones_por_inversores 
                SET cantidad_acciones = cantidad_acciones + %s, 
                    precio_compra = %s, 
                    precio_venta = %s
                WHERE id_inversor = %s AND id_accion = %s
            """
            self.conexion.ejecutar_query(query_update, (cantidad, precio_compra, precio_venta, id_inversor, id_accion))
            print(f"Se añadieron {cantidad} acciones adicionales con precio de compra {precio_compra}.")
        else:
            # Inserta una nueva entrada si no tiene acciones previas
            query_insert = """
                INSERT INTO acciones_por_inversores (id_inversor, id_accion, cantidad_acciones, precio_compra, precio_venta) 
                VALUES (%s, %s, %s, %s, %s)
            """
            self.conexion.ejecutar_query(query_insert, (id_inversor, id_accion, cantidad, precio_compra, precio_venta))
            print(f"Se asignaron {cantidad} acciones con precio de compra {precio_compra}.")

        self.conexion.confirmar()
