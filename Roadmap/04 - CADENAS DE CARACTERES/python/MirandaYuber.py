from builtins import list

print('#####  CADENAS DE CARACTERES #####')

string = 'Programa en python'
print(str(reversed(string)))

print(f"Concatenación: {'Hola ' + string}")

print(f'Multiplicación: {3 * string}')

print(f"Indexación: {string[0] + string[1] + string[2]}")

print(f'Longitud de un string: {len(string)}')

print(f'Subcadena con los 3 primeros caracteres de la cadena "{string}": {string[0:3:1]}')  # [Inicio: Fin: paso]
print(f'Subcadena del 2do caracter al ultimo de la cadena "{string}": {string[1:]}')  # [Inicio: Fin: paso]

print(f"Buscador: {'Python' in string}")

print(f"Reemplaza la 'e' de la cadena '{string}' por la 'E': {string.replace('e', 'E')}")

print(f"Dividir cadena: {string.split(' ')}")

print(f'Pasamos a mayusculas la cadena "{string}": {string.upper()}')

print(f'Pasamos a minusculas la cadena "{string}": {string.lower()}')

print(f'Pasamos a notación de titulo la cadena "{string}": {string.title()}')

print(f"Capitalizar la cadena 'yuber Miranda': {'yuber Miranda'.capitalize()}")

new_string = '      Hola Python      '

print(f'Elimina los espacios vacios al inicio de la cadena "{new_string}": {new_string.lstrip()}')

print(f'Elimina los espacios vacios al final de la cadena "{new_string}": {new_string.rstrip()}')

print(f'Elimina todos los espacios vacios de la cadena "{new_string}": {new_string.strip()}')

print(f'Recorrer caracteres de la cadena "{string}":')
for caracter in string:
    print(caracter)

print(f"Buscar al principio de la cadena: {string.startswith('Pro')} || {string.startswith('Py')}")

print(f"Buscar al final de la cadena: {string.endswith('thon')} || {string.endswith('ma')}")

print(f"Buscar posición: {string.find('en')} || {string.lower().find('En')}")  # -1 es cuando no es encontrado

print(f"Buscar concurrencias: {string.lower().count('o')}")

print("Formateo: String1 = {}, string2 = {}".format(string, new_string))

print(f"Interpolación: String1 = {string}, string2 = {new_string}")

list_characters = list(string)
print(f"Transforma string en lista: {list_characters}")

print(f"Transforma lista en string: {''.join(list_characters)}")

print(f"Transforma string a enteros: {type(int('12345'))}")

print(f"Transforma string a decimales: {type(float('12.4'))}")

print(f"Comprueba si es un número: {string.isalnum()}")
print(f"Comprueba si es un string: {string.isalpha()}")
print(f"Comprueba si es númerico: {string.isnumeric()}")

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
