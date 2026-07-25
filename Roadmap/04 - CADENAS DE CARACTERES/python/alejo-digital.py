# 04 CADENA DE CARACTERES

"""
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
"""

# Operaciones con cadenas de caracteres en Python

my_string = "Hola, Mundo!"
print("Cadena original:", my_string)
# Acceso a caracteres específicos
print("Primer carácter:", my_string[0])  # H
print("Último carácter:", my_string[-1])  # !

# Subcadenas
sub_string = my_string[0:4]  # Hola
print("Subcadena:", sub_string)

# Longitud
length = len(my_string)
print("Longitud de la cadena:", length)  # 13

# Concatenación
another_string = " soy Python."
concatenated_string = my_string + another_string
print("Cadena concatenada:", concatenated_string)  # Hola, Mundo! soy Python

# Repetición
repeated_string = my_string * 2
print("Cadena repetida:", repeated_string)  # Hola, Mundo!Hola, Mundo

# Recorrido
def recorrido(a_string):
    contador_v = 0
    contador_c = 0
    for char in a_string:
        if char in ("a", "e", "i", "o", "u"):
            contador_v += 1
            print(f"vocal: {char}")
        elif char.isalpha():
            print(f"consonante: {char}")
            contador_c += 1
        else:
            print(f"{char} no es una letra")
    print(f"Total de vocales: {contador_v}")
    print(f"Total de consonantes: {contador_c}")

recorrido(concatenated_string)

# Conversión a mayúsculas y minúsculas

upper_string = my_string.upper()
print("Cadena en mayúsculas:", upper_string)  # HOLA, MUNDO
lower_string = upper_string.lower()
print("Cadena en minúsculas:", lower_string)  # hola, mundo!

# Reemplazo
replaced_string = my_string.replace("Mundo", "Python")
print("Cadena con reemplazo:", replaced_string)  # Hola, Python!

# División
split_string = my_string.split(", ")
print("Cadena dividida:", split_string)  # ['Hola', 'Mundo!']

# Unión
joined_string = " - ".join(split_string)
print("Cadena unida:", joined_string)  # Hola - Mundo!

# Interpolación
name = "Python"
interpolated_string = f"Hola, {name}!"
print("Cadena interpolada:", interpolated_string)  # Hola, Python!

# Verificación
is_alpha = my_string.isalpha()  # False, porque contiene espacios y puntuación
print("¿La cadena es alfabética?", is_alpha)
is_digit = my_string.isdigit()  # False, porque no es numérica
print("¿La cadena es numérica?", is_digit)
is_lower = my_string.islower()  # False, porque contiene mayúsculas
print("¿La cadena está en minúsculas?", is_lower)
is_upper = my_string.isupper()  # False, porque contiene minúsculas
print("¿La cadena está en mayúsculas?", is_upper)


# DIFICULTAD EXTRA: Análisis de palabras

def es_palindromo(palabra):
    palabra = palabra.replace(" ", "").lower()
    return palabra == palabra[::-1]

def son_anagramas(palabra1, palabra2):
    palabra1 = palabra1.replace(" ", "").lower()
    palabra2 = palabra2.replace(" ", "").lower()
    return sorted(palabra1) == sorted(palabra2)

def es_isograma(palabra):
    palabra = palabra.replace(" ", "").lower()
    return len(palabra) == len(set(palabra))

def analizar_palabras(palabra1, palabra2):
    print(f"Análisis de las palabras: '{palabra1}' y '{palabra2}'")
    
    if es_palindromo(palabra1):
        print(f"'{palabra1}' es un palíndromo.")
    else:
        print(f"'{palabra1}' no es un palíndromo.")
    
    if es_palindromo(palabra2):
        print(f"'{palabra2}' es un palíndromo.")
    else:
        print(f"'{palabra2}' no es un palíndromo.")
    
    if son_anagramas(palabra1, palabra2):
        print(f"'{palabra1}' y '{palabra2}' son anagramas.")
    else:
        print(f"'{palabra1}' y '{palabra2}' no son anagramas.")
    
    if es_isograma(palabra1):
        print(f"'{palabra1}' es un isograma.")
    else:
        print(f"'{palabra1}' no es un isograma.")

    if es_isograma(palabra2):
        print(f"'{palabra2}' es un isograma.")
    else:
        print(f"'{palabra2}' no es un isograma.")

# Ejemplo de uso
palabra1 = "Anita lava la tina"
palabra2 = "Ala tita"
analizar_palabras(palabra1, palabra2)