"""
Crear una agenda telefonoca usando diccionarios
"""

telefonos = {"Andres": 4565464, 
            "Pedro": 665845,
            "Octavio": 64522,
            "Flavio": 534654}

while True:

    print()
    print("---Agenda---")
    print("1. Consultar por nombre")
    print("2. Consultar por telefono")
    print("3. Listar toda la agenda")
    print("4. Salir")
    print()
    op = input("Elige una opcion: ")

    if op == "1":

        nombre = input("Nombre: ")
        telf = telefonos.get(nombre, "Ese nombre no existe")
        print("{}: {}".format(nombre, telf))        

    elif op == "2":

        tel = input("Telefono: ")

        if tel in telefonos.values():
            for nombre in telefonos:
                if telefonos[nombre] == telf:
                    print("{}: {}".format(telf, nombre))
        else:
            print("Ese telefono no esta en la agenda")    


    elif op == "3":

        print("---Agenda---")
        for clave, valor in telefonos.items():
            print(" {}: {} ".format(clave, valor))
    
    elif op == "4":
        print("Saliendo")
        break
        
    
    else:
        print("Ingresa una opcion valida")
