"""
/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 */
"""

# Operaciones con strings
texto = "En python es muy fácil programar"
print(f"Texto original: {texto}\n")

"""Acceso a caracteres específicos"""
print(f"Primera letra: {texto[0]}")
print(f"Última letra: {texto[-1]}\n")

"""Subcadenas"""
subcadena_python = texto[3:9]
print(f"Subcadena '3:9': {subcadena_python}\n")

"""Longitud"""
longitud_texto = len(texto)
print(f"El texto mide: {longitud_texto} caracteres\n")

"""Concanetación"""
texto_concatenado = texto + " gracias a la comunidad"
print(f"Texto concatenado: {texto_concatenado}\n")

"""Repetición"""
texto_repetido = (texto + "\n") * 2
print(f"Texto repetido:\n{texto_repetido}")

"""Recorrido"""
letras = []
for letra in texto:
    letras.append(letra)
print(f"Recorrido: {letras}\n")

"""Conversión a mayúsculas y minúsculas"""
texto_mayus = texto.upper()
print(f"Texto en Mayúsculas: {texto_mayus}")
texto_minus = texto.lower()
print(f"Texto en Minúsculas: {texto_minus}\n")

"""Reemplazo"""
texto_reemplazado = texto.replace("python", "bash")
print(f"Texto Reemplazado: {texto_reemplazado}\n")

"""División"""
texto_dividido = texto.split()
print(f"Texto Dividido: {texto_dividido}\n")

"""Unión"""
texto_unido = "$".join(texto)
print(f"Texto Unido: {texto_unido}\n")

"""Interpolación"""
texto_interpolado = f"Y entonces el ordenador dijo: '{texto}'"
print(f"Texto Interpolado:\n{texto_interpolado}\n")

"""Verificación"""
es_str = "programar" in texto
print(f"Texto Verificado:\n¿Está 'programar' en texto?: {es_str}")


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
"""


def filtro(str_1: str, str_2: str):
    palindromo(str_1)
    palindromo(str_2)
    anagrama(str_1, str_2)
    isograma(str_1)
    isograma(str_2)


def palindromo(str_: str):
    letras = []
    ciclo = -1
    for let in str_:
        if let == str_[ciclo]:
            ciclo -= 1
        else:
            return print(f"{str_} NO es palíndromo")
    return print(f"{str_} es palíndromo")


def generar_dic(str_) -> dict[str:int]:
    list_str = {}
    for let in str_:
        if let not in list_str:
            list_str[let] = 1
        elif let in list_str:
            list_str[let] += 1
    return list_str


def anagrama(str_1: str, str_2: str):
    if len(str_1) == len(str_2):

        list_str_1: dict = generar_dic(str_1)
        list_str_2: dict = generar_dic(str_2)
        if list_str_1 == list_str_2:
            print(f"{str_1} y {str_2} son anagramas")
        else:
            print(f"{str_1} y {str_2} NO son anagramas")
    else:
        print(f"{str_1} y {str_2} NO son anagramas")


def isograma(str_: str):
    lista = generar_dic(str_)
    for value in lista.values():
        if value > 1:
            return print(f"{str_} No es un isograma")
    return print(f"{str_} es un isograma")


filtro("amar", "rama")
filtro("noon", "salsa")
