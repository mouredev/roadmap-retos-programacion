# ============================================
# OPERACIONES CON CADENAS DE CARACTERES
# ============================================

print("====== OPERACIONES CON CADENAS EN PYTHON ======")

texto = "Python es poderoso"

# Acceso a caracteres específicos
print("Primer carácter:", texto[0])
print("Último carácter:", texto[-1])

# Subcadenas (slicing)
print("Subcadena [0:6]:", texto[0:6])
print("Subcadena desde el 7:", texto[7:])
print("Cada segundo carácter:", texto[::2])

# Longitud
print("Longitud:", len(texto))

# Concatenación
saludo = "Hola " + "mundo"
print("Concatenación:", saludo)

# Repetición
repetido = "ja" * 3
print("Repetición:", repetido)

# Recorrido
print("Recorrido por caracteres:")
for letra in "Hola":
    print(letra, end=" ")
print()

# Mayúsculas y minúsculas
print("Mayúsculas:", texto.upper())
print("Minúsculas:", texto.lower())
print("Capitalizado:", texto.capitalize())
print("Título:", texto.title())
print("Swapcase:", texto.swapcase())

# Reemplazo
print("Reemplazo:", texto.replace("poderoso", "genial"))

# División y unión
palabras = texto.split()
print("Split (división en lista):", palabras)
unido = "-".join(palabras)
print("Join (lista a cadena):", unido)

# Interpolación
lenguaje = "Python"
print(f"Interpolación con f-string: {lenguaje} es increíble")
print("Interpolación con format: {} es genial".format(lenguaje))

# Verificación
print("¿Empieza con 'Python'?", texto.startswith("Python"))
print("¿Termina con 'poderoso'?", texto.endswith("poderoso"))
print("¿Contiene 'es'?", "es" in texto)
print("¿Es alfanumérico?", "abc123".isalnum())
print("¿Es alfabético?", "abc".isalpha())
print("¿Está en minúsculas?", "python".islower())
print("¿Está en mayúsculas?", "PYTHON".isupper())
print("¿Es espacio?", "   ".isspace())
print("¿Es título?", "Hola Mundo".istitle())
print()


# ============================================
# ANALIZADOR DE PALABRAS (DIFICULTAD EXTRA)
# ============================================

def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    return palabra == palabra[::-1]

def es_anagrama(p1, p2):
    return sorted(p1.lower().replace(" ", "")) == sorted(p2.lower().replace(" ", ""))

def es_isograma(palabra):
    letras = palabra.lower().replace(" ", "")
    return len(set(letras)) == len(letras)

print("====== ANALIZADOR DE PALABRAS ======")
palabra1 = input("Introduce la primera palabra: ").strip()
palabra2 = input("Introduce la segunda palabra: ").strip()

# Palíndromos
print(f"¿'{palabra1}' es palíndromo?", es_palindromo(palabra1))
print(f"¿'{palabra2}' es palíndromo?", es_palindromo(palabra2))

# Anagramas
print(f"¿'{palabra1}' y '{palabra2}' son anagramas?", es_anagrama(palabra1, palabra2))

# Isogramas
print(f"¿'{palabra1}' es isograma?", es_isograma(palabra1))
print(f"¿'{palabra2}' es isograma?", es_isograma(palabra2))
