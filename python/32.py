"""
Calculo de nota final
"""


def calcula_nota(aci):
    nota = (aci * 0.25) - (40 - aci) * 0.10

    return nota


aciertos = int(input("Intoduce le numero de aciertos: "))
nota = calcula_nota(aciertos)

print(nota)



