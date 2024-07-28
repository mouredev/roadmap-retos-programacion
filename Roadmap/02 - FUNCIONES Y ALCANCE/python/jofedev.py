"""
    EJERCICIO:
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

"""
    Funciones definidas por el usuario
"""

            # Simples

def greet():
    print("Hola, cómo estás?")

greet()


            # Retorno

def return_def():
    return "Esta es un funcion con retorno"

return_functon = return_def()
print(return_functon)


            # Con un argumento

def arg_greet(name):
    print(f"Hola, {name}" )

arg_greet("Jose con un argumento!")


            # Con varios Argumentos

def args_greet(greet, name):
    print(f"{greet}, {name}")

args_greet("Hola", "Jose con varios argumentos!")


            # Con un argumento predeterminado

def pre_greet(name="Jose"):
    print(f"Hola, {name}, con un argumento predeterminado!")

pre_greet()

            # Con varios argumentos predeterminados

def pre_args_greet(greet= "Hola", name="Jose con varios argumentos predeterminados!"):
    print(greet, name)

pre_args_greet()


            # Con varios argumentos y return

def return_args_greet(greet, name):
    return f"{greet}, {name}"

print(return_args_greet("Hola", "Jose con varios argumentos y return!"))


            # Con retorno de varios valores

def return_greet_name():
    return "Hola", "Jose con retorno de varios valores!"

greet, name = return_greet_name()
print("Hola")
print("Jose con retorno de varios valores!")


            # Con un numero variable de argumentos


def variable_args_greet(*names):
    for name in names:
        print(f"Hola, {name}")

variable_args_greet("Jose", "Hola", "Estoy imprimiendo valores con un numero variables de argumentos")


            # Con un numero variable de argumentos con palabra clave

def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"Hola, {key} ({value})")

variable_key_arg_greet(
    nombre="Jose",
    saludo="Hola!"
)


"""
    Funcion dentro de otra funcion
"""

def outer_function():
    def inner_function():
        print("Estoy imprimiendo una funcion dentro de otra funcion")
    inner_function()

outer_function()

"""
    Funciones del lenguaje (built-in)
"""

print(len("Jose"))
print(type(6.3))
print("Jose".upper())
print("jose".capitalize())


"""
    Variables locales y globales
"""

global_variable = "Python"


def functtion_var():
    local_variable = "Hola"
    print(f"{local_variable}, {global_variable}")


functtion_var()



"""
    Extra
"""


def print_text(text_1, text_2) ->int:
    count = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(text_1 + text_2)
        elif i % 3 == 0:
            print(text_1)
        elif i % 5 == 0:
            print(text_2)
        else:
            print(i)
            count += 1 
    return count

print(print_text("fizz","buzz"))