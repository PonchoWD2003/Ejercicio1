import ipaddress, os
###Ingresar la direcicion en el siguiente formato xxx.xxx.xxx.xxx/xx
##Las x son los numeros de la ip

def host(ip):
    fin = ip[-2:]
    ceros = 32 - int(fin)
    host = 2**ceros - 2
    print(f"Numero de Host: {host}")

def no_subR(ip):
    fin = ip[-2:]
    cadena = ip[:-3]
    print(f"IP: {cadena}")

    ##Scacar en clase esta la cadena
    v1 = []
    result = cadena.split(".")
    for x in result:
        v1.append(x)

            #Convercion a valores de binario
    lista_bin = []
    for f in v1:
        resB = "{0:b}".format(int(f))
        lista_bin.append(resB)
    


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


def datos_Ip(ip):
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



def menu():
    os.system("clear")
    print("      --- CALCULADORA SUBNETEO ---     ")
    print("        --         IPv4  --        ")
    print("                n = salir           ")

while True:
    menu()
    ip = input("    Ingreasa la IP con prefijo:\n \t ")
    host(ip)
    no_subR(ip)
    datos_Ip(ip)
    s = input().lower()

    if  s == "n":
        break
    else:
        os.system("clear")

