# 04 CADENAS DE CARACTERES

"""
/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */
"""

String = "HOLA MUNDO"
String2 = "ESTO ES PYTHON"
# Acceso a un caracter
print("Acceso a un caracter:")
print(String[2])

# Subcadena
print("\nSubcadena:")
print(String[0:4])
print(String[-3:-1])

# Longitud
print("\nLongitud:")
print("Cantidad de caracteres en el string:", len(String))

# Concatenación
print("\nConcatenación:")
String3 = String + String2
print("Cadena concatenada:", String3)

# Repetición
print("\nRepetición:")
print(String3 * 2)

# Recorrido
print("\nRecorrido:")
for caracter in String3:
    print(caracter, end=".")

# Conversiones
print("\n\nConversiones:")

# Minúsculas
print("Minúsculas:", String3.lower())

# Mayúsculas
print("Mayúsculas:", String3.upper())

# Reemplazo
print("Reemplazo:", String3.replace("O", "0"))

# Separación
print("Separación:", String3.split(" "))

# Unión
print("Unión:", "".join(String3))

# Interpolación
print(f"\nInterpolación:\nEl texto original es: {String}, y ahora es {String3}")

# Verificación
print("\nVerificación:")
if "HOLA" in String3:
    print(f"HOLA está en: {String3}")

# Métodos extras
print("\nMétodos extras:")
print("Es alfabético:", String3.isalpha())
print("Capitalizado:", String3.capitalize())
print(String3.count("O"))


###DIFICULTAD EXTRA

def palidromo (texto):
    "el palidromo son las paralabras que se leen igual de al reverso"

    if texto != texto[::-1]: #le da vuelta al texto
        return "NO ES UN PALIDROMO "

    else:
        return f"{texto} es un palidromo"


def Anagramas(texto1 , texto2):
    "un anagrama son 2 palabras que contienen las misma letras"

    if len(texto1) != len(texto2):
        return "no es un anagrama"


    for caracter  in texto1 :
        if caracter not in texto2:
            return "no es un anagrama"

    return "si es un anagrama"


def Isogramas(texto : str):
    "un isograma es una palabra o frase donde no hay caracteres repetidos"

    textocopy=texto
    texto.split()
    texto = set(texto)
    texto = "".join(texto)

    if len(texto) != len(textocopy):
        return "no es un isograma"

    return "si es un isograma"


print(palidromo("reconocer"))
print(Anagramas("amor" , "romaa"))
print(Isogramas("maximo"))