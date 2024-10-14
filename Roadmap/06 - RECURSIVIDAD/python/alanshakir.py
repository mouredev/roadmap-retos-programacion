"""
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
 """

def regresion_recursiva(numero: int):
    if numero >= 0:
        print(numero)
        regresion_recursiva(numero - 1)

regresion_recursiva(100)

"""
EXTRA
"""

def factorial_numero(numero: int):
    if numero == 1:
        return 1
    else:
        return numero * factorial_numero(numero - 1)

print(factorial_numero(3))

def sucession_fibonacci(numero: int):
    if numero == 0 or numero == 1:
        return numero
    else:
        return(sucession_fibonacci(numero-1) + sucession_fibonacci(numero-2))
    
print(sucession_fibonacci(7))
