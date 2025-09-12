''' * EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
 */'''
import re

texto = "Este texto numero 546 es 1 ejemplo para poder extraer varios numeros como 67 o 230 con expresiones regulares"

patron_numeros = r'\d+'
numeros_encontrados = re.findall(patron_numeros, texto)
print("Números encontrados:", numeros_encontrados)




patron_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
patron_telefono = r'^(\+\d{1,3})?\s?(\d{3}|\(\d{3}\))[\s.-]?\d{3}[\s.-]?\d{4}$'
patron_url = r'^(https?://)?(www\.)?[\w-]+\.[a-z]{2,}(\/\S*)?$'

def validar(entrada, patron):
    return bool(re.match(patron, entrada))

email_valido = "pedrito@ejemplo.com"
email_invalido = "pedrito@.com"

telefono_valido = "122-655-7240"
telefono_invalido = "023-406-555" 

url_valida = "https://www.pedrito.com"
url_invalida = "pedrito.com"

print("Email válido:", validar(email_valido, patron_email))
print("Email inválido:", validar(email_invalido, patron_email))

print("Teléfono válido:", validar(telefono_valido, patron_telefono))
print("Teléfono inválido:", validar(telefono_invalido, patron_telefono))

print("URL válida:", validar(url_valida, patron_url))
print("URL inválida:", validar(url_invalida, patron_url))
