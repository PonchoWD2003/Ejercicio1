"""

Deffie y Hellman

"""

from time import time

def g_claves():

    print("Intercanvio de clave segura mediante Diffe y Hellman \n")

    print("Hola bienvenido al sistema de generacion de clave de sesion")

    nombre=input("\n Ingresa tu nombre: ")

    print("\n Seleccion de datos Publicos \n")
    p=int(input("Hola " + nombre +" ingresa un numero primo: "))
    a=int(input( nombre +" ingresa una raiz primitiva del numero primo ingresado: "))

    print("\n Seleccion de datos Privados \n")
    cprivada=int(input(nombre + " ingresa tu clave privada: "))

    cpublica= (a**cprivada)% p
    print(nombre + " tu clave publica es: ",cpublica)


    yb=int(input("\n "+ nombre + " ingresa la clave publica de tu amigo: "))

    print("\n Clave de secion \n")

    k = (yb**cprivada)% p
    print(nombre+ " la clave de sesion es: ", k)



def desifrar_claves():

    
    

    inicio = time()

    print("--------------")
    print("Programa para calcular la clave secreta")
    print("--------------\n")
    clave = int(input("Hola ingresa la clave Publica: "))
    q= int(input("Ingresa el numero primo q: "))
    a= int(input("Ingresa el valor de la raiz primitiva: "))

    for i in range(q):
        ck = (a**i)%q
        if clave==ck:
            resultado=i
            i=q
            
    print(" \n La clave privada es: ", resultado)

    final= time()

    tiempo=(final-inicio)

    print("\n El tiempo de computo es: ",tiempo)



while True:


    print("1. Crear clave")
    print("2. Desifrar clave")
    op = input("Elige una opcion: ")

    if op == "1":
        g_claves()

    elif op == "2":
        desifrar_claves()
    
    