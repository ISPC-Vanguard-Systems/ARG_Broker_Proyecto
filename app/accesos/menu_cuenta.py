from app.base_de_datos.conexion import Conexion
from app.controladores.cuenta_controlador import CuentaControlador
from app.servicios_dao.inversor_dao import Inversor_DAO
from app.servicios_dao.accion_dao import AccionesDAO

def ejecutar_menu_transacciones(cuenta_controlador, inversor, id_inversor):

    while True:
# <<<<<<< HEAD:app/accesos/menu_cuenta.py
# #HEAD:app/accesos/menu_cuenta.py
#
#         print("1. Mostrar datos de la cuenta")
#         print("2. Salir al menu principal")
#         opcion = input("Seleccione una opcion:")
# #
# =======
        print(f"\n--- MENÚ DE TRANSACCIONES PARA {inversor.razon_social} ---")
        print("1. Comprar acciones")
        print("2. Vender acciones")
        print("3. Volver al menú principal")

# >>>>>>> origin/main:app/accesos/mostrar.py
        opcion = input("Seleccione una opción: ")
#origin/main:app/accesos/mostrar.py

        if opcion == "1":
            cuenta_controlador.comprar_acciones(id_inversor)

        elif opcion == "2":
            cuenta_controlador.vender_acciones(id_inversor)

#HEAD:app/accesos/menu_cuenta.py
        elif opcion == "2":
            print("Saliendo del programa")
#
        elif opcion == "3":
            print("Volviendo al menú principal...")
#origin/main:app/accesos/mostrar.py
            break

        else:
            print("Opción no válida.")


def ejecutar(inversor):
    try:
        cuenta_controlador = CuentaControlador()
        inversor_dao = Inversor_DAO()

        # Obtener información del inversor
        inversor_info = inversor_dao.obtener_uno(inversor.email)
        if not inversor_info:
            raise Exception("No se pudo obtener la información del inversor")

        id_inversor = inversor_info[0][0]
        while True:
            print(f"\n--- BIENVENIDO {inversor.razon_social} ! ---")
            print("1. Mostrar datos de la cuenta")
            print("2. Listar activos de la cuenta")
            print("3. Realizar transacciones")
            print("4. Cerrar sesión")
            opcion = input("Seleccione una opcion: ")

            if opcion == "1":
                cuenta_controlador.mostrar_datos_cuenta(id_inversor)
            elif opcion == "2":
                pass
            elif opcion == "3":
                ejecutar_menu_transacciones(cuenta_controlador, inversor, id_inversor)
            elif opcion == "4":
                break
            else:
                print("Opción no válida")
    except Exception as e:
        print(f"Error durante la ejecución: {e}")


