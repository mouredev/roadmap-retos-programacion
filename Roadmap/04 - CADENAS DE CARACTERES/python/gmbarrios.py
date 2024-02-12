"""
Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres en tu lenguaje. Algunas de estas operaciones podrían ser (busca todas las que puedas): acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido, conversion a mayúsculas y minúsculas, reemplazo, division, union, interpolación, verificación...
"""

cadena = "Esto es una cadena de texto."

# Acceso a caracteres
print(cadena[5])
print(cadena[-2])

# Subcadenas
subcadena = "Texto"
print(cadena.find(subcadena))

# Longitud
print(len(cadena))

# Concatenación
pregunta = "¿Que es esto?"
print(f"{pregunta} \n{cadena}")

# Repetición
print(cadena * 3)

# Recorrido
for i in cadena:
    print(i)

# Conversion a mayúsculas y minúsculas.
print(cadena.upper())
print(cadena.lower())

# Reemplazo
print(cadena.replace("texto", "hierro"))

# Division
print(cadena.split(' '))

# Union
print(" ".join(cadena))

# Interpolación
print(f"CADENA - {cadena} - INTERPOLADA.")

# Verificación
verificar = "666"
print(verificar.isalnum())
print(verificar.isalpha())
print(verificar.isdecimal())
print(verificar.isdigit())
print(verificar.isascii())
print(verificar.isupper())
print(verificar.islower())
print(verificar.isnumeric())
print(verificar.isprintable())
print(verificar.isspace())
print(verificar.istitle())
print(verificar.startswith("9"))
print(verificar.endswith("6"))


"""
Dificultad extra
Crea un programa que analice dos palabras diferentes y realice comprobaciones para descubrir si son:
- Palíndromos
- Anagramas
- Isogramas
"""
# Palindromo: palabra o frase cuyas letras están dispuestas de tal manera que resulta la misma leída de izquierda a derecha que de derecha a izquierda.

def palindrome(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]


print(palindrome("tomate"))
print(palindrome("arepera"))


# Anagrama: cambio en el orden de las letras de una palabra o frase que da lugar a otra palabra o frase distinta.

def anagram(word1, word2):
    if word1.lower() == word2.lower():
        return False
    return sorted(word1.lower()) == sorted(word2.lower())


print(anagram("ramo", "amor"))
