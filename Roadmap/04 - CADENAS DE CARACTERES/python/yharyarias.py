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

# Acceso a carácteres específicos

cadena = 'Reto cuatro'
print(cadena[0])
print(cadena[-1])

# Subacadenas

print(cadena[2:6])
print(cadena[:4])
print(cadena[5:])

# Longitud

print(len(cadena))

# Concatenación

cadena2 = ' de programación'
concatenar = cadena + cadena2
print(concatenar)

print(f'* {cadena}')

# Repetición
palabra_repetir = cadena * 2
print(palabra_repetir)

# Recorrido

for caracrer in cadena:
    print(caracrer)

# Conversión a mayúsculas y minúsculas

print(concatenar.upper())
print(concatenar.lower())

# Reemplazar

nueva_cadena = cadena.replace('Hola', 'Hi')

# División

sub_cadena = cadena.split(' ')
print(sub_cadena)

# Unión

sub_cadena = ['Hola', 'Hi']
cadena_nueva = ' '.join(sub_cadena)
print(cadena_nueva)

# Interpolación

nombre = 'Yhary'
edad = 28
print(f'Mi nombre es {nombre} y tengo {edad}')

# Verificación

print('cuatro' in cadena)

# DIFICULTAD EXTRA (opcional):


def palindromos(palabra: str) -> bool:
    '''
        Palabra o frase que son iguales leidas de izquierda a 
        derecha que de derecha a izquierda.
    '''
    return palabra == palabra[::-1]


def anagrama(palabra1: str, palabra2) -> bool:
    '''
        Cambio en el orden de las letras de una palabra o frase 
        que da lugar a otra palabra o frase distinta.
    '''
    return sorted(palabra1) == sorted(palabra2)

def isograma(palabra: str) -> bool:
    '''
        Es una palabra o frase en la que cada letra aparece el 
        mismo número de veces
    '''
    return len(palabra) == len(set(palabra))

def main():
    palabra1 = input('Ingresa la primera palabra\n')
    palabra2 = input('Ingresa la segunda palabra\n')

    palabra1 = palabra1.lower().replace(" ", "")
    palabra2 = palabra2.lower().replace(" ", "")

    if palindromos(palabra1):
        print(f'La palabra "{palabra1}" es palíndromo')
    else:
        print(f'La palabra "{palabra1}" no es palíndromo')
    
    if palindromos(palabra2):
        print(f'La palabra "{palabra2}" es palíndromo')
    else:
        print(f'La palabra "{palabra2}" no es palíndromo')
    
    if anagrama(palabra1, palabra2):
        print(f'Las palabra "{palabra1}" y "{palabra2}" crean un anagrama')
    else:
        print(f'Las palabra "{palabra1}" y "{palabra2}" no crean un anagrama')
    
    if isograma(palabra1):
        print(f'Las palabra "{palabra1}" es un isograma')
    else:
        print(f'Las palabra "{palabra1}" no es un isograma')

    if isograma(palabra2):
        print(f'Las palabra "{palabra2}" es un isograma')
    else:
        print(f'Las palabra "{palabra2}" no es un isograma')
    


if __name__ == '__main__':
    main()

