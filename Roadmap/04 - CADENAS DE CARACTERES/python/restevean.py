"""
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
"""

# String creation
s = "Hello World!"

# Access specific character
print(f"Accessing to 67th char: {s[6]}")  # Output: W

# Substring
print(f"Extracting substring: {s[0:5]}")  # Output: Hello

# Length
print(f"Length: {len(s)}")  # Output: 13

# Concatenation
s2 = " How are you?"
print(f"Concatenation: {s + s2}")  # Output: Hello, World! How are you?

# Repetition
print(f"Repetition: {s * 2}")  # Output: Hello, World!Hello, World!

# Iteration
print("Iteration:")  # Output: Iteration:
for char in s:
    print(char)

# Conversion to uppercase
print(f"Uppercase: {s.upper()}")  # Output: HELLO WORLD!

# Conversion to lowercase
print(f"Lowercase: {s.lower()}")  # Output: hello world!

# Replacement
print(f"Replacement: {s.replace("World", "Python")}")  # Output: Hello Python!

# Splitting
print(f"Splitting: {s.split(",")}")  # Output: ['Hello', ' World!']

# Joining
words = ['Hello', 'World!']
print(f"Joining: {' '.join(words)}")  # Output: Hello World!

# Interpolation
name = "Python"
print(f"Interpolation: Hello, {name}!")  # Output: Hello, Python!

# Checking if string starts with a substring
print(f"String starts with 'Hello': {s.startswith("Hello")}")  # Output: True

# Checking if string ends with a substring
print(f"String ends with '!': {s.endswith("!")}")  # Output: True

# Checking if string contains a substring
print(f"String contains 'World'; {"World" in s}")  # Output: True


# EXTRA
class WordAnalyzer:
    def __init__(self, word1, word2):
        self.word1 = word1.lower()
        self.word2 = word2.lower()

    def is_palindrome(self, word):
        return word == word[::-1]

    def is_anagram(self):
        return sorted(self.word1) == sorted(self.word2)

    def is_isogram(self, word):
        return len(word) == len(set(word))


def main():
    word1 = input("Enter first word: ")
    word2 = input("Enter second word: ")

    analyzer = WordAnalyzer(word1, word2)

    print(f"{word1} is a palindrome: {analyzer.is_palindrome(word1)}")
    print(f"{word2} is a palindrome: {analyzer.is_palindrome(word2)}")

    print(f"{word1} and {word2} are anagrams: {analyzer.is_anagram()}")

    print(f"{word1} is an isogram: {analyzer.is_isogram(word1)}")
    print(f"{word2} is an isogram: {analyzer.is_isogram(word2)}")


if __name__ == "__main__":
    main()
