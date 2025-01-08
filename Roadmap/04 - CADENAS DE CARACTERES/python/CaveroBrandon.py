"""
Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres en tu lenguaje.
Algunas de esas operaciones podrían ser (busca todas las que puedas):
- Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación
"""


def string_exercise(first_string='First string', second_string='Second string'):
    string_concatenated = first_string + '-' + second_string  # Concatenation of strings
    print('Concatenated string:', string_concatenated)

    string_multiplication = first_string * 3  # Multiplication of a string or repetition
    print('Repetition of a string:', string_multiplication)

    first_char = first_string[0]  # Accessing a specific character
    print('First character of a string:', first_char)

    sliced_string = first_string[0:5]  # Slicing an string
    print('Sliced string:', sliced_string)

    split_string = first_string.split()  # Splitting a string
    print('Split string:', split_string)

    lower_case_string = first_string.lower()  # Transforming any string to lower case
    print('The lower case version of the string is:', lower_case_string)

    upper_case_string = first_string.upper()  # Transforming any string to upper case
    print('The upper case version of the string is:', upper_case_string)

    replace_text = second_string.replace('string', 'text')  # Replacing a string
    print('Replacing the text "string" to "text":', replace_text)

    find_string = first_string.find('string')  # Find a word in a string
    print('The word "string" is in the position:', find_string)

    first_string_length = len(first_string)  # Getting the length of a string
    print('The length of the string is:', first_string_length)

    for i in first_string:  # Navigate a string using a for
        print(i)

    print(f'String interpolation using the {first_string} and the {second_string}')  # String interpolation


"""
DIFICULTAD EXTRA (opcional):
Crea un programa que analice dos palabras diferentes y realice comprobaciones para descubrir si son:
- Palíndromos
- Anagramas
- Isogramas
"""


def is_palindrome(text):
    testing_text = text.lower()
    testing_text = testing_text.replace(' ', '')

    inverted_text = text[::-1]
    inverted_text = inverted_text.lower()
    inverted_text = inverted_text.replace(' ', '')

    if testing_text == inverted_text:
        print(f'The text "{text}" is a palindrome')
    else:
        print(f'The text "{text}" is not a palindrome')


def is_isogram(text):
    test_text = text.replace(' ', '')
    for letter in test_text:
        if test_text.count(letter) != 1:
            print(f'The text "{text}" is not an isogram')
            return
    print(f'The text "{text}" is an isogram')


def is_anagram(text1, text2):
    test_text1 = text1.replace(' ', '')
    test_text1 = test_text1.lower()
    test_text1 = sorted(test_text1)

    test_text2 = text2.replace(' ', '')
    test_text2 = test_text2.lower()
    test_text2 = sorted(test_text2)

    if test_text1 == test_text2:
        print(f'The text {text1} and {text2} are anagram')
    else:
        print(f'The text {text1} and {text2} are not anagram')


string_exercise()

print(' \n **** DIFICULTAD EXTRA ****')
text = input('Input a text to verify if is palindrome and isogram:')
is_palindrome(text)
is_isogram(text)
anagram1 = input('Input a text the first text to verify if is an anagram:')
anagram2 = input('Input a text the first text to verify if is an anagram:')
is_anagram(anagram1, anagram2)
