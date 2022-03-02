from persona import Persona
from zombi import Zombi
import os

os.system("clear")

print()
print(" La ciudad se ha llenado de zombis.")
print(" Estas en la calle 1 y has de llegar.")
print(" a la calle 40 para poder salvarte.")
print()
print(" Los zombis avanzan 1, 2 o 3 calles.")
print("Tu puedes avanzar 1, 2 o 3  calles.")
print()

nombre = input(" ¿Estas preparado? Cual es tu nombre: ").capitalize()

##Creamos el objeto de la clase persona
jugador = Persona(nombre)

##Creamos los zombis
horda = []
for i in range(10):
    z = Zombi()
    horda.append(z)

while True:

    os.system("clear")
    print(jugador.situacion())


    calles = []
    for zombi in horda:
        calles.append(zombi.calle)

    calles.sort()
    print("Hay zombis en las calles:")
    for elemento in calles:
        print(elemento, end="")
    
    print()
    print()

    if jugador.calle > 40:
        print(" No te ha visto ningun zombi.")
        print(" Te has librado de ser comido.")
        print()
        break

    
    comido = False
    for zombi in horda:
        if zombi.calle == jugador.calle:
            comido = True

    
    if comido:
        print(" Un zombi te acaba de ver.")
        print(" Te va a comer. Se acabo el juego.")
        print()
        break


    velocidad = ""
    while velocidad not in ("1","2","3"):
        velocidad = input(" Cuanto quieres correr(1/2/3): ")
    jugador.moverse(velocidad)

    for z in horda:
        z.moverse()