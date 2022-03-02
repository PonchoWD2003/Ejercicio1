"""
En una tienda quieren hacer un inventario de las figuras que tienen y el número de unidades de cada una. Crea una lista anidada que contenga los datos del inventario:
6 cuadrados, 5 círculos, 4 triángulos y 3 rectángulos.

"""


tabla = [["Cuadrados", 6, [3,1]],
            ["Circulos", 5, [1,2]],
            ["Triangulos", 4, [2, 2]],
            ["Rectangulos", 3, [4,3] ]]

tabla[0][1] = 5
tabla[0][2] = [1, 3]
tabla[3][2] [0] = 2

for i in tabla:

    print("{:10}: {:2}: {}".format(i[0], i[1], i[2]))
