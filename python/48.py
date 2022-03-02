"""
Diccionarios
"""
telefonos = {"Martin": 12345, 
            "Pedro": 547675, 
            "Andres": 325647,
            "Lucia": 54654}


if "Julia" in telefonos:
    print(telefonos["Julia"])
else:
    print("Esa clave no existe")

telefonos["Jorge"] = 654544
print(telefonos)

telefonos["Pedro"] = 55555
print(telefonos)

del telefonos["Martin"]
print(telefonos)