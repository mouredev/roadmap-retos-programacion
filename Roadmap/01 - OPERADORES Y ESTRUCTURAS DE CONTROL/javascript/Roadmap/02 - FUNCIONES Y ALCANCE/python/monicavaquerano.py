# 02 FUNCIONES Y ALCANCE
# Mónica Vaquerano
# https://monicavaquerano.dev

"""
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes posibilidades del lenguaje:
"""


# Sin parámetros ni retorno
def cuentaRegresiva():
    for i in range(10, -1, -1):
        if i == 0:
            print("Boom!")
        else:
            print(i, end=", ")


# Con parámetro, no retorno
def greeting(name: str):
    print(f"¡Hola, {name}!")


# Con uno o más parámetros y con retorno
def suma(a: int, b: int) -> int:
    return a + b


# Una lista como argumento
def printSortedList(list: list) -> list:
    list.sort()
    print(list)


# Parámetros arbitrarios, *args
def ultimaPersona(*persona):
    print("La última persona que vino fue " + persona[-1])


# Parámetros con keywords
def vocales(vocal1, vocal2, vocal3, vocal4, vocal5):
    print(
        f"Las vocales cerradas son {vocal4} y {vocal5}, las abiertas son {vocal3}, {vocal2} & {vocal1}."
    )


# Parámetros arbitrarios con keyword
def suApellido(**persona):
    print("Su apellido es " + persona["apellido"])


# Recursion
def recurrente(num: int) -> int:
    if num > 0:
        resultado = num + recurrente(num - 1)
        print(resultado, end=", ")
    else:
        resultado = 0
    return resultado


"""
* - Comprueba si puedes crear funciones dentro de funciones.
"""


def funcionPrincipal(string: str):
    def funcionSecundaria(string: string):
        for i in range(len(string)):
            if i % 2 == 0:
                print(f"\033[0;33m{string[i]}\033[0m", end="")
            else:
                print(f"\033[0;31m{string[i]}\033[0m", end="")
        print()

    return funcionSecundaria(string)


"""
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
"""

print("\nAlgunas funciones ya creadas en Python (Built-in Functions):")

lista = [5, 7, 4, 6, 1]

# Abs
print(f"abs(): el absoluto de -20 es: {abs(-20)}")
# Len
print(f"len(): la longitud de {lista} es de: {len(lista)}")
# Max
print(f"max(): el máximo en {lista} es: {max(lista)}")
# Min
print(f"min(): el mínimo en {lista} es: {min(lista)}")
# Pow
print(f"pow(): dos elevado al cuadrado es {pow(2,2)}")
# Print
print(f"print(): imprime los resultados en la consola. {True}, {None}, {lista}, etc.")
# Sorted
print(f"sorted(): la lista ({lista}) ordenada se ve así {sorted(lista)} ")
# Sum
print(f"sum(): la suma de todos los números en {lista} es igual a {sum(lista)}")


"""
* - Pon a prueba el concepto de variable LOCAL y GLOBAL. 
"""

print("\nVariable local y global:")

# Variable Global
nombre = "Juan"


def devolverNombre():
    # Variable Local
    nombre = "Carlos"
    return nombre


print(
    f"Yo regreso la variable global (nombre = {nombre})\nYo regreso la variable local dentro de la funcion (nombre = {devolverNombre()})."
)

"""
* - Debes hacer print por consola del resultado de todos los ejemplos.
*   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
"""

print("\nResultados de todos los ejemplos de funciones:")
cuentaRegresiva()
greeting("Monica")
print(f"1 + 2 = {suma(1, 2)}")
printSortedList([9, 0, 8, 1, 7, 2, 6, 3, 5, 4])
ultimaPersona("Emil", "Tobias", "Linus")
vocales(vocal2="e", vocal1="a", vocal3="i", vocal5="u", vocal4="o")
suApellido(nombre="Jane", apellido="Doe")
print("Función con recusión: ")
recurrente(3)
funcionPrincipal("Soy una string de prueba")


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


def miFuncion(string1: str, string2: str) -> int:
    counter = 0
    for i in range(1, 100):
        if i % 3 == 0 and i % 5 == 0:
            print(string1 + " " + string2, end=", ")
        elif i % 5 == 0:
            print(string2, end=", ")
        elif i % 3 == 0:
            print(string1, end=", ")
        else:
            print(f"\033[0;31m{i}\033[0m", end=", ")
            counter += 1
    print()
    return counter


print("\nDIFICULTAD EXTRA (opcional):")
x = miFuncion("hakuna", "matata")
print(f"\nNúmero de veces que se ha impreso el número en lugar de los textos:\n> {x}")
