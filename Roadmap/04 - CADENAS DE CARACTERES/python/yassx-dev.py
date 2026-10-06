"""
Operaciones
"""

s1 = "Hola"
s2 = "Python"

# Concatenación
print(s1 + ", " + s2 + "!")

# Repetición
print(s1 * 3)

# Indexación
print(s1[0] + s1[1] + s1[2] + s1[3])

# Longitud
print(len(s2))

# Slicing (porción)
print(s2[2:6])
print(s2[2:])

# Búsqueda
print("a" in s1)
print("i" in s1)

# Reemplazo
print(s1.replace("o", "a"))

# División
print(s2.split("t"))

# Mayúsculas, minúsculas y letras en mayúsculas
print(s1.upper())
print(s1.lower())
print("brais moure".title())
print("brais moure".capitalize())

# Eliminación de espacios al principio y al final
print(" brais moure ".strip())

# Búsqueda al principio y al final
print(s1.startswith("Ho"))
print(s1.startswith("Py"))

s3 = "Brais Moure @mouredev"

# Búsqueda de posición
print(s3.find("moure"))
print(s3.find("Moure"))
print(s3.find("M"))
print(s3.lower().find("m"))

# Búsqueda de ocurrencias
print(s3.lower().count("m"))

# Formateo
print("Saludo: {}, lenguaje: {}!".format(s1, s2))

# Interpolación
print(f"Saludo: {s1}, lenguaje: {s2}!")

# Tranformación en lista de caracteres
print(list(s3))

# Unión de lista de caracteres
l1 = [s1, ", ", s2, "!"]
print("".join(l1))

# Transformaciones numéricas
s4 = "123456"
s4 = int(s4)
print(s4)

s5 = "123456.123"
s5 = float(s5)
print(s5)

# Comprobaciones varias
s4 = "123456"
print(s1.isalnum())
print(s1.isalpha())
print(s4.isalpha())

def verificar(str1, str2: str):
    # Normalización a minúsculas
    s1 = str1.lower()
    s2 = str2.lower()

    def isogram(word: str) -> bool:
        if not word:
            return True

        word_dict = dict()
        for character in word:
            word_dict[character] = word_dict.get(character, 0) + 1

        values = list(word_dict.values())
        isogram_len = values[0]
        
        for character_count in values:
            if character_count != isogram_len:
                return False
                
        return True

    # Palíndromos
    print(f"¿{str1} es un palíndromo?: {s1 == s1[::-1]}")
    print(f"¿{str2} es un palíndromo?: {s2 == s2[::-1]}")
    
    # Anagramas (Corregido: comparar ambas listas ordenadas)
    print(f"¿{str1} y {str2} son anagramas?: {sorted(s1) == sorted(s2)}")

    # Heterogramas
    print(f"¿{str1} es un heterograma?: {len(s1) == len(set(s1))}")
    print(f"¿{str2} es un heterograma?: {len(s2) == len(set(s2))}")
    
    # Isogramas
    print(f"¿{str1} es un isograma?: {isogram(s1)}")
    print(f"¿{str2} es un isograma?: {isogram(s2)}")


while True:
    str1 = input("INGRESA LA PALABRA 1: ")
    str2 = input("INGRESA LA PALABRA 2: ")

    if str1.isalpha() and str2.isalpha():
        break
    print("Error: Solo se permiten letras (sin números ni símbolos). Intenta de nuevo.")

verificar(str1, str2)


                





