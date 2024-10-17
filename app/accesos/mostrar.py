from app.base_de_datos.conexion import Conexion
from app.controladores.cuenta_controlador import CuentaControlador
from app.controladores.inversor_controller import iniciar_sesion, registrar_nuevo_inversor

def ejecutar():
    acceso_bd = Conexion()
    cuenta_controlador = CuentaControlador(acceso_bd)
    while True:

        print("1. Mostrar datos de la cuenta")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":

            id_cuenta = int(input("Ingrese el ID de la cuenta: "))
            cuenta_controlador.mostrar_datos_cuenta(id_cuenta)

        elif opcion == "5":
            print("Saliendo del programa")
            break

        else:
            print("Opcion no valida")


# def ejecutar_menu():
#     from app.accesos.mostrar import iniciar_sesion, registrar_nuevo_inversor  # Importación diferida
#
#     while True:
#         print("\n--- MENÚ ---")
#         print("1. Registrar inversor")
#         print("2. Iniciar sesión")
#         print("3. Salir")
#
#         opcion = input("Seleccione una opción: ")
#
#         if opcion == '1':
#             registrar_nuevo_inversor()
#         elif opcion == '2':
#             if iniciar_sesion():  # Verifica el resultado de iniciar_sesion()
#                 ejecutar()  # Llama a la función ejecutar() solo si fue exitoso
#         elif opcion == '3':
#             print("Saliendo...")
#             break
#         else:
#             print("Opción no válida. Intente de nuevo.")

# def ejecutar_menu():
#     while True:
#         print("\n--- MENÚ ---")
#         print("1. Registrar inversor")
#         print("2. Iniciar sesion")
#         print("3. Salir")
#         opcion = input("Seleccione una opción: ")
#
#         if opcion == '1':
#             registrar_nuevo_inversor()
#         elif opcion == '2':
#             iniciar_sesion()
#             bandera = 1
#             if bandera == 1:
#                 ejecutar()
#         elif opcion == '3':
#             print("Saliendo...")
#             break
#         else:
#             print("Opción no válida. Intente de nuevo.")
