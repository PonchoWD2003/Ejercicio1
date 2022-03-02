"""
Crear matriz con los elementos que le metamos
"""

filas = int(input("Ingresa el numero de filas: "))
columnas = int(input("Ingresa el numero de columnas: "))

matriz = []

for i in range(filas):
    matriz.append([0] * columnas)
    for j in range(columnas):
        valor = float(input("Fila {}, Columna {} :".format(i+1, j+1)))
        matriz[i].append(valor)


print()

for fila in matriz:
    print("[", end = " ")
    for elemento in fila:
        print("{}".format(elemento), end = " ")
    
    print("]")

print()
