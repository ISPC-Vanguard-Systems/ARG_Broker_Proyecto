class Usuario:
    def __init__(self, id: int, nombre: str, edad: int):
        self.id = id
        self.nombre = nombre
        self.edad = edad

    def __repr__(self):
        return f"Usuario(id={self.id}, nombre='{self.nombre}', edad={self.edad})"
