"""EJERCICIO:
Utilizando tu lenguaje, explora el concepto de expresiones regulares,
creando una que sea capaz de encontrar y extraer todos los números
de un texto."""

import re


def find_numbers_in_a_text(text: str):
    numbers = re.findall(r'\d+\.?\d*', text)
    if numbers:
        print(f'The number founded in the text are: {numbers}')
        return
    else:
        print('There are no numbers in the text')
        return

"""DIFICULTAD EXTRA (opcional):
Crea 3 expresiones regulares (a tu criterio) capaces de:
- Validar un email.
- Validar un número de teléfono.
- Validar una url."""


def is_email(email: str):
    email_pattern = r'^[\w\._-]+@[\w\._-]+\.\w+$'
    if re.match(pattern=email_pattern, string=email):
        print(f'The email "{email}" is a valid email')
    else:
        print(f'The text "{email}" is not a valid email')


def is_phone_number(phone_number: str):
    phone_number_pattern = r'^(\(\d{3}\)|\d{3})[\s.-]?\d{3}[\s.-]?\d{4}$'
    if re.match(pattern=phone_number_pattern, string=phone_number):
        print(f'The phone number "{phone_number}" is a valid phone number')
    else:
        print(f'The phone number "{phone_number}" is not a valid phone number')


def is_url(url: str):
    url_pattern = r'^(https):\/\/([A-Za-z0-9\-._~:/?#[\]@!$&\'()*+,;=%]+)$'
    if re.match(pattern=url_pattern, string=url):
        print(f'The url "{url}" is a valid url')
    else:
        print(f'The "{url}" is not a valid url')


find_numbers_in_a_text(input('Enter text to analyze (to find numbers): '))
print('********')
is_email(input('Enter an email to validate: '))
print('********')
is_phone_number(input('Enter a phone number (don\'t include country code): '))
print('********')
is_url(input('Enter an url: '))
