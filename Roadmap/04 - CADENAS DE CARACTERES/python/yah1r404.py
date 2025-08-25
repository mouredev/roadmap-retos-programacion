"""
OPERACIONES
"""

text1 = "Hola"
text2 = "Python"

# CONCATENACIÓN

print(text1 + ", " + text2 + "!")

# REPETICIÓN

print(text1 * 5)

# INDEXACIÓN

print(text1[0] + text1[1] + text1[2] + text1[3])

# LONGITUD

print(len(text2))

# SLICING (PORCIÓN)

print(text2[2:6])
print(text2[2:])
print(text2[0:2])
print(text2[:2])

# BÚSQUEDA

print("a" in text1)
print("m" in text1)

# REEMPLAZO

print(text1.replace("o", "a"))

# DIVISIÓN

print(text2.split("t"))

# MAYÚSCULAS Y MINÚSCULAS

print(text1.upper())
print(text2.lower())
print("yahir sulu".title())
print("yahir sulu".capitalize())

# QUITAR ESPACIOS

print(" yahir sulu ".strip())

# BÚSQUEDA AL PRINCIPIO Y AL FINAL

print(text1.startswith("Ho"))
print(text1.startswith("Py"))
print(text1.endswith("la"))
print(text1.endswith("thon"))

name = "Yahir sulu @yahir404."

# BÚSQUEDA DE POSICIÓN

print(name.find("yahir"))
print(name.find("Yahir"))
print(name.find("y"))
print(name.lower().find("y"))

# BÚSQUEDA DE OCURRENCIAS

print(name.lower().count("u"))

# FORMATEO

print("Saludo: {}, Lenguaje: {}!".format(text1, text2))

# INTERPOLACIÓN

print(f"Saludo: {text1}, Lenguaje: {text2}!")

# TRANSFORMACIÓN EN LISTA DE CARÁCTERES

print(list(name))

# TRANSFORMACIÓN DE LISTA EN CADENA

lista1 = [text1, ", ", text2, "!"]
print("-".join(lista1))

# TRANSFORMACIÓN NUMÉRICA

num = "12345"
num = int(num)
print(num)

num1 = "12345.54321"
num1 = float(num1)
print(num1)


# COMPROBACIONES VARIAS

print(text1.isalnum())
print(text1.isalpha())
print(text1.isnumeric())

"""
EXTRA TASK
"""

def analizar_palabras(palabra1, palabra2):

    # Palíndromo: se lee igual al derecho y al revés
    print(f"{palabra1} es palíndromo:", palabra1 == palabra1[::-1])
    print(f"{palabra2} es palíndromo:", palabra2 == palabra2[::-1])

    # Anagrama: tienen las mismas letras, orden diferente
    print("Son anagramas:", sorted(palabra1) == sorted(palabra2))

    def isogram(word: str) -> bool:
    # Creamos un diccionario para contar las apariciones de cada letra
        word_dict = dict()

        for character in word:
            word_dict[character] = word_dict.get(character, 0) + 1

    # Obtenemos la lista de cuántas veces aparece cada letra
        values = list(word_dict.values())
    
    # Tomamos el valor de repetición de la primera letra
        isogram_len = values[0]
        isogram = True

    # Comparamos todas las repeticiones con la primera
        for word_count in values:
            if word_count != isogram_len:
                isogram = False
                break

        return isogram
# Ejemplos:
    print("¿'aabbcc' es isograma?", isogram("aabbcc"))  # True
    print("¿'aabc' es isograma?", isogram("aabc"))      # False
    print("¿'abab' es isograma?", isogram("abab"))      # True

analizar_palabras("amor", "roma")