"""
Entiende el concepto de recursividad creando una función recursiva que imprima números del 100 al 0.
"""

'''
Función de Recursividad en Python

Una función recursiva en Python es una función que se llama a sí misma durante su ejecución. 
Esto permite dividir un problema complejo en subtareas más simples, 
hasta llegar a un caso base que se puede resolver directamente.

Ventajas y desventajas

- Ventajas:

Simplifica la implementación de algoritmos que requieren la repetición de operaciones similares.
Puede ser más fácil de leer y entender que un bucle iterativo.

- Desventajas:

Puede ser menos eficiente que un bucle iterativo, ya que cada llamada a la función recursiva crea una nueva pila de ejecución.
Se puede producir un error de “RecursionError” si la función se llama demasiadas veces, lo que puede causar un stack overflow.
'''

print("\nFUNCIÓN RECURSIVA\n")

def descent(value:int):
    if value >= 0:
        print(value)
        descent(value - 1)

mi_int = 100
descent(mi_int)

"""
DIFICULTAD EXTRA (opcional):
 Utiliza el concepto de recursividad para:
 - Calcular el factorial de un número concreto (la función recibe ese número).
 - Calcular el valor de un elemento concreto (según su posición) en la sucesión de Fibonacci (la función recibe la posición).
"""

print("\nFUNCIÓN FACTORIAL\n")

'''
Función factorial
La función factorial, representada por el símbolo !, es una fórmula matemática que se utiliza para calcular el producto de todos los números enteros positivos desde 1 hasta un número dado n. Se expresa como n!, donde n es el número del que se calcula el factorial.

Ejemplo
5! = 5 × 4 × 3 × 2 × 1 = 120
'''

def factorial(number:int):
    # Evitamos los número negativos
    if number < 0:
        print("Facilite un número positivo para el cálculo.")
        return 0
    elif number == 0:
        return 1
    else:
        # Al tener la función en el cálculo se consigue crear esa recrsividad restando al número hasta que no se cumple la condición
        return number * factorial(number - 1)

mi_factorial = 5 
print(factorial(mi_factorial))

print("\nFUNCIÓN FIBONACCI\n")

'''
La función de Fibonacci es una sucesión infinita de números naturales que se define recursivamente como:

F(n) = F(n-1) + F(n-2)

Donde F(0) = 0 y F(1) = 1.
'''

def fibonacci(number:int):
    # Evitamos los número negativos
    if number < 0:
        print("Facilite una posición en positivo")
        return 0
    # Los primeros números no son tan exactos por eso se ponen a fuego
    elif number == 0 or number == 1:
        return 0
    elif number == 2:
        return 1
    # Resto de números superiores o iguales a 3
    else:
        # Aplicamos la función de la explicación
        return fibonacci(number-1) + fibonacci(number-2)
    
mi_fibonacci = 10
print(fibonacci(mi_fibonacci))
