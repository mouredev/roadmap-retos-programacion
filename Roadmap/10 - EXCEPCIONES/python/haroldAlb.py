# EJERCICIO #
nombres = ["Greg", "Ideafix", "Canelo", "Kiwi", "Pia"]

for index, nombre in enumerate(nombres):
    print(f"{index}.{nombre}")
try:
    option = int(input("Opción: "))
    print(nombres[option])

except IndexError:
    print("Indice de lista fuera de rango")

print("Fin de la ejecución.")

# EXTRA #
class MinimumRangeError(Exception):
    def __str__(self):
        return "El dividendo debe ser mayor que el divisor" # Sobre escribo el método str para cuando imprima el error


def proceso_parametros(num1, num2):
    if num1 < num2:
        raise MinimumRangeError() # Lanzo la excepción que lo recoje el Except de donde se ejecuta el programa
    
    print(num1/num2)

try:
    proceso_parametros(4, 5)

except ZeroDivisionError:
    print("No es posible dividir entre 0.")

except TypeError:
    print("Sólo números enteros")

except Exception as e:
    print(f"{e}")

else:
    print("ningún error encontrado") # si no ha ocurrido ningun error se ejecuta el "else"

finally:
    print("Finalización del programa") # Tanto si se ejecuta lo del try como lo del except, lo del finally se ejecuta siempre