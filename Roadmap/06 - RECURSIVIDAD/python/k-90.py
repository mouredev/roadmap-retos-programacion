""""
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 """

def func_recur(number:int):
    if number >= 0:
        print(number)
        func_recur(number -1)
    
print(func_recur(100))    

### Extra

def factorial (number):
    r = 1
    i = 2 
    while i <= number:
        r *= i
        i += 1
    return r
print(factorial(5))

def factorial_recursivo(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursivo(n-1)

print(factorial_recursivo(5))

def fib_recur(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recur(n-1) + fib_recur(n-2)

print(fib_recur(7))