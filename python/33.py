"""
Hacer un programa con una función para calcular la nota de cualquier examen en general.
Es decir, que calcule la nota (en base a 10 puntos) de un examen que puede tener cualquier 
cantidad de puntos, y por cada fallo se reste cualquier cantidad de puntos.
"""


def calcula_nota(aci, pre, quita):

    punto = 10/pre
    nota = (aci * punto) - (pre - aci) * quita

    return nota

preguntas = int(input("Intoduce el numero de preguntas: "))
aciertos = int(input("Intoduce le numero de aciertos: "))
quita_fallos = int(input("Introduce quitar fallos: "))
nota = calcula_nota(aciertos, preguntas, quita_fallos)

print(nota)