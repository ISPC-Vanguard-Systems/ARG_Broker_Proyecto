from app.base_de_datos.conexion import Conexion
from app.controladores.cuenta_controlador import CuentaControlador
from app.servicios_dao.inversor_dao import Inversor_DAO

def ejecutar_menu_transacciones(cuenta_controlador, inversor, id_inversor):
    print(f"\n--- MENÚ DE TRANSACCIONES PARA {inversor.razon_social} ---")
    print("1. Comprar acciones (Asignar al inversor)")
    print("2. Vender acciones")
    print("3. Volver al menú principal")

    while True:
#HEAD:app/accesos/menu_cuenta.py

        print("1. Mostrar datos de la cuenta")
        print("2. Salir al menu principal")
        opcion = input("Seleccione una opcion:")
#
        opcion = input("Seleccione una opción: ")
#origin/main:app/accesos/mostrar.py

        if opcion == "1":
            cuenta_controlador.comprar_acciones(id_inversor)

        elif opcion == "2":
            id_accion = int(input("Ingrese el ID de la acción a vender: "))
            cantidad = int(input("Ingrese la cantidad de acciones a vender: "))
            cuenta_controlador.vender_acciones(inversor['id_inversor'], id_accion, cantidad)

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
    acceso_bd = Conexion()
    try:
        cuenta_controlador = CuentaControlador(acceso_bd)
        inversor_logueado = Inversor_DAO().obtener_uno(inversor.email)

        id_inversor = inversor_logueado[0][0]
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
    finally:
        acceso_bd.cerrar_conexion()


