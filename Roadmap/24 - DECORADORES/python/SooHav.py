# 24 PATRONES DE DISEÑO: DECORADORES

# Ejercicio

"""
Estructura: Se crea una función llamada decorador que toma como argumento a otra función llamada func.
Al interior del decorador, se crea otra función que se llama wrapper, 
que tiene como objetivo “envolver” la función func.

Los argumentos de la función wrapper son *args y **kwargs, porque no se sabe que argumentos específicos
tendran las funciones a las que se aplica el decorador. 
*args y **kwargs garantizan que el resultado del decorador va a usar esos mismos argumentos.

Dentro de la función wrapper se definen las acciones que vas a implementar antes o después 
de la función original.
"""


def decorador(func):
    # Definir una nueva función que "envuelve" la función original
    def wrapper(*args, **kwargs):
        # Hacer algo antes de llamar la función original
        print("Se inicia el proceso...")
        resultado = func(*args, **kwargs)
        # Hacer algo después de llamar la función original
        print("Finaliza el proceso")
        return resultado
    # Devolver la nueva función
    return wrapper


@decorador
def mi_funcion(nombre):
    # Mi función creada
    nombre = nombre
    return print(f"Hola {nombre}!")


mi_funcion("Juan")

# Extra

# Ejemplo 1


def operacion(funcion):
    def nueva_funcion(a, b):
        c = funcion(a, b)
        nueva_funcion.contador += 1
        print(f"Resultado número: {nueva_funcion.contador}")
        return c
    nueva_funcion.contador = 0
    return nueva_funcion


def redondeo_decimales(funcion):
    def nueva_funcion(a, b):
        c = funcion(a, b)
        return round(c, ndigits=None)
    return nueva_funcion


@operacion
@redondeo_decimales
def suma(a, b):
    print("Funcion suma")
    return a + b


@operacion
@redondeo_decimales
def resta(a, b):
    print("Funcion resta")
    return a - b


print(suma(5.5, 3))
print(suma(1, 8.2))
print(resta(6.1, 3))
print(resta(5.9, 3))

# Ejemplo 2


def contador_llamadas(func):
    def wrapper(*args, **kwargs):
        wrapper.contador += 1
        print(f"Llamada número: {wrapper.contador}")
        return func(*args, **kwargs)
    wrapper.contador = 0
    return wrapper


@contador_llamadas
def say_hello(name):
    print(f"Hola, {name}!")


say_hello("SooHav")
