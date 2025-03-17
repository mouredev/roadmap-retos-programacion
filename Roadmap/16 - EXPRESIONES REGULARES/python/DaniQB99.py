'''
EJERCICIO:
Utilizando tu lenguaje, explora el concepto de expresiones regulares,
creando una que sea capaz de encontrar y extraer todos los numeros de
un texto.
'''

import re

def find_numbers(text: str) -> list:
    # return re.findall(r'[0-9]+', text)
    return re.findall(r'\d+', text)  # \d es un alias para [0-9]

print(find_numbers("Hola, mi nombre es Daniel y nací el 26/07/1999"))


'''
DIFICULTAD EXTRA (opcional):
Crea 3 expresiones regulares (a tu criterio) capaces de:
- Validar un email.
- Validar un número de teléfono.
- Validar una url.
'''

print("\n\nDIFICULTAD EXTRA\n")

# Email
def validate_email(email: str) -> bool:
    pattern = r'^[\w.+-]+@+[\w]+\.(?:com|net|es|ai|ia|mx|co|uy|org)$'
    if re.match(pattern, email):
        return email + " es válido"
    return email + " no es válido"

    # \w es un alias para [a-zA-Z0-9_]
    # \d es un alias para [0-9] 
    # $ indica el final de la cadena
    # + indica que se puede repetir 1 o más veces
    # ^ indica que se debe empezar en la primera posición
    # (?:com|net|es|ai|ia|mx|co|uy|org) es un grupo de caracteres que se puede repetir 0 o más veces
    
print(validate_email("daniqb99@gmail.com"))
print(validate_email("daniqb99@gmail.com.com"))

# Número de teléfono
def validate_phone(phone: str) -> bool:
    pattern = r'^\+34(6|7)[0-9]{8}$'
    if re.match(pattern, phone):
        return phone + " es válido"
    return phone + " no es válido"

print(validate_phone("+34649116982"))
print(validate_phone("+34649116982a"))

# URL
def validate_url(url: str) -> bool:
    pattern = r'^http[s]?://(www.)?[\w]+\.(?:com|net|es|ai|ia|mx|co|uy|org)$'
    if re.match(pattern, url):
        return url + " es válida"
    return url + " no es válida"

print(validate_url("https://www.google.es"))
print(validate_url("https://google.es"))
print(validate_url("https://google.es.com"))