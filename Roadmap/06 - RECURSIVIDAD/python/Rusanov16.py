"""/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 */
"""
#*-------------------------------------------------------------------------------------------------------------#
print("-----------------------------------------------------------------------------------------------------")
print("Recursividad")

def numero_recursivo(n):
    for i in range(n, -1, -1):
        print(i)
numero_recursivo(100)

#*-------------------------------------------------------------------------------------------------------------#
print("-----------------------------------------------------------------------------------------------------")
print("Factorial")
def factorial(n):
    resultado = 1
    for i in range(2, n + 1): 
        resultado *= i
    return resultado

numero = int(input("Indique el número: "))
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")

#*-------------------------------------------------------------------------------------------------------------#
print("-----------------------------------------------------------------------------------------------------")
print("Fibonacci")
def fibonacci(n):
    if n <= 0:
        return "La posición debe ser un número entero positivo."
    elif n == 1:
        return 0  
    elif n == 2:
        return 1  
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) 

posicion = int(input("Ingrese la posición en la sucesión de Fibonacci: "))
resultado = fibonacci(posicion)
print(f"El elemento en la posición {posicion} de la sucesión de Fibonacci es {resultado}")