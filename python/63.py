"""
Excepciones
"""
try:
    numero = int(input("Edad: "))
    if numero >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")

except ValueError: 
    print("Valor invalido!")



try: 
    numero = int(input("Edad: "))

except ValueError: 
    print("Valor invalido!")

else:
    if numero >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")