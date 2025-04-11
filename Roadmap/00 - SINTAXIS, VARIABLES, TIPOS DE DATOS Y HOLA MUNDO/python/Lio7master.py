'''
  EJERCICIO 00 - SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO:
  - Crea un comentario en el código y coloca la URL del sitio web oficial del
    lenguaje de programación que has seleccionado.
  - Representa las diferentes sintaxis que existen de crear comentarios
    en el lenguaje (en una línea, varias...).
  - Crea una variable (y una constante si el lenguaje lo soporta).
  - Crea variables representando todos los tipos de datos primitivos
    del lenguaje (cadenas de texto, enteros, booleanos...).
  - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
'''
# Enlace a la página oficial de Python: https://www.python.org/

# Este es un comentario de una línea -> La documentacion lo indica como el medio oficial en 2.1.3. Comments
# Cita de la documentacion oficial de Python:
# "A comment starts with a hash character (#) that is not part of a string literal, and ends at the end of the physical line.
#  A comment signifies the end of the logical line unless the implicit line joining rules are invoked. 
#  Comments are ignored by the syntax."


#Los  string no son comentarios, pero se pueden usar como tal mientras no esten asignados a una variable se consideran comentarios.
# Uso de strings como comentarios multilínea 
'''
   En python se puede usar comillas simples o dobles para crear cadenas de texto.
   En este caso se han utilizado comillas simples para crear un comentario multilínea.
   Python no tiene un símbolo específico para comentarios multilínea, pero ignora las cadenas de texto
   que no están asignadas a ninguna variable.
'''

"""
   En python se puede usar comillas simples o dobles para crear cadenas de texto.
   En este caso se han utilizado comillas dobles para crear un comentario multilínea.
   Python no tiene un símbolo específico para comentarios multilínea, pero ignora las cadenas de texto
   que no están asignadas a ninguna variable.
"""
# Uso de strings como comentarios de línea 
" En python se puede usar comillas simples o dobles para crear cadenas de texto."

'En python se puede usar comillas simples o dobles para crear cadenas de texto.'

#Creación de variables
# En python se recomienda usar snake_case para nombrar variables, aunque no es obligatorio.
    #Los nombres de las varibles se diferencian incluso por el uso de mayúsculas y minúsculas.
   

mi_variable_1 = 2025 #Tipo int
mi_variable_2 = 3.14 #Tipo float
mi_variable_3 = True #Tipo bool

mi_variable = "Mexico" #tipo str
Mi_variable = 'Cadena de caracteres, entre comillas simples' #Tipo str
Mi_Variable = "Cadena de caracteres, entre comillas dobles" #Tipo str
    #Por convención, para nombrar constantes en Python, se escribe en mayúsculas.
MI_CONSTANTE = "hola mundo" #Tipo str

print(MI_CONSTANTE) #Imprime el texto en la terminal