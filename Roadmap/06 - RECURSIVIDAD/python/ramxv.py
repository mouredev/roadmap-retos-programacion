''' 
La Recursion es un proceso en el que una función se llama a sí misma 
de forma repetida hasta que se satisface una condición específica.
'''
def vamo_pa_atras(n) -> int:
    if n == 0:
        print(n, end=" ")
        return 0
    print(n, end=" ")
    return vamo_pa_atras(n-1)
  
vamo_pa_atras(100)

# EXTRAS #

print("\n\n### FACTORIAL ###\n")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

# n = int(input("Ingrese un número: "))
# print(f"El factorial de {n} es =", end=" ")
print("El factorial es =",factorial(5))

print("\n### FIBONACCI ###\n")

suma_count = 0

def fibonacci(posicion):
    global suma_count
    if posicion < 2:
        return posicion
    suma_count += 1
    return fibonacci(posicion-1) + fibonacci(posicion-2)
        

print("El valor del elemento es =",fibonacci(10),"\n")
print(f"Se realizaron {suma_count} sumas para calcular el número de Fibonacci\n")
