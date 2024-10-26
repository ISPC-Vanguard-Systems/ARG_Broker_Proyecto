from app.controladores.ejemplo_controlador import ver_datos, insertar_datos, actualizar_datos, eliminar_datos


def ejecutar_menu():
    while True:
        print("=== Menú Principal ===")
        print("1. Ver datos")
        print("2. Insertar datos")
        print("3. Actualizar datos")
        print("4. Eliminar datos")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ver_datos()
        elif opcion == "2":
            nombre = input("Ingresa el nombre: ")
            edad = input("Ingresa la edad: ")
            insertar_datos(nombre, edad)
        elif opcion == "3":
            id = input("Ingresa el ID del registro a actualizar: ")
            nuevo_nombre = input("Ingresa el nuevo nombre: ")
            nueva_edad = input("Ingresa la nueva edad: ")
            actualizar_datos(id, nuevo_nombre, nueva_edad)
        elif opcion == "4":
            id = input("Ingresa el ID del registro a eliminar: ")
            eliminar_datos(id)
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")