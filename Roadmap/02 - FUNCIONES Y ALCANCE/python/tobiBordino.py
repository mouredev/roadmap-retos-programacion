# 02 FUNCIONES Y ALCANCE

'''
- Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
'''

# Funciones simples sin parámetros ni retorno
def funcionSinParametrosNiRetorno():
    print("Función sin parámetros ni retorno")

# Funciones con parámetros
def funcionConParametros(parametro1, parametro2):
    print(f"Función con parámetros: {parametro1} {parametro2}")

# Funciones con retorno
def funcionConRetorno():
    return "Función con retorno"

# Funciones con parámetros y retorno
def print_numbers(parametro1, parametro2="Mundo"):
    return f"Función con parámetros y retorno: {parametro1} {parametro2}"

# Llamada a funciones
funcionSinParametrosNiRetorno()
funcionConParametros("Hola", "mundo")
# La función con retorno se puede imprimir directamente
print(funcionConRetorno())
print(print_numbers("Hola", "mundo"))
print(print_numbers("Hola"))

# Comprobación de crear funciones dentro de funciones
def funcionExterna():
    def funcionInterna():
        print("Función interna")
    funcionInterna()

funcionExterna()

# Funciones propias de Python
print("--- Funciones propias del lenguaje PYTHON ---")
print(len("Hola mundo"))
print(type("Hola mundo"))
print("Hola mundo".upper())

# - Pon a prueba el concepto de variable LOCAL y GLOBAL.

# Variable global
variableGlobal = "Variable global"

def funcionConVariableGlobal():
    print(variableGlobal)

funcionConVariableGlobal()

# Variable local
def funcionConVariableLocal():
    variableLocal = "Variable local"
    print(variableLocal)

funcionConVariableLocal()

# Función con número variable de argumentos
def funcionConNumeroVariableDeArgumentos(*name):
    for i in name:
        print(f"Hola {i}")

funcionConNumeroVariableDeArgumentos("Python", "C#")

# Número variable de argumentos con palabra clave
def funcionConNumeroVariableDeArgumentosYPalabraClave(**name):
    for key, value in name.items():
        print(f"Hola, {value} ({key})!")

funcionConNumeroVariableDeArgumentosYPalabraClave(name="Python" , language="C#")

# DIFICULTAD EXTRA
'''
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
'''

def print_numbers(parametro1, parametro2):
    contador = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(parametro1 + parametro2)
        elif i % 3 == 0:
            print(parametro1)
        elif i % 5 == 0:
            print(parametro2)
        else:
            print(i)
            contador += 1
    return contador

print(print_numbers("Texto1", "Texto2"))