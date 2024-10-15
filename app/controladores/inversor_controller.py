import re
from app.servicios_dao.inversor_dao import registrar_inversor, obtener_inversor_por_email
from app.clases.inversor import Inversor
from app.base_de_datos.conexion import Conexion


def ejecutar_menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Registrar inversor")
        print("2. Iniciar sesion")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_nuevo_inversor()
        elif opcion == '2':
            iniciar_sesion()
        elif opcion == '3':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

"""VALIDACION DE EMAIL"""
def validar_email(email):
    # Expresión regular para validar email
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, email) is not None

"""VALIDACION DOCUMENTO"""
def validar_documento(documento, tipo_documento):
    # Define las longitudes esperadas para cada tipo
    longitudes = {1: 11, 2: 11, 3: 9}  # CUIL/CUIT: 11 dígitos, Pasaporte: 9 dígitos
    return documento.isdigit() and len(documento) == longitudes.get(tipo_documento, 0)

"""FUNCION PARA EL MANEJO DE LAS OPCIONES"""
def solicitar_opcion(mensaje, opciones_validas):
    while True:
        try:
            opcion = int(input(mensaje))
            if opcion in opciones_validas:
                return opcion
            else:
                print(f"Por favor, ingrese un valor válido: {opciones_validas}.")
        except ValueError:
            print("Debe ingresar un número.")

"""FUNCION PEDIDO DE DOCUMENTO"""
def solicitar_documento(tipo_documento, conexion):
    tipos = {1: "CUIL", 2: "CUIT", 3: "Pasaporte"}
    while True:
        documento = input(f"Ingrese su {tipos[tipo_documento]}: ")
        if validar_documento(documento, tipo_documento) and not conexion.verificar_existencia("documento", documento):
            return documento
        else:
            print("Documento inválido o ya registrado.")

"""VALIDACION CONTRASEÑA"""
def validar_contrasena(contrasena):
    if (len(contrasena) < 8 or
        not re.search(r"[A-Z]", contrasena) or  # Al menos una letra mayúscula
        not re.search(r"[a-z]", contrasena) or  # Al menos una letra minúscula
        not re.search(r"[0-9]", contrasena) or  # Al menos un número
        not re.search(r"[!@#$%^&*(),.?\":{}|<>]", contrasena)):  # Al menos un símbolo
        return False
    return True

def solicitar_contrasena():
    while True:
        contrasena = input("Ingrese la contraseña: ")
        if validar_contrasena(contrasena):
            print("Contraseña válida.")
            return contrasena
        else:
            print("Contraseña inválida. Debe tener al menos 8 caracteres, incluyendo una mayúscula, una minúscula, un número y un símbolo.")

def registrar_nuevo_inversor():
    # Instanciar la conexión
    conexion = Conexion()
    # Establecer la conexión
    conexion.establecer_conexion()

    razon_social = ""
    while True:
        razon_social = input("Ingrese la razón social: ")
        if not conexion.verificar_existencia("razon_social", razon_social):
            break
        print("Razón social ya registrada.")

    tipo_documento = solicitar_opcion("Seleccione el tipo de documento (1- CUIL, 2- CUIT, 3- Pasaporte): ", [1, 2, 3])

    documento = solicitar_documento(tipo_documento, conexion)

    email = ""
    while True:
        email = input("Ingrese el email: ")
        if validar_email(email) and not conexion.verificar_existencia("email", email):
            break
        print("Email inválido o ya registrado.")

    telefono = ""
    while True:
        telefono = input("Ingrese el teléfono: ")
        if not conexion.verificar_existencia("telefono", telefono):
            break
        print("Teléfono ya registrado.")

    perfil_inversor = solicitar_opcion("Seleccione el perfil del inversor (1- Conservador, 2- Agresivo): ", [1, 2])

    tipo_inversor = solicitar_opcion("Seleccione el tipo de inversor (1- Persona Física, 2- Empresa): ", [1, 2])

    contrasena = solicitar_contrasena()

    inversor = Inversor(documento, email, telefono, razon_social, perfil_inversor, tipo_documento, tipo_inversor, contrasena)
    registrar_inversor(inversor)


# Trabajo con el inicio de sesion

def iniciar_sesion():

    conexion = Conexion()
    conexion.establecer_conexion()

    email = input("Ingrese su email: ")
    contrasena = input("Ingrese su contraseña: ")

    inversor = obtener_inversor_por_email(conexion, email)

    if inversor:
        # Comparar la contraseña ingresada con la registrada
        if inversor[0][1] == contrasena: 
            print(f"Inicio de sesión exitoso. Bienvenido, {inversor[0][5]}!")
        else:
            print("Contraseña incorrecta. Intente nuevamente.")
    else:
        print("Email no registrado.")

    conexion.cerrar_conexion()
