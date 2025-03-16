"""
/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 */
"""

# Concepto de Recursividad:

def cuenta_atras(inicio):
    if inicio != -1:
        print(inicio)
        cuenta_atras(inicio - 1)
cuenta_atras(100)

"""
     * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
"""
def factorial(numero):
    if numero < 0:
        return f"Entrada Erronea: {numero}"
    elif numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)
        
print(factorial(5))

def fibon(numero):
    if numero < 0:
        return f"Entrada Erronea: {numero}"
    elif numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return fibon(numero - 1) + fibon(numero - 2)

print(fibon(4))