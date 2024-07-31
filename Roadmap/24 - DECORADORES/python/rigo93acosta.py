# #24 PATRONES DE DISEÑO: DECORADORES
'''
/*
 * EJERCICIO:
 * Explora el concepto de "decorador" y muestra cómo crearlo
 * con un ejemplo genérico.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un decorador que sea capaz de contabilizar cuántas veces
 * se ha llamado a una función y aplícalo a una función de tu elección.
 */
'''

## Ejercicio

def print_call(func):
    def print_function():
        print(f"La funcion '{func.__name__}' ha sido llamada")
        return func    
    return print_function

@print_call
def example_function():
    # print("La funcion 'example_function' ha sido llamada")
    pass

@print_call
def example_function_2():
    # print("La funcion 'example_function_2' ha sido llamada")
    pass

@print_call
def example_function_3():
    # print("La funcion 'example_function_3' ha sido llamada")
    pass

example_function()
example_function_2()
example_function_3()

## Dificultad extra
