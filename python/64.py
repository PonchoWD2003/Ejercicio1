"""
Repetir codigo hasta que sea numero entero
"""


from tkinter.tix import INTEGER


while True:

    try:
        numero = int(input("Ingresa un numero: "))
        
    
    except ValueError:
        print("Introduce un numero entero")
    
    else:

        if numero >= 18:
            print("Eres mayor de edad")
        else:
            print("Eres menor de edad")
        
        break