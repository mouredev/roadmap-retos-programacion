def sumaRecursiva (a,b):
    if b == 0:
        return a
    else:
        return sumaRecursiva(a+1,b-1)

print("Suma recursiva de 5 y 3: ")
print(sumaRecursiva(5,3))

def potenciaRecursiva(a,b):
    if b == 0:
        return 1
    else:
        return a * potenciaRecursiva(a,b-1)

print("Potencia recursiva de 2^3: ")
print(potenciaRecursiva(2,3))

def imprimir_numeros(numero):
    if numero >= 0:
        print(numero, end=" ")
        imprimir_numeros(numero - 1)

print("De 100 a 0 usando rercursividad: ")
imprimir_numeros(100)
print();

# Extra
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print("Factorial de 5: ")
print(factorial(5))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print("Fibonacci de 5: ")
print(fibonacci(5))

print("Vamos a comprobar ahora las funciones de factorial y fibonacci de forma interactiva")

print("Introduce un número para calcular su factorial: ")
n = int(input())
print(factorial(n))

print("Introduce un número para calcular su fibonacci: ")
n = int(input())
print(fibonacci(n))
