""" #04 CADENAS DE CARACTERES """


# Cadenas Base
string = "hola allan"
anotherString = "hola python"
stringStrip = "  hola allan  "

# Acceso a caracteres según indices
print("-- Acceso a caracteres según indices --")
print(f"{string}[0] = {string[0]}")  # h
print(f"{string}[:] = {string[:]}")  # hola allan
print(f"{string}[2:] = {string[2:]}")  # la allan
print(f"{string}[:5] = \"{string[:5]}\"")  # "hola "
print(f"{string}[-1] = {string[-1]}")  # n
print(f"{string}[::-1] = {string[::-1]}")  # nalla aloh

# Longitud

print("-- Longitud -- ")
print(f"{string} tiene {len(string)} caracteres")

# Reccorrido con for

print("-- Recorrido con for --")
for char in string:  # Orden normal del string
    print(char, end=", ")

print("")

for char in string[::-1]:  # Orden inverso del string
    print(char, end=", ")

# Concatenación

print("\n-- Concatenación --")
print(string + anotherString)  # Signo + con cadenas, concatena
print(f"{string} - {anotherString}")  # f string tambien concatena, da formato
# Con join, lo que está entre comillas dobles es el separador
stringList = list(string)
print("".join(stringList))

# Operaciones que regresan una copia de la cadena
print("-- Operaciones que regresan una copia de la cadena --")
# Regresa una copia de la cadena con el 1er caracter en Mayusculas
print(f"{string}.capitalize() = {string.capitalize()}")  # Hola allan
# Regresa una copia de la cadena con el 1er caracter de cada palabra en Mayusculas
print(f"{string}.title() = {string.title()}")  # Hola Allan
# Regresa una copia de la cadena con todos las caracteres en mayusculas
print(f"{string}.upper() = {string.upper()}")
# Regresa una copia de la cadena con todos los caracteres en minusculas
print(f"{string}.lower() = {string.lower()}")
# Regresa una copia de la cadena sin espacios a la izquierda
# "   hola allan   " regresa "holla allan   "
print(f"{stringStrip}.lstrip() = \"{stringStrip.lstrip()}\"")
# Regresa una copia de la cadena sin espacios a la derecha
# "   hola allan   " regresa "   holla allan"
print(f"{stringStrip}.rstrip() = \"{stringStrip.rstrip()}\"")
# Regresa una copia de la cadena sin espacios a la izquierda y derecha
# "   hola allan   " regresa "holla allan"
print(f"{stringStrip}.strip() = \"{stringStrip.strip()}\"")
# Regresa una copia de la cadena con el valor de la derecha reemplazando al de la izquierda
print(f"{string}.replace(\"allan\",\"mundo\") = {
      string.replace("allan", "mundo")}")

# Operaciones que devuelven otra cosa como indices, booleanos o estructuras de datos

# Regresa el indice menor donde se encuentra la cadena dentro de parentesis,
# devuelve -1 si no encuentra una coincidencia
print(string.find("ho"))  # 0
# Igual que find, solo que si no encuentra coincidencia, devuelve un error
print(string.index("la"))  # 2
# Devuelve True si todos los caracteres son letras
print(string.isalpha())  # False (Porque tiene un espacio)
# Regresa una tupla con 3 cadenas: anterior a ocurrencia, ocurrencia o separador, despues a ocurrencia
print(string.partition("a a"))  # ('hol','a a','llan')
# Regresa una lista con las palabras encontradas como cada valor
# Recibe un separador cualquiera, si no se agrega, toma el espacio como separador
print(string.split())  # ['hola', 'allan']


# ------------ EJERCIO ------------

print("\n---------- EJERCICIO ----------\n")

# Palabra/Frase sin espacios


def sentenceWithoutSpace(word):
    return word.lower().replace(" ", "")

# Palíndromo


""" Un palindromo es una palabra que se escribe igual al derecho y al reves
Por ejemplo: reconocer

En la función, comparamos la misma cadena, una en su forma original y otra en su forma inversa """


def palindrome(word):
    word = sentenceWithoutSpace(word)
    return word == word[::-1]


# Anagrama

""" Un anagrama es una palabra que con mover sus letras, puede crear otra distinta
Por ejemplo: Amor y Roma

En la función, ordenamos las letras de dos palabras y comparamos si tienen las mismas letras
validando que ambas palabras son anagramas """


def anagram(firstWord, secondWord):
    firstWord = sentenceWithoutSpace(firstWord)
    secondWord = sentenceWithoutSpace(secondWord)
    return sorted(firstWord) == sorted(secondWord)


# Isograma

""" Un isograma es una palabra cuyos caracteres son únicos.
Por ejemplo: Murcielago

En la función, regresamos True o False
Comparamos el numero de caracteres la palabra
La primera toma el numero de caracteres de la palabra real
la segunda toma el numero de caracteres del conjunto de la palabra real

Recuerda que un conjunto almacena entre llaves los caracteres sin ordenar y sin repetir """


def isogram(word):
    word = sentenceWithoutSpace(word)
    return len(word) == len(set(word))


# Principal


def main():
    firstWord = str(input("Ingresa la primer palabra: "))
    secondWord = str(input("Ingresa la segunda palabra: "))
    # Mensaje según el resultado de palindrome()
    message = "es Palindromo" if palindrome(firstWord) else "no es Palindromo"
    print(f"{firstWord} {message}")
    # Mensaje segun el resultado de anagram()
    message = "son Anagramas" if anagram(
        firstWord, secondWord) else "no son Anagramas"
    print(f"{firstWord} y {secondWord} {message}")
    # Mensaje segun el resultado de isogram()
    message = "es Isograma" if isogram(firstWord) else "no es Isograma"
    print(f"{firstWord} {message}")


main()
