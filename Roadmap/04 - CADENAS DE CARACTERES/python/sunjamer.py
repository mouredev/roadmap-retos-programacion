# cadenas de caracteres

# Operaciones con cadenas de caracteres

# crear cadena

mi_cadena = "una cadena de texto"
print(mi_cadena)

# longitud de una cadena

print(f"La cadena tiene una longitud de {len(mi_cadena)} caracteres")

# concaterar cadenas

mi_nombre = "Pedro"
mi_apellido = "Pérez"
mi_segundo_apellido = "Gracia"
espacio = " "

mi_nombre_completo = mi_nombre + espacio + mi_apellido + espacio + mi_segundo_apellido

print (mi_nombre_completo)

# repetición

print(mi_nombre * 3)

# indexación
print (mi_nombre[0])
print (mi_nombre[2])
print (mi_nombre[4])

# slicing (quedarse con una parte de la cadena)
print(mi_nombre[0:5])
print(mi_nombre[3:5])
print(mi_nombre[1:])
print(mi_nombre[:3])

# invertir string i slicing
mi_nombre = "Pamplona"
print ("reverse de Pamplona")
print(mi_nombre[::-1])
print(mi_nombre[4::-1])   # la cadena se invierte y se recorre de derecha a izq

# busqueda
print("p" in mi_nombre)
print("P" in mi_nombre)
print(mi_nombre.startswith("P"))
print(mi_apellido.endswith("z"))

# reemplazo
print(mi_nombre.replace("P", "X"))

# División
print(mi_nombre.split("d"))

print(mi_nombre_completo)
print (mi_nombre_completo.split(espacio))

# mayusculas, minusculas, letras mayusculas
print(mi_apellido.upper())
print(mi_apellido.lower())
print("pedro".capitalize())
print("pedro perez gracia".title())

# eliminar espacios al principio y al final
print(" esto es un texto con espacios ".strip())

# buscar al principio y al final
print(mi_nombre_completo.startswith("Pe"))
print(mi_nombre_completo.startswith("Dro"))
print(mi_nombre_completo.lower().find("z"))
print(mi_nombre_completo.lower().find("i"))

# buscar ocurrencias (cuantas veces se repite)
print(mi_nombre_completo.lower().count("p"))
print(mi_nombre_completo.lower().count("r"))
print(mi_nombre_completo.lower().count("e"))

# transformaciones numéricas
num1 = "12345"
num2 = "67890"
print(num1)
print(num2)
print (num1 + num2)
num1 = int(num1)
num2 = int(num2)
print(num1 + num2)

num3 = "666.66"
print(num3 + "cadena")
num3 = float(num3)
print(num3 + 9.99)

# comprobaciones varias
num4 = "abc012"
num5 = "abc"
num6 = "012"
print(num4.isalnum())
print(num5.isalpha())
print(num6.isnumeric())
print(num5.isnumeric())

"""
Extra
"""

# palindroms
palabra1 = "patata"
palabra2 = "remer"

print(f"La paraula {palabra2} és palindrom: {palabra2 == palabra2[::-1]}")
print(f"La paraula {palabra1} és palindrom: {palabra1 == palabra1[::-1]}")

# anagrama: 2 palabras tienen las mismas letras
palabra1 = "cosas"
palabra2 = "casus"

palabra1_ord = sorted(palabra1)
print(palabra1_ord)
palabra2_ord = sorted(palabra2)
print(palabra2_ord)
print(f"La palabra {palabra1} es anagrama de {palabra2}: {palabra1_ord == palabra2_ord}")

# isogramas   usamos set() para ver si alguna letra de la palabra se repite

palabra1 = "copla"
palabra2 = "camino"
palabra3 = "caramelo"

print (palabra1)
print (set(palabra1))
print (f"La palabra {palabra1} es isograma? {len(palabra1) == len(set(palabra1))} ")

print (palabra2)
print (set(palabra2))
print (f"La palabra {palabra2} es isograma? {len(palabra2) == len(set(palabra2))} ")

print (palabra3)
print (set(palabra3))
print (f"La palabra {palabra3} es isograma? {len(palabra3) == len(set(palabra3))} ")

# isogramas con listas

palabra1 = "primavera"
dicc_palabra = dict()
print (f" --> {dicc_palabra}")
for word in palabra1:
    print(word) 
    print(palabra1)
    dicc_palabra[word] = dicc_palabra.get(word,0) + 1
print(dicc_palabra)
Is_isograma = True
 
valores_palabra = list(dicc_palabra.values())   # necesito una lista con los values del diccionario
print(valores_palabra)

primer_valor_palabra = valores_palabra[0]  # me guardo cuantas veces se repite la primera letra
print(primer_valor_palabra)
for value_letra in valores_palabra:  # recorro la lista de cuantas veces se repite cada letra  y voy comparando con el primer valor
    if valores_palabra[value_letra] != primer_valor_palabra: # cuando encuentro un valor de repeticiones que es diferente al primero ya veo que no es isograma y salgo
        Is_isograma = False
        break

print(f"Es {palabra1} un isograma? {Is_isograma}")

# print(dicc_palabra)
# print(word)
# print(dicc_palabra[word])







# dicc_palabra1 = dict(palabra1[0])
