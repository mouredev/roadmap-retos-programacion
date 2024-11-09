# #06 RECURSIVIDAD

"""
* EJERCICIO:
* Entiende el concepto de recursividad creando una función recursiva que imprima
* números del 100 al 0.
"""

"""
La recursividad es una técnica de programación donde una función se llama a sí misma para resolver un problema. En cada llamada, se trabaja con una versión reducida del problema hasta alcanzar una condición base, que detiene la recursión.

Cualquier función recursiva tiene dos secciones de código claramente divididas:

Por un lado tenemos la sección en la que la función se llama a sí misma.
Por otro lado, tiene que existir siempre una condición en la que la función retorna sin volver a llamarse. Es muy importante porque de lo contrario, la función se llamaría de manera indefinida.
"""

print("Números del 100 al 0")

def print_numbers(n):
    # Condición base: si n es menor que 0, detenemos la recursión
    if n < 0:
        return  # Termina la ejecución
    # Imprimimos el número actual
    print(n)
    # Llamamos recursivamente a la función con n - 1
    print_numbers(n - 1)

# Llamamos a la función con 100 como punto de partida
print_numbers(100)

"""
* DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
"""
print("\nDIFICULTAD EXTRA")

print("\nFactorial de un número")

def factorial(n):
    # Condición base: si n es igual a 1, detenemos la recursión
    # n! = 1 si n = 1 
    if n == 1:
        return 1# Termina la ejecución
    # Llamada recursiva
    else:
        # n! = n * (n-1)! si n > 1
        return n * factorial(n - 1)

n = 5
print(f"El factorial de {n} es: {factorial(n)}")

print("\nCalcular el valor de un elemento concreto (según su posición) en la sucesión de Fibonacci")

# Dicha serie calcula el elemento n sumando los dos anteriores n - 1 + n - 2
# Se asume que los dos primeros elementos son 0 y 1.
def fibonacci(n):
    # Condicion base
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
n = 7
print(f"El valor del elemento {n} en la serie fibonacci es: {fibonacci(7)}")