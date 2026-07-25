# 04 - Cadenas de caracteres 

# Cadenas de caracteres y operaciones

cadena = "Hola Mundo"
print("Mi cadena: " + cadena)
print("Primer caracter: " + cadena[0] + " - Ultimo caracter: " + cadena[-1])
print("Subcadena: " + cadena[0:4])
print("Longitud de la cadena: " + str(len(cadena)))
print("Concatenación: " + cadena + " desde Python")
print("Repetición: " + (cadena + " ")* 3)
print("Recorrido:")
for caracter in cadena:
    print(caracter)
print("Mayúsculas: " + cadena.upper())
print("Minúsculas: " + cadena.lower())
print("Reemplazo: " + cadena.replace("Mundo", "Universo"))
print("División: " + str(cadena.split(" ")))
print("Unión: " + " ".join(["Hola", "Mundo"]))
cadena1 = "casa!"
print("Interpolación: " + f"{cadena} desde {cadena1}")
print("Verificación: " + str(cadena.startswith("Hola")))
print("Verificación: " + str(cadena.endswith("Mundo")))
print("Busqueda: " + str(cadena.find("Mundo")))
print("Comparación: " + str(cadena == "Hola Mundo"))


# EXTRA: Análisis de palabras

# Palíndromo: Palabra o frase que se lee igual de izquierda a derecha que de derecha a izquierda.
def es_palindromo(palabra):
    return palabra == palabra[::-1]

# Anagrama: Palabra o frase que resulta de la transposición de letras de otra palabra o frase.
def es_anagrama(palabra1, palabra2):
    return sorted(palabra1) == sorted(palabra2)

# Isograma: Palabra que no tiene letras repetidas.
def es_isograma(palabra):
    return len(palabra) == len(set(palabra))

print("\n-----Análisis de palabras-----")
print("Nota: las comparaciones dan prioridad a la primera palabra.")
palabra1 = input("Ingrese una palabra: ")
palabra2 = input("Ingrese otra palabra: ")
print(f"¿Es palíndromo?: {es_palindromo(palabra1)}")
print(f"¿Es anagrama?: {es_anagrama(palabra1, palabra2)}")
print(f"¿Es isograma?: {es_isograma(palabra1)}")