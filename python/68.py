"""
Matriz
"""


consumo = [[21,18.75,35,40],
            [19,11,21,14],
            [12,5,20,30.8]]


for lista in consumo:
    print("[", end = " ")
    for elemento in lista:
        print("{:8.2f}".format(elemento), end = " ")
    print("]")