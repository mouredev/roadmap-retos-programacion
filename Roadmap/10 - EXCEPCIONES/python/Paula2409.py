"""
/*
 * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado. 
 */
"""

my_list = [0,2,6]
# Try / Except: el programa continua
try:
    my_list[1]/my_list[0]
except ZeroDivisionError as error:
    print(f"Error: {error}")
# Else: se ejecuta si no hubo error
else:
    print('La division se pudo calcular')
# Finally: se ejecuta sin importar si hubo o no error
finally:
    print('Programa terminado')

try:
    print(my_list[3])
except IndexError:
    print('No existe ese indice')
    
# Raise: el programa se detiene
# if my_list[0] != 0:
#     my_list[1]/my_list[0]
# else:
#     raise ZeroDivisionError('No se puede dividir por 0')

# if len(my_list) > 3:
#     print(my_list[3])
# else:
#     raise IndexError

# Uso de Exception: clase base de excepciones. Identifica el error por si solo
try:
    print(my_list[3])
except Exception as error:
    print(f'Error con clase Exception: {error}')

# Jerarquia de clases
print(ZeroDivisionError.mro())

# Assert: chequea si una condicion se cumple. Si no es asi, el programa se detiene
a = 10
b = 15
assert a+b > 20, 'El resultado debe ser menor a 20'

class IncorrectType(Exception):
    def __init__(self, message='Valor incorrecto, ingrese un numero'):
        self.message = message
        super().__init__(self.message)
        
def division(a,b):
    if type(a) != int or type(b) != int:
        raise IncorrectType()
    elif b == 0:
        raise ZeroDivisionError()
    elif a == '' or b == '':
        raise TypeError()
    else:
        return a/b

try:
    dividir = division(5,4)
except IncorrectType as error:
    print(f'Error propio: {error}')
except ZeroDivisionError as error:
    print(f'Tipo de error: {type(error)}: {error}')
except TypeError as error:
    print(f'Tipo de error: {type(error)}: {error}')
else:
    print('La division se pudo realizar')
    print(dividir)

finally:
    print('El programa termino')
    
    
    