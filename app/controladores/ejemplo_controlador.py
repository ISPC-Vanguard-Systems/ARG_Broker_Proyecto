from app.servicios_dao import ejemplo_dao
def ver_datos():
    print("Mostrando los datos:")
    datos = ejemplo_dao.obtener_datos()
    for dato in datos:
        print(f"ID: {dato['id']}, Nombre: {dato['nombre']}, Edad: {dato['edad']}")


def insertar_datos(nombre, edad):
    print(f"Insertando {nombre} con edad {edad}...")
    resultado = ejemplo_dao.insertar_dato(nombre, edad)
    if resultado:
        print("Datos insertados correctamente.")
    else:
        print("Error al insertar los datos.")


def actualizar_datos(id, nuevo_nombre, nueva_edad):
    print(f"Actualizando registro con ID {id}...")
    resultado = ejemplo_dao.actualizar_dato(id, nuevo_nombre, nueva_edad)
    if resultado:
        print("Datos actualizados correctamente.")
    else:
        print("Error al actualizar los datos.")


def eliminar_datos(id):
    print(f"Eliminando registro con ID {id}...")
    resultado = ejemplo_dao.eliminar_dato(id)
    if resultado:
        print("Datos eliminados correctamente.")
    else:
        print("Error al eliminar los datos.")
