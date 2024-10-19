from app.controladores.inversor_controller import Inversor_Controller
from app.accesos.mostrar import ejecutar

controlador = Inversor_Controller()

def ejecutar_menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Registrar inversor")
        print("2. Iniciar sesión")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            controlador.registrar_nuevo_inversor()
        elif opcion == '2':
            inversor_logueado = controlador.iniciar_sesion()
            if inversor_logueado:  # Solo llama a ejecutar() si el inicio de sesión es exitoso
                ejecutar(inversor_logueado)
        elif opcion == '3':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def main():
    print("Bienvenido a la plataforma de inversión.")
    ejecutar_menu()


if __name__ == "__main__":
    main()
