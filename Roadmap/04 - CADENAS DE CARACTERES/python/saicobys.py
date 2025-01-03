# Cadenas de ejemplo
texto1 = "Hola, mundo!"
texto2 = "Python es genial"

# Acceso a caracteres y subcadenas
print(texto1[0])      # H (Primer carácter)
print(texto1[7:12])   # mundo (Subcadena desde el índice 7 hasta el 11)
print(texto1[-1])     # ! (Último carácter)

# Longitud
print(len(texto1))    # 12 (Número de caracteres en la cadena)

# Concatenación (unir cadenas)
texto_combinado = texto1 + " " + texto2
print(texto_combinado)  # Hola, mundo! Python es genial

# Repetición
texto_repetido = texto1 * 3
print(texto_repetido)  # Hola, mundo!Hola, mundo!Hola, mundo!

# Recorrido (iterar sobre caracteres)
for caracter in texto2:
    print(caracter)    # Imprime cada carácter en una línea nueva

# Conversión a mayúsculas y minúsculas
print(texto1.upper())  # HOLA, MUNDO!
print(texto2.lower())  # python es genial

# Reemplazo
nuevo_texto = texto2.replace("genial", "fantástico")
print(nuevo_texto)     # Python es fantástico

# División (split)
palabras = texto2.split(" ")
print(palabras)        # ['Python', 'es', 'genial']

# Unión (join)
nueva_cadena = "-".join(palabras)
print(nueva_cadena)    # Python-es-genial

# Verificación (contiene, comienza, termina)
print("mundo" in texto1)          # True
print(texto1.startswith("Hola"))  # True
print(texto2.endswith("!"))       # False

# Interpolación (formateo de cadenas)
nombre = "Carlos"
edad = 30
mensaje = f"Hola, me llamo {nombre} y tengo {edad} años."
print(mensaje)        # Hola, me llamo Carlos y tengo 30 años.

# Analizador de Palabras

def es_palindromo(palabra):
    """Verifica si una palabra es un palíndromo (se lee igual de derecha a izquierda)."""
    palabra = palabra.lower().replace(" ", "")  # Normalización
    return palabra == palabra[::-1]  # Compara la palabra con su reverso

def es_anagrama(palabra1, palabra2):
    """Verifica si dos palabras son anagramas (tienen las mismas letras en diferente orden)."""
    palabra1 = palabra1.lower().replace(" ", "")
    palabra2 = palabra2.lower().replace(" ", "")
    return sorted(palabra1) == sorted(palabra2)  # Compara las palabras ordenadas

def es_isograma(palabra):
    """Verifica si una palabra es un isograma (no tiene letras repetidas)."""
    palabra = palabra.lower().replace(" ", "")
    return len(palabra) == len(set(palabra))  # Compara la longitud original con la del conjunto (sin duplicados)

# Ejemplo de uso
palabra1 = "Anita lava la tina"
palabra2 = "Amor a Roma"
palabra3 = "Python"

print(f"'{palabra1}' es palíndromo: {es_palindromo(palabra1)}")
print(f"'{palabra1}' y '{palabra2}' son anagramas: {es_anagrama(palabra1, palabra2)}")
print(f"'{palabra3}' es isograma: {es_isograma(palabra3)}")
