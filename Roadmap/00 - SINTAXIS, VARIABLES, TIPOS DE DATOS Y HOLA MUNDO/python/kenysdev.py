# ╔══════════════════════════════════════╗
# ║ Autor: Kenys Alvarado                ║
# ║ GitHub: https://github.com/Kenysdev  ║
# ║ 2024 - Python                        ║
# ╚══════════════════════════════════════╝

# 1. Sitio web oficial:
# *********************
# https://www.python.org/

# 2. Sintaxis para comentarios:
# *****************************
suma = 1 + 2 # comentario inline

# Comentarios Block
suma = 1 + 2
'''
comentario para
múltiples líneas.
'''
# TODO Para explicar función de código aún no escrito
# TODO actualizaciones o cambios en tu código.

"""Docstring en una linea"""

"""
Comentarios Docstring múltiples líneas.
primera declaración en una definición 
de módulo, función, clase o método. 
https://peps.python.org/pep-0257/
"""

# 3. Variable y constante.
# ************************
variable_str = "ejemplo str"

# python no tiene contantes pero 
# por convenio comunitario se usa:
CONSTANTS_STR = "https://peps.python.org/pep-0008/#constants"

# 4. Variables para datos primitivos.
# ***********************************
int_entero = 12
float_decimal = 12.21
str_texto = "Hola, Python"
bool_booleano = True # o False
# a + b numeros reales y j unidad imaginaria  
complex_complejo = 12 + 21j 

# imprimir tipo de variable:
print(type(int_entero)) # Salida: <class 'int'>

# 5. Imprime: hola, lenguaje:
# **************************
print("¡Hola, Python!")
