# Ejercicio 

def contar_atras(n):
    if n < 0:
        return
    print(n)
    contar_atras(n-1)

print(contar_atras(100))

# Calcular el factorial de un número
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))


#  Fibonacci
def fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)

posicion = 10
print(f"El valor en la posición {posicion} de la sucesión de Fibonacci es: {fibonacci(posicion)}")