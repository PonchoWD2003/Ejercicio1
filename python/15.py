"""
Programa que administra una lista de la compra
"""

print("---ADMINISTRACION DE COMPRA---")
print()
compra = ["maiz", "pan", "azucar", "tortillas"]

while True:

    

    print("1. Añadir producto ")
    print("2. Eliminar producto ")
    print("3. Mostrar lista ")
    print("4. Salir ")
    opcion = input("Elige una opcion: ")
    print()

    if opcion == "1":

        elemento = input("Ingresa el elemento a añadir: ").capitalize()

        if elemento in compra:
            print("Este elemento ya esta en la lista ")
            print()
        else:
            compra.append(elemento)
            print("Elemento añadido con exito")
            print()

    elif opcion == "2":
        eliminar = input("Que elemento deseas eliminar: ").capitalize()

        if eliminar in compra:
            compra.remove(eliminar)
            print("Se elimino con exito")
            print()
        else:
            print("El elemento no esta en la lista")
            print()

    elif opcion == "3":
        for i in compra:
            print("{} ".format(i))
    elif opcion == "4":
        print("Cerrando sesion")
        break
    else: 
        print("Esta opcion no existe")