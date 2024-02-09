'''
  EJERCICIO:  Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de 
  caracteres en tu lenguaje.
'''

# Concatenación de caracteres

name = 'César'
lastname = 'Carmona'
full_name = name + ' ' + lastname
print(full_name)
print('Hola %s %s' % (name, lastname))
print('{1} {0}, ¿Cómo estás?'.format(lastname, name))
print(f'Adiós {name} {lastname}')
numbers = ['16', '62', '35']
print(' '.join(numbers))

# repetición
print(name * 4)

# Indexación
print(name[0] + name[1] + name[2] + name[3])

# Longitud
print(len(lastname))

# Slicing (porción)
print(lastname[2:6])
print(lastname[2:])
print(lastname[0:2])
print(lastname[:2])

# Busqueda
print("a" in lastname)
print("i" in name)

# Reemplazo
print(lastname.replace("a", "x"))

# División
print(lastname.split("m"))

# Mayúsculas, minúsculas y letras en mayúsculas
print(lastname.upper())
print(name.lower())
print("hello world".title())
print("mexico city".capitalize())

# Eliminación de espacios al principio y al final
print(" cesar leroy ".strip())

# Búsqueda al principio y al final
print(lastname.startswith("ca"))
print(name.startswith("er"))
print(lastname.endswith("na"))
print(name.endswith("sar"))


# Comprobaciones varias
my_string = "123456"
print(my_string.isalnum())
print(my_string.isalpha())
print(my_string.isalpha())
print(my_string.isnumeric())

"""
Extra
"""


def check(word1: str, word2: str):

    # Palíndromos
    print(f"¿{word1} es un palíndromo?: {word1 == word1[::-1]}")
    print(f"¿{word2} es un palíndromo?: {word2 == word2[::-1]}")

    # Anagramas
    print(f"¿{word1} es anagrama de {word2}?: {sorted(word1) == sorted(word2)}")

    # Isogramas

    def isogram(word: str) -> bool:

        word_dict = dict()
        for character in word:
            word_dict[character] = word_dict.get(character, 0) + 1

        isogram = True
        values = list(word_dict.values())
        isogram_len = values[0]
        for word_count in values:
            if word_count != isogram_len:
                isogram = False
                break

        return isogram

    print(f"¿{word1} es un isograma?: {isogram(word1)}")
    print(f"¿{word2} es un isograma?: {isogram(word2)}")


check("radar", "pythonpythonpythonpython")
check("amor", "roma")