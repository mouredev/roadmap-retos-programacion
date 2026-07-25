# Día 4: Cadenas de Caracteres

# --- String base para los ejemplos ---
cadena = "Hola, Mundo! Este es mi string de prueba."
print(f"String original: '{cadena}'\n" + "="*40)

# --- Acceso y Subcadenas (Slicing) ---
print("\n## 1. Acceso y Subcadenas ##")
# Acceso a un carácter específico (índice 0 es el primero)
primer_caracter = cadena[0]
print(f"El primer carácter (índice 0) es: '{primer_caracter}'")

# Acceso al último carácter
ultimo_caracter = cadena[-1]
print(f"El último carácter (índice -1) es: '{ultimo_caracter}'")

# Acceso a una subcadena (slicing)
subcadena = cadena[6:11] # Desde el índice 6 hasta el 10
print(f"Subcadena de [6:11]: '{subcadena}'")

# --- Longitud ---
print("\n## 2. Longitud de la Cadena ##")
longitud = len(cadena)
print(f"La longitud de la cadena es: {longitud} caracteres")

# --- Concatenación ---
print("\n## 3. Concatenación ##")
saludo = "Mi nombre es Willian"
frase_completa = cadena + " " + saludo
print(f"Frase concatenada: '{frase_completa}'")

# --- Repetición ---
print("\n## 4. Repetición ##")
risa = "Ja"
risa_repetida = risa * 5
print(f"String repetido: '{risa_repetida}'")

# --- Recorrido (Iteración) ---
print("\n## 5. Recorrido de la Cadena ##")
print("Imprimiendo cada carácter de la palabra 'Mundo':")
for caracter in "Mundo":
    print(f"- {caracter}")

# --- Conversión a Mayúsculas y Minúsculas ---
print("\n## 6. Mayúsculas y Minúsculas ##")
print(f"En mayúsculas: '{cadena.upper()}'")
print(f"En minúsculas: '{cadena.lower()}'")
print(f"Con primera letra en mayúscula: '{cadena.capitalize()}'")
print(f"Con cada palabra capitalizada: '{cadena.title()}'")

# --- Reemplazo ---
print("\n## 7. Reemplazo de Caracteres ##")
cadena_reemplazada = cadena.replace("Mundo", "Python")
print(f"Reemplazando 'Mundo' por 'Python': '{cadena_reemplazada}'")

# --- División (Split) ---
print("\n## 8. División en una Lista ##")
palabras = cadena.split() # Por defecto, divide por los espacios
print(f"La cadena dividida en palabras: {palabras}")

# --- Unión (Join) ---
print("\n## 9. Unión de Elementos ##")
lista_palabras = ["Python", "es", "genial"]
frase_unida = " ".join(lista_palabras)
print(f"Uniendo una lista con espacios: '{frase_unida}'")

# --- Interpolación (f-strings) ---
print("\n## 10. Interpolación ##")
nombre = "Willian"
edad = 51
print(f"Interpolación: Me llamo {nombre} y tengo {edad} años.")

# --- Verificación (startswith, endswith, is...) ---
print("\n## 11. Verificación de Contenido ##")
print(f"¿La cadena empieza con 'Hola'?: {cadena.startswith('Hola')}")
print(f"¿La cadena termina con 'prueba.'?: {cadena.endswith('prueba.')}")
print(f"¿La cadena '123' contiene solo dígitos?: {'123'.isdigit()}")
print(f"¿La cadena 'abc' contiene solo letras?: {'abc'.isalpha()}")

# Reto #04 - Analizador de Palabras
print("ANALIZADOR DE PALABRAS")
print("=" * 40)

# Entrada de datos
palabra1 = input(" Ingresa la primera palabra: ")
palabra2 = input("Ingresa la segunda palabra: ")

# Limpiar palabras (minúsculas y sin espacios)
def limpiar_palabra(palabra):
    return palabra.lower().replace(" ", "").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")

p1 = limpiar_palabra(palabra1)
p2 = limpiar_palabra(palabra2)

# 1. Verificar Palíndromos
def es_palindromo(palabra):
    return palabra == palabra[::-1]

pal1_palindromo = es_palindromo(p1)
pal2_palindromo = es_palindromo(p2)

# 2. Verificar Anagramas
def son_anagramas(pal1, pal2):
    return sorted(pal1) == sorted(pal2)

anagramas = son_anagramas(p1, p2)

# 3. Verificar Isogramas
def es_isograma(palabra):
    return len(palabra) == len(set(palabra))

pal1_isograma = es_isograma(p1)
pal2_isograma = es_isograma(p2)

# Mostrar resultados
print("\nRESULTADOS DEL ANÁLISIS:")
print("=" * 40)

print(f"Palabra 1: '{palabra1}' → '{p1}'")
print(f"Palabra 2: '{palabra2}' → '{p2}'")
print("-" * 40)

print(f" ¿'{palabra1}' es palíndromo? {' Sí' if pal1_palindromo else '❌ No'}")
print(f" ¿'{palabra2}' es palíndromo? {' Sí' if pal2_palindromo else '❌ No'}")
print(f" ¿Son anagramas? {' Sí' if anagramas else '❌ No'}")
print(f" ¿'{palabra1}' es isograma? {' Sí' if pal1_isograma else '❌ No'}")
print(f" ¿'{palabra2}' es isograma? {' Sí' if pal2_isograma else '❌ No'}")