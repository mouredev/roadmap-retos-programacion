# EJERCICIO:
# - Crea ejemplos de funciones básicas que representen las diferentes
#   posibilidades del lenguaje:
#   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...

# Sin parámetros y sin retorno
def print_hello_world():
    print("Hello, World!")
print_hello_world()

# Sin parámetros y con retorno
def get_username():
    return "HaloGabriel"
username = get_username()
print(username)

# Con un parámetro y sin retorno
def print_username(username = "USER"):
    print(username)
print_username()
print_username("HaloGabriel")

# Con un parámetro y con retorno
def elevar_al_cuadrado(number: int):
    return number ** 2
result = elevar_al_cuadrado(10)
print(f"10 ** 2 = {result}")

# Con dos parámetros y sin retorno
def print_evens_by_range(end, start = 0):
    evens_count = 0
    if start > end:
        print(f"Rango no válido: {start} a {end}")
        return
    for number in range(start, end + 1):
        if number % 2 == 0:
            print(number)
            evens_count += 1
    if evens_count == 0:
        print(f"Ningún número para hallado en rango de {start} a {end}")
print_evens_by_range(20)
print()
print_evens_by_range(end = 1, start = 10)
print()

# Con dos parámetros y con retorno
def sumar_dos_numeros(num1: int, num2: int):
    return num1 + num2
suma = sumar_dos_numeros(5, 24)
print(f"5 + 24 = {suma}\n")

# Con un parámetro arbitrario y sin retorno
def print_odds(*numbers):
    odds_count = 0
    for number in numbers:
        if type(number) == int:
            if number % 2 != 0:
                print(number)
                odds_count += 1
    if odds_count == 0:
        print("No se hallaron números impares")
print_odds(1, "Halo", 2, 3, "Gabriel", 4, 5, 6, 6.7, 7, 8, 9, 10, True)
print()
print_odds("Halo", 2, "Gabriel", 4, 6, 6.7, 8, 10, True)

# Con un parámetro arbitrario y con retorno
def return_only_with_numbers_value(**kwargs):
    numbers_data = {}
    for k, v in kwargs.items():
        if type(v) == int or type(v) == float:
            numbers_data[k] = v
    return numbers_data
numbers_data = return_only_with_numbers_value(name="Gabriel", age=25, day="Monday", random_float=10.5)
print(numbers_data)
numbers_data = return_only_with_numbers_value(name="Gabriel", day="Monday")
print(numbers_data)
    
# - Comprueba si puedes crear funciones dentro de funciones
def sumar_dos_numeros(num1: int, num2: int):
    def suma(num1: int, num2: int):
        return num1 + num2
    return suma(num1, num2)
suma = sumar_dos_numeros(6, 7)
print(f"6 + 7 = {suma}")

# - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
my_string = "Halo Gabriel"
print(my_string.upper())
print(my_string.lower())
print(len(my_string))
print(print("XD"))
print(my_string.split(sep = " "))

# - Pon a prueba el concepto de variable LOCAL y GLOBAL.

# Variable Global - Puede ser usada dentro de funciones y fuera de ellas también
global_variable = "HaloGabriel"
def my_function():
    print(f"Usada dentro de funciones: {global_variable}")

print(f"Usada fuera de funciones: {global_variable}")
my_function()

# Variable Local - Puede ser usada solo dentro de su función
def my_other_function():
    local_variable = "Python"
    print(f"Usada dentro de funciones: {local_variable}")

my_other_function()
#print(f"Usada fuera de funciones (lanza error): {local_variable}")
print()

# DIFICULTAD EXTRA (opcional):
# Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
# - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
#   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
#   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
#   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

def special_function(string_one: str, string_two: str) -> int:
    count = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(string_one, string_two)
        elif number % 3 == 0:
            print(string_one)
        elif number % 5 == 0:
            print(string_two)
        else:
            print(number)
            count += 1
    return count

count = special_function("Halo", "Gabriel")
print(f"Se imprimieron {count} veces un número en lugar de un texto.")