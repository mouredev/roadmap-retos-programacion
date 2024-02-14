inicial = 100
def cientozero(inicial):
    if inicial >= 0:
        print(inicial)
        cientozero(inicial-1)
        
cientozero(inicial)

# Ejercicio EXTRA

print("Ejercicio EXTRA")

def factorial(numero: int) -> int:
    if numero == 1:
        return numero
    else:
        numero = factorial(numero-1)

print(factorial(3))