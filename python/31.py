"""
Haz un programa con una función que muestre un saludo, 
dando la bienvenida al usuario, utilizando su nombre, el cual se 
ha de pedir antes de llamar a la función.

Esta función no devuelve ningún valor específico, sino que devuelve 
el valor None. Definir la función con un parámetro (el nombre del usuario).
"""


from re import I


def ejemplo(nom):

    print("******************************************")
    print("*                                        *")
    print("*        PANTALLA DE INICIO              *")
    print("*      Bienvenido al sistema             *")
    print("*                                        *")
    print("              ",nom,"                     ")
    print("*                                        *")
    print("******************************************")


    return None



nombre = input("Ingresa tu nombre: ")
print(ejemplo(nombre))



