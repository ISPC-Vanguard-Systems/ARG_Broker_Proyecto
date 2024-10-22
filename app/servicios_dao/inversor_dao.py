import random
import string
from datetime import date
from app.base_de_datos.conexion import Conexion
from app.clases.inversor import Inversor
from app.clases.interface_dao import InterfaceDAO

class Inversor_DAO(InterfaceDAO):
    def __init__(self):
        """Inicializa el DAO con una conexión a la base de datos."""
        self.conexion_db = Conexion()

    def _generar_numero_cuenta_aleatorio(self):
        """Genera un número de cuenta aleatorio que no se repita en la base de datos."""
        while True:
            # Generar un número de cuenta alfanumérico de 20 caracteres
            numero_cuenta = ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))

            # Verificar si el número ya existe en la base de datos
            query = "SELECT COUNT(*) FROM cuentas WHERE numero_cuenta = %s"
            cursor = self.conexion_db.obtener_cursor()
            if cursor is None:
                return None

            resultado = self.conexion_db.ejecutar_query(query, (numero_cuenta,))
            if resultado is False:
                print("Error al ejecutar la consulta para verificar el número de cuenta.")
                cursor.close()
                return None

            # Obtener el resultado de la consulta
            count = resultado[0][0]
            cursor.close()

            if count == 0:  # Si no existe, retornar el número de cuenta
                return numero_cuenta

    def _verificar_id_inversor(self, id_inversor):
        """Verifica si el id_inversor existe en la tabla inversores."""
        query = "SELECT COUNT(*) FROM inversores WHERE id_inversor = %s"
        resultado = self.conexion_db.ejecutar_query(query, (id_inversor,))

        if resultado is False:
            print("Error al verificar el inversor.")
            return False

        return resultado[0][0] > 0  # Retorna True si existe, False si no

    def verificar_existencia(self, campo, valor):
        """Verifica si existe un registro según el campo y valor proporcionado."""
        return bool(self.conexion_db.verificar_existencia('inversores', campo, valor))

    def obtener_uno(self, email):
        """Obtiene un inversor por email."""
        query = "SELECT * FROM inversores WHERE email = %s"
        resultado = self.conexion_db.ejecutar_query(query, (email,))
        return resultado if resultado else None

    def insertar(self, inversor: Inversor):
        """Registra un nuevo inversor y su cuenta asociada."""
        try:
            # Inicia la transacción
            if not self.conexion_db.obtener_cursor:
                self.conexion_db.iniciar_transaccion()

            # Intentar registrar el inversor
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

            if not self.conexion_db.ejecutar_query(query_inversor, valores_inversor):
                raise Exception("Error al ejecutar la inserción del inversor.")

            print("Inversor creado correctamente.")

            # Generar un número de cuenta único
            numero_cuenta = self._generar_numero_cuenta_aleatorio()

            if numero_cuenta is None:
                raise Exception("Error al generar un número de cuenta único.")

            # Obtener el ID del inversor creado
            id_inversor = self.conexion_db.ejecutar_query("SELECT LAST_INSERT_ID()")
            if id_inversor:
                id_inversor = id_inversor[0][0]
            else:
                raise Exception("No se pudo obtener el ID del inversor creado.")

            if self._verificar_id_inversor(id_inversor):
                query_cuenta = """
                    INSERT INTO cuentas (numero_cuenta, saldo, fecha_creacion, id_inversor) 
                    VALUES (%s, %s, %s, %s)
                """
                valores_cuenta = (numero_cuenta, 1000000.00, date.today(), id_inversor)

                if not self.conexion_db.ejecutar_query(query_cuenta, valores_cuenta):
                    raise Exception("Error al insertar la cuenta.")

                # Confirmar la transacción completa
                self.conexion_db.confirmar()
                print("Cuenta creada exitosamente. Inversor y cuenta registrados.")
            else:
                raise Exception(f"El id_inversor {id_inversor} no existe.")

        except Exception as e:
            # Revertir la transacción en caso de error
            print(f"Error al registrar el inversor y su cuenta: {e}")
            self.conexion_db.revertir()
        
        finally:
            # Cerrar el cursor y la conexión
            self.conexion_db.cerrar_conexion()

    # Métodos no implementados de la interfaz
    def actualizar(self, objeto):
        """Actualizar un registro existente."""
        raise NotImplementedError("El método actualizar no está implementado.")

    def eliminar(self, id_objeto):
        """Eliminar un registro por su ID."""
        raise NotImplementedError("El método eliminar no está implementado.")

    def obtener_todos(self):
        """Obtener todos los registros de inversores."""
        raise NotImplementedError("El método obtener_todos no está implementado.")