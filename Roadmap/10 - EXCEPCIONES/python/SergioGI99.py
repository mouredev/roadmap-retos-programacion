"""
-----------
EXCEPCIONES
-----------
EJERCICIO:
Explora el concepto de manejo de excepciones según tu lenguaje.
Fuerza un error en tu código, captura el error, imprime dicho error
y evita que el programa se detenga de manera inesperada.
Prueba a dividir "10/0" o acceder a un índice no existente
de un listado para intentar provocar un error.

DIFICULTAD EXTRA (opcional):
Crea una función que sea capaz de procesar parámetros, pero que también
pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
corresponderse con un tipo de excepción creada por nosotros de manera
personalizada, y debe ser lanzada de manera manual) en caso de error.
- Captura todas las excepciones desde el lugar donde llamas a la función.
- Imprime el tipo de error.
- Imprime si no se ha producido ningún error.
- Imprime que la ejecución ha finalizado.
"""

# Ejercicio

x = 10
y = 0

try:
    z = x / y
except Exception as e:
    print(f"Error:{e}")

print("Hello")
    
# Extra

inp_one = input("First input: ")
inp_two = input("Second input: ")

class MissingInputError(Exception):
    def __init__(self, info):
        self.info = info

def div(x_val, y_val):
    
    if x_val == "" or y_val == "":
        raise MissingInputError("Missing Input")
    else:
        x_val = float(x_val)
        y_val = float(y_val)
        result = (f"{x_val} / {y_val} = {x_val / y_val}")
        print(result)

try:
    div(inp_one, inp_two)
except Exception as error:
    print(f"Error:{error}({type(error).__name__})")
else:
    print("No se ha producido ningún error")
finally:
    print("Final de ejecución")