"""
Proyecto de Ajedrez basico con python
Jose Alfonso Alvarado Peña
2B
"""
import os

def mesa():
    tablero = []
    ##Con estso creamos una matriz y la llenamos con puntos
    for i in range(8):
        tablero.append([])
        for j in range(8):
            tablero[i].append(".")

    return tablero

def acomodo():

    ##Aqui llamamos a la funcion anterior
    tablero = mesa()

    ##LE agregamos las piezas al ajedres

    for i in range(0,8):
        for j in range(0, 8):

            if (j == 1 or j == 6):
                tablero[i][j] = "P"

            elif (i == 0 or i == 7) and (j == 0 or j == 7):
                tablero[i][j] = "T"
            
            elif ((i == 1 or i == 6) and (j == 0 or j == 7)):
                tablero[i][j] = "C"

            elif ((i == 2 or i == 5) and (j == 0 or j == 7)):
                tablero[i][j] = "A"

            elif (i == 3 and (j == 0 or j == 7)):
                tablero[i][j] = "D"

            elif (i == 4 and (j == 0 or j == 7)):
                tablero[i][j] = "R"

    return tablero

    
tablero = acomodo()
os.system("clear")
print("   TABLERO DE AJEDREZ CON MATRICES  ")
print()

for i in range(8):
    for j in range(8):
        print(tablero[i][j], end = " ")
    print()


print("--- Que elemento deseas mover ---")
fila = int(input("Fila: "))
columna = int(input("Columna: "))

print("A que lugar deseas mover dicho elemento")
f_m = int(input("Fila: "))
c_m = int(input("Columna: "))

del tablero[fila][columna]
tablero.insert([fila][columna], ".")

del tablero[f_m][c_m]
tablero.insert([f_m][c_m], "P")


print(tablero)
