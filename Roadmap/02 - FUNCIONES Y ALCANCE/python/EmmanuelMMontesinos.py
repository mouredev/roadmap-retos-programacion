"""
 * EJERCICIO:
 * x Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * x Comprueba si puedes crear funciones dentro de funciones.
 * x Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * x Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * x Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */
"""

# Funciones
"""Sin Parámetros ni Retorno"""


def funcion_1():
    print("Esto es una función sin parámetros ni retorno\n")


funcion_1()

"""Con uno o varios Parámetros"""
parametro_1 = "Parámetro 1"
parametro_2 = "Parámetro 2"


def funcion_2(param_1, param_2):
    print(
        f"Esto es una función con uno o varios Parámetros sin retorno\nParámetros:\n{param_1}\n{param_2}\n")


funcion_2(parametro_1, parametro_2)

"""Con Retorno"""


def funcion_3():
    return "Esto es el retorno de funcion_3"


print(f"Esto es una función con retorno:\n{funcion_3()}\n")

"""Finciones dentro de funciones"""


def funcion_4():
    print("funcion_4\n")
    num_1 = 2
    num_2 = 3

    def funcion_5(num, num2):
        print("funcion_5 dentro de la funcion_4\n")
        return num + num2
    num_3 = funcion_5(num_1, num_2)
    return num_1 + num_2 + num_3


print(
    f"Esto es una función dentro de otra función:\nResultado {funcion_4()}\n")

"""Función ya creada en Python"""
print("Esto es una Funcíon ya creada en Python, ¿Es 1 un int):\n",
      isinstance(1, int), "\n")

"""Variables Locales"""
variable = "hola!"


def funcion_6():
    variable = "Ni hao!"
    return variable


print(f"Esto es una variable fuera de la función:\n{variable}")
print(
    f"Esto es una variable local con el mismo nombre que la de fuera:\n{funcion_6()}")
print(
    f"Sin modificar la variable existente fuera de la función:\n{variable}\n")

"""Varialbes Globales"""
variable = "hola!"


def funcion_7():
    global variable
    variable = "Ni hao!"
    return variable


print(f"Esto es una variable fuera de la función:\n{variable}")
print(f"Esto es una variable global dentro de la función:\n{funcion_7()}")
print(f"Esto es una variable fuera de la función despues:\n{variable}\n")

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
"""


def funcion_8(text_1: str = "Ping", text_2: str = "Pong") -> int:
    ciclo: int = 0
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print(f"{text_1} {text_2}")
        elif num % 3 == 0:
            print(f"{text_1}")
        elif num % 5 == 0:
            print(f"{text_2}")
        else:
            print(num)
            ciclo += 1
    return ciclo


print(
    f"Número de veces que se ha impreso el número en lugar de los textos:\n{funcion_8()}")
