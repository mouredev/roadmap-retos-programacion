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

def find_numbers(text):

    pattern_num = r"-?\d+\.?\d*"
    numbers_found = re.findall(pattern_num, text)
    numbers_found = [float(num) for num in numbers_found]
    return numbers_found

texto = "Este es un texto de prueba con varios numeros: 123, 45.6, -0.3, 789. Es importante encontrarlos todos."
numeros = find_numbers(texto)

print(numeros)


########## --------------------------- EXTRA ------------------------------  #####################


def validate_email(email: str):

    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(pattern, email):
        return True
    else:
        return False    
print(validate_email("nombre.apellido123@dominio.com"))
print(validate_email("correo.invalido@com"))


def validate_phoneNumber(num):
    
    pattern_num = r'^(\+\d{1,3}\s?)?[-\s]?[0-9]{7,8}$'
    if re.match(pattern_num, num):
        return True
    else:
        return False    
print(validate_phoneNumber("+591 79338521"))


def validar_url(url):
    pattern_url = r"^(https?://)?(www\.)?[\w\.-]+\.[a-zA-Z]{2,}(/\S*)?$"
    if re.match(pattern_url, url):
        return True
    else:
        return False    
print(validar_url("http://www.moure.dev"))





