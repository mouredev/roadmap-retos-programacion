
# Operaciones con Strings tipo str

my_string = "Hola soy DevsDav "
print(my_string)

# Acceso a caracteres
print(my_string[0])  # Acceder al primer caracter
print(my_string[2:6])  # Acceder a un rango
print('')

# Recorrer un String
for caracter in my_string:
    print(caracter)

# Confirmar si existe uno o mas caracters en el String
print("DevsDav" in my_string)  # Si existe
print("DevDav" not in my_string)  # Si no existe

# Longitud de un String
print(f'La longitud del string es: {len(my_string)}')

# Conectar o Unir dos o mas Strings
print('Uniremos el mensaje ", soy ingeniero electrónico" al string anterior')
print(my_string + ", soy ingeniero electrónico")

# Convertir en mayúsculas todas las letras del String
print(my_string.upper())

# Convertir en minúsculas todas las letras del String
print(my_string.lower())


"""Podemos validar si todos los caracteres estan
en mayúsculas o minúscolas con isupper() o islower
Retornara True si es correcto."""

my_string = my_string.lower()

print(my_string.isupper())  # Verifica que este todo en mayúsculas
print(my_string.islower())  # Verifica que este todo en minúsculas

# Verificaciones

my_other_string = "123456789D"
print(my_other_string.isnumeric())  # Verifica si es númerico
print(my_other_string.isalnum())  # Verifica si es alfanúmerico
print(my_other_string.isalpha())  # Verifica si es alfabetico


"""strip() Retornar el string eliminando los espacios
en blanco iniciales y finales"""

print(my_string.strip())


"""string.split(a): retorna una lista con los elementos
del string que están separados por el string a. Si se
omite a, asume que el separador es uno o más espacios
en blanco o el salto de línea."""

print(my_string.split())


"""p.join(lista): suponiendo que p es un string, retor-
na un nuevo string conteniendo los elementos de la
lista "unidos" por el string p.
"""

print(my_string.join(['a', 'b', 'c']))


# replace(): Reemplazar un caracter en la cadena

print(my_string.replace("h", "H"))

# Repetición de un String
print(my_string * 3)


# count(a): Cuenta cuantas veces 'a' esta en la cadena
print(my_string.count("a"))


"""Extra
Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
"""


def is_anagram(word1: str, word2: str):

    if sorted(word1.lower()) == sorted(word2.lower()):
        return True
    return False


def is_palindrome(word1: str):

    bool_word1 = False
    if word1.lower() == word1.lower()[::-1]:
        bool_word1 = True

    return bool_word1


def is_isogram(word1: str):

    bool_word1 = True

    for caracter in word1:
        if word1.lower().count(caracter.lower()) < 2:
            bool_word1 = False

    return bool_word1


word_1 = input("Ingrese la palabra 1:")
word_2 = input("Ingrese la palabra 2:")

print(f"Las palabras son '{word_1}' y '{word_2}'")
print(f"¿{word_1} es un palindromo? {is_palindrome(word_1)}")
print(f"¿{word_2} es un palindromo? {is_palindrome(word_2)}")
print(f"¿{word_1} es un anagrama de '{word_2}'? {is_anagram(word_1, word_2)}")
print(f"¿{word_1} es un isograma? {is_isogram(word_1)}")
print(f"¿{word_2} es un isograma? {is_isogram(word_2)}")
