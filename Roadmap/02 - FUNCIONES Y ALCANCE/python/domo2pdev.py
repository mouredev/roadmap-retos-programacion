"""
EJERCICIO:
 - Crea ejemplos de funciones basicas que representen las diferentes posibilidades del lenguaje: Sin parametros ni retorno, con uno o varios parametros, con retorno...
 - Comprueba si puedes crear funciones dentro de funciones.
 - Utiliza algun ejemplo de funciones ya creadas en el lenguaje.
 - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 - Debes hacer print por consola del resultado de todos los ejemplos.
   (tener en cuenta que cada lenguaje puede poseer mas o menos posibilidades)
 
 DIFICULTAD EXTRA (opcional):
 Crea una funcion que reciba dos parametros de tipo cadena de texto y retorne un numero.
- La funcion imprime todos los numeros del 1 al 100. Teniendo en cuenta que:
   - Si el numero es multiplo de 3, muestra la cadena de texto del primer parumetro.
   - Si el numero es multiplo de 5, muestra la cadena de texto del segundo parumetro.
   - Si el numero es multiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
   - La funcion retorna el numero de veces que se ha impreso el numero en lugar de los textos.
 
 Presta especial atencion a la sintaxis que debes utilizar en cada uno de los casos.
 Cada lenguaje sigue una convenciones que debes de respetar para que el codigo se entienda.
"""

# Funciones Definidas por el usuario


# Simple functions:
def greet():
    print("Hello, Python")


greet()


# Return functions:
def return_greet():
    return "Hello, Returned Python"


greet = return_greet()
print(greet)
print(return_greet())


# Functions with parameters:
def arg_greet(name):
    print(f"Hello, {name}")


arg_greet("Paul")


def square(number):
    return number**2


my_square = square(9)
print(my_square)
print(square(10))


def add(number_a, number_b):
    return number_a + number_b


add(1, 3)
print(add(1, 3))

# Functions with default parameters:


def circle_area(radius, pi=3.1416):
    return pi * (radius**2)


print(circle_area(15))
result_circle_area = circle_area(15)
print(result_circle_area)


# Keyword arguments:
def division(dividend, divisor):
    return dividend / divisor


print(division(divisor=5, dividend=10))
result_division = division(dividend=24, divisor=4)
print(result_division)

# Multiple return functions:


def multiple_return(place_a, place_b):
    return place_a, place_b


place_a, place_b = multiple_return("Place A", "Place B")
print(place_a)
print(place_b)


# Variable number of arguments: *args
def print_args_greet(*names):
    for name in names:
        print(f"Hello, {name}")


print_args_greet("Paul", "Paco", "Pepito", "Pepa", "Pepita")


def sum_args(*args):
    return sum(args)


print(sum_args(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# Variable number of keyword arguments: **kwargs
def print_kwargs_greet(**kwargs):
    for key, value in kwargs.items():
        print(f"Hello, {value}")


print_kwargs_greet(name="Paul", surname="Perez")


def variable_keyword_arg_mission(**names):
    for name in names.values():
        print(f"Mission, {name}")


variable_keyword_arg_mission(
    name="Jhon", surname="Connor", target="Yes", location="Unknown"
)

# Nested functions:


def outer_function():
    print("Outer function")

    def inner_function():
        print("Inner function")

    inner_function()


outer_function()

# Bilt-in functions:
# See https://pytthon.org for more information
print("Hello, World")
length = len("Hello, World")
print(length)

# Variable scope in Python:
global_var = "I am a global variable"  # Global variable


def print_global_var():
    print(global_var)


print_global_var()  # Outputs: I am a global variable

# Local variables:
# Local variables are accessible only within the scope of the method
# where they are declared.


def print_local_var():
    local_var = "I am a local variable"  # Local variable
    print(local_var)


print_local_var()

""" 
DIFICULTAD EXTRA (opcional):
 Crea una funcion que reciba dos parametros de tipo cadena de texto y retorne un numero.
   - La funcion imprime todos los numeros del 1 al 100. Teniendo en cuenta que:
   - Si el numero es multiplo de 3, muestra la cadena de texto del primer parumetro.
   - Si el numero es multiplo de 5, muestra la cadena de texto del segundo parumetro.
   - Si el numero es multiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
   - La funcion retorna el numero de veces que se ha impreso el numero en lugar de los textos.
"""


def print_numbers(text1, text2):
    count = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(text1 + text2)
        elif number % 3 == 0:
            print(text1)
        elif number % 5 == 0:
            print(text2)
        else:
            print(number)
            count += 1

    return count


print(print_numbers("Es multiplo de 3", "Es multiplo de 5"))
