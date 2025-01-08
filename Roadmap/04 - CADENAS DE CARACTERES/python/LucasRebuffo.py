""" /*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */ """

""" Operaciones con Strings """

import re
from xmlrpc.client import Boolean


my_string_1 = "Hola"
my_string_2 = "Lucas"

# Concatenacion
print(my_string_1 + " " + my_string_2)

# Repeticion
print(my_string_2 * 5)

# Indexacion
print(my_string_1[0] + my_string_2[1])

# Longitud
print(len(my_string_1))
# Slicing (partir la cadena de texto)
print(my_string_1[1:3])
print(my_string_2[1:])
print(my_string_1[:-1])
print(my_string_2[0:3])
print(my_string_1[:2])

# Reemplazo
print(my_string_1.replace("a", "x"))

# Busqueda
print("h" in my_string_1)
print("x" in my_string_2)

# Division
print(my_string_2.split("c"))

# Mayusculas y minusculas
print(my_string_1.upper())
print(my_string_1.lower())
print(my_string_1.capitalize())
print(my_string_1.title())


# Eliminacion de espacios (strip)
print("Lucas Rebuffo".strip())

# Busqueda al principio y al final
print(my_string_1.startswith("Ho"))
print(my_string_2.endswith("as"))

# Busqueda de posicion
print("lucasrebu@outlook.com".find("@"))
print("lucasrebu@outlook.com".find("@"))
print("lucasrebu@outlook.com".find("u@"))

# Busqueda de ocurrencias
print("Lucas Rebuffo".count("f"))

# Formateo
print("{} {} !".format(my_string_1, my_string_2))

# Interpolacion
print(f"{my_string_1} {my_string_2} !")

# Transferencia de lista de caracteres
lista_char = list(my_string_1)
print(lista_char)
print("-".join(lista_char))

# Transformacion numerica
print(int("452"))
print(float("452.2"))

# Comprobaciones
print("151".isdecimal())
print("151a".isalnum())
print("a".isascii())
print("def".isidentifier())


"""  * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */ """


def is_palindrome(cadena: str):
    return cadena[::-1].strip().lower() == cadena.strip().lower()


def is_anagram(cadena1: str, cadena2: str):
    return sorted(cadena1.lower()) == sorted(cadena2.lower())


def is_isogram(cadena: str):
    set_caracteres = set(cadena)
    lista = list(map(lambda char: cadena.count(char), set_caracteres))
    r = set(lista)
    return len(r) == 1


def chequear_palabras(cadena1: str, cadena2: str):

    print("Chequeo de palindromo: ")
    if is_palindrome(cadena1):
        print(f"{cadena1} es palindromo")
    else:
        print(f"{cadena1} NO es palindromo")
    if is_palindrome(cadena2):
        print(f"{cadena2} es palindromo")
    else:
        print(f"{cadena2} NO es palindromo")

    print("----------------------------------------")

    print("Chequeo de anagrama: ")
    if is_anagram(cadena1, cadena2):
        print(f"{cadena1} y {cadena2} son anagramas")
    else:
        print(f"{cadena1} y {cadena2} NO son anagramas")

    print("----------------------------------------")

    print("Chequeo de isograma: ")
    if is_isogram(cadena1):
        print(f"{cadena1} es isograma")
    else:
        print(f"{cadena1} NO es isograma")
    if is_isogram(cadena2):
        print(f"{cadena2} es isograma")
    else:
        print(f"{cadena2} NO es isograma")

    print("----------------------------------------")
    print("----------------------------------------")


chequear_palabras("amor", "roma")
chequear_palabras("neuquen", "quenneu")
