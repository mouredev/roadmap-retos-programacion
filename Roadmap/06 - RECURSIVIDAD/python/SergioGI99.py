"""
------------
RECURSIVIDAD
------------
EJERCICIO:
Entiende el concepto de recursividad creando una función recursiva que imprima
números del 100 al 0.
DIFICULTAD EXTRA (opcional):
Utiliza el concepto de recursividad para:
- Calcular el factorial de un número concreto (la función recibe ese número).
- Calcular el valor de un elemento concreto (según su posición) en la 
  sucesión de Fibonacci (la función recibe la posición * EJERCICIO:)
"""
def countdown(number: int):
    if number >= 0:
        print(number)
        countdown(number - 1)

countdown(100)

def factorial(number: int) -> int:
    if number < 0:
        print("Los números negativos no son validos")
        return 0
    elif number == 0:
        return 1
    else:
        return number * factorial(number - 1)

print(factorial(10))

def fibonacci(number: int) -> int:
    if number <= 0:
        print("La posición tiene que ser mayor que cero")
        return 0
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)

print(fibonacci(10))