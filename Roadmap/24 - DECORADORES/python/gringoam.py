"""
Ejercicio
"""


def funcion_decoradora(func):
    def imprime_func():
        print(f"Se imrime {func.__name__}")
        return func
    return imprime_func




@funcion_decoradora
def funcion1():
    print("se imprime  primero")

@funcion_decoradora
def funcion2():
    pass

funcion1()
funcion2()

"""
Extra
"""

def contador_llamado(func):
    
    def llamados():
        llamados.llamado+=1
        print(f"La funcion {func.__name__} se llamo {llamados.llamado}")
        return func
    llamados.llamado=0
    return llamados

@contador_llamado
def funcion3():
    pass

@contador_llamado
def funcion4():
    pass

funcion4()
funcion3()
funcion4()