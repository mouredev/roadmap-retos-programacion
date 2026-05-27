# EJERCICIO:
# Utilizando tu lenguaje, explora el concepto de expresiones regulares,
# creando una que sea capaz de encontrar y extraer todos los números
# de un texto.
import re


def find_numbers(text: str) -> list:
    return re.findall(r"\d+", text)

texto = "Este es el ejercicio 16 publicado 15/04/2024."
print(find_numbers(texto))


#
# DIFICULTAD EXTRA (opcional):
# Crea 3 expresiones regulares (a tu criterio) capaces de:
# - Validar un email.
# - Validar un número de teléfono.
# - Validar una url.

def validate_email(email: str) -> bool:
    return bool(re.match(r"^[\w.+-]+@[\w]+\.[a-zA-Z]+$", email))

def validate_phone(phone: str) -> bool:
    return bool(re.match(r"^\+?[\d\s-]{3,}$", phone))

def validate_url(url: str) -> bool:
    return bool(re.match(r"^http[s]?://(www.)?[\w]+\.[a-zA-Z]{2,}$", url))

email = "test@test.com"
phone = "+54-9-011-4223-5656"
phone2 = "+54 9 011 4223 5656"
url = "https://www.test.com"

print(validate_email(email))
print(validate_phone(phone))
print(validate_phone(phone2))
print(validate_url(url))

"""
Patrones comunes para validaciones:

- ^  : Inicia la expresión.
- \d : Un dígito (0-9).
- \w : Un carácter alfanumérico (letras, números, guión bajo).
- \s : Espacio en blanco.
- [] : Define un conjunto de caracteres (ejemplo: [a-z] para letras minúsculas).
- () : Define un grupo de caracteres (ejemplo: (a-z) para letras minúsculas).
- *  : 0 o mas repeticiones.
- +  : 1 o mas repeticiones.
- ?  : 0 o una repeticion.
- .  : cualquier caracter (excepto salto de linea).
- $  : Termina la expresión.
"""