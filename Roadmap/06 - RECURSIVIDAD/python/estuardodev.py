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

def numeros(numero):
        if numero >= 0:
            print(numero)
            numeros(numero - 1)

def factorial(numero) -> int:
        if numero < 0:
            return 1
        elif numero == 0:
            return 1
        else:
            return numero * factorial(numero - 1)
        
def fibonacci(posicion) -> int:
        if posicion <= 0:
            return 0
        elif posicion == 1:
            return 0
        elif posicion == 2:
            return 1
        else:
            return fibonacci(posicion - 1) + fibonacci(posicion - 2)

numeros(100)
print(factorial(5))
print(fibonacci(5))