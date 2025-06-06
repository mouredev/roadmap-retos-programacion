# Sitio oficial de Python: https://www.python.org/

# Comentarios
# Esto es un comentario de una línea

"""
Este es un comentario
de varias líneas
"""
''' 
Esto tambien es un 
comentario de varias lineas
'''

# Variable normal
lenguaje = "Python"

# 📌 Constante por convención (pero no protegida)
PI = 3.14159

# 🧠 Tipos de datos primitivos
entero = 42                   # int
decimal = 3.14                # float
booleano = True               # bool
caracter = 'A'                # string de un solo carácter
cadena = "Hola mundo"         # str
lista = [1, 2, 3]             # list
tupla = (1, 2)                # tuple
diccionario = {"a": 1, "b": 2}# dict
nulo = None                   # NoneType

# Conversión de tipos (casting)
numero = "10"
suma = int(numero) + 5  # sin int() fallaría

# Control de flujo
if booleano:
    print("El valor booleano es verdadero")

# Función
def saludar(nombre):
    return f"Hola, {nombre}!"

# Imprimir resultados
print(saludar(lenguaje))
print(f"Valor de PI (constante): {PI}")
print(f"Suma convertida: {suma}")
print(f"Tipos: entero={type(entero)}, cadena={type(cadena)}, lista={type(lista)}")
