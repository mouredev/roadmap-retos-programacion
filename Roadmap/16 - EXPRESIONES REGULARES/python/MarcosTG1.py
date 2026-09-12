
"""
* EJERCICIO:
* Utilizando tu lenguaje, explora el concepto de expresiones regulares,
* creando una que sea capaz de encontrar y extraer todos los números
* de un texto.
"""
import re

text = "Hola Cola fue un emperador bizantino en el año 542 A.C murió a los 97 años en Mongolia."

def find_numbers(text: str) -> list:

    ocurrencias = re.findall("[0-9]+", text)
    return ocurrencias

# print(find_numbers(text))

"""
* DIFICULTAD EXTRA (opcional):
* Crea 3 expresiones regulares (a tu criterio) capaces de:
* - Validar un email.
* - Validar un número de teléfono.
* - Validar una url.
"""
list_of_emails = ["pedro@gmail.com", "juis@gmail", "lorena 97 gamer@yahoo.com",
                "jonasbrothers-89@outlook.org", "PEDRO@GMAIL.COM", "contacto@mi-empresa24.com"]

list_of_phones = [
    "+34 901 65 89 04",
    "600123456",
    "+1 555 123 4567",
    "+34 654 321 098",
    "telefono_falso",
    "+34-901-65-89-04",
    "1234",
    "+abc 123 456"
]

list_of_urls = [
    "https://www.google.com",
    "http://moure.dev",
    "https://github.com",
    "http://www.ejemplo.org",
    "https://sitio_sin_dominio",
    "https://sitio_sin_dominio",
    "http://",
    "www.google.com",
    "esto_no_es_una_url"
]


regex_email = r"^[\w\.-]+@[a-zA-Z0-9\-]+\.[a-zA-Z]{2,6}$"
regex_email_moure = r"^[\w.+-]+@[\w]+\.[a-zA-Z]+$"

regex_phones = r"^(?=.{7,})[\+0-9]+\s?(?:[0-9]+\s?)*$"
regex_phones_moure = r"^\+?[\d\s]{3,}$"

regex_urls = r"^https?://[\w_.]+\.[\w]{3,5}$"

def validator(list, regex: str):
    ocurrencias = []
    for item in list: 
        if re.findall(regex, item):
            ocurrencias.append(True)
            print(re.match(regex, item).string)
        else:
            ocurrencias.append(False)
    return ocurrencias
        
    
# print(validator(list_of_emails))
print(validator(list_of_emails, regex_email))
print("\n")
print(validator(list_of_phones, regex_phones))
print("\n")
print(validator(list_of_urls, regex_urls))