"""
Programa que elimina los elementos repetidos de una lista, quedando
solo elementos unicos, no repetidos.
"""

data = [1,2,3,2,5,3,4,6,5,7,8]
resultado = []

for i in data:

    if i not in resultado:
        resultado.append(i)

print(resultado)