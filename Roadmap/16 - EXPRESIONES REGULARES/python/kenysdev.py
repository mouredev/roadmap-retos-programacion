# ╔═════════════════════════════════════╗
# ║ Autor:  Kenys Alvarado              ║
# ║ GitHub: https://github.com/Kenysdev ║
# ║ 2024 -  Python                      ║
# ╚═════════════════════════════════════╝

# -----------------------------------
# * EXPRESIONES REGULARES
# -----------------------------------
# https://docs.python.org/es/3/howto/regex.html

"""
* EJERCICIO #1:
* Utilizando tu lenguaje, explora el concepto de expresiones regulares,
* creando una que sea capaz de encontrar y extraer todos los números
* de un texto.
"""

import re

def to_numbers(text: str) -> list:
    number_pattern = r'\d+'
    return re.findall(number_pattern, text)

string = "abcdsfs1s(*&#}2. a3// 45sdf67"
list_numbers = to_numbers(string)
print(list_numbers)


"""
* EJERCICIO #2:
* Crea 3 expresiones regulares (a tu criterio) capaces de:
* - Validar un email.
* - Validar un número de teléfono.
* - Validar una url.
"""

def is_email(text: str) -> bool:
    pattern = r'^[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, text):
        return True
    else:
        return False

def is_phone_number(text: str) -> bool:
    pattern = r'^(\d{3}-\d{3}-\d{4}|\d{10})$'
    if re.match(pattern, text):
        return True
    else:
        return False

def is_url(text: str) -> bool:
    pattern = r'^(https?://)?(www\.)?([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(/\S*)?$'
    if re.match(pattern, text):
        return True
    else:
        return False


print("\nis_email")
print(is_email("ejm@dmn.com"))        # True
print(is_email("e_jm-2+b@dmn.co.hn")) # True
print(is_email("ejm@dmn.com_"))       # False
print(is_email("ejm@dmn"))            # False

print("\nis_email")
print(is_phone_number("123-456-7890"))  # True
print(is_phone_number("1234567890"))    # True
print(is_phone_number("123456-7890"))   # False
print(is_phone_number("uno234567890"))  # False

print("\nis_url")
print(is_url("http://www.ejm.com"))   # True
print(is_url("google.com"))           # True
print(is_url("ejm.com/a/b/c"))        # True
print(is_url("https://.ejm.com"))     # False
print(is_url("https://.ejm.com/a b")) # False

