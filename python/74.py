# Variables del ejercicio (no las modifiques)
cadena_corrupta = "airotsiH,6.7,aícraG nómaR"

# Completa el ejercicio

cadena_volteada = cadena_corrupta[::-1]

nota = cadena_volteada[13:16] 
materia = cadena_volteada[-8:]
nombre = cadena_volteada[:12]

print("{} ha sacado una {} en {}".format(nombre, nota,materia))