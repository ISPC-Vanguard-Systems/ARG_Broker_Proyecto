import random
import string
from datetime import date
from app.base_de_datos.conexion import Conexion
from app.clases.inversor import Inversor
from app.clases.interface_dao import InterfaceDAO

class Inversor_DAO(InterfaceDAO):

    def _generar_numero_cuenta_aleatorio(self):
        """Genera un número de cuenta aleatorio que no se repita en la base de datos."""
        while True:
            numero_cuenta = ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))
            query = "SELECT COUNT(*) FROM cuentas WHERE numero_cuenta = %s"
            
            with Conexion() as conexion_db:
                resultado = conexion_db.ejecutar_query(query, (numero_cuenta,))
                if resultado is False:
                    return None
                
                count = resultado[0][0]
                if count == 0:
                    return numero_cuenta

    def verificar_existencia(self, campo, valor):
        """Verifica si el campo existe en la tabla inversores."""
        query = f"SELECT * FROM inversores WHERE {campo} = %s"
        
        with Conexion() as conexion_db:
            resultado = conexion_db.ejecutar_query(query, (valor,))
            if len(resultado) < 1:
                return False
            print(resultado)
            return resultado[0][0] > 0

    def insertar(self, inversor: Inversor):
        """Registra un nuevo inversor y su cuenta asociada."""
        try:
            with Conexion() as conexion_db:
                query_inversor = """
                    INSERT INTO inversores (documento, email, telefono, razon_social, hashed_password, 
                                            id_perfil_inversor, id_tipo_documento, id_tipo_inversor)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """
                valores_inversor = (
                    inversor.documento, inversor.email, inversor.telefono, 
                    inversor.razon_social, inversor.contrasena, 
                    inversor.id_perfil_inversor, inversor.id_tipo_documento, inversor.id_tipo_inversor
                )
                if not conexion_db.ejecutar_query(query_inversor, valores_inversor):
                    raise Exception("Error al ejecutar la inserción del inversor.")
                
                print("Inversor creado correctamente.")
                
                numero_cuenta = self._generar_numero_cuenta_aleatorio()
                if numero_cuenta is None:
                    raise Exception("Error al generar un número de cuenta único.")

                id_inversor = conexion_db.ejecutar_query("SELECT LAST_INSERT_ID()")
                if id_inversor:
                    id_inversor = id_inversor[0][0]
                else:
                    raise Exception("No se pudo obtener el ID del inversor creado.")

                if self.verificar_existencia('id_inversor', id_inversor):
                    query_cuenta = """
                        INSERT INTO cuentas (numero_cuenta, saldo, fecha_creacion, id_inversor) 
                        VALUES (%s, %s, %s, %s)
                    """
                    valores_cuenta = (numero_cuenta, 1000000.00, date.today(), id_inversor)
                    if not conexion_db.ejecutar_query(query_cuenta, valores_cuenta):
                        raise Exception("Error al insertar la cuenta.")

                    print("Cuenta creada exitosamente. Inversor y cuenta registrados.")
                else:
                    raise Exception(f"El id_inversor {id_inversor} no existe.")
        
        except Exception as e:
            print(f"Error al registrar el inversor y su cuenta: {e}")
    
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