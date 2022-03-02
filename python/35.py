"""
Converciones 
"""

def Kg_Lb(kilo):
    return kilo * 2.2

def Lb_Kg(libra):
    return libra * 0.45





while True:

    print("----Converciones----")
    print("1. Kg a Lb ")
    print("2. Lb a Kg ")
    print("3. Salir")
    opcion = input("Elije una opion ")
    print()

    if opcion == "1":
        print("Kg a Lb")
        kg = float(input("Ingresa los kg: "))
        j=Kg_Lb(kg)
        print(f"Total: {j} Kg")

    elif opcion == "2":
        print("Lb a Kg")
        lb = float(input("Ingresa las Lb: "))
        j=Lb_Kg(lb)
        print(f"Total: {j} Lb")

    elif opcion == "3":
        print("Saliendo")
        break

    else:
        print("Esa opcion no existe")        



