# 04 CADENAS DE CARACTERES
# Mónica Vaquerano
# https://monicavaquerano.dev

"""
EJERCICIO:
Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):

- Acceso:
            # a caracteres específicos,
            # subcadenas, 
            # longitud, 
            # concatenación, 
            # recorrido,
            # conversión a mayúsculas y minúsculas, 
            # reemplazo, 
            # verificación
            # repetición, 
            # división, 
            # unión, 
            # interpolación, 
            ...

"""
print("\nCADENA DE CARACTERES O STRINGS\n")

# Asignar a una variable (Assign String to a Variable)
string = "hello, world!"
print(f"* String o cadena de caracteres:\t{string}")

# Cadenas de caracteres multilínea (Multiline Strings)
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(f"\n* Un multiline string puede usar comillas simples(') o dobles(\"):\n{a}")

# Acceso a un caracter específico (Access to specific elements of a string)
print(
    f"\n* Acceso a un caracter específico:\tstring[1] -> {string[1]}, string[5] -> {string[5]}"
)

# Recorriendo una string (Looping Through a String)
print("* Recorrinedo una string:\t", end="")
for char in string:
    print(char, end=" ")
print()

# Longitud de una string (String Length)
print(f"* Longitud de una cadena:\tlen(string) -> {len(string)}")

# Verificación de string (Check String)
print(
    f"* Verificación de string:\t'hello' in string -> {'hello' in string}\n\t\t\t\t'hello' not in string -> {'hello' not in string}"
)

# Subcadenas (Access to specific elements of a string)
print(
    f"\n* Acceso a subcadenas:\t\tstring[0:5] -> {string[0:5]}\n\t\t\t\tstring[7:-1] -> {string[7:-1]}"
)
print(f"  (Index negativos y pasos):\tstring[-1::-1] -> {string[-1::-1]}\n")

# Concatenación y repeticion de strings (Concatenate Strings)
a, b = "Hello", "World"
c = a + b
print(f"* Concatenación de strings (a, b = 'Hello', 'World'):\ta + b -> {c}")
print(f"* Repetición de strings (a = 'Hello'):\t(a * 3) -> {a * 3}")

# Format Strings
print("\n* Formateo de strings:")
print(
    """string.format():
Use the string.format() method to insert numbers into strings:
    age = 36
    txt = "My name is John, and I am {}"
    print(txt.format(age)) -> My name is John, and I am 36

f-string format:
    age = 36
    txt = f"My name is John, and I am {age}"
    print(text) -> My name is John, and I am 36
    """
)

# Modificación de strings (Modify Strings)
print(f"* Modificación de strings:\tUpper Case: string.upper() -> {string.upper()}")
print(f"\t\t\t\tLower Case: string.lower() -> {string.lower()}")
print(f"\t\t\t\tTitle Case: string.title() -> {string.title()}")
print(f"\t\t\t\tSwap Case: string.swapcase() -> {string.title().swapcase()}")
print(f"\t\t\t\tCapitalize Case: string.capitalize() -> {string.capitalize()}")
print(
    f"\t\t\t\tRemove Whitespace: lstrip(), rstrip(), strip(): string.strip() -> {string.strip()}"
)
print(f"\t\t\t\tReplace String: string.replace('e','a') -> {string.replace('e', 'a')}")
print(f"\t\t\t\tSplit String: string.split(', ') -> {string.split(', ')}")

# Metodos de strings (String Methods)
print(
    f"* Otros métodos de strings:\tCase Fold: Converts string into lower case too): string.casefold() -> {string.casefold()}"
)
print(f"\t\t\t\tCenter: string.center(50) -> {string.center(50)}")
print(f"\t\t\t\tCount: string.count('l') -> {string.count('l')}")
print(f"\t\t\t\tEnds with: string.endswith('world!') -> {string.endswith('world!')}")
print(
    f"\t\t\t\tStarts with: string.startswith('world!') -> {string.startswith('world!')}"
)
print(
    f"\t\t\t\tFind and Index: string.find('w') or string.index('w') -> {string.find('w')}"
)
print(
    f"\t\t\t\tIs Alphanumeric: checks if the text is alphanumeric: string.isalnum() -> {string.isalnum()}"
)
print(
    f"\t\t\t\tIs Alpha: checks if the text is all text: string.isalpha() -> {string.isalpha()}"
)
print(
    f"\t\t\t\tIs Numeric: checks if the text is all numeric: string.isnumeric() -> {string.isnumeric()}"
)
print(
    f"\t\t\t\tMake translation and translate: Create a mapping table, and use it in the translate() method to replace any character:",
)
print(
    f'\t\t\t\t\t\t  txt = "Hello Sam!" ->  mytable = str.maketrans("S", "P") -> print(txt.translate(mytable)) -> "Hello Pam"'
)
print(
    f"\t\t\t\tPartition(Rpartition too): Returns a tuple where the string is parted into three parts: string.partition('world!') -> {string.partition('world')}"
)
print(
    f"\t\t\t\tRfind and rindex: Searches the string for a specified value and returns the last position of where it was found:\n\t\t\t\t\t\t  string.rfind('l') or string.rindex('l') -> {string.rfind('l')}"
)
print(
    f"\t\t\t\tZfill: Fills the string with a specified number of 0 values at the beginning:\n\t\t\t\t\t\t  '50'.zfill(10) -> {'50'.zfill(10)}"
)

myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(
    f"\t\t\t\tJoin: join all items in an iterable into a string, using a hash character as separator:\n\t\t\t\t\t\t  myTuple = ('John', 'Peter'', 'Vicky') -> x = '#'.join(myTuple) = {x}"
)

"""
DIFICULTAD EXTRA (opcional):
Crea un programa que analice dos palabras diferentes y realice comprobaciones
para descubrir si son:
    - Palíndromos:  Palabra o frase cuyas letras están dispuestas de tal manera que resulta la misma leída de izquierda a derecha que de derecha a izquierda.
    - Anagramas: Cambio en el orden de las letras de una palabra o frase que da lugar a otra palabra o frase distinta.
    - Isogramas: Un isograma (del griego isos, 'igual' y gramma, 'letra') es una palabra o frase en la que cada letra aparece el mismo número de veces.
        Ejemplos:
        Heterogramas: yuxtaponer (10), centrifugado (12), luteranismo (11), adulterinos (11), hiperblanduzcos (15)...
        Isogramas con una repetición o de segundo orden: acondicionar (11), escritura (9), intestinos (10), papelera (8)...
"""
print("\nDIFICULTAD EXTRA (opcional):\n")


def palindrome(word: str):
    reversed_word = word[::-1]
    print(
        f"-> Is '{word}' a palindrome?: {word.strip().lower() == reversed_word.strip().lower()}"
    )


def anagram(word1: str, word2: str):
    listChar1, listChar2 = sorted(word1.strip().lower()), sorted(word2.strip().lower())
    print(f"-> Are '{word1}' and '{word2}' anagrams?: {listChar1 == listChar2}")


def isogram(word: str):
    isogram = True
    charDict = {}
    for char in word:
        charDict[char] = charDict.get(char, 0) + 1

    values = list(charDict.values())
    value_count = values[0]
    for char_count in values:
        if char_count != value_count:
            isogram = False
            break

    print(f"-> Is '{word}' an isogram?: {isogram}")


def compare_strings(word1: str, word2: str):
    print("Comparing two strings:")
    palindrome(word1)
    palindrome(word2)
    anagram(word1, word2)
    isogram(word1)
    isogram(word2)


compare_strings("Saco", "radar")
compare_strings("Roma", "yuxtaponer")
