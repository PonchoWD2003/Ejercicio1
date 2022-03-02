"""
Desifrar la contraseña de un candado de 4 rotaciones
"""


for i in range(0,10):

    for j in range(0,10):

        for k in range(0, 10):

            for m in range(0, 10):

                combinaciones = str(i) + str(j) + str(k) + str(m)
                print(combinaciones)
print()