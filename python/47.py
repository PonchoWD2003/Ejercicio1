"""
Jose Alfonso Alvarado Peña
2A
Programa que calcula el ISR
"""
import os

def bienvenida():

    os.system("clear")

    print("******************************************")
    print("*                                        *")
    print("*        PANTALLA DE INICIO              *")
    print("*      Bienvenido al sistema             *")
    print("*                                        *")
    print("*          CALCULO DE ISR                *")
    print("*                                        *")
    print("******************************************")

    input()

    os.system("clear")



bienvenida()

while True:

    try:
        mensualidad = float(input("Ingresa el salario mensual a calcular: "))
    except ValueError:
        print("Ingresa una cantidad valida")
    else:


        if mensualidad >= 0.1 and mensualidad <= 644.58:
            print("Monto a pagar: 0.0 pesos")
            input()
            os.system("clear")

        elif mensualidad >= 644.59 and mensualidad <= 5470.92:
            
            v = (mensualidad - 644.54) * 0.064
            s = v + 12.38
            print("Monto a pagar: {:.2f} pesos".format(s))
            input()
            os.system("clear")

        elif mensualidad >= 5470.93 and mensualidad <= 9614.66:
            
            v = (mensualidad - 5470.93) * 0.1088
            s = v + 321.26
            print("Monto a pagar: {:.2f} pesos".format(s))
            input()
            os.system("clear")


        elif mensualidad >= 9614.67 and mensualidad <= 1117.62:
            
            v = (mensualidad - 9614.67) * 0.16
            s = v + 772.10
            print("Monto a pagar: {:.2f} pesos".format(s))
            input()
            os.system("clear")

        elif mensualidad >= 1117.63 and mensualidad <= 13381.47:
            
            v = (mensualidad - 1117.63) * 0.17
            s = v + 1022.01
            print("Monto a pagar: {:.2f} pesos".format(s))
            input()
            os.system("clear")

        elif mensualidad >= 13381.48 and mensualidad <= 26988.50:
            
            v = (mensualidad - 13381.48) * 0.21 
            s = v + 1417.12
            print("Monto a pagar: {:.2f} pesos".format(s))
            input()
            os.system("clear")

        elif mensualidad >= 26988.51 and mensualidad <= 42537.58:
            
            v = (mensualidad - 26988.51) * 0.23
            s = v + 4323.58
            print("Monto a pagar: {:.2f} pesos".format(s))
            input()
            os.system("clear")

        elif mensualidad >= 42537.59 and mensualidad <= 81211.25:
            
            v = (mensualidad - 42537.59) * 0.3
            s = v + 7980.73
            print("Monto a pagar: {:.2f} pesos".format(s))
            input()
            os.system("clear")

        elif mensualidad >= 81211.26 and mensualidad <= 108281.67:
            
            v = (mensualidad - 82111.26) * 0.32
            s = v + 19582.83
            print("Monto a pagar: {:.2f} pesos".format(s))
            input()
            os.system("clear")

        elif mensualidad >= 108281.68 and mensualidad <= 324845.01:
            
            v = (mensualidad - 108281.68) * 0.34
            s = v + 28245.36
            print("Monto a pagar: {:.2f} pesos".format(s))
            input()
            os.system("clear")

        else:
            
            v = (mensualidad - 324845.02) * 0.35
            s = v + 101876.90
            print("Monto a pagar: {:.2f} pesos".format(s))
            input()
            os.system("clear")

        print("Deseas calcular otro ISR ??")
        op = input("S / N : ").lower()
        if op in "s":
            os.system("clear")
            continue
            
        else:
            print("Saliendo")
            break
    
    
        