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
from abc import ABC, abstractmethod


def string_operations(text: str) -> None:
    first_char = text[0]
    substring = text[1:]
    length = len(text)
    concatenation = text + text
    repeated = text * 2

    for char in text:
        print(char)

    text_to_upper = text.upper()
    text_to_lower = text.lower()
    replace_last_char_in_text = text[:-1] + first_char
    other_replace = text.replace(text[0], "")
    interpolation = f"{text} {text}"
    verification = text == text[::-1]
    verification2 = "h" in text
    division_for_words = text.split()
    division_for_chars = list(text)
    division_for_chars2 = [char for char in text]

    print("first_char:", first_char)
    print("substring:", substring)
    print("length:", length)
    print("concatenation:", concatenation)
    print("repeated:", repeated)
    print("text_to_upper:", text_to_upper)
    print("text_to_lower:", text_to_lower)
    print("replace_last_char_in_text:", replace_last_char_in_text)
    print("other_replace:", other_replace)
    print("interpolation:", interpolation)
    print("verification:", verification)
    print("verification2:", verification2)
    print("division_for_words:", division_for_words)
    print("division_for_chars:", division_for_chars)
    print("division_for_chars2:", division_for_chars2)


class Comprobator(ABC):
    @abstractmethod
    def is_palindrome(self) -> bool:
        pass

    @abstractmethod
    def is_anagram(self) -> bool:
        pass

    @abstractmethod
    def is_isogram(self) -> bool:
        pass


class Program(Comprobator):
    def __init__(self, text1: str, text2: str) -> None:
        self.text1 = text1.lower()
        self.text2 = text2.lower()

    def is_palindrome(self) -> bool:
        return self.text1 == self.text2[::-1]

    def is_anagram(self) -> bool:
        return len(self.text1) == len(self.text2) and all(
            char in self.text2 for char in self.text1
        )

    def is_isogram(self) -> bool:
        word1_is_isogram = len(set(self.text1)) == len(self.text1)
        word2_is_isogram = len(set(self.text2)) == len(self.text2)
        print("text1 is isogram:", word1_is_isogram)
        print("text2 is isogram:", word2_is_isogram)

        return word1_is_isogram and word2_is_isogram


def main() -> None:
    string_operations(text="hello")

    program = Program(text1="hola", text2="aloh")
    print(program.is_palindrome())
    print(program.is_anagram())
    print(program.is_isogram())


if __name__ == "__main__":
    main()
