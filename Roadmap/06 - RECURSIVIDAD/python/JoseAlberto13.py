"""EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *"""

inicio = 100

def funcionRecursiva(num):
    if num >= 0:
        print(num)
        num -= 1
        funcionRecursiva(num)

funcionRecursiva(inicio)

"""* DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición)."""

def factorialRecursiva(num):
    if num < 0:
        print("Verifica el número ingresado ")
        return 0
    elif num == 0:
        return 1
    else:
        resultado = num * factorialRecursiva(num-1)
        print(f"{num} * {int(resultado/num)} = {resultado}") # Observamos la recursividad
        return(resultado)


print(factorialRecursiva(7))


def fibonacciRecursiva(num):
    if num <= 0:
        print("Verfica el número ingresado ")
        return 0
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        resultado = fibonacciRecursiva(num -1) + fibonacciRecursiva(num -2)
        return resultado
    
print(fibonacciRecursiva(5))