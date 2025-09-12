import re

texto = "Hoy es 24 de abril de 2024. El número de teléfono es 555-123-4567 y el precio es $99.99."

numeros_encontrados = re.findall(r"\d+", texto)

print("Números encontrados:", numeros_encontrados)


# Ejercicio extra


def validar_email(email):
    # Expresión regular para validar email
    patron_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(patron_email, email) is not None


def validar_telefono(telefono):
    # Expresión regular para validar número de teléfono
    patron_telefono = r"^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$"
    return re.match(patron_telefono, telefono) is not None


def validar_url(url):
    # Expresión regular para validar URL
    patron_url = r"^(http|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?$"
    return re.match(patron_url, url) is not None


# Ejemplos
email = "ejemplo@dominio.com"
telefono = "(555) 123-4567"
url = "https://www.ejemplo.com"

print("Email válido:", validar_email(email))
print("Teléfono válido:", validar_telefono(telefono))
print("URL válida:", validar_url(url))
