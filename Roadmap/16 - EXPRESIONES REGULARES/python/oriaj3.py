"""
16 - EXPRESIONES REGULARES

Autor de la solución: Oriaj3	

Teoría:	
Las expresiones regulares son patrones utilizados para encontrar una determinada
secuencia de caracteres dentro de una cadena de texto. Son una herramienta
poderosa y flexible que permite buscar y extraer información de manera eficiente
y precisa.

En Python, las expresiones regulares se pueden utilizar a través del módulo
re, que proporciona una serie de funciones y métodos para trabajar con ellas.
Para utilizar expresiones regulares en Python, se debe importar el módulo re y
luego compilar el patrón de expresión regular utilizando la función compile().

Por ejemplo, la siguiente expresión regular encuentra y extrae todos los números
de una cadena de texto:

import re

# Compila el patrón de expresión regular
pattern = re.compile(r'\d+')

# Cadena de texto de ejemplo
text = 'Hoy es 25 de diciembre de 2021'

# Busca y extrae todos los números de la cadena de texto
numbers = pattern.findall(text)

# Imprime los números encontrados
print(numbers)

En este caso, la expresión regular \d+ busca uno o más dígitos en la cadena de
texto. Al compilar el patrón de expresión regular y utilizar el método findall(),
se obtienen todos los números de la cadena de texto.

Re usa una sintaxis especial para definir patrones de expresión regular. Algunos
de los caracteres especiales más comunes son:

\d: Coincide con cualquier dígito.
\w: Coincide con cualquier carácter alfanumérico.
\s: Coincide con cualquier carácter de espacio en blanco.
.: Coincide con cualquier carácter excepto un salto de línea.
*: Coincide con cero o más repeticiones del carácter anterior.
+: Coincide con una o más repeticiones del carácter anterior.
?: Coincide con cero o una repetición del carácter anterior.
[]: Coincide con cualquier carácter dentro de los corchetes.
(): Agrupa una serie de caracteres para aplicar operadores como * o +.
|: Coincide con cualquiera de las opciones separadas por el operador.
^: Coincide con el inicio de una cadena de texto.
$: Coincide con el final de una cadena de texto.
"""

"""
/*
 * EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
"""

import re

texto = 'Hoy es 25 de diciembre de 2021, tengo 30 años y mi número de teléfono es 1234567890, vivo en la calle 1234 y mi código postal es 54321.'

# Compila el patrón de expresión regular
pattern = re.compile(r'\d+') # \d+ busca uno o más dígitos en la cadena de texto r indica que es una cadena cruda (raw string)

# Busca y extrae todos los números de la cadena de texto
numeros = pattern.findall(texto)

# Imprime los números encontrados
print(numeros)

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
 */
"""
"""
Patrón explicado: 
^: Inicio de la cadena.
[a-zA-Z0-9._%+-]+: Uno o más caracteres alfanuméricos, puntos, guiones bajos, porcentajes, signos más o menos (parte local del correo).
@: El símbolo arroba.
[a-zA-Z0-9.-]+: Uno o más caracteres alfanuméricos, puntos o guiones (nombre de dominio).
\.: Un punto literal.
[a-zA-Z]{2,}$: Dos o más letras (dominio de nivel superior, como .com, .es, .org).
$: Fin de la cadena.
"""

def valida_email(email: str):
    patron = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    if re.match(patron, email) is not None:
        return True
    else: 
        return False

print(valida_email("pepe@gmail.com"))

"""
Patrón explicado:
^: Inicio de la cadena.
\+\d\d\s\d{9}: Un signo más seguido de dos dígitos, un espacio en blanco y nueve dígitos.
"""

def valida_telefono(num: str):
    patron = re.compile(r'^\+\d\d\s\d{9}$')
    if re.match(patron, num):
        return True
    else:
        return False

print(valida_telefono("+34 644112233"))

"""
Patrón explicado en comentarios en el código
"""

def valida_url(url: str):
    patron_url = re.compile(
    r'^(https?://)?'  # Protocolo (http://, https://) opcional
    r'(www\.)?'       # www. opcional
    r'[a-zA-Z0-9.-]+'  # Nombre de dominio (letras, números, guiones, puntos)
    r'\.[a-zA-Z]{2,}'  # Dominio de nivel superior (.com, .es, etc.)
    r'(:\d+)?'        # Puerto opcional (por ejemplo, :8080)
    r'(/.*)?$'        # Path opcional (cualquier cosa después de la barra /)
    )

    if re.match(patron_url, url):
        return True
    else:
        return False
    
print(valida_url("https://www.google.com"))
