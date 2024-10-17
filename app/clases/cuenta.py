class Cuenta:
    def __init__(self, id_cuenta, numero_cuenta, saldo, fecha_creacion):
        self.__id_cuenta = id_cuenta
        self.__numero_cuenta = numero_cuenta
        self.__saldo = saldo
        self.__fecha_creacion = fecha_creacion

    def get_id_cuenta(self):
        return self.__id_cuenta

    def set_id_cuenta(self, id_cuenta):
        self.__id_cuenta = id_cuenta

    def get_numero_cuenta(self):
        return self.__numero_cuenta

    def set_numero_cuenta(self, numero_cuneta):
        self.__numero_cuenta = numero_cuneta

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def get_fecha_creacion(self):
        return self.__fecha_creacion

    def set_fecha_creacion(self, fecha_creacion):
        self.__fecha_creacion = fecha_creacion

