"""
Crear una baraja
"""

tantos = ["A", "2", "3", "4", "5", "6", "7", "S", "C", "R"] 
palos = ["oros", "copas", "espadas", "bastos"]

baraja=[]

for t in tantos:

    for b in palos:

        carta = "{} de {} ".format(t, b)
        baraja.append(carta)

for i in range(0, 40, 4):

    for j in range(4):
        print("{}".format(baraja[i+j]), end = " ")
    print()