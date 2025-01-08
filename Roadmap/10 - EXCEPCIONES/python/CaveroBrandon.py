"""EJERCICIO:
Explora el concepto de manejo de excepciones según tu lenguaje.
Fuerza un error en tu código, captura el error, imprime dicho error
y evita que el programa se detenga de manera inesperada.
Prueba a dividir "10/0" o acceder a un índice no existente
de un listado para intentar provocar un error."""


def division_by_zero():
    try:
        ans = 1 / 0
        print(ans)
    except ZeroDivisionError as e:
        print(f'Division by zero is not possible: {e}')
        print('****************')


def value_error():
    try:
        ans = int('abc')
        print(ans)
    except ValueError as e:
        print(f'Converting a string to int is not possible: {e}')
        print('****************')


def index_error():
    try:
        ans = []
        print(ans[5])
    except IndexError as e:
        print(f'Index not found: {e}')
        print('****************')


input('Press enter to try a division (1/0) - Division by zero')
division_by_zero()
input('Press enter to try convert a string to int')
value_error()
input('Press enter to try getting a non existing index')
index_error()


"""DIFICULTAD EXTRA (opcional):
Crea una función que sea capaz de procesar parámetros, pero que también
pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
corresponderse con un tipo de excepción creada por nosotros de manera
personalizada, y debe ser lanzada de manera manual) en caso de error.
- Captura todas las excepciones desde el lugar donde llamas a la función.
- Imprime el tipo de error.
- Imprime si no se ha producido ningún error.
- Imprime que la ejecución ha finalizado."""


class CustomError(Exception):
    def __init__(self, message='Custom Error'):
        self.message = message
        super().__init__(self.message)


def division(number):
    return 10 / number


while True:
    try:
        number = int(input('Enter the value to divide: '))
        if number < 0:
            raise CustomError('Negative numbers are not allowed')
        else:
            print(f'The function execution is completed, no errors were raised the division is: {division(number)}')
    except ZeroDivisionError as e:
        print(f'Division by zero is not allowed: {e}')
    except ValueError as e:
        print(f'The value must be a positive integer: {e}')
    except CustomError as e:
        print(f'The value cannot be a negative number: {e}')
