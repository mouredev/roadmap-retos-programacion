"""
* DIFICULTAD EXTRA (opcional):
* Crea un programa que analice dos palabras diferentes y realice comprobaciones
* para descubrir si son:
* - Palíndromos
* - Anagramas
* - Isogramas
"""

from collections import Counter

def check_words(word_1, word_2):
    # Convertimos las palabras a minúsculas para evitar diferencias entre mayúsculas y minúsculas
    word_1, word_2 = word_1.lower(), word_2.lower()
    
    # Palíndromos
    # Palabras que se leen igual de izquierda a derecha y viceversa.
    print(f"¿{word_1} es Palindromo?: {word_1 == word_1[::-1]}")
    print(f"¿{word_2} es Palindromo?: {word_2 == word_2[::-1]}")

    # Anagramas
    # Ambas palabras tienen las mismas letras, solo en diferente orden.
    """
    Counter crea un diccionario donde las claves son los caracteres y los valores son las frecuencias de esos caracteres.
    """
    print(f"¿{word_1} y {word_2} son Anagramas?: {Counter(word_1) == Counter(word_2)}")

    # Isogramas
    # Palabras en las que ninguna letra se repite.
    print(f"¿{word_1} es Isograma?: {len(word_1) == len(set(word_1))}")
    print(f"¿{word_2} es Isograma?: {len(word_2) == len(set(word_2))}")

    
check_words("oso", "reconocer")
check_words("acto", "taco")
check_words("cielo", "mundo")