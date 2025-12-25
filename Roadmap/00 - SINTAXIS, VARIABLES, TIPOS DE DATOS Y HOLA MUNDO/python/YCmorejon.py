# Visita la documentación oficial en: https://www.python.org

# --------------------------------------------------
# COMENTARIOS EN PYTHON
# --------------------------------------------------
print("\n--- COMENTARIOS EN PYTHON ---")

# Esto es un comentario de una línea (usando #)

"""
Este es un comentario multilínea
usando comillas dobles triples
Puede abarcar múltiples líneas
"""

'''
Este también es un comentario multilínea
usando comillas simples triples
Igualmente válido en Python
'''

# --------------------------------------------------
# VARIABLES Y CONSTANTES
# --------------------------------------------------
print("\n--- VARIABLES Y CONSTANTES ---")

# Creando una variable (nombre en minúsculas)
variable = "Dato"
print(f"Variable normal: {variable}")

# Creando una constante (por convención se usa MAYÚSCULAS)
CONSTANTE = "Valor que no debería cambiar"
print(f"Constante (por convención): {CONSTANTE}")

# Nota: En Python no existen constantes inmutables realmente,
# pero por convención usamos MAYÚSCULAS para indicar que no deberían modificarse

# --------------------------------------------------
# TIPOS DE DATOS BÁSICOS
# --------------------------------------------------
print("\n--- TIPOS DE DATOS BÁSICOS ---")

# Cadena de texto (str)
texto = "Hola Mundo"  # Usando comillas dobles
print(f"String (str): {texto} - Tipo: {type(texto)}")

# Número entero (int)
entero = 42
print(f"Entero (int): {entero} - Tipo: {type(entero)}")

# Número decimal (float)
decimal = 3.1416
print(f"Decimal (float): {decimal} - Tipo: {type(decimal)}")

# Valores booleanos (bool)
verdadero = True
falso = False
print(f"Booleanos (bool): {verdadero} y {falso} - Tipos: {type(verdadero)} y {type(falso)}")

# --------------------------------------------------
# IMPRESIÓN EN CONSOLA
# --------------------------------------------------
print("\n--- IMPRESIÓN EN CONSOLA ---")

# Usando f-strings (formato moderno, Python 3.6+)
nombre_lenguaje = "Python"
print(f"Hola {nombre_lenguaje}!")

# Formas alternativas de imprimir
print("Hola", nombre_lenguaje)  # Múltiples argumentos
print("Hola {}".format(nombre_lenguaje))  # Método format