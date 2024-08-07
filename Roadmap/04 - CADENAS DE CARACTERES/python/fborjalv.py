# OPERACIONES CON CADENAS DE TEXTO EN PYTHON
# ACCESO A CARACTERES ESPECIFICOS 

cadena = "Esta es una cadena de ejemplo"
cadena_2 = "Soy la Cadena 2"

print(f"acceso a un caracter concreto: {cadena[10]}")
print(f"acceso a los primeros n caracteres: {cadena[:10]}")
print(f"acceso a los últimos n caracteres: {cadena[10:]}")
print(f"acceso a los caracteres de las posición n hasta la posición m: {cadena[10:15]}")

# LONGITUD

print(f"La longitud de la cadena es de {len(cadena)} caracteres")

# CONCATENACIÓN 

print(f"Contenando la cadena 1 y la cadena 2 = {cadena + ' ' + cadena_2}")

# REPETICIÓN

print(cadena_2 * 4)

# CONVERSIÓN A MAYÚSCULAS Y MINÚSCULAS, 

print(f"Convertimos todo a mayúsculas: {cadena.upper()}")
print(f"Convertimos todoo a minúsculas: {cadena.lower()} ")
print(f"Establecemos primera letra en mayúsculas: {cadena.capitalize()}")
print(f"Usamos la función titulo: {cadena.title()}")


# REEMPLAZO

print(f'Función de reemplazo: {cadena.replace("ejemplo", "ejercicio")}')

# DIVISIÓN

print(cadena.split("cadena")) # devuelve un array con los partes restantes 
print(cadena.strip())

# UNIÓN

cadena_3 = cadena.join(cadena_2)
print(f"cadena 3 es una unión de cadena y cadena_2: {cadena_3}")


# BUSQUEDA POSICIÓN
print(f"Busca dentro de una cadena: {cadena.find('ejemplo')}")

# CREA UN PROGRAMA QUE ANALICE DOS PALABRAS DIFERENTES Y REALIZE LAS COMPROBACIONES PARA DESCUBRIR SI SON: 

print(cadena_2.count("a"))


def word_analysis (word_1, word_2):

    # ANAGRAGAMA 
    print(f"¿Son anagramas las palabras {word_1} y {word_2}?: {sorted(word_1) == sorted(word_2)}")

    # Palíndromo
    print(f"¿Es palíndroma la palabra {word_1}? {word_1[::1] == word_1[::-1]}")
    print(f"¿Es palíndroma la palabra {word_2}? {word_2[::1] == word_2[::-1]}")

    # Isogramas
    def is_isogram (word):
        isograma = True
        for elemento in word: 
            if word.count(elemento) > 1: 
                isograma = False
                return isograma
            else: 
                pass
        isograma = True
        return isograma

    print(f"{word_1}  es un isograma?: {is_isogram(word_1)} " )
    print(f"{word_2}  es un isograma?:{is_isogram(word_2)} ")

#word_analysis("radar", "anilina")
#word_analysis("amor", "roma")
word_analysis("pythonpythonpythonpython","roma")
