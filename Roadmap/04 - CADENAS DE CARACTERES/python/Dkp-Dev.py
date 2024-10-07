"""
EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
"""

# Operaciones

x1 = "Perro"
x2 = "Conejo"
x3 = "tortuga nadando"

print(x1 + x2)      # Concatenacion (pegar dos o mas cadenas de texto)

print(x1 * 3)       # Repeticion

print(x1[4] + x1[3] + x1[2] + x1[1] + x1[0])    # Indexacion (indicar un solo caracter de la cadena)

print(len(x2))      # Longitud

print(x2[2:6])      # Slicing (porcionar la cadena de texto)
print(x2[2:])
print(x2[:4])

print("e" in x1)    # Busqueda (comprobar si el/los caracteres se encuentran en una cadena de texto)
print("jo" in x2)

print(x2.replace("o","a"))  # Remplazo

print(x2.split("e"))        # Division de una cadena que da como resultado una lista

print(x3.upper())   # Convertir a Mayusculas

print(x1.lower())   # Convertir a minusculas

print(x3.title())   # Primera letra a mayuscula de cada palabra

print(x3.capitalize())  # Primera letra a mayuscula de toda la cadena de texto

print(" Dkp Dev ")
print(" Dkp Dev ".strip())  # Elimincacion de espacios al comienzo y al final de la cadena

print(x3.startswith("Tor")) # Comprueba si la cadena inicia con los caracteres que se especifiquen
print(x3.startswith("tor"))

print(x3.find("ando"))  # Busqueda por posicion del caracter

print(x3.count("a"))    # Busqueda de ocurrencias (cuantas veces aparece el caracter)

print("{}, {} y {}".format(x1,x2,x3))   # Formateo de una cadena eligiendo donde insertare mis cadenas de texto

print(f"{x2}, {x1} y {x3}")     # Interpolacion

print(list(x1))         # Transforma una cadena en lista

l1 = [x1, x2, "y", x3]
print(" ".join(l1))     # Transforma una lista a cadena de texto

x4 = "357"          # Transformar una cadena numerica en un 'int'
x4 = int(x4)
print(x4)

x5 = "35.7"         # Transformar una cadena numerica en un 'float'
x5 = float(x5)
print(x5)

x1 = "Perro"            # Comprobaciones
x6 = "123123"
print(x1.isalpha())     # Si la cadena es alfabetica (solo contiene letras)
print(x6.isalpha())

print(x1.isnumeric())   # Si la cadena es numerica (solo contiene numeros)
print(x6.isnumeric())

print(x1.isalnum())     # Si la cadena es alfanumerica (contiene letras y/o numeros)
print(x6.isalnum())

"""
DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos (palabras que se leen igual aunque se posiciones en orden inverso como radar o salas)
 * - Anagramas (palabras que contiene las mismas letras pero en diferente orden)
 * - Isogramas (palabras que no tienen mas de una letra repetida)

"""

def check(cadena1: str,cadena2: str):

    # Palindromo
    print(f"Es {cadena1} un palindromo?: {cadena1 == cadena1[::-1]}")   # Mediante el slicing comprobamos si la cadena se lee igual en reversa
    print(f"Es {cadena2} un palindromo?: {cadena2 == cadena2[::-1]}")

    # Anagramas
    print(f"Es {cadena1} un anagrama de {cadena2}?: {sorted(cadena1) == sorted(cadena2)}")      # Se ordenan las cadenas y se comprueban los characteres

    # Isograma

    def isograma(cadena:str) -> bool:       # Funcion que recibe una cadena y arroja un booleano

        cadena_dict = dict()        # Primero un dict de la cadena
        for letras in cadena:
            cadena_dict[letras] = cadena_dict.get(letras, 0) + 1

        isograma = True
        valor = list(cadena_dict.values())      # Lista de values
        isograma_len = valor[0]
        for cadena_count in valor:              # Se cuentan los values
            if cadena_count != isograma_len:    # Se comprueban ambas listas
                isograma = False
                break

        return isograma

    print(f"Es {cadena1} un isograma? {isograma(cadena1)}")
    print(f"Es {cadena2} un isograma? {isograma(cadena2)}")


   

check("radar","quesoqueso")
check("amor","roma")