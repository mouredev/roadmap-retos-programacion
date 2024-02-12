#04 CADENAS DE CARACTERES

#Operaciones con cadenas de caracteres
texto = "¡Hola Mundo!"
print(texto) # ¡Hola Mundo!
print(type(texto)) # <class 'str'>

# Operador de suma y concatenación
texto1 = "¡Hola"
texto2 = "Mundo!"
saludo = texto1 + " " + texto2
print(saludo) # ¡Hola Mundo!

lista_texto = ['Python', 'saluda', 'con', '¡Hola', 'Mundo!']
separador = " "
mensaje = separador.join(lista_texto)
print(mensaje) # Python saluda con ¡Hola Mundo!

texto1 = "¡Hola"
texto2 = " Mundo!"
texto1 += texto2
print(texto1)

# Operador de multiplicación
texto  = "¡Hola!"
eco = texto * 3
print(eco) # ¡Hola! ¡Hola! ¡Hola!

# Operador len (longitud)
texto = "¡Hola Mundo!"
longitud = len(texto)
print(longitud) # 12

#Operdaores para subcadenas y caracteres epecíficos
texto = "¡Hola Mundo!"
print(texto[0:6:2]) # ¡oa

texto = "En el lenguaje de Python, el primer paso es siempre decir ¡Hola Mundo! y comenzar la magia."
subcadena = texto[58:70]
print(subcadena) # ¡Hola Mundo!

texto = "¡Hola Mundo!"
print(texto[0])  #¡
print(texto[-1]) #!

#Encontrar caracteres específicos
texto = "¡Hola mundo!"
print(texto.find("o")) # 2
print(texto.find("¡")) # 0
print(texto.rfind("o")) # 10
print(texto.index("mun")) # 6
#print(texto.index("x")) # ValueError: substring not found

#Conversión a mayúsculas y minúsculas
texto = "Python saluda con ¡Hola Mundo!"
print(texto.capitalize()) # Python saluda con ¡hola mundo!
print(texto.upper()) # PYTHON SALUDA CON ¡HOLA MUNDO!
print(texto.lower()) # python saluda con ¡hola mundo!

#Contar la repeticion de un caracter o una subcadena
texto = "¡Hola Mundo!"
print(texto.count("o")) # 2

#Division de un texto
texto = "Python saluda con ¡Hola Mundo!"
lista_del_texto = texto.split(" ")
print(lista_del_texto) # ['Python', 'saluda', 'con', '¡Hola', 'Mundo!']

#Reemplazo de una cadena o parte de una cadena
texto = "Python saluda con ¡Hola Mundo!"
texto = texto.replace("saluda con ¡Hola Mundo!", "es uno de los lenguajes más usados.")
print(texto) # Python es uno de los lenguajes más usados.

#Verificación
texto = "Python saluda con ¡Hola Mundo!"
print("saluda" in texto) #True
print(texto.startswith("Python")) # True
print(texto.endswith("do!")) # True
print(texto.isalpha())  # True

#Interpolacion de un string
lenguaje = "Python"
ranking = 3
anio = 2023

texto = f"{lenguaje} estuvo en el puesto {ranking} en el ranking de los lenguajes de programación durante {anio}." # con f-strings
print(texto)

texto = "{} estuvo en el puesto {} en el ranking de los lenguajes de programación durante {}.".format(lenguaje, ranking,anio) #con format()
print(texto)

texto = "%s estuvo en el puesto %d en el ranking de los lenguajes de programación durante %d." % (lenguaje, ranking, anio) # con formatting()
print(texto)

#Recorrido
texto = "¡Hola Mundo!"

# Recorrido utilizando un bucle for
for caracter in texto: #bucle for
    print(caracter)

for indice, caracter in enumerate(texto):  #con índices
    print(f"Índice: {indice}, Carácter: {caracter}")

#Otras
texto = "  ¡Hola Mundo!  "
print(texto.strip()) #elimina espacios en blanco start y end

texto = "abc"
print(texto.zfill(5)) #00abc agrega ceros adelante

texto = "calcuta"
mi_set = set(texto)
print(mi_set)

"""
Palíndromo: Un palíndromo es una palabra, frase, número u otra secuencia de caracteres que se lee igual hacia 
adelante que hacia atrás. Los palindromos pueden llegar a ser anagramas si se cumple la condicion.
Ejemplo: "reconocer", "anilina".

Anagrama: Un anagrama es una palabra o frase que resulta de la transposición de letras de otra palabra o frase. 
Es decir, que usa todas las letras originales exactamente una vez.
Ejemplo: "amor" y "roma" y "mora" y "ramo", "monja" y "jamon", "lamina" y "animal", "esponja" y "japones"

Isograma: Un isograma es una palabra o frase en la que no hay letras repetidas; cada letra aparece una sola vez.
Los isogramas pueden llegar a ser anagramas si se cumple la condicion.
Ejemplo: "murciélago".
"""

def comparacion_palabras(palabra_1, palabra_2):
    palabra_1_invertida = palabra_1[::-1].lower()
    palabra_2_invertida = palabra_2[::-1].lower()
    resultados = []

    if palabra_1 != palabra_2:
        if palabra_1_invertida == palabra_1:
            resultados.append(f"La palabra {palabra_1_invertida} es palíndromo.")

        if palabra_2_invertida == palabra_2:
            resultados.append(f"La palabra {palabra_2_invertida} es palíndromo.")

        if len(set(palabra_1)) == len(palabra_1):
            resultados.append(f"La palabra {palabra_1} es isograma.")

        if len(set(palabra_2)) == len(palabra_2):
            resultados.append(f"La palabra {palabra_2} es isograma.")

        if sorted(palabra_1) == sorted(palabra_2):
            resultados.append(f"Las palabras {palabra_1} y {palabra_2} son anagramas.")

        if len(resultados) == 0:
            resultados.append(f"Las palabras {palabra_1} y {palabra_2} no cumplen con ninguna condición.")
    else:
        print(f"Las palabras {palabra_1} y {palabra_2} son identicas.")

    return resultados

resultados = comparacion_palabras("murciélago", "anilina")

for resultado in resultados:
    print(resultado)
