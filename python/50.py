inventario = {"Tornillos": 44, 
                "Tuercas": 22,
                "Clavos": 88}

articulo = input("Articulo: ")
numero = inventario.get(articulo, "No existe")

print("{}: {} ".format(articulo, numero))