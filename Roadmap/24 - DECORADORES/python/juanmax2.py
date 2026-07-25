
"""
Ejercicio
"""
def print_call(func):
    
    def print_function():
        print(f"La función {func.__name__} ha sido llamada")
        return func
    return print_function

@print_call
def example_function():
    pass

@print_call
def example_function_1():
    pass

@print_call
def example_function_2():
    pass

example_function()
example_function_1()
example_function_2()

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un decorador que sea capaz de contabilizar cuántas veces
 * se ha llamado a una función y aplícalo a una función de tu elección.
"""

def count_func(func):
    
    def contador():
        contador.count_func += 1
        print(f"La funcion {func.__name__} se ha llamado {contador.count_func} veces")
        return func
    contador.count_func = 0
    return contador

@count_func
def example_function_3():
    pass

@count_func
def example_function_4():
    pass

example_function_3()
example_function_3()
example_function_3()
example_function_4()
example_function_3()
example_function_4()