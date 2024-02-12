# CADENAS DE CARACTERES

str1 = "Euler"
str2 = "Number"

# Concatenación
print(str1 + "'s" + " " + str2)

# Longitud
print(len(str1))

# Indexación
print(str1[0] + str1[1] + str2[2] + str2[3])

# Búsqueda
print("l" in str1)
print("b" in str1)

# División
print(str1.split("e"))

# Slicing
print(str1[1:5])
print(str1[1:])
print(str1[0:4])
print(str1[:4])

# Repetición
print(str1 * 4)

# Reemplazo
print(str1.replace("E", "O"))

# Mayúsculas
print(str1.upper())
# Minúsculas
print(str1.lower())
# Letras Mayúsculas
print("euler's number".title())
print("euler's number".capitalize())

# Eliminación de espacios iniciales y finales
print(" euler's number ".strip())

# Búsqueda al inicio y al final
print(str1.startswith("Eu"))
print(str1.startswith("Num"))
print(str1.endswith("ler"))
print(str1.endswith("ber"))

str3 = "Euler's number is a constant"

# Búsqueda de posición
print(str3.find("constant"))
print(str3.find("Euler"))
print(str3.find("n"))
print(str3.lower().find("n"))

# Búsqueda de ocurrencias
print(str3.lower().count("n"))

# Formateo
print("Mathematical: {}, type: {}".format(str1, str2))

# Interpolación
print(f"Mathematical: {str1}, type: {str2}")

# Transformación de una lista en una cadena
list1 = [str1, "'s", str2]
print("".join(list1))

# Transformaciones numéricas
str4 = "271828"
str4 = int(str4)
print(str4)

str5 = "2.71828"
str5 = float(str5)
print(str5)

# Comprobaciones
str5 = "2,71828"
print(str1.isalnum())
print(str1.isalpha())
print(str5.isalpha())
print(str5.isnumeric())



# Extra

print("🧩 DIFICULTAD EXTRA 🧩")

def check(w1: str, w2: str):
    # Palindromes
    print(f"Is {w1} a palindrome?: {w1 == w1[::-1]}")
    print(f"Is {w2} a palindrome?: {w2 == w2[::-1]}")

    # Anagrams
    print(f"Is {w1} an anagram of {w2}?: {sorted(w1) == sorted(w2)}")

    # Isograms
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
    
    print(f"Is {w1} an isogram?: {isogram(w1)}")
    print(f"Is {w2} an isogram?: {isogram(w2)}")

check("radar", "bebe")