"""
Resolver la suma de martices
"""

from operator import le


a = [[32,32,66,4],
    [32,75,34,2],
    [44,54,23,44],
    [47,9,5,33,4]]

b = [[32,32,66,4],
    [32,75,34,2],
    [44,54,23,44],
    [47,9,5,33,4]]

def sumar_matrices(m1, m2):

    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        
        m3 = []
        for i in range(len(m1)):
            m3.append([])
            for j in range(len(m1[0])):
                m3[i].append(m1[i][j] + m2[i][j])
        return m3

    else:
        return None

m3 = sumar_matrices(a,b)

if m3 == None:
    print("No se puede sumar")
else:
    for fila in m3:
        print("[", end = " ")
        for elemento in fila:
            print("{}".format(elemento), end = " ")
        
        print("]")

print()