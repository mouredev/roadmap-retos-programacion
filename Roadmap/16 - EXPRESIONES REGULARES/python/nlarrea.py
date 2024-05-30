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

import re

text = """
Lorem ipsum dolor1 sit amet, consectetur adipiscing elit. Nullam ac mi in
ipsum ultricies 2 varius. Nullam euismod, justo nec fermentum ultricies, nunc
nisl tempus purus, 3 sed dictum 563 nulla odio nec purus. Nullam nec purus
consectetur, consectetur justo. 10 Nullam nec purus consectetur, consectetur.
"""

numbers_pattern = r"[\d]{1,}"
numbers = re.findall(numbers_pattern, text)
print(numbers)
# ['1', '2', '3', '563', '10']

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
"""


def print_test(pattern: str, text: str) -> bool:
    print(text + ":", bool(re.match(pattern, text)))


print("\nTesting emails:")
email_pattern = r"^[\w]{1,}[\w\d\._]{4,}\@[\w]{2,}\.[\w]{2,3}$"
print_test(email_pattern, "an_email@gmail.com")  # True
print_test(email_pattern, "1234@email.com")  # False
print_test(email_pattern, "an_email1234")  # False
print_test(email_pattern, "an2_email4@gmail.com")  # True
print_test(email_pattern, "another.2024@gmail")  # False
print_test(email_pattern, "another.2024@gmail.")  # False
print_test(email_pattern, "another.2024@gmail.com")  # True

phone_pattern = r"^\+?\d{3,}$"
print_test(phone_pattern, "123456789")  # True
print_test(phone_pattern, "+34123456789")  # True
print_test(phone_pattern, "abcdefghi")  # False

url_pattern = r"^https?://(w{3}\.)?[\w\d\.\-\?]+\.[\w]{2,}/?$"
print_test(url_pattern, "https://github.com/")  # True
print_test(url_pattern, "https://www.twitch.tv/")  # True
