""" /*
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
 */ """

import re

#EJERCICIO

def find_numbers(text: str) -> list:
    return re.findall(r"[0-9]+", text)

print(find_numbers("Este es el ejercicio 16."))

#DIFICULTAD EXTRA

def email_check(email: str) -> bool:
    return bool(re.match(r"^[\w.+-]+@[\w]+\.[a-zA-Z]+$", email))

print(email_check("ropeda98@gmail.com"))
print(email_check("ropeda98@gmailcom"))

def phone_number_check(phonenumber: str) -> bool:
    return bool(re.match(r"^[+]?[\d\s]{3,}$", phonenumber))

print(phone_number_check("444444444"))
print(phone_number_check("444 44 44 44"))
print(phone_number_check("+44 4444444"))
print(phone_number_check("4"))

def url_check(url: str) -> bool:
    return bool(re.match(r"^http[s]?://(www.)?[\w]+\.[a-zA-Z]+$", url))

print(url_check("https://klajsdlkas.com"))
print(url_check("http://klajsdlkas.com"))
print(url_check("http://www.klajsdlkas.com"))
print(url_check("http://klajsdlkas"))