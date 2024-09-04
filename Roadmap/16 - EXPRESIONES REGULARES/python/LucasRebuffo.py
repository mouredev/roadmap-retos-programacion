""" /*
 * EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
 */ """

import re

regex = r"[\d]+"

found = re.compile(regex).findall("1515dasdsd55dsf897fdfd988 !@ 15")

print(found)


regex_email = r"^[\w\.+-]+@[\w]+\.[a-zA-Z]{2,4}$"

def validate_email(email: str):
    return bool(re.match(regex_email,email))

print(validate_email("lucas@gmail.com"))
print(validate_email("lucasgmail.com"))

regex_phone = r"^\+?[\d\s]{3,}$"

def validate_phone(phone: str):
    return bool(re.match(regex_phone,phone))

print(validate_phone("1131639967"))
print(validate_phone("11 3163 9967"))
print(validate_phone("113163a99674"))
print(validate_phone("+54 11316399674"))


regex_url = r"^http[s]?://(www.)?[\w]+\.[a-zA-Z]{2,4}$"

def validate_url(url: str):
    return bool(re.match(regex_url,url))

print(validate_url("http://lucas.dev"))
print(validate_url("http://www.lucas.dev"))
print(validate_url("https://lucas.dev"))
print(validate_url("https://www.lucas.dev"))
print(validate_url("https://ww.lucas.dev"))

