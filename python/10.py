"""
Pasar una lista bidimensional a dos listas unidimensionales, y viceversa, 
pasar dos listas unidimensionales a una lista bidimensional.
"""

grupos = [[1,"A"],[2,"B"],[3,"C"],[4,"D"],[5,"E"],
        [6,"F"],[7,"G"],[8,"H"],[9,"I"],[0,"J"]]
numeros = []
letras = []
extra = []

for i in grupos:

    #print(i[0],i[1])

    numeros.append(i[0])
    letras.append(i[1])

print(numeros)
print(letras)


for i in range(len(numeros)):

    extra.append([numeros[i], letras[i]])


print(extra)


