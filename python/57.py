"""
Guardar registro de los paises
"""

prefijos = {
    "COLOMBIA": 65,
    "ARGENTINA": 44,
    "PERU": 33,
    "MEXICO": 65,
    "BOLIVIA": 85,
    "CHILE": 44,
    "ESPAÑA": 62,
    "ECUADOR": 77
    }

print("Prefijos internacionales")
print("\"q\" salir")

contador = {}

while True:

    pais = input("Pais: ").upper()

    if pais == "Q":
        break


    acumulacion = prefijos.get(pais, "No disponible")
    print("{}: {}".format(pais, acumulacion))

    ##Conteo de los elementos
    contador.setdefault(pais, 0)
    contador[pais] += 1

    print("Registro de busquedas")
    for k, v in contador.items():
        print("{}: {}".format(k, v))
