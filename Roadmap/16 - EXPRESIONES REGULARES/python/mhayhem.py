# EJERCICIO:
# Utilizando tu lenguaje, explora el concepto de expresiones regulares,
# creando una que sea capaz de encontrar y extraer todos los números
# de un texto.

import re

text = "Hola, 12 de cada 20 animales están abandocnados en una calle"

patron = r"\d+"

nums = re.findall(patron, text)
print(nums)

# DIFICULTAD EXTRA (opcional):
# Crea 3 expresiones regulares (a tu criterio) capaces de:
# - Validar un email.
# - Validar un número de teléfono.
# - Validar una url.


def re_web(text: str):
    re_url = r"^(www)\.[a-z0-9.+-]+\.[a-z]{2,10}$"
    is_web = bool(re.fullmatch(re_url, text))
    return is_web


def re_telephon_number(phone: str):
    re_phone = r"^\d{9}$"
    is_phone = bool(re.fullmatch(re_phone, phone))
    return is_phone


def re_mail(mail: str):
    re_mail = r"^[A-Za-z0-9.+-]+@[A-Za-z0-9.+-]+\.[A-Za-z]{2,63}$"
    is_mail = bool(re.fullmatch(re_mail, mail))
    return is_mail

