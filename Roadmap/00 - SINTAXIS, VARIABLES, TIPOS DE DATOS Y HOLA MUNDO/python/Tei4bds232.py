"""
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
"""
#Comentario en una linea con url de python: https://www.python.org
"""
Comentario de
varias 
lineas
en
python
https://www.python.org    
"""
#Comentario
#Varias
#Lineas
#Pero poco profesional

# - Crea una variable (y una constante si el lenguaje lo soporta).
var = "hola python" #Esto es una variable
NUMERO_PY = 3.14159 #Esto es una constante con un valor inmutable

# - Crea variables representando todos los tipos de datos primitivos
var_1 = int(23)#Esto es un dato de tipo entero
print(f"Hola!! soy un dato de tipo entero:{var_1}")
var_2 = str("Hola string")#Esto es un dato de tipo string o cadena de caracteres
print(f"Hola!! soy un dato de tipo str o string o cadena de texto:{var_2}")
var_3 = float(2.24)#Esto es un dato de tipo float y representa numeros decimales
print(f"Hola!! soy un dato de tipo decimal o numero flotante:{var_3}")
var_3 = bool(True)#Esto es un tipo de dato bool
var_4 = bool(False)#Esto tambien es un tipo de dato bool
print(f"Hola!! soy un dato de tipo booleano solamente tengo dos resultados o:{var_3} o {var_4}")

#- Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
VAR_5 = "python"
print(f"Hola!!{VAR_5}")