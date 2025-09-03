'''
EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
'''

# Función de recursividad

def recursividad(n):
    if n < 0:
        return
    print(n)
    
    recursividad(n - 1)

recursividad(100)


# Cálculo del Factorial de un numero utilzando la recursividad. 

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Introduzca el número: "))

print(f'El factorial de {n} es: {factorial(n)}')

# Cálculo sucesión de Fibonacci haciendo uso de la recursividad.

def fibonacci(numero: int)-> int:
    if numero < 0:
        raise ValueError('número debe de ser un entero no negativo')
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return fibonacci(numero - 1) + fibonacci(numero - 2)

print(f'F(5): {fibonacci(5)}')