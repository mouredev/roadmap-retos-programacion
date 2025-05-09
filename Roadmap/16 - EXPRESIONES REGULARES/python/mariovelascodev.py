import re

text = "El ejercicio 16 de expresiones regulares ha sido resulto el 05/03/2025"

#Expresión regular que busca números
regular_expression = "\d+"

#Encontrar y mostrar todos los números de una cadena
print(re.findall(regular_expression, text))


#EXTRA
#Validar email
email_validate = "^[a-zA-Z]+.?[a-zA-Z0-9]+.?[a-zA-Z0-9]+\@[a-zA-Z]+\.[a-zA-Z]+"
valid_email = re.match(email_validate, "correo2@correo.es")

if valid_email is not None:
    print("Email correcto")
else:
    print("El email no es valido")

#Validar número de teléfono
phone_validate = "\+?\d{3,15}$"

valid_phone = re.match(phone_validate, "+34123456789")

if valid_phone is not None:
    print("Número de teléfono correcto")
else:
    print("El número de teléfono no es valido")

#Validar una url
url_validate = "[w]{0,3}\.?\w{3,}\.{1}[a-z]{2,4}$"

valid_url = re.match(url_validate, "google.com")

if valid_url is not None:
    print("La url es correcta")
else:
    print("La url no es valida")