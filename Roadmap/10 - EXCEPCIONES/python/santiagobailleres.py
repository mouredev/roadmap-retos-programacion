'''EJERCICIO:
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
- Imprime que la ejecución ha finalizado. '''

# Manejo de excepciones en Python
try: # try sirve para intentar ejecutar un bloque de código
    # División por cero
    print(10/0)
except Exception as e:
    print(f'Error: {e} ({type(e).__name__})')

# error para acceder a un índice no existente
try:
    lista = [1, 2, 3]
    print(lista[3])
except Exception as e:
    print(f'Error: {e} ({type(e).__name__})')

# EXTRA
# Función que procesa parámetros y lanza excepciones
class StrTypeError(Exception): # Excepción personalizada
    pass

def process_params(params: list):
    if len(params) < 3:
        raise IndexError('La lista debe tener al menos 3 elementos') #raise lanza una excepción manualmente, lo que se pone entre paréntesis es el mensaje de error
    elif params[1] == 0:
        raise ZeroDivisionError('No se puede dividir por cero')
    elif type(params[2]) == str:
        raise StrTypeError('El tercer elemento no puede ser un string')

    print(params[2])
    print(params[0]/params[1])
    print(params[2]+5)

try:
    process_params([1, 1, 1])
except IndexError as e:
    print(f'Error: {e} ({type(e).__name__})')
except ZeroDivisionError as e:
    print(f'Error: {e} ({type(e).__name__})')
except StrTypeError as e:
    print(f'Error: {e} ({type(e).__name__})')
except Exception as e:
    print(f'Error: {e} ({type(e).__name__})')
else:
    print('No se ha producido ningún error')
finally:
    print('La ejecución ha finalizado')