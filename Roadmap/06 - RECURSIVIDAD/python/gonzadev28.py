"""EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0."""

def recursividad(n):
    if (n < 0):
        return 
    else:
        print(n)
        return recursividad(n - 1)
    
recursividad(100)

"""DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición)."""

# - Calcular el factorial de un número concreto (la función recibe ese número).
def factorial(fac : int):
    if (fac == 0):
        return 1
    else:
        return (fac * factorial(fac - 1))

print(factorial(5))

#- Calcular el valor de un elemento concreto (según su posición) en la sucesión de Fibonacci
# (la función recibe la posición).
def fibonacci(n):
    if (n < 1):
        print("Numero debe ser mayor o igual a 1")
    elif(n == 1):
        return 0
    elif(n == 2):
        return 1
    else:
        return fibonacci(n -1) + fibonacci(n - 2)
    
print(fibonacci(5)) # Sucesion de fibonacci 0, 1, 1, 2, "3", 5, 8...