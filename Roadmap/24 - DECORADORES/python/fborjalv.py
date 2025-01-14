"""
/*
 * EJERCICIO:
 * Explora el concepto de "decorador" y muestra cómo crearlo
 * con un ejemplo genérico.

"""

def decorator_operations(function):
    def show_name(*args):
        print(f"Estás utilizando la función {function.__name__}:")
        return function(*args)
    return show_name


@decorator_operations
def sumar(a, b):
    print(f"{a} + {b} = {a+b}") 

def resta(a, b):
    print(f"{a} - {b} = {a-b}")  

def multiplica(a, b):
    print(f"{a} x {b} = {a*b}") 

sumar(2, 4)
resta(2, 4)
multiplica(2, 4)

"""
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un decorador que sea capaz de contabilizar cuántas veces
 * se ha llamado a una función y aplícalo a una función de tu elección.
 */

"""


def func_counter(function):
    
    def counter(*args):
        counter.call_counter +=1
        print(f"La función {function.__name__} se ha ejecutado {counter.call_counter} veces")
        return function(*args)
    counter.call_counter = 0
    return counter


@func_counter
def saludo(name):
    print(f"Hola, {name} ¿Cómo estás?")


for name in ["Brais", "Borja", "Sonia"]:
    saludo(name)
