#  EJERCICIO:
#  Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
#  en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
#  - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
#    conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...

#  DIFICULTAD EXTRA (opcional):
#  Crea un programa que analice dos palabras diferentes y realice comprobaciones
#  para descubrir si son:
#  - Palíndromos
#  - Anagramas
#  - Isogramas

cadena = "Hola Mundo"
print("Cadena original:", cadena)

# Acceso a caracteres específicos
print("Primer carácter:", cadena[0])
print("Último carácter:", cadena[-1])

# Subcadenas
print("Subcadena (del 0 al 3 caracter sin incluir el 3 ):", cadena[0:3])
print("Subcadena (del 5 al ultimo caracter ):", cadena[5:])

# Longitud
print("Longitud de la cadena:", len(cadena))

# Concatenación
cadena2 = " Python"
cadena_concatenada = cadena + cadena2
print("Cadena concatenada:", cadena_concatenada)

# Repetición
cadena_repetida = cadena * 2
print("Cadena repetida:", cadena_repetida)

# Recorrido
for caracter in cadena:
    print(caracter, end=' ')
print("\nRecorrido completo de la cadena con un ciclo for:", cadena)

# Conversión a mayúsculas y minúsculas
print("Cadena en mayúsculas:", cadena.upper())
print("Cadena en minúsculas:", cadena.lower())
print("Cadena capitalizada:", cadena.capitalize())
print("Cadena con título:", cadena.title())

# Conversión a lista de caracteres
lista_caracteres = list(cadena)
print("Lista de caracteres, convirtiendo una cadena de caracteres a una lista:", lista_caracteres)

# Reemplazo
cadena_reemplazada = cadena.replace("Mundo", "Python")
print("Cadena reemplazada:", cadena_reemplazada)

# División
cadena_dividida = cadena.split(" ")
print("Cadena dividida con split :", cadena_dividida)
print(type(cadena_dividida))  # Verifica el tipo de dato

# Unión
cadena_unida = " ".join(cadena_dividida)
print("Cadena unida:", cadena_unida)
print(type(cadena_unida))  # Verifica el tipo de dato

# Interpolación (f-strings)
nombre = "Juan"
edad = 30
print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")

# Verificación
print("¿La cadena contiene 'Mundo'?", "Mundo" in cadena)
print("¿La cadena empieza con 'Hola'?", cadena.startswith("Hola"))


# un palíndromo es una palabra que se lee igual de izquierda a derecha que de derecha a izquierda
def es_palindromo(palabra):
    # Eliminar espacios y convertir a minúsculas para la comparación
    palabra = palabra.replace(" ", "").lower()
    return palabra == palabra[::-1]


def es_anagrama(palabra1, palabra2):  # un anagrama es una palabra formada por las letras de otra palabra
    palabra1 = palabra1.replace(" ", "").lower()  # remover espacios y convertir a minúsculas
    palabra2 = palabra2.replace(" ", "").lower()  # remover espacios y convertir a minúsculas
    return sorted(palabra1) == sorted(palabra2)  # comparar las letras ordenadas de ambas palabras


def es_isograma(palabra):  # un isograma es una palabra en la que no se repite ninguna letra
    palabra = palabra.replace(" ", "").lower()
    return len(palabra) == len(set(palabra))


def main():
    palabra = "Anita lava la tina"
    print(f"¿'{palabra}' es un palíndromo?", es_palindromo(palabra))

    palabra1 = "amor"
    palabra2 = "roma"
    print(f"¿'{palabra1}' y '{palabra2}' son anagramas?", es_anagrama(palabra1, palabra2))

    palabra3 = "murcielago"
    print(f"¿'{palabra3}' es un isograma?", es_isograma(palabra3))


if __name__ == "__main__":
    main()


for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
