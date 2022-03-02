"""
Mayor y menor de una lista 
"""

#numeros = [29,43,5,74,2,55,39,22,6,99]
numeros = [-33,55,-55,-5,-71,-3,31,8]
max = max(numeros)
min = min(numeros)

print("Maximo: {} y Minimio: {} ".format(max, min))

mayor = None
menor = None
for i in numeros:


    if mayor == None or i > mayor:
        mayor = i
    elif menor == None or i < menor:
        menor = i

print("Maximo: {} y Minimio: {} ".format(mayor, menor))