"#[número] - [lenguaje_utilizado]"
# 
# EJERCICIO:
# Explora el concepto de manejo de excepciones según tu lenguaje.
# Fuerza un error en tu código, captura el error, imprime dicho error
# y evita que el programa se detenga de manera inesperada.
# Prueba a dividir "10/0" o acceder a un índice no existente
# de un listado para intentar provocar un error.
# 
# DIFICULTAD EXTRA (opcional):
# Crea una función que sea capaz de procesar parámetros, pero que también
# pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
# corresponderse con un tipo de excepción creada por nosotros de manera
# personalizada, y debe ser lanzada de manera manual) en caso de error.
# - Captura todas las excepciones desde el lugar donde llamas a la función.
# - Imprime el tipo de error.
# - Imprime si no se ha producido ningún error.
# - Imprime que la ejecución ha finalizado.
# 
def serparacion(cadena):
    print('{}'.format(cadena * 20))

for i in range(5,-6,-1):
    try:
        result = 25/i
        print(f'25 / {i} = {25/i}')
    except ZeroDivisionError:
        print(f'No es posible la división ya que no se puede dividir entre {i}')


serparacion('-*-')
listNumberToPass = [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
]

for i in range(13):
    try:
        print(listNumberToPass[i])
    except IndexError:
        print(f'No hay valor en la posición {i} de la lista. {listNumberToPass}')

serparacion('-#-')
listNumberToPassb = [
        0, 2, 6, "A",
]
class MyOwnError(Exception):
    pass

def parameter_process(arguments):
    from random import randint
    numa  = randint(0,7)
    numb = randint(0,7)
    if numa == 7:
        raise MyOwnError
    return f'{arguments[numa]} / {arguments[numb]} = {arguments[numa] / arguments[numb]}'

for i in range(20):
    try:
        print(parameter_process(listNumberToPassb))
    except MyOwnError as excep:
        print(f'Se ha producido el error: {MyOwnError}: {excep}')
    except IndexError as excep:
        print(f'Se ha producido el error: {IndexError}: {excep}')
    except ZeroDivisionError as excep:
        print(f'Se ha producido el error: {ZeroDivisionError}: {excep}')
    except Exception as excep:
        print(f'Se ha producido el error: {Exception}: {excep}')
    else:
        print('No ha habido errores.')
    finally:
        print("Se ha terminado la ejecución")
        serparacion('-:-')
