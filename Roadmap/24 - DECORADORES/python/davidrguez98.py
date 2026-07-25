""" /*
 * EJERCICIO:
 * Explora el concepto de "decorador" y muestra cómo crearlo
 * con un ejemplo genérico.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un decorador que sea capaz de contabilizar cuántas veces
 * se ha llamado a una función y aplícalo a una función de tu elección.
 */ """

#EJERCICIO

def print_call(function):
    def print_function():
        print(f"La función {function.__name__} ha sido llamada.")
        return function
    return print_function

@print_call
def example_function():
    pass

@print_call
def example_function2():
    pass

@print_call
def example_function3():
    pass

example_function()
example_function2()
example_function3()

#DIFICULTAD EXTRA

def function_call(function):
    def function_counter():
        function_counter.function_call += 1
        print(f"La función {function.__name__} ha sido llamada {function_counter.function_call} veces.")
        return function
    
    function_counter.function_call = 0
    return function_counter


@function_call
def example_function4():
    pass

@function_call
def example_function5():
    pass

example_function4()
example_function4()
example_function4()
example_function5()