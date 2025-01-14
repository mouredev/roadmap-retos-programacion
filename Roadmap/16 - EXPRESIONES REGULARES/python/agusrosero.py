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

# EJERCICIO:
texto = 'Este es mi texto numero 123456'
busqueda = re.findall('[0-9]', texto)
print(busqueda)

# DIFICULTAD EXTRA:
validar_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
validar_telefono = '^\\+?[1-9][0-9]{7,14}$'
validar_url = '((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*'

print(re.fullmatch(validar_email, 'test@gmail.com'))
print(re.match(validar_telefono, '+543413333333'))
print(re.match(validar_url, 'https://www.google.com'))
