# EJERCICIO:
# Entiende el concepto de recursividad creando una función recursiva que imprima
# números del 100 al 0.

def imprimir_y_restar_uno(numero: int):
    print(numero)
    numero -= 1
    if numero >= 0:
        imprimir_y_restar_uno(numero)

def imprimir_hasta_cero(numero: int):
    imprimir_y_restar_uno(numero)

imprimir_hasta_cero(100)

# DIFICULTAD EXTRA (opcional):
# Utiliza el concepto de recursividad para:
# - Calcular el factorial de un número concreto (la función recibe ese número).

def multiplicar_por_el_entero_anterior(numero: int):
    resultado = 1
    if numero == 0:
        return resultado
    
    if numero - 1 >= 1:
        resultado = numero * (numero - 1)
        numero -= 2
        resultado *= multiplicar_por_el_entero_anterior(numero)
    return resultado

def calcular_factorial(numero: int):
    return multiplicar_por_el_entero_anterior(numero)

print(f"Factorial de 0: {calcular_factorial(0)}")
print(f"Factorial de 1: {calcular_factorial(1)}")
print(f"Factorial de 2: {calcular_factorial(2)}")
print(f"Factorial de 3: {calcular_factorial(3)}")
print(f"Factorial de 4: {calcular_factorial(4)}")
print(f"Factorial de 5: {calcular_factorial(5)}")

# - Calcular el valor de un elemento concreto (según su posición) en la
#   sucesión de Fibonacci (la función recibe la posición).

def continuar_sucesion_fibonacci(posicion: int):
    if posicion <= 1:
        return 0
    elif posicion <= 3:
        return 1
    else:
        return continuar_sucesion_fibonacci(posicion - 1) + continuar_sucesion_fibonacci(posicion - 2)

def calcular_fibonacci(posicion: int):
    return continuar_sucesion_fibonacci(posicion)

print(f"Sucesión de Fibonacci (0 elementos): {calcular_fibonacci(0)}")
print(f"Primer elemento en la Sucesión de Fibonacci: {calcular_fibonacci(1)}")
print(f"Segundo elemento en la Sucesión de Fibonacci: {calcular_fibonacci(2)}")
print(f"Tercer elemento en la Sucesión de Fibonacci: {calcular_fibonacci(3)}")
print(f"Cuarto elemento en la Sucesión de Fibonacci: {calcular_fibonacci(4)}")
print(f"Quinto elemento en la Sucesión de Fibonacci: {calcular_fibonacci(5)}")
print(f"Décimo elemento en la Sucesión de Fibonacci: {calcular_fibonacci(10)}")
print(f"Diecisieteavo elemento en la Sucesión de Fibonacci: {calcular_fibonacci(17)}")