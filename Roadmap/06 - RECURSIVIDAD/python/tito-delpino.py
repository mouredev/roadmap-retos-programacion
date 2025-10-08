# /*
#  * EJERCICIO:
#  * Entiende el concepto de recursividad creando una función recursiva que imprima
#  * números del 100 al 0.

def rec(n):
    if n == 0:
        return 0
    else:
        print(n)
        return rec(n-1)

numeros = rec(100)
print(numeros)


#  * DIFICULTAD EXTRA (opcional):
#  * Utiliza el concepto de recursividad para:
#  * - Calcular el factorial de un número concreto (la función recibe ese número).

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
result = factorial(5)
print(result)


#  * - Calcular el valor de un elemento concreto (según su posición) en la 
#  *   sucesión de Fibonacci (la función recibe la posición).

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
valor = fibonacci(9)
print(valor)