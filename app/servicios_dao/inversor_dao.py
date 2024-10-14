import random
import string
from datetime import date
from app.base_de_datos.conexion import Conexion
from app.clases.inversor import Inversor

def generar_numero_cuenta_aleatorio(conexion_db):
    """Genera un número de cuenta aleatorio que no se repita."""
    while True:
        # Generar un número de cuenta alfanumérico de 20 caracteres
        numero_cuenta = ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))

        # Verificar si el número ya existe en la base de datos
        query = "SELECT COUNT(*) FROM cuentas WHERE numero_cuenta = %s"
        
        # Obtener el cursor
        cursor = conexion_db.obtener_cursor()
        if cursor is None:
            print("Error al obtener el cursor.")
            return None  # O maneja el error según lo necesites
        
        resultado = conexion_db.ejecutar_query(query, (numero_cuenta,))

        if resultado is False:
            print("Error al ejecutar la consulta para verificar el número de cuenta.")
            cursor.close()  # Asegúrate de cerrar el cursor en caso de error
            return None

        # Obtener el resultado de la consulta
        count = resultado[0][0]

        cursor.close()  # Cerrar el cursor después de usarlo
        
        if count == 0:  # Si no existe, retornarlo
            return numero_cuenta
        
def verificar_id_inversor(conexion_db, id_inversor):
    """Verifica si el id_inversor existe en la tabla inversores."""
    query = "SELECT COUNT(*) FROM inversores WHERE id_inversor = %s"
    resultado = conexion_db.ejecutar_query(query, (id_inversor,))
    
    if resultado is False:
        print("Error al verificar el inversor.")
        return False

    return resultado[0][0] > 0  # Retorna True si existe, False si no

def obtener_inversor_por_email(conexion, email):
    query = "SELECT * FROM inversores WHERE email = %s"
    resultado = conexion.ejecutar_query(query, (email,))
    return resultado if resultado else None

def verificar_existencia(conexion, campo, valor):
    query = f"SELECT 1 FROM inversores WHERE {campo} = %s"
    return bool(conexion.consultar(query, (valor,)))


def registrar_inversor(inversor: Inversor):
    conexion_db = Conexion()
    conexion_db.establecer_conexion()
    try:
        # Inicia la transacción
        conexion_db.iniciar_transaccion()

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
        
        if not conexion_db.ejecutar_query(query_inversor, valores_inversor):
            raise Exception("Error al ejecutar la inserción del inversor.")
        
        print("Inversor creado correctamente.")
    
        # Si el inversor fue creado, procedemos a registrar la cuenta
        print("Procediendo a crear la cuenta con saldo inicial...")
        
        # Generar un número de cuenta único
        numero_cuenta = generar_numero_cuenta_aleatorio(conexion_db)

        if numero_cuenta is None:
            raise Exception("Error al generar un número de cuenta único.")
        
        # Obtener el ID del inversor creado
        id_inversor = conexion_db.ejecutar_query("SELECT LAST_INSERT_ID()")
        if id_inversor:
            id_inversor = id_inversor[0][0]
        else:
            raise Exception("No se pudo obtener el ID del inversor creado.")

        if verificar_id_inversor(conexion_db, id_inversor):
            numero_cuenta = generar_numero_cuenta_aleatorio(conexion_db)
            query_cuenta = """
                INSERT INTO cuentas (numero_cuenta, saldo, fecha_creacion, id_inversor) 
                VALUES (%s, %s, %s, %s)
            """
            valores_cuenta = (numero_cuenta, 1000000.00, date.today(), id_inversor)

            if not conexion_db.ejecutar_query(query_cuenta, valores_cuenta):
                raise Exception("Error al insertar la cuenta.")
            
            # Confirmar la transacción completa
            conexion_db.confirmar()
            print("Cuenta creada exitosamente. Inversor y cuenta registrados.")
        else:
            print(f"El id_inversor {id_inversor} no existe.")



    except Exception as e:
        # Si hay un error al crear la cuenta, revertimos toda la transacción
        print(f"Error al crear la cuenta: {e}")
        conexion_db.revertir()

    finally:
        # Cerramos la conexión
        conexion_db.cerrar_conexion()









