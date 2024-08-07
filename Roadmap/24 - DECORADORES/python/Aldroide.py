""" 
    Ejercicio
    Explora el concepto de "decorador" y muestra cómo crearlo con un ejemplo genérico
"""


def mi_decorador(func):
    def funcion_(a, b):
        print("Antes de llamar a la función")
        resultado = func(a, b)
        print("Se llamo la función")
        return resultado
    return funcion_


@mi_decorador
def suma(a, b):
    print("Entró a funcion suma")
    return a+b


@mi_decorador
def resta(a, b):
    print("Entró a función resta")
    return a-b


r = suma(4, 5)
print(r)
r = resta(5, 3)
print(r)


"""
    Crea un decorador que sea capaz de contabilizar cuántas veces
    se ha llamado a una función y aplícalo a una función de tu elección.
"""


def count_call(func):
    def new_func():
        new_func.contador += 1
        print(
            f"La función '{func.__name__}' ha sido llamada {new_func.contador} veces")
        return func
    new_func.contador = 0
    return new_func


@count_call
def my_func():
    print("Ejecutanto la funcion")


my_func()
my_func()
my_func()
