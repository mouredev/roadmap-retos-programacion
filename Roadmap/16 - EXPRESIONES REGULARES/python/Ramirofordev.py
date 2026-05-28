# Crea una expresion regular que sea capaz de encontrar y extraer todos los numeros de un texto.

import re

def get_numbers(text: str) -> str:
    numbers = re.findall(r'\d+', text)
    return numbers

print(get_numbers("562489X"))

'''
Dificultad extra:
Crea 3 expresiones regulares capaces de:
    * Validar un email
    * Validar un numero de telefono
    * Validar una url
'''

def check_email(em: str):
    if re.fullmatch(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', em):
        return True
    else:
        return False
    
print(check_email("nacho.ramiro@gmail.com"))

def check_phone_number(number: str):
    if re.fullmatch(r'^\+34[0-9]{9}$', number.replace(" ", "")):
        return True
    else:
        return False

print(check_phone_number("+34 889 89 22 34"))

def check_url(url: str):
    if re.fullmatch(r'https?://[a-zA-Z0-9.-]?[a-zA-Z0-9.-]+(?:/[a-zA-Z0-9._/-]*)?(?:\?[a-zA-Z0-9&=%._/-]*)?', url):
        return True
    else:
        return False
    
print(check_url("https://campus.mouredev.pro/courses/take/logica-programacion/lessons/62605792-expresiones-regulares"))