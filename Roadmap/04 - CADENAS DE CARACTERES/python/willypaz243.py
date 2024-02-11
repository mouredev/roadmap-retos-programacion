"""Todo lo que se puede hacer con strings en python"""
import sys
from typing import Any

from colorama import Fore, Style


def print_colored(name: str, value: Any, description: str, *args: list[str]):
    """Print colored"""
    string = Style.RESET_ALL + name + " "
    string += Fore.RED + str(value) + " "
    string += Fore.GREEN + description
    string += " ".join([str(arg) for arg in args])
    print(string.strip())


def string_functions(string: str) -> None:
    """Todas las funciones que contiene el obejeto string"""
    print(f"Original String: {string}\n")

    print_colored(
        "1. capitalize():",
        string.capitalize(),
        "Retorna el string con el primer caracter en Mayuscula",
    )
    print_colored(
        "2. casefold():",
        string.casefold(),
        "Retorna el string con todos los caracteres en minusculas",
    )
    print_colored(
        "3. center(20, '*'):",
        string.center(20, "*"),
        "Retorna un string del tamaño n=20 con el string original en el centro",
    )
    print_colored(
        "4. count('l'):",
        string.count("l"),
        "Cuenta las veces que aparece el sub-string 'l' en el string",
    )
    print_colored(
        "5. encode():",
        string.encode(),
        "Convierte el string a bytes",
    )
    print_colored(
        "6. endswith('world'):",
        string.endswith("world"),
        "Comprueba si el string termina en 'world'",
    )
    print_colored(
        "7. find('l'):",
        string.find("l"),
        "Retorna el indice inicial de la primera vez que aparece el sub-string 'l'",
    )
    print_colored(
        "8. format('John'):",
        string.format("John"),
        "Reemplaza \{\} con 'John'",
    )
    try:
        print_colored(
            "9. index('l'):",
            string.index("l"),
            "Hace exactamente lo mismo que 'find('l')'",
        )
    except ValueError as error:
        print_colored(
            "9. index('l'):",
            error,
            "Hace lo mismo que 'find('l')' pero lanza ValueError si no encuentra el subtring",
        )
    print_colored(
        "10. isalnum():",
        string.isalnum(),
        "Verifica si el string es numerico o alfabético",
    )
    print_colored(
        "11. isalpha():",
        string.isalpha(),
        "Verifica si el string es solamente alfabético",
    )
    print_colored(
        "12. isdecimal():",
        string.isdecimal(),
        "Verifica si todos los caracteres en el string son decimales",
    )
    print_colored(
        "13. isdigit():",
        string.isdigit(),
        "Verifica si todos los caracteres en el string son dígitos",
    )
    print_colored(
        "14. islower():",
        string.islower(),
        "Verifica si todos los caracteres en el string están en minúsculas",
    )
    print_colored(
        "15. isnumeric():",
        string.isnumeric(),
        "Verifica si todos los caracteres en el string son numéricos",
    )
    print_colored(
        "16. isspace():",
        string.isspace(),
        "Verifica si todos los caracteres en el string son espacios en blanco",
    )
    print_colored(
        "17. istitle():",
        string.istitle(),
        "Verifica si el string está en formato de título (cada palabra comienza con mayúscula)",
    )
    print_colored(
        "18. isupper():",
        string.isupper(),
        "Verifica si todos los caracteres en el string están en mayúsculas",
    )
    print_colored(
        "19. join(['a', 'b', 'c']):",
        "-".join(["a", "b", "c"]),
        "Une elementos de un iterable (por ejemplo, una lista) en un string utilizando el string como separador",
    )
    print_colored(
        "20. ljust(20, '*'):",
        string.ljust(20, "*"),
        "Retorna un string justificada a la izquierda en un ancho dado, con caracteres de relleno opcionales",
    )
    print_colored(
        "21. lower():", string.lower(), "Retorna una copia de el string en minúsculas"
    )
    print_colored(
        "22. lstrip():",
        string.lstrip(),
        "Elimina los espacios en blanco a la izquierda de el string",
    )
    print_colored(
        "23. partition('l'):",
        string.partition("l"),
        "Divide el string en tres partes usando un separador y devuelve una tupla",
    )
    print_colored(
        "24. replace('l', 'x'):",
        string.replace("l", "x"),
        "Reemplaza todas las ocurrencias de un sub-string con otra",
    )
    print_colored(
        "25. rfind('l'):",
        string.rfind("l"),
        "Similar a find(), pero busca desde el final de el string",
    )
    try:
        print_colored(
            "26. rindex('l'):",
            string.rindex("l"),
            "Similar a index(), pero busca desde el final de el string",
        )
    except ValueError as error:
        print_colored(
            "26. rindex('l'):",
            error,
            "Similar a index(), pero busca desde el final de el string",
        )
    print_colored(
        "27. rjust(20, '*'):",
        string.rjust(20, "*"),
        "Devuelve un string justificada a la derecha en un ancho dado, con caracteres de relleno opcionales",
    )
    print_colored(
        "28. rpartition('l'):",
        string.rpartition("l"),
        "Divide el string en tres partes usando un separador, comenzando desde el final",
    )
    print_colored(
        "29. rsplit(' ', 1):",
        string.rsplit(" ", 1),
        "Divide el string en sub-strings utilizando un separador desde la derecha",
    )
    print_colored(
        "30. rstrip():",
        string.rstrip(),
        "Elimina los espacios en blanco a la derecha de el string",
    )
    print_colored(
        "31. split(' '):",
        string.split(" "),
        "Divide el string en sub-strings utilizando un separador",
    )
    print_colored(
        "32. splitlines():",
        string.splitlines(),
        "Divide el string en líneas y devuelve una lista de líneas",
    )
    print_colored(
        "33. startswith('Hello'):",
        string.startswith("Hello"),
        "Verifica si el string comienza con el prefijo especificado",
    )
    print_colored(
        "34. strip():",
        string.strip(),
        "Elimina los espacios en blanco al principio y al final de el string",
    )
    print_colored(
        "35. swapcase():",
        string.swapcase(),
        "Intercambia mayúsculas y minúsculas en el string",
    )
    print_colored(
        "36. title():",
        string.title(),
        "Devuelve una versión de el string con cada palabra en mayúsculas",
    )
    print_colored(
        "37. upper():", string.upper(), "Devuelve una copia de el string en mayúsculas"
    )
    print_colored(
        "38. zfill(20):",
        string.zfill(20),
        "Rellena el string con ceros a la izquierda hasta alcanzar la longitud especificada",
    )


def string_operations_example(string_1: str, string_2: str):
    """Operaciones que se pueden realizar a uno o varios strings"""
    result_concat = string_1 + ", " + string_2

    print("Strings originales: ", string_1, string_2)

    print_colored(
        "1. Concatenación: 'str1' + 'str2'",
        result_concat,
        "Combina dos o más strings en una sola string más larga",
    )

    result_repeat = string_1 * 3
    print_colored(
        "2. Repetición: str * 3",
        result_repeat,
        "Repite un string un número especificado de veces",
    )

    result_format = "La primera string es '{}' y la segunda es '{}'.".format(
        string_1, string_2
    )
    print_colored(
        "3. 'Formateo de \{string\}'.format('string'):",
        result_format,
        "Incorpora valores en un string usando marcadores de posición",
    )

    len_str1 = len(string_1)
    print_colored(
        "4. Longitud de el string len(str):",
        len_str1,
        "Obtiene la cantidad de caracteres en un string",
    )

    first_char = string_1[0]
    last_char = string_1[-1]
    print_colored(
        "5. Acceso a caracteres por índice: str[0], str[-1]",
        f"Primer caracter: {first_char}, Último caracter: {last_char}",
        "Obtiene caracteres individuales de un string utilizando su posición",
    )

    slice_str1 = string_1[1:4]
    print_colored(
        "6. Slice de string (índices 1 a 3): str[1:4]",
        slice_str1,
        "Extrae una porción específica de un string",
    )

    reverse_string = string_1[::-1]
    print_colored(
        "7. invertir string: str[::-1]",
        reverse_string,
        "Invierte los caracteres del string",
    )


def is_palindrome(string: str):
    return string[::-1] == string


def are_anagrams(string_1: str, string_2: str):
    return sorted(string_1) == sorted(string_2)


def are_isograms(string_1: str, string_2: str):
    return len(set(string_1)) == len(string_1) and len(set(string_2)) == len(string_2)


def main():
    """The Main Function"""

    if not len(sys.argv) > 1:
        raise Exception("Debe proporcionar algun argumento de string para la función.")
    string_functions(sys.argv[1])
    if not len(sys.argv) > 2:
        print("Pase 2 string como argumentos para mostrar las demas operaciones")
        return
    string_operations_example(sys.argv[1], sys.argv[2])
    print_colored(
        "Son Palindromos",
        f"string 1: {is_palindrome(sys.argv[1])}, string 2: {is_palindrome(sys.argv[2])}",
        "Verifica si el primer string es un palindromo del segundo string y biceversa",
    )
    print_colored(
        "Son Anagramas",
        are_anagrams(sys.argv[1], sys.argv[2]),
        "Verifica si un string es un anagrama del otro string",
    )
    print_colored(
        "Son Isogramas",
        are_isograms(sys.argv[1], sys.argv[2]),
        "Verifica si los strings son isogramas",
    )


if __name__ == "__main__":
    main()
