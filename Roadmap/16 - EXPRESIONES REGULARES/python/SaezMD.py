#16 - EXPRESIONES REGULARES
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

def extract_numbers(text:str)-> str:

    numbers = re.findall('[\d]+',text)

    #To find commas, e.g. 12,300 or 12,300.00
    #r'[\d]+[.,\d]+'  
    #To find floats, e.g. 0.123 or .123
    #r'[\d]*[.][\d]+'     
    #To find integers, e.g. 123
    #r'[\d]+'

    all_numbers = "".join(numbers)
    return all_numbers

print(extract_numbers("hello23 numbers 1234, not"))
      
print(extract_numbers("hello 2,3 numbers 1234, not"))


#EXTRA:
#Validate EMAIL:
def validEmail(email):
    regexEmail = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regexEmail, email):
      print("Valid email")
    else:
      print("Invalid email")

validEmail("saezmd@gmail.net")
validEmail("sae.zmd@gmail.net")
validEmail("saezmd@gmail")
validEmail("saezmd@dotdot.net")
validEmail("saezmd@gmail..net")

#Validate Phone Number:
def validPhone(phoneNumber):
    regexPhone = re.compile(r'^(\+\d{1,2}|00\d{2})?[ -]*(6|7)[ -]*([0-9][ -]*){8}$')
    phoneNumber = str(phoneNumber)
    if re.fullmatch(regexPhone, phoneNumber):
      print("Valid phone")
    else:
      print("Invalid phone")

validPhone("0034612358902")
validPhone("+34612358902")
validPhone(612358902)
validPhone("+34239847298435")

#Validate URL:

def validURL(URLlink):
    regexURL = re.compile(
            r'^(?:http|ftp)s?://' # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
            r'localhost|' #localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    if re.fullmatch(regexURL, URLlink):
       print("Valid URL")
    else:
       print("Invalid URL")


validURL("http://www.saezMD.com")
validURL("example.com")
validURL("https://saezmd.vercel.app/")




