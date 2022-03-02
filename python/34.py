"""
Hacer un programa que compruebe si un número es múltiplo de otro, 
mediante una función que contenga dos sentencias return.
"""

def si_no(num, mul):

    if num % mul == 0:
        return True

    return False

numero = int(input("Ingresa un numero: "))
multiplo = int(input("Ingresa un multiplo: "))

if si_no(numero, multiplo):

    print("Es multiplo")
else:
    print("No es multiplo")



