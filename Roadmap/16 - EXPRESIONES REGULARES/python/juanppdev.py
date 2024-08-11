"""
 * EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
"""

import re

def extraer_numeros(texto):
    # Definir la expresión regular para encontrar números
    patron = r'\d+'
    # Buscar todos los números en el texto
    numeros = re.findall(patron, texto)
    return numeros

# Ejemplo de uso
texto = "En 2023, la población de la ciudad era de 1,234,567 personas."
numeros = extraer_numeros(texto)
print(numeros)  # Salida: ['2023', '1', '234', '567']


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
"""

import re

def validar_email(email):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, email) is not None

# Ejemplo de uso
email = "ejemplo@dominio.com"
print(validar_email(email))  # Salida: True

def validar_telefono(telefono):
    patron = r'^\+?\d{1,3}?[-.\s]?\(?\d{1,4}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}$'
    return re.match(patron, telefono) is not None

# Ejemplo de uso
telefono = "+34 123-456-789"
print(validar_telefono(telefono))  # Salida: True

def validar_url(url):
    patron = r'^(https?|ftp)://[^\s/$.?#].[^\s]*$'
    return re.match(patron, url) is not None

# Ejemplo de uso
url = "https://www.ejemplo.com"
print(validar_url(url))  # Salida: True
