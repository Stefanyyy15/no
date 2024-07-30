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


def modificar():
    jms= zumba.cargar_datos()
    dixi={}
    doc=input("Ingrese codigo: ")
    if doc in jms["Usuarios"]:
        dixi["Nombre"]=input("Ponga su name otra vez, imbecil: ")
        dixi["Edad"]=input("Ponga su Edad otra vez, imbecil: ")
        dixi["Estado"]=input("Ponga su Estado otra vez, imbecil: ")
        dixi["Correo"]=input("Ponga su Correo otra vez, imbecil: ")
        jms["Usuarios"][doc]=dixi
        print("Se modifico correctamente")
        zumba.guardar_datos(jms)
    else:
        print("NO esiste")

modificar()

