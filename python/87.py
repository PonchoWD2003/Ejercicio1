
"""
Juego de simulacion de ajedrez 
Al usuario le doy la opcion de elegir a cual pocision mover las piezas del tablero
y si ese lugar ya esta ocupado no podra seleccionar dicha ubicacion tendra que elegir una nueva.
En esta primera prueba no agregue lo de comerse las piezas del contrincante espero con el 
paso del tiempo ir implementando nuevas funciones. Una de esas seria agregare un grafico con 
tkinter.
Esto solo fue una prueba para manipular las matrices.

Jose Alfonso Alvarado Peña
2 A

"""

import os
os.system("clear")

##Creamos el mensaje de Bienvenida
def bienvenida():
    print("""
            ********************************
            *                              *    
            *    AJEDREZ CON MATRICES      *
            *                              *
            *        Version 1.0.0         *
            *                              *    
            *    Jose Alfonso Alvarado     *
            *                              *
            ********************************    
    """)
    input()
    os.system("clear")
##Declaramos la matriz
tablero = []
##Con estso creamos una matriz y la llenamos con puntos
for i in range(8):
    tablero.append([])
    for j in range(8):
        tablero[i].append(".")

##En estos dos for vamos iterando por filas y columnas para agregar los elementos del tablero
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

##Mandamos llamar la funcion de bienvenida
bienvenida()

##PEdimos los nombres de los 2 jugadores
print("Ingresa los nombres de los jugadores: ")
j1 = input("Jugador 1: ").strip()
j2 = input("Jugador 2: ").strip()
input()
os.system("clear")

#Aqui imprimimos el tablero antes de su modificacion
print()
print("----- Tablero -----")
print()
for i in range(8):
    for j in range(8):
        print(tablero[i][j], end = " ")
    print()

##Funcion para mover la posicion de los elementos del tablero
def jugador1(tablero):


    ##Creamos una excepcion para verificar los valores ingresados
    try:
        ##Ingresamos los valores del elemento que desea mover
        xanterior = int(input("Fila: "))
        yanterior = int(input("Columna: "))
        
        ##Agregamos los valores del nuevo lugar a donde se desea mover.
        print("A que lugar deseas mover dicho elemento")
        xfinal = int(input("Fila: "))
        yfinal = int(input("Columna: "))


        ##En este condicional es donde comparamos si un lugar esta libre
        ##en caso de estar vacio agregaremos el valor
        ##caso contrario le pediremos que ingrese una nueva cordenada
        if tablero[xfinal][yfinal] == ".":

            tablero[xfinal][yfinal] = tablero[xanterior][yanterior]
            tablero[xanterior][yanterior] = "."
        
        else:
            print("No puedes agregar la letra")
            print("Esta posicion ya esta siendo ocupada")

        ##Aqui mostramos el valor actualizado
        os.system("clear")
        print("----- Tablero -----")
        for i in range(8):
            for j in range(8):
                print(tablero[i][j], end = " ")
            print()
        
    ##El ValueError es por si ingresa un string en lugar de un entero
    except ValueError:
        print("Ingresa un dato valido")
        print("Tienes que ingresar un entero")
        #En caso de haber un error mandara llamar a la funcion de nuevo
        jugador1(tablero)
    ##Y por ultimo el index es para verificar que las cordenadas esten en el rango
    except IndexError:
        print("Ingresa un numero en el rango")
        #En caso de haber un error mandara llamar a la funcion de nuevo
        jugador1(tablero)

##Bucle para que los dos jugadores puedan estar eligiendo posisicones en la matriz
while True:	
    
    ##Preguntamos si desea seguir jugando
    op = input("¿Deseas seguir jugando? S/N  ").upper().strip()
    if op == "N":
        print("Cerrando jugada.")
        break
    else:
        print("Mueve una pieza", j1)
        print(jugador1(tablero))

        print("Mueve una pieza", j2)
        print(jugador1(tablero))

    
    

	