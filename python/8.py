tabla = [["Cuadrados", 6, [3,1]],
            ["Circulos", 5, [1,2]],
            ["Triangulos", 4, [2, 2]],
            ["Rectangulos", 3, [4,3] ]]

tabla[0][1] = 5
tabla[0][2] = [1, 3]
tabla[3][2] [0] = 2

for i in tabla:

    print("{:12}   -Cantidad: {:2}  -> Columna {}. Fila{} ".format(i[0], i[1], i[2], i[2][0], i[2][1]))
