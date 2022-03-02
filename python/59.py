"""
Contar todas las letras
"""

frase = "Poncho esta aprendiendo a programar con videos de youtube"

letras = "abcdefghijklmnñopqrstivwxyz"

conteo = dict.fromkeys(letras, 0)

for letra in frase.lower():
    if letra in conteo:
        conteo[letra] += 1

for k, v in conteo.items():
    print("{}: {}".format(k, v))