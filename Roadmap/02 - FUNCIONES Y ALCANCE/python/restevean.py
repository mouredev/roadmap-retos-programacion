"""
 * EJERCICIO:
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
 * - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 * - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 * - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 * - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue unas convenciones que debes de respetar para que el código se entienda.
"""


# Function without parameters or return
def greet():
    print("Hello, world!")


# Function with one parameter without return
def greet_person(name):
    print(f"Hello, {name}!")


# Function with multiple parameters without return
def greet_person_in_language(name, language):
    greetings = {"English": "Hello", "Spanish": "Hola", "French": "Salut"}
    print(f"{greetings[language]}, {name}!")


# Function with return
def add_numbers(a, b):
    return a + b


# Function within a function
def outer_function():
    def inner_function():
        print("Hello from the inner function!")

    inner_function()


# Test of local and global variables
global_var = "I'm a global variable"


def test_variables():
    local_var = "I'm a local variable"
    print(f"\n{local_var}, {global_var}.")


# Call to the functions
greet()
greet_person("Alice")
greet_person_in_language("Alice", "Spanish")
greet_person_in_language("John", "French")
greet_person_in_language("Helen", "English")
print(add_numbers(2, 3))
outer_function()
test_variables()

# Use of a built-in function
text = "Using a built-in function, print()"
print(text)

# Extra difficulty
print("\nExtra difficulty:")


def print_numbers_and_strings(str1, str2):
    my_count = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(str1 + str2)
        elif number % 3 == 0:
            print(str1)
        elif number % 5 == 0:
            print(str2)
        else:
            print(number)
            my_count += 1
    return f"Total elements printed {my_count}"


# Call the function
print(print_numbers_and_strings("Fizz", "Buzz"))
