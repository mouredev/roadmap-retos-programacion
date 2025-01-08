def imprimir_numeros(n):
    if n < 0:
        return
    print(n, end=" ")
    imprimir_numeros(n - 1)


imprimir_numeros(100)


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def fibonacci(pos):
    if pos <= 1:
        return pos
    return fibonacci(pos - 1) + fibonacci(pos - 2)


print("\n")
print("Factorial de 5:", factorial(5))
print("Elemento en la posición 7 de Fibonacci:", fibonacci(7))
