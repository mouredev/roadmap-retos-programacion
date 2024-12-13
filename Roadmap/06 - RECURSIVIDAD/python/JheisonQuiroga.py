"""
Recursividad

La recursividad es una técnica en la cual una función se llama así misma 
"""



# Ejemplo de recursividad
def numbers(n):
    if n <= 0:
        print(0)
    else:
        print(n)
        numbers(n - 1) # Imprime los números de 100 - 0

numbers(100)

"""
Extra
"""
# Calcular el factorial de un número

def factorial(n):
    if n <= 1:
        return n * 1 # Caso base
    else:
        return n * factorial(n - 1) # Llamada recursiva
    
print(factorial(5)) # 120

# Sucesión de fibonacci con recursividad

def fibonacci(n):
    if n == 0:  # Caso base 1
        return 0
    elif n == 1:  # Caso base 2
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) # Llamada recursiva

print("-" * 5, "Fibonacci", "-" * 5)
print("Resultado:" , fibonacci(3)) # Resultado de la funcion (fibonacci(2) = 1 + fibonacci(1) = 1) = 2


# Ejemplo con bucle del factorial
num = 5

for n in range(1, num):
    num *= n
    print(num)

# Ejemplo con bucle While

a, b = 0, 1

while a < 10:
    print(a)
    a, b = b, a + b
