"""
Palabra con palindromo
"""
cadena = "Allí por la tropa portado, traído a ese paraje de maniobras, una tipa como capitán usar boina me dejara, pese a odiar toda tropa por tal ropilla." 
# A la cadena la dejamos "desnuda" y en minúsculas
cadena = cadena.lower().replace(",", "").replace(".", "").replace(" ", "").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u") 
# A continuación damos la vuelta a la cadena
palindromo = cadena[::-1]
print("Cadena original:", cadena)
print()
print("Cadena reversa:", palindromo)
# Comprobamos si ambas cadenas son iguales
if cadena == palindromo:
    print()
    print("Es un palíndromo")