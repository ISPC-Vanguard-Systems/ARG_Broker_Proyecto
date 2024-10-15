from app.servicios_dao import cuenta_dao

def mostrar_datos_cuenta(id_cuenta):

    cuenta = cuenta_dao.obtener_datos_cuenta(id_cuenta)

    if cuenta:
        print(f"Numero de Cuenta: {cuenta_dao.Cuenta.get_numero_cuenta()}")
        print(f"Saldo: {cuenta_dao.Cuenta.get_saldo()}")

    else:
        print("Cuenta no econtrada")




