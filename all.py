import datos as zumba

def registrar():
    jms= zumba.cargar_datos()
    dixi={}
    doc=int(input("Ingrese codigo: "))
    if doc in jms["Usuarios"]:
        print("Ya esiste")
    else:
        dixi["Nombre"]=input("POnga name: ")
        dixi["Edad"]=input("POnga Edad: ")
        dixi["Estado"]=input("POnga Estado: ")
        dixi["Correo"]=input("POnga Correo: ")
        jms["Usuarios"][doc]=dixi
        print("Se registró correctamente")
    zumba.guardar_datos(jms)

