"""
Define una funcion que calcule la potencia de un numero
"""
from math import sqrt

def potencia(num):

    res = sqrt(num)
    print(f"Raiz: {res}")


numero = int(input("Ingresa un numero: "))
potencia(numero)