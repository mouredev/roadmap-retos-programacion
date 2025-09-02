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

# Concatenación
cadena1 = "Hola!"
cadena2 = " Mundo"
cadenaP = 'Hannah'


# Repetición
cadena4 = "Hola" * 3
print(cadena4)

# Acceso a caracteres específicos
print(cadena1[0])

# Subcadenas
print(cadena1[0:2])

# Longitud de la cadena
longitud = len(cadena1)
print(longitud)

# Concatenación
concatenacion = cadena1 + " " + cadena2
print(concatenacion)

#interpolación con f-strings
nombre = "Dimas"
saludo_f = f"{cadena1}, {nombre}"
print(saludo_f)

# Recorrido
for caracter in cadena1:
    print(caracter)

# Conversión a mayúsculas
print(cadena1.upper())

# Conversión a minúsculas
print(cadena1.lower())

# Reemplazo
reemplazada = cadena1.replace("o", "a")
print(reemplazada)

# División
dividida = cadena1.split(",")
print(dividida)

# Unión
unida = '-'.join(dividida)
print(unida)

# Verificación
inicio_con_hola = cadena1.startswith("Hola")
termina_con_exclamacion = cadena1.endswith("!")

print(f"Inicia con 'Hola': {inicio_con_hola}")
print(f"Termina con '!': {termina_con_exclamacion}")

def es_palindromo(cadena):
    print('un palíndromo es una palabra que se lee igual de izquierda a derecha que de derecha a izquierda\n')
    palabra1 = input('Ingrese una palabra: ')
    palindromo = palabra1.lower() == palabra1.lower()[::-1]
    if palindromo:
        print(f"Palabra {palabra1} es palíndromo\n\n")
    else:
        print(f"Palabra {palabra1} no es palíndromo\n\n")

def es_anagrama():
    print('un anagrama es una palabra que se forman con las letras de otra palabra\n')
    palabra1 = input('Ingrese una palabra1: ')
    palabra2 = input('Ingrese una palabra2: ')
    anagrama = sorted(palabra1.lower()) == sorted(palabra2.lower())
    if anagrama:
        print(f"Palabra {palabra1} y {palabra2} son anagramas\n\n")
    else:
        print(f"Palabra {palabra1} y {palabra2} no son anagramas\n\n")

def es_isograma():
    print('un isograma es una palabra que no tiene letras repetidas\n')
    palabra1 = input('Ingrese una palabra: ')
    isograma = len(set(palabra1)) == len(palabra1)
    if isograma:
        print(f"Palabra {palabra1} es un isograma\n\n")
    else:
        print(f"Palabra {palabra1} no es un isograma\n\n")

print('\n\n\n')

while True:
    print('1. Palíndromo')
    print('2. Anagrama')
    print('3. Isograma')
    print('4. Salir')
    opcion = int(input('Ingrese una opció: '))

    if opcion == 1:
        es_palindromo(cadena1)
    elif opcion == 2:
        es_anagrama()
    elif opcion == 3:
        es_isograma()
    elif opcion == 4:
        print('Adios\n')
        break
