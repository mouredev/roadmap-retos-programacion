import re

# Function	Description
# findall -	Returns a list containing all matches
# search -	Returns a Match object if there is a match anywhere in the string
# split -	Returns a list where the string has been split at each match
# sub - Replaces one or many matches with a string

cadena = "Esto es un texto de ejemplo con el número 12345 y otro número 54321"
resultado = re.findall(r"\d+", cadena) # \d+ busca uno o más dígitos 
print(resultado)
resultado = re.findall(r"\d{3}", cadena) # \d{3} busca exactamente 3 dígitos
print(resultado)
resultado = re.search(r"texto", cadena) # search() busca la primera ocurrencia de la cadena "texto" y devuelve un objeto Match
print(resultado)
resultado = re.split(r"\d+", cadena) # split() divide la cadena en una lista donde se encuentran los números
print(resultado)
resultado = re.sub(r"\d+", "XXXX", cadena) # sub() reemplaza los números por la cadena "XXXX"
print(resultado)

"""
DIFICULTAD EXTRA (opcional):
Crea 3 expresiones regulares (a tu criterio) capaces de:
- Validar un email.
- Validar un número de teléfono.
- Validar una url.
"""
def validar_email(email):
    return bool(re.match(r"^[\w.+-]+@[\w]+\.[a-zA-Z]+$", email))

def validar_telefono(phone):
    return bool(re.match(r"^\+?[\d\s]{3,}$", phone))

def validar_url(url):
    return bool(re.match(r"^(http[s]?://)?(www.)?[\w]+\.[\w]{2,}[/]?$", url))

print(validar_email("marcos@gmail.com"))
print(validar_email("marcos@gmail.com"))
print(validar_email("marcos@gmail.com"))
print(validar_telefono("632562345"))
print(validar_telefono("+34632562345"))
print(validar_telefono("+34 632 56 23 45"))
print(validar_url("http://www.marcos.com"))
print(validar_url("https://www.marcos.com"))
print(validar_url("http://www.marcos.com/"))
print(validar_url("www.marcos.com"))
print(validar_url("www.marcos.com/"))
print(validar_url("marcos.com"))
print(validar_url("m4rc0s.com"))
