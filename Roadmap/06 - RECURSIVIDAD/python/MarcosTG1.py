"""
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
"""

def imprimir_numeros():
    for i in reversed(range(0, 101)):
        print(i)

# imprimir_numeros()

def countdown(number: int):
    if number == 0:
        print(number)
        return
    print(number)
    countdown(number - 1)
    
# countdown(100)


"""
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
"""

# lista_prueba = [5]

# resultado = lista_prueba[0] * 5

# print(resultado)

def calcular_factorial_norecursividad(numero: int):

    contenedor_resultado = 1

    for i in reversed(range(numero)):
        if numero >= 1:
            
            print(numero)

            contenedor_resultado = contenedor_resultado * numero
            print(contenedor_resultado)

            numero = numero - 1

    return contenedor_resultado

def calcular_factorial_norecursividad_corregido(numero: int) -> int:
    if numero < 0:
        raise ValueError("El factorial no está definido para números negativos.")

    resultado = 1
    # Multiplicamos directamente usando la variable i del bucle
    for i in range(1, numero + 1):
        resultado *= i

    return resultado

def calcular_factorial_recursividad(numero: int) -> int:
    if numero < 0:
        raise ValueError("No se aceptan números negativos para calcular el factorial")
    elif numero == 0:
        return 1 
    else:
        return numero * calcular_factorial_recursividad(numero - 1)


# contenedor_resultado = calcular_factorial_norecursividad(5)
# print(f"\nEl factorial calculado es: {contenedor_resultado}")

print(calcular_factorial_recursividad(5))

def fibonacci(posicion: int) -> int:
    """
    Recibe la posición y calcula el valor para dicha posición.
    """

    if posicion < 0:
        raise ValueError("El número debe de ser positivo cruck")

    elif posicion == 0:
        raise IndexError("La posición en la lista no puede ser 0")
    
    elif posicion == 1:
        return 0
    
    elif posicion == 2:
        return 1
    
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)


print(fibonacci(10))