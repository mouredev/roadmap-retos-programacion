"""
Operaciones
"""
s1 = "Hola"
s2 = "Python"
s3 = "Brian Silvero @briandavid"

# Concatenación 
print(s1 + "," + s2 + "!" )

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

# Busqueda
print("a" in s1)
print("i" in s1)

# Reemplazo
print(s1.replace("o", "a"))

# Division
print(s2.split("t"))


# Mayúscula, minúscula y letras en mayúscula
print(s1.upper())
print(s1.lower())
print("brian silvero".title())
print("brian silvero".capitalize())

# Eliminación de espacios al principio y al final 
print(" brian silvero ".strip())

# Busqueda al principio y al final
print(s1.startswith("Ho"))
print(s1.startswith("Py")) 
print(s1.endswith("la"))
print(s1.endswith("ton"))

# Busquedad de posicion
print(s3.find("brian"))
print(s3.find("Brian"))
print(s3.find("B"))
print(s3.lower().find("b"))

# Busqueda de ocurrencia
print(s3.lower().count("brian"))

# Formateo
print("Saludo: {}, Lenguaje: {}!".format(s1,s2))

# Interpolación
print(f"Saludo: {s1}, Lenguaje: {s2}!")

# Transformación en lista de caracteres
print(list(s3))

# Transformación de lista en cadena 
l1 = [s1,",", s2,"!"]
print(" ".join(l1))

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
print(s4.isnumeric())


"""
Extra
"""

def check(word1:str , word2:str):
    # Palindromo
    print(f"La palabra {word1} es un palidromo?: {word1== word1[::-1]}")
    print(f"La palabra {word2} es un palidromo?: {word2 == word2[::-1]}")
    
    # Anagramas
    print(f"La palabra {word1} es anagrama de {word2}? {sorted(word1) == sorted(word2)}")
    
    
    # Isograma
    
    def isograma(word: str) -> bool:
        
        word_dict = dict()
        for character in word:
            word_dict[character] = word_dict.get(character, 0) + 1
            
        isograma = True
        
        values = list(word_dict.values())
        isogram_len = values [0]
        for word_count in values:
            if word_count != isogram_len:
                isograma = False	
                break
        return isograma

    print(f"{word1} es un isograma?: {isograma(word1)}")
    print(f"{word2} es un isograma?: {isograma(word2)}")

check("radar","pythonpythonpython")

check("amor","roma")

