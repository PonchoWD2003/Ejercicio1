"""
Operacion de estudio de direccion IP

-Evaluar que clase es la ip para de ahi asignar los valores de la mascara por ejemolo
si es clase A se asignan 8 bits encendidos, clase B se signan 16 bits , clase C 24 bits y por
ultimo los 32 bits

"""
import ipaddress 

ip = input("Ingresa una direccion IP y prefijo: ")

##Mascara
fin = ip[-2:]

##Procesar cadena
cadena = ip[:-3]
print(f"IP: {cadena}")

##Scacar en clase esta la cadena
v1 = []
result = cadena.split(".")
for x in result:
    v1.append(x)
print(v1)


        #Convercion a valores de binario
lista_bin = []
for f in v1:
    resB = "{0:b}".format(int(f))
    lista_bin.append(resB)
print(lista_bin)

##Numero de host
ceros = 32 - int(fin)
host = 2**ceros - 2
print(f"Numero de Host: {host}")

##Calcular la mascara    
MAs = ipaddress.IPv4Network(ip, strict=False)
print("La mascara de subred es: ",MAs.netmask)

##Calcular primera y ultima IP
primera, segunda = MAs[1], MAs[-2]
print(f"First Address: {primera}")
print(f"Last Address: {segunda}")

##Calcular Subred
print(f"Subred: ",MAs.network_address)

#Calcular Brocast
print("Broadcast: ",MAs.broadcast_address)


lon = len(lista_bin[0])
if lon >= 1 and lon <= 7:
    print("Es clase A")
    encendidos = int(fin) - 8
    sub = 2**encendidos
    print(f"Numero de subredes: {sub}")

elif lista_bin[0].startswith("10"):
    print("Es clase B")
    encendidos = int(fin) - 16
    sub = 2**encendidos
    print(f"Numero de subredes: {sub}")

elif lista_bin[0].startswith("110"):
    print("Es clase C")
    encendidos = int(fin) - 24
    sub = 2**encendidos
    print(f"Numero de subredes: {sub}")




