
from enum import auto



##Esta es la super clase
class Producto:

    def __init__(self, referencia,nombre,pvp,descripcion):

        self.referencia = referencia
        self.nombre = nombre 
        self.pvp = pvp
        self.descripcion = descripcion

    def __str__(self):
        return """\
REFERENCIA \t{}
NOMBRE \t\t{}
PVP \t\t{} 
DESCRIPCION \t{}""".format(self.referencia, self.nombre, self.pvp, self.descripcion)

class Adorno(Producto):
    pass

class Alimento(Producto):
    productor = ""
    distribuidor = ""

    def __str__(self):
        return """\
REFERENCIA\t{}
NOMBRE\t\t{}
PVP\t\t{} 
DESCRIPCION\t{}
PRODUCTOR\t{}
DISTRIBUIDOR\t{}""".format(self.referencia, self.nombre, self.pvp, self.descripcion, self.productor, self.distribuidor)


class Libro(Producto):
    isbn = ""
    autor = ""

    def __str__(self):
        return """\
REFERENCIA\t{}
NOMBRE\t\t{}
PVP\t\t{} 
DESCRIPCION\t{}
ISBN\t\t{}
AUTOR\t\t{}""".format(self.referencia, self.nombre, self.pvp, self.descripcion, self.isbn, self.autor)


#a = Adorno(234,"Vaso",5434, "De porcelana")
#print(a)


#al = Alimento(232,"Aceite", 54,"250Ml")
#al.productor = "La aceitera"
#al.distribuidor = "Comex"
#print(al)


li = Libro(2132,"Mero tu version",55,"Superacion personal")
li.isbn = 32342
li.autor = "Ponchito"
print(li)