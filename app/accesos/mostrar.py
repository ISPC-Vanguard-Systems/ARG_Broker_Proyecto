from app.controladores.cuenta_controlador import mostrar_datos_cuenta


def ejecutar():
    while True:

        print("1. Mostrar datos de la cuenta")

        opcion = input("Seleccione una opcion")

        if opcion == '1':

            id_cuenta = int(input("Ingrese el ID de la cuenta:"))
            mostrar_datos_cuenta(id_cuenta)

        else:
            print("Opcion no valida")
