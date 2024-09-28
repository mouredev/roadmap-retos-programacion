inicial = 100
def cientozero(inicial):
    if inicial >= 0:
        print(inicial)
        cientozero(inicial-1)
        
cientozero(inicial)

# Ejercicio EXTRA

print("Ejercicio EXTRA")

def factorial(numero: int) -> int:
    if numero < 0:
        print("El número debe ser mayor o igual que cero.")
        return 0
    elif numero == 0:
        return 1
    else:
        return numero*factorial(numero-1)

print(f"Factorial: {factorial(5)}")

def fibonacci(posicion:int) -> int:
    if posicion <= 0:
        print("La posición debe ser mayor a cero.")
        return 0
    elif posicion == 1:
        return 0
    elif posicion == 2:
        return 1
    else:
        return fibonacci(posicion-1) + fibonacci(posicion-2)
    
print(f"Fibonacci: {fibonacci(5)}")