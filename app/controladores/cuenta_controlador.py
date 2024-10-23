from app.servicios_dao.cuenta_dao import CuentaDao
from app.clases.cuenta import Cuenta 
from app.servicios_dao.accion_dao import AccionesDAO
from decimal import Decimal
from app.base_de_datos.conexion import Conexion

class CuentaControlador:
    def __init__(self):
        self.cuenta_dao = CuentaDao()
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
        # Mostramos en primer lugar la lista de acciones
        self.acciones_dao.listar_acciones_disponibles()

        try:
            id_accion = int(input("Ingrese el ID de la acción que desea comprar: "))
            with Conexion() as conexion:
                try:
                    conexion.iniciar_transaccion()
                
                    # Verificar si la acción existe y obtener su información
                    accion = self.acciones_dao.comprobar_accion(id_accion)

                    if accion:
                        print(f"Precio Compra: {accion[0][3]} - Precio Venta: {accion[0][4]}")
                        cantidad = int(input("Ingrese la cantidad de acciones que desea comprar: "))
                        
                        # Calcular el monto total de la compra con la comisión (15%)
                        precio_compra = accion[0][3]
                        monto_total = round((precio_compra * cantidad) * Decimal(1.15), 2)  # 15% de comisión

                        # Obtener el saldo del inversor
                        saldo = self.acciones_dao.obtener_saldo_inversor(id_inversor)

                        if saldo >= monto_total:
                            # Registrar la transacción en la tabla `transacciones`
                            self.acciones_dao.registrar_transaccion(
                                id_inversor, id_accion, cantidad, monto_total, Decimal(0.15) * monto_total, 1
                            )

                            # Actualizar el saldo del inversor
                            self.acciones_dao.actualizar_saldo(id_inversor, saldo - monto_total)

                            # Asignar las acciones al inversor en la tabla `acciones_por_inversores`
                            self.acciones_dao.asignar_acciones(
                                id_inversor, id_accion, cantidad, precio_compra, accion[0][4]
                            )

                            conexion.confirmar()

                            print(f"Compra exitosa: {cantidad} acciones de {accion[0][2]} por ${monto_total:.2f}.")
                        else:
                            print("Saldo insuficiente para realizar la compra.")
                    else:
                        print("La acción no existe. Por favor, ingrese un ID válido.")

                except Exception as e:
                    conexion.revertir()
                    print(f"Error en la transacción: {e}")

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




