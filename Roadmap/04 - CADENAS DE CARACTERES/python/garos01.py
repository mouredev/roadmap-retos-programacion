# Acceso a caracteres específicos
cadena = "Hola, mundo!"
print(cadena[0])

# Subcadenas
subcadena = cadena[1:5]
print(subcadena)

# Longitud de la cadena
longitud = len(cadena)
print(longitud)

# Concatenación
otra_cadena = "¡Cómo estás?"
concatenacion = cadena + " " + otra_cadena
print(concatenacion)

# Repetición
repetida = cadena * 3
print(repetida)

# Recorrido
for letra in cadena:
    print(letra)

# Conversión a mayúsculas y minúsculas
mayusculas = cadena.upper()
minusculas = cadena.lower()
print(mayusculas)
print(minusculas)

# Reemplazo
nueva_cadena = cadena.replace("mundo", "amigo")
print(nueva_cadena)

# División
palabras = cadena.split()
print(palabras)

# Unión
union = " ".join(palabras)
print(union)

# Interpolación
nombre = "Juan"
saludo_personalizado = f"Hola, {nombre}!"
print(saludo_personalizado)

# Verificación
contiene_hola = "Hola" in cadena
print(contiene_hola)


# Ejercicio extra


def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    return palabra == palabra[::-1]


def es_anagrama(palabra1, palabra2):
    palabra1 = palabra1.lower().replace(" ", "")
    palabra2 = palabra2.lower().replace(" ", "")
    return sorted(palabra1) == sorted(palabra2)


def es_isograma(palabra):
    palabra = palabra.lower().replace(" ", "")
    return len(palabra) == len(set(palabra))


def analizar_palabras(palabra1, palabra2):
    if es_palindromo(palabra1):
        print(f"{palabra1} es un palíndromo.")
    else:
        print(f"{palabra1} no es un palíndromo.")

    if es_anagrama(palabra1, palabra2):
        print(f"{palabra1} y {palabra2} son anagramas.")
    else:
        print(f"{palabra1} y {palabra2} no son anagramas.")

    if es_isograma(palabra1):
        print(f"{palabra1} es un isograma.")
    else:
        print(f"{palabra1} no es un isograma.")

    if es_palindromo(palabra2):
        print(f"{palabra2} es un palíndromo.")
    else:
        print(f"{palabra2} no es un palíndromo.")

    if es_anagrama(palabra1, palabra2):
        print(f"{palabra1} y {palabra2} son anagramas.")
    else:
        print(f"{palabra1} y {palabra2} no son anagramas.")

    if es_isograma(palabra2):
        print(f"{palabra2} es un isograma.")
    else:
        print(f"{palabra2} no es un isograma.")


palabra1 = input("Ingresa la primera palabra: ")
palabra2 = input("Ingresa la segunda palabra: ")

analizar_palabras(palabra1, palabra2)
