'''
 EJERCICIO:
* Utilizando python, explora el concepto de expresiones regulares,
* creando una que sea capaz de encontrar y extraer todos los números
* de un texto.
'''
import re

def num_text(texto: str) -> list:
    return re.findall(r"\d+", texto)


frase = "Fue a por 100 cervezas y trajo 95"

print(num_text(frase))


print("*"*60)

'''
* DIFICULTAD EXTRA (opcional):
* Crea 3 expresiones regulares (a tu criterio) capaces de:
* - Validar un email.
* - Validar un número de teléfono.
* - Validar una url.
'''

def email_text(email:str) -> bool:
    return re.match(r"^[\w]+@[\w]+\.[\w]{3}$", email)

print(bool(email_text("rsog066@gmail.com")))

print("*"*60)

def tlf_text(tlf:str) -> bool:
    return re.match(r"^\+|(00)[\d]{2}[\s][\d]{9}$", tlf)

print(bool(tlf_text("0034 618846071")))

print("*"*60)

def url_text(url:str) -> bool:
    return re.match(r"^http[s]?://(w)*\.*[\w]+\.[\w]+$", url)

print(bool(url_text("https://www.google.com")))