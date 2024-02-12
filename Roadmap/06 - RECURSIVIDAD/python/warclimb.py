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
def factorial(num_factorial):
    """Los factoriales son funciones matemáticas.
    Multiplican un número por todos los números que lo preceden.
    La fórmula del factorial puede expresarse como: = n ( n − 1 )
    """
    pass

# Calcular el valor de un elemento concreto (según su posición) en la sucesión de Fibonacci.
def fibonacci(num_fibonacci):
    """La secuencia de sucesión de Fibonacci tiene la fórmula
    Fn = Fn-1 + Fn-2 .
    En otras palabras, el siguiente número es una suma de los dos anteriores.
    Los dos primeros números son 1 , luego 2(1+1) , luego 3(1+2) , 5(2+3) y así sucesivamente: 1, 1, 2, 3, 5, 8, 13, 21...
    """
    pass

if __name__ == "__main__":
    # Llamamos a la funcion del ejercicio 1
    recursiva()
    factorial(58)