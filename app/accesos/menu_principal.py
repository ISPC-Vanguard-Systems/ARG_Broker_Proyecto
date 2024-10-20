from app.controladores.inversor_controller import Inversor_Controller
from app.accesos.mostrar import ejecutar

def ejecutar_menu():
    inversor_ctrl = Inversor_Controller()

    while True:
        print("\n--- MENÚ ---")
        print("1. Registrar inversor")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            inversor_ctrl.registrar_nuevo_inversor()
        elif opcion == '2':
            if inversor_ctrl.iniciar_sesion():
                ejecutar()
        elif opcion == '3':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")