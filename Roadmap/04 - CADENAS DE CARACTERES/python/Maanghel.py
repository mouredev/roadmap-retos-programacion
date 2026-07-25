"""
EJERCICIO:
Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
    - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
    conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...

DIFICULTAD EXTRA (opcional):
Crea un programa que analice dos palabras diferentes y realice comprobaciones
para descubrir si son:
    - Palíndromos
    - Anagramas
    - Isogramas
"""

text1 = "Github"
text2 = "Maanghel"
texts = ["Hola", "Python"]
text3 = "124123"
text4 = "Mañana sera un gran dia"

# Acceso a caracteres específicos
print("Acceso a caracteres específicos:")
print(text1[0])

# Acceso a subcadenas
print("\nAcceso a subcadenas:")
print(text1[0:3])

# Longitud de la cadena
print("\nLongitud de la cadena:")
print(len(text1))

# Concatenacion de cadenas
print("\nConcatenacion de cadenas:")
print(text1 + " " + text2)

# Repeticion de cadenas
print("\nRepetición de cadenas:")
print(text2 * 5)

# Recorrido de cadenas
print("\nRecorrido de cadenas:")
for letra in text2:
    print(letra, end="")

# Conversion a mayúsculas
print("\n\nConversión a mayúsculas:")
print(text1.upper())

# Conversión a minúsculas
print("\nConversión a minúsculas:")
print(text2.lower())

# Reemplazo de caracteres en python
print("\nReemplazo de caracteres:")
print(text2.replace("a", "A"))

# División de cadenas
print("\nDivisión de cadenas:")
print(text1.split("t"))

# Union de cadenas
print("\nUnión de cadenas:")
print(" ".join(texts))

# Interpolación de cadenas
print("\nInterpolación de cadenas:")
print(f"Mi {text1} es {text2}")

# Verificación
print("\nVerificacion en cadenas:")
print("a" in text2)

# Comprobaciones
print("\nComprobaciones varias:")
print(text3.isalnum())
print(text1.isalpha())
print(text3.isalpha())

# Eliminacion de espacios al inicio y final
print("\nEliminación de espacios al inicio y al final:")
print(text1.strip())

# Convertir la cadena en una lista
print("\nConvertir la cadena en una lista:")
print(text4.split(" "))

# EXTRA

def verificar_palindromo(palabra1: str, palabra2: str) -> bool:
    """Verifica si las dos palabras son palindromas"""
    return palabra1[::-1].lower() == palabra2.lower()

def verificar_anagrama(palabra1: str, palabra2: str) -> bool:
    """Verifica si las dos palabras son anagramas"""
    return sorted(palabra1.lower()) == sorted(palabra2.lower())

def verificar_isograma(palabra: str) -> bool:
    """Verifica si la palabra es un isograma"""
    return len(set(palabra.lower())) == len(palabra.lower())

print(verificar_palindromo("Ana", "ana"))
print(verificar_palindromo("Roberto", "Ana"))

print(verificar_anagrama("Amor", "Roma"))
print(verificar_anagrama("Hola", "Python"))

print(verificar_isograma("Hola"))
print(verificar_isograma("mañana"))
