#OPERACIONES

s1 = "Hola"
s2 = "Python"

#Concatenacion
print(s1 + ", " + s2 + "!")

#Repetición
print(s1 * 3)

#Indexación
print(s1[1] + s1[3] + s2[4])

#Longitud
print(len(s1))

#Slicing (porción)
print(s2[2:4])
print(s2[2:])
print(s2[:2])

#Búsqueda
print("a" in s1)
print("on" in s1)

#Reemplazo
print(s1.replace("o","a"))

#División
print(s1.split("l"))

#Mayusculas y minúsculas
print(s1.upper())
print(s2.lower())
print("victor fer".title())
print("victor fer".capitalize())

#Eliminacion de espacios al principio y al final
print("   victor fer    ")
print("   victor fer    ".strip())

#Búsqueda al principio y al final
print(s1.startswith("Ho"))
print(s1.startswith("la"))
print(s1.endswith("Ho"))
print(s1.endswith("la"))

#Búsqueda de posición
print("qwerty victor fer asdf".find("victor"))
print("qwerty victor fer asdf".find("v"))

#Búsqueda de ocurrencia
print("qwerty victor fer asdf".lower().count("e"))

#Formateo
print("Saludos, {} lenguaje {}!".format(s1.lower(), s2))

#Interpolacion
print(f"Saludos, {s1.lower()} lenguaje {s2}!")

#Transformación de lista de caracteres
print(list("qwert asdf zxcv"))

#Transformación de lista en cadena
li = [s1, ", ", s2, "!"]
print("".join(li))

#Transformaciones numéricas
s4 = "12345.123"
s5 = float(s4)
print(s5)


#EJERCICIO EXTRA

def isPalindromo(palabra):
    i = 0
    cont = len(palabra) - 1
    for i in palabra:
        if i != palabra[cont]:
            return False
        cont -= 1
    return True
    

def isAnagrama(palabra1, palabra2):
    if sorted(palabra1) == sorted(palabra2):
        return True
    else:
        return False


def isIsograma(palabra):
    tmp = dict()
    for c in palabra:
        tmp[c] = tmp.get(c, 0) + 1

    values = list(tmp.values())
    isogram_len = values[0]
    for word_count in values:
        if word_count != isogram_len:
            return False

    return True


def comprobaciones(palabra1: str, palabra2: str):

    if isPalindromo(palabra1):
        print(f"Las palabras {palabra1} es palíndromo")

    if isPalindromo(palabra2):
        print(f"Las palabras {palabra2} es palíndromo")

    if isAnagrama(palabra1, palabra2):
        print(f"Las palabras {palabra1} y {palabra2} son anagramas")

    if isIsograma(palabra1):
        print(f"Las palabras {palabra1} es isogrma")

    if isIsograma(palabra2):
        print(f"Las palabras {palabra2} es isograma")

comprobaciones("amor", "roma")
comprobaciones("radar", "barco")