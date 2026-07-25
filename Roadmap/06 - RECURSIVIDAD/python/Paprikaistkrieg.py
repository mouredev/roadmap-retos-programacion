#recursividad


"""
Recursividad es una técnica de programación donde una función se llama a sí misma para resolver un problema.
Cada llamada a la función trabaja en una versión más pequeña del problema hasta llegar a un caso base que se puede resolver directamente.
Es importante definir un caso base para evitar llamadas infinitas y asegurar que la recursión termine.
La recursividad es útil para problemas que pueden dividirse en subproblemas similares, como el cálculo de factoriales, 
la generación de secuencias (como Fibonacci) y 
la exploración de estructuras de datos (como árboles y grafos).
Sin embargo, la recursividad puede ser menos eficiente en términos de uso de memoria y tiempo de ejecución en comparación con las soluciones iterativas, 
especialmente para problemas con una gran profundidad de recursión.
Cada llamada a una función recursiva se apila en la memoria hasta que se alcanza el caso base, lo que puede llevar a un uso significativo de memoria.
Además, cada llamada a la función implica un pequeño overhead debido a la gestión de la pila de llamadas.
Por lo tanto, es importante considerar si la recursividad es la mejor solución para un problema específico, especialmente en casos donde la profundidad de recursión puede ser grande.
En algunos lenguajes de programación, como Python, existe un límite en la profundidad de recursión para evitar desbordamientos de pila, 
lo que puede ser una limitación para problemas que requieren una gran cantidad de llamadas recursivas.
En resumen, la recursividad es una herramienta poderosa en programación que puede simplificar la solución de ciertos problemas, 
pero debe usarse con cuidado debido a sus implicaciones en el rendimiento y el uso de memoria.
Es importante entender cuándo y cómo usar la recursividad de manera efectiva.
Además, algunas funciones recursivas pueden ser optimizadas mediante técnicas como la memorización o la recursión de cola para mejorar su eficiencia.
La memorización es una técnica de optimización que consiste en almacenar los resultados de funciones costosas para evitar cálculos redundantes en futuras llamadas con los mismos argumentos.
La recursión de cola es una forma de recursión donde la llamada recursiva es la última operación en la función, 
lo que permite optimizaciones por parte del compilador o intérprete para reutilizar el marco de pila actual y reducir el uso de memoria.
Sin embargo, Python no optimiza la recursión de cola, por lo que su uso no mejora el rendimiento en este lenguaje.
En conclusión, la recursividad es una técnica valiosa en programación que, cuando se usa adecuadamente, puede simplificar la solución de problemas complejos.
Sin embargo, es crucial considerar sus limitaciones y optimizaciones para garantizar un rendimiento eficiente.
"""

"""/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 */"""
def print_numbers(number: int) -> int: #aqui definimos la funcion, number es un parametro, print_numbers es el nombre de la funcion
    if number >= 0: #caso base, si el numero es mayor o igual a 0
        print(number) #imprime el numero
        return print_numbers(number-1) #llamada recursiva, se llama a si misma con el numero -1

def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print_numbers(100)
print(factorial(5))
print(fibonacci(8)) #Salida: 21
#La función print_numbers imprime números del 100 al 0 de forma recursiva.
#La función factorial calcula el factorial de un número dado de forma recursiva.
#La función fibonacci calcula el n-ésimo número de Fibonacci de forma recursiva.    
#Por ejemplo, fibonacci(8) devuelve 21, que es el 8º número en la sucesión de Fibonacci (0, 1, 1, 2, 3, 5, 8, 13, 21).
