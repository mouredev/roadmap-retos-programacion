"""
 * EJERCICIO:
 * Explora el concepto de "decorador" y muestra cómo crearlo
 * con un ejemplo genérico.
"""

from functools import reduce

def decorador(funcion):
    def nueva_funcion(*args):
        print("Se va a llamar")
        c = funcion(*args)
        print("Se ha llamado")
        return c
    return nueva_funcion

#@decorador
def suma (*args:int):
    print("Entra en suma")
    return reduce(lambda x,y:x+y,[*args])

#print(f"El resultado de la suma es: {suma (7,9,3,1,2)}")

@decorador
def resta(*args:int):
    print("Entra en la resta")
    return reduce(lambda x,y:x-y,[*args])

print(f"El resultado de la resta es: {resta(7,3)}")

funcion_decorada = decorador(suma)
funcion_decorada(3,5,7)

"""DIFICULTAD EXTRA (opcional):
 * Crea un decorador que sea capaz de contabilizar cuántas veces
 * se ha llamado a una función y aplícalo a una función de tu elección.
"""
def count_decorator(function):
    def original_function(*args:int):
        original_function.count += 1
        print(f"La función {function.__name__} se ha llamado {original_function.count} vez/veces")
        return function(*args)

    original_function.count = 0 #es una variable que declaro para la función original_function llamada count
    return original_function
#el decorador es capaz de diferenciar entre funciones a las que llama
#genera un ámbito de ejecución para la misma función que se ejecuta
#la instancia de "multiplicar" es diferente de otras funciones como "suma_2"

@count_decorator
def multiplicar(*args:int):
    return reduce(lambda x,y: x*y,[*args])

@count_decorator
def suma_2(*args:int):
    return reduce(lambda x,y: x+y,[*args])

print(multiplicar(3,2))
print(multiplicar(4,2))
print(multiplicar(5,2))
print(suma_2(3,8))
print(suma_2(9,1,5))
