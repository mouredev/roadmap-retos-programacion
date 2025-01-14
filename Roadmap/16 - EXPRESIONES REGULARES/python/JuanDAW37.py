"""* EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url."""
import re # Librería para expresiones regulares

regex = r"[0-9]+" # Valdría también usando \d+

texto_con_numeros = 'Hoy es miércoles 04/09/2024'

def encontrar_numeros(texto_con_numeros:str):
    return re.findall(regex, texto_con_numeros)

print(encontrar_numeros(texto_con_numeros))

#EXTRA
#Validar un email
regex_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z]"
#Validar un número de teléfono
regex_telefono = r"\d{3}.\d{3}.\d{3}"
#Validar una url
regex_url = r"^https?://[a-zA-Z0-9.-]+\.[a-zA]"

email = 'pepe@gmail.com'
telefono = '627.998.325'
url = 'https://urlfalsa.com'

def valida_email():
    return re.match(regex_email, email) is not None

def valida_telefono():
    return re.match(regex_telefono, telefono) is not None

def valida_url():
    return re.match(regex_url, url) is not None

print(valida_email())
print(valida_telefono())
print(valida_url())