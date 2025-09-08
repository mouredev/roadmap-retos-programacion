# Sitio oficial de python: https://www.python.org/
#hay 2 formas principales de crear comentarios en python:
# 1. Comentarios de una sola línea: Se utilizan el símbolo # al inicio de la línea.Se usan para explicar una línea específica de código o para desactivar código temporalmente.
#Para explicar el propósito de una variable.
#Para describir qué hace una función breve.
#Para "desactivar" una línea de código sin borrarla (debugging).
# # Ejemplo: Esto es un comentario de una línea

print("Hola mundo")  # Este comentario explica esta línea en específico
# La línea de abajo está "comentada" y no se ejecutará
# print("Esto no se imprimirá")

# 2. Comentarios de varias líneas o docstrings: Se encierran entre comillas triples (''' o """). Se usan principalmente para documentar módulos, clases, funciones o métodos.
#ejemplo: Documentar una función o clase.
def mi_funcion():
    """
    Esta es una docstring que explica la función.
    Puede tener múltiples líneas y se usa para documentar.
    """
    return True

'''
Esto también es una docstring (pero no es la forma convencional para comentar).
Se usa más para documentación que para comentarios temporales.
'''
#variables: (puede cambiar), minusculas_con_guiones_bajos
edad = 25
nombre = "Ana"
precio_producto = 19.99
esta_activo = True

# "Constantes" : (por convención, no se deberían cambiar),MAYUSCULAS_CON_GUIONES_BAJOS
PI = 3.1415926535
IVA = 0.21
URL_BASE = "https://mi-api.com"
MAXIMO_INTENTOS = 3

# Las usamos en cálculos
radio = 5
area_circulo = PI * radio ** 2

# 1. CADENA DE TEXTO (string - str)
# Secuencia de caracteres: entre comillas simples o dobles
nombre = "Ana García"
mensaje = 'Hola, ¿cómo estás?'

# 2. ENTERO (integer - int)
# Número sin parte decimal
edad = 25
cantidad_productos = 10

# 3. FLOTANTE (float)
# Número con parte decimal
precio = 19.99
pi = 3.141592

# 4. BOOLEANO (bool)
# Solo puede ser True (Verdadero) o False (Falso)
es_mayor_de_edad = True
tiene_descuento = False

# 5. COMPLEJO (complex)
# Número con parte real e imaginaria (se usa en matemáticas avanzadas)
numero_complejo = 3 + 4j
impedancia = 5 + 2j

# 6. NONE TYPE (NoneType)
# Representa la ausencia de valor
resultado = None
dato_faltante = None

print("¡Hola , Python!")

