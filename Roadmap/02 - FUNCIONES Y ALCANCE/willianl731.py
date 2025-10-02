# ---funciones basicas de python---

# a. sin parametros y sin retorno: esta funcion saluda sin personalizar   
def saludar():
    print("¡Hola! Bienvenido al reto #2.")

# b. con parametros y sin retorno: esta funcion saluda a una persona por su nombre
nombre = "Giovanni" # variable global
def saludar_persona(nombre):
    print(f"¡Hola, {nombre}! Bienvenido al reto #2.")
saludar_persona(nombre)

# c. con parametros y con retorno:  """Esta función recibe dos números y devuelve su suma."""
# crear la funcion
def sumar_numeros(a, b):
    return a + b

# Define los números en variables
num1 = 5
num2 = 10

# Llama a la función usando las variables
resultado_final = sumar_numeros(num1, num2)

# Imprime el mensaje usando las mismas variables
print(f"El resultado de sumar {num1} + {num2} es: {resultado_final}")

# --- PRUEBA CAMBIANDO LOS NÚMEROS ---
# Ahora, si cambiamos los números, el mensaje también se actualiza.
num1 = 100
num2 = 50
resultado_final = sumar_numeros(num1, num2)
print(f"El resultado de sumar {num1} + {num2} es: {resultado_final}")

# 2. Funcion dentro de otra funcion (anidada): esta funcion multiplica por 2 y suma 3      
#crear la funcion
def funcion_externa(x):
    def funcion_interna(y):
        return y * 2
    return funcion_interna(x) + 3

# Elige un número para probar y guárdalo en una variable
numero_de_prueba = 10

# Llama a la función externa y guarda el resultado que devuelve
resultado_final = funcion_externa(numero_de_prueba)

# Imprime el resultado de forma descriptiva
print(f"Al llamar a funcion_externa con {numero_de_prueba}, el resultado es: {resultado_final}") 

# 3. funciones ya creadas en python
# a. funcion print(): muestra mensajes en la consola
print("¡Hola, mundo!") 
# b. funcion len(): devuelve la longitud de una cadena o lista
longitud = len("Hola")
print(f"La longitud de 'Hola' es: {longitud} letras")
# c. funcion type(): devuelve el tipo de dato de una variable
tipo = type(42)
print(f"El tipo de dato de 42 es: {tipo}")  
# d. funcion input(): recibe datos del usuario (comentada para evitar interrupciones)
# nombre_usuario = input("Por favor, ingresa tu nombre: ")
# print(f"¡Hola, {nombre_usuario}!")
# e. funcion .upper(): convierte una cadena a mayúsculas
texto = "hola"
texto_mayusculas = texto.upper()
print(f"Texto en mayúsculas: {texto_mayusculas}")
# f. funcion .lower(): convierte una cadena a minúsculas
texto_minusculas = texto.upper().lower()
print(f"Texto en minúsculas: {texto_minusculas}")
# g. funcion .append(): añade un elemento al final de una lista
mi_lista = [1, 2, 3]
mi_lista.append(4)
print(f"Lista después de append: {mi_lista}")  
# h. funcion .remove(): elimina un elemento específico de una lista
mi_lista.remove(2)
print(f"Lista después de remove: {mi_lista}")
# i. funcion .sort(): ordena los elementos de una lista
mi_lista.sort()
print(f"Lista después de sort: {mi_lista}")
# j. funcion .reverse(): invierte el orden de los elementos en una lista
mi_lista.reverse()
print(f"Lista después de reverse: {mi_lista}")
# k. funcion .split(): divide una cadena en una lista según un separador
frase = "Hola mundo"
lista_palabras = frase.split()
print(f"Lista de palabras: {lista_palabras}")
# l. funcion .join(): une los elementos de una lista en una cadena con un separador
nueva_frase = " ".join(lista_palabras)
print(f"Nueva frase: {nueva_frase}")
# m. funcion range(): genera una secuencia de números
numeros = list(range(5))
print(f"Lista de números: {numeros}")
# n. funcion sum(): suma todos los elementos de una lista
suma_numeros = sum(numeros)
print(f"La suma de los números es: {suma_numeros}")
# o. funcion max(): devuelve el valor máximo de una lista
maximo = max(numeros)
print(f"El valor máximo de la lista es: {maximo}")

# 4. variables globales y locales
# Variable global
variable_global = "soy una variable global"

def funcion_con_variable_local():
    variable_local = "soy una variable local"
    print(variable_local)

funcion_con_variable_local()
print(variable_global)

# ejercicio extra:
"""
Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
"""
# crear la funcion
def juego_matematicas(numero, matematicas):
    """
    Juego para aprender múltiplos
    palabra_numeros: texto para múltiplos de 3 (ej: "Número")
    palabra_matematicas: texto para múltiplos de 5 (ej: "Matemáticas")
    """
    veces_texto = 0

    print(f"\n=== Juego de múltiplos ===")
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print(numero + matematicas)
        elif num % 3 == 0:
            print(numero)
        elif num % 5 == 0:
            print(matematicas)
        else:
            print(num)
            veces_texto += 1
    return veces_texto

# Usamos el juego
textos_usados = juego_matematicas("Número", "Matemáticas")
print(f"\nEl juego usó palabras {textos_usados} veces")