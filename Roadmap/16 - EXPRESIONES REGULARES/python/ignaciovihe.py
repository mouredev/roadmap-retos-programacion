"""
 * EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
"""

import re

text = "Hola, mi nonbre es Pedro y tengo 25 años. Mi direccción es calle falsa 12-3. Mi número favorito es el 7. mi Perro tien3 12 años"
pattern = r"\d+"
print(re.findall(pattern, text))


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
"""

def validate_data():
    email_pattern = r"^[\w.+-]+@[\w&-]+\.[a-zA-z]{2,}$"
    telefon_pattern = r"^\+?[\d\s]{3,}$"
    url_pattern = r"^http[s]?://(?:www\.)?[\w-]+\.[a-zA-Z]{2,}$" # Usa grupo no capturador

    while True:
        data = input("Introduce un email, un telefono o una url para validar, o 'salir' para terminar: ")
        if data == "salir":
            break
        if re.match(email_pattern, data):
            print("Email valido")
            continue
        elif re.match(telefon_pattern, data):
            print("Telefono válido")
            continue
        elif re.match(url_pattern, data):
            print("Url válido")
            continue
        else:
            print("Formato invalido")
            continue

validate_data()






"""Conceptos explorados adicionales"""

print("-----------------re.search()----------------------")
texto = "Hola, me gustan los gatos y los perros."
patron = r"g[aeiou]tos"  # Encuentra "gatos" pero no "g1tos"

resultado = re.search(patron, texto)

if resultado:
    print(f"Encontrado: {resultado.group()}")  # Devuelve la palabra encontrada
else:
    print("No encontrado.")


print("-----------------re.findall()----------------------")
texto = "gato perro Python calle paraguas"
patron = r"\b[Pp]\w+"

resultado = re.findall(patron, texto)

if resultado:
    print("¡Coincidencia encontrada!")
    print(resultado)
else:
    print("No se encontró la palabra.")


print("-----------------re.sub()----------------------")
texto = "Mi número es 123-456-7890"
patron = r"\d"  # Cualquier número

nuevo_texto = re.sub(patron, "X", texto)

print(nuevo_texto)


print("-----------------Grupos y Capturas----------------------")
texto = "Teléfono: (123) 456-7890"
patron = r"\((\d{3})\) (\d{3})-(\d{4})" #Si quiero aplicar un grupo no capturador --> (?:)

resultado = re.search(patron, texto)

if resultado:
    print("Código de área:", resultado.group(1))
    print("Primera parte:", resultado.group(2))
    print("Segunda parte:", resultado.group(3))
    print(resultado.groups())
else:
    print("NO se encontro el patrón")


print("-----------------re.match()----------------------")
email = "correo@example.com"
patron = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"

if re.match(patron, email):
    print("Correo válido")
else:
    print("Correo inválido")


print("-----------------groupdict()----------------------")
texto = "Mi email es juan.perez@example.com"
patron = r"(?P<usuario>[a-zA-Z0-9_.+-]+)@(?P<dominio>[a-zA-Z0-9-]+\.[a-zA-Z]{2,})"

resultado = re.search(patron, texto)

if resultado:
    print(resultado.groupdict())