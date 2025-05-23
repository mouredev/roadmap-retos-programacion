'''
EJERCICIO:
Entiende el concepto de recursividad creando una función recursiva que imprima números del 100 al 0.
'''
def countdown(number: int):
    if number >= 0:
        print(number)
        countdown(number-1)
    
countdown(100)

print('-----------------------------------------------------')
'''
DIFICULTAD EXTRA (opcional):
Utiliza el concepto de recursividad para:
- Calcular el factorial de un número concreto (la función recibe ese número).
- Calcular el valor de un elemento concreto (según su posición) en la sucesión de Fibonacci (la función recibe la posición).
'''
# Factorial
def factorial(n: int):
    if n >= 0 and n <= 1:
        return 1
    elif n < 0:
        print('No se puede calcular el factorial de un número negativo')
        return 0
        
    return n * factorial(n - 1)

numero = int(input('Introduce un número: '));
print(f'El factorial de {numero} es {factorial(numero)}')

# Fibonacci
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
def fibonacci(p: int):
    if p <= 0:
        print('La posición no puede ser negativa')
        return 0
    elif p == 1:
        return 0
    elif p == 2:
        return 1
    else:
        return fibonacci(p - 1) + fibonacci (p - 2)

    
n = int(input('Introduce un número: '))
print(f'El fibonacci en la posición {n} es {fibonacci(n)}')