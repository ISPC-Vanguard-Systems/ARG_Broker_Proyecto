from app.servicios_dao.cuenta_dao import CuentaDao
from app.clases.cuenta import Cuenta


class CuentaControlador:
    def __init__(self, acceso_db):
        self.cuenta_dao = CuentaDao(acceso_db)

    def mostrar_datos_cuenta(self, id_cuenta):

        datos = self.cuenta_dao.obtener_datos_cuenta(id_cuenta)

        if datos:
            cuenta = Cuenta(id_cuenta, *datos)
            print(f"Numero de Cuenta: {cuenta.get_numero_cuenta()}")
            print(f"Saldo: {cuenta.get_saldo()}")

        else:
            print("Cuenta no econtrada")




