
#  * DIFICULTAD EXTRA (opcional):
#  * Utiliza el concepto de recursividad para:
#  * - Calcular el factorial de un número concreto (la función recibe ese número).
#  * - Calcular el valor de un elemento concreto (según su posición) en la 
#  *   sucesión de Fibonacci (la función recibe la posición).
#  */

# Funcion recursiva que por defecto tiene numero 100 como parametro
def printing(n=100):
    print(n)
    
    # Cuando es menor o igual a 0 sale
    if n <= 0: 
        return 0
    
    # La funcion se retornara a si misma(recursiva) restandose en uno su parametro
    return n - printing(n - 1)  

printing(100)


# DIFICULTAD EXTRA (opcional):
# Factorial
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1);

# print(factorial(5)) #120


# Fibonacci (2)
def fibonacci(n):
    if n <= 0: return 0
    elif n == 1: return 1 
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"Posiition 4: {fibonacci(4)}")