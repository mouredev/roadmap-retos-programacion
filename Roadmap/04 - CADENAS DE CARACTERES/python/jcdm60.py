# #04 CADENAS DE CARACTERES
#### Dificultad: Media | Publicación: 22/01/24 | Corrección: 29/01/24

## Ejercicio


# EJERCICIO:
# Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
# en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
# - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
#   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
#
# DIFICULTAD EXTRA (opcional):
# Crea un programa que analice dos palabras diferentes y realice comprobaciones
# para descubrir si son:
# - Palíndromos
# - Anagramas
# - Isogramas
#

# Acceso a caracteres específicos
cadena = "Hola, mundo!"
primer_caracter = cadena[0]
ultimo_caracter = cadena[-1]

print(f"Primer caracter: {primer_caracter}")
print(f"Último caracter: {ultimo_caracter}")

# Subcadenas
subcadena = cadena[6:11]  # Extrae desde el índice 6 hasta el 10 (sin incluir el 11)
print(f"Subcadena: {subcadena}")

# Longitud de una cadena
longitud = len(cadena)
print(f"Longitud de la cadena: {longitud}")

# Concatenación
otra_cadena = " ¡Bienvenido!"
concatenada = cadena + otra_cadena
print(f"Concatenación: {concatenada}")

# Repetición
repetida = cadena * 3
print(f"Repetición: {repetida}")

# Recorrido de caracteres
for caracter in cadena:
    print(caracter, end=' ')

# Conversión a mayúsculas y minúsculas
mayusculas = cadena.upper()
minusculas = cadena.lower()
print(f"\nMayúsculas: {mayusculas}")
print(f"Minúsculas: {minusculas}")

# Reemplazo
reemplazada = cadena.replace("mundo", "Python")
print(f"Reemplazo: {reemplazada}")

# División
dividida = cadena.split(",")  # Divide la cadena en una lista usando la coma como separador
print(f"División: {dividida}")

# Unión
unida = '-'.join(dividida)  # Une los elementos de la lista con '-' como separador
print(f"Unión: {unida}")

# Interpolación de cadenas (formato de f-strings)
nombre = "Juan"
edad = 63
mensaje = f"Hola, me llamo {nombre} y tengo {edad} años."
print(mensaje)

# Verificación
inicio_con_hola = cadena.startswith("Hola")
termina_con_exclamacion = cadena.endswith("!")

print(f"Inicia con 'Hola': {inicio_con_hola}")
print(f"Termina con '!': {termina_con_exclamacion}")


# DIFICULTAD EXTRA
def es_palindromo(palabra):
    palabra = palabra.lower()
    return palabra == palabra[::-1]

def es_anagrama(palabra1, palabra2):
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    return sorted(palabra1) == sorted(palabra2)

def es_isograma(palabra):
    palabra = palabra.lower()
    return len(set(palabra)) == len(palabra)

def main():
    palabra_palindromo = input("Ingrese una palabra para verificar si es un palíndromo: ")
    if es_palindromo(palabra_palindromo):
        print(f"{palabra_palindromo} es un palíndromo.")
    else:
        print(f"{palabra_palindromo} no es un palíndromo.")

    palabra_anagrama1 = input("Ingrese la primera palabra para verificar si es un anagrama: ")
    palabra_anagrama2 = input("Ingrese la segunda palabra para verificar si es un anagrama: ")
    if es_anagrama(palabra_anagrama1, palabra_anagrama2):
        print(f"{palabra_anagrama1} y {palabra_anagrama2} son anagramas.")
    else:
        print(f"{palabra_anagrama1} y {palabra_anagrama2} no son anagramas.")

    palabra_isograma = input("Ingrese una palabra para verificar si es un isograma: ")
    if es_isograma(palabra_isograma):
        print(f"{palabra_isograma} es un isograma.")
    else:
        print(f"{palabra_isograma} no es un isograma.")

if __name__ == "__main__":
    main()

