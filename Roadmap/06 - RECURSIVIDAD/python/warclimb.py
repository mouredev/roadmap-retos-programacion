# #06 RECURSIVIDAD
#### Dificultad: Difícil | Publicación: 05/02/24 | Corrección: 12/02/24

## Ejercicio


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
# contar de 100 a 0
def recursiva():
    for num in range(100, -1, -1):
        print(num)


# Ejercicio extra
# Calcular el factorial de un número concreto (la función recibe ese número)
def factorial(n):
    """Los factoriales son funciones matemáticas que
    multiplican un número por todos los números que lo preceden.
    La fórmula del factorial puede expresarse como: = n ( n − 1 )
    """
    result = 1 # Almacenamos el resultado
    for i in range(1, n + 1): # recorremos desde 1 hasta el numero introducido en incrementos de 1
        result *= i # multiplicamos el resultado por el numero actual
    return result

# Calcular el valor de un elemento concreto (según su posición) en la sucesión de Fibonacci.
def fibonacci(fn):
    """La secuencia de sucesión de Fibonacci consiste en la fórmula:
    Fn = Fn-1 + Fn-2 .
    En otras palabras, el siguiente número es una suma de los dos anteriores.
    Los dos primeros números son 1 , luego 2(1+1) , luego 3(1+2) , 5(2+3) y así sucesivamente: 1, 1, 2, 3, 5, 8, 13, 21...
    """
    result = 0
    # recorremos desde 1 hasta el numero introducido en incrementos de 1
    for i in range(1, fn + 1):
        result += i # sumamos el el numero anterior por el actual
    return result

# Vamos a ello! Aqui llamamos las funciones
if __name__ == "__main__":
    # Llamamos a la funcion del ejercicio 1
    recursiva()

    # Llamamos a la funcion del factorial
    print(factorial(8)) # Factorial de 8 deberia dar 40320

    # Llamamos a la funcion de fibonacci
    print(fibonacci(8)) # Fibonacci de 8 deberia dar 36