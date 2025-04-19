#  * EJERCICIO:
#  * Entiende el concepto de recursividad creando una función recursiva que imprima
#  * números del 100 al 0.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Utiliza el concepto de recursividad para:
#  * - Calcular el factorial de un número concreto (la función recibe ese número).
#  * - Calcular el valor de un elemento concreto (según su posición) en la 
#  *   sucesión de Fibonacci (la función recibe la posición).

# Recursividad:

def secuencia(n):
    if n == 0: # ---> Caso base
        return 0
    else:
        print(n)
        return secuencia(n-1) # ---> Llamada recursiva
    
secuencia(100)

# DIFICULTAD EXTRA

def factorial(n):
    if n == 0 or n == 1: # ---> Caso base
        return 1
    else:
        return n * factorial(n-1) # ---> Llamada recursiva
     
print(factorial(5))

def fibonacci(p):
    if p == 0:
        return 0
    elif p == 1:
        return 1
    else:
        return fibonacci(p-1) + fibonacci(p-2)
    
print(fibonacci(9))
