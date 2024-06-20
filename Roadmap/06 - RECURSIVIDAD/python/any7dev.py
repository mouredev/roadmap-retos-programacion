""" /*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 */ """

def ejercicio(n):
    print(n)
    if n > 0:
        ejercicio(n-1)        

def factorial(numero):
    if numero == 1:
        fact = 1
    else:
        fact = numero * factorial(numero-1)
    return fact

if __name__ == '__main__':
    ejercicio(100)
    print(factorial(7))
    