"""
EJERCICIO:
 - Crea ejemplos de funciones básicas que representen las diferentes
   posibilidades del lenguaje:
   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 - Comprueba si puedes crear funciones dentro de funciones.
 - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 - Debes hacer print por consola del resultado de todos los ejemplos.
   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)

 DIFICULTAD EXTRA (opcional):
 Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

 Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
"""

"""
Run a Mojo file.
1. Instalación del Mojo SDK 
  https://docs.modular.com/mojo/manual/get-started/

2. Run a Mojo file.
  mojo angelsanchezt.mojo
"""

"""
Funciones definidas por el usuario: Mojo soporta 2 tipos de funciones
def
fn
"""

# Simple

def greet():
    print("Hola, Python! def")

fn greet_fn():
    print("Hola, Python! fn")

# Con retorno

def return_greet():
    return "Hola, Python! def"

fn return_greet_fn() -> String:
    return "Hola, Python! fn"


# Con un argumento

def arg_greet(name):
    print("Hola, " + name + "!")

fn arg_greet_fn(name: String):
    print("Hola, " + name + "!")

fn greet2(name: String) -> String:
    return "Hello, " + name + "!"

# Con argumentos

def args_greet(greet, name):
    print(greet + "," + name + "!")

fn args_greet_fn(greet: String, name: String):
    print(greet + "," + name + "!")

# Con un argumento predeterminado

def default_arg_greet(name="Python"):
    print("Hola, " + name + "!")

fn default_arg_greet_fn(name: String ="Python" ):
    print("Hola, " + name + "!")


# Con argumentos y return

def return_args_greet(greet, name):
    return greet + ", " + name + "!"

fn return_args_greet_fn(greet: String, name: String) -> String:
    return greet + ", " + name + "!"

# Con retorno de varios valores

fn multiple_return_greet() -> Tuple[StringLiteral, StringLiteral] :
    return "Hola", "Python"

# Mojo aun no soporta variable de argumentos
# Mojo aun no soporta variable de argumentos con palabra clave.


"""
Funciones dentro de funciones
"""


def outer_function():
    def inner_function():
        print("Función interna: Hola, Python !")
    inner_function()



"""
Variables locales y globales
"""

let global_var = "Python"


def hello_python():
    let local_var = "Hola"
    print(global_var)
    print(local_var)
    # print(local_var + ", " + global_var + "!")


"""
Extra
"""


def print_numbers(text_1, text_2) -> Int:
    count = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(text_1 + text_2)
        elif number % 3 == 0:
            print(text_1)
        elif number % 5 == 0:
            print(text_2)
        else:
            print(number)
            count += 1
    return count

def main():
    greet()
    greet_fn()
    print(return_greet())
    print(return_greet_fn())
    arg_greet("AngelSanchezT")
    arg_greet_fn("AngelSanchezT")
    args_greet("Hi", "Angel")
    args_greet(name="Angel", greet="Hi")
    args_greet_fn("Hi", "Angel")
    args_greet_fn(name="Angel", greet="Hi")
    default_arg_greet("Angel")
    default_arg_greet()
    default_arg_greet_fn("Angel")
    default_arg_greet_fn()
    print(return_args_greet("Hi", "Angel"))
    print(return_args_greet_fn("Hi", "Angel"))

    var greet = ''
    var name = ''
    greet, name = multiple_return_greet()
    print(greet)
    print(name)

    outer_function()
    """
    Funciones del lenguaje (built-in)
    """

    print(len("AngelSanchezT"))


    print(global_var)
    # print(local_var) No se puede acceder desde fuera de la función

    hello_python()

    print(print_numbers("Fizz", "Buzz"))

    




