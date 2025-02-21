# Regex

"""
Es una herramienta para trabjar con texto
Se trabaja a traves del modulo 'Re'
    Permite buscar, coincidir y manipular cadenas de texto
Se usan para:
    * Validar formatos (correos electronicos o numeros de telefono)
    * Extraer info especifica de un texto (fechas o palabras clave)
    * Reemplazar partes de un texto
"""

# Importamos el modulo re
import re

"""
Metodos clave:
    * re.search() Busca la primera coincidencia del patron del texto
    * re.match() Verifica si el patron coincide al inicio del texto
    * re.findall() Devuelve todas las coincidencias en una lista
    * re.sub() Reemplaza coincidencias por otro texto
"""

# Ejercicio:
texto = 'Mi numero es 1234 y el tuyo es 5678'
patron = r'\d+' # '\d+' uno o mas digitos
numeros = re.findall(patron, texto)
print(numeros)

"""
Caracteres comunes es regex
    * .: cualquier caracter (excepto salto de linea)
    * *: 0 o mas repeticiones
    * +: 1 o mas repeticiones
    * ?: 0 o una repeticion
    * \d: Un dígito (0-9).
    * \w: Un carácter alfanumérico (letras, números, guión bajo).
    * \s: Espacio en blanco.
    * []: Define un conjunto de caracteres (ejemplo: [a-z] para letras minúsculas).
"""

# Validar un email
email = 'usuario@dominio10.com'
patron = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z]+\.[a-zA-Z]+$"
if re.match(patron, email):
    print('Email valido')
else:
    print('Email invalido')

# Validar telefono
telefono = '+99(534)547-5561'
patron = r'\+[0-9]+\([0-9]+\)[0-9]+\-[0-9]'
if re.match(patron, telefono):
    print('Numero valido')
else:
    print('Numero invalido')

# Validar una url
url = 'http://sample.info/?insect=fireman&porter=attraction#cueva'
patron = r'^http[s]?://(www\.)?[\w-]+\.[a-zA-Z]{2,}$'
if re.match(patron, url):
    print('Url valida.')
else:
    print('Url invalida.')