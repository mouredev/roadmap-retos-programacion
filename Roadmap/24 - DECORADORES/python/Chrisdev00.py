"""
* EJERCICIO:
* Explora el concepto de "decorador" y muestra cómo crearlo
* con un ejemplo genérico.
*
* DIFICULTAD EXTRA (opcional):
* Crea un decorador que sea capaz de contabilizar cuántas veces
* se ha llamado a una función y aplícalo a una función de tu elección.
"""

import time

def calcularTiempo(fun):

    def funcionModificada(*args, **kwargs):
        inicio = time.time()
        resultado = fun(*args, **kwargs)
        final = time.time()
        print(f"El tiempo de ejecucion es: {final - inicio} segundos")
        return resultado

    return funcionModificada

@calcularTiempo
def sum_numeros(a, b):
    return a + b

@calcularTiempo
def imprimirNumeros(num):
    for i in range(num):
        print(i)

print(sum_numeros(16556301655659919911, 896474544))
imprimirNumeros(8)


########### --------------------------------- EXTRA ---------------------------------- ##################

def contador(fun):

    def funcion_modificada(*args, **kwargs):
        funcion_modificada.llamadas += 1
        print(f"La funcion {fun.__name__} ha sido llamada {funcion_modificada.llamadas} veces")
        return fun(*args, **kwargs)
    
    funcion_modificada.llamadas = 0
    return funcion_modificada

@contador
def factorial(num):
    res = 1
    for i in range(1, num+1):
        res = res * i
    return res


print(factorial(5))
print(factorial(4))
print(factorial(3))