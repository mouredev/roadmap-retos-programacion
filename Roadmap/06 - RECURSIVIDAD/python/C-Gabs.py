#Reto 06

''' Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).'''

def nums(n = 100):
    if n >= 0:
        print(n)
        return nums(n-1)

nums()


#Reto extra

def factorial(n):
    if n < 0:
        print("Los numeros negativos no tienen factorial")
        return 0
    elif n < 2:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))


def fibonacci(n):
    if n <= 1:
        return 0
    if n < 3:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
         

print(fibonacci(8))