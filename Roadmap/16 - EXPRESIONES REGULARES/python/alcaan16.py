"""/*
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
 */"""

import re

#ejercicio

frase = "hoy es el dia 22/01/2025"

def find(frase)-> list:
    return re.findall(r"\d+", frase)# entre comilla:\d el tipo de caracter y el + el numero de caracter
    #return re.findall(r"\d{2}", frase) #digitos separados por 2

print(find(frase))

#extra

email1 = "angel@correo.com"
email2 = "correo.com" 

def find_email(email)->bool:
    # encuentra solo el simbolo @ en la frase
    #if "@" in re.findall(r"[@]",email) : return True; 
    #else : return False
    
    return bool(re.match(r"^[\w.+-]+@[\w]+\.[a-zA-z]+$", email))

print(f"{email1} es un correo? {find_email(email1)}")
print(f"{email2} es un correo? {find_email(email2)}")

phone1 = "123456789"
phone2 = "13"

def find_phone(phone)->bool:

    return bool(re.match(r"^\+?[\d\s]{3,9}$", phone))
    
    
print(f"{phone1} es un telefono? {find_phone(phone1)}")
print(f"{phone2} es un telefono? {find_phone(phone2)}")

url1 = "http://www.google.com"
url2 = "cor" 



def find_url(url)->bool:
    
    return bool(re.match(r"^http[s]?://(www.)?[\w]+\.[a-zA-Z]{2,}$", url))

print(f"{url1} es un correo? {find_url(url1)}")
print(f"{url2} es un correo? {find_url(url2)}")
