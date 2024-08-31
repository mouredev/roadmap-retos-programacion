# Sitio web Oficial: https://www.python.org/

## Comentarios ##

# En python tenemos 2 formas diferentes de comentar. 

# Inline (en línea).

'''
Y multilínea, este tenemos dos maneras de escribirlo.
Podemos hacer comentarios multilínea con 
comillas simples ('').
'''

"""
También podemos hacer comentarios multilínea 
con comillas dobles("").
"""

## Variables y Constantes ##

una_variable = "Retos de Programación"
'''
Python no soporta las constantes. No obstante, podemos trabajar con estas
escribiendo una variable en mayúsculas para indicar que esa variable debe
tratarse como una constante. 
'''
UNA_CONSTANTE = 2024

## Tipos de Datos ##

# int 
edad = 22
# float
salario = 1350.70
# complex 
complx = 1j + 2
# string
texto = "Roadmap 2024"
# bool
es_anio_nuevo = True
# diccionario
dicc = {"nombre":"Ram", "edad":22}
# lista
li = [1,34,55,9j,12]
# tupla
tu = (3,'ratón',2.3)
# conjunto (set)
con = {3,14,89,'Juan',True}
# conjunto inmutable
con_inm = frozenset([1,3,'Luis',1j,4.5])
# rango 
ran = range(5,12)
# binario
by = bytes(15)

## Impresión por Terminal ##

lenguaje = "Python"
print(f"¡Hola, {lenguaje}!")
