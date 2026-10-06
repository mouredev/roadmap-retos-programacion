"""
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
"""

# URL: https://github.com/Asabeneh/30-Days-Of-Python/blob/master/18_Day_Regular_expressions/18_regular_expressions.md

import re

texto: str = "Uno es 1, dos es 2, tres es 3, cuatro es 4, cinco es 5, seis es 6, siete es 7, ocho es 8, nueve es 9 y cero es 0."

regex_pattern = r'[0-9]'
matches = re.findall(regex_pattern, texto)
print(matches); print()

regex_pattern = r'\d'
matches = re.findall(regex_pattern, texto)
print(matches); print()

txt: str = "Mi número de teléfono es 123-123-1234, y es mi tercer número que adquiero. Los 2 anteriores los perdí en fiestas. Fueron 5 fiestas que asistí y en cualquiera de esas 5 ocurrieron. 1, 2, 3, 4"

print(
    re.findall(r'\d', txt),
    re.findall(r'[0-9]', txt),
    '\n'
)

#### EXTRA ####

# EMAIL

email_pattern = r'[A-Za-z0-9]+@[A-Za-z0-9]+.[A-Za-z0-9]+'

emails = ['mail.mail@mail.com', 'fresh@gmail.com', '@.', 'jaun@juan.dru']

matches = []
for email in emails:
    matches.append(re.findall(email_pattern, email))
print(matches, '\n')

# NÚMERO DE TELÉFONO

phone_pattern = r'[0-9]{3}-*[0-9]{3}-*[0-9]{4}'

phones = ['552-123-1234', '5521231234', '557-1234321', '557123-4321', '@1231231234']

matches = []

for phone in phones:
    matches.append(re.findall(phone_pattern, phone))

print(matches, '\n')

# URL

url_pattern = r'http[s]?://[A-Za-z0-9./\-_%]{1,}'

urls = ["https://github.com/Asabeneh/30-Days-Of-Python/blob/master/18_Day_Regular_expressions/18_regular_expressions.md", "https://www.google.com"]

matches = []

for url in urls:
    matches.append(re.findall(url_pattern, url))
else:
    print(matches, '\n')


####

def find_numbers(text: str) -> list:
    return re.findall(r"\d+", text)

print(find_numbers(texto))
print(find_numbers(txt))
print(find_numbers("Este es el ejercicio 16 publicado 15/04/2024"))

def validate_email(email: str) -> bool:
    return bool(re.match(r"^[\w\.+\-]+@[\w]+\.[a-zA-Z]+$", email))

print(validate_email("mouredev@gmail.com"))
print(validate_email("mouredev@gmailcom"))
print()

def validate_phone(phone: str) -> bool:
    return bool(re.match(r"^\+?[\d\s]{3,}$", phone))

print(validate_phone("091"))
print(validate_phone("+52123123123091"))
print(validate_phone("091 123 4321"))
print()

def validate_url(url: str) -> bool:
    return bool(re.match(r"^http[s]?://(www.)?[\w]+\.[a-zA-Z]+$", url))