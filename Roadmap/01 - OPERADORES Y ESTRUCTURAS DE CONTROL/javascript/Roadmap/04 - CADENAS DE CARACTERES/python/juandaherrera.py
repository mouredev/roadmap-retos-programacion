"""
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 *
"""
from collections import Counter
from typing import Callable, Optional

REPLACEMENTS = (("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"), (" ", ""))


def replace_special_characters(input: str) -> str:
    """Reemplaza caracteres especiales en una cadena con sus equivalentes sin tilde.

    Args:
        input_str (str): La cadena de entrada que puede contener caracteres especiales.

    Returns:
        str: La cadena resultante con los caracteres especiales reemplazados.
    """
    for a, b in REPLACEMENTS:
        input = input.replace(a, b)
    return input


def string_to_list(input: str) -> list:
    """Convierte una cadena en una lista de caracteres.

    Args:
        input_str (str): La cadena de entrada.

    Returns:
        list: Lista de caracteres individuales de la cadena de entrada.
    """
    return [letter for letter in input]


def is_palindrome(input: str) -> bool:
    """Verifica si una cadena es un palíndromo.

    Args:
        input_str (str): La cadena de entrada.

    Returns:
        bool: True si la cadena es un palíndromo, False en caso contrario.
    """
    modified_input = replace_special_characters(input.lower())
    return modified_input == modified_input[::-1]


def is_anagram(input_1: str, input_2: str) -> bool:
    """Verifica si dos cadenas son anagramas entre sí.

    Args:
        input_1 (str): La primera cadena.
        input_2 (str): La segunda cadena.

    Returns:
        bool: True si las cadenas son anagramas, False en caso contrario.
    """
    if len(input_1) != len(input_2):
        return False
    new_input_1, new_input_2 = replace_special_characters(input_1.lower()), replace_special_characters(input_2.lower())
    new_input_1, new_input_2 = sorted(string_to_list(new_input_1)), sorted(string_to_list(new_input_2))

    return new_input_1 == new_input_2


def is_isogram(input: str) -> bool:
    """Verifica si una cadena es un isograma (no repite ninguna letra).

    Args:
        input_str (str): La cadena de entrada.

    Returns:
        bool: True si la cadena es un isograma, False en caso contrario.
    """
    input = replace_special_characters(input)
    counter = Counter(sorted(string_to_list(input)))
    return max(counter.values()) == 1


def request_input(prompt: str, validation: Optional[Callable[[str], bool]] = None) -> str:
    """Solicita entrada al usuario hasta que cumpla con la validación.

    Args:
        prompt (str): El mensaje a mostrar al usuario.
        validation (Optional[Callable[[str], bool]]): La función de validación que debe pasar la entrada.

    Returns:
        str: La entrada del usuario que pasó la validación.
    """
    while True:
        user_input = input(prompt)
        if not validation or validation(user_input):
            return user_input


def main():
    while True:
        print("-------------------------------------------------")
        print("1. Validar si una palabra es palíndroma.")
        print("2. Validar dos palabras son anagramas.")
        print("3. Validar si una palabra es isograma.")
        print("4. Salir del programa.")
        option = input("Ingrese su opción: ")
        match option:
            case "1":
                word = request_input("Ingresa la palabra: ")
                response = (
                    f"La palabra {word} es palíndroma" if is_palindrome(word) else f"La palabra {word} NO es palíndroma"
                )
                print(response)
            case "2":
                word_1 = request_input("Ingresa la primera palabra: ")
                word_2 = request_input("Ingresa la segunda palabra: ")
                response = (
                    f"{word_1} y {word_2} son anagramas"
                    if is_anagram(word_1, word_2)
                    else f"{word_1} y {word_2} NO son anagramas"
                )
                print(response)
            case "3":
                word = request_input("Ingresa la palabra: ")
                response = f"La palabra {word} es isograma" if is_isogram(word) else f"La palabra {word} NO es isograma"
                print(response)
            case "4":
                print("Saliendo del programa...")
                break
            case _:
                print("Ingresa una opción válida.")


if __name__ == "__main__":
    main()
