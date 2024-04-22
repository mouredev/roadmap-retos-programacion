"""
 * EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
"""

import re

test_cases = ["1249830hola", "Esto nos costó 56800", "1278, no se, 2121"]

pattern = r"\d+"
results = [re.findall(pattern, test_case) for test_case in test_cases]
print(results)

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
"""

email_pattern = r"^\w+@\w+\.\w+$"
phone_pattern = r"^3[0-9]{9}$"
url_pattern = r"^https?:\/\/[\w\-]+(\.[\w\-]+)+[/#?]?.*$"

test_emails = [
    "juandaherreparra@gmail.com",
    "juanda.com",
    "juanda@gmail",
    "juanda45@yahoo.es",
    "no soy un correo",
]

test_phones = ["3218199645", "2178929201", "3128436677", "31284399001"]

test_urls = [
    "http://www.juanda.com",
    "https://www.juanda.com",
    "https://web.com.co",
    "https://www.my_web.com/hola_mundo",
    "321819",
    "prueba",
]


def compare_pattern(pattern: str, compare_list: list[str]) -> dict[str, bool]:
    print({compare_item: bool(re.match(pattern, compare_item)) for compare_item in compare_list})


compare_pattern(email_pattern, test_emails)
compare_pattern(phone_pattern, test_phones)
compare_pattern(url_pattern, test_urls)
