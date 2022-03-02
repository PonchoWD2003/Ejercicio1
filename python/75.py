lista1 = [1, 12, 123]
lista2 = ["Bye", "Ciao", "Agur", "Adieu"]

# completa el ejercicio
lista1.append(1234)
lista1.append("Hola")
print(lista1)

lista2.append("Adios")
lista2.append(1234)
print(lista2)

lista3 = lista1[:-1]
print(lista3)

lista4 = lista2[1:-1]
print(lista4)

lista5 = lista4+lista3
print(lista5)