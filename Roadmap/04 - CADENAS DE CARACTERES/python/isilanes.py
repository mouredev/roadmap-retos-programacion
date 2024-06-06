import re


def main():
    string = "This is a String"
    other = "Another String"

    print(f"s == '{string}'")

    print("\nAcceso al caracter enésimo:")
    print(f"s[3] == '{string[3]}'")

    print("\nAcceso al último caracter:")
    print(f"s[-1] == '{string[-1]}'")

    print("\nAcceso a subcadena:")
    print(f"s[5:7] == '{string[5:7]}'")

    print("\nCálculo de longitud:")
    print(f"len(s) == {len(string)}")

    print("\nConcatenación de dos cadenas:")
    print(f"o == '{other}'")
    print(f"s + ':' + o == '{string+':'+other}' <- inefficient, don't use")
    print(f"':'.join([s, o]) == '{':'.join([string, other])}' <- proper way")
    print(f"f'{{s}}:{{o}}' == '{string}:{other}' <- also good way")

    print("\nRepetición de cadena:")
    print(f"s*3 == '{string*3}'")
    print(f"':'.join([s]*3) == '{':'.join([string]*3)}'")

    print("\nRecorremos los 3 primeros caracteres:")
    print("for c in s[:3]:\n    print(c)")
    for c in string[:3]:
        print(c)

    print("\nConversión a mayúsculas:")
    print(f"s.upper() == '{string.upper()}'")

    print("\nConversión a minúsculas:")
    print(f"s.lower() == '{string.lower()}'")

    print("\nReemplazar partes de una cadena es imposible, puesto que en Python las cadenas son inmutables.")
    print("Para lograr una modificación, tendremos que crear otra cadena, que equivalga a la primera modificada.")
    print(f"s.replace('s', 'J') == {string.replace('s', 'J')}")

    print("\nDivisión de una cadena:")
    print(f"s.split('is') == {string.split('is')}")

    print("\nLa interpolación de cadenas puede hacerse de varias maneras. La mejor son los f-strings:")
    print("Nótese que coerce variables de tipo no cadena, a cadena (p.e. el entero 666 a continuación)")
    print("nombre = 'Iñaki'")
    print("edad = 666")
    name, age_years = "Iñaki", 666
    print('f"Me llamo {nombre}, y mi edad es {edad} años" ==', f"'Me llamo {name} y mi edad es {age_years} años'")

    print("\nA una cadena se le pueden hacer muchas verificaciones.")
    print("Supongamos que queremos verificar que una cadena contiene un código ISO de nación, seguido")
    print("de cuatro cifras (ni más ni menos), separados ambos grupos por un guión:")
    print("patt = re.compile(r'^[A-Z]{2}-\d{4}$')")
    patt = re.compile(r'^[A-Z]{2}-\d{4}$')
    print("patt.match('ES-1234') ==", patt.match("ES-1234"))
    print("patt.match('es-1234') ==", patt.match("es-1234"))
    print("patt.match('ES-123') ==", patt.match("ES-123"))
    print("patt.match('ES-12345') ==", patt.match("ES-12345"))
    print("patt.match('ES 1234') ==", patt.match("ES 1234"))


def extra():

    print("\nDificultad extra:")

    def is_word(word: str) -> bool:
        """
        Returns True if 'word' is a word (only contains letters). False, otherwise.
        Only strings of len > 0 will be considered.

        Args:
            word (str):
                String that we want to check.

        Returns:
            Boolean. Whether input is a word or not.
        """
        if not isinstance(word, str):
            return False

        patt = re.compile(r"^[a-z]+$", re.IGNORECASE)

        return patt.match(word) is not None

    def is_palindrome(word: str) -> bool:
        """
        Returns True if 'word' is a word, and it is a palindrome.

        Args:
            word (str):
                Word to check whether it is a palindrome.

        Returns:
            True if input word is a palindrome, False otherwise.
        """
        if not is_word(word):
            return False

        word = word.lower()  # just in case, ignore capitalization

        return word == word[::-1]

    def are_anagrams(word_a: str, word_b: str) -> bool:
        """
        Returns True if 'word_a' and 'word_b' are words, and an anagram
        of each other.

        Args:
            word_a (str):
                First word of pair to check.
            word_b (str):
                Second word of pair to check.

        Returns:
            True if both input words are anagrams of each other, False otherwise.
        """
        if not is_word(word_a) or not is_word(word_b):
            return False

        word_a = word_a.lower()  # just in case, ignore capitalization
        word_b = word_b.lower()

        return sorted(word_a) == sorted(word_b)

    def order_of_isogram(word: str) -> int | None:
        """
        Return the order of isogram 'word' constitutes. If 'word' is not an isogram,
        then return None.

        An isogram is defined as a word where each distinct letter appears the same amount
        of times. The amount of repetitions of each letter is the order. For example 'intestinos'
        is an isogram of order 2.

        Args:
            word (str):
                Word for which we want to calculate the isogram order.

        Returns:
            An integer representing the isogram order of the input word. If the input word
            is not an isogram, return None.
        """
        if not is_word(word):
            return None

        count = {}
        for letter in word:
            count[letter] = count.get(letter, 0) + 1

        orders = set(count.values())

        return None if len(orders) > 1 else list(orders)[0]

    print("is_word('abc') ==", is_word("abc"))
    print("is_word('a bc') ==", is_word("a bc"))
    print("is_word('aCbc') ==", is_word("aCbc"))
    print("is_word('aC1c') ==", is_word("aC1c"))
    print("is_word('aC,c') ==", is_word("aC,c"))
    print("is_palindrome('abc') ==", is_palindrome("abc"))
    print("is_palindrome('abba') ==", is_palindrome("abba"))
    print("are_anagrams('abba', 'baba') ==", are_anagrams("abba", "baba"))
    print("are_anagrams('perro', 'gato') ==", are_anagrams("perro", "gato"))
    print("are_anagrams('Tokyo', 'Kyoto') ==", are_anagrams("Tokyo", "Kyoto"))
    for word in (
        "perro",
        "intestinos",
        "gato",
        "papelera",
        "baba",
        "cuscus",
    ):
        order = order_of_isogram(word)
        if order is None:
            print(f"La palabra '{word}' no es un isograma.")
        else:
            print(f"La palabra '{word}' es un isograma de orden {order}.")


if __name__ == "__main__":
    main()
    extra()
