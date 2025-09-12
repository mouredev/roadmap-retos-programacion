
# Teoría:

#  La recursividad es un concepto fundamental en la programación que se refiere a la capacidad de una función
#  para llamarse a sí misma dentro de su propia definición. Funciona permitiendo que un problema se divida en 
#  subproblemas más pequeños de la misma naturaleza, facilitando su solución de manera más sencilla y directa. 
#  La recursividad es especialmente útil en tareas que pueden ser descompuestas en tareas más simples de la 
#  misma índole, como los problemas de búsqueda y ordenamiento, el cálculo de factorial, la generación de 
#  secuencias y el procesamiento de estructuras de datos recursivas (como árboles y grafos).

# Para que una función recursiva funcione correctamente y no entre en un bucle infinito, debe tener:
# 1.Caso base:
#  Una condición que detiene la recursión. Es el escenario más simple que no requiere recursividad para resolverse.
# 2.Caso recursivo: 
# La llamada a sí misma con diferentes argumentos, acercándose al caso base.

### Ejemplo: Búsqueda Binaria
# La búsqueda binaria es un algoritmo eficiente para encontrar un elemento en una lista ordenada. Funciona dividiendo 
# repetidamente a la mitad la porción de la lista que podría contener al elemento, hasta que queda reducida a un solo 
# elemento.

def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        # Si el elemento es el punto medio
        if arr[mid] == x:
            return mid
        
        # Si el elemento es más pequeño que el medio, entonces solo puede
        # estar presente en el subarreglo izquierdo
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        
        # De lo contrario, el elemento solo puede estar presente
        # en el subarreglo derecho
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # El elemento no está presente en el arreglo
        return -1

# Ejercicio

def print_numbers(n):
    if n == 0:
        return print(n)
    else:
        print(n)
        return print_numbers(n - 1)

print_numbers(100)

# Ejercicios Extra

# Factorial de un Número
# El factorial de un número `n` (denotado como `n!`) es el producto de todos los números positivos menores o iguales a 
# `n`. Por definición, `0! = 1`.

def factorial(n):
    if n == 0:
        return 1  # Caso base
    else:
        return n * factorial(n - 1)  # Caso recursivo

# Fibonacci
# La secuencia de Fibonacci es una secuencia de números donde cada número es la suma de los dos anteriores, empezando 
# con 0 y 1. Es decir, Fib(0) = 0, Fib(1) = 1, y Fib(n) = Fib(n-1) + Fib(n-2) para n > 1.

def fibonacci(n):
    if n == 0:
        return 0  # Caso base 1
    elif n == 1:
        return 1  # Caso base 2
    else:
        return fibonacci(n-1) + fibonacci(n-2)  # Caso recursivo


myFactorialNumber = factorial(15)
print(myFactorialNumber)
myFiboNumber = fibonacci(15)
print(myFiboNumber)
