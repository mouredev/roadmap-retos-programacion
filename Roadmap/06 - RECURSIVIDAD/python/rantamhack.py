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
"""

print("\n\n=====================================EJERCICIO=====================================\n\n")

def recursive(x):
    if x >= 0:
        print(x)
        recursive(x-1)

recursive(100)    

print("\n\n=====================================DIFICULTAD EXTRA=====================================\n\n")

# Función factorial

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n -1)
          
resultado = factorial(6)
print(f"El factorial de 6 es {resultado}")

print("\n\n==========================================================================================\n\n")

# Función factorial aplicada a posicion de elementos  en fibonacci

def fibonacci(number:int) -> int:
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number -1) + fibonacci(number -2)

number = int(input("¿Que valor, en funcion de la posicion en la serie de fibonacci deseas conocer?: "))
fibonacci(number)
position = fibonacci(number)

print(f"El valor de la posicion {number} es {position}")

print("\n\n==========================================================================================\n\n")


n = fibonacci(number)
def factorial_fibonacci(n):
    factorial = n * factorial_fibonacci(n -1)
    return factorial

factorial(n)

print(f"El valor de la posicion {number} en la sucesion de fibonacci es {position} y el valor factorial de esta posicion es:  {factorial(n)}")






