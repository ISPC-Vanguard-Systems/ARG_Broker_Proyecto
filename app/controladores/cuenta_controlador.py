from app.servicios_dao.cuenta_dao import CuentaDao
from app.clases.cuenta import Cuenta 
from app.controladores.accion_controller import AccionesDAO

class CuentaControlador:
    def __init__(self, acceso_db):
        self.cuenta_dao = CuentaDao(acceso_db)
        self.acciones_dao = AccionesDAO()

    def mostrar_datos_cuenta(self, id_cuenta):

        datos = self.cuenta_dao.obtener_datos_cuenta(id_cuenta)

        if datos:
            cuenta = Cuenta(id_cuenta, *datos)
            print(f"Numero de Cuenta: {cuenta.get_numero_cuenta()}")
            print(f"Saldo: {cuenta.get_saldo()}")

        else:
            print("Cuenta no econtrada")


    def comprar_acciones(self, id_inversor):
        self.acciones_dao.listar_acciones_disponibles()

        while True:
            try:
                id_accion = int(input("Ingrese el ID de la acción que desea comprar: "))
                
                # Verificar si la acción existe y obtener su información
                accion = self.acciones_dao.comprobar_accion(id_accion)

                if accion:
                    print(f"Precio Compra: {accion[0][3]} - Precio Venta: {accion[0][4]}")
                    cantidad = int(input("Ingrese la cantidad de acciones que desea comprar: "))
                    
                    # Asignar las acciones al inversor
                    self.acciones_dao.asignar_acciones(
                        id_inversor, id_accion, cantidad, accion[0][3], accion[0][4]
                    )

                    print(f"El inversor ha comprado {cantidad} acciones de {accion[0][2]} a ${accion[0][4]}.")
                    break  # Salir del bucle después de una compra exitosa
                else:
                    print("La acción no existe. Por favor, ingrese un ID válido.")

            except ValueError:
                print("Entrada inválida. Asegúrese de ingresar un número válido.")
            



    def vender_acciones(self, id_cuenta, id_accion, cantidad):
        query_check = """
            SELECT cantidad_acciones FROM acciones_por_inversores 
            WHERE id_inversor = %s AND id_accion = %s
        """
        resultado = self.conexion.ejecutar_query(query_check, (id_cuenta, id_accion))

        if resultado and resultado[0][0] >= cantidad:
            query_update = """
                UPDATE acciones_por_inversores 
                SET cantidad_acciones = cantidad_acciones - %s 
                WHERE id_inversor = %s AND id_accion = %s
            """
            self.conexion.ejecutar_query(query_update, (cantidad, id_cuenta, id_accion))
            self.conexion.confirmar()
            print(f"Se vendieron {cantidad} acciones del ID {id_accion}.")
        else:
            print("No tiene suficientes acciones para vender.")




