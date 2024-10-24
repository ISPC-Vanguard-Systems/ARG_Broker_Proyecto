from mysql.connector import Error
from app.base_de_datos.conexion import Conexion
from app.clases.interface_dao import InterfaceDAO
# from app.clases.cuenta import Cuenta


class CuentaDao(InterfaceDAO):
    
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

    def verificar_existencia(self, campo, valor):
        """Verifica si existe un registro según el campo y valor proporcionado"""
        raise NotImplementedError("El método verificar_existencia no está implementado.")

    def obtener_todos(self):
        """Obtiene todos los registros"""
        raise NotImplementedError("El método obtener_todos no está implementado.")

    def obtener_uno(self, id):
        """Encuentra un registro por su ID"""
        raise NotImplementedError("El método obtener_uno no está implementado.")

    def eliminar(self, id):
        """Elimina un registro por su ID"""
        raise NotImplementedError("El método eliminar no está implementado.")

    def actualizar(self, id, data):
        """Actualiza un registro existente"""
        raise NotImplementedError("El método actualizar no está implementado.")

    def insertar(self, data):
        """Inserta un nuevo registro"""
        raise NotImplementedError("El método insertar no está implementado.")
