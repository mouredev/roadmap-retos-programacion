print("Números del 100 al 0 con recursividad:")

def recursividad(n) -> None:
    if n == 0:
        print(n)
    else:
        print(n, end=', ')
        recursividad(n - 1)

recursividad(100)

#---DIFICULTAD: EXTRA---#

print("\nFactorial de un número con recursividad:")

def factorial_recursivo(n) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursivo(n - 1)
    
print(factorial_recursivo(5))

print("\nFibonacci de un número con recursividad:")
def fibonacci_recursivo(n) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)
    
print(fibonacci_recursivo(5))

