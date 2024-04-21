#16 -- EXPRESIONES REGULARES

"""
/*
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
 */
"""
import re


def exprecion_regular_numeros(texto: str):
    numeros = re.findall(r'\d+', texto)

    print("Números encontrados:")
    for numero in numeros:
        print(numero)

texto = """hola mundo esto es una prueba del reto de programacion numero 16 , esto significa que
que han vido otros retos como el 10 , 5 o un reto numero 0"""

exprecion_regular_numeros(texto)

### Extra
email_exprecion = r'^[\w\.-]+@[\w\.-]+\.\w+$'
numero_exprecion = r'^\d{4}\s\d{4}$'

url_exprecion = r'^(https?://)?([a-z0-9]*\.)?[a-z0-9-]+\.[a-z]{2,3}$'  # Patrón de URL modificado
def email_numero_url(elemento: str):
    if re.match(email_exprecion, elemento):
        print(f"El texto '{elemento}' es un correo electrónico válido.")
    elif re.match(numero_exprecion, elemento):
        print(f"El texto '{elemento}' es un número de teléfono válido.")
    elif re.match(url_exprecion, elemento):
        print(f"El texto '{elemento}' es una URL válida.")
    else:
        print(f"El texto '{elemento}' no coincide con ningún patrón de correo electrónico, número de teléfono o URL.")

numero_valido = "8888 9999"
numero_invalido = "8888999"

email_valido = "jlopezsanty1@gmail.com"
email_invalido = "13lopez@com"

url_valida = "https://www.holamundo.day"
url_invalida = "www.hola_mundo.dev"

email_numero_url(numero_valido)
email_numero_url(email_valido)
email_numero_url(url_valida)

print("\n---------------------------------\n")

email_numero_url(numero_invalido)
email_numero_url(email_invalido)
email_numero_url(url_invalida)
