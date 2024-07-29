"""
  EJERCICIO
"""

def imprimir_descendente(n):
    # Caso Base: cuando n es menor que 0, terminamos la recursión
    if n < 0:
        return
    # Caso Recursivo
    # Imprimimos el número actual
    print(n)
    # Llamamos a la función con el siguiente número menor
    imprimir_descendente(n - 1)

# Llamamos a la función con el valor inicial 100
imprimir_descendente(100)

"""
 DIFICULTAD EXTRA
"""

def factorial(n):
    # Caso Base: el factorial de 0 o 1 es 1
    if n == 0 or n == 1:
        return 1
    # Caso Recursivo: n! = n * (n-1)!
    else: 
        return n * factorial(n - 1)

print(factorial(5))

def fibonacci(n):
    # Caso Base: la secuencia inicia con 0 y 1
    if n == 1:
        return 1
    elif n == 0:
        return 0
    # Caso Recursivo: fn: fn - 1 + fn - 2
    else: 
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print(fibonacci(10))
