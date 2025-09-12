# Función sin parámetros ni retorno
def hola():
    print('¿Esto es un retorno?')

hola()

# Función con parámetro sin retorno
def hola_y_medio(message: str):
    print(f'No soy un retorno, pero puedo mostrar un mensaje: {message}')

hola_y_medio('Wakanda!')

# Función con parámetro y retorno
def chao(message: str):
    return f'Soy un retorno y puedo llevar un mensaje: {message}'

print(chao('Viva Falcao!'))

# Función con retorno de varios valores

def multiple_return():
    return "Hola", "Python"


greet, name = multiple_return()
print(greet)
print(name)

# Con un número variable de argumentos


def variable_arg(*names):
    for name in names:
        print(f"Hola, {name}!")


variable_arg("Python", "Guillermo", "Colombia", "Voleibol")

print()

# Funciones dentro de funciones

def super_funcion():
    def sub_funcion():
        return 'Puedo crear funciones dentro de funciones!'
    return sub_funcion()
    
print(super_funcion())

print()

# Funciones ya creadas.

print(type(range(2)))
print(type(len(range(2))))
print(len(range(2))) # Longitud del rango de 0 a 1

print()

# Variable LOCAL y GLOBAL

variable_global = 'Soy una variable global'

def prueba_variables():
    variable_local = 'Soy una variable local'
    print(f"Desde una función: {variable_local}")
    print(f"Desde una función: {variable_global}")

prueba_variables()

try:
    print("Fuera de la función", variable_local)
except NameError as e:
    print("Nao nao, no existe. Error:", e)

print("Fuera de la función:", variable_global)

print()

# Ejercicio EXTRA

def extra(string_one: str, string_two: str) -> int:
    cuenta = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(f"Primera cadena: {string_one} más la segunda cadena: {string_two}")
        elif number % 3 == 0:
            print(f"Cadena de texto del primer parámetro: {string_one}")
        elif number % 5 == 0:
            print(f"Cadena de texto del segundo parametro: {string_two}")
        else:
            print(number)
            cuenta += 1
    return cuenta
    
print(extra('Hola!', 'Perú!'))