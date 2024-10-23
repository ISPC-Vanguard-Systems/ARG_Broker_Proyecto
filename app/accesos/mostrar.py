from app.base_de_datos.conexion import Conexion
from app.controladores.cuenta_controlador import CuentaControlador
from app.servicios_dao.inversor_dao import Inversor_DAO
from app.servicios_dao.accion_dao import AccionesDAO

def ejecutar_menu_transacciones(cuenta_controlador, inversor, id_inversor):

    while True:
        print(f"\n--- MENÚ DE TRANSACCIONES PARA {inversor.razon_social} ---")
        print("1. Comprar acciones (Asignar al inversor)")
        print("2. Vender acciones")
        print("3. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cuenta_controlador.comprar_acciones(id_inversor)

        elif opcion == "2":
            id_accion = int(input("Ingrese el ID de la acción a vender: "))
            cantidad = int(input("Ingrese la cantidad de acciones a vender: "))
            cuenta_controlador.vender_acciones(inversor['id_inversor'], id_accion, cantidad)

        elif opcion == "3":
            print("Volviendo al menú principal...")
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
            opcion = input("Seleccione una opcion: ")

            if opcion == "1":
                cuenta_controlador.mostrar_datos_cuenta(id_inversor)
            elif opcion == "2":
                pass
            elif opcion == "3":
                ejecutar_menu_transacciones(cuenta_controlador, inversor, id_inversor)
            elif opcion == "5":
                print("Saliendo del programa")
                break
            else:
                print("Opción no válida")
    except Exception as e:
        print(f"Error durante la ejecución: {e}")


