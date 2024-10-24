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
            cuenta_controlador.vender_acciones(id_inversor)
        elif opcion == "3":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida.")
