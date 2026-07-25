"""
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
"""

def countdown(number: int):
    if number > -1:
        print(number)
        countdown(number - 1)

countdown(100)


"""
* DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
"""

def factorial(number: int) -> int:
    if number < 0:
        print("El factorial de numeros negativos no esta definido")
        return 0
    elif number > 0:
        return number * factorial(number - 1)
    else:
        return 1

my_number = 5
print(f"Fatorial de {my_number} = {factorial(my_number) if factorial(my_number) != 0 else "No definido"}")


"""
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
"""

def fibonacci(position: int) -> int:
    if position < 0:
        print("La posicion debe ser mayor que 0")
        return 0
    elif position == 1:
        return 0
    elif position == 2:
        return 1
    else:
        return fibonacci(position - 1) + fibonacci(position - 2)

my_position = -1
print(f"La posicion {my_position} de la secuencia de fibonacci es: {fibonacci(my_position)}")