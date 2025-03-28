import re
"""
Expresiones regulares
"""





def find_numbers(text: str) -> list:
    """Esta función se encarga de buscar números en el texto"""
    return re.findall(r"\d+", text)

text = "Esta es el ejercicio 16 publicado el 15/04/2024"
print(find_numbers(text))


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
 */
"""

def validate_email(email: str) -> bool:
    return bool(re.match(r"^[\w.+-]+@[\w]+.[a-zA-Z]+$", email))

print(validate_email("juanmajge@gmail.com"))

def validate_phone(phone: str) -> bool:
    return bool(re.match(r"^\+?[\d\s]{3,}$", phone))

print(validate_phone("+123"))

def validate_url(url: str) -> bool:
    return bool(re.match(r"^http[s]?://(www.)?[\w]+\.[a-zA-Z]+$", url))

print(validate_url("https://juanma.com"))

print(validate_url("https://www.juanma.com"))