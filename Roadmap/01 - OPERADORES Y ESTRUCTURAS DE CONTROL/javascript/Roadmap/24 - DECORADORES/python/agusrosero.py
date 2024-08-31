"""
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
# EJERCICIO:


def mi_decorador(fn):
    def wrapper(*args, **kwargs):
        print("Mi decorador...")
        return fn(*args, **kwargs)
    return wrapper


@mi_decorador
def suma(a, b):
    return a + b


print(suma(10, 20))

# DIFICULTAD EXTRA:


def counter(fn):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return fn(*args, **kwargs)
    wrapper.count = 0
    return wrapper


@counter
def resta():
    return 10 - 5


resta()
resta()
resta()
print(resta.count)
