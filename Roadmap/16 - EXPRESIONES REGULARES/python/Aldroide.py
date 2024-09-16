import re
""" 
    Utilizando tu lenguaje, explora el concepto de expresiones regulares,
    creando una que sea capaz de encontrar y extraer todos los números
    de un texto.
"""

regex = r"[0-9]+"
text = "Ejercicio del 15/04/2024"


def find_number(text: str) -> list:
    return re.findall(r"\d+", text)


print(find_number("Ejercicio 16 del 15/04/2024"))


"""
    Ejercicio Extra
    Crea 3 expresiones regulares (a tu criterio) capaces de:
        * Validar un email.
        * Validar un número de teléfono.
        * Validar una url.
"""


def validar_email(text: str) -> bool:
    return bool(re.match(r"^[\w.+-]+@[\w]+\.[a-zA-z]+", text))


def validar_telefono(phone: str) -> bool:
    return bool(re.match(r"^\+?[\d\s]{3,}$", phone))


def validar_url(url: str) -> bool:
    return bool(re.match(r"^http[s]?://(www.)?[\w]+\.[a-zA-z]{2,}$", url))


print(validar_email("Aldroide@gmail.com"))
print(validar_telefono("+5394576298"))
