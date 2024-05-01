""" 

/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 */
 
 """


def count_to_one(n):
    print(n)
    if n > 1:
        count_to_one(n - 1)

count_to_one(50)


def factorial(n):
    if(n > 1):
        return n * factorial(n - 1)
    return 1

print(factorial(5))

def fibonacci(n):
    if(n > 1):
        return fibonacci(n - 1) + fibonacci(n - 2)
    return 0 if n == 0 else 1

print(fibonacci(10))

