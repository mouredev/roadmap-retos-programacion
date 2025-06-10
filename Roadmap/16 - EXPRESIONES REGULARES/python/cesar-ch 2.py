"""
    * #16 EXPRESIONES REGULARES
"""

import re

texto = "Es texto contiene 5 numeros del 1 al 5: 1,2,3,4,5"
regex_numeros = r"\d+"
print("Numeros encontrados:", re.findall(regex_numeros, texto))

"""
    * DIFICULTAD EXTRA
"""

email_correcto = "abc@mail.com"
email_incorrecto = "abcmail.com"
regex_email = r"^[a-zA-Z0-9._+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$"

print(
    f"{email_correcto} es un email válido? ",
    bool(re.match(regex_email, email_correcto)),
)
print(
    f"{email_incorrecto} es un email válido? ",
    bool(re.match(regex_email, email_incorrecto)),
)

numero_correcto = "+51 987654321"
numero_incorrecto = "987654321"
regex_numero = r"^\+[0-9]{2}\s[0-9]{9}$"

print(
    f"{numero_correcto} es un número válido? ",
    bool(re.match(regex_numero, numero_correcto)),
)
print(
    f"{numero_incorrecto} es un número válido? ",
    bool(re.match(regex_numero, numero_incorrecto)),
)

url_correcta = "https://retosdeprogramacion.com"
url_incorrecta = "retosdeprogramacion.com/"
regex_url = r"^https?://(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"

print(f"{url_correcta} es una URL válida? ", bool(re.match(regex_url, url_correcta)))
print(
    f"{url_incorrecta} es una URL válida? ", bool(re.match(regex_url, url_incorrecta))
)
