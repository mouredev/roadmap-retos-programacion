# EJERCICIO:
# Explora el concepto de manejo de excepciones según tu lenguaje.
# Fuerza un error en tu código, captura el error, imprime dicho error
# y evita que el programa se detenga de manera inesperada.
# Prueba a dividir "10/0" o acceder a un índice no existente
# de un listado para intentar provocar un error.

'''ZeroDivisionError'''

try:
    print(10 / 0)
except ZeroDivisionError as error:
    print(f"ZeroDivisionError: {error}")

'''ValueError'''

try:
    int('zero')
except ValueError as error:
    print(f"ValueError: {error}")

'''IndexError'''

numeros = [1, 2, 3, 4, 5]
index = 0
try:
    while index <= len(numeros):
        print(numeros[index])
        index += 1
except IndexError as error:
    print(f"IndexError: {error}")

'''TypeError'''

try:
    print(1 + '1')
except TypeError as error:
    print(f"TypeError: {error}")

'''NameError'''

try:
    print(my_name)
except NameError as error:
    print(f"NameError: {error}")

'''AttributeError'''

class Person:
    def __init__(self, nombres, apellidos):
        self.__nombres = nombres
        self.__apellidos = apellidos

    def get_nombres(self):
        return self.__nombres

    def get_apellidos(self):
        return self.__apellidos

try:
    my_person = Person('Gabriel', 'Halo')
    print(my_person.get_nombres())
    print(my_person.get_apellidos())
    print(my_person.get_edad())
except AttributeError as error:
    print(f"AttributeError as {error}")

'''ModuleNotFoundError'''

try:
    from video_games import game
except ModuleNotFoundError as error:
    print(f"ModuleNotFoundError: {error}")

'''KeyError'''

dict_people = {
    'user_01': {
        'username': 'HaloGabriel'
    }
}

try:
    print(dict_people['user_01'])
    print(dict_people['user_02'])
except KeyError as error:
    print(f"KeyError: {error}")

'''RecursionError'''

def loop():
    loop()

try:
    loop()
except RecursionError as error:
    print(f"RecursionError: {error}")
print()

# DIFICULTAD EXTRA (opcional):
# Crea una función que sea capaz de procesar parámetros, pero que también
# pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
# corresponderse con un tipo de excepción creada por nosotros de manera
# personalizada, y debe ser lanzada de manera manual) en caso de error.
# - Captura todas las excepciones desde el lugar donde llamas a la función.
# - Imprime el tipo de error.
# - Imprime si no se ha producido ningún error.
# - Imprimir que la ejecución ha finalizado.

class EmptyStrError(Exception):
    def __init__(self, placeholder):
        super().__init__(f"Empty value assigned to '{placeholder}'")

def check_python_programmer_data(name: str, surname: str, languages: list = []):
    print("Printing programmer name...")
    if name == '':
        raise EmptyStrError('name')
    if surname == '':
        raise EmptyStrError('surname')
    if type(name) != str:
        raise TypeError('Not valid string assigned to \'name\'')
    if type(surname) != str:
        raise TypeError('Not valid string assigned to \'surname\'')
    print(f"Programmer: ", name + ' ' + surname)
    print("Searching for 'Python' knowledge...")
    if 'Python' not in languages:
        raise ValueError('No \'Python\' found in languages')
    print(f"Found: {languages[languages.index('Python')]}")

def checking_for_exceptions(name: str, surname: str, languages: list = []):
    try:
        check_python_programmer_data(name, surname, languages)
    except EmptyStrError as error:
        print(f"{type(error).__name__}: {error}")
    except TypeError as error:
        print(f"{type(error).__name__}: {error}")
    except ValueError as error:
        print(f"{type(error).__name__}: {error}")
    except Exception as error:
        print(f"Unexpected Error: {error}")
    else:
        print("Programmer Data: OK")
    finally:
        print("Checking for Programmer Data finished\n")

print("=== EMPTY STR ERROR ===")
checking_for_exceptions('', 'Gabriel', ['Java', 'C++'])
checking_for_exceptions('Halo', '', ['Java', 'C++'])

print("=== TYPE ERROR ===")
checking_for_exceptions(10, 'Gabriel', ['Java', 'C++'])
checking_for_exceptions('Halo', 20, ['Java', 'C++'])

print("=== VALUE ERROR ===")
checking_for_exceptions('Halo', 'Gabriel', ['Java', 'C++'])

print("=== NO ERROR ===")
checking_for_exceptions('Halo', 'Gabriel', ['Python', 'C++', 'Python'])