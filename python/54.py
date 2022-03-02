"""
Contador de letras
"""
frase = "Ponchito esta aprendiendo programacion con videos de youtube"

conteo = {}

for letra in frase.lower():
    if letra not in conteo:
        conteo[letra] = 1
    else:
        conteo[letra] += 1

for clave, valor in conteo.items():

    print("{}: {}".format(clave, valor))