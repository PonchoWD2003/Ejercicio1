"""
inventario de letras cajonera
"""

cajonera = [
            [[["A", 6],["B",3],["C", 3],["D", 4],["E", 6]],
            [["F",7],["G",1],["H",6],["I", 5],["J",6]],
            [["K", 4],["L", 5],["M",5],["N",9],["Ñ",8]]],

            [[["O", 6],["P",3],["Q", 3],["R", 4],["S", 6]],
            [["T",7],["U",1],["V",6],["W", 5],["X",6]],
            [["Y", 4],["Z", 5],[" ",0],[" ",0],[" ",0]]],
            
            ]


print("Cajon")
print()


while True:

    print()
    print("1. Mostrar inventario")
    print("2. Venta de letra")
    print("3. Resposicion de letra")
    print("4. Salir")

    opcion = input("---> ")

    if opcion == "1":

        for cajon in cajonera:
            for fila in cajon:
                for espacio in fila:
                    print("{} : {}    ". format(espacio[0], espacio[1]), end="")
        
                print()
            print()

    elif opcion == "2":

        letra = input("Que letra deseas comprar: ")
        cantidad = int(input("Ingresa la cantidad de letras: "))
        for cajon in cajonera:
            for fila in cajon:
                for espacio in fila:
                    
                    if espacio[0] == letra:
                        espacio[1] -= cantidad
    
    elif opcion == "3":

        letra = input("Que letra deseas recuperar: ")
        cantidad = int(input("Ingresa la cantidad de letras: "))
        for cajon in cajonera:
            for fila in cajon:
                for espacio in fila:
                    
                    if espacio[0] == letra:
                        espacio[1] += cantidad

    else:
        print("Salir")
        break
