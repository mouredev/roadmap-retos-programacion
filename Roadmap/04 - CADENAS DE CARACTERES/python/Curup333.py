"""
Operaciones
"""

from operator import le


s1 = "Hola"
s2 = "Python"

# Concatenacion
print(s1 + ", " + s2 + "!")

# Repeticion
print(s1 * 3)

# Indexacion
print(s1[0] + s1[1] + s1[2] + s1[3])

# Longitud
print(len(s2))

# slicing (porcion)
print(s2[2:6])
print(s2[2:])
print(s2[0:2])
print(s2[:2])

# Busqueda
print("a" in s1)
print("i" in s1)

# Remplazo
print(s1.replace("o", "a"))

# Divicion
print(s2.split("t"))


# Mayusculas y minusculas
print(s1.upper())
print(s1.lower())
print("angel curup".title())
print("angel curup".capitalize())

# Eliminacion de espacios al principio y al final
print(" angel curup ".strip())

# Busqueda al principio y al final
print(s1.startswith("Ho"))
print(s1.startswith("Py"))
print(s1.endswith("la"))
print(s1.endswith("thon"))

s3 = "Angel Curup @curup"

# Busqueda de posicion
print(s3.find("curup"))
print(s3.find("Curup"))
print(s3.find("C"))
print(s3.lower().find("c"))

# Busqueda de ocurrencias
print(s3.lower().count("c"))

# Formateo
print("Saludo: {}, lenguaje: {}!".format(s1, s2))

# Interpolacion
print(f"Saludo: {s1}, lenguaje: {s2}!")

# transformacion en lista de caracteres
print(list(s3))

# Transformacion de lista en cadena
l1 = [s1, " ", s2, "!"]
print("-".join(l1))

# Transformacion numericas
s4 = "123456"
s4 = int(s4)
print(s4)

s5 = "123456.123"
s5 = float(s5)
print(s5)

# Comparaciones varias
s4 = "123456"
print(s1.isalnum())
print(s1.isalpha())
print(s4.isalpha())
print(s4.isnumeric())


"""
Extra
"""


def check(word1: str, word2: str):
    # Palindromos
    print(f"{word1} es un palindromo?: {word1 == word1[::-1]}")
    print(f"{word2} es un palindromo?: {word2 == word2[::-1]}")

    # Anagramas
    print(f"{word1} es anagrama de {word2}?: {sorted(word1) == sorted(word2)}")

    # Isograma
    def isogram(word: str) -> bool:

        word_dic = {}
        for character in word1:
            word_dic[character] = word_dic.get(character, 0) + 1

        isogram = True
        values = list(word_dic.values())
        isogram_len = values[0]

        for word_count in values:
            if word_count != isogram_len:
                isogram = False
            break

        return isogram

    print(f"{word2} es un isograma?: {isogram(word1)}")
    print(f"{word2} es un isograma?: {isogram(word2)}")


check("radar", "pythonpython")
# check("amor", "roma")