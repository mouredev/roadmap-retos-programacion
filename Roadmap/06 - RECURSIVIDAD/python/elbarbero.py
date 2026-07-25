"""
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 *
 """
 
def printNumbers(limit: int, current_number: int):
    if current_number < limit:
        print(current_number)
        current_number += 1
        printNumbers(limit, current_number)

def recursiveFactorialNumber(n: int, i = 1, factorial = 1):
    if i < (n + 1):
        factorial *= i
        i += 1
        recursiveFactorialNumber(n, i, factorial)
    else:
        print(f"El factorial de {n} es {factorial}")

def factorialNumber(n: int):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"El factorial de {num} es {factorial}")

def fibonacci(n: int):
    num1 = 0
    num2 = 1
    next_number = num2  
    count = 1

    while count <= n:
        print(next_number, end=" ")
        count += 1
        num1, num2 = num2, next_number
        next_number = num1 + num2
    
def recursiveFibonacci(n: int):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return recursiveFibonacci(n-1) + recursiveFibonacci(n-2)
    

if __name__ == "__main__":
    printNumbers(limit = 100, current_number = 0)
    recursiveFactorialNumber(6)
    print(f"El número fibonacci del número 8 es {recursiveFibonacci(9)}")