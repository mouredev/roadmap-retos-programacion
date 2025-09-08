# Ejercicio 06 
"""
RECURSIVIDAD
"""
def cuenta_regresiva(n):
    # Caso base: cuando llegamos a -1, terminamos la recursión
    if n < 0:
        return
    # Imprimimos el número actual
    print(n)
    # Llamada recursiva con el siguiente número (n-1)
    cuenta_regresiva(n - 1)

# Llamamos a la función empezando en 100
cuenta_regresiva(100)
 
def factorial(facto):
    if facto == 0 or facto == 1:  # Caso base
        return 1
    else:
        return facto * factorial(facto - 1)  # Paso recursivo
    
resultado = factorial(5)  # Calcula 5! = 120
print(resultado)     

def fibonacci(number: int)-> int:
    if number <= 0:
        print("La posición tiene que ser mayor que cero.")
        return 0
    elif number <= 2:
        return number -1
    else:
        return fibonacci(number-1) + fibonacci(number-2)
    
print(fibonacci(10))

    
    

