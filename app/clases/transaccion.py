class Transaccion:

    def __init__(self, simbolo, cantidad_acciones, monto_total, comision):
        self.__simbolo = simbolo
        self.__cantidad_acciones = cantidad_acciones
        self.__monto_total = monto_total
        self.__comision = comision

    def get_simbolo(self):
        return self.__simbolo

    def set_simbolo(self, simbolo):
        self.__simbolo = simbolo

    def get_cantidad_acciones(self):
        return self.__cantidad_acciones

    def set_cantidad_acciones(self, cantidad_acciones):
        self.__cantidad_acciones = cantidad_acciones

    def get_monto_total(self):
        return self.__monto_total

    def set_monto_total(self, monto_total):
        self.__monto_total = monto_total

    def get_comision(self):
        return self.__comision

    def set_comision(self, comision):
        self.__comision = comision