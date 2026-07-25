# RETO 16 EXPRESIONES REGULARES

import re

"""
EXPRESIÓN REGULAR QUE SEA CAPAZ DE
EXTRAER TODOS LOS NÚMEROS DE UN TEXTO
"""

def find_numbers(text: str) -> list:
    return re.findall(r"\d+", text)

print(find_numbers("El 20/07/1969, la misión estadounidense Apolo 11 colocó a los primeros hombres en la Luna: el comandante Neil Armstrong y el piloto Edwin F. Aldrin"))

# Extra

print("🧩 DIFICULTAD EXTRA - 3 EXPRESIONES REGULARES 🧩")

"""
CREA 3 EXPRESIONES REGULARES CAPACES DE:
1.- VALIDAR UN EMAIL
2.- VALIDAR UN NÚMERO DE TELÉFONO
3.- VALIDAR UNA URL
"""

def validate_email(email: str) -> bool:
    return bool(re.match(r"^[w.+-]+@[\w]+ \.[a-zA-Z]+$", email))

print(validate_email("zetar92@mail.com"))

def validate_phone(phone: str) -> bool:
    return bool(re.match(r"^\+?[\d\s]{3,}$", phone))

print(validate_phone("+34 928 00 00 00"))

def validate_url(url: str) -> bool:
    return bool(re.match(r"^http[s]?://(www.)?[\w]+\.[a-zA-Z]{2,}$", url))

print(validate_url("http://www.zeta92.dev"))