""""
/*
 * EJERCICIO:
 * Explora el concepto de "decorador" y muestra cómo crearlo
 * con un ejemplo genérico.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un decorador que sea capaz de contabilizar cuántas veces
 * se ha llamado a una función y aplícalo a una función de tu elección.
 */
"""

def mi_decorador(funcion):    
    def nueva_funcion(a, b):
        print("se va a llamar")
        c = funcion(a, b)
        print("se ha llamado")
        return c    
    return nueva_funcion
    
@mi_decorador
def suma(a, b):
    print(f"La Suma de {a} + {b} es igual a: ", a + b)

suma(5,8)
suma(9,8)

#Extra

def call_dec(funcion):
    def count_dec(a ,b):
        count_dec.call_deco += 1
        c = funcion(a, b)
        print(f"la funcion {funcion.__name__} se ha contabilizado {count_dec.call_deco} veces")
        return funcion
    count_dec.call_deco = 0
    return count_dec

@call_dec
def suma(a, b):
    print(f"La Suma de {a} + {b} es igual a: ", a + b)

@call_dec
def resta(a, b):
    print(f"La Suma de {a} - {b} es igual a: ", a - b)

@call_dec
def mutiplica(a, b):
    print(f"La Suma de {a} * {b} es igual a: ", a * b)

suma(8,5)
suma(8,9)
suma(8,65)
resta(9,8)
resta(10,8)
mutiplica(2,5)
mutiplica(2,9)
mutiplica(58,5)
mutiplica(8,2)
