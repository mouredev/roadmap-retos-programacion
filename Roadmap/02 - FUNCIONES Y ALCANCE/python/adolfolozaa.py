'''
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
'''
"""
Funciones definidas por el usuario
"""

# Simple

def saludos():
    print("Hola Amigos!!!")

saludos()

# Con retorno

def retorno_saludo():
    return "Hola Python!!!"

print(retorno_saludo())

# Con argumentos

def args_greet(greet, name):
    print(f"{greet}, {name}!!!")

args_greet("Hola", "Adolfo")
args_greet(name="Gaby", greet='Buen dia')

# Con argumento predeterminado

def arg_greet(name= 'ADOLFO'):
    print(f"{name}!!!")

arg_greet("Adolfo")
arg_greet()


# Con argumentos y retorno
def args_greet(greet, name):
    return f"{greet}, {name}!!!"

print(args_greet("Hi", "Francisco"))

# con retorno de varios valores

def multiple_return_greet():
    return "Hola", "Python"

greet, name = multiple_return_greet()
print(greet)
print(name)

# con un numero variable de argumentos

def variable_arg_greet(*names):
    for name in names:
        print(f"Hola, {name}!!!")

variable_arg_greet("rojo", 'azul', "verde", "blanco")

# con numer variable de argumentos con palabra clave

def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"{value} ({key})!!!")

variable_key_arg_greet(
    language = "Python",
    name = "Adolfo",
    alias = "ALA",
    age = 56
)

variable_key_arg_greet()

"""
Funciones dentro de funciones
"""

def outer_function():
    def inner_function():
        print("Funcion interna: Hola, Python")
    inner_function()
outer_function()

"""
Funciones del lenguaje (built-in)
"""

print('Tamano de la palabra: ' + str(len('Adolfo')) + ' letras')
print(type("Adolfo"))
print
("Adolfo Loza".upper())

"""
Variables locales y globales
"""
# Globales
global_var = "python"

print(global_var)

def hello_python():
    local_var = 'Hola'
    print(f"{local_var}, {global_var}!!!")

hello_python()
#print(local_var) no se puede acceder desde fuera de la funcion

"""
Dificultad Extra
Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
"""

def print_numbers(texto_1, texto_2) -> int:
    counter = 0
    for number in range(0,101):
        if number % 3 == 0 and number % 5 == 0:
            print(texto_1 +' '+ texto_2)
        elif number % 3 == 0:
            print(texto_1)
        elif number % 5 == 0:
            print(texto_2)
        else:
            print(number)
            counter += 1
    return counter
            
print(print_numbers('Fizz', 'Buzz'))






