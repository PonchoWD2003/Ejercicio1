"""
Haz un programa, que dada una lista con datos, informa del número de datos de esa lista, y 
pide el número de datos de esa lista que se van a mantener.

A continuación se mantienen ese número de datos y se elimina el resto de datos de la lista.
(Usar la sentencia del)
"""

datos = [1.12, 2.18, 1.45, 2.21, 3.07, 2.32, 3.41, 1.39]

mantener = int(input("Ingresa hasta que indice deseas mantener: "))


del datos[mantener:]

for i in range(len(datos)):
    print(f"Los datos son: {datos[i]}")