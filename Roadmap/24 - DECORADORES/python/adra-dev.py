"""
EJERCICIO:
Explora el concepto de "decorador" y muestra cómo crearlo con un 
ejemplo genérico. 

DIFICULTAD EXTRA(opcional):
Crea un decorador que sea capaz de contabilizar cuántas veces se ha 
llamado a una función y aplicalo a una función de tu elección.

by adra-dev
"""

"""
Decoradores:
Un decorador es un modificador de un metodo o funcion que "envuelve"
el codigo de dicho metodo con instrucciones adicionales. Regularmente
vamos a hacer uso de los decoradores para extender el uso de una 
funcion ya sea porque no podemos modificar la funcion o no es 
conveniente hacerlo.

Los decoradores nos sirven para realizar tareas muy complejas y 
repetitivas como lo son conectarse a una BD, enviar un email, 
leer un archivo excel o cualquier tarea que se necesite realizar 
antes o despues de llamar a la funcion a decorar.
"""

def funcion_a(funcion_b):

    def funcion_c():
        print(">>> Antes del llamado.")
        funcion_b()
        print(">>> Despues del llamado.")

    return funcion_c


@funcion_a
def saludar():
    print('Hola, nos encontramos en una fucnion') 

saludar()


"""
Extra
"""

def print_call_counter(function):
    def counter_function():
        counter_function.call_count += 1
        print(
            f"La funcion '{function.__name__}' se ha llamado {counter_function.call_count} veces.")
        return function
        
    counter_function.call_count = 0
    return counter_function



@print_call_counter
def example_function():
    pass


@print_call_counter
def saludar():
    print('Hola, nos encontramos en una fucnion') 


example_function()
saludar()
saludar()
saludar()
example_function()
saludar()
saludar()