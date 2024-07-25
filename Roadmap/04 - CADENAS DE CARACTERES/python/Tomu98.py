""" Reto 04: Cadena de Caracteres """

""" Operaciones """

s1 = "Hola"
s2 = "Python"
s3 = "Abel Tomás @Tomu98"

# Concatenación
print(s1 + " " + s2 + "!")

# Repetición
print(s1 * 3)

# Indexación
print(s1[0] + s1[1] + s1[2] + s1[3])

# Longitud
print(len(s2))

# Slicing (porción)
print(s2[2:6])
print(s2[2:])
print(s2[0:2])
print(s2[:2])

# Búsqueda
print("a" in s1)
print("i" in s1)

# Reemplazo
print(s1.replace("o", "a"))

# División
print(s2.split("t"))

# Mayúsculas, minúsculas y primera letra en mayúsculas
print(s1.upper())
print(s1.lower())
print("abel tomás".title())
print("abel tomás".capitalize())

# Eliminación de espacios al principio y al final
print(" Abel Tomás ".strip())

# Búsqueda al principio y al final
print(s1.startswith("Ho"))
print(s1.startswith("Py"))
print(s1.endswith("la"))
print(s1.endswith("thon"))

# Búsquda de posición
print(s3.find("Tomu"))
print(s3.find("Abel"))
print(s3.find("T"))
print(s3.lower().find("u"))

# Búsqueda de ocurrencias
print(s3.lower().count("m"))

# Formateo
print("Saludo: {}, lenguaje: {}!".format(s1, s2))

# Interpolación
print(f"Saludo: {s1}, lenguaje: {s2}!")

# Transformación en lista de caracteres
print(list(s3))

# Transformación de lista en cadena
l1 = [s1, ", ", s2, "!"]
print("".join(l1))

# Transformaciónes númericas
s4 = "123456"
s4 = int(s4)
print(s4)

s5 = "123456.12"
s5 = float(s5)
print(s5)

# Comprobaciones varias
s4 = "123456"
#print(s1.isalnum())
#print(s1.isalpha())
#print(s4.isalpha())
#print(s4.isnumeric())



""" Reto extra """

def analize_string(word1: str, word2: str):
    # Palíndromo
    print(f"¿{word1} es un palíndromo?: {word1.lower() == word1[::-1].lower()}")
    print(f"¿{word2} es un palíndromo?: {word2.lower() == word2[::-1].lower()}")

    # Anagrama
    print(f"¿{word1} es anagrama de {word2}?: {sorted(word1.lower()) == sorted(word2[::-1].lower())}")

    # Isograma
    def isogram(word: str) -> bool:
        word_dict = dict()
        for char in word:
            word_dict[char] = word_dict.get(char, 0) + 1

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

analize_string("Tommu", "Python")
