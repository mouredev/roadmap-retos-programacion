"""
 EJERCICIO:
 Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...

 DIFICULTAD EXTRA (opcional):
 Crea un programa que analice dos palabras diferentes y realice comprobaciones
 para descubrir si son:
 - Palíndromos
 - Anagramas
 - Isogramas
"""
print("Con dir(cadena) podemos ver los atributos y métodos de una variable de clase 'str'.")
print(dir("Hola mundo"))
print(f"Clase de la cadena: 'Hola mundo'.__class__.__name__ = {'Hola mundo'.__class__.__name__}")
print(f"Largo de la cadena: 'Hola mundo'.__len__() = {'Hola mundo'.__len__()}")
print(f"Cambiar a minúscula: 'Hola mundo'.lower() = {'Hola mundo'.lower()} ")
print(f"Cambiar a mayúscula: 'Hola mundo'.lower() = {'Hola mundo'.upper()} ")
print(f"Inicio de palabras en mayúscula: 'Hola mundo'.title() = {'hola mundo'.title()}'")
print(f"Inicio de frase en mayúscula: 'hola mundo'.capitalize() = {'hola mundo'.capitalize()}'")
print(f"Dividir frase en palabras: 'Hola mundo'.split() = {'Hola mundo'.split()}")
print(f"Buscar un caracter en particular: 'Hola mundo'.index('n') = {'Hola mundo'.index('n')}")
print(f"Mostrar el caracter de la posición 7: 'Hola mundo'[7] = {'Hola mundo'[7]}")
print(f"Mostrar una subcadena: 'Hola mundo'[1:4] = {'Hola mundo'[1:4]}")
print(f"Mostrar desde el final de la cadena: 'Hola mundo'[3:0:-1] = {'Hola mundo'[3:0:-1]}")
print(f"Invertir el orden: 'Hola mundo'[1:4][::-1] = {'Hola mundo'[1:4][::-1]}")
print(f"Concatenar cadenas: ' '.join(['Hola mundo'[1:4][::-1], 'monde']) = {' '.join(['Hola mundo'[1:4][::-1], 'monde'])}")
print("Una cadena se comporta como una lista de caracteres: cantidad de consonantes => ", end="")
print(f"[x for x in 'Hola mundo' if x.lower() not in ' aeiou'].__len__() = {[x for x in 'Hola mundo' if x.lower() not in ' aeiou'].__len__()}")
print("Se puede formatear usando distintas cadenas y los métodos de ajuste:")
print("""    vertical = '\\u2502'
    up_left = '\\u250c'
    flat = '\\u2500'
    up_right = '\\u2510'
    down_left = '\\u2514'
    down_right = '\\u2518'
    under = "*"
    print(f'{up_left + flat * 25 + up_right}')
    print(f'{vertical.ljust(3, " ")}{"Saludito".center(20, " ")}{vertical.rjust(4, " ")}')
    mus = under * "Saludito".__len__()
    print(f'{vertical.ljust(3, " ")}{mus.center(20, " ")}{vertical.rjust(4, " ")}')
    for j, item in enumerate('Hola mundo'.split()):
        print(
            f'{vertical.ljust(3, " ")}{str(j).ljust(2, " ")}{item.ljust(20, " ")}{vertical.rjust(2, " ")}')
    print(f'{down_left + flat * 25 + down_right}')
""")
vertical = "\u2502"
up_left = "\u250c"
flat = "\u2500"
up_right = "\u2510"
down_left = "\u2514"
down_right = "\u2518"
under = "*"   # "\u23ba"
print(f'{up_left + flat * 25 + up_right}')
print(f'{vertical.ljust(3, " ")}{"Saludito".center(20, " ")}{vertical.rjust(4, " ")}')
mus = under * "Saludito".__len__()
print(f'{vertical.ljust(3, " ")}{mus.center(20, " ")}{vertical.rjust(4, " ")}')
for j, item in enumerate('Hola mundo'.split()):
    print(
        f'{vertical.ljust(3, " ")}{str(j).ljust(2, " ")}{item.ljust(20, " ")}{vertical.rjust(2, " ")}')
print(f'{down_left + flat * 25 + down_right}')

# Complejidad extra


def normalizar(cadena: str) -> str:
    """
    Suprime caracteres no alfanumericos <= hay librerías que hacen esto => va de ejemplo nomás
    """
    translate_chars = "".maketrans("áàéèíìóòúùüñÁÀÉÈÍÌÓÒÚÙÜÑ", "aaeeiioouuunAAEEIIOOUUUN")
    replace_chars = "_-.,;:'¿?¡!·@#"
    for i in replace_chars:
        cadena = cadena.replace(i, " ")
    normalizada = cadena.translate(translate_chars)
    return normalizada


def es_anagrama(cadena1: str, cadena2: str) -> bool:
    return sorted(normalizar(cadena1.lower()).replace(" ", "")) == sorted(normalizar(cadena2.lower()).replace(" ", ""))


def es_isograma(cadena1: str, cadena2: str) -> bool:
    normalizada1 = sorted(normalizar(cadena1.lower()).replace(" ", ""))
    normalizada2 = sorted(normalizar(cadena2.lower()).replace(" ", ""))
    for lista_de_letras in (normalizada1, normalizada2):
        if any(x for x in lista_de_letras if lista_de_letras.count(x) > 1):
            return False
    letras1 = set(normalizada1)
    letras2 = set(normalizada2)
    return not letras1.intersection(letras2)


def es_palindromo(cadena: str) -> bool:
    normalizada = normalizar(cadena).replace(" ", "").lower()
    return normalizada == normalizada[::-1]


def main():
    while True:
        resultado = "Las cadenas NO entran en ninguna categoría."
        cadena1 = input("Ingrese una palabra o frase (X para salir): ")
        if cadena1 == "X":
            break
        if not cadena1:
            continue
        cadena2 = input("Ingrese OTRA cadena o frase (Enter para ignorar: ")

        if es_palindromo(cadena1):
            resultado = f"La cadena {cadena1} es un palíndromo."
        if cadena2:
            if es_anagrama(cadena1, cadena2):
                resultado = f"Ambas cadenas son anagramas."
            else:
                if es_isograma(cadena1, cadena2):
                    resultado = f"Ambas cadenas son isogramas."

        print(resultado)


if __name__ == '__main__':
    main()
