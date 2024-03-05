'''
*EJERCICIO:
* Explora el concepto de manejo de excepciones según tu lenguaje.
* Fuerza un error en tu código, captura el error, imprime dicho error
* y evita que el programa se detenga de manera inesperada.
* Prueba a dividir "10/0" o acceder a un índice no existente
* de un listado para intentar provocar un error.
'''
#Distinto a otros lenguajes que utilizan Try Catch, en Python se usa try except:

try:
    # Intentar dividir por cero
    resultado = 10 / 0
except ZeroDivisionError as e:
    # Capturar la excepción ZeroDivisionError
    print(f"Error: {e}")
    resultado = None

print("Después de la excepción. Resultado:", resultado)

# Intentar acceder a un índice no existente en una lista
lista = [1, 2, 3]
try:
    elemento = lista[10]
except IndexError as e:
    # Capturar la excepción IndexError
    print(f"Error: {e}")
    elemento = None

print("Después de la excepción. Elemento:", elemento)


#Cada bloque except captura la excepción correspondiente, imprime el error y, en este caso, asigna un valor predeterminado es un variable despues del error
#para que se pueda asignar otro valor (None) para evitar que el programa se detenga abruptamente.

'''
