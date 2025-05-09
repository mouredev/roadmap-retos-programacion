#06 RECURSIVIDAD

#  * EJERCICIO:
#  * Entiende el concepto de recursividad creando una función recursiva que imprima
#  * números del 100 al 0.

"""
La recursividad es una técnica de programación en la que una función se llama a sí misma para resolver subproblemas más pequeños de un problema más grande. 
Es una forma de descomponer problemas complejos en partes más manejables y más pequeñas.

Componentes de la Recursividad
Caso Base: Es la condición que termina las llamadas recursivas. Sin un caso base, la función recursiva se llamaría indefinidamente, causando un desbordamiento de pila.

Caso Recursivo: Es la parte de la función que divide el problema en subproblemas más pequeños y se llama a sí misma con estos subproblemas.
"""

def count_down(n):
    #caso base
    if n == 0:
        return print(0)
    else:
        print(n)
        return count_down(n-1)

count_down(100)

#  * DIFICULTAD EXTRA (opcional):
#  * Utiliza el concepto de recursividad para:
#  * - Calcular el factorial de un número concreto (la función recibe ese número).
#  * - Calcular el valor de un elemento concreto (según su posición) en la 
#  *   sucesión de Fibonacci (la función recibe la posición).


# Factorial
# n!=n×(n−1)×(n−2)×⋯×2×1

print("\nDesafio factorial\n")
def factorial(n):
    if n == 0:
        return 1
    else:        
        return n * factorial(n-1)

print(factorial(10))
print(factorial(20))    

# Fibonacci 
"""
F(0) = 0
F(1) = 1

Para n>=2

F(n) = F(n-1)+F(n-2)
"""
print("\nDesafio fibonacci\n")

def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
    
print(fibo(0))
print(fibo(1))
print(fibo(2))
print(fibo(3))
print(fibo(4))
print(fibo(5))
print(fibo(6))
print(fibo(7))
print(fibo(8))
print(fibo(9))
print(fibo(10))