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
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
"""

# FUNCIONES SIN PARÁMETROS

def greet() -> None:
    print('Hello there!')

# FUNCIONES CON PARÁMETROS

def greet_user(name: str, surname: str) -> None:
    print(f"Hello {name} {surname}!")

# FUNCIONES CON RETORNO

def add_two(num_one: int | float, num_two: int | float) -> int | float:
    return num_one + num_two

# FUNCIONES CON FUNCIONES DENTRO

def greet_user_with_inner (name: str, surname: str):
    def get_full_name(): return f"{name} {surname}"

    print(f"Hello {get_full_name()}!")

# BUILT IN FUNCTIONS

STRING_NUMBER = '11'
NUMBER = int(STRING_NUMBER)
print(f"STRING_NUMBER is {type(STRING_NUMBER)}, but NUMBER is {type(NUMBER)}")
# STRING_NUMBER is <class 'str'>, but NUMBER is <class 'int'>

# LLAMADA A LAS FUNCIONES

greet()

greet_user('Naia', 'Larrea')

print(add_two(2, 3))      # 5

greet_user_with_inner('Naia', 'Larrea')


"""
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

def print_numbers(text_one, text_two):
    counter = 0

    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print(f"{text_one}{text_two}")
        elif num % 3 == 0:
            print(text_one)
        elif num % 5 == 0:
            print(text_two)
        else:
            print(num)
            counter += 1

    return counter

print(print_numbers('fizz', 'buzz'))  # 53