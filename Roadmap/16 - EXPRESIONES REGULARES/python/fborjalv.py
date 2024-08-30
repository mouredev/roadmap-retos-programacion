import re




"""
/*
 * EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
 *
"""




text = "Este es el ejercicio 16 publicado 15/04/2024"


def find_numbers(text):
    return re.findall(r"\d+", text)

print(find_numbers(text))

"""
* DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
 */

"""

def validate_email(email):
    return bool(re.match(r"^[\w.+-]+@[\w]+\.[a-zA-Z]+$", email)) 


print(validate_email("fborjalv@gmail.com"))

def validate_phone_number(phone):
    return bool(re.match(r"^\+?[\d\s]{3,}$", phone))

print(validate_phone_number("+34 679200199"))

def validate_url(url):
    return bool(re.match(r"^http[s]?://(www.)?[\w]+\.[a-zA-Z]+$", url))

print(validate_url("https://mouredev.es"))