from datos import *

def elim():
    Json = cargar_datos()
    while True:
        print("----escribe porfavor tu documento para eliminar----")
        doc = input("->")
        if str(doc) in Json["Usuarios"]:
            Json["Usuarios"].pop(doc)
            guardar_datos(Json)
            break
        else:
            print("***********************************************************")
            print("______Error este doc no existe______")
            print("***********************************************************")
