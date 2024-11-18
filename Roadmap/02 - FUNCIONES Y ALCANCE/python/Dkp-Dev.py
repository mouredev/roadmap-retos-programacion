"""EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 """

"""
Funciones definidas por el usuario
"""

# Funciones Simples

def greet():
    print("Hola Dkp!")

greet()

# Con retorno

def return_greet():
    return "Hola Dkp2!"

print(return_greet())

# Con un argumento

def arg_greet(name):
    print(f"Hola {name}!")

arg_greet("Perrito")

# Con argumentos

def args_greet(greet, name, name2):
    print(f"{greet} {name} y {name2}!")

args_greet("Hola","perrito","gato" )

# Con un argumento predeterminado

def default_arg_greet(name = "Conejo"):
    print(f"Hola {name}!")

default_arg_greet("Perrito")
default_arg_greet()

# Con argumentos, uno predeterminado y con cambios de posicion

def def_args_greet(greet, name, name2="conejo"):
    print(f"{greet} {name} y {name2}!")

def_args_greet("Hola","perrito")
def_args_greet(name2="gato",name="perrito",greet="Hola")

# Con argumentos y return

def return_arg_greet(greet,name):
    return f"{greet} {name}!!"

print(return_arg_greet(name="conejo",greet="Holaa"))

# Con retorno de varios valores

def multiple_return_greet():
    return "Hola","perrito"

greet, name = multiple_return_greet()
print(greet)
print(name)

# Con un numero variable de argumentos

def variable_args_greet(*names):
    for name in names:
        print(f"Hola {name}!!")

variable_args_greet("Perrito","Gato","Conejo","Tortuga")

# Con un numero variable de argumentos con palabra clave

def variable_key_args_greet(**names):
    for key, value in names.items():
        print(f"Hola {value} eres un ({key})!!")

variable_key_args_greet(
    canino="Perrito",
    felino="Gato",
    roedor="Conejo",
    anfibio="Tortuga"
)

"""
Funciones dentro de funciones
"""

def outer_function():
    def inner_function():
        print("Funcion interna")
    inner_function()
    
outer_function()

"""
Funciones dentro del lenguaje (built in)
"""

print("Hola Dkp")
print(len("Dkp"))
print(type("Dkp"))
print(type(29))

"""
Variables locales y globales
"""

global_variable = "Globo"

print(global_variable)

def greet():
    local_var = "Holaa"
    print(f"{local_var} {global_variable}!!")

greet()

print("Fin del ejercicio")

"""
DIFICULTAD EXTRA (opcional):
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

def extra(cadena1, cadena2) -> int:
    contador = 0
    for var in range(1,101):
        if var % 3 == 0 and var % 5 == 0:
            print(cadena1 + cadena2)
        elif var % 3 == 0:
            print(cadena1)
        elif var % 5 == 0:
            print(cadena2)
        else:
            print(var)
            contador += 1
    return contador


print(extra("Perro","Gato"))
