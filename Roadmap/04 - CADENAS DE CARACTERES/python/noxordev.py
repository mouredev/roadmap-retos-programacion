"""
Cadenas de caracteres
"""

string = "Hola!"
string2 = "¿Qué tal?"

print(string + ", " + string2) # Concatenacion
print(string * 3) # Repeticion
print(string[2]) # Acceso a caracteres especificos
print(string[:2]) # Slicing
print(string[2:]) # Slicing
print(string[::-1]) # Slicing inverso
print(len(string2)) # Longitud
print('a' in string) # Busqueda
print(string.upper()) # Mayusculas
print(string.lower()) # Minusculas
print(string2.title()) # Primera letra en mayuscula
print(string2.capitalize()) # Primera letra en mayuscula de la oracion

print(string.replace("a", "5")) # Reemplazo
print(string2.split("tal")) # Division
print("   Esto es una prueba   ".strip()) # Eliminacion de espacios al principio y al final

print(string.startswith("H")) # Busqueda al principio
print(string.endswith("!")) # Busqueda al final
print(string.count("o")) # Busqueda de ocurrencias
print(string.split("o")) # Division de cadenas

print(string.isalnum()) # Comprobacion de alfanumericos
print(string.isalpha()) # Comprobacion de alfabeticos
print(string.isnumeric()) # Comprobacion de numericos
print(string.isspace()) # Comprobacion de espacios
print(string.isupper()) # Comprobacion de mayusculas
print(string.islower()) # Comprobacion de minusculas

print("Hola, mundo! @noxordev".find("noxordev")) # Busqueda de posicion
print("Hola, mundo! @noxordev".find("mu")) # Busqueda de posicion
print("Hola, mundo! @noxordev".lower().find("la")) # Busqueda de posicion en minúsculas

print(f"Saludo: {string} , lenguaje: {string2}!") # Interpolacion
print("Saludo: {} , lenguaje: {}!".format(string, string2))  # Formateo

print(list(string)) # Transformacion en lista de caracteres
print("".join(list(string))) # Transformacion de lista en cadena

Lista = ["Hola", "Python.", string2]
print(" ".join(Lista)) # Transformacion de lista en cadena

numero1 = "123456" # Transformacion numerica
print(numero1)

print(numero1.isalnum())
print(numero1.isalpha())
print(numero1.isnumeric())
print(numero1.isspace())

"""
Extra
"""
print ("Ejercicio extra:")

word1 = "radar"
word2 = "amor"

def check(word1: str, word2: str):

    # Palíndromos
    print(f"La palabra {word1} es un palindromo?: {word1 == word1[::-1]}")
    print(f"La palabra {word2} es un palindromo?: {word2 == word2[::-1]}")

    # Anagramas
    print(f"La palabra {word1} es un anagrama de {word2}?: {sorted(word1) == sorted(word2)}")

    # Isogramas
    print(f"La palabra {word1} es un isograma?: {len(word1) == len(set(word1))}")
    print(f"La palabra {word2} es un isograma?: {len(word2) == len(set(word2))}")

    def isogram(word: str) -> bool:

        word_dict = dict()
        for letter in word:
                word_dict[letter] = word_dict.get(letter, 0) + 1
        
        isogram = True
        values = list(word_dict.values())
        isogram_len = values[0]
        for word_count in values:
            if word_count != isogram_len:
                isogram = False
                break  
        return isogram
        
    print(f"La palabra {word2} es un isograma?: {isogram(word2)}")

check(word1, word2)
check("amor", "roma")
check("prueba", "pythonpythonpython")