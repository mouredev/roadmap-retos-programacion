#02 - Python

""" * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
"""

# Función sin parámetros ni retorno
def greet():
    print("Hello, world!")

# Función con un parámetro
def greet_person(name):
    print(f"Hello, {name}!")

# Función con múltiples parámetros
def add_numbers(num1, num2):
    return num1 + num2

# Función con retorno
def square_number(num):
    return num ** 2

# Función dentro de una función
def outer_function():
    def inner_function():
        print("This is an inner function")
    inner_function()

# Uso de una función incorporada en Python
def show_length(s):
    print(len(s))

# Variable global y local
x = "global"

def test_scope():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)

# Llamada a las funciones
greet()
greet_person("Francisco")
print(add_numbers(5, 3))
print(square_number(4))
outer_function()
show_length("Hello, world!")
test_scope()


# Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
def print_numbers_and_strings(str1, str2):
    count = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(str1 + str2)
        elif i % 3 == 0:
            print(str1)
        elif i % 5 == 0:
            print(str2)
        else:
            print(i)
            count += 1
    return count

# Llamada a la función
print(print_numbers_and_strings("perro", "salchicha"))