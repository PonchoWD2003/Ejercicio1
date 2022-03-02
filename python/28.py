"""
Hace la resta las veces que indique el usuario
"""

def restas(min, sus, vec):

    l = sus * veces
    res = min - l
    return res    



minuendo = int(input("Ingresa el minuendo: "))
sustraendo = int(input("Ingresa el sustraendo: "))
veces = int(input("Numero de veces: "))

resultado = restas(minuendo, sustraendo, veces)

print(f"El resultado es: {resultado}")
