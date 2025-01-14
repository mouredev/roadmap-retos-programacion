'''EJERCICIO:
Entiende el concepto de recursividad creando una función recursiva que imprima
números del 100 al 0.
DIFICULTAD EXTRA (opcional):
Utiliza el concepto de recursividad para:
- Calcular el factorial de un número concreto (la función recibe ese número).
- Calcular el valor de un elemento concreto (según su posición) en la sucesión de Fibonacci (la función recibe la posición).'''

# Recursividad para imprimir números del 100 al 0
def recursividad(n):
    if n >= 0:
        print(n)
        recursividad(n-1)

recursividad(100)

# EXTRA
# Recursividad para calcular el factorial de un número
def factorial(n:int):
    if n < 0:
        print("No se puede calcular el factorial de un número negativo")
        return 0
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(4))

# Recursividad para calcular el valor de un elemento en la sucesión de Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34... es decir, el siguiente número es la suma de los dos anteriores
def fibonacci(n:int):
    if n <= 0:
        print("La posición debe ser mayor a 0")
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))

# Otra forma de hacerlo
def fibonacci2(n:int):
    if n <= 0:
        print("La posición debe ser mayor a 0")
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n):
            a, b = b, a+b
        return b

print(fibonacci2(6))