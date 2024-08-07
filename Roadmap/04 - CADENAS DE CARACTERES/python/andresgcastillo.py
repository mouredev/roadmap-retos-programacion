# Crear una cadena de caracteres
cadena = "Hola Mundo"

# Acceso a caracteres específicos
print(cadena[0])  # H

# Subcadenas
print(cadena[0:4])  # Hola

# Longitud
print(len(cadena))  # 10

# Concatenación
cadena2 = " Python"
print(cadena + cadena2)  # Hola Mundo Python

# Repetición
print(cadena * 2)  # Hola MundoHola Mundo

# Recorrido
for caracter in cadena:
    print(caracter)

# Conversión a mayúsculas
print(cadena.upper())  # HOLA MUNDO

# Conversión a minúsculas
print(cadena.lower())  # hola mundo

# Reemplazo
print(cadena.replace("Mundo", "Python"))  # Hola Python

# División
print(cadena.split(" "))  # ['Hola', 'Mundo']

# Unión
lista = ['Hola', 'Mundo']
print(" ".join(lista))  # Hola Mundo

# Interpolación
nombre = "Python"
print(f"Hola {nombre}")  # Hola Python

# Verificación
print("Mundo" in cadena)  # True

#Dificultad Extra

def es_palindromo(palabra):
    return palabra == palabra[::-1]

def es_anagrama(palabra1, palabra2):
    return sorted(palabra1) == sorted(palabra2)

def es_isograma(palabra):
    return len(palabra) == len(set(palabra))

# Prueba
palabra1 = "anagram"
palabra2 = "nagaram"

print(f"¿'{palabra1}' es un palíndromo? {es_palindromo(palabra1)}")
print(f"¿'{palabra1}' y '{palabra2}' son anagramas? {es_anagrama(palabra1, palabra2)}")
print(f"¿'{palabra1}' es un isograma? {es_isograma(palabra1)}")