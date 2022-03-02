"""
Proyecto final convercion de unidades
Jose Alfonso Alvarado Peña 2B
"""
#OS para limpiar la pantalla
import os

menu = ["1. Metros a Pulgadas", "2. Pies a Millas", 
            "3. Cm a Yardas", "4. Galones a Litros", "5. km/h a m/s", 
            "6. cm2 a m2", "7. mill/h  a  pies/seg", "8. pesos Mex a Dlls", 
            "9. Pie a Pulgada", "10. Celsius a Fahrenheit" , "11. Salir"]



os.system("clear")

print("******************************************")
print("*                                        *")
print("*        PANTALLA DE INICIO              *")
print("*      Bienvenido al sistema             *")
print("*                                        *")
print("*      CONVERSION DE UNIDADES            *")
print("*                                        *")
print("******************************************")

input()

os.system("clear")

#Funciones para realizar las operaciones
def opp1(m):
    return m * 39.37

def opp2(p):
    return  p / 5280

def opp3(cm):
    return cm * (1/100)*(1/0.9144)

def opp4(gal):
    return gal * (3.785/1)

def opp5(kmh):
    return kmh * (1000/1) * (1/3600)

def opp6(cmc):
    return cmc * (1/10000)

def opp7(mi):
    return mi * (1/3600) * (5280/1)

def opp8(pe):
    return (pe * 1)/20

def opp9(pie):
    return pie * (12/1)

def opp10(cel):
    return (cel *1.8) +32



#Ciclo para relizar le programa hasta que el usuario quiera salir


while True:

    print("----Menu----")
    print("Elije una opcion")

    for i in menu:

        print(i)


    opcion = input("Elije una opcion: ")

    os.system("clear")

    #Condiciones para procesar la opcion

    if opcion == "1":

        print("Metros a Pulgadas")
        metros = float(input("Ingres los metros a convertir: "))
        print("{} Metros equivalen a: {:.3f} ft".format(metros, opp1(metros)))
        input()
        os.system("clear")


    elif opcion == "2":

        print("Pies a Millas")
        pies = float(input("Ingres los pies convertir: "))
        print("{} Pies equivalen a: {:.3f} Millas".format(pies, opp2(pies)))
        input()
        os.system("clear")

    elif opcion == "3":
    
        print("Cm a Yardas")
        cm = float(input("Ingres los cm a convertir: "))
        print("{} Cm equivalen a: {:.3f} Yardas".format(cm, opp3(cm)))
        input()
        os.system("clear")


    elif opcion == "4":
    
        print("Galones a Litros")
        galones = float(input("Ingres los galones a convertir: "))
        print("{} Galones equivalen a: {:.3f} Lts".format(galones, opp4(galones)))
        input()
        os.system("clear")

    elif opcion == "5":
    
        print("km/h  a  m/s")
        kmh = float(input("Ingres los km/h a convertir: "))
        print("{} Km/h equivalen a: {:.3f} M/s".format(kmh, opp5(kmh)))
        input()
        os.system("clear")

    elif opcion == "6":
    
        print("Cm2 a m2")
        cmc = float(input("Ingres los cm2 a convertir: "))
        print("{} Cm2 equivalen a: {:.3f} m2".format(cmc, opp6(cmc)))
        input()
        os.system("clear")

    elif opcion == "7":

        print("Millas/hora  a  Pies/segundos")
        mill_h = float(input("Ingres las mill/h a convertir: "))
        print("{} Millas/h equivalen a: {:.3f} Pies/seg".format(mill_h, opp7(mill_h)))
        input()
        os.system("clear")

    elif opcion == "8":

        print("Pesos Mex a Dlls")
        pesos = float(input("Ingres los pesos a convertir: "))
        print("{} Pesos equivalen a: {:.3f} Dlls".format(pesos, opp8(pesos)))
        input()
        os.system("clear")

    elif opcion == "9":

        print("Pies a Pulgadas")    
        pies = float(input("Ingres los pies a convertir: "))
        print("{} Pies equivalen a: {:.3f} Pulgadas".format(pies, opp9(pies)))
        input()
        os.system("clear")

    elif opcion == "10":

        print("Grados Celsius a Fahrenheit")
        celsius = float(input("Ingres los grados Celsius a convertir: "))
        print("{} Celsius equivalen a: {:.3f} Fahrenheit".format(celsius, opp10(celsius)))
        input()
        os.system("clear")

    elif opcion == "11":
        print("Saliendo")
        break

    else:
        print("Esa opcion no existe")
        print("Ingresa una opcion valida")
        input()
        os.system("clear")