"""
EJERCICIO:
Utilizando tu lenguaje, explora el concepto de expresiones regulares,
creando una que sea capaz de encontrar y extraer todos los numeros de
un texto.

DIFICULTAD EXTRA (opcional):
Crea 3 expresiones regulares (a tu criterio) capaces de:
- Validar un email.
- Validar un número de teléfono.
- Validar una url.

by adra-dev
"""


"""
Expresiones regulares:

Una expresion regular es una cadena de caracteres especial que define
un patron de busqueda. Son una herramienta fundamental para manipular
conjuntos de datos en texto, como las listas de nombres de archivos, 
direcciones de correo electronico, modelos de productos, etc. 
Las expresiones regulares pueden ahorrarte mucho trabajo si sabes 
sacarle partido y Python ofrece potentes herramientas para su 
manipulacion.
"""

import re

regex1 = r'\d+'
regex2 = re.compile(r'\d+')

text  = """ En un lugar muy lejano, había un Rey al que todos consideraban muy sabio.

Gobernaba con gran justicia 99 aldeas. Las 9 eran vecinas y en perfecta armonía todas convivían.

El Rey se ocupaba de que todas las aldeas tuvieran agua, comida y una bonita escuela.

Las 9 aldeas estaban rodeadas por 999999 riachuelos. 

Y el Rey construyo 90123 molinos y 10 puentes para que todos pudieran cruzar de un lado a otro sin correr ningún riesgo."""

print(re.findall(regex2, text))


"""
Extra
"""

regex_email = re.compile('^[\w\-\.]+@([\w-]+\.)+[\w-]{2,}$')

regex_phone = re.compile('(?:([+]\d{1,4})[-.\s]?)?(?:[(](\d{1,3})[)][-.\s]?)?(\d{1,4})[-.\s]?(\d{1,4})[-.\s]?(\d{1,9})')

regex_url = re.compile('^(http://|https://|http://www\.|https://www\.|www\.)?(www\.(twanda))?(([\w\-]+)?\.?(twanda|))(\.ch|\.com)(:\d+)?/.+$')

