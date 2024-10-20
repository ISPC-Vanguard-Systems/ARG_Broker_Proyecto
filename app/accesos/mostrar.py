from app.base_de_datos.conexion import Conexion
from app.controladores.cuenta_controlador import CuentaControlador


def ejecutar():
    acceso_bd = Conexion()
    cuenta_controlador = CuentaControlador(acceso_bd)
    while True:

        print("1. Mostrar datos de la cuenta")
        print("2 Salir al menu principal")
        opcion = input("Seleccione una opcion:")

        if opcion == "1":

            id_cuenta = int(input("Ingrese el ID de la cuenta: "))
            cuenta_controlador.mostrar_datos_cuenta(id_cuenta)

        elif opcion == "2":
            print("Saliendo del programa")
            break

        else:
            print("Opcion no valida")


