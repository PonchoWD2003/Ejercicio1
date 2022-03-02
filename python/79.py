
def ejemplo(*args):
    
    print(args)

ejemplo(324,55,22,"Hola")


def ejemplo2(**kwargs):
    
    print(kwargs)

ejemplo2(a=324,b=55,c=22,f="Hola")


def super_funcion(*args, **kwargs):
    t = 0

    for arg in args:
        t += arg

    print(f"sumatorio indetermiando es: {t}")

    for kwarg in kwargs:
        print(kwarg,"", kwargs[kwarg])

super_funcion(10,50,33,77,2,5, nombre="hector", edad=27)
