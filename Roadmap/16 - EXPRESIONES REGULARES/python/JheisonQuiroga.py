import re

"""
/*
 * EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
"""

txt = """
Cristiano Ronaldo dos Santos Aveiro (Funchal, Madeira, 5 de febrero de 1985)
es un futbolista portugués. Juega como delantero y su equipo actual es el 
Al-Nassr F. C. de la Liga Profesional Saudí. Es internacional absoluto con la 
selección de Portugal, de la cual es capitán, máximo goleador histórico y 
jugador con más presencias con 217 partidos, logro alcanzado en las eliminatorias 
para la Eurocopa 2024, reconocido por el Libro Guinness de los récords.
"""

regex_pattern = r"\d+"

matches = re.findall(regex_pattern, txt)
print(matches)

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
 */
"""

# Validando un e-mail

def email_validation(email):

    reg_pattern = r"^[a-zA-Z0-9]+([.+-_][a-zA-Z0-9]+)*@([a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}$"

    # Verificamos si toda la cadena coincide con el patron

    return True if re.fullmatch(reg_pattern, email) else False


emails = [
    "usuario@example.com",
    "user.name@sub.domain.org",
    "correo@dominio.co",
    "usuario123@dominio.com",
    "mal.correo@com",        # Inválido (extensión incorrecta)
    "sin-arroba.com",        # Inválido (falta @)
    "@sin_nombre.com"        # Inválido (falta nombre)
]

for email in emails:
    print(f"{email}: {"Valido" if email_validation(email) else "Invalido"}")

# Validando un número de telefono en Colombia.
# Formato 300-000-0000, debe tener 10 digitos

def phone_validation(phone):

    reg_pattern = r'^([3][0-9]{2}-?[0-9]{3}-?[0-9]{4})'
    return True if re.fullmatch(reg_pattern, phone) else False


print(phone_validation("320-326-7902")) # True
print(phone_validation("320-326-790235")) # False
print(phone_validation("3203267902")) # True
print(phone_validation("2203267902")) # False



# Validando una URL
def url_validate(url:str) -> bool:
    
    pattern = (
        r'^(https?://)' # Protocolo
        r'([a-zA-Z0-9-]+\.)*' # Subdominios
        r'[a-zA-Z]{2,}' # TLD ej. (.com , .org)
        r'(:[0-9]{1,5})?' # Puerto (opcional) ej. :8000
        r'(/.*)?$'
    )
    # reg_pattern = r'^(https?://)?(www\.)?([a-zA-Z0-9.-]+)\.[a-zA-Z]{2,6}(/.*)?$'

    return True if re.fullmatch(pattern, url) else False


urls = [
    "https://www.google.com",   # Válido
    "http://example.org",       # Válido
    "https://sub.dominio.co/path?query=123",  # Válido
    "ftp://invalid.com",        # Inválido (no es HTTP o HTTPS)
    "www.nodominio",            # Inválido (falta extensión)
    "http://localhost:8000",    # Valido
]


print("\nValidación de URLs:")
for url in urls:
    print(f"{url}: {'Válido' if url_validate(url) else 'Inválido'}")