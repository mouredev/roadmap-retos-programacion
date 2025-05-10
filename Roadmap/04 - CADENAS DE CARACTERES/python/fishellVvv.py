# operaciones
str1 = "Queso"
str2 = "supercalifragilistoespialidoso"

# concatenación
print(str1 + " y " + str2)

# repetición
print(str1 * 3)

# indexación
print(str1[0])

# longitud
print(len(str2))

# slicing
print(str1[:3], str1[2:4], str1[2:5] + "? " + str1[2:5], str1[2:4], str1)
print(str2[:3], str2[3:9], str2[26:], str2[1:10:2])

# busqueda
print("super" in str2)
print(str2.startswith("sup"))
print(str2.endswith("eso"))

# reemplazo
print(str2.replace("i", "."))

# división
print(str2.split("l"))

# mayúsculas y minúsculas
print(str1.upper())
print(str1.lower())
print(str2.capitalize())
print("victor vigil".title())

# eliminación de espacios iniciales y finales
print(" hola mundo  ".strip())

# busqueda de posición
print(str2.find("fragil"))

# busqueda de ocurrencias
print(str2.count("i"))

# formateo
print("El {} estaba {}!".format(str1.lower(), str2[:5]))

# interpolación
print(f"El {str1.lower()} estaba {str2[:5]}!")

# trasformación en lista de caracteres
print(list(str1))

# transformación de lista a cadena
list1 = ["El", str1, "estaba", str2[:5], "!"]
print("-".join(list1))

# transformaciones numéricas
str3 = "42"
str3 = int(str3)
print(str3)

# comprobaciones
print(str1.isalnum())
print(str1.isalpha())
print(str3.is_integer())

# EXTRA
def check(word1: str, word2: str):

    print("\nPalíndromos:")
    if word1 == word1[::-1]:
        print(f"{word1} es palíndromo.")
    else:
        print(f"{word1} no es palíndromo.")
    if word2 == word2[::-1]:
        print(f"{word2} es palíndromo.")
    else:
        print(f"{word2} no es palíndromo.")

    print("\nAnagrama:")
    if sorted(word1.lower().replace(" ", "")) == sorted(word2.lower().replace(" ", "")):
        print(f"{word2} es un anagram de {word1}.")
    else:
        print(f"{word2} no es un anagram de {word1}.")

    print("\nIsograma:")
    def isograma(word: str) -> bool:
        word_dict = dict()

        for character in word:
            word_dict[character] = word_dict.get(character, 0) +1

        return len(set(word_dict.values())) == 1
    
    if isograma(word1):
        print(f"{word1} es un isograma.")
    else:
        print(f"{word1} no es un isograma.")
    if isograma(word2):
        print(f"{word2} es un isograma.")
    else:
        print(f"{word2} no es un isograma.")

check("elle", "lele")