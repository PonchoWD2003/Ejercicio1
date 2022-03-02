"""
Programa que elimina todos los meses que tengan la letra b
"""

meses = ["enero", "febrero", "marzo", "abril",
            "mayo", "junio", "julio", "agosto",
            "septiembre", "octubre", "noviembre", "diciembre"]

nuevo = tuple(meses)

for i in nuevo:
    
    if "b" in i:

        meses.remove(i)

print(meses)