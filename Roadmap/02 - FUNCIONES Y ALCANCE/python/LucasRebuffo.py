""" /*
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
 */ """

## Funcion sin retorno y sin argumentos


from cgi import print_arguments


def saludar():
    print("Hola a todos!")


saludar()

## Funcion con retorno sin argumentos


def my_name():
    return "Lucas"


print(my_name())

## Funcion con retorno y argumentos


def suma(a, b):
    return a + b


print(suma(1, 1))


## Funcion con parametro por defecto


def saludo_default(nombre="Lucas"):
    print(f"Hola {nombre}")


saludo_default()


## Retorno multiple


def saludar_multiple():
    return "Hola", "Python"


saludo, name = saludar_multiple()

print(saludo)
print(name)

## Con numero variables de argumentos posicionales


def variables_args_saludo(*args):
    for name in args:
        print(f"Hola {name}")


variables_args_saludo("pablo", "comunidad", "Python")

## Con numero variable de argumentos pero con **kwargs


def kwargs_saludo(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")


kwargs_saludo(nombre1="lucas", nombre2="pepe", nombre3="numero")


## Funciones detro de otras


def funcion_exterior():
    def funcion_interna():
        print("Funcion interna: Hola Python")

    funcion_interna()


funcion_exterior()

## Funciones del lenguaje

print("Imprime el texto")

print(len("String"))
print(len([1, 2, 3]))

print(type(6))
print(type(True))
print(type("6"))

print(chr(45))

print(hash("Hola"))

## Variable locales y globales

variable_global = "Node.js"

print(variable_global)


def hello_node():
    variable_local = "Python"
    print(f"Hola, {variable_local} {variable_global}")


print(variable_global)

hello_node()

""" * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 * """


def print_numbers(cadena1: str, cadena2: str):
    contador = 0

    for num in range(1, 102):
        if num % 3 == 0 and num % 5 == 0:
            print(cadena1 + cadena2)
        elif num % 3 == 0:
            print(cadena1)
        elif num % 5 == 0:
            print(cadena2)
        else:
            print(num)
            contador += 1

    return contador

print(print_numbers("fizz", "buzz"))