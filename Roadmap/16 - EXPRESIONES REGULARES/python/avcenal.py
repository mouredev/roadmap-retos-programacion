"""
 * EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
"""
import re

def extract_numbers(one_string):
    pattern = r"\d+"
    findall = re.findall(pattern,one_string)
    final=""
    for element in findall:
        final += element
    return final

print(f"Los números de la cadena \"4l3j4ndr0\" son: {extract_numbers("4l3j4ndr0")}")

"""
* DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
URL: ^https:\\\\(?:www\.)*[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)*\.(?:(?:com|net|org)|(?:es|ai|io))$
"""

def email_validation(one_email):
    pattern = r"^[A-Za-z]+(?:(?:\.|_)*[A-Za-z]*)*@[A-Za-z]+\.(?:com|net|es|ai|ia|mx|co|uy|org)$"
    match = re.match(pattern,one_email)
    if match == None:
        return False
    else:
        return True

def spanish_mobile_phone_number_validation(one_phone):
    pattern = r"^\+34(6|7)[0-9]{8}"
    match = re.match(pattern,one_phone)
    if match == None:
        return False
    else:
        return True
    
def url_validation(one_url): #faltaría añadir los casos de http: que aún existen dominios no seguros
    pattern = r"^(?:https:\\\\(?:www\.){0,1}|(?:https:\\\\){0,1}www\.)[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)*\.(?:(?:com|net|org|es|ai|io))$"
    match = re.match(pattern,one_url)
    if match == None:
        return False
    else:
        return True


if (email_validation("avcenal@gmail.com")):
    print("El email avcenal@gmail.com es válido")
else:
    print("El email avcenal@gmail.com no es válido")

if (spanish_mobile_phone_number_validation("+34649116982")):
    print("El teléfono +34649116982 es válido")
else:
    print("El teléfono +34649116982 no es válido")

if (url_validation("https:\\\\google.es")):
    print("La url https:\\\\google.es es válida")
else:
    print("La url https:\\\\google.es no es válida")
