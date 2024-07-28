# Autor: Héctor Adàn
# GitHub: https://github.com/hectorio23

'''
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
'''

def discover_type(value1, value2):
    # Se guarda una variable local la cual sera modificada
    # para posteriormente ser comparada con la segunda palabra.
    # Se puede observar que se ordena de manera contraria
    value_reverse = value1[::-1]

    if value_reverse == value2:
        return "\nLas palabras anteriormente insertadas forman en realidad un palíndromo\n\n"
    elif isograma(value1) and isograma(value2):
        return "\nAmbas palabras son isogramas\n\n"
    elif isograma(value1) or isograma(value2):
        return "\nUna de las palabras es un isograma\n\n"
    elif anagrama(value1, value2):
        return "\nEs un anagrama\n\n"

    return "\nLas palabras proporcionadas no cumplen con las condiciones para ser un palíndromo, isograma o anagrama\n"

def isograma(palabra):
    _tmp_ = ""
    for item in palabra:
        if item in _tmp_:
            return False
        _tmp_ += item
    return True

def anagrama(palabra1, palabra2):
    palabra1_sorted = sorted(palabra1)
    palabra2_sorted = sorted(palabra2)

    if len(palabra1) != len(palabra2) or palabra1_sorted != palabra2_sorted:
        return False
    return True

def main():
    # Las siguientes variables almacenan las palabras
    # insertadas por el usuario
    value1 = input("Inserta la primera palabra: ")
    value2 = input("Ahora inserta la segunda palabra: ")

    cadena1 = "Hola"
    cadena2 = "Mundo"

    # Modifican la variable original transformando sus caracteres en minúsculas
    value1 = value1.lower()
    value2 = value2.lower()

    # Se llama a la función discoverType, la cual devuelve una cadena dependiendo de
    # si las palabras ingresadas por el usuario forman parte de un palíndromo, anagrama o isograma.
    # Para lograr esto, se invocan otras funciones cuyo único propósito es verificar
    # si las palabras cumplen con las especificaciones dadas.
    print(discover_type(value1, value2))

    # Concatenación de dos cadenas
    concatenacion = cadena1 + " " + cadena2
    print(f"Concatenación: {concatenacion}")

    # Se elimina cualquier espacio de la cadena de caracteres
    cadena_prueba = concatenacion.replace(" ", "")
    print(f"Cadena sin espacios en blanco: {cadena_prueba}")

    # Obtención de la longitud de dos cadenas
    print(f"Longitud de la cadena 1: {len(cadena1)}")
    print(f"Longitud de la cadena 2: {len(cadena2)}")

    # Acceso a caracteres individuales
    print(f"Primer caracter de la cadena 1: {cadena1[0]}")
    print(f"Último caracter de la cadena 2: {cadena2[-1]}")

    # Comparación
    if cadena1 == cadena2:
        print("Las cadenas son iguales")
    else:
        print("Las cadenas son diferentes")

    # Subcadena
    subcadena = concatenacion[5:10]  # Extrae "Mundo"
    print(f"Subcadena: {subcadena}")

    # Búsqueda
    buscar = "Mundo"
    posicion = concatenacion.find(buscar)
    if posicion != -1:
        print(f"La cadena '{buscar}' fue encontrada en la posición {posicion}")
    else:
        print(f"La cadena '{buscar}' no fue encontrada")

    # Modificación
    concatenacion = concatenacion.replace("Mundo", "Universo")
    print(f"Después de reemplazar 'Mundo' por 'Universo': {concatenacion}")

if __name__ == "__main__":
    main()
