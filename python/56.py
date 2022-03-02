"""
metodo setdefault
"""

materiales = {"Cuadernos": 3,
                "Lapiz": 8,
                "Pluma": 3,
                "Borrador": 4}

articulo = input("Articulo: ")
unidades=materiales.setdefault(articulo, 0)

print("Hay {} unidades de {}".format(unidades, articulo))
print(materiales)