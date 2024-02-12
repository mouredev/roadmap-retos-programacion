"""
* EJERCICIO:
* Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
* en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
* - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
*   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
*
* DIFICULTAD EXTRA (opcional):
* Crea un programa que analice dos palabras diferentes y realice comprobaciones
* para descubrir si son:
* - Palíndromos
* - Anagramas
* - Isogramas
"""

# Asignacion de cadena
cadena = "Hola Python!!"
print(type(cadena))

numero = 10
texto = str(numero)
print(type(texto))

# Acceso a caracteres
print(cadena[2])  # Muestra el caracter en la posicion 2
print(cadena[-1])  # Muestra el ultimo caracter
print(cadena[0:4])  # Muestra los caracteres desde el 0 al 4 exclusive
print(cadena[5:])  # Muestra los caracteres desde la posicion 5 hasta el final
print(cadena[0:7:2])  # Muestra los caracteres desde el 0 al 7 de dos en dos
print(cadena[0::2])  # Muestra todos los caracteres de la cadena de dos en dos

# Buscar una subcadena en una cadena
sub = "Python"
print(sub in cadena)

# Longitud de cadena
print("Longitud: ", len(cadena))

# concatenacion
print(cadena + texto)
print(cadena, "Hola mundo!")

# Repeticion
print("-" * 30)

# Recorrido
for letra in cadena:
    print(letra)

# Conversion de letras
texto = "HOLA MUNDO!"
print(cadena.upper())  # Todo a mayusculas
print(texto.lower())  # Todo a minusculas
print(texto.capitalize())  # La primer letra de la oracion en mayuscula
print(texto.swapcase())  # Alterna mayuscula y minuscula

# Division en subcadenas
texto = "Juan-Jose-Pedro"
cadena = texto.split("-")
print(cadena)

# Union de cadenas
print(" - ".join(cadena))

# Verificacion
print(texto.isalnum())
print(texto.isalpha())

import re


# Dificultad extra
def insert_word():
    word = input("Ingrese una palabra: ")
    word = word.lower()
    if re.match("^[a-zñ]*$", word):
        return word
    else:
        print("Error, ingrese solo letras sin acentos")
        insert_word()


def palindromos(word):
    word_aux = word[::-1]
    if word_aux == word:
        return "es un palindromo"
    else:
        return "no es un palindromo"


def isogramas(word):
    word_aux = set(word)
    if len(word) == len(word_aux):
        return "es un isograma"
    else:
        return "no es un isograma"


word_1 = insert_word()
word_2 = insert_word()

if word_1 != word_2:
    # Verifica si son palindromos
    print(f"\nLa palabra {word_1} {palindromos(word_1)}")
    print(f"La palabra {word_2} {palindromos(word_2)}")

    # Verifica si son anagramas entre si
    if set(word_1) == set(word_2):
        print(f"\nLa palabra {word_1} es un anagrama de la palabra {word_2}")
    else:
        print(f"La palabra {word_1} no es un anagrama de la palabra {word_2}")

    # Verifica si son isogramas
    print(f"\nLa palabra {word_1} {isogramas(word_1)}")
    print(f"La palabra {word_2} {isogramas(word_2)}")
else:
    print("\nLas palabras son iguales")
