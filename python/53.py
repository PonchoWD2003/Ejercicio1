"""
Diccionario a lista
"""

pares = {"A":1, "B": 2, "C": 3, "D": 4, "E": 5}
c = []
v = []
for clave, valor in pares.items():
    
    c.append(clave)
    v.append(valor)

print(c)
print(v)

#Convertir las listas en diccionario

diccionario = dict(zip(c, v))
print(diccionario)