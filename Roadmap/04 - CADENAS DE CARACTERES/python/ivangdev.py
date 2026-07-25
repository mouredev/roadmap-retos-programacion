# ---------------- Cadenas de caracteres ---------------------
# Acesso a caracteres
texto = "Hola Ivan"
print(texto[0])
print(texto[-1])

# Subcadenas
print(texto[0:4])  # Desde el indice 0 hasta el 3
print(texto[5:])  # Desde el indice 5 hasta el final
print(texto[:4])  # Desde el inicio 0 hasta el 3
print(texto[::2])  # Uno si, uno no

# Longuitud
print(len(texto))

# Concatenacion
nombre = "Ivan"
apellido = "Guerrero"
print(nombre + " " + apellido)

# Repeticion
print("ivan" * 4)

# Recorrido
for letra in texto:
    print(letra)

# Mayuscula
print(texto.upper())
print(texto.lower())
print(texto.title())
print(texto.capitalize())

# Reemplazo
print(texto.replace("Ivan", "Mundo"))

# Division y union
print(texto.split(" "))  # Division
print("-".join(texto))  # Union

# Interpolacion
edad = 25
print(f"Me llamo {nombre} y tengo {edad}")  # f-string
print("Me llamo {} y tengo {}".format(nombre, edad))  # format

# Verificacion
print("123".isdigit())  # True -> solo numeros
print("abc".isalpha())  # True -> solo letras
print("abc123".isalnum())  # True -> solo letras y numeros
print("       ".isspace())  # True -> solo espacios
print("hola".startswith("ho"))  # True
print("Hola".endswith("la"))  # True

# Eliminar espacios
espacios = "          prueba            "
print(espacios.strip())  # 'prueba'
print(espacios.lstrip())  # 'prueba    '
print(espacios.rstrip())  # '      prueba'

# Buscar
print(texto.find("Ivan"))  # 5 -> posicion
print(texto.find("Raul"))  # -1 -> no encontrado
print("Mundo" in texto)  # False
print("Python" not in texto)  # True


#  * DIFICULTAD EXTRA (opcional):
#  * Crea un programa que analice dos palabras diferentes y realice comprobaciones
#  * para descubrir si son:
#  * - Palíndromos
#  * - Anagramas
#  * - Isogramas


def analizarPalabra(palabra1, palabra2):
    if palabra1 == palabra1[::-1]:
        print(f"{palabra1}: Es palindromo")
    else:
        print(f"{palabra1}: No es palindromo")

    if palabra2 == palabra2[::-1]:
        print(f"{palabra2}: Es palindromo")
    else:
        print(f"{palabra2}: No es palindromo")

    # palabra_1 = list(palabra1)
    # palabra_2 = list(palabra2)

    if len(palabra1) != len(palabra2):
        print("No son anagramas")

    anagrama = {}
    for letra in palabra1:
        if letra in anagrama:
            anagrama[letra] += 1
        else:
            anagrama[letra] = 1

    anagrama2 = {}
    for letra in palabra2:
        if letra in anagrama2:
            anagrama2[letra] += 1
        else:
            anagrama2[letra] = 1

    if anagrama == anagrama2:
        print(f"Las palabras {palabra1} y {palabra2}: son anagrama")
    else:
        print(f"Las palabras {palabra1} y {palabra2}: no son anagrama")

    cantidadLetras = {}
    for letra in palabra1:
        if letra in cantidadLetras:
            cantidadLetras[letra] += 1
        else:
            cantidadLetras[letra] = 1
    cantidad = list(cantidadLetras.values())

    cantidadLetras2 = {}
    for letra in palabra2:
        if letra in cantidadLetras2:
            cantidadLetras2[letra] += 1
        else:
            cantidadLetras2[letra] = 1
    cantidad2 = list(cantidadLetras2.values())

    if min(cantidad) == max(cantidad) and min(cantidad2) == max(cantidad2):
        print(
            f"Las palabras {palabra1} y {palabra2}: Es isograma {cantidad} {cantidad2}"
        )
    else:
        print(f"Las palabras {palabra1} y {palabra2}: no son isograma")


analizarPalabra("mama", "abab")
