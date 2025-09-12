"""
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
"""


def cuenta_regresiva(num):
    if num >= 1:
        print(num, end="-")
        return cuenta_regresiva(num - 1)
    else:
        print(num)


print("Cuenta regresiva de 100 a 0")
cuenta_regresiva(100)


"""
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
"""
print("\n")


def calculo_factorial(num1):
    if num1 <= 1:
        return num1
    else:
        return num1 * calculo_factorial(num1 - 1)


def calculo_fibonacci(num2):
    if num2 <= 1:
        return num2
    else:
        return calculo_fibonacci(num2 - 1) + calculo_fibonacci(num2 - 2)


print("El factorial del numero 6 es:", calculo_factorial(6))
print("\n")
print("El valor de la sucecion de Fibonacci en la posicion 8 es:", calculo_fibonacci(8))
