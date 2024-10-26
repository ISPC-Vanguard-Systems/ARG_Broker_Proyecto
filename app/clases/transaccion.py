class Transaccion:

    def __init__(self, id_accion, simbolo, razon_social, monto_total, comision, tipo):
        self.__id_accion = id_accion
        self.__simbolo = simbolo
        self.__monto_total = monto_total
        self.__comision = comision
        self.__razon_social = razon_social
        self.__tipo = tipo

    def get_id_accion(self):
        return self.__id_accion
    
    def set_id_accion(self, id_accion):
        self.__id_accion = id_accion

    def get_simbolo(self):
        return self.__simbolo

    def set_simbolo(self, simbolo):
        self.__simbolo = simbolo

    def get_monto_total(self):
        return self.__monto_total

    def set_monto_total(self, monto_total):
        self.__monto_total = monto_total

    def get_comision(self):
        return self.__comision

    def set_comision(self, comision):
        self.__comision = comision

    def get_razon_social(self):
        return self.__razon_social

    def set_razon_social(self, razon_social):
        self.__razon_social = razon_social

    def get_tipo(self):
        return self.__tipo

    def set_tipo(self, tipo):
        self.__tipo = tipo


