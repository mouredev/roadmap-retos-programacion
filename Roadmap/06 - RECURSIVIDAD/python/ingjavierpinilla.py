"""

/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 */
 
 """


def imprime_numeros(n: int):
    if n < 0:
        return
    print(n)
    imprime_numeros(n - 1)


def factorial(n: int):
    if n == 0:
        return 1
    return n * factorial(n - 1)


# 1, 1, 2, 3, 5, 8, 13, 21


def fibonacci(n: int):
    print(f"calculando el fibonacci de: {n}")
    if n <= 1:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


def main():
    imprime_numeros(100)
    print(factorial(5))
    print(fibonacci(7))


if __name__ == "__main__":
    main()
