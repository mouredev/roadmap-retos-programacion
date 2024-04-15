
'''
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la
 *   sucesión de Fibonacci (la función recibe la posición).
'''

numbers_to_print=[]
def printing_numbers(n):
    if n < 0:
        return numbers_to_print
    numbers_to_print.append(n)
    printing_numbers(n - 1)

printing_numbers(100)
print('los valores impresos son: ', numbers_to_print)


def factorial(n):
    if n == 0:
        return 1
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
n=12
result=factorial(n)
print(f'el factorial de {n} es: {result}')

def fibonacci(position):
    if position <= 0 or position == 1:
        return 0
    elif position == 2:
        return 1
    else:
        return fibonacci(position - 1) + fibonacci(position - 2)
    
position=12
result=fibonacci(position)
print(f'el valor de la serie de fibonacci en la posicion {position} es: {result}')
