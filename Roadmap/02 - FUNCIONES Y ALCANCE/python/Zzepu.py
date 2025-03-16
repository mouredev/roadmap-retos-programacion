"""
Funciones creadas por usuario
"""

# Simple

def piloto():
    print('Hamilton')

piloto()


# Con retorno

def auto():
    return 'Ferrari'

# autito = auto()
# print(autito)

print(auto())


# Con un argumento

def arg_pilot(name):
    print(f'El mejor piloto de la historia es {name}')

arg_pilot('Fangio')


# Mas de un argumento

def args_pilot(car, name):
    print(f'{car}, {name}')

args_pilot('Red Bull', 'Verstappen')


# Con un valor predeterminado

def default_arg_pilot(name='Leclerc'):
    print(f'Hi {name}!')

default_arg_pilot()


# Con argumentos y return

def return_args_pilot(car, pilot):
    return f'{car}, {pilot}'

print(return_args_pilot('McLaren', 'Norris'))

# Con retorno de varios valores

def multiple_return_team():
    return 'Alpha Tauri', 'Tsunoda'

team, pilot = multiple_return_team()
print(team)
print(pilot)


# Con un numero variable de argumentos

def variable_arg_team(*names):
    for name in names:
        print(f'Hola {name}!')

variable_arg_team('Red Bull', 'Ferrari', 'Mercedes')


# Con un numero variable de argumentos con palabra clave

def variable_key_arg_teams(**names):
    for key, value in names.items():
        print(f'{key} ({value})')

variable_key_arg_teams(
    car = 'W15',
    pilot = 'Hamilton',
    age = 35,
    alias = 'GOAT'
)


"""
Funciones dentro de funciones wtf?
"""

def outer_function():
    def inner_function():
        print('Hola Python!')
    inner_function()

outer_function()

"""
Funciones del propio lenguaje (built-in functions)
"""

print(len('Ferrari'))
print(type(44))


"""
Variables globales y locales
"""

global_var = 'Lewis'

def hello_drive():
    local_var = 'Hamilton'
    print(f'{global_var} {local_var}!')

print(global_var)
#print(local_var) No se puede llamar por fuera de la funcion

hello_drive()


"""
Ejercicio extra!
"""

def crazy_numbers(text1, text2):
    count = 0
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print(f'{text1} {text2}')
        elif num % 3 == 0:
            print(text1)
        elif num % 5 == 0:
            print(text2)
        else:
            print(num)
            count += 1
    return count

print(crazy_numbers('Lionel', 'Messi'))







