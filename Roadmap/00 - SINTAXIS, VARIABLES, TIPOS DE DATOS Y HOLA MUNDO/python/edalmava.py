# Un comentario comienza con un carácter de almohadilla (#) que no es parte de un literal de cadena,
# y termina al final de la línea física
# Comentario de una línea que va hasta el final

# Si un comentario en la primera o segunda línea del script de Python coincide con la expresión regular 
# coding[=:]\s*([-\w.]+), este comentario se procesa como una declaración de codificación; 
# -*- coding: <encoding-name> -*-
# Si no hay una declaración de codificación, la codificación por defecto es UTF-8

# Sitio oficial: https://www.python.org/

# Variables
variable = 'valor'         # Operador de asignación =

# Tipos Numéricos
enteros = -37              # Números enteros (int)
flotante = 10.5            # Números de punto flotante de doble precisión (float)
complejo = complex(1, 4.5) # complex(real=0, imag=0)

# Tipos Booleanos (bool) en Python son un subtipo del tipo entero
verdadero = True           # Se comporta como un 1
falso = False              # Se comporta como un 0

# Tipos Texto: son secuencias inmutables
saludo = "Hola"
lenguaje = 'Python'
# f-strings
mensaje = f"¡{saludo}, {lenguaje}!"

# Tipos Compuestos
# Tuplas: secuencias inmutables
tupla = (1, 2, 3, 4, 5)
# Listas: secuencias mutables
numeros = [1, 2, 3, 4, 5]

# Mapeos - Diccionarios - son mutables
# Estos representan conjuntos finitos de objetos indexados por conjuntos de índices arbitrarios. 
diccionario = {'hello': "hola", 'sun': "sol", 'hi': "hola"}

# Imprimir por consola
print(mensaje)
