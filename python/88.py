"""
Practica hoteles
Mauricio
"""
import random

edificio1 = [[[random.choice([True, False]) for k in range(5)]for j in range(3)]for i in range(3)]
edificio2 = [[[ random.choice([True, False]) for k in range(5)]for j in range(3)]for i in range(3)]
edificio3 = [[[ random.choice([True, False]) for k in range(5)]for j in range(3)]for i in range(3)]

print("----Cadena de hoteles Mauricio----")
print("Hotel 1 \nHotel 2 \nHotel 3 \n ")

while True:
    hot = int(input("En que hotel te deseas hospedar: "))

    if hot == 1: 

        piso = int(input("En que piso te deseas quedar: "))
        habitacion = int(input("En que habitacion te deseas hospedar: "))

        if edificio1[hot][piso][habitacion] == True:
            print("Habitacion disponible")
            edificio1[hot][piso][habitacion] = "False"
            print("La habitacion ser resevo")
        else:
            print("Habitacion reservada")
            print("No te puedes quedar en dicha habitacion")
            print("Elije otra")

    elif hot == 2: 

        piso = int(input("En que piso te deseas quedar: "))
        habitacion = int(input("En que habitacion te deseas hospedar: "))

        if edificio1[hot][piso][habitacion] == True:
            print("Habitacion disponible")
            edificio1[hot][piso][habitacion] = "False"
            print("La habitacion ser resevo")
        else:
            print("Habitacion reservada")
            print("No te puedes quedar en dicha habitacion")
            print("Elije otra")

    elif hot == 3: 

        piso = int(input("En que piso te deseas quedar: "))
        habitacion = int(input("En que habitacion te deseas hospedar: "))

        if edificio1[hot][piso][habitacion] == True:
            print("Habitacion disponible")
            edificio1[hot][piso][habitacion] = "False"
            print("La habitacion ser resevo")
        else:
            print("Habitacion reservada")
            print("No te puedes quedar en dicha habitacion")
            print("Elije otra")


    salir = input("Deseas seguir ejecutando el codigo S/N: ").lower()
    if salir == "n":
        break
