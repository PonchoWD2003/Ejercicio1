
"""
    Funciones 
"""

print("Ejercicio")

def doble_triple(numero):

    doble = numero * 2
    triple = doble * 3
    return triple


numero = int(input("Ingresa un numero: "))
j = doble_triple(numero)
print(f"El resultado es: {j}")