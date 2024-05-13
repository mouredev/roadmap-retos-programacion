
# RECURSIVIDAD

# Imprimir (recursivamente) del 100 al 0

def conteo_regresivo(x: int):
    if(x >= 0):
        print(x)
        conteo_regresivo(x-1)

print("Imprimiendo los números del 100 al 0 con recursividad...")
conteo_regresivo(100)

"""
DIFICULTAD EXTRA (opcional):
"""

print("\n ---- 🌩 DIFICULTAD EXTRA 🌩 ----\n")

# Factorial

def factorial(n: int):
    if(n>=1):
        return n*factorial(n-1)
    elif(n == 0):
        return 1;
    else:   
        print("WARNING! No se puede calcular el factorial de un número negativo.")

num = 9
print(f"{num}! = {factorial(num)}")


# Fibonacci

def fibonacci(pos: int):
    if(pos <= 0):
        print("WARNING! La posición debe ser un entero positivo.")
        return 0
    elif(pos == 1):
        return 0    
    elif(pos == 2):
        return 1
    else:
        return fibonacci(pos-1) + fibonacci(pos-2) 
    

num = 30
print(f"número #{num} de Fibonacci = {fibonacci(num)}")