

def menu():
    list = ["1.para añadir usuario","2.para modificar un usuario", "3.para eliminar usuario","4.para salir"]
    while True:
        print("--Porfavor elije una de las siguientes opcciones--")
        for i in list:
            print(i)
        opc = int(input("->"))
        if opc == 1:
            print("accediendo")
        elif opc == 2:
            print("accediendo")
        elif opc == 3:
            print("accediendo")
        elif opc == len(list):
            print("------saliendo------")