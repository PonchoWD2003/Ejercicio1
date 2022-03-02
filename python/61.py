"""
Saldar deuda diccionario
"""

deudas = {
            "Jorge": 12,
            "Marco": 10,
            "Pedro": 8, 
            "Antonio": 4
            }

total = sum(list(deudas.values()))

while True:

    print("1. Saldar deuda")
    print("2. Ver entradas")
    print("3. Ver total deuda")
    print("4. Salir")

    op = input("Elige una opcion: ")

    if op == "1":
        nombre = input("Nombre: ")
        if nombre not in deudas:
            print("No hay deuda para ese nombre")
        else:
            saldo = deudas.pop(nombre)
            total =- saldo
            print("Deuda saldada {}".format(saldo))


    elif op == "2":
        for nombre, deuda in deudas.items():
            print("{:8}: {:4d}".format(nombre, deuda))

    elif op == "3":
        print("Deuda total: {}".format(total))

    elif op == "4":
        print("Saliendo")
        break

    else: 
        print("Ingresa una opcion valida")