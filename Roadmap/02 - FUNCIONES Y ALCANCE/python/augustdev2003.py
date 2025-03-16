"""
Funciones definidas por el usuario
"""

# Vacía


def empty():
    pass

# Simple


def simple():
    print('Simple Function')


simple()

# Con retorno


def with_return():
    return "Return function"


print(with_return())

# Con argumento


def with_argument(city):
    print(f'Vivo en {city}.')


with_argument('Madrid')

# Con argumentos


def with_arguments(name, age):
    print(f'Me llamo {name} y tengo {age} años.')


with_arguments('Augusto', '20')
with_arguments(age=20, name='Augusto')

# Argumento predeterminado


def default_arg(name, greet='Hi'):
    print(f'{greet}, {name}')


default_arg('Pedro')
default_arg('Pedro', 'Hello')

# Argumentos y retorno


def args_return(name, surname):
    return f'{name} {surname}'


print(args_return('Pablo', 'Gonzalez'))

# Retorno de varios valores


def multiple_values():
    return 'Hi', 'Python'


greet, name = multiple_values()
print(greet)
print(name)

# Número variable de argumentos


def variable_args(*countries):
    for country in countries:
        print(f'Vivo en {country}')


variable_args('Argentina', 'Jamaica', 'España', 'Inglaterra')

# Número variable de argumentos con palabra clave


def variable_key_arg(**ages):
    for key, value in ages.items():
        print(f'{key}: {value}')


variable_key_arg(
    name='Augusto',
    age=20,
    language='Python',
    birthday='2003-08-28'
)

"""
Funciones dentro de funciones
"""


def outside():
    def inside():
        print('Estoy dentro de la función')
    inside()


outside()

"""
Funciones propias del lenguaje
"""

lenguaje = 'Python'
print(len(lenguaje))
print(type(lenguaje))
print(lenguaje.index('on'))

"""
Globales y locales
"""

variable_global = 'Python'


def hello():
    variable_local = 'Hola'
    print(f'{variable_local} {variable_global}')


print(variable_global)
# print(variable_local) # No se puede acceder a esta variable ya que se encunetra dentro de la función

"""
Extra
"""


def print_numbers(text1, text2) -> int:
    count = 0
    for n in range(1, 101):
        if n % 15 == 0:
            print(text1 + text2)
        elif n % 3 == 0:
            print(text1)
        elif n % 5 == 0:
            print(text2)
        else:
            print(n)
            count += 1
    return count


print(print_numbers('Hola', 'Python'))
