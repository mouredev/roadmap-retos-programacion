"""
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

# La recursividad en Python (y en la programación en general) es un concepto poderoso 
# que se utiliza cuando una función se llama a sí misma directa o indirectamente. 
# La idea detrás de la recursividad es dividir un problema en subproblemas más pequeños 
# y resolverlos de manera recursiva hasta llegar a un caso base que se puede resolver directamente.

# Una función recursiva es aquella que se llama a sí misma dentro de su definición.
# En cada llamada recursiva, se trabaja con un conjunto de datos más pequeño 
# o se realiza algún tipo de operación para acercarse al caso base.

def print_numbers(n):

    if n >= 0:
        print(n)
        print_numbers(n-1)

print_numbers(100)
        
"""
        --------------------------  Dificultad Extra ---------------------------------------
"""

def factorial(n):

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

resul = factorial(5)
print(resul)



def fibonnaci(n):

    if n <= 1:
        return n
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)

res = fibonnaci(9)
print(res)

    
