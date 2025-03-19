"""
EJERCICIO:
Entiende el concepto de recursividad creando una funcion recursiva 
que imprima numeros del 100 al 0.

DIFICULTAD EXTRA (opcional):
Utiliza el concepto de recursividad para:
- Calcular el factorial de un numero concreto (la funcion recibe ese
numero).
- Calcular el valor de un elemento concreto (segun su posicion) en la
sucesion de Fibonacci (la funcion recibe la posicion).

by adra-dev.
"""

"""
Recursividad:
    Una funcion recursiva es una funcion que se llama a si misma, un 
    ejemplo tipico es el calculo del factorial
"""

def countdown(number:int):
    if number >= 0:
        print(number)
        countdown(number= number - 1)



countdown(100)

"""
Extra
"""


def factorial(number:int) -> int:
    if number < 0:
        print("Los numeros negativos no son validos")
        return 0
    elif number == 0 or number == 1:
        return 1 
    else:
        return number * factorial(number - 1)


print(factorial(5))


def fibonacci(number:int) -> int:
    if number <= 0 :
        print("La posicion tiene que ser mayor que cero")
        return 0
    elif number == 1 :
        return 0
    elif number == 2:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)



print(fibonacci(5))