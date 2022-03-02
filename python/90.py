

cadena = input("Inresa la cadena: ")

s = []
for i in cadena:
    s.append(i)
print(s)

bloque = 1
bloqueMaximo = 0 
acumuladoEspacios = 0
numeroBloques = 0

for elemento in range(0, len(s) -1 ): 
    
    if s[elemento] == s[elemento+1]:

        bloque += 1
        if bloque > bloqueMaximo:
            bloqueMaximo = bloque
        
    else:
        bloque = 1
        numeroBloques += 1
            

print(bloqueMaximo)


