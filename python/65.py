"""
Programa de division con excepciones
"""
try: 
    dividendo = float(input("Introduce un dividendo: "))
    divisor = float(input("Introduce el divisor: "))

    resultado = dividendo/divisor

except ValueError:
    print("Dato invalido")

except ZeroDivisionError:
    print("No se puede dividir entre cero.")

else:
    print(resultado)