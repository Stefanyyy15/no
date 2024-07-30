from datos import *

def elim():
    Json = cargar_datos()
    while True:
        doc = str(input("----escribe porfavor tu documento para eliminar----"))
        if str(doc) in Json["Usuarios"]:
            Json["Usuarios"].pop(doc)
        else:
            print("***********************************************************")
            print("______Error este doc no existe______")
            print("***********************************************************")