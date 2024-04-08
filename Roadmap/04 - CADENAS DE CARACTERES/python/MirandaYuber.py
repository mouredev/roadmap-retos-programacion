print('#####  CADENAS DE CARACTERES #####')

string = 'Programa en Python'
print(str(reversed(string)))

concatenation = 'Hola ' + string
print(f"Concatenación: {concatenation}")

multiplication = 3 * string
print(f'Multiplicación: {multiplication}')

len_string = len(string)
print(f'Obtener largo de una string: {len_string}')

sub_string = string[0:3:1]  # [Inicio: Fin(no incluido): paso]
print(f'Subcadena con los 3 primeros caracteres de la cadena "{string}": {sub_string}')

upper_string = string.upper()
print(f'Pasamos a mayusculas la cadena "{string}": {upper_string}')

lower_string = string.lower()
print(f'Pasamos a minusculas la cadena "{string}": {lower_string}')

title_string = lower_string.title()
print(f'Pasamos de minusculas a notación de titulo la cadena "{lower_string}": {title_string}')

replace_string = string.replace('e', 'E')
print(f'Reemplazamos la "e" de la cadena "{string}" por la "E": {replace_string}')

new_string = '      Hola Python      '

print(f'Elimina los espacios vacios al inicio de la cadena "{new_string}": {new_string.lstrip()}')

print(f'Elimina los espacios vacios al final de la cadena "{new_string}": {new_string.rstrip()}')

email = 'example@example.com'
print(f'Separa las palabras de la cadena "{string}" acorde al parametro enviado: {email.split("@")}')

print(f'Recorrer caracteres de la cadena "{string}":')
for caracter in string:
    print(caracter)

access_first_character = string[0]
print(f'Acceder al primer caracter del string: {access_first_character}')

access_last_character = string[-1]
print(f'Acceder al ultimo caracter de la string: {access_last_character}')


print('#####  EXTRA  #####')

print("Programa para analizar dos palabras diferentes y comprobar si son palindromas, anagramas o isogramas.")
first_string = str(input('Digite la primera palabra: '))
second_string = str(input('Digite la segunda palabra: '))

while first_string == second_string:
    print('Las palabras deben ser diferentes.')
    first_string = str(input('Digite la primera palabra: '))
    second_string = str(input('Digite la segunda palabra: '))


def check(word1: str, word2: str):
    # Palindromos
    print(f"¿La palabra {word1} es palindroma?: {word1 == word1[::-1]}")

    print(f"¿La palabra {word2} es palindroma?: {word2 == word2[::-1]}")

    # Anagramas
    print(f"¿La palabra {word1} es anagrama de la palabra {word2}?: {sorted(word1) == sorted(word2)}")

    # Isogramas
    def isogram(word: str) -> bool:

        word_dict = dict()
        for character in word:
            word_dict[character] = word_dict.get(character, 0) + 1

        isogram = True
        values = list(word_dict.values())
        print(f"prueba: {values}")
        isogram_len = values[0]
        for word_count in values:
            if word_count != isogram_len:
                isogram = False
                break

        return isogram

    print(f"¿{word1} es un isograma?: {isogram(word1)}")
    print(f"¿{word2} es un isograma?: {isogram(word2)}")


check(first_string, second_string)
