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
    print("1. Consultar")
    print("2. Añadir")
    print("3. Modificar")
    print("4. Borrar")
    print("5. Salir")
    print()
    op = input("Elige una opcion: ")

    if op == "1":

        nombre = input("Nombre: ")
        if nombre not in telefonos:
            print("Este nombre no existe")
        else: 
            telef = telefonos[nombre]
            print(nombre, ":", telef)


    elif op == "2":

        nombre = input("Nombre: ")

        if nombre in telefonos:
            print("Ese nobre ya esta en la agenda")
        else: 
            telef = int(input("Telefono: "))
            telefonos[nombre] = telef
            print("El telefono se agrego con exito")

    elif op == "3":

        nombre = input("Nombre: ")
        if nombre not in telefonos:
            print("Ese nombre no existe")
        else:
            telefn = int(input("Ingresa el telefono nuevo: "))
            telefonos[nombre] = telefn
            print("El telefono se modifico con exito")
    
    elif op == "4":

        nombre = input("Nombre: ")
        if nombre not in telefonos:
            print("Ese nombre no existe!")
        else:
            del telefonos[nombre]
            print("El contacto se elimino con exito")
    
    elif op == "5":
        print("Saliendo")
        break

    else:
        print("Ingresa una opcion valida")
