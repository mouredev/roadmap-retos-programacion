"""/*
* EJERCICIO:
* Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
* en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
* - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
*   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
*   interpolación, verificación...
*/"""

cadena1 = "Hola"
cadena2 = "Python"

# Concatenación
print(cadena1 + ", " + cadena2 + "!")

# Repetición
print(cadena1 * 3)

# Acceso a caracteres específicos (indexación)
print(cadena1[0] + cadena1[1] + cadena1[2] + cadena1[3])

# longitud
print(f"Longitud de cadena2: {len(cadena2)}")

# subcadenas (slicing)
print(cadena1[1:4])
print(cadena2[2:6])
print(cadena2[2:])

# busqueda
print("a" in cadena1)
print("y" in cadena2)

print(f"Busqueda al principio: {cadena1.startswith('Ho')}")
print(f"Busqueda al final: {cadena2.endswith('on')}")

cadena3 = "Cristian Floyd @cristianfloyd"
print(f"Posicion de floyd: {cadena3.find('floyd')}")

# recorrido (conteo de ocurrencias)
print(f"Número de ocurrencias de 'c': {cadena3.lower().count('c')}")


# reemplazo
cadena1_reemplazada = cadena1.replace("o", "a")
print(cadena1_reemplazada)

# division
print(cadena1.split("l"))

# conversión a mayúsculas y minúsculas
print(cadena1.lower())
print(cadena1.upper())
print("cristian floyd".title())
print("cristian floyd".capitalize())

# eliminación de espacios al principio y al final
cadena_con_espacios = "  cristian floyd  "
print(cadena_con_espacios.strip())

# trasnformación a lista de caracteres
lista_caracteres = list(cadena3)
print(f"De cadena a lista: {lista_caracteres}")

# transformacion de lista a cadena
print(f"De lista a cadena str: {''.join(lista_caracteres)}")

cadena4 = "123456"
print(f"Conversion de cadena a entero: {int(cadena4) + 10}")
print(f"Conversion de cadena a float: {float(cadena4 + '.5')}")

print(f"Es alfanumerico?: {cadena4.isalnum()}")
print(f"Es alfabetico?: {cadena4.isalpha()}")
print(f"Es digito?: {cadena4.isdigit()}")
print(f"Es minuscula?: {cadena4.islower()}")
print(f"Es mayuscula?: {cadena4.isupper()}")
print(f"Es numerico?: {cadena4.isnumeric()}")
print(f"Es espacio?: {'   '.isspace()}")
print(f"Es titulo?: {'Cristian Floyd'.istitle()}")
print(f"Es ascii?: {cadena4.isascii()}")


"""/*
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */ """


def es_palindromo(palabra: str) -> bool:
    """Verifica si una palabra es un palíndromo.
    def: palabra o frase que se lee igual de izquierda a derecha que de derecha a izquierda
    """
    palabra = palabra.replace(" ", "").lower()
    return palabra == palabra[::-1]


def es_anagrama(palabra1: str, palabra2: str) -> bool:
    """Verifica si dos palabras son anagramas.

    def: palabra o frase que se crea reorganizando las letras de otra palabra o frase, 
         de manera que todas las letras originales se usan exactamente una vez
    """
    return sorted(palabra1.replace(" ", "").lower()) == sorted(
        palabra2.replace(" ", "").lower()
    )


def es_isograma(palabra: str) -> bool:
    """Verifica si una palabra es un isograma.
    def: palabra que no tiene letras repetidas
    """
    palabra = palabra.replace(" ", "").lower()
    return len(set(palabra)) == len(palabra)


def check(palabra1: str, palabra2: str):
    print(f"{palabra1} es un palíndromo") if es_palindromo(palabra1) else None
    print(f"{palabra2} es un palíndromo") if es_palindromo(palabra2) else None

    print(f"{palabra1} es un anagrama de {palabra2}") if es_anagrama(
        palabra1, palabra2
    ) else None

    print(f"{palabra1} es un isograma") if es_isograma(palabra1) else None

    print(f"{palabra2} es un isograma") if es_isograma(palabra2) else None


# check("radar", "pythonpythonpythonpython")
check("amor", "roma")
