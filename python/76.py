nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = int(input("Edad: "))
magico = float(input("Magico: "))

print("{} {} Tu numero de la suerte es {:.2f}".format(nombre, apellido, edad*magico))