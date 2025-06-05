"""
Expresiones reguales
"""

#Expresiones regulares (regex) son patrones de búsqueda que se usan para validar, buscar o reemplazar texto en cadenas. Se componen de caracteres normales y especiales.

# Importa el módulo 're' que permite trabajar con expresiones regulares en Python
import re

# Define una función llamada 'find_number' que recibe un parámetro 'text' de tipo string y devuelve una lista 
def find_number(text: str) -> list:
    # Utiliza 're.findall' para buscar todas las secuencias de uno o más dígitos (\d+)
    # en el texto recibido. Retorna una lista con todas las coincidencias encontradas.
    return re.findall(r"\d+", text) #tambien se puede usar r"[0-9]+, text

# Llama a la función 'find_number' con un texto de ejemplo y muestra en pantalla la lista de números encontrados
print(find_number("Este es el ejercicio 16 publicado 15/04/24"))

""" * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:


 * - Validar un email."""


# Retorna True si 'email' coincide con el patrón:
    # - ^ 	Indica el inicio de la cadena.
    # - Empieza con letras/números/_.+-
    # - Sigue un @
    # - Dominio con letras/números/_
    # - Un punto
    # - Y termina con al menos dos letras
    # - $ Indica el final de la cadena.
def validate_email(email: str)-> bool:
    return bool(re.match(r"^[\w+.-]+@[\w]+\.[a-zA-Z]{2,}$", email))


print(validate_email("Complex-_+.@gmail.com"))


""" - Validar un número de teléfono."""


def validate_phone(phone: str)-> bool:
      return bool(re.match(r"^(\+1[\s-])?[\d\s-]{3,12}$", phone))

# ^\+1 → debe empezar con +1
#"?" Hace que el elemento anterior sea opcional: Es decir, puede aparecer una vez o no aparecer.
# [\s-]? → espacio o guion opcional después de +1
# [\d\s-]{3,12} → luego entre 3 y 12 caracteres que sean dígitos, espacios o guiones
# $ → final de cadena


print(validate_phone("+1 809 019 1092"))





"""- Validar una url."""

def validate_url(url: str)-> bool:
    # Usa re.match para verificar si la URL cumple con el patrón.
    # Si coincide, devuelve True, si no, False.
    return bool(re.match(r"^http[s]?://(www.)?[\w]+\.[a-zA-Z]{2,}$", url))

# ^	Inicio de la cadena
# http[s]?://	Debe empezar con http:// o https:// (s es opcional por [s]?)
# (www.)?	Opcionalmente permite www. justo después (el ? lo hace opcional)
# [\w]+	Uno o más caracteres alfanuméricos o guion bajo (\w equivale a [a-zA-Z0-9_])
# \.	Un punto literal .
# [a-zA-Z]{2,}	Dos o más letras (la extensión, como com, net, io)
# $	Fin de la cadena



print(validate_url("http://Complex01_.com"))


#pagina web para evaluar codigo de expresiones reguales: https://regex101.com/
