import re

def reg_expr(cadena):
    patron = r'-?\d+\.?\d*'
    numeros = re.findall(patron, cadena)

    print("Números encontrados:")
    for numero in numeros:
        print(numero)

    print("\n")

texto = "Este es un texto con números como 123, 45.6, -7 y 1000."
print("Vamos a analizar el siguiente texto:")
print("'" + texto + "'\n")
reg_expr(texto)

texto = "123Erase una vez un número 1234567890 y otro 0987654321. Y para terminar456"
print("Vamos a analizar el siguiente texto:")
print("'" + texto + "'\n")
reg_expr(texto)

def email_validation(email):
    patron = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'
    if re.match(patron, email):
        print("El email", email, "es válido.")
    else:
        print("El email", email, "no es válido.")

def phone_validation(phone):
    patron = r'^\+?(\d{2,3})?[-. ]?\d{9}$'
    if re.match(patron, phone):
        print("El teléfono", phone, "es válido.")
    else:
        print("El teléfono", phone, "no es válido.")

def url_validation(url):
    patron = r'^(http|https):\/\/[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}'
    if re.match(patron, url):
        print("La URL", url, "es válida.")
    else:
        print("La URL", url, "no es válida.")

email_validation("correo@correo.com")
email_validation("correo@correo")

phone_validation("+34 123456789")
phone_validation("123456789")

url_validation("http://www.google.com")
url_validation("www.google.com")
