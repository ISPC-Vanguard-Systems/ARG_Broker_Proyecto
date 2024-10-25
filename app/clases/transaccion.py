class Transaccion:

    def __init__(self, simbolo, cantidad_acciones, monto_total, comision, valor_inicial, rendimiento):
        self.__simbolo = simbolo
        self.__cantidad_acciones = cantidad_acciones
        self.__monto_total = monto_total
        self.__comision = comision
        self.__valor_inicial = valor_inicial
        self.__rendimiento = rendimiento

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

    def get_valor_inicial(self):
        return self.__valor_inicial

    def set_valor_inicial(self, valor_inicial):
        self.__valor_inicial = valor_inicial

    def get_rendimiento(self):
        return self.__rendimiento

    def set_rendimiento(self, rendimiento):
        self.__rendimiento = rendimiento



