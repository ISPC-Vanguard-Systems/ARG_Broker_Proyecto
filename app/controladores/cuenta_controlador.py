from datetime import datetime, date
from app.servicios_dao.cuenta_dao import CuentaDAO
from app.clases.cuenta import Cuenta
from app.servicios_dao.accion_dao import AccionesDAO
from decimal import Decimal
from app.base_de_datos.conexion import Conexion
import random

class CuentaControlador:
    def __init__(self):
        self.cuenta_dao = CuentaDAO()
        self.acciones_dao = AccionesDAO()

    def mostrar_activos_portafolio(self, id_inversor):
        """Genera precios aleatorios y muestra los activos del inversor con rendimiento."""
        activos = self.acciones_dao.listar_acciones_por_inversor(id_inversor)

        if not activos:
            print("No tienes activos en tu portafolio.")
            return

        print("\n--- Activos del Portafolio ---")
        for activo in activos:
            id_accion = activo[0]
            nombre_empresa = activo[1]
            cantidad = int(activo[2])
            precio_compra = Decimal(activo[3])  # Precio de compra almacenado

            # Generar precios aleatorios
            nuevo_precio_compra = round(precio_compra * Decimal(random.uniform(0.9, 1.1)), 2)
            nuevo_precio_venta = round(precio_compra * Decimal(random.uniform(0.9, 1.1)), 2)

            # Calcular rendimiento económico
            rendimiento = round((nuevo_precio_venta - precio_compra) * cantidad, 2)

            # Mostrar resultados
            signo = "+" if rendimiento >= 0 else ""
            print(f"ID: {id_accion} - Empresa: {nombre_empresa}")
            print(f"Cantidad: {cantidad} acciones")
            print(f"Precio Compra Actual: ${nuevo_precio_compra}")
            print(f"Precio Venta Actual: ${nuevo_precio_venta}")
            print(f"Rendimiento: {signo}${rendimiento}\n")

    def mostrar_datos_cuenta(self, id_inversor):
        rendimiento_acumulado = 0
        total_invertido = 0

        datos = self.cuenta_dao.obtener_datos_cuenta(id_inversor)
        if datos:
            cuenta = Cuenta(id_inversor, *datos)
            transacciones = self.cuenta_dao.obtener_transacciones_por_cuenta(id_inversor)

            fecha_creacion = cuenta.get_fecha_creacion()

            if isinstance(fecha_creacion, (datetime, date)):
                fecha_formateada = fecha_creacion.strftime("%d-%m-%Y")
            else:
                fecha_creacion = datetime.strptime(fecha_creacion, "%Y-%m-%d")
                fecha_formateada = fecha_creacion.strftime("%d-%m-%Y")

            if transacciones:
                # Calcular total invertido y rendimiento acumulado
                total_invertido = (
                    sum(t.get_monto_total() for t in transacciones if t.get_tipo() == 1) -
                    sum(t.get_monto_total() for t in transacciones if t.get_tipo() == 2)
                )
                
                acciones_dao = AccionesDAO()

                # Calcular rendimiento acumulado
                for t in transacciones:
                    id_accion = t.get_id_accion()
                    datos_accion = acciones_dao.comprobar_accion(id_accion)
                    cantidad = acciones_dao.comprobar_accion_por_inversor(id_inversor, id_accion)[0][2]

                    if datos_accion:
                        precio_compra = datos_accion[0][3]
                        precio_venta = datos_accion[0][4]

                        # Generar precios aleatorios
                        nuevo_precio_compra = round(precio_compra * Decimal(random.uniform(0.9, 1.1)), 2)
                        nuevo_precio_venta = round(precio_compra * Decimal(random.uniform(0.9, 1.1)), 2)

                        rendimiento = round((nuevo_precio_venta - nuevo_precio_compra) * cantidad, 2)

                        rendimiento_acumulado += rendimiento

            else:
                print("No hay transacciones para esta cuenta")

            # Mostrar la información de la cuenta
            print(f"Fecha de Alta: {fecha_formateada}")
            print(f"Nro de Cuenta: {cuenta.get_numero_cuenta()}")
            print(f"Saldo Disponible: ${cuenta.get_saldo():.2f}")
            print(f"Total Invertido: ${total_invertido:.2f}")
            print(f"Rendimiento Acumulado: ${rendimiento_acumulado:.2f}")

        else:
            print("Cuenta no encontrada")

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

        finally:
            conexion.cerrar_conexion()

    def vender_acciones(self, id_inversor):
        # Listar acciones disponibles del inversor
        acciones_inversor = self.acciones_dao.listar_acciones_por_inversor(id_inversor)

        if not acciones_inversor:
            print("No tienes acciones disponibles para vender.")
            return

        # Mostrar acciones disponibles
        print("\n--- Tus Acciones ---")
        for accion in acciones_inversor:
            print(f"ID: {accion[0]} - Empresa: {accion[1]} - Cantidad: {accion[2]} - Precio Venta: {accion[3]}")

        # Selección del ID de la acción a vender
        try:
            id_accion = int(input("\nIngrese el ID de la acción que desea vender: "))
            accion = self.acciones_dao.comprobar_accion_por_inversor(id_inversor, id_accion)

            if accion:
                cantidad_disponible = accion[0][2]
                cantidad = int(input(f"Ingrese la cantidad a vender (disponible: {cantidad_disponible}): "))

                if cantidad <= cantidad_disponible:
                    precio_venta = accion[0][3]
                    monto_total = (precio_venta * cantidad) * Decimal(0.85)  # 15% de comisión

                    # Registrar la transacción
                    self.acciones_dao.registrar_transaccion(
                        id_inversor, id_accion, cantidad, monto_total, Decimal(0.15) * monto_total, 2
                    )

                    # Actualizar el saldo del inversor
                    saldo_actual = self.acciones_dao.obtener_saldo_inversor(id_inversor)
                    self.acciones_dao.actualizar_saldo(id_inversor, saldo_actual + monto_total)

                    # Actualizar la cantidad de acciones
                    self.acciones_dao.actualizar_cantidad_acciones(id_inversor, id_accion, -cantidad)

                    print(f"Venta exitosa: {cantidad} acciones de {accion[0][1]} por ${monto_total:.2f}.")
                else:
                    print("No tienes suficientes acciones para vender esa cantidad.")
            else:
                print("No tienes esa acción en tu portafolio.")
        except ValueError:
            print("Entrada inválida. Asegúrese de ingresar un número válido.")
 