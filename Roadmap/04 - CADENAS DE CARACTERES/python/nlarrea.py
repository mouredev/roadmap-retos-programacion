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

# CREATE A STRING

my_str = "Hello world!"
# Simple '' can be used too

# ACCESS CHARACTERS

print(my_str[6])  # w
first_word = my_str[:5]
print(first_word)  # Hello
print(my_str[::-1])  # !dlrow olleH

# Separate string in each space and take the second item from the list
second_word = my_str.split(" ")[1]
print(second_word)  # world!

# LENGTH

print(len(my_str))  # 12
print(len(first_word))  # 5
print(len(second_word))  # 6

# INTERPOLATION, CONCATENATION AND FORMAT

# Using string templates
sentence_1 = f"{first_word} {second_word}"
print(sentence_1)  # Hello world!

# Using join
sentence_2 = " ".join([first_word, second_word])
print(sentence_2)  # Hello world!

# Using math +
sentence_3 = first_word + " " + second_word
print(sentence_3)  # Hello world!

# Using format
sentence_4 = "{} {}".format(first_word, second_word)
print(sentence_4)  # Hello world!

# REPETITION

print(first_word * 2)  # HelloHello

# CHECK

print("h" in my_str)  # False
print("H" in my_str)  # True
print("world" in my_str)  # True
print(my_str.startswith("Hell"))  # True
print(my_str.endswith("!"))  # True

# REPLACE

print(my_str.replace("!", "."))  # Hello world.

# DIVISION

print(my_str.split(" "))  # ['Hello', 'world!']

# UPPER AND LOWER CASES

print(my_str.upper())  # HELLO WORLD! -> all words in upper case
print(my_str.lower())  # hello world! -> all words in lower case
print(
    my_str.capitalize()
)  # Hello world! -> only first char in upper and the rest in lower case
print(
    my_str.title()
)  # Hello World! -> first char of each word in upper and the rest in lower case

# REMOVE EMPTY SPACES FROM BEGINNING AND END

my_other_str = "    Hello there!   "
print(len(my_other_str))  # 19
print(
    len(my_other_str.strip())
)  # 12 -> .strip() removes spaces at the beginning and the end of the str
print(len(my_other_str.rstrip()))  # 16 -> remove empty spaces from the right
print(len(my_other_str.lstrip()))  # 15 -> remove empty spaces from the left

# FIND AND COUNT

long_str = "the quick brown fox jumped over the lazy dog"

print(long_str.find("quick"))  # 4 -> where the word starts
print(long_str.find("QUICK"))  # -1 -> doesn't exist in the sentence
print(long_str.count("o"))  # 4
print(long_str.count("q"))  # 1

# FROM NUMERIC STRING TO NUMBER

str_num = "1234"
int_num = int(str_num)
print(type(str_num))  # <class 'str'>
print(type(int_num))  # <class 'int'>

str_num_2 = "1234.56"
float_num = float(str_num_2)
print(type(str_num_2))  # <class 'str'>
print(type(float_num))  # <class 'float'>

print(str_num.isalnum())  # True
print(str_num.isalpha())  # False
print(str_num.isalpha())  # False
print(str_num.isnumeric())  # True

print(str_num_2.isalnum())  # False
print(str_num_2.isalpha())  # False
print(str_num_2.isalpha())  # False
print(str_num_2.isnumeric())  # False


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
"""


def check_is_palindrome(word: str) -> bool:
    reversed_word = word[::-1]

    return word == reversed_word


def check_is_anagram(word_one: str, word_two: str) -> bool:
    return sorted(word_one) == sorted(word_two)


def check_is_isogram(word: str) -> bool:
    # Store how many times appears each character
    chars_dict = dict()
    for char in word:
        chars_dict[char] = chars_dict.get(char, 0) + 1

    # Check if all the characters appear equal times
    is_isogram = True
    chars_values = list(chars_dict.values())
    first_ch_qty = chars_values[0]
    for char_qty in chars_values:
        if char_qty != first_ch_qty:
            is_isogram = False
            break

    return is_isogram


def check_words(word_one: str, word_two: str) -> None:
    # Check if words are palindromes
    print(f"\nIs {word_one} a palindrome? {check_is_palindrome(word_one)}")
    print(f"Is {word_two} a palindrome? {check_is_palindrome(word_two)}")

    # Check if words are anagrams
    print(
        f"\nIs {word_one} {word_two}'s anagram? {check_is_anagram(word_one, word_two)}"
    )

    # Check if words are isograms
    print(f"\nIs {word_one} an isogram? {check_is_isogram(word_one)}")
    print(f"Is {word_two} an isogram? {check_is_isogram(word_two)}\n")


check_words("rotor", "anna")
check_words("amor", "roma")
