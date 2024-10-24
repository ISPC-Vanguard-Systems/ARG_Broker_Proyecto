from abc import ABC, abstractmethod


class InterfaceDAO(ABC):

    @abstractmethod
    def verificar_existencia(self, campo, valor):
        """Verifica si existe un registro según el campo y valor proporcionado"""
        pass

    @abstractmethod
    def obtener_todos(self):
        """Obtiene todos los registros"""
        pass

    @abstractmethod
    def obtener_uno(self, id):
        """Encuentra un registro por su ID"""
        pass

    @abstractmethod
    def eliminar(self, id):
        """Elimina un registro por su ID"""
        pass

    @abstractmethod
    def actualizar(self, id, data):
        """Actualiza un registro existente"""
        pass

    @abstractmethod
    def insertar(self, data):
        """Inserta un nuevo registro"""
        pass