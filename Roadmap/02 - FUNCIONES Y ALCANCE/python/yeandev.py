"""
Respuesta al ejercicio 02
/*
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
 */
"""

"""
Funciones definidas por el usuario
"""

# Función simple

def greet():
    print("Hola, Python!")

greet()

# Función con retorno

def return_greet():
    return "Hola, Python! Esto es un return"

print(return_greet())

# Función con un argumento

def arg_greet(name):
    print(f"Hola, {name}!")

arg_greet("Yean")

# Función con argumentos

def args_greet(greet, name):
    print(f"{greet}, {name}!")

args_greet("Hi", "Yean")
args_greet(name="Yean", greet="Hi")

# Función con un argumento predeterminado

def arg_greet(name="Python"):
    print(f"Hola, {name}!")

arg_greet("Yean")
arg_greet()

# Función con argumentos y return

def return_args_greet(greet, name):
    return f"{greet}, {name}!"

print(return_args_greet("Hi", "Yean"))

# Función con retorno de varios valores

def multiple_return_greet():
    return "Hola", "Python"

greet, name = multiple_return_greet()
print(greet)
print(name)

# Función con un número variable de argumentos

def variable_arg_greet(*names): # * número indefinido de valores
    for name in names:
        print(f"Hola, {name}!")

variable_arg_greet("Python", "Yean", "YeanGit", "Comunidad")

# Función con un número variable de argumentos con palabra clave

def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"{value} ({key})!")

variable_key_arg_greet(
    language="Python",
    name="Yean",
    alias="YeanGit",
    age=24
)

"""
Funciones dentro de funciones
"""

def outer_function():
    def inner_function():
        print("Función interna: Hola, Python!")
    inner_function()

outer_function()

"""
Funciones del lenguaje
"""

print(len("YeanGit")) # len cuenta la longitud de un objeto (str, list, tuple, dict, set o range)
print(type("H")) # type indica el tipo de dato de un objeto

"""
Variables locales y globales
"""

global_var = "Python"

def hello_python():
    local_var = "Hola"
    print(f"{local_var}, {global_var}!")

print(global_var)
# print(local_var) no se puede acceder desde fuera de la función

hello_python()

"""
Extra
"""

def print_numbers(text_1, text_2)-> int:
    count = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(text_1, text_2)
        elif number % 3 == 0:
            print(text_1)
        elif number % 5 == 0:
            print(text_2)
        else:
            print(number)
            count += 1
    return count 
print(print_numbers("Fizz", "Buzz"))