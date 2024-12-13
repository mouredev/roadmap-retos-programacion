
try:
    print(10/0)

except Exception as e:

    print(f"se ha producido un error: {e}")

"""
Posibles errores: 
- división entre cero
- operación entre entero y string
- array fuera de rango
"""

"""
DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado.
"""

# personalizar un error

class ErrorPersonalizado(Exception):
    pass

def my_function(lista: list):
    if lista[0] == 0:
        raise ZeroDivisionError
    if lista[1] == 2:
        raise ErrorPersonalizado

try:
    my_function([0,0,3,4])
except ZeroDivisionError:
    print(f"Error en el segundo ejercicio")
except ErrorPersonalizado:
    print(f"Este es mi error personalizado mediante la clase que hereda de Exception")
else: 
    print("Este mensaje si no se produce ningún error.")
finally:
    print("Este mensaje se reproduce siempre")