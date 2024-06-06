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


# Función recursiva que hace una cuenta atrás de 100 a 1
def cuenta_atras_recursiva(n):
    if n >= 0:
        print(n)
        cuenta_atras_recursiva(n-1)


cuenta_atras_recursiva(100)

print()
print("::::::::::::::::::::::::::::::::::::: EXTRA :::::::::::::::::::::::::::::::::::::")
print()


# Calcular el factorial de un número concreto (la función recibe ese número).
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)



print(factorial(5))
