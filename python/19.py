"""
En este reto partimos de los retos 2 y 3 del nivel 12. Partimos de una baraja que creamos y 
mostramos en filas.
Ahora se trata de repartir 5 cartas a 4 jugadores, y luego mostrar las manos de 
los jugadores y también mostrar el resto de cartas de la baraja sin repartir. 
"""

import random

tantos = ["A", "2", "3", "4", "5", "6", "7", "S", "C", "R"]
palos = ["oros", "copas", "espads", "bastos"]
baraja = [] 

for t in tantos:
    for p in palos:
        carta = "{} de {}".format(t,p)
        baraja.append(carta)

random.shuffle(baraja)

##---------------------

jugador1 = []
jugador2 = []
jugador3 = []
jugador4 = []

for i in range(5):
    carta1 = baraja.pop(0)
    jugador1.append(carta1)

    carta2 = baraja.pop(0)
    jugador2.append(carta2)

    carta3 = baraja.pop(0)
    jugador3.append(carta3)

    carta4 = baraja.pop(0)
    jugador4.append(carta4)


jugadores = [jugador1, jugador2, jugador3, jugador4]

for i in range(4):
    print("Jugador {}: ".format(i+1))
    for j in range(5):
        print("{:16}".format(jugadores[i][j]), end="")
    print()
print()


for i in range(0, 20, 40):
    for j in range(4):
        print("{:14}".format(baraja[i+j]), end= " ")
    print()
print()