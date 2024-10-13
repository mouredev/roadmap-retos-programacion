'''
 * EJERCICIO:
 * Explora el concepto de "decorador" y muestra cómo crearlo
 * con un ejemplo genérico.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un decorador que sea capaz de contabilizar cuántas veces
 * se ha llamado a una función y aplícalo a una función de tu elección.

'''
def mi_decorador(func):
    def envoltura():
        print("Algo se está ejecutando antes de la función.")
        func()
        print("Algo se está ejecutando después de la función.")
    return envoltura

@mi_decorador
def saludar():
    print("¡Hola!")

saludar()


'''
Dificultad extra
'''

def call_counter(funcion):
    def counter_function():
        counter_function.call_count += 1
        print(
            f"La función '{funcion.__name__} se ha llamado {counter_function.call_count}' vez/veces.")
        return funcion
    
    counter_function.call_count = 0
    return counter_function


@call_counter
def example_function():
    pass

example_function()
example_function()
example_function()