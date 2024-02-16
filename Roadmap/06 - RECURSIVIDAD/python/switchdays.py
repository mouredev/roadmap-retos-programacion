"""
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
"""


def print_numbers(number):
    # Caso base: detener la recursión cuando number llega a 0
    if number < 0:
        return
    else:
        # Imprimir el número actual
        print(number)
        # Llamar recursivamente a la función con un número más pequeño
        print_numbers(number - 1)

# Llamada a la función con number = 100
print_numbers(100)


"""
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
"""


def factorial(number):

    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)
    

def fibonacci(posicion):

    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)
    

print("Introduce un número cualquiera.\nEn el primer caso sacará el factorial de ese número.\nEn el segundo caso sacará el valor de fibonaci en la posición de ese número.)")

input = input("Introduce el número: ")

try:
    number = int(input)

    print("El factorial de ", number, "es: ", factorial(number))
    print("El valor de la posición ", number, "de fibonaci es: ", fibonacci(number))
except:
    print("El valor ", input, "no es válido.")
