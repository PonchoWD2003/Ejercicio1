import pprint

cantidad1=5
cantidad2=3
cantidad3=4

#Declarar matriz tridimensional
matriz_3d= [[[0 for i in range(cantidad1)] for j in range(cantidad2)] for k in range(cantidad3)]

#Mostrar matriz tridimensional
print('\n Mostrar matriz tridimensional con "pprint":')
pprint.pprint(matriz_3d)

print('\n Mostrar matriz tridimensional con "print":')
print(matriz_3d)

print('\n Ejemplo 1 de recorrido:')
# Ejemplo 1 de recorrido en matriz tridimensional
for k in matriz_3d:
    for j in k:
        for i in range(len(j)):
            j[i]=i
pprint.pprint(matriz_3d)

print('\n Ejemplo 2 de recorrido:')
# Ejemplo 2 de recorrido en matriz tridimensional
for k in matriz_3d:
    print(k)
    for j in k:
        print(j)
        for i in j:
            print(i)

print('\n Cambiar valores 1:')
#Cambiar valores 1
matriz_3d[0][0][0]="Primera posición"
pprint.pprint(matriz_3d)

print('\n Cambiar valores 2:')
#Cambiar valores 2
matriz_3d[3][2]=['p1','p2','p3','p4','p5']
pprint.pprint(matriz_3d)

print('\n Acceder a una posición:')
#Acceder a una posición
print(matriz_3d[0][0][0])