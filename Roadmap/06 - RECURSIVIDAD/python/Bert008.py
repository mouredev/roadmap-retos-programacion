# #06 RECURSIVIDAD
'''
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
'''

# recursividad


def retorno(n, m):
    if n == m:
        print(n)
    elif n != m:
        print(n)
        retorno(n + 1, m)
 
retorno(1, 100)

# extra
# factorial
def factorial(n):
    if n <= 1:
        return n
    return n * factorial(n-1)

factor = factorial(8)
print(factor)

# fibonachi
def fibonachi(n):
    if n == 0:
        return n
    elif n == 1:
        return n
    else:
        return fibonachi(n - 1) + fibonachi(n - 2)
    
fibo = fibonachi(8)

print(fibo)