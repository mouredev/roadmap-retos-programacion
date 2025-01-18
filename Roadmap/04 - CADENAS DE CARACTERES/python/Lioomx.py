''' 
Operaciones con cadenas de caracteres
'''

# Concatenación de cadenas

c1 = "Hola"
c2 = "Mundo"
resultado = c1 + " " + c2
print(resultado)

# Repetición de cadenas

cadena = "Python"
print(cadena * 3)

# Longitud de una cadena

cadena = "Curso de Python"
print(len(cadena))

# Acceso a caracteres

cadena = "Python"
print(cadena[0])
print(cadena[-1])

# Rebanado (slicing)

cadena = "Curso de Python"
print(cadena[0:8]) # Salida: Curso de
print(cadena[:8]) # Salida: Curso de (inicio implicito)
print(cadena[9:]) # Salida: Python (final implicito)
print(cadena[::-1]) # Salida: nohtyP ed osruC (Cadena invertida)

# Mayúsculas y minúsculas

cadena = "Python"
print(cadena.upper()) # PYTHON
print(cadena.lower()) # python

# Eliminar espacios

cadena = "  Hola Mundo  "
print(cadena.strip()) # Salida: Hola Mundo
print(cadena.lstrip()) # Salida: "Hola Mundo  "
print(cadena.rstrip()) # Salida: "  Hola Mundo"

# Buscar y reemplazar

cadena = "Aprender Python es divertido"
print(cadena.find("Python")) # Salida: 9 (posición)
print(cadena.replace("divertido", "facil")) # Salida: Aprender Python es facil

# Dividir y unir cadenas

cadena = "uno, dos, tres"
lista = cadena.split(", ")
print(lista) # Salida: ['uno', 'dos', 'tres']

nueva_cadena = " - ".join(lista)
print(nueva_cadena) # Salida: uno - dos - tres

# Verificar contenido

cadena = "Python3"
print(cadena.startswith("Py")) # Salida: True
print(cadena.endswith("3")) # Salida: True
print(cadena.isalpha()) # Salida: False (tiene números)
print("12345".isdigit()) # Salida: True


""" EXTRA """

def palindromo(palabra):
    palabra = palabra.lower().replace(" ", "") # Ignora mayúsculas y espacios
    return palabra == palabra[::-1]

def anagrama(palabra1, palabra2):
    palabra1 = palabra1.lower().replace(" ", "")
    palabra2 = palabra2.lower().replace(" ", "")
    return sorted(palabra1) == sorted(palabra2)

def isograma(palabra):
    palabra = palabra.lower().replace(" ", "")
    return len(palabra) == len(set(palabra))

print("Analizador de palabras")
palabra1 = input("Ingresa la primera palabra: ")
palabra2 = input("Ingresa la segunda palabra: ")

if palindromo(palabra1): 
    print(f"- '{palabra1}' es un palindromo.")
else: 
    print(f"- '{palabra1}' no es un palindromo.")

if anagrama(palabra1, palabra2):
    print(f"- '{palabra1}' y '{palabra2}' son anagramas.")
else:
    print(f"- '{palabra1}' y {palabra2}' no son anagramas.")

if isograma(palabra1):
    print(f"- '{palabra1}' es un isograma.")
else: 
    print(f"- '{palabra2}' no es un isograma.")

    