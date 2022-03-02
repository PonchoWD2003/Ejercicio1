"""
Define una funcion que devuelva el que sea intermedio de los 3
"""

def num_intermedio(a,b,c):

    if a < b < c or c < b < a:
        return b
    elif b < a < c or c < a < b:
        return a
    
    elif  a < c < b or b < c < a:
        return c
    
    elif a == b or a == c:
        return a
    elif b == c:
        return b

 

print("Ingresa 3 numeros: ")
n1 = int(input())
n2 = int(input())
n3 = int(input())
res = num_intermedio(n1, n2, n3)
print(res)