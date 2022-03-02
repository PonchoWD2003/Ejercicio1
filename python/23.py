"""
Numeros palindromos
"""


inicio = 10000
final = 12000
capicuas = []

for i in range(inicio, final+1):

    cadena = str(i)
    reverso = cadena[::-1]

    if cadena == reverso:
        capicuas.append(i)

print(capicuas)