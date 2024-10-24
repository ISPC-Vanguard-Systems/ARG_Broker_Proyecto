from app.clases.inversor import Inversor
from app.servicios_dao.inversor_dao import Inversor_DAO
from app.base_de_datos.conexion import Conexion


class Inversor_Controller():

    def __init__(self):
        self.Inversor_dao = Inversor_DAO()
        # self.conexion_db = Conexion() La eliminamos porque es una conexion permanente


    def _solicitar_opcion(self, mensaje, opciones_validas):
        while True:
            try:
                opcion = int(input(mensaje))
                if opcion in opciones_validas:
                    return opcion
                else:
                    print(f"Por favor, ingrese un valor válido: {opciones_validas}.")
            except ValueError as e:
                print(f"Error: {e}. Debe ingresar un número.")

    def _solicitar_documento(self, tipo_documento):
        tipos = {1: "CUIL", 2: "CUIT", 3: "Pasaporte"}
        while True:
            try:
                documento = input(f"Ingrese su {tipos[tipo_documento]}: ")
                if not Inversor.validar_documento(documento, tipo_documento):
                    print("Documento inválido.")
                elif self.Inversor_dao.verificar_existencia("documento", documento):
                    print("Documento ya registrado.")
                else:
                    return documento
            except Exception as e:  # Captura cualquier excepción que pueda surgir
                print(f"Error al validar el documento: {e}")

    def _solicitar_contrasena(self):
        while True:
            try:
                contrasena = input("Ingrese la contraseña: ")
                if Inversor.validar_contrasena(contrasena):
                    print("Contraseña válida.")
                    return contrasena
                else:
                    print("Contraseña inválida.")
            except Exception as e:  # Captura cualquier excepción durante la validación
                print(f"Error al validar la contraseña: {e}")

    def registrar_nuevo_inversor(self):
        razon_social = ""
        while True:
            razon_social = input("Ingrese la razón social: ")
            if not self.Inversor_dao.verificar_existencia("razon_social", razon_social):
                break
            print("Razón social ya registrada.")

        tipo_documento = self._solicitar_opcion("Seleccione el tipo de documento (1- CUIL, 2- CUIT, 3- Pasaporte): ", [1, 2, 3])
        documento = self._solicitar_documento(tipo_documento)

        email = ""
        while True:
            email = input("Ingrese el email: ")
            if Inversor.validar_email(email):
                break
            print("Email inválido o ya registrado.")

        telefono = ""
        while True:
            telefono = input("Ingrese el teléfono: ")
            if not self.Inversor_dao.verificar_existencia("telefono", telefono):
                break
            print("Teléfono ya registrado.")

        perfil_inversor = self._solicitar_opcion("Seleccione el perfil del inversor (1- Conservador, 2- Agresivo): ", [1, 2])
        tipo_inversor = self._solicitar_opcion("Seleccione el tipo de inversor (1- Persona Física, 2- Empresa): ", [1, 2])
        contrasena = self._solicitar_contrasena()

        inversor = Inversor(
            documento=documento,
            email=email,
            telefono=telefono,
            razon_social=razon_social,
            perfil_inversor=perfil_inversor,
            tipo_documento=tipo_documento,
            tipo_inversor=tipo_inversor,
            contrasena=contrasena
        )

        return self.Inversor_dao.insertar(inversor)

    def iniciar_sesion(self): 
        email = input("Ingrese su email: ")
        
        # Intento de conectar a la base de datos y obtener el inversor por email
        inversor = self.Inversor_dao.obtener_uno(email)

        if inversor:
            intentos = 3  # Número máximo de intentos permitidos
            while intentos > 0:
                contrasena = input("Ingrese su contraseña: ")

                # Comparar la contraseña ingresada con la registrada
                if inversor[0][1] == contrasena:  # Asumiendo que la contraseña está en la columna 1
                    print(f"Inicio de sesión exitoso. Bienvenido, {inversor[0][5]}!")
                    
                    # Crear un objeto inversor y devolverlo para futuras operaciones
                    inversor_obj = Inversor(
                        documento=inversor[0][2],           # Documento
                        email=inversor[0][3],               # Email
                        telefono=inversor[0][4],            # Teléfono
                        razon_social=inversor[0][5],        # Razón social
                        perfil_inversor=inversor[0][6],     # Perfil
                        tipo_documento=inversor[0][7],      # Tipo documento
                        tipo_inversor=inversor[0][8],       # Tipo inversor
                        contrasena=inversor[0][1]           # Contraseña
                    )
                    return inversor_obj  # Retorna el objeto inversor
                else:
                    intentos -= 1
                    if intentos > 0:
                        print(f"Contraseña incorrecta. Intentos restantes: {intentos}.")
                    else:
                        print("Ha superado el número máximo de intentos. Sesión bloqueada.")
                        return None  # Bloqueo, retorna None
        else:
            print("Email no registrado.")
            return None  # Email no encontrado

