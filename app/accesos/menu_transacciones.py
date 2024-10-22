from app.base_de_datos.conexion import Conexion


def ejecutar_menu_transacciones(cuenta_controlador, inversor, id_inversor):
    print(f"\n--- MENÚ DE TRANSACCIONES PARA {inversor.razon_social} ---")
    print("1. Comprar acciones (Asignar al inversor)")
    print("2. Vender acciones")
    print("3. Volver al menú principal")

    while True:

        opcion = input("Seleccione una opción: ")


        if opcion == "1":
            cuenta_controlador.comprar_acciones(id_inversor)

        elif opcion == "2":
            id_accion = int(input("Ingrese el ID de la acción a vender: "))
            cantidad = int(input("Ingrese la cantidad de acciones a vender: "))
            cuenta_controlador.vender_acciones(inversor['id_inversor'], id_accion, cantidad)


        elif opcion == "3":
            print("Volviendo al menú principal...")
            # origin/main:app/accesos/mostrar.py
            break

        else:
            print("Opción no válida.")


