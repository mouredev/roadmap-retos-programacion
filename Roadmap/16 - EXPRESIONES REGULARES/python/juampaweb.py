# # #16 EXPRESIONES REGULARES
# > #### Dificultad: Media | Publicación: 15/04/24 | Corrección: 22/04/24

# ## Ejercicio

# ```
# /*
#  * EJERCICIO:
#  * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
#  * creando una que sea capaz de encontrar y extraer todos los números
#  * de un texto.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea 3 expresiones regulares (a tu criterio) capaces de:
#  * - Validar un email.
#  * - Validar un número de teléfono.
#  * - Validar una url.
#  */
# ```
# #### Tienes toda la información extendida sobre el roadmap de retos de programación en **[retosdeprogramacion.com/roadmap](https://retosdeprogramacion.com/roadmap)**.

# Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

# > Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**.


import re


def extract_number(texto):
    """Return a dictionary with the list of numbers and the string without numbers."""
    response = {}
    response['list_numbers'] = re.findall(r'\d+', texto)
    response['string_not_numbers'] = re.sub(r'\d+', '', texto)

    return response

def validate_email(email):
    """Return True if the email is valid, False otherwise."""
    patron = r'^[a-zA-Z0-9._+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'
    if re.match(patron, email):
        return True
    return False

def validate_phone(phone):
    """Return True if the phone is valid, False otherwise."""
    patron = r'^\+?(\d{2,3})?[-. ]?(\d[-. ]?){0,9}(\d)$'
    if re.match(patron, phone):
        return True
    return False

def validate_url(url):
    """Return True if the url is valid, False otherwise."""
    patron = r'^(http|https):\/\/[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}'
    if re.match(patron, url):
        return True
    return False


# Validación de extracción de números en un texto

list_strings = [
    "Este es un texto con números como 123, 45.6, -7 y 1000.",
    "123Erase una vez un número 1234567890 y otro 0987654321. Y para terminar456",
    "hola 1234 mundo 5678",
]
for string in list_strings:
    new_string = extract_number(string)
    print("Cadena original: ", string)
    print("Números encontrados: ", new_string['list_numbers'])
    print("Cadena sin números: ", new_string['string_not_numbers'])
    print("--------------------")
    print("\n")

print()
print()

### FIN de validación de extracción de números en un texto





# Validación de los emails
test_emails = [
    "jauns@pepe.com",
    "jauns@pepe",
    "pe@",
    "pepe@com",
    "juans+pepe@ally.com.ar",
    "__pepe@juan.com",
]


for email in test_emails:
    if validate_email(email):
        print("El email", email, "es válido.")
    else:
        print("El email", email, "no es válido.")

print()
print()
### FIN de validación de emails



# Validación de teléfonos
test_phones = [
    "+34 123456789",
    "123456789",
    "+34-123456789",
    "123-456-789",
    "+54 11.5140.8258"
]

for phone in test_phones:
    if validate_phone(phone):
        print("El teléfono", phone, "es válido.")
    else:
        print("El teléfono", phone, "no es válido.")

print()
print()
### FIN de validación de teléfonos


# Validación de URLs
test_urls = [
    "http://www.google.com",
    "www.google.com",
    "http://www.google",
    "http://www.google.com.ar",
    "http://www.google.com.ar.com",
    "http://www.google.com.ar.com.ar",
    "://www.google.com.ar.com.ar.com",
]

for url in test_urls:
    if validate_url(url):
        print("La URL", url, "es válida.")
    else:
        print("La URL", url, "no es válida.")

### FIN de validación de URLs






