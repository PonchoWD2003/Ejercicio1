"""
Calcular raiz cuadrada en pithon
"""


import math

try:
    numero = float(input("Ingresa un numero: "))
    res = math.sqrt(numero)

except ValueError:
    print("Ingresa un dato valido")

else:
    print(f"Resultado: {res}")
