# Cadenas de caracteres

string = "Hola Python"
string2 = "Como estan?"

# Concatenacion 
print(string + ", " + string2)

# Repeticion
print(string * 3)

# Acceso a caracteres especificos
print(string[2])

# Slicing
print(string[:5])

# Longitud
print(len(string2))

# Busqueda 
print('a' in string)
print('h' in string2)

# Conversion a mayusculas, minusculas y primera letra en mayusculas
print(string.upper())
print(string.lower())
print(string2.title())
print("me llamo nacho".capitalize())

# Remplazo
print(string.replace("a", "5"))

# Division
print(string2.split("o"))

# Eliminacion de espacios al principio y al final
print("    hola mi nombre es nacho     ".strip())

# Encontrar 
print(string.find("P"))

# Busqueda al principio y al final
print(string.startswith("h"))
print(string.endswith("n"))


# Busqueda de ocurrencias
print(string.count("o"))

# Formateo
print("AAAA {} texto sin sentido. {}".format(string, string2))

# Interpolacion
print(f"Viva molotov, {string2}")

# Transformacion en lista de caracteres
caracters = list(string)

# Transformaciones numericas
s1 = "12131341"
s1 = int(s1)

s2 = "1.5"
s2 = float(s2)

# Transformacion de lista en cadena
lista = ["Hola", "Python", "Weyes"]
print(" ".join(lista))

# Comprobaciones
print(string.isalnum())
print(string.isalpha())
print(string.isascii())
print(string.isdecimal())
print(string.isdigit())
print(string.islower())
# Etc..

# Ejercicio extra

def check(word1: str, word2: str):

    # Palindromos
    print(f"{word1} es un palindromo?: {word1 == word1[::-1]}")
    print(f"{word2} es un palindromo?: {word2 == word2[::-1]}")

    # Anagramas
    print(f"{word1} es un anagrama de {word2}: {sorted(word1) == sorted(word2)}")
        
    # Isograma
    def isogram(word: str) -> bool:
        
        word_dict = {}
        for character in word:
            word_dict[character] = word_dict.get(character, 0) + 1

        isograma = True
        values = list(word_dict.values())
        isagram_len = values[0]
        for word_count in values:
            if word_count != isagram_len:
                isograma = False
                break
        return isograma

    print(f"{word2} es un isograma? {isogram(word2)}")
    print(f"{word2} es un isograma? {isogram(word2)}")


check("radar", "Python")
check("amor", "roma")