"""
/*
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
 */
"""

import re

def find_extract(text: str):
    regex_pattern = r"\d"
    findall = re.findall(regex_pattern, text, re.I)
    return findall
print(find_extract("Est5o e8s un 8te9xto con numeros4"))

#Extra

def mail_validate(email: str):
    mail_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(mail_pattern, email))
print(mail_validate("alan2085@gmail.com"))

def phone_validate(phone: str):
    phone_pattern = r'^(\+\d{1,3}\s?)?[-\s]?[0-9]{7,8}$'
    return bool(re.match(phone_pattern, phone))

print (phone_validate("+569 53155806"))

def url_validate(url: str):
    url_pattern = r"^[a-zA-Z0-9_.+-]+:+//[a-zA-Z0-9-.]+[a-zA-Z0-9-.]+$"
    return bool(re.match(url_pattern, url))

print(url_validate("https://www.google.com"))
