
class Pelicula:

    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento

        print("Se ha credo la pelicula ",self.titulo)

    #Destructor de clase
    def __del__(self):
        print("Se esta eliminando la pelicula",self.titulo)

    def __str__(self):
        return "{} lanzada en {} con una duracion de {} minutos".format(self.titulo,self.lanzamiento,self.duracion)

p = Pelicula("El padrino",175,1972)
print(str(p))