## Recursividad

# Concepto: La recursividad es una técnica de programación en la que una función se llama a sí misma para resolver un problema. Se utiliza comúnmente para dividir problemas complejos en subproblemas más simples.

# creando una función recursiva que imprima números del 100 al 0.

def cuenta_regresiva(num):
    if num >= 0:
        print(num)
        cuenta_regresiva(num-1)
    
cuenta_regresiva(100)

""" Explicación: La función cuenta_regresiva utiliza la recursividad para imprimir números del 100 al 0. En cada llamada, se verifica si el número actual es mayor o igual a 0. Si es así, se imprime el número y se realiza una llamada recursiva a la función con el número decrementado en 1. Esto continúa hasta que el número es menor que 0, momento en el cual la función deja de llamarse a sí misma y finaliza."""

"""Hacer una funcion recursiva para imprimir los numeros del 100 a 0, no es algo que se utilice comumente en la vida real, pero es un buen ejercicio para entender cómo funciona la recursividad. """

## Extra

# Calcular el factorial de un número concreto (la función recibe ese número).

def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        print("El factorial no está definido para números negativos.")
    else:
        return n * factorial(n-1)

print(factorial(5))

# Calcular el valor de un elemento concreto (según su posición) en la sucesión de Fibonacci (la función recibe la posición).

def fibonacci(pos):
    if pos < 0:
        print("La posicion no puede ser negativa.")
    elif pos == 0:
        return 0
    elif pos == 1:
        return 0
    elif pos == 2:
        return 1
    else:
        return fibonacci(pos-1) + fibonacci(pos-2)
    
print(fibonacci(10))

