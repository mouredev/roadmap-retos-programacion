"""
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
"""

#Función recursiva: es aquella función que se llama a si misma dentro de su propia ejecución

def print_numbers_recursive(start:int, end:int):
    if start <= end:
        print(start)
        print_numbers_recursive(start + 1, end)

print_numbers_recursive(0, 100)


#----EXTRA----

#Función factorial

def factorial(num:int) -> int:
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
    
answer = int(input("¿De qué número desea calcualr el factorial? "))

result = factorial(answer)
print(f"El factorial de {answer} es {result}")

#Función Fibonacci

def fibonacci(position:int):
    if position == 0:
        return 0
    elif position == 1:
        return 1
    else:
        return fibonacci(position - 1) + fibonacci(position - 2)
    
answer = int(input("¿Qué posición de la serie de Fibonacci desea conocer? "))    
    
result = fibonacci(answer)
print(f"El valor de Fibonacci de la posición {answer} es: {result}")
    
