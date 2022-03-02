"""
Programa que muestre todas las posibles combinaciones 
para poder abrir un candado de clave de tres ruedas
"""

for i in range(0,10):

    for j in range(0,10):

        for k in range(0, 10):

            print("{} {} {}   ".format(i, j, k), end = "" )
        
        
print()
