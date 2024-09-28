cadena = "Hola Mundo"
print("Acceso a caracteres específicos:")
print("Primer caracter:", cadena[0])
print("Último caracter:", cadena[-1])

print("\nSubcadenas:")
print("Subcadena desde el segundo caracter hasta el final:", cadena[1:])
print("Subcadena desde el segundo al quinto caracter:", cadena[1:6])

print("\nLongitud de la cadena:", len(cadena))

cadena2 = " de Python"
concatenada = cadena + cadena2
print("\nConcatenación:", concatenada)

print("\nRepetición:")
repetida = cadena * 3
print(repetida)

print("\nRecorrido:")
for letra in cadena:
    print(letra)

print("\nConversión a mayúsculas y minúsculas:")
print("Mayúsculas:", cadena.upper())
print("Minúsculas:", cadena.lower())

print("\nReemplazo:")
nueva_cadena = cadena.replace("Mundo", "Python")
print(nueva_cadena)

print("\nDivisión:")
dividida = cadena.split(" ")
print(dividida)

print("\nUnión:")
unida = "-".join(dividida)
print(unida)

print("\nInterpolación:")
nombre = "Alice"
edad = 30
print(f"Mi nombre es {nombre} y tengo {edad} años.")

print("\nVerificación:")
print("¿La cadena contiene solo letras?", cadena.isalpha())
print("¿La cadena contiene solo números?", cadena.isdigit())
print("¿La cadena contiene solo letras o números?", cadena.isalnum())
print("¿La cadena está en minúsculas?", cadena.islower())
print("¿La cadena está en mayúsculas?", cadena.isupper())
print("¿La cadena comienza con 'H'?", cadena.startswith("H"))
print("¿La cadena termina con 'o'?", cadena.endswith("o"))


# EXTRA
def es_palindromo(palabra):
    return palabra == palabra[::-1]


def es_anagrama(palabra1, palabra2):
    return sorted(palabra1.lower()) == sorted(palabra2.lower())


def es_isograma(palabra):
    return len(set(palabra.lower())) == len(palabra)


def analizar_palabras(palabra1, palabra2):
    if es_palindromo(palabra1):
        print(f"{palabra1} es un palíndromo.")
    else:
        print(f"{palabra1} no es un palíndromo.")

    if es_palindromo(palabra2):
        print(f"{palabra2} es un palíndromo.")
    else:
        print(f"{palabra2} no es un palíndromo.")

    if es_anagrama(palabra1, palabra2):
        print(f"{palabra1} y {palabra2} son anagramas.")
    else:
        print(f"{palabra1} y {palabra2} no son anagramas.")

    if es_isograma(palabra1):
        print(f"{palabra1} es un isograma.")
    else:
        print(f"{palabra1} no es un isograma.")

    if es_isograma(palabra2):
        print(f"{palabra2} es un isograma.")
    else:
        print(f"{palabra2} no es un isograma.")


palabra1 = "oso"
palabra2 = "soso"
analizar_palabras(palabra1, palabra2)
