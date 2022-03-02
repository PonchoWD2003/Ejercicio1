texto= "aabbba"
texto = texto[:] + '.'
print("Texto: ",texto)
total = []
ant = texto[0] 
cont = 1
cartNum = 0
for i in range(len(texto)-1):
    print(texto[i])
    if ant == texto[i+1]:
        cont+=1
    else:
        total.append(cont)
        cont = 1
        ant = texto[i+1]

for i in total:
    cartNum += max(total) - i

print("Car: ",cartNum)
print("Tot: ",total)