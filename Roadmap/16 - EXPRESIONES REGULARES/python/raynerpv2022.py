# /*
#  * EJERCICIO:
#  * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
#  * creando una que sea capaz de encontrar y extraer todos los números
#  * de un texto.
#  *
import re

pattern = r'\d+'
text = """Utilizando tu lenguaje, explora el concepto de expres67676iones regulares,
#  * creando una que sea capaz de encontrar y extraer todos los 333números
#  * de un texto.DIFICULTAD334 EXTRA (opcional):
#  * Crea 3 expresiones regulares (a tu criterio) ca343434paces de:
#  * - Validar un email.
#  * - Validar565  un número de teléfono.
#  * - Validar una url."""
result = re.search(pattern,text)
print(result.group())
result = re.findall(pattern,text)
print(result)




#  * DIFICULTAD EXTRA (opcional):
#  * Crea 3 expresiones regulares (a tu criterio) capaces de:
#  * - Validar un email.
#  * - Validar un número de teléfono.
#  * - Validar una url.
#  */

def check_email(email):
    
     p = r"^[\w.]+@[a-zA-Z0-9.-]+\.+[a-zA-Z]{2,}$"
       
     result = re.fullmatch(p,email)
     if result:
        return email
     else:
         return f"{email} : "+"".join("No valido")

    

def emails():
    emails = [
    "user@example.com",
    "firstname.lastname@example.co.uk",
    "user+name@example.com",
    "user_name@example.org",
    "user.name123@example.info",
    "user123@example.org",
    "user.name+label@example.com",
    "username@subdomain.example.com",
    "user@example.travel",
    "user@example.name",
    "user@.com",
    "@example.com",
    "user@com",
    "user@exam_ple.com",
    "user@ex-ample..com",
    "user@.example.com",
    "user@example.c",
    "user@-example.com",
    "user@example..com",
    "user@exa_mple.com"
    ]

    for e in emails:
        print(check_email(e))

def check_phone(number):
    ps = r"^(\+34\s)?[\d]{3}\s[\d]{3}\s[\d]{3}$"
    result = re.fullmatch(ps,number)
    if result:
        return result.group()
    else:
        return f"{number} : "+"".join("No valida")

     

def telephon_NUmber():
    telefonos = [
    '+34 612 345 678',   # Válido
    '612 345 678',       # Válido
    '912 345 678',       # Válido
    '(912) 345 678',     # Válido
    '612345678',         # Válido
    '+34 (612) 345 678', # Válido
    '612 34 56',         # No válido (menos dígitos)
    '612-345-678',       # No válido (caracteres no permitidos)
    '123 456 789',       # No válido (no comienza con 6, 7, o 9)
    '9123456789',        # No válido (demasiados dígitos)
    '(612)345678',       # No válido (espacio mal ubicado)
    '612 345678'         # No válido (espacio mal ubicado)
]
    
    for n in telefonos:
        print(check_phone(n))

def check_url(url):
     
    ps = r"^https?://[\w.]+\.[a-zA-Z]{2,}$"
    result = re.match(ps,url)
    if result:
        return result.group()
    else:
        return f"{url} : "+"".join("No valida")

    
def urls():

    urls = [
        "http://www.example.com",
        "https://subdomain.example.org",
        "http://example.co.uk",
        "http://example.com2",
        "http://www.example.c",
        "https://www.example.edu",
        "http://example",
        "ftp://example.com",
        "https://example.com/path",
        "http://123.456.789.0"
    ]

    for l in urls:

        print(check_url(l))
urls()
print()
emails()
print()
telephon_NUmber()


