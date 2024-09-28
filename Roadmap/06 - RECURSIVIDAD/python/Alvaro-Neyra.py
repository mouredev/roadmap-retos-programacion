
# * EJERCICIO:
# * Entiende el concepto de recursividad creando una función recursiva que imprima
# * números del 100 al 0.

# ** QUE ES LA RECURSIVIDAD?
# ** La recursividad en la programacion es una tecnica de una funcion que se llama a si misma durante su ejecucion. Este proceso
# ** se repite hasta que se cumpla una condicion base que evita que la funcion se llame recursivamente.

def recursive_function(number):
    if number == 0:
        print(number)
        return
    print(number)
    recursive_function(number - 1)

recursive_function(100)

# * DIFICULTAD EXTRA (opcional):
# * Utiliza el concepto de recursividad para:
# * - Calcular el factorial de un número concreto (la función recibe ese número).
def factorial_recursivo(numero):
    if numero == 1 or numero == 0:
        return 1
    return numero * factorial_recursivo(numero - 1)

resultado_del_factorial = factorial_recursivo(6)
print(f"Este es el resultado del factorial de 6: {resultado_del_factorial}")

# * - Calcular el valor de un elemento concreto (según su posición) en la 
# *   sucesión de Fibonacci (la función recibe la posición).
def fibonacci_factorial(number, diccionario_de_valores = {}):
    # Creamos la funcion fibonacci con un diccionario que guarda los valores de cada valor fibonacci
    # Si el argumento es menor a 0, no validar
    if (number < 0):
        return None
    elif (number == 0):
        return 0
    elif (number == 1):
        return 1
    # Si el valor del numero esta en el diccionario de valores de fibonacci, retornar
    elif number in diccionario_de_valores:
        return diccionario_de_valores[number]
    # Si no es 0 ni 1 entonces llamar a la funcion dos veces sumandolas:
    else:
        result = fibonacci_factorial(number - 1, diccionario_de_valores) + fibonacci_factorial(number - 2, diccionario_de_valores)
        # Guardar el valor de fibonacci en el diccionario con su clave y valor correspondiente
        diccionario_de_valores[number] = result
        # Retornar resultado
        return result
    
resultado_fibonacci = fibonacci_factorial(15)
print(resultado_fibonacci)