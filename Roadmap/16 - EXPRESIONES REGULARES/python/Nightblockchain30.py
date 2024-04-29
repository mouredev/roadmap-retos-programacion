
# 
#
# EJERCICIO:
# Utilizando tu lenguaje, explora el concepto de expresiones regulares,
# creando una que sea capaz de encontrar y extraer todos los números
# de un texto.
#
# DIFICULTAD EXTRA (opcional):
# Crea 3 expresiones regulares (a tu criterio) capaces de:
# - Validar un email.
# - Validar un número de teléfono.
# - Validar una url.
#

import re

def find_numbers(text: str)-> list:
    return re.findall(regex,text)

regex = r'\d+'
text = "1234 Hola soy un 56 texto de ejemplo 78 9"

print(find_numbers(text))


# EXTRA

def check_email(email: str)->bool:
    return bool(re.match(regex_email,email))

regex_email = r'^[\w.+-_]+@[\w]+\.[a-z]{2,3}$'
email = "nig_h-t+@gmail.com"

print(check_email(email))


def check_number(number: str)->bool:
    return bool(re.search(regex_number,number))

regex_number = r'^(\+[0-9]{1,3}\s)?\d{1,9}$'
number = "567437079"

print(check_number(number))


def check_url(url : str)->bool:
    return bool(re.match(regex_url,url))

regex_url = r'^(http[s]?://)?[\w]+\.[\w]+\.[a-z]{2,}$'
url = "https://www.google.com"

print(check_url(url))