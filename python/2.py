"""
Tablas de multiplicar del 2 al 7
"""


for i in range(1, 11):
   

    for j in range(1, 8):
        resu = j * i
        print("{:2} x {:2} = {:2}    ".format(j, i, resu), end = "")
    
    print()