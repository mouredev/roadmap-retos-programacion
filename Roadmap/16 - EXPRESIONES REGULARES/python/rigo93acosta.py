'''
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
'''

import re

"""
Ejericio
"""

# regex = r"[0-9]+" # Otra forma de hacerlo
regex = r"\d+"

text = "El 18/12/2022 Argentina ganó el mundial de fútbol."

def find_numbers(text: str, regex) -> list:
    return re.findall(regex, text)


print(find_numbers(text, regex))

"""
Extra
"""

def validate_email(email: str) -> bool:
    
    regex = r"^[\w.+-]+@[\w]+\.[a-zA-Z]+$"
    return bool(re.match(regex, email))

def validate_phone(phone: str) -> bool:

    regex = r"^\+?[\d\s]{3,}$"
    return bool(re.match(regex, phone))

def validate_url(url: str) -> bool:

    regex = r"^http[s]?://(www.)?[\w]+\.[a-zA-Z]{2,}$"
    return bool(re.match(regex, url))

print(validate_email("rigo93acosta@gmail.com"))
print(validate_phone("+54 9 11 555 55555"))
print(validate_url("https://www.google.com"))
