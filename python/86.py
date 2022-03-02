"""
Fernanda Chavez 
2A
"""

ajedrez = [["T","P",".",".",".",".","P","T"],
			["C","P",".",".",".",".","P","C"],
			["A","P",".",".",".",".","P","A"],
			["D","P",".",".",".",".","P","R"],
			["R","P",".",".",".",".","P","D"],
			["A","P",".",".",".",".","P","A"],
			["C","P",".",".",".",".","P","C"],
			["T","P",".",".",".",".","P","T"]]


for i in range(8):
    for j in range(8):
        print(ajedrez[i][j], end = " ")
    print()

while True:

	print("Ingresa las cordenadas del elemento a mover: ")
	f1 = int(input("Fila: "))
	c1 = int(input("Columna: "))

	print("Ingresa las cordenadas de la nueva ubicacion")
	fn1 = int(input("Fila: "))
	cn2 = int(input("Columna: "))

	if ajedrez[fn1][cn2] == ".":

		ajedrez[fn1][cn2] = ajedrez[f1][c1]
		ajedrez[f1][c1] = "."
	else:
		print("Error!! no se puede agregar el elemento")
		print("La posicion esta ocupada")



	for i in range(8):
		for j in range(8):
			print(ajedrez[i][j], end = " ")
		print()



	opcion = input("Deseas seguir jugando S/N:   ")
	if opcion == "n":
		break




	