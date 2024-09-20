
'''
Operaciones
'''

s1 = "Hola"
s2 = "Python"

# Concatenación
print(s1 + ", " + s2 + "!") 

# Repetición
print(s1 * 3)

# Indexación
print(s1[0] + s1[1] + s1[2] + s1[3])

# Longitud
print(len(s1))

# Slicing (porción)
print(s2[2:5])
print(s2[2:])
print(s2[0:])

# Búsqueda
print("a" in s1)
print("i" in s1)

# Reemplazo
print(s1.replace("o", "a"))

# División
print(s2.split("t"))

# Mayúsculas y minúsculas
print(s1.upper())
print(s1.lower())
print("pedro garcía".title())
print("pedro garcía".capitalize())

# Eliminación de espacios al principio y al final
print("  pedro garcía  ". strip())

# Búsqueda al principio y final
print(s1.startswith("Ho"))
print(s1.endswith("la"))

s3 = "Brais Moure @mouredev"

# Búsqueda de posición
print(s3.find("m"))

# Búsqueda de ocurrencias
print(s3.lower().count("m"))

# Formateo
print("Saludo: {}, lenguaje: {}!".format(s1, s2))

# Interpolación
print(f"Saludo: {s1}, lenguaje: {s2}!")

# Transformación en lista
print(list(s3))

# Transformación de lista en cadena
l1 = [s1, ", ", s2, "!"]
print("".join(l1))

# Transformaciones numéricas
s4 = "123456"
print(int(s4))
s4 = "123456.17"
print(float(s4))

# Comprobaciones varias
print(s1.isalnum())     #Alphaanumérico (texto + números)
print(s1.isalpha())     #Alpha (solo texto)
print(s1.isnumeric())   #Numérico


'''
Ejercicio extra
'''
def analyze_strings(str1, str2):
    # Palíndromo
    if str1 == str2[::-1]:
        print(f"{str1} y {str2} son palíndromos!")
    # Anagrama
    if sorted(str1) == sorted(str2):
        print(f"{str1} es un anagrama de {str2}!")
    # Isograma
    if isograma(str1):
        print(f"{str1} es un isograma!")
    if isograma(str2):
        print(f"{str2} es un isograma!")

def isograma(str) -> bool:
    word_dict = dict()
    for letter in str:
        word_dict[letter] = word_dict.get(letter, 0) + 1
    
    values = list(word_dict.values())
    isogram_len = values[0]
    for letter in values:
        if letter != isogram_len:
            return False
    return True

analyze_strings("pedro", "ordep")

