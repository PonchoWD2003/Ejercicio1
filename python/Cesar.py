"""
Algoritmo de cifrado de CESAR
Modelo basico

Este metodo conciste en desplazar los caracteres por ejemplo en el abecedario 
tenemos una letra ejemplo la p a esta le desplasamos cierta cantidad de caracteres por 
ejemplo 2 el resultado sera la letra que esta en esa posicion.

P = R
p = r

"""

from string import ascii_lowercase, ascii_uppercase

def cifrado_cesar(texto_og, pasos):
    
    resultado = []


    for i in texto_og:

        if i in ascii_lowercase:
            
            indice = ascii_lowercase.index(i)
            nuevo_indice = (indice + pasos) % len(ascii_lowercase) 
            resultado.append(ascii_lowercase[nuevo_indice])

        elif i in ascii_uppercase:
            
            indice = ascii_uppercase.index(i)
            nuevo_indice = (indice + pasos) % len(ascii_uppercase) 
            resultado.append(ascii_uppercase[nuevo_indice])

        else: 

            resultado.append(i)
    
    return "".join(resultado)


texto = input("Ingresa el texto: ")
despl = int(input("Caracteres a desplazar: "))
res = cifrado_cesar(texto, despl)

print(res)