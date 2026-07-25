"""
EJERCICIO:
Entiende el concepto de recursividad creando una función recursiva que imprima
    números del 100 al 0.

DIFICULTAD EXTRA (opcional):
Utiliza el concepto de recursividad para:
- Calcular el factorial de un número concreto (la función recibe ese número).
- Calcular el valor de un elemento concreto (según su posición) en la 
    sucesión de Fibonacci (la función recibe la posición).
 */
"""

def recursion_example(num = 100):  # Función con parámetro inicial por defecto en 100
    """Ejemplo de una funcion recursiva"""
    if num < 0: # Caso base: cuando el número es menor que 0, detenemos la recursión
        return None
    print(num) # Imprime el número actual
    return recursion_example(num - 1) # Llama a la función recursivamente con el número decrementado

recursion_example()

# EXTRA

def recursion_factorial(num: int) -> int:
    """Retorna el factorial de un numero dado"""
    if num == 1: # Caso base: el factorial de 1 es 1
        return 1
    return num * recursion_factorial(num - 1) # Llamada recursiva multiplicando el número actual por el factorial de (num - 1)

print(recursion_factorial(5))

def recursion_fibonacci(n: int) -> int:
    """Retorna la posicion en la serie Fibonacci segun un numero dado"""
    if n < 0:
        raise ValueError("La posición debe ser mayor o igual a cero.") # Valida que n no sea negativa
    if n == 0:
        return 0 # Caso base: posición 0 → valor 0
    if n == 1:
        return 1 # Caso base: posición 1 → valor 1
    return recursion_fibonacci(n - 1) + recursion_fibonacci(n - 2) # Llamada recursiva sumando los dos valores anteriores

print(recursion_fibonacci(6))
