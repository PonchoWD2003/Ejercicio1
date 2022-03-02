"""
Simulacion de calculadora
"""

def suma(n1, n2):
    return n1 + n2

def resta(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

def menu():

    print("+")
    print("-")
    print("/")
    print("*")
    op = input("Elige la operacion: ")

    if op == "+":
        n1 = float(input())
        n2 = float(input())
        print("{}".format(suma(n1, n2)))

    if op == "-":
        n1 = float(input())
        n2 = float(input())
        print("{}".format(resta(n1, n2)))

    if op == "*":
        n1 = float(input())
        n2 = float(input())
        print("{}".format(mult(n1, n2)))

    if op == "/":
        n1 = float(input())
        n2 = float(input())
        print("{}".format(div(n1, n2)))


menu()