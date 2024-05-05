"""
Crea un programa que analice dos palabras diferentes y realice comprobaciones
para descubrir si son:
- Palíndromos
- Anagramas
- Isogramas
"""

#  --- Manejo de cadenas  --- 

my_string = "mi amigo Worlion es UN BRASAS"

# Operaciones contempladas en el enunciado
print(f"Acceso a caracteres específicos: {my_string[3]}") # ACCESO A CARACTERES ESPECIFICOS
print(f"Acceso a subcadenas: {my_string[3:10]}") # ACCESO A SUBCADENAS
print(f"Longitud: {len(my_string)}") # LONGITUD
print(f"Concatenación: {my_string + ' y un pesado'}") # CONCATENACIÓN
print(f"Repetición: {my_string * 3}") # REPETICIÓN

# RECORRIDO
print("Recorrido:")
for char in my_string:
    if(char == " "): 
        print("\t- Espacio!")

print(f"Conversión a mayúsculas: {my_string.upper()}") # CONVERSIÓN A MAYÚSCULAS
print(f"Conversión a minúsculas: {my_string.lower()}") # CONVERSIÓN A MINÚSCULAS
print(f"Reemplazo: {my_string.replace('mi', 'tu')}") # REEMPLAZO
print(f"División: {my_string.split(' ')}") # DIVISIÓN
print(f"Unión: {' '.join(my_string.split(' '))}") # UNIÓN
print(f"Interpolación: {my_string} y {my_string}") # INTERPOLACIÓN
print(f"Verificación: {'mi' in my_string}") # VERIFICACIÓN

# Otros
print(f"capitalize: {my_string.capitalize()}") # CAPITALIZADO
print(f"casefold: {my_string.casefold()}") # CASEFOLD
print(f"center: {my_string.center(50, '-')}") # CENTER
print(f"count ('mi'): {my_string.count('mi')}") # COUNT
print(f"encode: {my_string.encode(encoding='utf-8', errors='strict')}") # ENCODE
print(f"endswith('AS'): {my_string.endswith('AS')}") # ENDSWITH
print(f"expandtabs: {my_string.expandtabs(tabsize=8)}") # EXPANDTABS 
print(f"find('CARCAMUSA'): {my_string.endswith('CARCAMUSA')}") # FIND
print(f"isalpha: {my_string.isalpha()}") # ISALPHA

"""
DIFICULTAD EXTRA (opcional): PALÍNDROMOS, ANAGRAMAS E ISOGRAMAS
"""

def is_palindrome(word):
    print(f"Es palindromo si {word} == {word[::-1]}")
    return word == word[::-1]

def is_anagram(word1, word2):
    print(f"Son anagramas si {sorted(word1)} == {sorted(word2)}")
    return sorted(word1) == sorted(word2)

def is_isogram(word):
    print(f"{word} es palindromo si cada letra se repite el mismo número de veces!")
    my_dict = {}

    for char in word:
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1
    
    num : int = 0
    
    for i in my_dict.values():
        if(num == 0):
            num = i
        elif(i != num):
            return False
        
    return True
    

def analyze_words(word1, word2):
    print(f"Las palabras {word1} y {word2} son:")
    print(f"Palíndromos: {is_palindrome(word1)} and {is_palindrome(word2)}")
    print(f"Anagramas: {is_anagram(word1, word2)}")
    print(f"Isogramas: {is_isogram(word1)} and {is_isogram(word2)}")

analyze_words("oso", "soso")
